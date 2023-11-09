# Cloud Run Domain Mapping with Pulumi
This project demonstrates how to map custom domains to services running on Google Cloud Run using Pulumi.

<br/>

## Directory Structure
- Pulumi.yaml: Pulumi project configuration file.
- __main__.py: The primary execution file to kick off the domain mapping.
- cloud_run_domain.py: Contains the class and related logic for mapping the custom domain to the Cloud Run service.
- config.py: Global configurations for the project (e.g., DOMAIN_NAME, DOMAIN_REGION).
- utils.py: Utility functions and classes.
- requirements.txt: List of required Python packages.
- venv: Virtual environment for the project.

<br/>

## Prerequisites
Set your desired project using the Google Cloud CLI:
```bash
gcloud config set project <PROJECT ID>
```

Enable the Cloud Run API:
```bash
gcloud services enable run.googleapis.com
```

<br/>

## Deployment

Initialize a new Pulumi stack:

```bash
pulumi stack init <STACK NAME>
```

Install the necessary packages:
```bash
pip install -r requirements.txt
```

Kick off the deployment using Pulumi:
```bash
pulumi up
```

<br/>

## Cleanup
To destroy the resources you've created:
```bash
pulumi destroy
```

And to delete the stack:
```bash
pulumi stack rm <STACK NAME>
```

<br/>

# Reference
- [gcp.cloudrun](https://www.pulumi.com/registry/packages/gcp/api-docs/cloudrun/#gcp-cloudrun)
- [gcp.dns](https://www.pulumi.com/registry/packages/gcp/api-docs/dns/)
