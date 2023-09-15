# __main__.py

import pulumi
from pulumi import Config
import gke
from config import REGION, SHARED_NETWORK, FN_SHARED_NETWORK, FN_SUBNETWORK

class ConfigSet:
    def __init__(self):
        self.gcp_config = Config("gcp")
        self.project_id = self.gcp_config.require("project")

        self.sharedvpc_config = Config("gke-autopilot-public")
        self.host_project_id = self.sharedvpc_config.require("host_project")

# Initialize ConfigSet
config = ConfigSet()

# Create GKE Cluster using GKECluster class
gke_instance = gke.GKECluster(config.project_id, REGION, SHARED_NETWORK, FN_SHARED_NETWORK, FN_SUBNETWORK)

# Export the Cluster's endpoint and the kubectl config
pulumi.export('endpoint', gke_instance.cluster.endpoint)
pulumi.export('kubeconfig', gke_instance.cluster.master_auth)
