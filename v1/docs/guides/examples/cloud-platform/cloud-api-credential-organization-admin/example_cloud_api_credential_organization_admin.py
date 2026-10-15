"""
Create a Cribl.Cloud API Credential (Organization Admin).

Creates a new API Credential with the Admin role on the Organization. That role
applies across the Organization, including all Workspaces and products (no
Workspace or product matrix is required).

NOTE: This example is for Cribl.Cloud only (`cribl.cloud.api_credentials`).

Required:
- CRIBL_CLIENT_ID, CRIBL_CLIENT_SECRET (an existing API Credential, to authenticate)
- CRIBL_ORGANIZATION_ID
- CRIBL_CLOUD_URL (workspace origin; still required by the client constructor)

The create response includes clientSecret once. Do not print or log it. Store it
securely if you will use the new credential later.

https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud
"""
import os

from cribl_python_sdk import APIError, AuthenticationError, Cribl, RateLimitError, Security

CLIENT_ID = os.getenv("CRIBL_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CRIBL_CLIENT_SECRET", "your-client-secret")
ORG_ID = os.getenv("CRIBL_ORGANIZATION_ID", "your-org-id")
CLOUD_URL = os.getenv("CRIBL_CLOUD_URL", "https://main-your-org.cribl.cloud")
IP_ALLOWLIST = ["203.0.113.0/24"]


def main() -> None:
    cribl = Cribl(
        server_url=CLOUD_URL,
        security=Security(client_id=CLIENT_ID, client_secret=CLIENT_SECRET),
    )
    try:
        resp = cribl.cloud.api_credentials.create(
            ORG_ID,
            name="Auto-Manage-Workspaces",
            description="Used for automated Workspace management",
            enabled=True,
            roles={"organizationRole": "admin"},
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
