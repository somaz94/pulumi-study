import pulumi
import pulumi_gcp as gcp
from pulumi_gcp import servicenetworking 
from utils import ResourceNamer
from config import PRIVATE_SERVICE_IP, PRIVATE_SERVICE_PREFIX

class PrivateServiceAccess:
    
    def __init__(self, vpc):
        self.vpc = vpc
        self.resource_namer = ResourceNamer()

    def create(self):
        self.reserved_range = self._create_reserved_range()
        self.service_connection = self._create_service_connection()
        return self.reserved_range, self.service_connection
    
    def _create_reserved_range(self):
        # Create a reserved IP range for Private Service Access
        return gcp.compute.GlobalAddress(
            self.resource_namer.get_name("private-service-range"),
            name=self.resource_namer.get_name("private-service-range"),
            address_type="INTERNAL",
            purpose="VPC_PEERING",
            address=PRIVATE_SERVICE_IP,
            prefix_length=PRIVATE_SERVICE_PREFIX,
            network=self.vpc.id,  # Change from self_link to id
            description="Reserved IP range for Private Service Access",
            opts=pulumi.ResourceOptions(depends_on=[self.vpc])
        )
    
    def _create_service_connection(self):
        # Use the apply method on the output attributes (name) of vpc and reserved_range
        def create_service_connection(args):
            vpc_name, range_name = args
            return servicenetworking.Connection(
                self.resource_namer.get_name("private-service-connection"),
                network=vpc_name,
                reserved_peering_ranges=[range_name],
                service="servicenetworking.googleapis.com",
                opts=pulumi.ResourceOptions(depends_on=[self.reserved_range])  # ensuring connection is made after address reservation
            )
        
        return pulumi.Output.all(self.vpc.name, self.reserved_range.name).apply(create_service_connection)
