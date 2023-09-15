## Preliminary Steps
Set up Shared VPC and Private Service Access before proceeding further.

You can also set up secret configurations using the commands provided below:
```bash
# Initialize a new stack with your desired name.
pulumi stack init <STACK_NAME>

# Set your Google Cloud project.
pulumi config set gcp:project <YOUR_GCP_PROJECT_ID>

# Set up database administrator credentials.
pulumi config set --secret db_admin_password <YOUR_DB_PASSWORD>
pulumi config set --secret db_admin_user <YOUR_DB_USER>

# Example with values:
pulumi config set --secret db_admin_password somaz@2023
pulumi config set --secret db_admin_user somaz

# Other necessary configurations:
pulumi config set --plaintext host_project somaz
pulumi config set --plaintext private_service_ip 10.1.16.0
pulumi config set --plaintext private_service_prefix 20
```

```bash
# Confirm your configuration:
pulumi config

# Expected output:
KEY                     VALUE
db_admin_password       [secret]
db_admin_user           [secret]
host_project            somaz
private_service_ip      10.1.16.0
private_service_prefix  20
gcp:project             dev-somaz
```
```bash
Retrieve the actual values of your secrets:
pulumi config get db_admin_password
somaz@2023

pulumi config get db_admin_user
somaz
```
