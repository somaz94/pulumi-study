# __main__.py
import pulumi
from pulumi import Config
from sa import ServiceAccount
from workload_identity_federation import WorkloadIdentityFederation
from iam import IAMPermissions

# Pulumi Configuration
config = Config('gcp')
project = config.require('project')

# Create Service Account
service_account_name = "github-action"
service_account = ServiceAccount(service_account_name, project)

# Create Workload Identity Federation
workload_identity = WorkloadIdentityFederation(project)

# Wait for the service account and workload identity to be created before setting IAM permissions
service_account_email = service_account.account_id.apply(lambda id: f"{id}@{project}.iam.gserviceaccount.com")

iam_permissions = IAMPermissions(
    project=project, 
    workload_identity_pool_id=workload_identity.pool_id, 
    service_account_email=service_account_email
)

# Outputs (if needed)
pulumi.export('service_account_id', service_account.account_id)


