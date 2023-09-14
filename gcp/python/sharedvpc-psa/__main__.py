# __main__.py
"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi import Config
from vpc import VPCManager, SharedVPCManager
from private_service_access import PrivateServiceAccess

class CloudInfrastructure:
    def __init__(self):
        self.gcp_config = Config("gcp")
        self.project_id = self.gcp_config.require("project")

        self.sharedvpc_config = Config("sharedvpc")
        self.host_project_id = self.sharedvpc_config.require("host_project")
        self.service_project_ids = self.sharedvpc_config.require_object("service_projects")

        self.vpc_manager = VPCManager()
        self.shared_vpc_manager = SharedVPCManager()

    def deploy(self):
        # Create VPC, and Subnet and etc..
        vpc, subnet_a, subnet_b, cloud_router, cloud_nat, internet_route = self.vpc_manager.create_vpc()

        # Create Shared VPC host project and attach service projects to the Shared VPC
        shared_vpc_host_project = self.shared_vpc_manager.create_shared_vpc_host_project(self.host_project_id)
        attached_service_projects = self.shared_vpc_manager.attach_service_projects_to_shared_vpc(self.host_project_id, self.service_project_ids)

        # Create Private Service Access for the VPC
        private_service = PrivateServiceAccess(vpc)
        reserved_range, service_connection = private_service.create()

        # Export some useful outputs
        pulumi.export('vpc_name', vpc.name)
        pulumi.export('subnet_a_name', subnet_a.name)
        pulumi.export('subnet_b_name', subnet_b.name)
        pulumi.export('cloud_router_name', cloud_router.name)  
        pulumi.export('cloud_nat_name', cloud_nat.name)
        pulumi.export('internet_route_name', internet_route.name)       
        pulumi.export('shared_vpc_host_project_id', shared_vpc_host_project.id)
        # Assuming there can be multiple service projects, you can export their names as a list:
        pulumi.export('attached_service_project_ids', [proj.id for proj in attached_service_projects])
        pulumi.export('reserved_range_name', reserved_range.id)
        pulumi.export('service_connection_name', service_connection.id)


# Deploy infrastructure
infrastructure = CloudInfrastructure()
infrastructure.deploy()
