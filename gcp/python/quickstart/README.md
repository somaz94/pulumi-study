## Create Project

```bash
mkdir quickstart && cd quickstart && pulumi new gcp-python

-bash: pulumi: command not found
...

# Shell Restart
exec bash

# Confirm PATH
echo $PATH

# Reinstall Pulumi
pulumi new gcp-python
```

## Review Project

```bash
ls
Pulumi.dev.yaml  Pulumi.yaml  __main__.py  requirements.txt  venv

cat Pulumi.dev.yaml
config:
  gcp:project: somaz


cat Pulumi.yaml
name: quickstart
runtime:
  name: python
  options:
    virtualenv: venv
description: A minimal Google Cloud Python Pulumi program


cat __main__.py
"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)


cat requirements.txt
pulumi>=3.0.0,<4.0.0
pulumi-gcp>=6.0.0,<7.0.0
```

