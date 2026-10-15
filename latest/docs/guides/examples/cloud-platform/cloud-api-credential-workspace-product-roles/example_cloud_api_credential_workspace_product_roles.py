"""
Create a Cribl.Cloud API Credential (Organization/Workspace User, Product Editor).

Creates a new API Credential with:
- User role on the Organization and the `main` Workspace
- Editor on all Cribl products in the `main` Workspace
- An optional IP allowlist

NOTE: This example is for Cribl.Cloud only (`cribl.cloud.api_credentials`).

Required:
- CRIBL_CLIENT_ID, CRIBL_CLIENT_SECRET (an existing API Credential, to authenticate)
- CRIBL_ORGANIZATION_ID
- CRIBL_CLOUD_URL (workspace origin; still required by the client constructor)

The create response includes clientSecret once. Do not print or log it.

https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud
"""
import os

from cribl_python_sdk import APIError, AuthenticationError, Cribl, RateLimitError, Security
from cribl_python_sdk.models import ApiCredentialRolesParam, ProductName

CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
ORG_ID = os.getenv("CRIBL_ORGANIZATION_ID", "your-org-id")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")
IP_ALLOWLIST = ["203.0.113.0/24"]

ALL_CRIBL_PRODUCTS: tuple[ProductName, ...] = ("stream", "search", "lake", "edge", "insights")


def main() -> None:
    roles: ApiCredentialRolesParam = {
        "organizationRole": "user",
        "workspaces": [
            {
                "workspaceId": "main",
                "workspaceRole": "user",
                "products": [
                    {"product": product, "role": "editor"}
                    for product in ALL_CRIBL_PRODUCTS
                ],
            }
        ],
    }

    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(client_id=CLIENT_ID, client_secret=CLIENT_SECRET),
    )
    try:
        resp = cribl.cloud.api_credentials.create(
            ORG_ID,
            name="Product-Editor",
            description="Editor Role on all Cribl Products",
            enabled=True,
            roles=roles,
            ipAllowlist=IP_ALLOWLIST,
        )
        cred = resp.data
        print(f"Created API Credential name={cred.name!r} clientId={cred.clientId!r}")
    except AuthenticationError:
        print("Authentication failed. Check CRIBL_CLIENT_ID and CRIBL_CLIENT_SECRET.")
    except RateLimitError:
        print("Rate limit reached. Try again in a few seconds.")
    except APIError as exc:
        print(f"Request failed: {exc.message}")
    finally:
        cribl.close()


if __name__ == "__main__":
    main()
