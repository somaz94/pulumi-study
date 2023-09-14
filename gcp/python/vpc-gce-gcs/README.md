## Preparation in advance
The vpc-gce-gcs project has two stacks: backend-setup and main-infrastructure.

## backend-setup

```bash
pulumi config set gcp:project <your gcp project id>

pulumi stack init backend-setup
Created stack 'backend-setup'

pulumi stack ls
NAME            LAST UPDATE  RESOURCE COUNT  URL
backend-setup*  n/a          n/a             https://app.pulumi.com/somaz94/vpc-gce-gcs/backend-setup
```

```bash
cat __main__.py
# Create backend-bucket.py 
import pulumi
from pulumi_gcp import storage

from bucket_backend import create_backend_bucket

# Call the function
create_backend_bucket()

# apply
pulumi up
```

Pulumi backend has now been changed from Pulumi cloud to gcs bucket.
__main__.In py, the bucket generation code is annotated.
```bash
pulumi login gs://somaz-state
Logged in to AD01769994 as somaz (gs://somaz-state)
```

```bash
pulumi stack init backend-setup
Created stack 'backend-setup'
Enter your passphrase to protect config/secrets:
Re-enter your passphrase to confirm:

pulumi stack ls
NAME                  LAST UPDATE  RESOURCE COUNT
backend-setup         n/a          n/a

pulumi stack select backend-setup

pulumi stack import --file=backend-setup.json
Import complete.
```

It now deletes the stack resources on the pulumi cloud.
```bash
pulumi login --cloud-url https://api.pulumi.com
pulumi stack rm --force
This will permanently remove the 'backend-setup' stack!
Please confirm that this is what you'd like to do by typing `backend-setup`: backend-setup
Stack 'backend-setup' has been removed!
```

## main-infra

Log in to the gs bucket again.
```bash
pulumi login gs://somaz-state

pulumi stack init main-infra
Created stack 'main-infra'
Enter your passphrase to protect config/secrets:
Re-enter your passphrase to confirm:

pulumi stack select main-infra
```

Sets the variable.
```bash
pulumi config set gcp:project <your gcp project id>
```

```bash
# apply
pulumi up
Enter your passphrase to unlock config/secrets
    (set PULUMI_CONFIG_PASSPHRASE or PULUMI_CONFIG_PASSPHRASE_FILE to remember):
Enter your passphrase to unlock config/secrets
...
Outputs:
    igw_name            : "somaz-igw"
    instance_external_ip: "34.64.93.60"
    instance_name       : "somaz-instance"
    subnet_name         : "somaz-subnet"
    vpc_name            : "somaz-vpc"

ssh -i ~/.ssh/id_rsa_somaz94 somaz@34.64.93.60

somaz@somaz-instance:~$ dpkg -l |grep apache2
iF  apache2                            2.4.41-4ubuntu3.14                amd64        Apache HTTP Server
ii  apache2-bin                        2.4.41-4ubuntu3.14                amd64        Apache HTTP Server (modules and other binary files)
ii  apache2-data                       2.4.41-4ubuntu3.14                all          Apache HTTP Server (common files)
ii  apache2-utils                      2.4.41-4ubuntu3.14                amd64        Apache HTTP Server (utility programs for web servers)
```

```bash
# delete
pulumi destrpy

pulumi stack ls

pulumi stack rm main-infra
pulumi stack rm --force

gsutil rm -r gs://somaz-state/
```
