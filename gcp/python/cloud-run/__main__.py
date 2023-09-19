# __main__.py

from cloud_run import CloudRunDeployment
import pulumi

image_name = "pengbai/docker-supermario:latest"
deployment = CloudRunDeployment(image_name)
service = deployment.deploy()

pulumi.export("serviceUrl", service.statuses[0].url)