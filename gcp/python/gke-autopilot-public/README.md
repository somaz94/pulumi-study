## Advance preparation
Create GKE Autopilot Public Resource

Setting Up GKE Autopilot Public Resource.

Before starting, ensure you set the necessary variables:
```bash
pulumi config set gcp:project <your gcp project id>
pulumi config set --plaintext host_project somaz
```

<br/>

## Preparation when creating a GKE cluster
This configuration relies on a shared VPC from somaz (the Host Project). If you're utilizing a service project with shared VPCs, set up IAM before proceeding with the GKE cluster creation using Pulumi.

Host Project
- somaz
Service Project
- dev-somaz

<br/>

### Sets the IAM
These instructions are written for the Service Project dev-somaz. Other Service Projects will follow similar steps.

Identify the service accounts:
- Google API ServiceAccount: <project-number>@cloudservices.gserviceaccount.com
- GKE API ServiceAccount: service-<project-number>@container-engine-robot.iam.gserviceaccount.com
```bash
GKE_SA=service-$(gcloud projects describe dev-somaz --format 'value(projectNumber)')@container-engine-robot.iam.gserviceaccount.com

echo $GKE_SA
service-<project-id>@container-engine-robot.iam.gserviceaccount.com

$ GCP_API_SA=$(gcloud projects describe dev-somaz --format 'value(projectNumber)')@cloudservices.gserviceaccount.com

$ echo $GCP_API_SA
<project-id>@cloudservices.gserviceaccount.com
```

<br/>

### Enable GKE API in projects

Activate the GKE API:
```bash
gcloud services enable container.googleapis.com

# Confirm
gcloud services list --enabled |grep Kubernetes
container.googleapis.com             Kubernetes Engine API
```

<br/>

### IAM Settings
- Grant the roles/container.serviceAgent permission to both the GKE API service account of the Host Project and the Google API service account GKE API of the Service Project (Permissions set in the Host Project).
- Assign the roles/editor role to the GKE API service account in the Service Project.
- Give the roles/compute.networkUser role to both the GKE API service account and the Google API service account in the Service Project (Permissions set in the Host Project).
- Optionally, for the relevant Subnet in the MGMT shared VPC, provide user permissions. For individual subnets, the roles/compute.networkUser can be granted.
- Grant the roles/compute.networkAdmin, roles/compute.viewer, and roles/editor roles to both the GKE API service account and the Google API service account in the Service Project (Permissions set in the Host Project).

<br/>

# Reference
- [gcp.container](https://www.pulumi.com/registry/packages/gcp/api-docs/container/#gcp-container)