"""A Google Cloud Python Pulumi program"""

import pulumi
from db import create_mysql
from redis_instance import create_redis_instance

# Deploy the resources
mysql_instance, mysql_db, mysql_user = create_mysql()

# Create the Redis instance
redis_instance = create_redis_instance()

# Export relevant information for easy access
pulumi.export("mysql_instance_name", mysql_instance.name)
pulumi.export("mysql_database_name", mysql_db.name)
pulumi.export("mysql_username", mysql_user.name)
pulumi.export("redis_instance_name", redis_instance.name)
