# __main__.py

import pulumi
from cloud_run_domain import CloudRunDeployment
from config import IMAGE_NAME, DOMAIN_NAME

cloud_run_deploy = CloudRunDeployment(IMAGE_NAME)
service = cloud_run_deploy.deploy()
domain = cloud_run_deploy.domain_mapping(DOMAIN_NAME)

# Add the call to create the CNAME record
cloud_run_deploy.create_dns_cname(DOMAIN_NAME, service)

pulumi.export("serviceUrl", service.statuses[0].url)
pulumi.export('domainUrl', domain)
