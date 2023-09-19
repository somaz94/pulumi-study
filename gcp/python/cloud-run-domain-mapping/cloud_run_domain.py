## cloud_run_domain.py
import pulumi
from pulumi import Config
from pulumi_gcp import cloudrun, dns
from utils import Utils
from config import DOMAIN_REGION, MANAGED_ZONE, DOMAIN_PROJECT

config = Config("gcp")
project = config.require("project")

class CloudRunDeployment:
    def __init__(self, image_name: str):
        self.image_name = image_name

    def deploy(self):
        self.service = cloudrun.Service(
            Utils.resource_name("supermario-service"),
            name = Utils.resource_name("supermario-service"),
            location=DOMAIN_REGION,
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
            location=DOMAIN_REGION,
            role="roles/run.invoker",
            member="allUsers",
        )
        
        # Derive the URL based on the service name and region
        return self.service

    def domain_mapping(self, domain_name: str):
        cloudrun.DomainMapping(
            Utils.resource_name("supermario-domain-mapping"),
            location=DOMAIN_REGION,
            metadata={
                "namespace": project,
            },
            name=domain_name,
            spec={
                "route_name": self.service.name,
            },
            opts=pulumi.ResourceOptions(depends_on=[self.service])
        )
        
        # For the sake of simplicity, just returning the domain name you provided 
        return domain_name

    def create_dns_cname(self, domain_name: str, service: cloudrun.Service):
        # Ensure domain_name ends with a trailing dot.
        if not domain_name.endswith('.'):
            domain_name += '.'
        
        # Get the default Cloud Run CNAME target.
        default_cname_target = "ghs.googlehosted.com."
        
        # Create the CNAME record.
        record_set = dns.RecordSet(
            "cnameRecord",
            name=domain_name,
            type="CNAME",
            ttl=60,
            rrdatas=[default_cname_target],
            managed_zone=MANAGED_ZONE,
            project=DOMAIN_PROJECT,
            opts=pulumi.ResourceOptions(depends_on=[self.service])
        )
        
        return record_set.name




