#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
K=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts
for suffix in log exit; do test ! -e "$TRACK/network-layout-pins1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(cat "$TRACK/network-layout-v-operation2.exit")" = 0
 VHEAD=$(cat "$TRACK/network-layout-v-operation2.sha")
 test "$(git ls-remote git@github.com:vpsfreecz/vpsadmin.git refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = "$VHEAD"
 test "$(git ls-remote git@github.com:vpsfreecz/vpsadmin-webui.git refs/heads/dev/network-enabled | cut -f1)" = ce856841a65d72648d03b6cba1748dd7dd9af048
 cd "$C"
 test "$(git rev-parse HEAD)" = a433e19a5aecdc934aedeecacc476404411de508
 test -z "$(git status --porcelain)"
 test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
 test "$(git rev-parse HEAD~2)" = 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3
 test "$(git diff --name-only HEAD~2 HEAD)" = flake.lock
 git fetch --no-tags origin +refs/heads/master:refs/remotes/origin/master
 test "$(git rev-parse origin/master)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
 git merge-base --is-ancestor HEAD~2 origin/master
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = a433e19a5aecdc934aedeecacc476404411de508
 git log --format=fuller HEAD~2..HEAD > "$TRACK/network-layout-c-old.history"
 git diff --binary --full-index HEAD~2 HEAD > "$TRACK/network-layout-c-old.diff"
 git rev-parse HEAD^{tree} > "$TRACK/network-layout-c-old.tree"
 git show HEAD:flake.lock > "$TRACK/network-layout-c-old.lock"
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 export NETWORK_LAYOUT_V_HEAD="$VHEAD"
 git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto origin/master HEAD
 nix develop --command bash -ec '
   test -x "$(git rev-parse --git-path hooks)/pre-commit"
   test -x "$(git rev-parse --git-path hooks)/commit-msg"
   confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$NETWORK_LAYOUT_V_HEAD"
   confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui ce856841a65d72648d03b6cba1748dd7dd9af048
 '
 test "$(git rev-parse HEAD~2)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
 test -z "$(git status --porcelain)"
 test "$(git diff --name-only origin/master HEAD)" = flake.lock
 python3 "$TRACK/fixture-final-pin-guards.py" config "$C" c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a "$VHEAD" ce856841a65d72648d03b6cba1748dd7dd9af048
 python3 - <<'GUARD'
import json,subprocess
old=json.loads(subprocess.check_output(['git','show','a433e19a5aecdc934aedeecacc476404411de508:flake.lock']))
new=json.load(open('flake.lock'))
for lock in (old,new):
 inputs=lock['nodes'][lock['root']]['inputs']
 lock['selectedW']=lock['nodes'][inputs['vpsadminWebui']]
assert old['selectedW']==new['selectedW'], 'Agreed W metadata or follows changed'
print('Agreed W node unchanged; fresh default graph retained')
GUARD
 git rev-parse HEAD > "$TRACK/network-layout-c-final.sha"
 git log --format=fuller origin/master..HEAD > "$TRACK/network-layout-c-final.history"
 git diff --binary --full-index origin/master HEAD > "$TRACK/network-layout-c-final.diff"
 cd "$K"
 test "$(git rev-parse HEAD)" = 819c4824eddbad89a3b1f797219becd8d33fcc48
 test -z "$(git status --porcelain)"
 test "$(git rev-parse HEAD~1)" = 873758fd6aec0c03f50a94600e0ceab97946f255
 test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
 git diff --name-only HEAD~1 HEAD > "$TRACK/network-layout-k-old.paths"
 printf '%s\n' captures.json contract/navigation.yml contract/pages.yml flake.lock flake.nix > "$TRACK/network-layout-k-expected.paths"
 cmp "$TRACK/network-layout-k-old.paths" "$TRACK/network-layout-k-expected.paths"
 git fetch --no-tags origin +refs/heads/master:refs/remotes/origin/master
 test "$(git rev-parse origin/master)" = 873758fd6aec0c03f50a94600e0ceab97946f255
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 819c4824eddbad89a3b1f797219becd8d33fcc48
 git log --format=fuller origin/master..HEAD > "$TRACK/network-layout-k-old.history"
 git diff --binary --full-index origin/master HEAD > "$TRACK/network-layout-k-old.diff"
 git rev-parse HEAD^{tree} > "$TRACK/network-layout-k-old.tree"
 git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto origin/master HEAD
 python3 "$TRACK/fixture-final-pin-guards.py" set-kb "$K" 819c4824eddbad89a3b1f797219becd8d33fcc48 "$VHEAD" 0000000000000000000000000000000000000000
 nix flake update vpsadmin
 python3 "$TRACK/fixture-final-pin-guards.py" kb "$K" 819c4824eddbad89a3b1f797219becd8d33fcc48 "$VHEAD" 0000000000000000000000000000000000000000
 git diff --name-only > "$TRACK/network-layout-k-candidate.paths"
 cmp "$TRACK/network-layout-k-candidate.paths" "$TRACK/network-layout-k-expected.paths"
 git diff --binary --full-index > "$TRACK/network-layout-k-candidate.diff"
 git diff --exit-code 819c4824eddbad89a3b1f797219becd8d33fcc48 -- screenshots scenarios fixtures contract/pages > "$TRACK/network-layout-k-protected.diff"
 git diff --cached --quiet
 echo 'K candidate prepared; root inspection/normal commit and both downstream publications remain separate.'
) > "$TRACK/network-layout-pins1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-layout-pins1.exit"
exit "$result"
