#!/usr/bin/env bash
# Release helper.
#
#   scripts/release.sh bump <part>...   bump version, open PR against v1
#                                       e.g. bump alpha | bump patch | bump patch alpha | bump stable
#   scripts/release.sh publish          after the bump PR is merged: tag + GitHub Release (triggers publish.yml)
set -euo pipefail

base=v1

case "${1:-}" in
  bump)
    shift
    [ $# -gt 0 ] || { echo "usage: $0 bump <major|minor|patch|stable|alpha|beta|rc|post|dev>..." >&2; exit 1; }
    [ -z "$(git status --porcelain)" ] || { echo "working tree not clean" >&2; exit 1; }
    bumps=()
    for b in "$@"; do bumps+=(--bump "$b"); done

    git switch -q "$base" && git pull -q --ff-only
    v=$(uv version "${bumps[@]}" --dry-run --short --no-sync)
    git switch -q -c "release/v$v"
    uv version "${bumps[@]}" --no-sync >/dev/null
    git commit -qam "Release v$v"
    git push -q -u origin "release/v$v"
    gh pr create --base "$base" --fill
    ;;
  publish)
    git fetch -q origin "$base"
    v=$(git show "origin/$base:pyproject.toml" | grep -m1 '^version' | cut -d'"' -f2)
    if git ls-remote --exit-code --tags origin "v$v" >/dev/null; then
      echo "tag v$v already exists" >&2; exit 1
    fi
    pre=()
    [[ $v =~ (a|b|rc|\.dev)[0-9]+$ ]] && pre=(--prerelease)
    read -rp "Release v$v from origin/$base${pre:+ (pre-release)}? [y/N] " ok
    [ "$ok" = y ] || exit 1
    gh release create "v$v" --target "$base" --generate-notes \
        --notes "📦 PyPI: https://pypi.org/project/cribl-python-sdk/$v/" ${pre[@]+"${pre[@]}"}
    ;;
  *)
    sed -n '2,6p' "$0" | sed 's/^# \{0,1\}//'
    exit 1
    ;;
esac
