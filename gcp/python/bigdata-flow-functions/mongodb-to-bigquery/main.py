import os
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
from flask import jsonify

def start_dataflow(request):
    # Since an HTTP request is a Flask Request object, use the object's methods to analyze the request data.
    # If you need to receive data through a POST request or use a different method, adjust accordingly.

    # Retrieve environment variables
    PROJECT_ID = os.environ.get('PROJECT_ID')
    REGION = os.environ.get('REGION')
    SHARED_VPC = os.environ.get('SHARED_VPC')
    SUBNET_SHARE = os.environ.get('SUBNET_SHARE')
    SERVICE_ACCOUNT_EMAIL = os.environ.get('SERVICE_ACCOUNT_EMAIL')

    # Authenticate with Google Cloud SDK
    credentials = GoogleCredentials.get_application_default()

    # Instantiate a Dataflow API client
    service = build('dataflow', 'v1b3', credentials=credentials)

    databases = ["dev1", "production"]  # Your list of MongoDB databases

    responses = []

    for database in databases:
        # Configuration for Dataflow job parameters
        # Check these links for reference:
        # https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch
        # https://cloud.google.com/dataflow/docs/guides/templates/provided/mongodb-to-bigquery

        job_parameters = {
            "launchParameter": {
                "jobName": f"{database}-to-bigquery-job",
                "parameters": {
                    "mongoDbUri": f"mongodb://mongo:mongo!23@44.44.44.444:27017",  # Format: mongodb://<id>:<pw>@<mongodb ip>:<port>
                    "database": database,
                    "collection": "mongologs",
                    "outputTableSpec": f"{PROJECT_ID}:mongodb_dataset.{database}-mongodb-internal-table", # <project id>:<dataset name>.<database>-<table name>
                    "userOption": "FLATTEN"
                },
                "environment": {
                    "tempLocation": "gs://mongodb-cloud-function-storage/tmp",
                    "network": SHARED_VPC,
                    "subnetwork": f"regions/{REGION}/subnetworks/{SUBNET_SHARE}-mgmt-b",
                    "serviceAccountEmail": SERVICE_ACCOUNT_EMAIL
                },
                "containerSpecGcsPath": 'gs://dataflow-templates/2023-08-29-00_RC00/flex/MongoDB_to_BigQuery' # https://console.cloud.google.com/storage/browser/_details/dataflow-templates/latest/flex/MongoDB_to_BigQuery;tab=live_object?hl=ko
            }
        }

        # Error handling
        try:
            # Launch the Dataflow job
            request = service.projects().locations().flexTemplates().launch(
                projectId=PROJECT_ID,
                location=REGION,
                body=job_parameters
            )
            response = request.execute()
            responses.append(response)

        except Exception as e:
            print(f"Error occurred while processing {database}: {e}")
            responses.append({"database": database, "error": str(e)})

    return jsonify(responses)
