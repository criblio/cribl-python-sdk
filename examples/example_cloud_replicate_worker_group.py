"""
Replicate a Worker Group — clone configuration from an existing group.

NOTE: This example is for Cribl.Cloud deployments only.

Required:
- CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET env vars
- CRIBL_CLOUD_URL env var
- An existing source Worker Group
"""
import asyncio
import os

from cribl_python_sdk import Cribl, Security


CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")
SOURCE_GROUP = os.getenv("CRIBL_SOURCE_GROUP", "my-worker-group")
REPLICA_GROUP = os.getenv("CRIBL_REPLICA_GROUP", "my-replica-group")


async def main():
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        ),
    )

    cribl.groups.create(
        id=REPLICA_GROUP,
        name="my-replica-worker-group",
        description=f"Cloned from {SOURCE_GROUP}",
        onPrem=False,
        workerRemoteAccess=True,
        sourceGroupId=SOURCE_GROUP,
    )
    print(f"Replicated: {REPLICA_GROUP} (from {SOURCE_GROUP})")

    with cribl.in_context(group_id=REPLICA_GROUP) as wg:
        resp = wg.versioning.commits.create(
            message="Commit for replicate Worker Group",
            effective=True,
        )
        commit = resp.data.items[0]

    assert commit.commit is not None
    cribl.groups.deploy(id=REPLICA_GROUP, version=commit.commit)
    print(f"Deployed: {REPLICA_GROUP}")

    await cribl.close_async()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {error}")
