## Advance preparation
Create GKE Autopilot Public Resource

Sets the variable.
```bash
pulumi config set gcp:project <your gcp project id>
pulumi config set --plaintext host_project somaz
```

## Preparation when creating a GKE cluster
The current architecture is configured using a shared VPC from somaz (Host Project).
Therefore, service projects using shared VPCs must set up IAM before creating a GKE cluster with Pulumi.

Host Project
- somaz
Service Project
- dev-somaz

### Sets the IAM
It is written by the Service Project based on dev-somaz. The rest of the Service Project is the same.
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

#### Enable GKE API in projects
```bash
gcloud services enable container.googleapis.com

# Confirm
gcloud services list --enabled |grep Kubernetes
container.googleapis.com             Kubernetes Engine API
```

#### IAM Settings
- Grant the roles/container.serviceAgent permission to the GKE API service account of the Host Project and the Google API service account GKE API of the Service Project (Granted in the Host Project).
- Grant the roles/editor permission to the GKE API service account of the Service Project (Granted in the Service Project).
- Grant the roles/compute.networkUser permission to the GKE API service account and the Google API service account of the Service Project (Granted in the Host Project).
- Grant user permissions to the relevant Subnet in the MGMT shared VPC (optional). You can grant roles/compute.networkUser permission for each subnet.
- Grant the roles/compute.networkAdmin, roles/compute.viewer, and roles/editor permissions to the GKE API service account and the Google API service account of the Service Project (Granted in the Host Project).
