# Pulumi GCP Artifact Registry Setup
This project contains Pulumi code for setting up Google Cloud Platform (GCP) Artifact Registries. Artifact Registries provide a single place for your organization to manage Docker container images, language packages, and other artifacts.

<br/>

## Structure
- `config.ts`: Contains configuration details like prefix, region, and repository names.
- `utils.ts`: Utility class for generating resource names.
- `artifactRegistry.ts`: Pulumi code for creating Artifact Registries on GCP.

<br/>

## Prerequisites
- Node.js and npm installed.
- [Pulumi CLI](https://www.pulumi.com/docs/cli/) installed.
- Configure Pulumi to use [GCP](https://www.pulumi.com/docs/clouds/gcp/setup/).

<br/>

## Usage
1. **Initialize a new Pulumi stack:**
   ```bash
   pulumi stack init [STACK_NAME]
   ```

2. **Set GCP configuration:**
   ```bash
   pulumi config set gcp:project [YOUR_GCP_PROJECT_ID]
   ```

3. **Install Node Modules**
   ```bash
   npm install
   ```

4. **Deploy the Pulumi stack:**
  ```bash
  pulumi up
  ```

<br/>

## Verifying Deployment
After deployment, verify that the Artifact Registries are set up correctly in your GCP console.

<br/>

## Troubleshooting
- Ensure all configurations in `config.ts` are correct.
- Check Pulumi CLI version compatibility with GCP.

<br/>

# Reference
- [GCP Artifact Registry Documentation](https://cloud.google.com/artifact-registry/docs)
- [Pulumi GCP Artifact Registry Package](https://www.pulumi.com/registry/packages/gcp/api-docs/artifactregistry/#gcp-artifactregistry)
