# scheduler_manager.py

from pulumi_gcp import cloudscheduler
import pulumi
from config import REGION, SERVICE_ACCOUNT_EMAIL

class CloudSchedulerManager:

    def __init__(self, function_manager_mdb_bq, function_manager_bq_sheet):
        self.function_manager_mdb_bq = function_manager_mdb_bq
        self.function_manager_bq_sheet = function_manager_bq_sheet

    def create_mongodb_bigquery_scheduler(self):
        return cloudscheduler.Job("mongodb_bigquery_job",
            name="mongodb-bigquery-job",  # Set the name explicitly
            region=REGION,
            schedule="20 14 * * *",   # Daily at 14:20 PM
            http_target=cloudscheduler.JobHttpTargetArgs(
                http_method="POST",
                uri=self.function_manager_mdb_bq.function.https_trigger_url,
                oidc_token=cloudscheduler.JobHttpTargetOidcTokenArgs(
                    service_account_email=SERVICE_ACCOUNT_EMAIL
                )
            ),
            time_zone="Asia/Seoul",  # Set the timezone to Asia/Seoul
            opts=pulumi.ResourceOptions(depends_on=[self.function_manager_mdb_bq.function])
        )

    def create_bigquery_googlesheet_scheduler(self):
        return cloudscheduler.Job("bigquery_googlesheet_job",
            name="bigquery-googlesheet-job",  # Set the name explicitly                     
            region=REGION,
            schedule="30 14 * * *",  # Daily at 14:40 PM
            http_target=cloudscheduler.JobHttpTargetArgs(
                http_method="POST",
                uri=self.function_manager_bq_sheet.function.https_trigger_url,
                oidc_token=cloudscheduler.JobHttpTargetOidcTokenArgs(
                    service_account_email=SERVICE_ACCOUNT_EMAIL
                )
            ),
            time_zone="Asia/Seoul",  # Set the timezone to Asia/Seoul
            opts=pulumi.ResourceOptions(depends_on=[self.function_manager_bq_sheet.function])
        )



