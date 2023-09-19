# cloud_run.py
from pulumi_gcp import cloudrun
from utils import Utils
from config import REGION

class CloudRunDeployment:
    def __init__(self, image_name: str):
        self.image_name = image_name

    def deploy(self):
        service = cloudrun.Service(
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
            service=service.name,
            location=REGION,
            role="roles/run.invoker",
            member="allUsers",
        )

        return service