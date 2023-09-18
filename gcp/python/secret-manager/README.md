# Secret Manager with Pulumi
This guide helps you to create and manage your secrets using Pulumi for your GCP project.

## Prerequisites
Ensure you have pulumi installed and are authenticated with the necessary cloud provider.

## Steps

### 1. Initialize a New Pulumi Stack

Begin by creating a new Pulumi stack for your project.
```bash
pulumi stack init <stack name>
```
Replace <STACK_NAME> with the desired name for your stack.

<br/>

### 2. Set GCP Project

Specify the GCP project ID where you intend to manage secrets.
```bash
pulumi config set gcp:project <YOUR_GCP_PROJECT_ID>
```
Replace <YOUR_GCP_PROJECT_ID> with your Google Cloud Project ID.

<br/>

### 3. Set Database Secrets

Provide the database credentials. These will be stored securely by Pulumi.

```bash
pulumi config set --secret dev_db_password <YOUR_DB_PASSWORD>
pulumi config set --secret dev_db_username <YOUR_DB_USER>
```
Replace <YOUR_DB_PASSWORD> and <YOUR_DB_USER> with your actual database credentials.

For demonstration purposes, using the following credentials:
```bash
pulumi config set --secret dev_db_password somaz@2023
pulumi config set --secret dev_db_username somaz
```

<br/>

### 4. Set Additional Plaintext Configuration

If you need to set any plaintext configurations (not recommended for sensitive data):
```bash
pulumi config set --plaintext dev_db_secret somaz-db-secret
```

<br/>

### 5. Verify Configuration
To check your current configurations, use:
```bash
pulumi config
```

Expected Output:
```bash
KEY              VALUE
gcp:project      somaz
dev_db_password  [secret]
dev_db_secret    somaz-db-secret
dev_db_username  [secret]
```

<br/>

### 6. Retrieve Secret Values
If you need to retrieve the secret values, you can do so as follows:
```bash
pulumi config get dev_db_password   # Outputs: somaz@2023
pulumi config get dev_db_username   # Outputs: somaz
```

<br/>

## Caution
Always ensure that secrets are handled with care. Avoid exposing them in logs, repositories, or other insecure locations.