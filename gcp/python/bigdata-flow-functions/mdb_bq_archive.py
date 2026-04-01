# mdb_bq_archive.py

import pulumi
from pulumi_gcp import storage
import os
import hashlib
import zipfile


class Archive:

    def __init__(self, bucket_resource):
        self.bucket_resource = bucket_resource

    def zip_and_upload(self):
        source_dir = os.path.join(os.getcwd(), 'mongodb-to-bigquery')
        zip_path = os.path.join(source_dir, 'mongodb-to-bigquery.zip')

        # Create zip archive using zipfile module
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for filename in ['main.py', 'requirements.txt']:
                filepath = os.path.join(source_dir, filename)
                zf.write(filepath, filename)

        # Calculate file hashes to detect changes
        with open(os.path.join(source_dir, "main.py"), "rb") as f:
            main_content_hash = hashlib.sha256(f.read()).hexdigest()

        with open(os.path.join(source_dir, "requirements.txt"), "rb") as f:
            requirements_content_hash = hashlib.sha256(f.read()).hexdigest()

        # If the files change, the archive is re-uploaded
        archive = storage.BucketObject("mongodb_bigquery_cloudfunction_archive",
            name="source/mongodb-to-bigquery.zip",
            bucket=self.bucket_resource.name,
            source=pulumi.FileAsset(zip_path),
            opts=pulumi.ResourceOptions(depends_on=[self.bucket_resource], custom_timeouts=pulumi.CustomTimeouts(create="5m"))
        )
        return archive
