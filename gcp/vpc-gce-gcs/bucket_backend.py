"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

def create_backend_bucket():
    # Create a GCP resource (Storage Bucket) with uniform access control, explicit name, and versioning
    bucket = storage.Bucket('somaz-state-resource',
                            name="somaz-state",  # This sets the exact name of the bucket
                            location="asia-northeast3",
                            uniform_bucket_level_access=True,  # Enable uniform bucket-level access
                            versioning=storage.BucketVersioningArgs(enabled=True))  # Enable bucket versioning
    
    # Export the DNS name of the bucket
    pulumi.export('bucket_name', bucket.url)
    return bucket  # Optionally return the bucket if needed for further operations
