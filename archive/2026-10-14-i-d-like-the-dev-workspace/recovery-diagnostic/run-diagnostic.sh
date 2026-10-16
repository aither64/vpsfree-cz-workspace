#!/usr/bin/env bash
# Prepared for ONE lead-assigned watcher run after direct fixture inspection.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
source ../runtime-dev-env.sh
test -f evaluated-provenance-final.json
sha256sum --check INPUTS.sha256
mkdir -- run # Never overwrite a previous attempt.
started_at=$(date --iso-8601=seconds)
diagnostic_stage=not-launched
finish() {
  result=$?
  trap - EXIT
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$started_at" "$(date --iso-8601=seconds)" "$result" > run/status
  python3 summarize-run.py "$result" "$diagnostic_stage"
  exit "$result"
}
trap finish EXIT
diagnostic_flake="path:$PWD"
nix eval --json --no-write-lock-file "$diagnostic_flake#lib.provenance" > run/provenance.json
python3 - <<'PY'
import json
from pathlib import Path
current = json.loads(Path('run/provenance.json').read_text())
reviewed = json.loads(Path('evaluated-provenance-final.json').read_text())
assert current == reviewed, 'diagnostic provenance changed; stop and inspect'
assert current['runtimeRevision'] == 'b8a6be26a75347dcc9ec0fd1330dff886e47c93f'
assert current['product'] == '/nix/store/54cv3sm4z10nal6hi4p214vds9cmjddd-dev-workspace-0.2.0'
assert current['productDrv'] == '/nix/store/77wgdsbc9ra6b23dd7w8kq3zk480zfyc-dev-workspace-0.2.0.drv'
assert current['originalCheckDrv'] == '/nix/store/62lvkrl2f6k82shyb6n4rii4myfmpy5k-vm-test-run-dev-workspace-session-recovery-boot.drv'
print('Original product/check and inspected diagnostic identities match.')
PY
diagnostic_stage=launched
nix build --no-link --no-write-lock-file --print-build-logs \
  "$diagnostic_flake#checks.x86_64-linux.session-recovery-diagnostic" > run/check.log 2>&1
