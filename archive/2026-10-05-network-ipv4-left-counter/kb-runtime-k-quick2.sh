#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-k-quick2
for suffix in log exit; do test ! -e "$tracking/$prefix.$suffix"; done
for check in toolchain syntax runtime closure driver connection-artifacts nix-json; do
  test ! -e "$tracking/$prefix-$check.log"
  test ! -e "$tracking/$prefix-$check.exit"
done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd "$tracking"
test "$(dev-session current)" = 2026-10-05-network-ipv4-left-counter
test -z "${DEV_SESSION_SLUG-}" || test "$DEV_SESSION_SLUG" = 2026-10-05-network-ipv4-left-counter
test -z "${DEV_SESSION_WORKSPACE-}" || test "$DEV_SESSION_WORKSPACE" = /home/aither/workspace/ai/vpsfree.cz
test "${DEV_SESSION_SLUG+x}" = "${DEV_SESSION_WORKSPACE+x}"
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
sha256sum --check "$tracking/$prefix.sha256"
nix-shell "$tracking/$prefix.nix" --run "bash $tracking/$prefix-checks.sh"
