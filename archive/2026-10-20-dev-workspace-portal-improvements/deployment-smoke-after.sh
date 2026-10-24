#!/usr/bin/env bash
set -euo pipefail
umask 077
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = f8f2938b4e2cfd6e5b82657d08f014357817808f
test -z "$(git status --porcelain)"
root=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-smoke/roots
mkdir -p "$root"
nix-store --add-root "$root/playwright" --indirect -r /nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1 >/dev/null
nix-store --add-root "$root/browsers" --indirect -r /nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers >/dev/null
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
export PORTAL_SMOKE_PACKAGE=/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0
export PORTAL_SMOKE_HEAD=f8f2938b4e2cfd6e5b82657d08f014357817808f
export PORTAL_SMOKE_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
export PORTAL_SMOKE_SHARED_SOURCE=/home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261020220147-852e8c510915
export PORTAL_SMOKE_AUTH_USER=aither
export PORTAL_SMOKE_PASSWORD_READ_MODE=ssh
test "$(readlink -f /home/aither/bin/workspace-host)" = "$PORTAL_SMOKE_PACKAGE/bin/workspace-host"
test "$(systemctl --user show workspace-codex@vpsfree-cz.service --property=MainPID --value)" = 3387667
test "$(systemctl --user show workspace-tmux@vpsfree-cz.service --property=MainPID --value)" = 435397
for smoke_unit in workspace-router.service workspace-coordinator.service workspace-portal@vpsfree-cz.service workspace-codex@vpsfree-cz.service workspace-tmux@vpsfree-cz.service; do
  systemctl --user is-active --quiet "$smoke_unit"
done
systemctl --user show workspace-router.service workspace-coordinator.service workspace-portal@vpsfree-cz.service workspace-codex@vpsfree-cz.service workspace-tmux@vpsfree-cz.service --property=Id,ActiveState,SubState,MainPID,FragmentPath
readlink -f /run/current-system
readlink -f /nix/var/nix/profiles/system
curl --fail --silent --show-error --max-time 10 --unix-socket /run/dev-workspaces/router.sock -H 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz' http://localhost/healthz
smoke_unauth_status=$(curl --silent --show-error --max-time 10 --cacert /var/lib/dev-workspaces/public/ca.pem --output /dev/null --write-out '%{http_code}' https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/healthz)
test "$smoke_unauth_status" = 401
printf 'unauthenticated_https=%s\n' "$smoke_unauth_status"
exec nix develop --command node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/deployment-smoke.cjs after /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-smoke/continuity-before.json
