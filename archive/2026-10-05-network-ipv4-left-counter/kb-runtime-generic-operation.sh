#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
case "${1-}" in commit|publish) operation=$1 ;; *) exit 64 ;; esac
prefix=kb-runtime-generic-operation-$operation
for suffix in log exit head tree diff hook-context.log default.sha remote-before.sha; do
  test ! -e "$tracking/$prefix.$suffix"
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
sha256sum --check "$tracking/kb-runtime-generic-operation.sha256"
nix-shell "$tracking/kb-runtime-generic-quick4.nix" --run "bash $tracking/kb-runtime-generic-operation-stage.sh $operation"
