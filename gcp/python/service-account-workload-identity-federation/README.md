# Workload Identity Federation with Pulumi
This project automates the creation and configuration of Workload Identity Federation using Pulumi and Google Cloud Platform (GCP).

<br/>

## Directory Structure
- Pulumi.somaz.yaml: A stack-specific configuration file for the Pulumi project.
- Pulumi.yaml: The primary Pulumi project file that describes the project, its dependencies, and its configuration schema.
- __main__.py: The main entry point for the Pulumi program. This is where Pulumi's deployment process begins.
- config.py: Contains configuration related code.
- iam.py: Contains the IAMPermissions class, responsible for assigning IAM permissions.
- requirements.txt: Lists the Python dependencies required for the project.
- sa.py: [Brief description of its role/functionality in the project].
- utils.py: Contains utility functions used across the project.
- workload_identity_federation.py: Contains the WorkloadIdentityFederation class which creates the necessary GCP resources for workload identity federation.

<br/>

# Reference
- [gcp.serviceAccount](https://www.pulumi.com/registry/packages/gcp/api-docs/serviceaccount/#gcp-serviceaccount)
- [gcp.projects](https://www.pulumi.com/registry/packages/gcp/api-docs/projects/#gcp-projects)