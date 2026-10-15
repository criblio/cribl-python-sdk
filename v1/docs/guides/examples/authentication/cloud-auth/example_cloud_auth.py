"""Cribl.Cloud OAuth2 client credentials flow."""
import asyncio
import os

from cribl_python_sdk import Cribl, Security


async def main() -> None:
    # OAuth2 client credentials — SDK fetches and refreshes the token automatically.
    # token_url and audience default to Cribl Cloud values from the OpenAPI spec.
    cribl = Cribl(
        server_url=os.getenv("CRIBL_CLOUD_URL", "https://your-workspace.cribl.cloud"),
        security=Security(
            client_id=os.getenv("CRIBL_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBL_CLIENT_SECRET", ""),
        ),
    )

    # List pipelines (async)
    resp = await cribl.pipelines.list_async()
    print(f"Found {resp.data.count} pipeline(s)")
    for p in resp.data.items:
        print(f"  - {p.id} (output: {p.conf.get('output', '-')})")

    # Health check
    health = await cribl.health.get_async()
    print(f"\nHealth: {health.data.status}")

    await cribl.close_async()


if __name__ == "__main__":
    asyncio.run(main())
