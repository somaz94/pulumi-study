import * as pulumi from "@pulumi/pulumi";
import { CloudArmor } from "./cloudArmor";
import { IP_ALLOW_RULE, IP_ALLOW_RULE_STANDARD, REGION_BLOCK_RULE } from "./config";

// Project ID
const projectConfig = new pulumi.Config("gcp");
const projectId = projectConfig.require("project");

// Create CloudArmor instance
const armor = new CloudArmor(projectId);

// IP Allow Rule Standard
const ipAllowStandardPolicy = armor.createPolicy(
    IP_ALLOW_RULE_STANDARD,
    "Cloud Armor Edge security policy for IP Allow (Standard)",
    "deny(403)",
    "CLOUD_ARMOR_EDGE",
    {
        "allow_specific_ip_range_standard": {
            action: "allow",
            priority: 10,
            description: "Allow specific IP ranges (Standard)",
            expression: "77.77.77.64/27, 88.88.88.88/30"  // Using a comma-separated list of IPs
        }
    }
);

// IP Allow Rule
const ipAllowPolicy = armor.createPolicy(
    IP_ALLOW_RULE,
    "Cloud Armor Edge security policy for IP Allow",
    "deny(403)",
    "CLOUD_ARMOR_EDGE",
    {
        "allow_specific_ip_range": {
            action: "allow",
            priority: 10,
            description: "Allow specific IP ranges",
            expression: "inIpRange(origin.ip, '77.77.77.64/27') || inIpRange(origin.ip, '88.88.88.88/30')"
        }
    }
);

// Region Block Rule
const regionBlockPolicy = armor.createPolicy(
    REGION_BLOCK_RULE,
    "Cloud Armor Edge security policy for Region block",
    "deny(403)",
    "CLOUD_ARMOR_EDGE",
    {
        "block_specific_regions": {
            action: "allow",
            priority: 1,
            description: "Block China Regions",
            expression: "origin.region_code != 'CN'"
        }
    }
);

// Export the names of the policies for reference
pulumi.output({
  ip_allow_standard_policy_name: ipAllowStandardPolicy.name,
  ip_allow_policy_name: ipAllowPolicy.name,
  region_block_policy_name: regionBlockPolicy.name
});


