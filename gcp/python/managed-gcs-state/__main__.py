"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket) with uniform access control, explicit name, and versioning
bucket = storage.Bucket('somaz-bucket-resource',
                        name="somaz-bucket",  # This sets the exact name of the bucket
                        location="asia-northeast3",
                        uniform_bucket_level_access=True,  # Enable uniform bucket-level access
                        versioning=storage.BucketVersioningArgs(enabled=True))  # Enable bucket versioning

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
