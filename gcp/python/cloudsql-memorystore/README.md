## Advance preparation
Create and proceed with Shared VPC and Private Service Access.

You can also create a Secret Config using the commands below.
```bash

pulumi stack init <stack name> # Do it with the stack name you want.

pulumi config set gcp:project <your gcp project id>

pulumi config set --secret db_admin_password <YOUR_DB_PASSWORD>
pulumi config set --secret db_admin_user <YOUR_DB_USER>

pulumi config set --secret db_admin_password somaz@2023
pulumi config set --secret db_admin_user somaz

pulumi config set --plaintext host_project somaz
pulumi config set --plaintext private_service_ip 10.1.16.0
pulumi config set --plaintext private_service_prefix 20

pulumi config
KEY                     VALUE
db_admin_password       [secret]
db_admin_user           [secret]
host_project            somaz
private_service_ip      10.1.16.0
private_service_prefix  20
gcp:project             dev-somaz

pulumi config get db_admin_password
somaz@2023

pulumi config get db_admin_user
somaz
```
