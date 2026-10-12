"""
Scale (provision) a Worker Group — update estimated ingest rate.

NOTE: This example is for Cribl.Cloud deployments only.

Required:
- CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET env vars
- CRIBL_CLOUD_URL env var
- An existing Worker Group to scale
"""
import asyncio
import os

from cribl_python_sdk import Cribl, Security


CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")
WORKER_GROUP_ID = os.getenv("CRIBL_WORKER_GROUP_ID", "my-worker-group")


async def main():
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        ),
    )

    # Scale up: update ingest rate and mark provisioned
    cribl.groups.update(
        id=WORKER_GROUP_ID,
        estimatedIngestRate=4096,  # 48 MB/sec
        provisioned=True,
    )
    print(f"Scaled: {WORKER_GROUP_ID} to 48 MB/s")

    with cribl.in_context(group_id=WORKER_GROUP_ID) as wg:
        resp = wg.versioning.commits.create(
            message="Scale Worker Group",
            effective=True,
        )
        commit = resp.data.items[0]

    assert commit.commit is not None
    cribl.groups.deploy(id=WORKER_GROUP_ID, version=commit.commit)
    print(f"Deployed: {WORKER_GROUP_ID}")

    await cribl.close_async()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {error}")
