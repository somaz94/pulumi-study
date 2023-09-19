# cloud_run.py
from pulumi import Config
from pulumi_gcp import cloudrun
from utils import Utils
from config import REGION

config = Config("gcp")
project = config.require("project")

class CloudRunDeployment:
    def __init__(self, image_name: str):
        self.image_name = image_name

    def deploy(self):
        self.service = cloudrun.Service(
            Utils.resource_name("supermario-service"),
            name = Utils.resource_name("supermario-service"),
            location=REGION,
            template={
                "spec": {
                    "containers": [{
                        "image": self.image_name,
                    }],
                },
            },
            traffics=[
                {
                    "percent": 100,
                    "latest_revision": True,
                },
            ],
        )

        cloudrun.IamMember(
            "supermario-invoker",
            service=self.service.name,
            location=REGION,
            role="roles/run.invoker",
            member="allUsers",
        )
        
        return self.service

    def domain_mapping(self, domain_name: str):
        return cloudrun.DomainMapping(
            Utils.resource_name("supermario-domain-mapping"),
            location=REGION,
            metadata={
                "namespace": project,  # Change this to your GCP project ID
            },
            spec={
                "route_name": self.service.name,
            },
        )

