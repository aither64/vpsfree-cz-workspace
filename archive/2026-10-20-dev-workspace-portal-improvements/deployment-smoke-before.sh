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
export PORTAL_SMOKE_PACKAGE=/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0
export PORTAL_SMOKE_HEAD=f8f2938b4e2cfd6e5b82657d08f014357817808f
export PORTAL_SMOKE_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
export PORTAL_SMOKE_SHARED_SOURCE=/home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261020220147-852e8c510915
export PORTAL_SMOKE_AUTH_USER=aither
export PORTAL_SMOKE_PASSWORD_READ_MODE=ssh
systemctl --user show workspace-router.service workspace-coordinator.service workspace-portal@vpsfree-cz.service workspace-codex@vpsfree-cz.service workspace-tmux@vpsfree-cz.service --property=Id,ActiveState,SubState,MainPID,FragmentPath
readlink -f /run/current-system
readlink -f /nix/var/nix/profiles/system
curl --fail --silent --show-error --max-time 10 --unix-socket /run/dev-workspaces/router.sock -H 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz' http://localhost/healthz
curl --silent --show-error --max-time 10 --cacert /var/lib/dev-workspaces/public/ca.pem --output /dev/null --write-out 'unauthenticated_https=%{http_code}\n' https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/healthz
exec nix develop --command node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/deployment-smoke.cjs before /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-smoke/continuity-before.json
