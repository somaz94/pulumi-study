# __main__.py
"""A Google Cloud Python Pulumi program"""

import pulumi
from db import MySQLManager
from redis_instance import RedisManager

class DeploymentManager:
    def __init__(self):
        self.mysql_manager = MySQLManager()
        self.redis_manager = RedisManager()

    def deploy(self):
        # Deploy MySQL resources
        mysql_instance, mysql_dbs, mysql_user = self.mysql_manager.create_instance("mysql-dev")

        # Deploy Redis instance
        redis_instance = self.redis_manager.create_instance()

        # Export relevant information for easy access
        pulumi.export("mysql_instance_name", mysql_instance.name)
        # Assuming you'd want to export the name of the first database for simplicity
        pulumi.export("mysql_database_name", mysql_dbs[0].name)
        pulumi.export("mysql_username", mysql_user.name)
        pulumi.export("redis_instance_name", redis_instance.name)

if __name__ == "__main__":
    manager = DeploymentManager()
    manager.deploy()
