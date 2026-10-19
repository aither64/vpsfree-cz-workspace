#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
trap 'build_status=$?; printf "%s\n" "$build_status" > "$tracking/creation-provider-candidate-build.status.tmp"; mv "$tracking/creation-provider-candidate-build.status.tmp" "$tracking/creation-provider-candidate-build.status"' EXIT
nix build --out-link "$tracking/creation-provider-candidate-gc-root" --print-out-paths .#default > "$tracking/creation-provider-candidate.path.tmp"
python3 - "$tracking/creation-provider-candidate.path.tmp" <<'VERIFY'
import sys
from pathlib import Path
value=Path(sys.argv[1]).read_text().strip()
assert value.startswith('/nix/store/') and '\n' not in value
assert (Path(value)/'bin/workspace-host').is_file()
VERIFY
mv "$tracking/creation-provider-candidate.path.tmp" "$tracking/creation-provider-candidate.path"
