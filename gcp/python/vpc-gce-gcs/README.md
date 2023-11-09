# Pulumi VPC-GCE-GCS Project Setup Guide
The vpc-gce-gcs project consists of two primary stacks: backend-setup and main-infra. This guide will walk you through the setup and management of these stacks.

## Prerequisites
Ensure you have pulumi and gsutil installed and authenticated with the required cloud provider.

<br/>

### 1. backend-setup Stack

<br/>

#### Initialization

Configure your GCP project:
```bash
pulumi config set gcp:project <YOUR_GCP_PROJECT_ID>
```

Initialize the backend-setup stack:
```bash
pulumi stack init backend-setup
```

Check your stacks:
```bash
pulumi stack ls
```

<br/>

#### Set Up the Backend

Use this Python code in __main__.py to create a backend bucket:
```bash
import pulumi
from pulumi_gcp import storage
from bucket_backend import create_backend_bucket

# Call the function
create_backend_bucket()
```

Apply the changes:
```bash
pulumi up
```

<br/>

#### Migrate Backend from Pulumi Cloud to GCS Bucket

Change Pulumi backend to the GCS bucket:
```bash
pulumi login gs://somaz-state
```

Re-initialize the stack and protect your config/secrets:
```bash
pulumi stack init backend-setup
```
- Follow the passphrase prompts.

Import the stack:
```bash
pulumi stack import --file=backend-setup.json
```

To delete the stack resources on Pulumi cloud, do the following:
```bash
pulumi login --cloud-url https://api.pulumi.com
pulumi stack rm --force backend-setup
```

<br/>

### 2. main-infra Stack

<br/>

#### Initialization

Log in to the GCS bucket:
```bash
pulumi login gs://somaz-state
```

Initialize the main-infra stack and protect your config/secrets:
```bash
pulumi stack init main-infra
```
- Follow the passphrase prompts.

Select the main-infra stack:
```bash
pulumi stack select main-infra
```

Set the project variable:
```bash
pulumi config set gcp:project <YOUR_GCP_PROJECT_ID>
```

<br/>

#### Infrastructure Deployment

Apply the changes:

```bash
pulumi up
```
- Follow the passphrase prompts.

You can SSH into your created instance:

```bash
ssh -i ~/.ssh/id_rsa_somaz94 somaz@<INSTANCE_IP>
```
- For example: ssh -i ~/.ssh/id_rsa_somaz94 somaz@34.64.93.60

<br/>

#### Cleanup

Delete the deployed resources:
```bash
pulumi destroy
```

Check and remove the stack:
```bash
pulumi stack ls
pulumi stack rm main-infra --force
```

Finally, remove the GCS state:
```bash
gsutil rm -r gs://somaz-state/
```

<br/>

# Reference
- [gcp.compute](https://www.pulumi.com/registry/packages/gcp/api-docs/compute/#gcp-compute)
- [gcp.storage](https://www.pulumi.com/registry/packages/gcp/api-docs/storage/#gcp-storage)