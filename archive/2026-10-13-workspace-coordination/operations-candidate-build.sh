#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
trap 'build_status=$?; printf "%s\n" "$build_status" > "$tracking/operations-candidate-build.status.tmp"; mv "$tracking/operations-candidate-build.status.tmp" "$tracking/operations-candidate-build.status"' EXIT
nix build --out-link "$tracking/operations-candidate-gc-root" --print-out-paths .#default > "$tracking/operations-candidate.path.tmp"
python3 - "$tracking/operations-candidate.path.tmp" <<'VERIFY'
import sys
from pathlib import Path
value=Path(sys.argv[1]).read_text().strip()
assert value.startswith('/nix/store/') and '\n' not in value
assert (Path(value)/'bin/workspace-host').is_file()
VERIFY
mv "$tracking/operations-candidate.path.tmp" "$tracking/operations-candidate.path"
