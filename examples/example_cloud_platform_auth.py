"""
Cribl.Cloud platform authentication example.

Validates OAuth2 against the Cribl.Cloud gateway: health check, then list Workspaces.

NOTE: This example is for Cribl.Cloud only. It calls `cribl.cloud.*` (gateway),
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

from cribl_python_sdk import APIError, AuthenticationError, Cribl, RateLimitError, Security

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
        print("Cribl.Cloud platform client created")

        health = await cribl.cloud.health.get_async()
        print(f"Health check passed. Status: {health.data.status or 'unknown'}")

        workspaces = await cribl.cloud.workspaces.list_async(ORG_ID)
        items = workspaces.data.items
        count = workspaces.data.count
        if items:
            print(f"Found {count} Workspace(s):")
        else:
            print(f"No Workspaces found for Organization {ORG_ID}")
        for ws in items:
            alias = f" ({ws.alias})" if ws.alias else ""
            print(f"  - {ws.workspaceId}{alias} - {ws.state} in {ws.region}")
    except AuthenticationError:
        print("Authentication failed. Check CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET.")
    except RateLimitError:
        print("Rate limit reached. Try again in a few seconds.")
    except APIError as exc:
        print(f"Request failed: {exc.message}")
    finally:
        await cribl.close_async()


if __name__ == "__main__":
    asyncio.run(main())
