from pulumi_gcp import storage
from config import REGION

class Storage:

    def create_bucket(self):

        bucket_config = {
            "name": "mongodb-cloud-function-storage", # storage name
            "location": REGION,
            "labels": {
                "env": "test"  # Modify with your labels if needed
            },
            "uniform_bucket_level_access": True,
            "force_destroy": True
        }

        mongodb_cloud_function_bucket = storage.Bucket("mongodb_cloud_function_storage", **bucket_config) 

        return mongodb_cloud_function_bucket

