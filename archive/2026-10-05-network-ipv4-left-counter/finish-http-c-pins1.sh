#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
cd "$C"
for suffix in log exit sha; do test ! -e "$TRACK/finish-http-c-pins1.$suffix"; done
set +e
(
  set -euo pipefail
  test "$(git rev-parse HEAD)" = f1141690dd3592cc1e7fc14b91e85aac8ec5d51d
  test -z "$(git status --porcelain)"
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  test "$(git rev-parse origin/master)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
  test "$(git ls-remote git@github.com:vpsfreecz/vpsadmin.git refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 7e86ee211d898256bd93cac7221c256636f3fcc3
  test "$(git ls-remote git@github.com:vpsfreecz/vpsadmin-webui.git refs/heads/dev/network-enabled | cut -f1)" = ce856841a65d72648d03b6cba1748dd7dd9af048
  git branch preserve/finish-http-c-f114 HEAD
  git log --format=fuller origin/master..HEAD > "$TRACK/finish-http-c-old.history"
  git diff --binary --full-index origin/master HEAD > "$TRACK/finish-http-c-old.diff"
  git show HEAD:flake.lock > "$TRACK/finish-http-c-old.lock"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop --command bash -ec '
    test -x "$(git rev-parse --git-path hooks)/pre-commit"
    test -x "$(git rev-parse --git-path hooks)/commit-msg"
    git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a f1141690dd3592cc1e7fc14b91e85aac8ec5d51d
    test "$(git rev-parse HEAD)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
    confctl inputs channel set --commit --no-editor vpsadmin vpsadmin 7e86ee211d898256bd93cac7221c256636f3fcc3
    confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui ce856841a65d72648d03b6cba1748dd7dd9af048
  '
  test -z "$(git status --porcelain)"
  test "$(git rev-parse HEAD~2)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
  test "$(git diff --name-only origin/master HEAD)" = flake.lock
  python3 "$TRACK/fixture-final-pin-guards.py" config "$C" c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a 7e86ee211d898256bd93cac7221c256636f3fcc3 ce856841a65d72648d03b6cba1748dd7dd9af048
  python3 - <<'PY'
import json, subprocess
old=json.loads(subprocess.check_output(['git','show','f1141690dd3592cc1e7fc14b91e85aac8ec5d51d:flake.lock']))
new=json.load(open('flake.lock'))
def selected(lock, name):
    return lock['nodes'][lock['nodes'][lock['root']]['inputs'][name]]
assert selected(old,'vpsadminWebui') == selected(new,'vpsadminWebui')
old_v=selected(old,'vpsadminServices')
new_v=selected(new,'vpsadminServices')
for node in (old_v,new_v):
    for key in ('rev','narHash','lastModified'): node['locked'].pop(key,None)
assert old == new, 'Changes beyond the selected V locked identity'
print('Only selected V revision/hash/time changed; exact W and whole graph preserved')
PY
  git rev-parse HEAD > "$TRACK/finish-http-c-pins1.sha"
  git log --reverse --format=fuller origin/master..HEAD > "$TRACK/finish-http-c-final.history"
  git diff --binary --full-index origin/master HEAD > "$TRACK/finish-http-c-final.diff"
  git rev-parse HEAD^{tree} > "$TRACK/finish-http-c-final.tree"
) > "$TRACK/finish-http-c-pins1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-c-pins1.exit"
exit "$result"
