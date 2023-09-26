# bq_sheet_function.py

from pulumi_gcp import cloudfunctions
import pulumi
from config import REGION, SERVICE_ACCOUNT_EMAIL

class Function:

    def __init__(self, archive_bucket_name, archive_object_name):
        self.archive_bucket_name = archive_bucket_name
        self.archive_object_name = archive_object_name

    def create_function(self, depends_on_archive):
        self.function = cloudfunctions.Function(
            "bigquery_googlesheet_function",
            name="bigquery-to-googlesheet",
            region=REGION,
            description="Sync data from BigQuery to Google Sheets",
            runtime="python38",
            timeout=540,
            opts=pulumi.ResourceOptions(depends_on=[depends_on_archive]),
            available_memory_mb=1024,
            source_archive_bucket=self.archive_bucket_name,
            source_archive_object=self.archive_object_name,
            trigger_http=True,
            entry_point="bigquery_to_sheets",
            service_account_email=SERVICE_ACCOUNT_EMAIL,
            environment_variables={
                "BIGQUERY_TABLE": f"{pulumi.Config('gcp').get('project')}.mongodb_dataset.mongodb-internal-table",
                "SHEET_ID": "115whxBxRBtWAb3a8jS5S3NN1wFMWRUBj5oqYFaXvB_M"
            }
        )



