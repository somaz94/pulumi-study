"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket) with uniform access control and explicit name
bucket = storage.Bucket('somaz-test-resource',
                        name="somaz-test",  # This sets the exact name of the bucket
                        location="asia-northeast3",
                        website=storage.BucketWebsiteArgs(main_page_suffix="index.html"),
                        uniform_bucket_level_access=True)  # Enable uniform bucket-level access

# In __main__.py, create a new bucket object by adding the following right after creating the bucket itself
bucket_object = storage.BucketObject(
    "index.html", bucket=bucket.name, source=pulumi.FileAsset("index.html")
)

# Below the BucketObject, add an IAM binding allowing the contents of the bucket to be viewed anonymously over the Internet
bucket_iam_binding = storage.BucketIAMBinding(
    "somaz-test-binding",
    bucket=bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"],
)

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)

pulumi.export(
    "bucket_endpoint",
    pulumi.Output.concat(
        "http://storage.googleapis.com/", bucket.id, "/", bucket_object.name
    ),
)
