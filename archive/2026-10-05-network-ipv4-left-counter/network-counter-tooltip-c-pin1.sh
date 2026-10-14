#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
cd "$C"
for suffix in log exit; do test ! -e "$TRACK/network-counter-tooltip-c-pin1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = 525c02fea0334222020c492c29bd9d8e06d29de9
 test "$(git rev-parse origin/master)" = 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3
 test -z "$(git status --porcelain)"
 test "$(git rev-list --count origin/master..HEAD)" = 2
 test "$(git diff --name-only origin/master..HEAD)" = flake.lock
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 525c02fea0334222020c492c29bd9d8e06d29de9
 test "$(git ls-remote origin refs/heads/master | cut -f1)" = 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3
 test "$(git ls-remote git@github.com:vpsfreecz/vpsadmin-webui.git refs/heads/dev/network-enabled | cut -f1)" = 1eb3f8d97f9091ec643ff63c2d0e4bb259e81a16
 git log --format=fuller origin/master..HEAD > "$TRACK/network-counter-tooltip-c-old.history"
 git diff --binary --full-index origin/master..HEAD > "$TRACK/network-counter-tooltip-c-old.diff"
 git rev-parse HEAD^{tree} > "$TRACK/network-counter-tooltip-c-old.tree"
 git show HEAD:flake.lock > "$TRACK/network-counter-tooltip-c-old.lock"
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop --command bash -ec '
   test -x "$(git rev-parse --git-path hooks)/pre-commit"
   test -x "$(git rev-parse --git-path hooks)/commit-msg"
   git -c rebase.autoStash=false rebase --onto origin/master HEAD
   confctl inputs channel set --commit --no-editor vpsadmin vpsadmin cc8e9e7e421a258a46279304c910f88e2ad33147
   confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui 1eb3f8d97f9091ec643ff63c2d0e4bb259e81a16
 '
 test "$(git rev-parse HEAD~2)" = 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3
 test -z "$(git status --porcelain)"
 test "$(git diff --name-only origin/master..HEAD)" = flake.lock
 python3 "$TRACK/fixture-final-pin-guards.py" config "$C" 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3 cc8e9e7e421a258a46279304c910f88e2ad33147 1eb3f8d97f9091ec643ff63c2d0e4bb259e81a16
 python3 - <<'GUARD'
import copy,json,subprocess
old=json.loads(subprocess.check_output(['git','show','525c02fea0334222020c492c29bd9d8e06d29de9:flake.lock']))
new=json.load(open('flake.lock'))
def normalize(lock):
 result=copy.deepcopy(lock); node=result['nodes'][result['nodes'][result['root']]['inputs']['vpsadminWebui']]
 for key in ('rev','narHash','lastModified'): node['locked'].pop(key)
 return result
assert normalize(old)==normalize(new), 'Beyond W locked metadata changed versus inspected C525'
print('W-only metadata delta; V and complete unrelated graph exact versus C525')
GUARD
 git rev-parse HEAD > "$TRACK/network-counter-tooltip-c-final1.sha"
 git log --format=fuller origin/master..HEAD > "$TRACK/network-counter-tooltip-c-final1.history"
 git diff --binary --full-index origin/master..HEAD > "$TRACK/network-counter-tooltip-c-final1.diff"
) > "$TRACK/network-counter-tooltip-c-pin1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-tooltip-c-pin1.exit"
exit "$result"
