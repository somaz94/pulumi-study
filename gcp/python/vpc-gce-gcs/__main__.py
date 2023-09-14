# __main__.py
"""A Google Cloud Python Pulumi program"""

import pulumi
from compute_engine import ComputeEngine
from vpc import VPC

# Create VPC, Route, and Subnet
vpc, route, subnet = VPC.create()

# Create a Compute Engine instance
instance = ComputeEngine.create_instance(vpc, subnet)

# Optionally, export some useful outputs
pulumi.export('instance_name', instance.name)
pulumi.export('instance_external_ip', instance.network_interfaces[0].access_configs[0].nat_ip)
pulumi.export('vpc_name', vpc.name)
pulumi.export('subnet_name', subnet.name)
pulumi.export('route_name', route.name)

# # Create backend-bucket.py 
# import pulumi
# from pulumi_gcp import storage

# from bucket_backend import create_backend_bucket

# # Call the function
# create_backend_bucket()
