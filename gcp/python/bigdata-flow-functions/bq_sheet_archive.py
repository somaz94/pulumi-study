# bq_sheet_archive.py

import pulumi
from pulumi_gcp import storage
import os
import hashlib

class Archive:

    def __init__(self, bucket_resource):
        self.bucket_resource = bucket_resource

    def zip_and_upload(self):
        # Define the base path for 'bigquery-to-google-sheet' directory
        base_path = os.path.join(os.getcwd(), 'bigquery-to-google-sheet')

        # Local archive creation using relative paths
        zip_command = f'zip -r {os.path.join(base_path, "bigquery-to-google-sheet.zip")} -j {os.path.join(base_path, "main.py")} {os.path.join(base_path, "requirements.txt")} {os.path.join(base_path, "bigquery.json")}'
        os.system(zip_command)

        # Calculate file hashes using absolute paths
        with open(os.path.join(base_path, "main.py"), "rb") as f:
            main_content_hash = hashlib.sha256(f.read()).hexdigest()

        with open(os.path.join(base_path, "requirements.txt"), "rb") as f:
            requirements_content_hash = hashlib.sha256(f.read()).hexdigest()

        # If the files change, the archive is re-uploaded
        archive = storage.BucketObject("bigquery_googlesheet_cloudfunction_archive",
            name="source/bigquery-to-google-sheet.zip",
            bucket=self.bucket_resource.name,
            source=pulumi.FileAsset(os.path.join(base_path, 'bigquery-to-google-sheet.zip')),
            opts=pulumi.ResourceOptions(depends_on=[self.bucket_resource], custom_timeouts=pulumi.CustomTimeouts(create="5m"))
        )
        return archive



