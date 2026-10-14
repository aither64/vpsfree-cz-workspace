#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
prefix=kb-runtime-e-review-eval1
for suffix in log exit derivations.json before.sha after.sha; do test ! -e "$tracking/$prefix.$suffix"; done
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd "$root"
test "$(dev-session current)" = 2026-10-05-network-ipv4-left-counter
test "$(git rev-parse HEAD)" = f6d2c080469b224ac77765aecd76a6d531358363
test -z "$(git status --porcelain=v1 --untracked-files=all)"
sha256sum flake.nix flake.lock >"$tracking/$prefix.before.sha"
nix eval --json --no-update-lock-file .#checks.x86_64-linux --apply 'c: { package = c.package.drvPath; compatibility = c.compatibility-package.drvPath; kb = c.kb-provider-package.drvPath; contract = c.kb-provider-contract.drvPath; metadata = c.package-metadata.drvPath; source = c.organization-source.drvPath; }' >"$tracking/$prefix.derivations.json"
sha256sum flake.nix flake.lock >"$tracking/$prefix.after.sha"
cmp "$tracking/$prefix.before.sha" "$tracking/$prefix.after.sha"
test "$(git rev-parse HEAD)" = f6d2c080469b224ac77765aecd76a6d531358363
test -z "$(git status --porcelain=v1 --untracked-files=all)"
cat "$tracking/$prefix.derivations.json"
