# __main__.py
from cloud_run import CloudRunDeployment
import pulumi

image_name = "pengbai/docker-supermario:latest"
deployment = CloudRunDeployment(image_name)
service = deployment.deploy()

domain_name = "mario.somaz.link"  # 이것을 원하는 도메인으로 변경하세요.
domain_mapping = deployment.domain_mapping(domain_name)

pulumi.export("serviceUrl", service.statuses[0].url)
pulumi.export("resourceRecords", domain_mapping.statuses[0].resource_records)