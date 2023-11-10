// // Use Suffix
// import * as pulumi from "@pulumi/pulumi";
// import * as gcp from "@pulumi/gcp";

// // Create a GCP resource (Storage Bucket)
// const bucket = new gcp.storage.Bucket("somaz-bucket", {
//     location: "asia-northeast3"
// });

// // Export the DNS name of the bucket
// export const bucketName = bucket.url;


// Remove Suffix
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
