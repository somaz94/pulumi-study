# Shared VPC & Private Service Access with Pulumi
This guide demonstrates how to set up a Shared VPC and Private Service Access using Pulumi for your GCP project.

## Prerequisites
Ensure you have pulumi installed.
Ensure you're authenticated with the necessary cloud provider.

## Steps

### 1. Set GCP Project
Before you start, specify the GCP project ID you intend to work with.
```bash
pulumi config set gcp:project <YOUR_GCP_PROJECT_ID>
```
Replace <YOUR_GCP_PROJECT_ID> with your Google Cloud Project ID.
<br/>

### 2. Login to Pulumi Cloud Service
Ensure you are logged into Pulumi's cloud service.
```bash
pulumi login --cloud-url https://api.pulumi.com
```
<br/>

### 3. Initialize a New Pulumi Stack
Create a new Pulumi stack specifically for Shared VPC and Private Service Access.
```bash
pulumi stack init sharedvpc-psa
```
This will output details about the created stack, for example:

```bash
Created stack 'sharedvpc-psa'
NAME            LAST UPDATE  RESOURCE COUNT  URL
sharedvpc-psa*  n/a          n/a             https://app.pulumi.com/somaz94/shared-vpc/sharedvpc-psa
```
<br/>

### 4. Set Configuration Variables
Configure the necessary variables for the shared VPC.
```bash
pulumi config set --plaintext host_project somaz
pulumi config set --plaintext service_projects '["dev-somaz", "qa-somaz"]'
```
Adjust somaz, dev-somaz, and qa-somaz to your specific project names if they are different.
<br/>

## Conclusion
You've now configured the settings required for creating a Shared VPC and Private Service Access using Pulumi on GCP. Make sure to follow any additional steps or scripts required to complete the deployment based on your project's specifics.
<br/>

## Caution
Always double-check configurations and ensure you're not unintentionally exposing sensitive information. Remember to adhere to the best practices when working with shared resources and service access on GCP.
