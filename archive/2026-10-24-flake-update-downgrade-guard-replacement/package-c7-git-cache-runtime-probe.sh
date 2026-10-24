#!/usr/bin/env bash
# Actual workflow development-shell boundary. No credential lookup or environment dump.
set -euo pipefail
: "${RUNTIME_RECEIPT:?set the owned caller receipt directory}"
: "${PROBE_INPUT:?set the selected root input}"
: "${EXPECTED_PROVIDER_BINARY:?set the verified retained provider wrapper}"
: "${CONFCTL_FLAKE:?set the exact immutable provider}"
mkdir "$RUNTIME_RECEIPT"
git rev-parse HEAD > "$RUNTIME_RECEIPT/source-head"
git status --porcelain=v1 > "$RUNTIME_RECEIPT/status-before"
printf 'RUBYOPT present: %s\nBUNDLE_GEMFILE present: %s\n' "${RUBYOPT+yes}" "${BUNDLE_GEMFILE+yes}" > "$RUNTIME_RECEIPT/caller-state"
nix shell "$CONFCTL_FLAKE" -c bash -c 'command -v confctl' > "$RUNTIME_RECEIPT/provider-binary"
test "$(realpath "$(cat "$RUNTIME_RECEIPT/provider-binary")")" = "$(realpath "$EXPECTED_PROVIDER_BINARY")"
# Preserve the real development shell's RUBYOPT/BUNDLE state.
nix shell "$CONFCTL_FLAKE" -c confctl inputs ls --json "$PROBE_INPUT" > "$RUNTIME_RECEIPT/resolved-input.json"
python3 - "$RUNTIME_RECEIPT/resolved-input.json" "$PROBE_INPUT" <<'PY'
import json,re,sys
rows=json.load(open(sys.argv[1]))
assert len(rows)==1 and rows[0]['input']==sys.argv[2]
assert isinstance(rows[0]['rev'],str) and re.fullmatch(r'[0-9a-fA-F]{40}',rows[0]['rev'])
PY
if [[ "${PROBE_CHANNELS:-0}" == 1 ]]; then
  nix shell "$CONFCTL_FLAKE" -c confctl inputs channel ls > "$RUNTIME_RECEIPT/channels"
fi
git status --porcelain=v1 > "$RUNTIME_RECEIPT/status-after"
cmp "$RUNTIME_RECEIPT/status-before" "$RUNTIME_RECEIPT/status-after"
