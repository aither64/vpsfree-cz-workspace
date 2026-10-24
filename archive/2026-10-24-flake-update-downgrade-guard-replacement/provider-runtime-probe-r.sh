#!/usr/bin/env bash
# Prepared for a fresh post-review verification watcher; do not run before review.
set -euo pipefail
: "${RUNTIME_RECEIPT:?set an owned receipt directory outside the checkout}"
: "${PROBE_INPUT:?set the selected root input name for this consumer}"
export PROBE_INPUT
export CONFCTL_FLAKE='github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db#confctl'
mkdir -p "$RUNTIME_RECEIPT"
git rev-parse HEAD > "$RUNTIME_RECEIPT/consumer-head"
sha256sum flake.nix flake.lock Gemfile Gemfile.lock > "$RUNTIME_RECEIPT/consumer-input-hashes"
git status --porcelain=v1 > "$RUNTIME_RECEIPT/status-before"
printf 'RUBYOPT set: %s\nBUNDLE_GEMFILE set: %s\n' "${RUBYOPT+yes}" "${BUNDLE_GEMFILE+yes}"
nix flake metadata --json --no-write-lock-file "${CONFCTL_FLAKE%#*}" | python3 -c '
import json,os,pathlib,sys
raw=sys.stdin.read()
if any(os.environ.get(name) and os.environ[name] in raw for name in ("GITHUB_TOKEN","GH_TOKEN")):
    raise SystemExit("Metadata unexpectedly contained a credential; receipt not written")
data=json.loads(raw)
assert data["locked"]["rev"]=="5436d3d7c36d3d5174eab3c44e3578830749d3db"
pathlib.Path(sys.argv[1]).write_text(json.dumps(data,indent=2)+"\n")
' "$RUNTIME_RECEIPT/tool-metadata.json"
nix shell "$CONFCTL_FLAKE" -c bash <<'INNER'
set -euo pipefail
provider_bin=$(command -v confctl)
printf 'Selected provider executable: %s\n' "$provider_bin"
python3 - "$provider_bin" "$RUNTIME_RECEIPT" <<'PY'
import json,os,pathlib,re,subprocess,sys
binary=pathlib.Path(sys.argv[1]).resolve()
wrapper=binary.read_text()
source=pathlib.Path(re.search(r'export RUBYLIB="([^"]+)/lib"',wrapper).group(1))
assert (source/'lib/confctl/inputs/forward_guard.rb').is_file()
runtime=re.search(r'export PATH="([^"]+):\$PATH"',wrapper).group(1)
nix=[pathlib.Path(p)/'nix' for p in runtime.split(':') if (pathlib.Path(p)/'nix').is_file()]
assert len(nix)==1,nix
version=subprocess.check_output([str(nix[0]),'--version'],text=True).strip()
receipt={'provider_binary':str(binary),'provider_source':str(source),'runtime_path':runtime,'bundled_nix':str(nix[0]),'bundled_nix_version':version}
print(json.dumps(receipt))
(pathlib.Path(sys.argv[2])/'wrapper-runtime.json').write_text(json.dumps(receipt,indent=2)+'\n')
PY
confctl inputs update --help > "$RUNTIME_RECEIPT/update-help"
python3 - "$RUNTIME_RECEIPT/update-help" <<'PY'
import pathlib,sys
assert 'forward-only' in pathlib.Path(sys.argv[1]).read_text()
PY
confctl inputs ls --json "$PROBE_INPUT" > "$RUNTIME_RECEIPT/inputs.json"
python3 - "$RUNTIME_RECEIPT/inputs.json" "$PROBE_INPUT" <<'PY'
import json,re,sys
rows=json.load(open(sys.argv[1]))
assert len(rows)==1 and rows[0]['input']==sys.argv[2]
assert isinstance(rows[0]['rev'],str) and re.fullmatch(r'[0-9a-fA-F]{40}',rows[0]['rev'])
PY
if [[ "${PROBE_CHANNELS:-0}" == 1 ]]; then
  confctl inputs channel ls > "$RUNTIME_RECEIPT/channels"
fi
INNER
git status --porcelain=v1 > "$RUNTIME_RECEIPT/status-after"
cmp "$RUNTIME_RECEIPT/status-before" "$RUNTIME_RECEIPT/status-after"
