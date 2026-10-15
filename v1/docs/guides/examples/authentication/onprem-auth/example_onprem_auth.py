"""On-premises login flow — authenticate with username/password, then use the token."""
import os

from cribl_python_sdk import Cribl, Security


def main() -> None:
    server_url = os.getenv("CRIBL_SERVER_URL", "http://localhost:9000")
    username = os.getenv("CRIBL_USERNAME", "admin")
    password = os.getenv("CRIBL_PASSWORD", "admin")

    # Login to get a bearer token
    cribl = Cribl(server_url=server_url)
    token = cribl.auth.tokens.get(username=username, password=password)

    # Create authenticated client (or use set_token)
    cribl = Cribl(
        server_url=server_url,
        security=Security(bearer_auth=token.data.token),
    )

    # List worker groups
    resp = cribl.groups.list(product="stream")
    print(f"Found {resp.data.count} worker group(s)")
    for g in resp.data.items:
        print(f"  - {g.id} ({g.description or 'no description'})")

    # Use in_context client for group-level operations
    if resp.data.items:
        with cribl.in_context(group_id=resp.data.items[0].id) as wg:
            sources = wg.sources.list()
            print(f"\nSources in group '{resp.data.items[0].id}': {sources.data.count}")
            for s in sources.data.items:
                print(f"  - {s.id} ({s.type})")

    cribl.close()


if __name__ == "__main__":
    main()
