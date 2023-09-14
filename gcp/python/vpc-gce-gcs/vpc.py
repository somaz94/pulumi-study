# vpc.py
from pulumi_gcp import compute
from config import NETWORK, REGION, SUBNET, IGW
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

        # Create an Internet Gateway for the VPC
        igw = compute.GlobalAddress(Utils.resource_name(IGW),
            name=Utils.resource_name(IGW),
            description=f"{Utils.resource_name(IGW)} network",
        )

        # Create a Subnet within the VPC
        subnet = compute.Subnetwork(Utils.resource_name(SUBNET),
            name=Utils.resource_name(SUBNET),
            network=vpc.self_link,
            ip_cidr_range="10.0.0.0/16",
            region=REGION,
            description=f"{Utils.resource_name(SUBNET)} network",
        )

        return vpc, igw, subnet
