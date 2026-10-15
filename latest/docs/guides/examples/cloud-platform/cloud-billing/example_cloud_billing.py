"""
Cribl.Cloud billing example.

Prints the Organization's credit balance and lists its credit grants.

NOTE: This example is for Cribl.Cloud only. It calls `cribl.cloud.billing.*` (gateway),
not the control-plane `/api/v1` APIs.

Required:
- CRIBL_CLIENT_ID, CRIBL_CLIENT_SECRET
- CRIBL_ORGANIZATION_ID
- CRIBL_CLOUD_URL (workspace origin; still required by the client constructor)

To get Client ID and Secret:
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud
"""
import asyncio
import os

from cribl_python_sdk import APIError, Cribl, Security

CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
ORG_ID = os.getenv("CRIBL_ORGANIZATION_ID", "your-org-id")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")


async def main() -> None:
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(client_id=CLIENT_ID, client_secret=CLIENT_SECRET),
    )
    try:
        stats = await cribl.cloud.billing.credits.stats.list_async(ORG_ID)
        print(f"Credits used: {stats.data.totalCreditsUsed}, remaining: {stats.data.totalCreditsRemaining}")

        grants = await cribl.cloud.billing.credits.grants.list_async(ORG_ID)
        for grant in grants.data.items:
            print(f"  - {grant.date}: {grant.creditsAcquired} credits ({grant.type})")
    except APIError as exc:
        print(f"Request failed: {exc.message}")
    finally:
        await cribl.close_async()


if __name__ == "__main__":
    asyncio.run(main())
