# main.py
import pulumi
from secret_manager import SecretManager

# Initialize SecretManager class
sm = SecretManager()

# Deploy the resources
my_secret, my_secret_version = sm.create_secret()

# Export relevant information for easy access
pulumi.export("secret_id", my_secret.secret_id)
pulumi.export("secret_version_name", my_secret_version.name)