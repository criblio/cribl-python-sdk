# cribl-python-sdk

Python SDK for the Cribl **Control Plane** API and the **Cribl.Cloud platform** (management) API.

| API surface | Purpose | API Reference |
|-------------|---------|---------------|
| Control Plane | Manage product resources, such as Pipelines, Sources, Destinations, and Worker Groups. Available in Cloud and on-prem deployments. | [Control Plane API](https://docs.cribl.io/cribl-as-code/api-reference/control-plane/) |
| Management Plane | Manage Cribl.Cloud Organizations, Workspaces, and other administrative resources. Cloud-only. | [Management Plane API](https://docs.cribl.io/cribl-as-code/api-reference/management-plane/) |

For more information about the distinction between these API surfaces, see [Control Plane and Management Plane](https://docs.cribl.io/cribl-as-code/api-reference/) in the official Cribl documentation.

Same `Security` (OAuth2 client credentials) for both Cloud hosts. On-prem username/password authenticates the control plane only.

## Table of Contents

* [Install](#install)
* [Quickstart](#quickstart)
* [Authentication](#authentication)
* [Scoped Client](#scoped-client)
* [Creating Resources](#creating-resources)
* [Environment Variables](#environment-variables)
* [Available Resources and Operations](#available-resources-and-operations)

## Install

### uv

```bash
uv add cribl-python-sdk
```

### pip

```bash
pip install cribl-python-sdk
```

### poetry

```bash
poetry add cribl-python-sdk
```

### Shell and script usage with uv

Use in a Python shell:

```bash
uvx --from cribl-python-sdk python
```

Standalone script without a project:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "cribl-python-sdk",
# ]
# ///

from cribl_python_sdk import Cribl, Security

cribl = Cribl(
    server_url="http://localhost:9000",
    security=Security(username="admin", password="admin"),
)
print(cribl.health.get().data.status)
```

Run with `uv run script.py`.

## Quickstart

A complete script: check server health, list Worker Groups, then list Sources and Pipelines in one group.
Replace the placeholders with your own values.

### Cribl.Cloud

```python
from cribl_python_sdk import Cribl, Security

with Cribl(
    server_url="https://main-your-org.cribl.cloud",  # your Workspace URL
    security=Security(client_id="your-client-id", client_secret="your-client-secret"),
) as cribl:
    health = cribl.health.get()
    print(f"Server health: {health.data.status}")

    groups = cribl.groups.list()
    print(f"Found {groups.data.count} Worker Group(s)")

    # Control-plane calls scoped to one Worker Group
    with cribl.in_context(group_id="default") as wg:
        print(f"Found {wg.sources.list().data.count} Source(s)")
        print(f"Found {wg.pipelines.list().data.count} Pipeline(s)")

    # Cribl.Cloud platform API: same client, same credentials
    workspaces = cribl.cloud.workspaces.list(organization_id="your-org")
    print(f"Found {len(workspaces.data.items)} Workspace(s)")
```

### On-prem

```python
from cribl_python_sdk import Cribl, Security

with Cribl(
    server_url="http://localhost:9000",  # your Leader URL
    security=Security(username="admin", password="admin"),
) as cribl:
    health = cribl.health.get()
    print(f"Server health: {health.data.status}")

    groups = cribl.groups.list()
    print(f"Found {groups.data.count} Worker Group(s)")

    # Control-plane calls scoped to one Worker Group
    with cribl.in_context(group_id="default") as wg:
        print(f"Found {wg.sources.list().data.count} Source(s)")
        print(f"Found {wg.pipelines.list().data.count} Pipeline(s)")
```

### Async

Every method has an `_async` twin. Use `async with` inside a coroutine and run it with `asyncio.run()`:

```python
import asyncio

from cribl_python_sdk import Cribl, Security


async def main() -> None:
    async with Cribl(
        server_url="http://localhost:9000",
        security=Security(username="admin", password="admin"),
    ) as cribl:
        health = await cribl.health.get_async()
        print(f"Server health: {health.data.status}")

        groups = await cribl.groups.list_async()
        print(f"Found {groups.data.count} Worker Group(s)")


asyncio.run(main())
```

See `examples/` for more usage patterns.

## Authentication

The SDK handles token acquisition and refresh automatically: pass credentials once in `Security(...)`
and the client manages the rest. Every snippet below plugs into `Cribl(server_url=..., security=security)`
as in the [Quickstart](#quickstart).

| Deployment | `Security(...)` | Authenticates |
|------------|-----------------|---------------|
| On-prem | `username=`, `password=` | Control plane |
| Cribl.Cloud | `client_id=`, `client_secret=` | Control plane and `cribl.cloud.*` |
| Any | `bearer_auth=` | Whatever the token is valid for |

### On-Prem (username/password)

The client calls `POST /auth/login` internally, stores the JWT, and refreshes it before expiry.

```python
from cribl_python_sdk import Security

security = Security(username="admin", password="admin")
```

### Cloud — Control Plane (OAuth2)

OAuth2 client credentials flow. The SDK fetches and refreshes the access token automatically.

```python
from cribl_python_sdk import Security

security = Security(client_id="your-client-id", client_secret="your-client-secret")
```

### Cloud — Management Plane (`cribl.cloud.*`)

Same client, same credentials. Management plane operations live under the `cribl.cloud.*` namespace and
route to the gateway (`https://gateway.cribl.cloud` by default), while control-plane calls go to `server_url`.

### Pre-existing Bearer Token

If you already have a token (e.g. from an external auth flow), pass it directly — no auto-login or refresh:

```python
from cribl_python_sdk import Security

security = Security(bearer_auth="your-token")
```

## Scoped Client

Instead of manually constructing group/node URLs, use `in_context()`. Control-plane calls route to
`/api/v1/m/{group_id}` automatically; `cribl.cloud.*` is unchanged (still the gateway).

```python
from cribl_python_sdk import Cribl, Security

with Cribl(
    server_url="http://localhost:9000",
    security=Security(username="admin", password="admin"),
) as cribl, cribl.in_context(group_id="my_fleet") as wg:
    sources = wg.sources.list()
    destinations = wg.destinations.list()
    pipelines = wg.pipelines.list()
```

## Creating Resources

Pipelines take explicit keyword arguments:

```python
from cribl_python_sdk import Cribl, Security

with Cribl(
    server_url="http://localhost:9000",
    security=Security(username="admin", password="admin"),
) as cribl, cribl.in_context(group_id="default") as wg:
    wg.pipelines.create(id="my_pipe", conf={"functions": []})
```

Sources, Destinations and Collectors accept either a typed model or a plain dict. Pick one:

### Typed model

```python
from cribl_python_sdk import Cribl, Security
from cribl_python_sdk.models.inputs import InputSyslog

with Cribl(
    server_url="http://localhost:9000",
    security=Security(username="admin", password="admin"),
) as cribl, cribl.in_context(group_id="default") as wg:
    wg.sources.create(InputSyslog(id="syslog_typed", host="0.0.0.0", udpPort=514))
```

### Plain dict

```python
from cribl_python_sdk import Cribl, Security

with Cribl(
    server_url="http://localhost:9000",
    security=Security(username="admin", password="admin"),
) as cribl, cribl.in_context(group_id="default") as wg:
    wg.sources.create({"id": "syslog_dict", "type": "syslog", "host": "0.0.0.0", "udpPort": 514})
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `CRIBL_SERVER_URL` | On-prem server origin (e.g. `http://localhost:9000`) |
| `CRIBL_USERNAME` | On-prem login username |
| `CRIBL_PASSWORD` | On-prem login password |
| `CRIBL_CLOUD_URL` | Cribl.Cloud workspace origin for the control plane (e.g. `https://main-your-org.cribl.cloud`) |
| `CRIBL_CLOUD_GATEWAY_URL` | Platform/mgmt gateway override (default: `https://gateway.cribl.cloud`) |
| `CRIBL_CLIENT_ID` | OAuth2 client ID (Cloud control plane + `cribl.cloud.*`) |
| `CRIBL_CLIENT_SECRET` | OAuth2 client secret (Cloud control plane + `cribl.cloud.*`) |
| `CRIBL_AUDIENCE` | OAuth2 audience (default: `https://api.cribl.cloud` from spec) |
| `CRIBL_TOKEN_URL` | OAuth2 token endpoint (default: `https://login.cribl.cloud/oauth/token` from spec) |
| `CRIBL_WORKER_GROUP_ID` | Target worker group ID |
| `CRIBL_ORGANIZATION_ID` | Cribl.Cloud organization id for `cribl.cloud.*` examples |
| `CRIBL_SDK_DEBUG` | Set to `true` to enable debug logging (zero-code activation) |

## Available Resources and Operations

All methods have sync + async variants (append `_async` to method name).

<details open>
<summary>Available methods</summary>

### Cloud

Cribl.Cloud platform API (`openapi/management-plane.yml`). Calls use the gateway, not `/api/v1`.

#### Cloud.Health

* `get` - Get the health status of the application

#### Cloud.ApiCredentials

* `list` - List API Credentials for an Organization
* `create` - Create an API Credential
* `get` - Get an API Credential
* `update` - Update an API Credential
* `delete` - Delete an API Credential

#### Cloud.Workspaces

* `list` - List all Workspaces for the specified Organization
* `create` - Create a Workspace in the specified Organization
* `get` - Get a Workspace
* `update` - Update a Workspace
* `delete` - Delete a Workspace

#### Cloud.Billing.Credits.ContractsUtilization

* `list` - Get contract credit utilization

#### Cloud.Billing.Credits.Timeseries

* `list` - Get credits timeseries

#### Cloud.Billing.Credits.Stats

* `list` - Get credit balance and consumption

#### Cloud.Billing.Credits.Grants

* `list` - Get credit grants

### Auth

#### Auth.Tokens

* `get` - Log in and fetch an authentication token

### Collectors

* `list` - List all Collectors
* `create` - Create a Collector
* `get` - Get a Collector
* `update` - Update a Collector
* `delete` - Delete a Collector

### DatabaseConnections

* `list` - List all Database Connections
* `create` - Create a Database Connection
* `get` - Get a Database Connection
* `update` - Update a Database Connection
* `delete` - Delete a Database Connection

### Datasets

* `list` - List all Lake Datasets (Cribl.Cloud only)
* `create` - Create a Lake Dataset (Cribl.Cloud only)
* `get` - Get a Lake Dataset (Cribl.Cloud only)
* `update` - Update a Lake Dataset (Cribl.Cloud only)
* `delete` - Delete a Lake Dataset (Cribl.Cloud only)

### Destinations

* `list` - List all Destinations
* `create` - Create a Destination
* `get` - Get a Destination
* `update` - Update a Destination
* `delete` - Delete a Destination

#### Destinations.Pq

* `get` - Get persistent queue info for a Destination
* `clear` - Clear the persistent queue for a Destination

#### Destinations.Samples

* `get` - Get sample event data for a Destination
* `create` - Send sample event data to a Destination

#### Destinations.Statuses

* `list` - List the status of all Destinations
* `get` - Get the status of a Destination

### Functions

* `list` - List all Functions
* `get` - Get a Function

### Groups

* `list` - List all Worker Groups, Outpost Groups, or Edge Fleets
* `create` - Create a Worker Group, Outpost Group, or Edge Fleet
* `get` - Get a Worker Group, Outpost Group, or Edge Fleet
* `update` - Update a Worker Group, Outpost Group, or Edge Fleet
* `delete` - Delete a Worker Group, Outpost Group, or Edge Fleet
* `deploy` - Deploy commits to a Worker Group, Outpost Group, or Edge Fleet

#### Groups.Acl

* `get` - Get the Access Control List for a Worker Group

#### Groups.Acl.Teams

* `get` - Get the Access Control List for teams with permissions on a Worker Group

#### Groups.Configs.Versions

* `get` - Get the configuration version for a Worker Group

### Health

* `get` - Get the health status of the server

### Nodes

* `list` - Get detailed metadata for Worker, Edge, or Outpost Nodes
* `get` - Get detailed metadata for a Node
* `restart` - Restart Worker, Edge, or Outpost Nodes
* `count` - Get a count of Worker, Edge, or Outpost Nodes

#### Nodes.Summaries

* `get` - Get a summary of the deployment for a Cribl product

### Packs

* `list` - List all Packs
* `install` - Install a Pack
* `upload` - Upload a Pack file
* `get` - Get a Pack
* `upgrade` - Upgrade a Pack
* `uninstall` - Uninstall a Pack

### Pipelines

* `list` - List all Pipelines
* `create` - Create a Pipeline
* `get` - Get a Pipeline
* `update` - Update a Pipeline
* `delete` - Delete a Pipeline

### Routes

* `list` - List all Routes
* `get` - Get a Routing table
* `update` - Update a Routing table
* `append` - Add a Route to the end of the Routing table

### Sources

* `list` - List all Sources
* `create` - Create a Source
* `get` - Get a Source
* `update` - Update a Source
* `delete` - Delete a Source

#### Sources.HecTokens

* `create` - Add an HEC token to a Splunk HEC Source
* `update` - Update metadata for an HEC token

#### Sources.Pq

* `get` - Get persistent queue info for a Source
* `clear` - Clear the persistent queue for a Source

#### Sources.Statuses

* `list` - List the status of all Sources
* `get` - Get the status of a Source

### System

#### System.Captures

* `create` - Capture live data (NDJSON stream)

#### System.Settings

* `restart` - Restart the Cribl server

#### System.Settings.Cribl

* `list` - Get system settings
* `update` - Update system settings

### Versioning

#### Versions.Branches

* `list` - List all branches in the Git repository
* `get` - Get the active Git branch name

#### Versions.Commits

* `list` - List the commit history
* `create` - Create a new commit for pending changes
* `diff` - Get the diff for a commit
* `push` - Push local commits to the remote repository
* `revert` - Revert a commit in the local repository
* `get` - Get the diff and log message for a commit
* `undo` - Discard uncommitted (staged) changes

#### Versions.Commits.Files

* `count` - Get a count of files changed since a commit
* `list` - Get names and statuses of files changed since a commit

#### Versions.Configs

* `get` - Get Git integration configuration and status

#### Versions.Statuses

* `get` - Get the status of the current working tree

</details>
