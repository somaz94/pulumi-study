# mdb_bq_archive.py

import pulumi
from pulumi_gcp import storage
import os
import hashlib

class Archive:

    def __init__(self, bucket_resource):
        self.bucket_resource = bucket_resource

    def zip_and_upload(self):
        # Save the original working directory
        original_directory = os.getcwd()

        # Local archive creation
        os.chdir('./mongodb-to-bigquery')
        os.system('zip -r mongodb-to-bigquery.zip main.py requirements.txt')

        # Calculate file hashes to detect changes
        with open("main.py", "rb") as f:
            main_content_hash = hashlib.sha256(f.read()).hexdigest()

        with open("requirements.txt", "rb") as f:
            requirements_content_hash = hashlib.sha256(f.read()).hexdigest()

        # Restore the original working directory
        os.chdir(original_directory)

        # If the files change, the archive is re-uploaded
        archive = storage.BucketObject("mongodb_bigquery_cloudfunction_archive",
            name="source/mongodb-to-bigquery.zip",  # Specifying the 'source/' directory here
            bucket=self.bucket_resource.name,
            source=pulumi.FileAsset('./mongodb-to-bigquery/mongodb-to-bigquery.zip'),
            opts=pulumi.ResourceOptions(depends_on=[self.bucket_resource], custom_timeouts=pulumi.CustomTimeouts(create="5m"))
        )
        return archive


