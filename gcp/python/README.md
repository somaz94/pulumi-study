# GCP Pulumi Study with Python

This repository contains a collection of Pulumi projects written in Python that aim to demonstrate various Google Cloud Platform (GCP) capabilities.

<br/>

## Projects

- **artifact-registry**: Demonstrates how to set up and manage an Artifact Registry.
- **bigdata-flow-functions**: Contains various scripts and functions to facilitate data flow between BigData platforms and tools such as MongoDB, BigQuery, and Google Sheets on Google Cloud Platform (GCP).
- **cloud-armor**: An example project showcasing the setup and use of Cloud Armor, a distributed denial-of-service (DDoS) defense and web application firewall (WAF) service.
- **cloud-dns-cdn**: A project illustrating the integration between Cloud DNS and Google's Content Delivery Network (CDN).
- **cloud-run**: Demonstrates how to deploy a Docker container to Google Cloud Run using Pulumi and Python. This project focuses on leveraging Cloud Run's serverless capabilities to run containers without the overhead of infrastructure management.
- **cloud-run-domain-mapping**: Demonstrates how to map custom domains to services running on Google Cloud Run using Pulumi and Python.
- **cloudsql-memorystore**: Showcases the setup and connection between CloudSQL and MemoryStore for enhanced caching capabilities.
- **common**: Shared utility module (`utils.py`) defining the canonical `Utils.resource_name()` pattern used across all projects.
- **gke-autopilot-public**: A project focused on deploying and managing Kubernetes clusters using GKE's Autopilot mode.
- **managed-gcs-state**: Demonstrates the use of Google Cloud Storage (GCS) for managing state in a Pulumi project.
- **quickstart**: A basic starter project to help you quickly get up and running with Pulumi on GCP using Python.
- **secret-manager**: Showcases the integration and usage of GCP's Secret Manager service.
- **service-account-workload-identity-federation**: A comprehensive project detailing the setup of service accounts, workload identities, and their federation.
- **sharedvpc-psa**: Illustrates the setup and usage of Shared VPCs and Private Service Access within GCP.
- **vpc-gce-gcs**: A project demonstrating the integration between Virtual Private Cloud (VPC), Google Compute Engine (GCE), and Google Cloud Storage (GCS).

<br/>

## Project Convention

All projects follow a consistent structure:

- `config.py` — Project-specific constants (`PREFIX`, `REGION`, etc.). Sensitive values should use environment variables or `pulumi.Config`.
- `utils.py` — Uses the standardized `Utils.resource_name()` static method for prefixed resource naming.
- `__main__.py` — Pulumi program entry point.

<br/>

## Getting Started

To work on any of the above projects:

1. Navigate to the desired project directory.
2. Initialize a new Pulumi stack using the command:
```bash
pulumi stack init <stack name>
```
3. Install the required Python dependencies using `pip install -r requirements.txt`.
4. Follow the specific README instructions (if available) within the chosen directory.

<br/>

## Prerequisites

- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- Python 3.6 or later
- An active Google Cloud Platform (GCP) account

<br/>

## Reference

- [Pulumi GCP API Docs](https://www.pulumi.com/registry/packages/gcp/api-docs)

<br/>

**Note**: Always ensure you are working in a virtual environment when running Pulumi Python projects to avoid any potential package conflicts.
