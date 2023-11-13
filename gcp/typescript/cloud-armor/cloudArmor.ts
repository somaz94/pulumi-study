import * as gcp from "@pulumi/gcp";

export class CloudArmor {
    private projectId: string;

    constructor(projectId: string) {
        this.projectId = projectId;
    }

    createPolicy(baseName: string, description: string, defaultRuleAction: string, type: string, customRules: any): gcp.compute.SecurityPolicy {
        const rules: any[] = []; // Use a more generic type for rules

        for (const ruleName in customRules) {
            const ruleValues = customRules[ruleName];
            let match: any; // Generic type for match

            if (ruleValues.expression.includes("inIpRange")) {
                match = {
                    expr: {
                        expression: ruleValues.expression
                    }
                };
            } else if (ruleValues.expression.includes(",")) { // Comma-separated list of IPs
                const ipRanges = ruleValues.expression.split(",").map((ip: string) => ip.trim());
                match = {
                    config: {
                        srcIpRanges: ipRanges
                    },
                    versionedExpr: "SRC_IPS_V1"
                };
            } else { // Using CEL expressions
                match = {
                    expr: {
                        expression: ruleValues.expression
                    }
                };
            }

            rules.push({
                action: ruleValues.action,
                description: ruleValues.description,
                priority: ruleValues.priority,
                match: match
            });
        }

        // Add Standard Rule
        rules.push({
            action: defaultRuleAction,
            description: "Default rule",
            priority: 2147483647,
            match: {
                config: {
                    srcIpRanges: ["*"]
                },
                versionedExpr: "SRC_IPS_V1"
            }
        });

        return new gcp.compute.SecurityPolicy(baseName, {
            name: baseName,
            project: this.projectId,
            description: description,
            type: type,
            rules: rules
        });
    }
}
