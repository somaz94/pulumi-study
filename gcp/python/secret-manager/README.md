## Preparation in advance
Create and proceed with Secret Manager

You can also create a Secret Config using the commands below.
```bash
pulumi config set --secret dev_db_password <YOUR_DB_PASSWORD>
pulumi config set --secret dev_db_username <YOUR_DB_USER>

pulumi config set --secret dev_db_password somaz@2023
pulumi config set --secret dev_db_username somaz

pulumi config set --plaintext dev_db_secret somaz-db-secret

pulumi config
KEY              VALUE
gcp:project      somaz
dev_db_password  [secret]
dev_db_secret    somaz-db-secret
dev_db_username  [secret]

pulumi config get dev_db_password
somaz@2023

pulumi config get dev_db_username
somaz
```
