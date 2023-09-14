# db.py
import pulumi
import pulumi_gcp as gcp
from config import REGION, NETWORK
from utils import resource_name

class MySQLManager:
    def __init__(self):
        # Fetch configuration values from the 'cloudsql-memorystore' namespace
        cloudsql_config = pulumi.Config("cloudsql-memorystore")
        self.host_project = cloudsql_config.require("host_project")
        self.db_admin_password = cloudsql_config.require_secret("db_admin_password")
        self.db_admin_user = cloudsql_config.require_secret("db_admin_user")

        # Fetch configuration values from the 'gcp' namespace
        gcp_config = pulumi.Config("gcp")
        self.project = gcp_config.require("project")

    def create_instance(self, instance_name):
        instance_name_resource = resource_name(instance_name)

        # Create a Google SQL Database Instance
        mysql_instance = gcp.sql.DatabaseInstance(
            resource_name=instance_name_resource,
            name=instance_name_resource,
            project=self.project,
            region=REGION,
            database_version="MYSQL_8_0",
            settings=gcp.sql.DatabaseInstanceSettingsArgs(
                tier="db-custom-2-3840",
                availability_type="ZONAL",
                maintenance_window=gcp.sql.DatabaseInstanceSettingsMaintenanceWindowArgs(
                    day=1,
                    hour=0,
                    update_track="stable"
                ),
                ip_configuration=gcp.sql.DatabaseInstanceSettingsIpConfigurationArgs(
                    ipv4_enabled=False,
                    require_ssl=False,
                    private_network=f"projects/{self.host_project}/global/networks/{NETWORK}",
                    authorized_networks=[],
                    allocated_ip_range="google-managed-services-mgmt-share-vpc",
                    enable_private_path_for_google_cloud_services=True,
                ),
            ),
            deletion_protection=False
        )

        # Create MySQL User
        mysql_user = gcp.sql.User(
            "user",
            name=self.db_admin_user,
            password=self.db_admin_password,
            instance=mysql_instance.name,
            host="%"
        )
        
        # Create Databases: somaz-dev, somaz-qa, and somaz-prod
        databases = ["somaz-dev", "somaz-qa", "somaz-prod"]
        mysql_dbs = []
        for db_name in databases:
            mysql_db = gcp.sql.Database(
                db_name,
                name=db_name,
                instance=mysql_instance.name
            )
            mysql_dbs.append(mysql_db)
        
        return mysql_instance, mysql_dbs, mysql_user
