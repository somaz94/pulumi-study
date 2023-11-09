# Pulumi GCP Artifact Registry Setup
This project contains Pulumi code for setting up Artifact Registries on Google Cloud Platform.

<br/>

## Structure
- config.py: Contains configuration details like prefix, region, and repository names.
- utils.py: Utility class for generating resource names.
- artifact_registry.py: Pulumi code for creating Artifact Registries on GCP.

<br/>

## Prerequisites
- Ensure you have [Pulumi CLI](https://www.pulumi.com/docs/cli/) installed.
- Configure Pulumi to use [GCP](https://www.pulumi.com/docs/clouds/gcp/setup/).
- Install the necessary Python packages: `pip install pulumi pulumi-gcp`

<br/>

## Usage
1. Initialize a new Pulumi stack: pulumi stack init [STACK_NAME]
2. Set GCP configuration: pulumi config set gcp:project [YOUR_GCP_PROJECT_ID]
3. Deploy the Pulumi stack: pulumi up

<br/>

# Reference
- [gcp.artifactregistry](https://www.pulumi.com/registry/packages/gcp/api-docs/artifactregistry/#gcp-artifactregistry)