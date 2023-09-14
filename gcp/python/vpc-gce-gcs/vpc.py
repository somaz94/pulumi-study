# vpc.py
from pulumi_gcp import compute
from config import NETWORK, REGION, SUBNET
from utils import Utils

class VPC:

    @staticmethod
    def create():
        # Create a new VPC
        vpc = compute.Network(Utils.resource_name(NETWORK),
            name=Utils.resource_name(NETWORK),
            auto_create_subnetworks=False,
            description=f"{Utils.resource_name(NETWORK)} network",
        )

        # Create internet Route
        route = compute.Route(Utils.resource_name(f"{NETWORK}-rt"),
            name=Utils.resource_name(f"{NETWORK}-rt"),
            description="Routing Table to access the internet",
            dest_range="0.0.0.0/0",
            network=vpc.self_link,
            next_hop_gateway="default-internet-gateway",
        )

        # Create a Subnet within the VPC
        subnet = compute.Subnetwork(Utils.resource_name(SUBNET),
            name=Utils.resource_name(SUBNET),
            network=vpc.self_link,
            ip_cidr_range="10.0.0.0/16",
            region=REGION,
            description=f"{Utils.resource_name(SUBNET)} network",
        )

        return vpc, route, subnet