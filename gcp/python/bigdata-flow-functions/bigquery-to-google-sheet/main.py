import os
import gspread
import datetime
from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials
import logging
import pytz  # Import the pytz library for timezone handling

MAX_ROWS_PER_BATCH = 1000  # Define the maximum number of rows to process at once.

def bigquery_to_sheets(request, desired_date="2023-06"): # Modify Date(ex.2023-06, 2023-07 ....)
    try:
        logging.info("Starting bigquery_to_sheets function")

        # BigQuery setup
        client = bigquery.Client()
        dataset_id = os.environ.get('BIGQUERY_DATASET', 'somaz.mongodb_dataset') # <project>.<dataset_name>
        
        # Get list of tables in the dataset
        tables = list(client.list_tables(dataset_id))
        
        if not tables:
            logging.warning("No tables found in the dataset.")
            return "No tables found in the dataset.", 400

        # Connect to Google Sheets
        scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('bigquery.json', scopes)    # bigquery and cloud function and cloud scheduler and dataflow admin service account json file   
        gc = gspread.authorize(creds)
        logging.info("Connected to Google Sheets")

        # Open Google Sheets document
        sh = gc.open_by_key('1xxxxxxxxxxxxxxxXvB_M...')     # Google Sheet ID

        for table in tables:
            table_id = table.table_id
            database_name = table_id.split('-')[0]

            # Date filter preparation
            if "-" in desired_date and len(desired_date.split("-")) == 2:
                # Fetch the entire month's data
                date_filter = f"FORMAT_DATE('%Y-%m', DATE(PARSE_TIMESTAMP('%a %b %d %H:%M:%S UTC %Y', time))) = '{desired_date}'"
            else:
                # Fetch data for that specific date
                date_filter = f"DATE(PARSE_TIMESTAMP('%a %b %d %H:%M:%S UTC %Y', time)) = '{desired_date}'"

            # Filter for the 'reason' column
            reason_filter = "(reason = '/login' OR reason = '/login/unity')"

            # Combine date and reason filters
            combined_filter = f"{date_filter} AND {reason_filter}"

            # Calculate the total number of rows in the table for the desired date and reason
            total_rows_query = f"SELECT COUNT(*) FROM `{dataset_id}.{table_id}` WHERE {combined_filter}"
            total_rows = client.query(total_rows_query).result().to_dataframe().iloc[0, 0]

            # Calculate the number of batches
            num_batches = -(-total_rows // MAX_ROWS_PER_BATCH)  # Ceiling division

            # Check if worksheet exists, if not create one
            try:
                worksheet = sh.worksheet(database_name)
                worksheet.clear()  # Clear data if sheet already exists
            except gspread.exceptions.WorksheetNotFound:
                worksheet = sh.add_worksheet(title=database_name, rows=str(total_rows+1), cols="20")

            # Add schema (column names) to the first row
            schema = [field.name for field in client.get_table(f"{dataset_id}.{table_id}").schema]
            worksheet.append_row(schema)

            for batch_num in range(num_batches):
                offset = batch_num * MAX_ROWS_PER_BATCH
                query = f"SELECT * FROM `{dataset_id}.{table_id}` WHERE {combined_filter} LIMIT {MAX_ROWS_PER_BATCH} OFFSET {offset}"
                rows = client.query(query).result()

                batch_data = []
                for row in rows:
                    row_data = []
                    for item in row.values():
                        if isinstance(item, datetime.datetime):
                            # Convert timestamp to 'Asia/Seoul' timezone
                            seoul_timezone = pytz.timezone('Asia/Seoul')
                            localized_timestamp = item.replace(tzinfo=pytz.utc).astimezone(seoul_timezone)
                            formatted_timestamp = localized_timestamp.strftime('%Y-%m-%d %H:%M:%S')
                            row_data.append(formatted_timestamp)
                        else:
                            row_data.append(item)
                    batch_data.append(row_data)

                # Use batch update for better performance
                worksheet.append_rows(batch_data)

        logging.info("Data synced to Google Sheets!")
        return "Data synced to Google Sheets!", 200

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise e
