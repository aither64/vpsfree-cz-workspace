#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(pwd -P) == /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration ]]
[[ $(git rev-parse HEAD) == cde8451718d75929c931db63626b48f7de92fc4f ]]
[[ -z $(git status --porcelain) ]]
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
test -f .overcommit.yml
[[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
[[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
for hook in pre-commit commit-msg; do
  hook_path=$(git rev-parse --git-path "hooks/$hook")
  test -x "$hook_path"
  rg -q 'Overcommit hook integration' "$hook_path"
done
bash "$tracking/set-network-config-pins.sh" "$1" "$2"
