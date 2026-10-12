"""
Replicate a Worker Group — clone from an existing group.

NOTE: This example is for on-prem deployments only.

Required:
- CRIBL_SERVER_URL, CRIBL_USERNAME, CRIBL_PASSWORD env vars
- An existing source Worker Group
"""
import asyncio
import os

from cribl_python_sdk import Cribl, Security
SERVER_URL = os.getenv("CRIBL_SERVER_URL", "http://localhost:9000")
USERNAME = os.getenv("CRIBL_USERNAME", "admin")
PASSWORD = os.getenv("CRIBL_PASSWORD", "admin")
SOURCE_GROUP = os.getenv("CRIBL_SOURCE_GROUP", "my-worker-group")
REPLICA_GROUP = os.getenv("CRIBL_REPLICA_GROUP", "my-replica-group")
async def main():
    cribl = Cribl(server_url=SERVER_URL)
    token = cribl.auth.tokens.get(username=USERNAME, password=PASSWORD)
    
    cribl = Cribl(
        server_url=SERVER_URL,
        security=Security(bearer_auth=token.data.token),
    )

    cribl.groups.create(
        id=REPLICA_GROUP,
        name="my-replica-worker-group",
        description=f"Cloned from {SOURCE_GROUP}",
        onPrem=True,
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

    cribl.close()
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {error}")
