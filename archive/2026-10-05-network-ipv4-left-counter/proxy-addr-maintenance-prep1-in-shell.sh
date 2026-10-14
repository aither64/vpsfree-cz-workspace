#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr
prefix=proxy-addr-maintenance-prep1
stage=${1:?Missing generate/quick stage}
[[ $(pwd -P) == "$repo_root" ]]
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter ]]
[[ ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]

run_step() {
  local name=$1 directory=$2 result
  shift 2
  [[ ! -e "$tracking/$prefix-$name.log" && ! -e "$tracking/$prefix-$name.exit" ]]
  printf 'Running %s in %s\n' "$name" "$directory"
  set +e
  (cd "$directory" && "$@") >"$tracking/$prefix-$name.log" 2>&1
  result=$?
  set -e
  printf '%s\n' "$result" >"$tracking/$prefix-$name.exit"
  printf '%s exited %s\n' "$name" "$result"
  return "$result"
}

case "$stage" in
  generate)
    run_step before "$repo_root" python3 "$tracking/$prefix-guard.py" before
    run_step remote-base "$repo_root" git ls-remote --heads origin \
      refs/heads/main refs/heads/dev/proxy-addr-patch
    run_step remote-guard "$repo_root" python3 "$tracking/$prefix-guard.py" remote
    run_step toolchain "$repo_root" npm run env:locked
    run_step registry-metadata "$repo_root/bff" npm view proxy-addr@2.0.8 --json \
      --registry=https://registry.npmjs.org --loglevel=error
    run_step lock-generator "$repo_root/bff" npm update proxy-addr --package-lock-only \
      --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org
    run_step lock-guard "$repo_root" python3 "$tracking/$prefix-guard.py" lock
    run_step install-root "$repo_root" npm ci --include=dev
    run_step install-bff "$repo_root/bff" npm ci --omit=dev
    run_step installed-leaf "$repo_root/bff" node --eval \
      'const assert = require("node:assert/strict"); const path = require("node:path"); const dependency = require.resolve("proxy-addr/package.json", { paths: [path.dirname(require.resolve("express"))] }); const value = require(dependency); assert.equal(value.version, "2.0.8"); console.log(JSON.stringify({ dependency, version: value.version }));'
    run_step dependency-lineage "$repo_root/bff" npm explain proxy-addr
    run_step production-audit-bff "$repo_root/bff" npm audit --omit=dev --audit-level=high --json
    run_step production-audit-root "$repo_root" npm audit --omit=dev --audit-level=critical --json
    run_step prefetch-bff "$repo_root" prefetch-npm-deps bff/package-lock.json
    run_step prefetch-root "$repo_root" prefetch-npm-deps package-lock.json
    run_step generation-receipts "$repo_root" python3 "$tracking/$prefix-guard.py" receipts
    git diff --binary >"$tracking/$prefix-generated.diff"
    printf 'Generator stage complete; stop for owner hash/docs reconciliation before quick stage\n'
    ;;
  quick)
    run_step ready "$repo_root" python3 "$tracking/$prefix-guard.py" ready
    run_step bff-tests "$repo_root" npm run test:bff
    run_step package-policy-tests "$repo_root" node --test \
      scripts/check-package-source.test.mjs scripts/check-package-contents.test.mjs \
      scripts/oauth-nginx-policy.test.mjs scripts/oauth-csp-contract.test.mjs
    run_step auth-unit-tests "$repo_root" npm test -- \
      src/app/runtimeBootstrap.test.ts src/app/runtimeBootstrap.required.test.ts \
      src/lib/auth/oauth2Client.test.ts
    run_step quality-types "$repo_root" npm run ci:quick
    run_step nix-format "$repo_root" nixfmt --check packages/bff.nix
    run_step final-scope "$repo_root" python3 "$tracking/$prefix-guard.py" ready
    git diff --binary >"$tracking/$prefix-quick-final.diff"
    ;;
  *) exit 2 ;;
esac
