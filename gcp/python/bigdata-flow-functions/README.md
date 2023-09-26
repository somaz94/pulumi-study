# Bigdata-Flow-Functions

This repository contains various scripts and functions to facilitate data flow between BigData platforms and tools such as MongoDB, BigQuery, and Google Sheets on Google Cloud Platform (GCP).

<br/>

## Directory Structure

- `bigquery-to-google-sheet/`: Contains scripts and tools for transferring data from BigQuery to Google Sheets.
- `mongodb-to-bigquery/`: Contains scripts and tools for transferring data from MongoDB to BigQuery.
- `scheduler_manager.py`: Scheduling manager script.
- `storage.py`: Utilities and functions related to cloud storage.
- `bq_dataset.py`: BigQuery dataset utilities.
- `bq_sheet_function.py`: Functions for BigQuery to Sheets operations.
- `bq_sheet_archive.py`: Archiving functionalities for BigQuery to Sheets data.
- `mdb_bq_function.py`: Functions for MongoDB to BigQuery operations.
- `mdb_bq_archive.py`: Archiving functionalities for MongoDB to BigQuery data.
- `utils.py`: General utility functions.
- `config.py`: Configuration file for defining constants and parameters.
- `requirements.txt`: Contains a list of necessary Python packages.
- `__main__.py`: Main entry point for the project.

<br/>

## Setup

1. Install Python 3.x.
2. Clone the repository:
    ```bash
    git clone <repository-url>
    cd bigdata-flow-functions
    ```

3. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Update the `config.py` with necessary parameters.

<br/>

## Usage

To start using the functions, refer to the `__main__.py` as the main entry point.

For detailed information and specific instructions about the `bigquery-to-google-sheet` and `mongodb-to-bigquery` directories, please check the comments in the `main.py` files inside each respective directory.

<br/>

## Contribution

Feel free to contribute by submitting pull requests. Ensure that your code is well-commented and adheres to the project's coding standards.

<br/>

## License

[MIT](LICENSE)

