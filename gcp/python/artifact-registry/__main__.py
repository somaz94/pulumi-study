# __main__.py

import pulumi
from artifact_registry import ArtifactRegistry

# Create the dev repositories
dev_repositories = ArtifactRegistry.create_dev_repositories()

# Create the prod repositories
prod_repositories = ArtifactRegistry.create_prod_repositories()

# Optionally, export any required outputs
pulumi.export("dev_repositories", dev_repositories)
pulumi.export("prod_repositories", prod_repositories)
