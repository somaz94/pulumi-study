# __main__.py
"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi import Config  # Import Pulumi.<stack-name>.yaml config file
from vpc import create_vpc
from private_service_access import create_private_service_access

# Import Pulumi.<stack-name>.yaml config file
config = Config()
host_project_id = config.require("host_project")
service_project_ids = config.require_object("service_projects")
private_service_ip = config.get("private_service_ip")  
private_service_prefix = config.get_int("private_service_prefix") 


# Create VPC, IGW, and Subnet
vpc, igw, subnet_a, subnet_b = create_vpc()

# Create Shared VPC host project and attach service projects to the Shared VPC
shared_vpc_host_project = create_shared_vpc_host_project(host_project_id)
attached_service_projects = attach_service_projects_to_shared_vpc(host_project_id, service_project_ids)

# Create Private Service Access for the VPC
reserved_range, service_connection = create_private_service_access(vpc, private_service_ip, private_service_prefix)

# Export some useful outputs
pulumi.export('vpc_name', vpc.name)
pulumi.export('subnet_a_name', subnet_a.name)
pulumi.export('subnet_b_name', subnet_b.name)
pulumi.export('igw_name', igw.name)
pulumi.export('shared_vpc_host_project_id', shared_vpc_host_project.id)
# Assuming there can be multiple service projects, you can export their names as a list:
pulumi.export('attached_service_project_ids', [proj.id for proj in attached_service_projects])
pulumi.export('reserved_range_name', reserved_range.id)
pulumi.export('service_connection_name', service_connection.id)