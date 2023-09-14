from pulumi_gcp import storage
from utils import Utils
import pulumi

class Storage:

    @staticmethod
    def create_bucket(dependencies=[]):
        return storage.Bucket(Utils.resource_name('bucket'),
            name='web.gcp.somaz.link',
            location='ASIA-NORTHEAST3',
            uniform_bucket_level_access=True,  # Enable uniform bucket-level access
            # versioning=storage.BucketVersioningArgs(enabled=True),  # Enable bucket versioning
            force_destroy=True,  # Force destroy
            website=storage.BucketWebsiteArgs(   # Add these lines
                main_page_suffix="index.html",
                not_found_page="404.html"       # Optional: if you have a custom 404 page
            ),         
            opts=pulumi.ResourceOptions(depends_on=dependencies)
        )

    @staticmethod
    def set_bucket_public_access(bucket):
        """
        Grants the allUsers entity the ObjectViewer role for the bucket
        """
        return storage.BucketIAMBinding(
            Utils.resource_name('bucket-public-access'),
            bucket=bucket.name,
            role="roles/storage.objectViewer",
            members=["allUsers"]
        )
        
    @staticmethod
    def upload_static_website(bucket):
        return storage.BucketObject(Utils.resource_name('index-object'),
            name='index.html',
            bucket=bucket.name,
            source=pulumi.FileAsset('index.html'),
            content_type='text/html',
        )
