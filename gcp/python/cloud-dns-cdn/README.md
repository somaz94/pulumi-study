## Preliminary Steps
Set up Cloud DNS & Cloud CDN.

To begin, you can set up the required configurations using the commands provided:
```bash
# Initialize a new stack with your preferred name.
pulumi stack init <STACK_NAME>

# Set your Google Cloud project.
pulumi config set gcp:project <YOUR_GCP_PROJECT_ID>
```
### Handling Potential Errors
Should you encounter the following error, it indicates a domain ownership issue:
```bash
Diagnostics:
  gcp:storage:Bucket (somaz-bucket):
    error: googleapi: Error 403: Another user owns the domain web.gcp.somaz.link or a parent domain...

pulumi:pulumi:Stack (cloud-dns-cdn-somaz):
    error: update failed
```

To resolve this, verify domain ownership in the Google Search Console.
![Verify domain ownership](https://search.google.com/search-console/welcome?new_domain_name=web.gcp.somaz.link)

Alternatively, if you do not own the domain, you may need to reach out to the current owner and request them to create the bucket for you.

### Cleanup
If needed, you can remove resources and the associated stack using:
```bash
pulumi destroy
```

## Completion
Upon successful setup, you should be able to view your configured resources:<br/>
![web-somaz](https://github.com/somaz94/pulumi-study/assets/112675579/0378e4f4-85ee-4d0f-8de8-cd4c5770038f)