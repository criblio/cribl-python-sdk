"""
Configure Resources — create source, destination, pipeline, route in a Worker Group.

NOTE: This example is for Cribl.Cloud deployments only.

Required:
- CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET env vars
- CRIBL_CLOUD_URL env var
- AWS credentials for the S3 destination
"""
import asyncio
import os

from cribl_python_sdk import Cribl, Security
from cribl_python_sdk.models import InputSyslog, OutputS3


CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")
WORKER_GROUP_ID = os.getenv("CRIBL_WORKER_GROUP_ID", "my-group")
AWS_API_KEY = os.getenv("AWS_ACCESS_KEY_ID", "your-aws-key")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your-aws-secret")
AWS_BUCKET = os.getenv("AWS_BUCKET_NAME", "your-bucket")
AWS_REGION = os.getenv("AWS_REGION", "us-east-2")


async def main():
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        ),
    )

    # Create worker group
    cribl.groups.create(
        id=WORKER_GROUP_ID,
        name=WORKER_GROUP_ID,
        onPrem=False,
    )
    print(f"Worker Group created: {WORKER_GROUP_ID}")

    with cribl.in_context(group_id=WORKER_GROUP_ID) as wg:
        # Syslog source
        wg.sources.create(InputSyslog.model_validate({"id": "in-syslog-9021", "type": "syslog", "host": "0.0.0.0", "port": 9021}))
        print("Syslog source created: in-syslog-9021")

        # S3 destination
        wg.destinations.create(OutputS3.model_validate({
            "id": "out_s3",
            "type": "s3",
            "bucket": AWS_BUCKET,
            "stagePath": "/tmp/cribl_stage",
            "region": AWS_REGION,
            "awsSecretKey": AWS_SECRET_KEY,
            "awsApiKey": AWS_API_KEY,
            "compress": "gzip",
        }))
        print("S3 destination created: out_s3")

        # Pipeline with eval function
        wg.pipelines.create(
            id="my_pipeline",
            conf={
                "asyncFuncTimeout": 1000,
                "functions": [
                    {
                        "id": "eval",
                        "filter": "true",
                        "conf": {"remove": ["*"], "keep": ["eventSource", "eventID"]},
                        "final": True,
                    }
                ],
            },
        )
        print("Pipeline created: my_pipeline")

        # Add a route to the default routing table
        wg.routes.append(
            "default",
            routes=[{
                "name": "my_route",
                "filter": "__inputId=='in-syslog-9021'",
                "pipeline": "my_pipeline",
                "output": "out_s3",
                "description": "Route syslog to S3",
                "final": True,
            }],
        )
        print("Route added")

        # Commit and deploy
        resp = wg.versioning.commits.create(message="Configure resources", effective=True)
        commit = resp.data.items[0]
        print(f"Committed: {commit.commit}")

    assert commit.commit is not None
    cribl.groups.deploy(id=WORKER_GROUP_ID, version=commit.commit)
    print(f"Deployed: {WORKER_GROUP_ID}")

    await cribl.close_async()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {error}")
