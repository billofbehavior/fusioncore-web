#!/usr/bin/env bash
# Mirror the SBoB docs from the kubescape.io clone into this Hugo site.
#
# Source of truth: ~/kubescape.io/docs/docs/operator/bill-of-behavior/
# Destination:     ./content/bob/docs/
#
# Authoring happens in the kubescape.io clone (so the diff there IS the
# upstream PR). This script translates MkDocs Material conventions into
# Hugo-compatible markdown:
#
#   !!! note   →   > **Note:** ...      (and similar for warning / tip)
#   ```mermaid →   left as-is; Hugo render hook handles it
#   relative .md links → kept as-is; Hugo respects them
#
# Run from the fusioncore-web repo root. Re-running is idempotent.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SRC="${SRC:-/home/croedig/kubescape.io/docs/docs/operator/bill-of-behavior}"
DST="${DST:-$REPO_ROOT/content/bob/docs}"

if [[ ! -d "$SRC" ]]; then
  echo "Source not found: $SRC" >&2
  echo "Set SRC env var, or clone https://github.com/kubescape/kubescape.io" >&2
  exit 1
fi

mkdir -p "$DST"
python3 "$SCRIPT_DIR/sync-sbob-docs.py" "$SRC" "$DST"
echo "Synced $(ls "$DST"/*.md 2>/dev/null | wc -l) files into $DST"
