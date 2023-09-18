## Create Project
Begin by setting up a new Pulumi project using the GCP Python template. If you encounter an error stating pulumi: command not found, you might need to restart your shell or verify the PATH.

```bash
mkdir quickstart
cd quickstart
pulumi new gcp-python

# If the pulumi command isn't found, try the following steps:

# Restart your shell
exec bash

# Confirm PATH includes the location of the Pulumi binary
echo $PATH

# Try creating a new Pulumi project again
pulumi new gcp-python
```

<br/>

## Review Project
Once your project is set up, review the generated files to understand the structure.

```bash
ls
Pulumi.yaml  README.md  __main__.py  index.html  requirements.txt
```

Pulumi.yaml: This file describes your Pulumi project, including the runtime and some metadata.

```bash
name: quickstart
runtime:
  name: python
  options:
    virtualenv: venv
description: A minimal Google Cloud Python Pulumi program
```

main.py: This is your main program file. Here's an example of its content, which creates a GCP storage bucket:
```bash
"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
```

requirements.txt: Lists the Python packages your program depends on.
```bash
pulumi>=3.0.0,<4.0.0
pulumi-gcp>=6.0.0,<7.0.0
```

index.html: This might be a placeholder or a sample HTML file. Ensure to review and modify it as per your project's needs.
