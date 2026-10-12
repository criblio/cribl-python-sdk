"""
List all Worker Groups in Cribl Stream.

NOTE: This example is for on-prem deployments only.

Required:
- CRIBL_SERVER_URL, CRIBL_USERNAME, CRIBL_PASSWORD env vars
"""
import os

from cribl_python_sdk import Cribl, Security
SERVER_URL = os.getenv("CRIBL_SERVER_URL", "http://localhost:9000")
USERNAME = os.getenv("CRIBL_USERNAME", "admin")
PASSWORD = os.getenv("CRIBL_PASSWORD", "admin")
def main():
    cribl = Cribl(server_url=SERVER_URL)
    token = cribl.auth.tokens.get(username=USERNAME, password=PASSWORD)
    
    cribl = Cribl(
        server_url=SERVER_URL,
        security=Security(bearer_auth=token.data.token),
    )

    resp = cribl.groups.list(product="stream")
    if resp.data.items:
        print(f"Worker Groups ({resp.data.count}):")
        for g in resp.data.items:
            print(f"  {g.id} — {g.description or '(no description)'}")
    else:
        print("No Worker Groups found.")

    cribl.close()
if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
