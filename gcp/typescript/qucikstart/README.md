## Create Project
Begin by setting up a new Pulumi project using the GCP Typescript template. 

```bash

# Node Install
sudo apt install npm

curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

sudo npm install latest

node -v
v18.17.1

# Create Directory and Initialize
mkdir quickstart && cd quickstart && pulumi new gcp-typescript

```

<br/>

## Review Project
Once your project is set up, review the generated files to understand the structure.

```bash
ls
Pulumi.yaml  index.ts  node_modules  package-lock.json  package.json  tsconfig.json
```

`Pulumi.yaml`: This file describes your Pulumi project, including the runtime and some metadata.

```bash
name: qucikstart
runtime: nodejs
description: A minimal Google Cloud TypeScript Pulumi program
```

`index.ts`: This is your main program file. Here's an example of its content, which creates a GCP storage bucket:
```bash
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("somaz-bucket", {
    name: "somaz-bucket",
    location: "asia-northeast3",
    uniformBucketLevelAccess: true
});

// Create a new object in the bucket
const bucketObject = new gcp.storage.BucketObject("index.html", {
    name: "index.html",
    bucket: bucket.name,
    source: new pulumi.asset.FileAsset("index.html")
});

// Create a bucket IAM binding to allow all users to view the object
const bucketBinding = new gcp.storage.BucketIAMBinding("somaz-bucket-binding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"]
});

// Export just the bucket name
export const bucketName = bucket.name;

// Construct the object URL for HTTP access
const bucketObjectUrl = pulumi.interpolate`https://storage.googleapis.com/${bucket.name}/${bucketObject.name}`;

// Export the object URL
export const bucketObjectEndpoint = bucketObjectUrl;

// Export the bucket IAM binding ID
export const bucketBindingName = bucketBinding.id;
```

`index.html`: This might be a placeholder or a sample HTML file. Ensure to review and modify it as per your project's needs.

<br/>

# Reference
- [Get started with Pulumi & Google Cloud](https://www.pulumi.com/docs/clouds/gcp/get-started/#get-started-with-pulumi-google-cloud)
