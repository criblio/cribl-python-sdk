"""Pack management example."""
import os

from cribl_python_sdk import Cribl, Security
def main() -> None:
    server_url = os.getenv("CRIBL_SERVER_URL", "http://localhost:9000")

    cribl = Cribl(server_url=server_url)
    token = cribl.auth.tokens.get(
        username=os.getenv("CRIBL_USERNAME", "admin"),
        password=os.getenv("CRIBL_PASSWORD", "admin"),
    )
    
    cribl = Cribl(
        server_url=server_url,
        security=Security(bearer_auth=token.data.token),
    )

    # List installed packs
    resp = cribl.packs.list()
    print(f"Installed packs ({resp.data.count}):")
    for p in resp.data.items:
        print(f"  {p.id} v{p.version} — {p.description or '(no description)'}")

    cribl.close()
if __name__ == "__main__":
    main()
