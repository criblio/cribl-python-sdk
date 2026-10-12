# cribl-python-sdk

Python SDK for the Cribl Control Plane API (`openapi/control-plane.yml`, v4.20.0) and the Cribl.Cloud platform API (`openapi/management-plane.yml`). One client: control plane on `server_url` + `/api/v1`; platform on `cribl.cloud.*` (gateway, default `https://gateway.cribl.cloud`). Same OAuth `Security` for both Cloud hosts.

## Install

```bash
pip install -e .
```

## Quickstart

```python
from cribl_python_sdk import Cribl, Security

# On-prem: login with username/password
cribl = Cribl(server_url="http://localhost:9000")
token = cribl.auth.tokens.get(username="admin", password="admin")

# Create authenticated client
cribl = Cribl(
    server_url="http://localhost:9000",
    security=Security(bearer_auth=token.token),
)

# List pipelines (sync)
pipelines = cribl.pipelines.list()

# Async variant
pipelines = await cribl.pipelines.list_async()

# Scoped to a worker group
wg = cribl.scoped(group_id="default")
sources = wg.sources.list()
```

## Scoped Client

Instead of manually constructing group/node URLs, use `scoped()`:

```python
# All calls route to /api/v1/m/{group_id} automatically
wg = cribl.scoped(group_id="my_fleet")
sources = wg.sources.list()
destinations = wg.destinations.list()
pipelines = wg.pipelines.list()

# Also works as context manager
with cribl.scoped(group_id="my_fleet") as wg:
    sources = wg.sources.list()
```

## Flattened Kwargs (No Model Import Needed)

Methods accept body fields as keyword arguments — you never need to import or construct model classes:

```python
# Just pass kwargs — the SDK builds the request body
cribl.pipelines.create(id="my_pipe", conf={"functions": []})
cribl.sources.create(id="syslog:in", type="syslog", host="0.0.0.0", port=514)
```

## Resources

| Resource | Methods |
|----------|---------|
| `cribl.auth.tokens` | get |
| `cribl.health` | get |
| `cribl.cloud.health` | get |
| `cribl.cloud.api_credentials` | list, create, get, update, delete |
| `cribl.cloud.workspaces` | list, create, get, update, delete |
| `cribl.cloud.billing.credits.contracts_utilization` | list |
| `cribl.cloud.billing.credits.timeseries` | list |
| `cribl.cloud.billing.credits.stats` | list |
| `cribl.cloud.billing.credits.grants` | list |
| `cribl.functions` | list, get |
| `cribl.pipelines` | list, get, create, update, delete |
| `cribl.routes` | list, get, update, append |
| `cribl.sources` | list, get, create, update, delete |
| `cribl.sources.hec_tokens` | create, update |
| `cribl.sources.pq` | get, clear |
| `cribl.sources.statuses` | list, get |
| `cribl.destinations` | list, get, create, update, delete, test |
| `cribl.destinations.pq` | get, clear |
| `cribl.destinations.samples` | get, create |
| `cribl.destinations.statuses` | list, get |
| `cribl.packs` | list, get, install, upload, upgrade, uninstall |
| `cribl.collectors` | list, get, create, update, delete |
| `cribl.database_connections` | list, get, create, update, delete |
| `cribl.groups` | list, get, create, update, delete, deploy |
| `cribl.nodes` | list, get, restart, count |
| `cribl.nodes.summaries` | get |
| `cribl.datasets` | list, get, create, update, delete |
| `cribl.system.captures` | create |
| `cribl.system.settings` | restart |
| `cribl.system.settings.cribl` | list, update |
| `cribl.versioning.branches` | list, get |
| `cribl.versioning.commits` | list, create, diff, push, revert, get, undo |
| `cribl.versioning.commits.files` | count, list |
| `cribl.versioning.configs` | get |
| `cribl.versioning.statuses` | get |

All methods have sync + async variants (append `_async` to method name).
