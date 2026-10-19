#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
trap 'build_status=$?; printf "%s\n" "$build_status" > "$tracking/stdout-candidate-build.status.tmp"; mv "$tracking/stdout-candidate-build.status.tmp" "$tracking/stdout-candidate-build.status"' EXIT
nix build --out-link "$tracking/stdout-candidate-gc-root" --print-out-paths .#default > "$tracking/stdout-candidate.path.tmp"
python3 - "$tracking/stdout-candidate.path.tmp" <<'VERIFY'
import sys
from pathlib import Path
value=Path(sys.argv[1]).read_text().strip()
assert value.startswith('/nix/store/') and '\n' not in value
assert (Path(value)/'bin/workspace-host').is_file()
VERIFY
mv "$tracking/stdout-candidate.path.tmp" "$tracking/stdout-candidate.path"
cp "$tracking/stdout-candidate.path" "$tracking/candidate-package.path"
