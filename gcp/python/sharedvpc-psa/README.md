## Advance preparation
Create and proceed with Shared VPC & Private Service Accessr

```bash
pulumi config set gcp:project <your gcp project id>

pulumi login --cloud-url https://api.pulumi.com

pulumi stack init sharedvpc-psa
Created stack 'sharedvpc-psa'

NAME            LAST UPDATE  RESOURCE COUNT  URL
sharedvpc-psa*  n/a          n/a             https://app.pulumi.com/somaz94/shared-vpc/sharedvpc-psa

```

Sets the variable.
```bash
pulumi config set gcp:project <your gcp project id>
pulumi config set --plaintext host_project somaz
pulumi config set --plaintext service_projects '["dev-somaz", "qa-somaz"]'
```


