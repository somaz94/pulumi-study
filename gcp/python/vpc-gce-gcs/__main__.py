"""A Google Cloud Python Pulumi program"""

import pulumi
from vpc import create_vpc
from compute_engine import create_compute_engine

# Create VPC, IGW, and Subnet
vpc, igw, subnet = create_vpc()

# Create a Compute Engine instance
instance = create_compute_engine(vpc, subnet, igw)

# Optionally, export some useful outputs
pulumi.export('instance_name', instance.name)
pulumi.export('instance_external_ip', instance.network_interfaces[0].access_configs[0].nat_ip)
pulumi.export('vpc_name', vpc.name)
pulumi.export('subnet_name', subnet.name)
pulumi.export('igw_name', igw.name)

## Create backend-bucket.py 
# import pulumi
# from pulumi_gcp import storage

# from bucket_backend import create_backend_bucket

# # Call the function
# create_backend_bucket()

