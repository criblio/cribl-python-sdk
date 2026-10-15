"""
Create a Worker Group on an on-prem Cribl instance.

NOTE: This example is for on-prem deployments only.

Required:
- CRIBL_SERVER_URL, CRIBL_USERNAME, CRIBL_PASSWORD env vars
"""
import asyncio
import os

from cribl_python_sdk import Cribl, Security
SERVER_URL = os.getenv("CRIBL_SERVER_URL", "http://localhost:9000")
USERNAME = os.getenv("CRIBL_USERNAME", "admin")
PASSWORD = os.getenv("CRIBL_PASSWORD", "admin")
WORKER_GROUP_ID = os.getenv("CRIBL_WORKER_GROUP_ID", "my-worker-group")
async def main():
    cribl = Cribl(server_url=SERVER_URL)
    token = cribl.auth.tokens.get(username=USERNAME, password=PASSWORD)
    
    cribl = Cribl(
        server_url=SERVER_URL,
        security=Security(bearer_auth=token.data.token),
    )

    cribl.groups.create(
        id=WORKER_GROUP_ID,
        name="my-worker-group",
        description="My Worker Group",
        onPrem=True,
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

    cribl.close()
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {error}")
