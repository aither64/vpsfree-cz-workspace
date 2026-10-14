#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
branch=2026-10-05-network-ipv4-left-counter
mode=${1:?Missing config/kb mode}
head=${2:?Missing exact published V head}
w_head=e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/visibility-source-v.sha") == "$head" ]]
[[ $(cat "$tracking/visibility-published-v.sha") == "$head" ]]
for source in vpsadmin vpsadmin-webui; do
  if [[ $source == vpsadmin ]]; then source_branch=$branch; source_default=master; source_head=$head;
  else source_branch=dev/network-enabled; source_default=main; source_head=$w_head; fi
  source_root="$worktrees/$source"
  [[ $(git -C "$source_root" rev-parse HEAD) == "$source_head" && -z $(git -C "$source_root" status --porcelain) ]]
  [[ $(git -C "$source_root" branch --show-current) == "$source_branch" ]]
  [[ $(git -C "$source_root" remote get-url origin) == "git@github.com:vpsfreecz/$source.git" ]]
  [[ $(git -C "$source_root" ls-remote --heads origin "refs/heads/$source_branch" | cut -f1) == "$source_head" ]]
  git -C "$source_root" fetch --no-tags origin \
    "refs/heads/$source_default:refs/remotes/origin/$source_default" \
    "+refs/heads/$source_branch:refs/remotes/origin/$source_branch"
  [[ $(git -C "$source_root" rev-parse "refs/remotes/origin/$source_branch") == "$source_head" ]]
  git -C "$source_root" merge-base --is-ancestor "origin/$source_default" "$source_head"
done
case "$mode" in
  config)
    repo=vpsfree-cz-configuration; base=cde8451718d75929c931db63626b48f7de92fc4f
    old=dd10d88073da3aed6c4512e938abe4374422aab1; count=2
    ;;
  kb)
    repo=vpsfree-kb-contracts; base=873758fd6aec0c03f50a94600e0ceab97946f255
    old=291566b2c0bd43389802f607852fd9a4f8241752; count=1
    ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "$worktrees/$repo" && $(git branch --show-current) == "$branch" ]]
[[ $(git rev-parse HEAD) == "$old" && -z $(git status --porcelain) ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master
git merge-base --is-ancestor origin/master "$base"
git merge-base --is-ancestor "$base" "$old"
[[ $(git rev-list --count "$base..$old") == "$count" ]]
lease=$(cat "$tracking/visibility-$mode-lease.expected")
[[ $lease == absent || $lease =~ ^[0-9a-f]{40}$ ]]
actual_lease=$(git ls-remote --heads origin "refs/heads/$branch" | cut -f1)
[[ ${actual_lease:-absent} == "$lease" ]]
printf '%s\n' "$lease" >"$tracking/visibility-$mode-old-remote.sha"
git rev-parse "$old^{tree}" >"$tracking/visibility-$mode-old-tree.sha"
git log --reverse --format=fuller "$base..$old" >"$tracking/visibility-$mode-old-history.log"
git diff --binary "$base..$old" >"$tracking/visibility-$mode-old.diff"
python3 - "$mode" "$base" "$old" <<'PY'
import subprocess, sys
mode, base, old = sys.argv[1:]
expected = {'flake.lock'} if mode == 'config' else {'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'}
changed = set(subprocess.check_output(['git', 'diff', '--name-only', base, old], text=True).splitlines())
assert changed == expected, changed
PY
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do [[ -z ${!bypass-} ]]; done
if [[ $mode == config ]]; then
  [[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
  [[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
  for hook in pre-commit commit-msg; do
    hook_path=$(git rev-parse --git-path "hooks/$hook")
    test -x "$hook_path"
    rg -q 'Overcommit hook integration' "$hook_path"
  done
  git diff --exit-code "$base" "$old" -- .overcommit.yml .git-hooks
fi
# Drop only the verified pin-only series; never reset or clean a repository.
git -c rebase.autoStash=false rebase --onto "$base" "$old" "$branch"
[[ $(git rev-parse HEAD) == "$base" && -z $(git status --porcelain) ]]
case "$mode" in
  config)
    confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$head"
    confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui "$w_head"
    [[ $(git rev-parse HEAD~2) == "$base" && -z $(git status --porcelain) ]]
    [[ $(git diff --name-only "$old" HEAD) == flake.lock ]]
    python3 "$tracking/visibility-config-pin-guard.py" "$PWD" "$old" "$head"
    git rev-parse HEAD~1 >"$tracking/visibility-config-v-pin.sha"
    git rev-parse HEAD >"$tracking/visibility-config-final.sha"
    git log --reverse --format=fuller "$base..HEAD" >"$tracking/visibility-config-final-history.log"
    git diff --binary "$base..HEAD" >"$tracking/visibility-config-final.diff"
    git diff --binary "$old" HEAD >"$tracking/visibility-config-current-delta.diff"
    ;;
  kb)
    python3 "$tracking/fixture-final-pin-guards.py" set-kb "$PWD" "$old" "$head" "$w_head"
    nix flake update vpsadmin
    python3 "$tracking/fixture-final-pin-guards.py" kb "$PWD" "$old" "$head" "$w_head"
    bin/check
    [[ $(git rev-parse HEAD) == "$base" && -z $(git diff --cached --name-only) ]]
    python3 - <<'PY'
import subprocess
expected = {'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'}
changed = set()
for entry in filter(None, subprocess.check_output(['git', 'status', '--porcelain=v1', '-z'], text=True).split('\0')):
    assert entry[:3] == ' M ', entry
    changed.add(entry[3:])
assert changed == expected, changed
PY
    git diff --binary >"$tracking/visibility-kb-candidate.diff"
    sha256sum flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml \
      >"$tracking/visibility-kb-candidate.sha256"
    # Leave the five-field candidate for root inspection; do not commit it here.
    ;;
esac
