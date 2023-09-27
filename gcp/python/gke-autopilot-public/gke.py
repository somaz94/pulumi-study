# gke.py

from pulumi_gcp import container
from utils import Utils

class GKECluster:
    def __init__(self, project_id, region, network, fn_network, subnetwork):
        self.project_id = project_id
        self.region = region
        self.network = network
        self.fn_network = fn_network
        self.subnetwork = subnetwork
        self.cluster_name = Utils.resource_name("gke-cluster")
        self.create()

    def create(self):
        zones = [f"{self.region}-a", f"{self.region}-b"]

        # Create a GKE cluster in Autopilot mode
        self.cluster = container.Cluster(self.cluster_name,
                                         name=self.cluster_name,
                                         project=self.project_id,
                                         location=self.region,
                                         initial_node_count=1,
                                         enable_autopilot=True,
                                         network=self.fn_network,
                                         subnetwork=self.subnetwork,
                                         ip_allocation_policy={
                                             "cluster_secondary_range_name": "pulumi-gke-pod",  # Secondary range for Pods
                                             "services_secondary_range_name": "pulumi-gke-service"  # Secondary range for Services
                                         },
                                         master_authorized_networks_config={
                                             "cidr_blocks": [{
                                                 "cidr_block": "xx.xx.xx.xxx/27",   # Public ip
                                                 "display_name": "somaz public ip"
                                             }]
                                         })
