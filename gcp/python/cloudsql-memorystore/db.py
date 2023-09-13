import pulumi
import pulumi_gcp as gcp
from config import REGION, NETWORK
from utils import resource_name

# Fetch configuration values from the 'cloudsql-memorystore' namespace
cloudsql_config = pulumi.Config("cloudsql-memorystore")
host_project = cloudsql_config.require("host_project")
db_admin_password = cloudsql_config.require_secret("db_admin_password")
db_admin_user = cloudsql_config.require_secret("db_admin_user")

# Fetch configuration values from the 'gcp' namespace
gcp_config = pulumi.Config("gcp")
project = gcp_config.require("project")

db_name_dev = resource_name("db-dev")

def create_mysql():
    # Create a Google SQL Database Instance
    mysql_instance = gcp.sql.DatabaseInstance(
        resource_name=db_name_dev,
        name=db_name_dev,
        project=project,
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
                private_network=f"projects/{host_project}/global/networks/{NETWORK}",
                authorized_networks=[],
                # Additional fields for private access
                allocated_ip_range="google-managed-services-mgmt-share-vpc",
                enable_private_path_for_google_cloud_services=True,
            ),
        ),
        deletion_protection=False
    )

    # Create MySQL User
    mysql_user = gcp.sql.User(
        "user",
        name=db_admin_user,
        password=db_admin_password,
        instance=mysql_instance.name,
        host="%"
    )
    
    # Create Database
    mysql_db = gcp.sql.Database(
        "database",
        name=db_name_dev,
        instance=mysql_instance.name
    )
    
    return mysql_instance, mysql_db, mysql_user


