#!/usr/bin/env bash
set -euo pipefail
webui=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async
provider=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/haveapi
: "${EVIDENCE:?Set EVIDENCE to a new absolute operation evidence directory}"
[[ "$EVIDENCE" = /* ]]
mkdir "$EVIDENCE"
cd "$webui"
guard() {
  test "$(git rev-parse HEAD)" = 8772bab21cd8739bf4672cdf4976aea2a6e59de3 || return 1
  test "$(git rev-parse HEAD^{tree})" = 3302fcf2bc01f1885426a69c7ddc364b8cdd35ad || return 1
  test -z "$(git status --porcelain=v1)" || return 1
  test "$(git -C "$provider" rev-parse HEAD)" = f94e65e35166a0bf8048a27c9d57c7d36957d65b || return 1
  test "$(git -C "$provider" rev-parse HEAD^{tree})" = 2f2879b95f4fba789d8a9d52ca914b8876438dae || return 1
  test -z "$(git -C "$provider" status --porcelain=v1)" || return 1
  printf '%s  %s\n' 0f1d21926f6d3a00527bcd486b7f3dae50134ca1e5316b990e3538e3c99b1a87 package-lock.json \
    41c3c3f16577dd7c8849f11615e3111302513af65a1e5640c9b121f772fb9975 \
    vendor/haveapi-client-f94e65e35166a0bf8048a27c9d57c7d36957d65b.tgz | sha256sum --check
}
snapshot() {
  git rev-parse HEAD HEAD^{tree}
  git -C "$provider" rev-parse HEAD HEAD^{tree}
  sha256sum package.json package-lock.json bff/package.json bff/package-lock.json \
    vendor/haveapi-client-provenance.json \
    vendor/haveapi-client-f94e65e35166a0bf8048a27c9d57c7d36957d65b.tgz
}
run() {
  local name=$1
  shift
  printf '%q ' "$@" > "$EVIDENCE/$name.command"
  printf '\n' >> "$EVIDENCE/$name.command"
  set +e
  "$@" > "$EVIDENCE/$name.stdout" 2> "$EVIDENCE/$name.stderr"
  local result=$?
  set -e
  printf '%s\n' "$result" > "$EVIDENCE/$name.exit"
  return "$result"
}
guard > "$EVIDENCE/pre-guard.log" 2>&1
snapshot > "$EVIDENCE/pre-identities.txt"
date --utc --iso-8601=seconds > "$EVIDENCE/started.txt"
trap 'result=$?; snapshot > "$EVIDENCE/post-identities.txt"; if ! guard > "$EVIDENCE/post-guard.log" 2>&1; then result=1; fi; if ! cmp "$EVIDENCE/pre-identities.txt" "$EVIDENCE/post-identities.txt"; then result=1; fi; date --utc --iso-8601=seconds > "$EVIDENCE/finished.txt"; printf "%s\n" "$result" > "$EVIDENCE/operation.exit"; exit "$result"' EXIT
run full-tests nix develop --command npm test
run production-build nix develop --command npm run build
cp dist/build-info.json "$EVIDENCE/normal-build-info.json"
run nix-build nix build --no-link --json --print-build-logs \
  .#frontend .#checks.x86_64-linux.source-contents \
  .#checks.x86_64-linux.provenance .#checks.x86_64-linux.package-contents
python3 - "$EVIDENCE" <<'PY'
import json,pathlib,subprocess,shutil
root=pathlib.Path(__import__('sys').argv[1]); builds=json.loads((root/'nix-build.stdout').read_text())
drvs=[entry['drvPath'] for entry in builds]
with (root/'derivations.json').open('w') as out, (root/'derivations.stderr').open('w') as err:
    result=subprocess.run(['nix','derivation','show',*drvs],stdout=out,stderr=err)
(root/'derivations.exit').write_text(str(result.returncode)+'\n')
if result.returncode: raise SystemExit(result.returncode)
for entry in builds:
    output=pathlib.Path(entry['outputs']['out']); metadata=output/'build-info.json'
    if metadata.is_file(): shutil.copyfile(metadata,root/'nix-frontend-build-info.json')
(root/'output-paths.json').write_text(json.dumps(builds,indent=2)+'\n')
PY
