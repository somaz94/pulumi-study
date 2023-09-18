# workload_identity_federation.py

from pulumi import Output, ResourceOptions
from pulumi_gcp import iam

class WorkloadIdentityFederation:
    def __init__(self, project, service_account_name):
        pool_id = "pool-github-action"
        
        self.pool = iam.WorkloadIdentityPool(
            pool_id,
            workload_identity_pool_id=pool_id,
            project=project,
            display_name="pool-github-action",
            description="pool for github-action",
        )

        provider_id = "provider-github-action"
        self.provider = iam.WorkloadIdentityPoolProvider(
            provider_id,
            workload_identity_pool_id=self.pool.workload_identity_pool_id,
            workload_identity_pool_provider_id=provider_id,
            display_name="provider-github-action",
            description="provider for github-action",
            attribute_mapping={
                "google.subject": "assertion.sub",
                "attribute.actor": "assertion.actor",
                "attribute.aud": "assertion.aud",
                "attribute.repository": "assertion.repository",
            },
            oidc=iam.WorkloadIdentityPoolProviderOidcArgs(
                allowed_audiences=[
                    "https://token.actions.githubusercontent.com",
                ],
                issuer_uri="https://token.actions.githubusercontent.com"
            )
        )

        # Expose the pool_id attribute
        self.pool_id = self.pool.workload_identity_pool_id

