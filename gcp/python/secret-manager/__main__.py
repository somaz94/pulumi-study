"""A Google Cloud Python Pulumi program"""

import pulumi
from secret_manager import create_secret

# Deploy the resources
my_secret, my_secret_version = create_secret()

# Export relevant information for easy access
pulumi.export("secret_id", my_secret.secret_id)
pulumi.export("secret_version_name", my_secret_version.name)

