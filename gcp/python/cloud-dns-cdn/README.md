## Advance preparation
Create Cloud DNS & Cloud CDN

You can also create a Secret Config using the commands below.
```bash
pulumi stack init <stack name> # Do it with the stack name you want.

pulumi config set gcp:project <your gcp project id>
```

If the following error occurs, create a bucket after domain authentication in the Google search console.
```bash
Diagnostics:
  gcp:storage:Bucket (somaz-bucket):
    error: 1 error occurred:
        * googleapi: Error 403: Another user owns the domain web.gcp.somaz.link or a parent domain. You can either verify domain ownership at https://search.google.com/search-console/welcome?new_domain_name=web.gcp.somaz.link or find the current owner and ask that person to create the bucket for you, forbidden

  pulumi:pulumi:Stack (cloud-dns-cdn-somaz):
    Error creating bucket web.gcp.somaz.link: googleapi: Error 403: Another user owns the domain web.gcp.somaz.link or a parent domain. You can either verify domain ownership at https://search.google.com/search-console/welcome?new_domain_name=web.gcp.somaz.link or find the current owner and ask that person to create the bucket for you, forbidden

    error: update failed

```

Delete Resource and Stack
```bash
pulumi destroy
```

## Complete
![web-somaz](https://github.com/somaz94/pulumi-study/assets/112675579/0378e4f4-85ee-4d0f-8de8-cd4c5770038f)