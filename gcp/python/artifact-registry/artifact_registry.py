# artifact_registry.py

import pulumi
from pulumi_gcp.artifactregistry import Repository
from config import REGION, dev_repo, prod_repo
from utils import Utils

class ArtifactRegistry:

    @staticmethod
    def create_repositories(repo_list: list, prefix: str):
        repositories = {}
        for repo in repo_list:
            repo_name = Utils.resource_name(f"{prefix}-{repo}")
            repositories[repo_name] = Repository(repo_name,
                                                 location=REGION,
                                                 format="DOCKER",
                                                 repository_id=repo_name,
                                                 labels={
                                                     "createdby": "pulumi",
                                                 })
        return repositories

    @staticmethod
    def create_dev_repositories():
        return ArtifactRegistry.create_repositories(dev_repo, "dev")

    @staticmethod
    def create_prod_repositories():
        return ArtifactRegistry.create_repositories(prod_repo, "prod")

