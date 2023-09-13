import pulumi
import pulumi_gcp as gcp
from config import REGION, NETWORK
from utils import resource_name

# Fetch configuration values from the 'cloudsql-memorystore' namespace
cloudsql_config = pulumi.Config("cloudsql-memorystore")
host_project = cloudsql_config.require("host_project")

# Fetch configuration values from the 'gcp' namespace
gcp_config = pulumi.Config("gcp")
project = gcp_config.require("project")

redis_name_dev = resource_name("redis-dev")

def create_redis_instance():
    # Construct the fully-qualified authorized network string
    authorized_network = f"projects/{host_project}/global/networks/{NETWORK}"

    # Create a Google Cloud MemoryStore Redis instance
    redis_instance = gcp.redis.Instance(
        resource_name=redis_name_dev,
        name=redis_name_dev,
        project=project,
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
