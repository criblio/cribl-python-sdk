"""Fail unless the pyproject version is canonical PEP 440 and, if a tag is given, matches it.

Usage: check_version.py [TAG]
"""

import sys
import tomllib

from packaging.version import InvalidVersion, Version

with open("pyproject.toml", "rb") as f:
    v = tomllib.load(f)["project"]["version"]

try:
    canonical = str(Version(v))
except InvalidVersion:
    sys.exit(f"{v!r} is not a valid PEP 440 version")
if canonical != v:
    sys.exit(f"{v} is not canonical PEP 440 (use {canonical})")

if len(sys.argv) > 1 and sys.argv[1] != f"v{v}":
    sys.exit(f"tag {sys.argv[1]} != v{v}")

print(f"version {v} OK")
