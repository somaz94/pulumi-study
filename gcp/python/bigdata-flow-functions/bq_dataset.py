# bq_dataset.py

from pulumi_gcp import bigquery
from config import REGION, SERVICE_ACCOUNT_EMAIL

class Dataset:

    def create_dataset(self):

        # Set dataset access controls
        owner_access = bigquery.DatasetAccessArgs(
            role="OWNER",
            user_by_email=SERVICE_ACCOUNT_EMAIL
        )

        additional_owner_access = bigquery.DatasetAccessArgs(
            role="OWNER",
            user_by_email=""     # ADD Service Account Email
        )

        # Create BigQuery dataset with access controls
        dataset_config = {
            "dataset_id": "mongodb_dataset",
            "friendly_name": "mongodb_dataset",
            "description": "This is a test description",
            "location": REGION,
            "labels": {
                "env": "test"  # Modify with your labels if needed
            },
            "accesses": [owner_access, additional_owner_access]
        }

        mongodb_dataset = bigquery.Dataset("mongodb_dataset", **dataset_config)

        return mongodb_dataset

