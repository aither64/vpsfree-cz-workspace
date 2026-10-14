#!/usr/bin/env bash
# Prepared for parent inspection; do not execute before accepted publication.
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
mode=${1:?Usage: config V_SHA W_SHA | kb V_SHA}
v_sha=${2:?Missing published V head}
[[ $v_sha =~ ^[0-9a-f]{40}$ ]]
[[ $v_sha == 30603a832d2848207bd7319c79c6b0388bc8646a ]]
sha256sum --check "$tracking/remediation-pin-operation-freeze.sha256"
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/remediation-pins-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/remediation-pins-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
verify_source() {
  local repo="$1" branch="$2" default="$3" revision="$4"
  [[ $(git -C "$worktrees/$repo" branch --show-current) == "$branch" ]]
  [[ $(git -C "$worktrees/$repo" rev-parse HEAD) == "$revision" ]]
  [[ -z $(git -C "$worktrees/$repo" status --porcelain) ]]
  [[ $(git -C "$worktrees/$repo" remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
  git -C "$worktrees/$repo" fetch --no-tags origin "refs/heads/$default:refs/remotes/origin/$default" "refs/heads/$branch:refs/remotes/origin/$branch"
  [[ $(git -C "$worktrees/$repo" rev-parse "refs/remotes/origin/$branch") == "$revision" ]]
  git -C "$worktrees/$repo" merge-base --is-ancestor "origin/$default" "$revision"
  git -C "$worktrees/$repo" log --oneline --left-right "origin/$default...$revision" >"$tracking/remediation-pins-$repo-default-comparison.log"
}
verify_source vpsadmin 2026-10-05-network-ipv4-left-counter master "$v_sha"
[[ $(cat "$tracking/remediation-published-v.sha") == "$v_sha" ]]
case "$mode" in
  config)
    w_sha=${3:?Missing published W head}
    [[ $w_sha =~ ^[0-9a-f]{40}$ ]]
    [[ $w_sha == b3b756a7b45864459bd39481a0d5245886777660 ]]
    verify_source vpsadmin-webui dev/network-enabled main "$w_sha"
    [[ $(cat "$tracking/remediation-published-w.sha") == "$w_sha" ]]
    repo=vpsfree-cz-configuration
    base=cde8451718d75929c931db63626b48f7de92fc4f
    old=dea15f88c38341ecfd3e5030c700d1fee3d854a7
    count=2
    ;;
  kb)
    repo=vpsfree-kb-contracts
    base=873758fd6aec0c03f50a94600e0ceab97946f255
    old=ef72876da07dae61449502e2d03856d1d3b133e4
    count=1
    ;;
  *) exit 2 ;;
esac
repo_root="$worktrees/$repo"
[[ $(git -C "$repo_root" branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
[[ $(git -C "$repo_root" rev-parse HEAD) == "$old" ]]
[[ $(git -C "$repo_root" remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
[[ -z $(git -C "$repo_root" ls-remote --heads origin refs/heads/2026-10-05-network-ipv4-left-counter) ]]
[[ -z $(git -C "$repo_root" status --porcelain) ]]
[[ $(git -C "$repo_root" rev-list --count "$base..HEAD") == "$count" ]]
git -C "$repo_root" fetch --no-tags origin refs/heads/master:refs/remotes/origin/master
git -C "$repo_root" merge-base --is-ancestor origin/master "$base"
python3 - "$repo_root" "$base" "$old" "$mode" <<'PY'
import subprocess, sys
repo, base, old, mode = sys.argv[1:]
allowed = {'flake.nix', 'flake.lock'} if mode == 'config' else {
    'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'
}
changed = set(subprocess.check_output(['git', '-C', repo, 'diff', '--name-only', base, old], text=True).splitlines())
assert changed and changed <= allowed, sorted(changed - allowed)
PY
git -C "$repo_root" log --format=fuller "$base..$old" >"$tracking/remediation-pins-$mode-original-history.log"
git -C "$repo_root" diff --binary "$base..$old" >"$tracking/remediation-pins-$mode-original.diff"
git -C "$repo_root" rev-parse HEAD >"$tracking/remediation-pins-$mode-original-head.sha"
git -C "$repo_root" rev-parse 'HEAD^{tree}' >"$tracking/remediation-pins-$mode-original-tree.sha"
# Drop only the obsolete feature pin commits. Clean-tree and exact history
# guards above preserve unrelated work; no reset, clean or default ref is used.
run_step "$mode-return-base" "$repo_root" nix develop --command git -c rebase.autoStash=false rebase --onto "$base" "$old"
[[ $(git -C "$repo_root" rev-parse HEAD) == "$base" ]]
[[ -z $(git -C "$repo_root" status --porcelain) ]]
case "$mode" in
  config)
    run_step config-set "$repo_root" nix develop --command bash "$tracking/remediation-config-pin-in-shell.sh" "$v_sha" "$w_sha"
    [[ $(git -C "$repo_root" rev-parse HEAD~2) == "$base" ]]
    [[ -z $(git -C "$repo_root" status --porcelain) ]]
    git -C "$repo_root" rev-parse HEAD~1 >"$tracking/remediation-pin-c-v.sha"
    git -C "$repo_root" rev-parse HEAD >"$tracking/remediation-pin-c-w.sha"
    git -C "$repo_root" diff --binary "$base..HEAD" >"$tracking/remediation-pins-config-final.diff"
    git -C "$repo_root" log --format=fuller "$base..HEAD" >"$tracking/remediation-pins-config-final-history.log"
    ;;
  kb)
    python3 "$tracking/set-network-kb-pin.py" "$repo_root" "$v_sha"
    run_step kb-flake-update "$repo_root" nix flake update vpsadmin
    git -C "$repo_root" diff --binary >"$tracking/remediation-pins-kb-candidate.diff"
    run_step kb-static-check "$repo_root" nix develop --command bin/check
    (cd "$repo_root" && sha256sum flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml) >"$tracking/remediation-kb-candidate.sha256"
    # Leave the verified candidate for parent diff inspection before commit.
    ;;
esac
