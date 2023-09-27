# cloud_armor.py
from pulumi_gcp import compute

class CloudArmor:

    def __init__(self, project_id):
        self.project_id = project_id

    def create_policy(self, base_name, description, default_rule_action, type, custom_rules):
        rules = []

        for _, rule_values in custom_rules.items():
            if "inIpRange" in rule_values['expression']:
                rules.append(
                    compute.SecurityPolicyRuleArgs(
                        action=rule_values['action'],
                        description=rule_values['description'],
                        priority=rule_values['priority'],
                        match=compute.SecurityPolicyRuleMatchArgs(
                            expr=compute.SecurityPolicyRuleMatchExprArgs(
                                expression=rule_values['expression']
                            )
                        )
                    )
                )
            elif ',' in rule_values['expression']:  # Checks if we have a comma-separated list of IPs
                ip_ranges = [ip.strip() for ip in rule_values['expression'].split(',')]
                rules.append(
                    compute.SecurityPolicyRuleArgs(
                        action=rule_values['action'],
                        description=rule_values['description'],
                        priority=rule_values['priority'],
                        match=compute.SecurityPolicyRuleMatchArgs(
                            versioned_expr="SRC_IPS_V1",
                            config=compute.SecurityPolicyRuleMatchConfigArgs(
                                src_ip_ranges=ip_ranges
                            )
                        )
                    )
                )
            else:  # Using CEL expressions
                rules.append(
                    compute.SecurityPolicyRuleArgs(
                        action=rule_values['action'],
                        description=rule_values['description'],
                        priority=rule_values['priority'],
                        match=compute.SecurityPolicyRuleMatchArgs(
                            expr=compute.SecurityPolicyRuleMatchExprArgs(
                                expression=rule_values['expression'],
                            )
                        )
                    )
                )

        # ADD Standard Rules
        rules.append(
            compute.SecurityPolicyRuleArgs(
                action=default_rule_action,
                description="Default rule",
                priority=2147483647,
                match=compute.SecurityPolicyRuleMatchArgs(
                    versioned_expr="SRC_IPS_V1",
                    config=compute.SecurityPolicyRuleMatchConfigArgs(
                        src_ip_ranges=["*"]
                    )
                )
            )
        )

        policy = compute.SecurityPolicy(
            base_name,
            name=base_name,
            project=self.project_id,
            description=description,
            type=type,
            rules=rules,
        )

        return policy


