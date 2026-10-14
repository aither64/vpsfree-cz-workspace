#!/usr/bin/env bash
set -euo pipefail
set -o noclobber
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
branch=2026-10-05-network-ipv4-left-counter
mode=${1:?Missing config/kb mode}
head=${2:?Missing exact published V head}
w_head=e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/legacy-network-client-source.sha") == "$head" ]]
[[ $(cat "$tracking/legacy-network-client-published-v.sha") == "$head" ]]
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
  if [[ $source == vpsadmin ]]; then
    git -C "$source_root" merge-base --is-ancestor "origin/$source_default" "$source_head"
  else
    # This follow-up does not change or publish W; retain its agreed exact pin.
    git -C "$source_root" merge-base --is-ancestor 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51 "$source_head"
    git -C "$source_root" log --oneline --left-right "origin/$source_default...$source_head" \
      >"$tracking/legacy-network-client-w-incoming-default-comparison-$mode.log"
  fi
done
case "$mode" in
  config)
    repo=vpsfree-cz-configuration; old_base=6f6aff9029cd57e1a0f9201356f7fdc9f6480671; base=6f6aff9029cd57e1a0f9201356f7fdc9f6480671
    old=b217e0f0a74b45fe2a95fcc79c2eb646f21248ce; count=2
    ;;
  kb)
    repo=vpsfree-kb-contracts; old_base=873758fd6aec0c03f50a94600e0ceab97946f255; base=$old_base
    old=609fd8a0070235339a4ddb567d905e466776d6a8; count=1
    ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "$worktrees/$repo" && $(git branch --show-current) == "$branch" ]]
[[ $(git rev-parse HEAD) == "$old" && -z $(git status --porcelain) ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master
[[ $(git rev-parse origin/master) == "$base" ]]
git merge-base --is-ancestor "$old_base" "$base"
git merge-base --is-ancestor "$old_base" "$old"
[[ $(git rev-list --count "$old_base..$old") == "$count" ]]
lease=$old
[[ $lease == absent || $lease =~ ^[0-9a-f]{40}$ ]]
actual_lease=$(git ls-remote --heads origin "refs/heads/$branch" | cut -f1)
[[ ${actual_lease:-absent} == "$lease" ]]
printf '%s\n' "$lease" >"$tracking/legacy-network-client-$mode-old-remote.sha"
git rev-parse "$old^{tree}" >"$tracking/legacy-network-client-$mode-old-tree.sha"
git log --reverse --format=fuller "$old_base..$old" >"$tracking/legacy-network-client-$mode-old-history.log"
git diff --binary "$old_base..$old" >"$tracking/legacy-network-client-$mode-old.diff"
python3 - "$mode" "$old_base" "$old" <<'PY'
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
  git diff --exit-code "$old_base" "$old" -- .overcommit.yml .git-hooks
  git diff --exit-code "$old_base" "$base" -- .overcommit.yml .git-hooks AGENTS.md flake.nix
fi
# Replace only the verified pin-only series on the freshly inspected default.
# Never reset, clean, stash or modify the default branch.
git -c rebase.autoStash=false rebase --onto "$base" "$old" "$branch"
[[ $(git rev-parse HEAD) == "$base" && -z $(git status --porcelain) ]]
case "$mode" in
  config)
    confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$head"
    confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui "$w_head"
    [[ $(git rev-parse HEAD~2) == "$base" && -z $(git status --porcelain) ]]
    [[ $(git diff --name-only "$base" HEAD) == flake.lock ]]
    python3 "$tracking/visibility-current-base-config-guard.py" "$PWD" "$old" "$base" "$head"
    git rev-parse HEAD~1 >"$tracking/legacy-network-client-config-v-pin.sha"
    git rev-parse HEAD >"$tracking/legacy-network-client-config-final.sha"
    git log --reverse --format=fuller "$base..HEAD" >"$tracking/legacy-network-client-config-final-history.log"
    git diff --binary "$base..HEAD" >"$tracking/legacy-network-client-config-final.diff"
    git diff --binary "$old" HEAD >"$tracking/legacy-network-client-config-current-delta.diff"
    ;;
  kb)
    python3 "$tracking/fixture-final-pin-guards.py" set-kb "$PWD" "$old" "$head" "$w_head"
    nix flake update vpsadmin
    python3 "$tracking/fixture-final-pin-guards.py" kb "$PWD" "$old" "$head" "$w_head"
    # Re-enter the pinned shell after changing the input; the outer shell still
    # carries VPSADMIN_KB_VPSADMIN_SOURCE from the previous lock.
    [[ ! -e "$tracking/legacy-network-client-kb-effective-v-source.path" ]]
    nix develop --command bash -c '
      set -euo pipefail
      expected_source=$(nix eval --raw .#devShells.x86_64-linux.default.VPSADMIN_KB_VPSADMIN_SOURCE)
      [[ ${VPSADMIN_KB_VPSADMIN_SOURCE-} == "$expected_source" ]]
      printf "%s\n" "$expected_source" >"/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/legacy-network-client-kb-effective-v-source.path"
      bin/check
    '
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
    git diff --binary >"$tracking/legacy-network-client-kb-candidate.diff"
    sha256sum flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml \
      >"$tracking/legacy-network-client-kb-candidate.sha256"
    # Leave the five-field candidate for root inspection; do not commit it here.
    ;;
esac
