# redis_instance.py
import pulumi
import pulumi_gcp as gcp
from config import REGION, NETWORK
from utils import resource_name

class RedisManager:
    def __init__(self):
        # Fetch configuration values from the 'cloudsql-memorystore' namespace
        cloudsql_config = pulumi.Config("cloudsql-memorystore")
        self.host_project = cloudsql_config.require("host_project")

        # Fetch configuration values from the 'gcp' namespace
        gcp_config = pulumi.Config("gcp")
        self.project = gcp_config.require("project")

    def create_instance(self, instance_name="redis-dev"):
        # Construct the fully-qualified authorized network string
        authorized_network = f"projects/{self.host_project}/global/networks/{NETWORK}"

        redis_name = resource_name(instance_name)

        # Create a Google Cloud MemoryStore Redis instance
        redis_instance = gcp.redis.Instance(
            resource_name=redis_name,
            name=redis_name,
            project=self.project,
            region=REGION,
            location_id=f"{REGION}-a",
            auth_enabled=False,
            transit_encryption_mode="DISABLED",
            tier="BASIC",
            connect_mode="PRIVATE_SERVICE_ACCESS",
            authorized_network=authorized_network,
            reserved_ip_range="google-managed-services-mgmt-share-vpc",
            memory_size_gb=1,
            persistence_config=gcp.redis.InstancePersistenceConfigArgs(
                persistence_mode="DISABLED"
            )
        )

        return redis_instance
