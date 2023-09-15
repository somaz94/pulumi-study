# __main__.py
import pulumi
from cloud_armor import CloudArmor
from config import IP_ALLOW_RULE, IP_ALLOW_RULE_STANDARD, REGION_BLOCK_RULE

# Project ID
project_id = pulumi.Config('gcp').require('project')

# Create CloudArmor instance
armor = CloudArmor(project_id)

# IP Allow Rule Standard
ip_allow_standard_policy = armor.create_policy(
    base_name=IP_ALLOW_RULE_STANDARD,
    description="Cloud Armor Edge security policy for IP Allow (Standard)",
    default_rule_action="deny(403)",
    type="CLOUD_ARMOR_EDGE",
    custom_rules={
        "allow_specific_ip_range_standard": {
            "action": "allow",
            "priority": 10,
            "description": "Allow specific IP ranges (Standard)",
            "expression": "77.77.77.64/27, 88.88.88.88/30"  # Using a comma-separated list of IPs
        }
    }
)

# IP Allow Rule
ip_allow_policy = armor.create_policy(
    base_name=IP_ALLOW_RULE,
    description="Cloud Armor Edge security policy for IP Allow",
    default_rule_action="deny(403)",
    type="CLOUD_ARMOR_EDGE",
    custom_rules={
        "allow_specific_ip_range": {
            "action": "allow",
            "priority": 10,
            "description": "Allow specific IP ranges",
            "expression": "inIpRange(origin.ip, '77.77.77.64/27') || inIpRange(origin.ip, '88.88.88.88/30')"
        }
    }
)

# Region Block Rule
region_block_policy = armor.create_policy(
    base_name=REGION_BLOCK_RULE,
    description="Cloud Armor Edge security policy for Region block",
    default_rule_action="deny(403)",
    type="CLOUD_ARMOR_EDGE",
    custom_rules={
        "block_specific_regions": {
            "action": "allow",
            "priority": 1,
            "description": "Block China Regions",
            "expression": "origin.region_code != 'CN'"
        }
    }
)

# Export the names of the policies for reference
pulumi.export('ip_allow_standard_policy_name', ip_allow_standard_policy.name)
pulumi.export('ip_allow_policy_name', ip_allow_policy.name)
pulumi.export('region_block_policy_name', region_block_policy.name)


