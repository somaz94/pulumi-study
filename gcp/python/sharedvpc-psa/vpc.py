# vpc.py
import pulumi
from pulumi_gcp import compute
from config import NETWORK, REGION, SUBNET_A, SUBNET_B, IGW
from utils import ResourceNamer
import pulumi_gcp as gcp

class VPCManager:
    def __init__(self):
        self.resource_namer = ResourceNamer()

    def create_vpc(self):
        # Create a new VPC
        vpc = compute.Network(self.resource_namer.get_name(NETWORK),
            name=self.resource_namer.get_name(NETWORK),
            auto_create_subnetworks=False,
            description=f"{self.resource_namer.get_name(NETWORK)} network",
        )

        # Create internet Route
        internet_route = compute.Route(self.resource_namer.get_name(f"{NETWORK}-rt"),
            name=self.resource_namer.get_name(f"{NETWORK}-rt"),
            description="Routing Table to access the internet",
            dest_range="0.0.0.0/0",
            network=vpc.self_link,
            next_hop_gateway="default-internet-gateway",
            opts=pulumi.ResourceOptions(depends_on=[vpc])
        )

        # Create a Cloud Router (required by Cloud NAT)
        cloud_router = compute.Router(
            self.resource_namer.get_name("router"),
            name=self.resource_namer.get_name("router"),
            network=vpc.self_link,
            region=REGION,
            opts=pulumi.ResourceOptions(depends_on=[vpc])
        )

        # Create a Cloud NAT
        cloud_nat = compute.RouterNat(
            self.resource_namer.get_name("nat"),
            name=self.resource_namer.get_name("nat"),
            router=cloud_router.name,
            region=REGION,
            nat_ip_allocate_option="AUTO_ONLY",
            source_subnetwork_ip_ranges_to_nat="ALL_SUBNETWORKS_ALL_IP_RANGES",
            opts=pulumi.ResourceOptions(depends_on=[cloud_router, vpc])
        )

        # Create a Subnet within the VPC
        subnet_a = compute.Subnetwork(self.resource_namer.get_name(SUBNET_A),
            name=self.resource_namer.get_name(SUBNET_A),
            network=vpc.self_link,
            ip_cidr_range="10.85.51.0/24",
            region=REGION,
            description=f"{self.resource_namer.get_name(SUBNET_A)} network",
        )
        subnet_b = compute.Subnetwork(self.resource_namer.get_name(SUBNET_B),
            name=self.resource_namer.get_name(SUBNET_B),
            network=vpc.self_link,
            ip_cidr_range="10.85.52.0/24",
            region=REGION,
            description=f"{self.resource_namer.get_name(SUBNET_B)} network",
        )

        return vpc, subnet_a, subnet_b, cloud_router, cloud_nat, internet_route

class SharedVPCManager:
    def __init__(self):
        self.resource_namer = ResourceNamer()

    def create_shared_vpc_host_project(self, host_project_id):
        # Set the host project to Shared VPC
        shared_vpc_host_project = gcp.compute.SharedVPCHostProject(
            self.resource_namer.get_name("shared-vpc-host"),
            project=host_project_id
        )
        return shared_vpc_host_project

    def attach_service_projects_to_shared_vpc(self, host_project_id, service_project_ids):
        attached_service_projects = []
        for service_project_id in service_project_ids:
            # Attach each service project to the Shared VPC
            service_project_attachment = gcp.compute.SharedVPCServiceProject(
                self.resource_namer.get_name(f"shared-vpc-service-{service_project_id}"),
                service_project=service_project_id,
                host_project=host_project_id,
                region=REGION  # Added region for service project attachment
            )
            attached_service_projects.append(service_project_attachment)
        return attached_service_projects
