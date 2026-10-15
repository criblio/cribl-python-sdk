"""
List all Worker Groups in Cribl Stream.

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


async def main():
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        ),
    )

    resp = await cribl.groups.list_async(product="stream")
    if resp.data.items:
        print(f"Worker Groups ({resp.data.count}):")
        for g in resp.data.items:
            print(f"  {g.id} — {g.description or '(no description)'}")
    else:
        print("No Worker Groups found.")

    await cribl.close_async()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {error}")
