#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
trap 'build_status=$?; printf "%s\n" "$build_status" > "$tracking/library-candidate-build.status.tmp"; mv "$tracking/library-candidate-build.status.tmp" "$tracking/library-candidate-build.status"' EXIT
nix build --out-link "$tracking/library-candidate-gc-root" --print-out-paths .#default > "$tracking/library-candidate.path.tmp"
python3 - "$tracking/library-candidate.path.tmp" <<'PY'
import sys
from pathlib import Path
value=Path(sys.argv[1]).read_text().strip()
assert value.startswith('/nix/store/') and '\n' not in value
assert (Path(value)/'bin/workspace-host').is_file()
PY
mv "$tracking/library-candidate.path.tmp" "$tracking/library-candidate.path"
cp "$tracking/library-candidate.path" "$tracking/candidate-package.path"
