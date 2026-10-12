"""
Create a Worker Group and deploy it.

NOTE: This example is for Cribl.Cloud deployments only.

Required:
- CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET env vars
- CRIBL_CLOUD_URL env var
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

    cribl.groups.create(
        id=WORKER_GROUP_ID,
        name="my-worker-group",
        description="Cribl.Cloud Worker Group",
        onPrem=False,
        workerRemoteAccess=True,
    )
    print(f"Worker Group created: {WORKER_GROUP_ID}")

    with cribl.in_context(group_id=WORKER_GROUP_ID) as wg:
        resp = wg.versioning.commits.create(
            message="Commit for create Worker Group",
            effective=True,
        )
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
