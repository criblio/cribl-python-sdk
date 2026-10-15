"""
Commit and deploy configuration changes for a Worker Group.

NOTE: This example is for Cribl.Cloud deployments only.

Required:
- CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET env vars (OAuth2 API credentials)
- CRIBL_CLOUD_URL env var (workspace URL)
- A Worker Group with pending changes
"""
import asyncio
import os

from cribl_python_sdk import Cribl, Security


CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")
WORKER_GROUP_ID = os.getenv("CRIBL_WORKER_GROUP_ID", "default")


async def main():
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        ),
    )

    with cribl.in_context(group_id=WORKER_GROUP_ID) as wg:
        resp = wg.versioning.commits.create(
            message="Commit for Cribl Stream example",
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
