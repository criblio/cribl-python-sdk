"""Scoped operations — access resources within a worker group context."""
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

    # Get first worker group
    resp = cribl.groups.list(product="stream")
    if not resp.data.items:
        print("No worker groups found")
        return
    print(f"Using worker group: {resp.data.items[0].id}")

    # Scope the client — all subsequent calls route to /m/{group_id}
    with cribl.in_context(group_id=resp.data.items[0].id) as wg:
        # List sources in this group
        resp = wg.sources.list()
        print(f"\nSources ({resp.data.count}):")
        for s in resp.data.items:
            print(f"  {s.id}: {s.type}")

        # List destinations in this group
        resp = wg.destinations.list()
        print(f"\nDestinations ({resp.data.count}):")
        for d in resp.data.items:
            print(f"  {d.id}: {d.type}")

        # List pipelines in this group
        resp = wg.pipelines.list()
        print(f"\nPipelines ({resp.data.count}):")
        for p in resp.data.items:
            print(f"  {p.id}")

        # Create a pipeline (flattened kwargs — no model class needed)
        resp = wg.pipelines.create(
            id="sdk_test_pipeline",
            conf={"functions": [{"id": "comment", "conf": {"comment": "Created by SDK"}}]},
        )
        print(f"\nCreated pipeline: {resp.data.items[0].id}")

        # Clean up
        wg.pipelines.delete("sdk_test_pipeline")
        print("Deleted test pipeline")

    cribl.close()
if __name__ == "__main__":
    main()
