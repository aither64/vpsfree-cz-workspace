#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr
prefix=proxy-addr-maintenance-final
prep=proxy-addr-maintenance-prep1
base=02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51
branch=dev/proxy-addr-patch
paths=(
  bff/package-lock.json
  packages/bff.nix
  docs/design/PACKAGING.md
  docs/work-log/2026-10-06-proxy-addr-patch.md
)

[[ $(pwd -P) == "$repo_root" ]]
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter ]]
[[ ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
sha256sum --check "$tracking/$prefix.freeze.sha256"
sha256sum --check "$tracking/$prep.freeze.sha256"
for receipt in generate-wrapper production-audit-bff production-audit-root \
  quick-wrapper ready bff-tests package-policy-tests auth-unit-tests quality-types nix-format final-scope; do
  [[ $(cat "$tracking/$prep-$receipt.exit") == 0 ]]
done
[[ $(cat "$tracking/$prefix-docs.exit") == 0 ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git remote get-url origin) == git@github.com:vpsfreecz/vpsadmin-webui.git ]]

run_step() {
  local name=$1 result
  shift
  [[ ! -e "$tracking/$prefix-$name.log" && ! -e "$tracking/$prefix-$name.exit" ]]
  printf 'Running %s in %s\n' "$name" "$repo_root"
  set +e
  "$@" >"$tracking/$prefix-$name.log" 2>&1
  result=$?
  set -e
  printf '%s\n' "$result" >"$tracking/$prefix-$name.exit"
  printf '%s exited %s\n' "$name" "$result"
  return "$result"
}

check_committed_head() {
  [[ $selected =~ ^[0-9a-f]{40}$ ]]
  [[ $(cat "$tracking/$prefix-committed.sha") == "$selected" ]]
  [[ $(git rev-parse HEAD) == "$selected" && -z $(git status --porcelain) ]]
  [[ $(git rev-parse HEAD^) == "$base" && $(git rev-list --count "$base..HEAD") == 1 ]]
  python3 "$tracking/$prefix-guard.py" committed "$selected"
}
