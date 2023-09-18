# Cloud Run Deployment with Pulumi
This project demonstrates how to deploy a Docker container to Google Cloud Run using Pulumi.

<br/>

## Directory Structure
- Pulumi.yaml: Pulumi project configuration file.
- __main__.py: The primary execution file to kick off the deployment.
- cloud_run.py: Contains the class and related logic for deploying the Cloud Run service.
- config.py: Global configurations for the project (e.g., PREFIX, REGION).
- utils.py: Utility functions and classes.
- requirements.txt: List of required Python packages.

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

