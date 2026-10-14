#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
if [[ ${DEV_SESSION_SLUG+x} || ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
fi
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
mode=${1:?Usage: prepare-network-pins.sh config V_SHA W_SHA | kb V_SHA}
v_sha=${2:?Missing published vpsAdmin commit}
[[ $v_sha =~ ^[0-9a-f]{40}$ ]]
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/pins-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/pins-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
verify_source() {
  local repo="$1" branch="$2" default="$3" commit="$4"
  [[ $(git -C "$worktrees/$repo" branch --show-current) == "$branch" ]]
  [[ $(git -C "$worktrees/$repo" rev-parse HEAD) == "$commit" ]]
  [[ -z $(git -C "$worktrees/$repo" status --porcelain) ]]
  [[ $(git -C "$worktrees/$repo" remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
  git -C "$worktrees/$repo" fetch --no-tags origin "refs/heads/$default:refs/remotes/origin/$default" "refs/heads/$branch:refs/remotes/origin/$branch"
  [[ $(git -C "$worktrees/$repo" rev-parse "refs/remotes/origin/$branch") == "$commit" ]]
  git -C "$worktrees/$repo" log --oneline --left-right "origin/$default...$commit" >"$tracking/pins-$repo-default-comparison.log"
  git -C "$worktrees/$repo" merge-base --is-ancestor "origin/$default" "$commit"
}
verify_source vpsadmin 2026-10-05-network-ipv4-left-counter master "$v_sha"
case "$mode" in
  config)
    w_sha=${3:?Missing published WebUI commit}
    [[ $w_sha =~ ^[0-9a-f]{40}$ ]]
    verify_source vpsadmin-webui dev/network-enabled main "$w_sha"
    repo_root="$worktrees/vpsfree-cz-configuration"
    [[ $(git -C "$repo_root" branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
    [[ -z $(git -C "$repo_root" status --porcelain) ]]
    git -C "$repo_root" fetch --no-tags origin refs/heads/master:refs/remotes/origin/master
    git -C "$repo_root" log --oneline --left-right origin/master...HEAD >"$tracking/pins-config-default-comparison.log"
    git -C "$repo_root" merge-base --is-ancestor origin/master HEAD
    run_step config-set "$repo_root" nix develop --command bash "$tracking/set-network-config-pins.sh" "$v_sha" "$w_sha"
    ;;
  kb)
    repo_root="$worktrees/vpsfree-kb-contracts"
    [[ $(git -C "$repo_root" branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
    [[ -z $(git -C "$repo_root" status --porcelain) ]]
    git -C "$repo_root" fetch --no-tags origin refs/heads/master:refs/remotes/origin/master
    git -C "$repo_root" log --oneline --left-right origin/master...HEAD >"$tracking/pins-kb-default-comparison.log"
    git -C "$repo_root" merge-base --is-ancestor origin/master HEAD
    python3 "$tracking/set-network-kb-pin.py" "$repo_root" "$v_sha"
    run_step kb-flake-update "$repo_root" nix flake update vpsadmin
    git -C "$repo_root" diff -- flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml >"$tracking/pins-kb.diff"
    run_step kb-static-check "$repo_root" nix develop --command bin/check
    ;;
  *) exit 2 ;;
esac
