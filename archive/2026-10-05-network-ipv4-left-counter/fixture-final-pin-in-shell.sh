#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
mode=${1:?Missing config/kb mode}
shift
source "$tracking/fixture-final-common.sh"
case "$mode" in
  config)
    repo=vpsfree-cz-configuration
    base=cde8451718d75929c931db63626b48f7de92fc4f
    old=a6243f09265398368e07695dd531e4a0e312350b
    ;;
  kb)
    repo=vpsfree-kb-contracts
    base=873758fd6aec0c03f50a94600e0ceab97946f255
    old=8c396b88ff10bf71c47e2364e7ea1ee34f20d184
    ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "$worktrees/$repo" ]]
[[ $(git rev-parse HEAD) == "$base" && -z $(git status --porcelain) ]]
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
case "$mode" in
  config)
    test -f .overcommit.yml
    [[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
    [[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
    for hook in pre-commit commit-msg; do
      hook_path=$(git rev-parse --git-path "hooks/$hook")
      test -x "$hook_path"
      rg -q 'Overcommit hook integration' "$hook_path"
    done
    confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$v_sha"
    confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui "$w_sha"
    [[ $(git rev-parse HEAD~2) == "$base" && -z $(git status --porcelain) ]]
    python3 "$tracking/fixture-final-pin-guards.py" config "$PWD" "$old" "$v_sha" "$w_sha"
    git rev-parse HEAD~1 >"$tracking/fixture-final-pin-c-v.sha"
    git rev-parse HEAD >"$tracking/fixture-final-pin-c-w.sha"
    git diff --binary "$base..HEAD" >"$tracking/fixture-final-config-final.diff"
    git log --format=fuller "$base..HEAD" >"$tracking/fixture-final-config-final-history.log"
    ;;
  kb)
    python3 "$tracking/fixture-final-pin-guards.py" set-kb "$PWD" "$old" "$v_sha" "$w_sha"
    nix flake update vpsadmin
    python3 "$tracking/fixture-final-pin-guards.py" kb "$PWD" "$old" "$v_sha" "$w_sha"
    bin/check
    [[ $(git rev-parse HEAD) == "$base" ]]
    git diff --binary >"$tracking/fixture-final-kb-candidate.diff"
    sha256sum flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml \
      >"$tracking/fixture-final-kb-candidate.sha256"
    # Root inspects this exact candidate before a separate normal-hook commit.
    ;;
esac
