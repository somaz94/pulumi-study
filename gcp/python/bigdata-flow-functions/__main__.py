# __main__.py

import pulumi
from bq_dataset import Dataset
from storage import Storage
from mdb_bq_archive import Archive as MdbBqArchive
from mdb_bq_function import Function as MdbBqFunction
from bq_sheet_archive import Archive as BqSheetArchive
from bq_sheet_function import Function as BqSheetFunction
from scheduler_manager import CloudSchedulerManager  

# Initialize BigQueryDataset and CloudStorage managers
bq_dataset_manager = Dataset()
storage_manager = Storage()

# Create Cloud Storage Bucket
mongodb_bucket = storage_manager.create_bucket()

# Initialize MdbBqArchive manager with the created bucket
archive_manager = MdbBqArchive(mongodb_bucket)

# Create BigQuery Dataset and Archive Workflow
mongodb_dataset = bq_dataset_manager.create_dataset()
mongodb_archive = archive_manager.zip_and_upload()

# Create the Cloud Function for MongoDB to BigQuery
dataflow_function_manager = MdbBqFunction(mongodb_bucket.name, mongodb_archive.name)
dataflow_function_manager.create_function(mongodb_archive)

# Initialize BqSheetArchive manager with the created bucket
googlesheet_archive_manager = BqSheetArchive(mongodb_bucket)

# Create BigQuery-to-GoogleSheet Archive Workflow
bigquery_googlesheet_archive = googlesheet_archive_manager.zip_and_upload()

# Create the BigQuery-to-GoogleSheet Cloud Function
googlesheet_function_manager = BqSheetFunction(mongodb_bucket.name, bigquery_googlesheet_archive.name)
googlesheet_function_manager.create_function(bigquery_googlesheet_archive)

# Initialize Cloud Scheduler managers with Cloud Functions
scheduler_manager = CloudSchedulerManager(dataflow_function_manager, googlesheet_function_manager)

# Create Cloud Schedulers for the Cloud Functions
mongodb_bigquery_scheduler = scheduler_manager.create_mongodb_bigquery_scheduler()
bigquery_googlesheet_scheduler = scheduler_manager.create_bigquery_googlesheet_scheduler()

# Output results
pulumi.export("mongodb_dataset_id", mongodb_dataset.dataset_id)
pulumi.export("mongodb_bucket_name", mongodb_bucket.name)
pulumi.export("mongodb_archive_url", mongodb_archive.self_link)
pulumi.export('function_url', dataflow_function_manager.function.https_trigger_url)
pulumi.export("bigquery_to_sheets_function_url", googlesheet_function_manager.function.https_trigger_url)

# Exporting Cloud Scheduler job names
pulumi.export("mongodb_bigquery_scheduler_name", mongodb_bigquery_scheduler.name)
pulumi.export("bigquery_googlesheet_scheduler_name", bigquery_googlesheet_scheduler.name)
