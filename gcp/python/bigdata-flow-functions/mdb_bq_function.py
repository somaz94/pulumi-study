# mdb_bq_function.py

from pulumi_gcp import cloudfunctions
import pulumi
from config import REGION, SHARED_VPC, SUBNET_SHARE, SERVICE_ACCOUNT_EMAIL

class Function:

    def __init__(self, archive_bucket_name, archive_object_name):
        self.archive_bucket_name = archive_bucket_name
        self.archive_object_name = archive_object_name

    def create_function(self, depends_on_archive):
        self.function = cloudfunctions.Function(
            "mongodb_bigquery_dataflow_function",
            name="mongodb-to-bigquery-dataflow",
            region=REGION,
            description="Function to mongodb-to-bigquery the Dataflow job",
            runtime="python38",
            timeout=540,
            opts=pulumi.ResourceOptions(depends_on=[depends_on_archive]),
            available_memory_mb=512,
            source_archive_bucket=self.archive_bucket_name,
            source_archive_object=self.archive_object_name,
            trigger_http=True,
            entry_point="start_dataflow",
            service_account_email=SERVICE_ACCOUNT_EMAIL,
            environment_variables={
                "PROJECT_ID": pulumi.Config("gcp").get("project"),
                "REGION": REGION,
                "SHARED_VPC": SHARED_VPC,
                "SUBNET_SHARE": SUBNET_SHARE,
                "SERVICE_ACCOUNT_EMAIL": SERVICE_ACCOUNT_EMAIL
            }
        )

