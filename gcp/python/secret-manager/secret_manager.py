# secret_manager.py
import pulumi
import pulumi_gcp as gcp
import json

class SecretManager:
    def __init__(self):
        # Fetch configuration values from the 'secret-manager' namespace
        secret_manager_config = pulumi.Config("secret-manager")
        self.dev_db_username = secret_manager_config.require_secret("dev_db_username")
        self.dev_db_password = secret_manager_config.require_secret("dev_db_password")
        self.dev_db_secret = secret_manager_config.require("dev_db_secret")

        # Fetch the project from the 'gcp' namespace
        gcp_config = pulumi.Config("gcp")
        self.project_id = gcp_config.require("project")

    def create_secret(self):
        # Create a Google Secret Manager Secret
        secret = gcp.secretmanager.Secret(self.dev_db_secret,
            project=self.project_id,
            labels={
                "environment": "dev",
                # Add any other labels you want here
            },
            replication=gcp.secretmanager.SecretReplicationArgs(automatic=True), 
            secret_id=self.dev_db_secret
        )

        # Using apply method to transform the Output values to JSON string
        secret_data = pulumi.Output.all(self.dev_db_username, self.dev_db_password).apply(
            lambda args: json.dumps({
                "username": args[0],
                "password": args[1]
            })
        )

        # Use apply method to create a SecretVersion using the actual secret_id from the secret
        secret_version = secret.id.apply(
            lambda secret_id: gcp.secretmanager.SecretVersion(f"{self.dev_db_secret}-version",
                secret=secret_id,
                secret_data=secret_data
            )
        )

        return secret, secret_version