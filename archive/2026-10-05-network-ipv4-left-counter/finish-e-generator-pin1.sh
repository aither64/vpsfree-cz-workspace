#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd "$tracking"
test "$(/home/aither/bin/dev-session current)" = 2026-10-05-network-ipv4-left-counter
test ! -e finish-e-generator-pin1.log
test ! -e finish-e-generator-pin1.exit
set -o noclobber
exec > >(tee finish-e-generator-pin1.log) 2>&1
trap 'result=$?; printf "%s\n" "$result" >finish-e-generator-pin1.exit' EXIT
sha256sum --check finish-e-generator-pin1.controls.sha256
nix-shell "$tracking/finish-e-generator-pin1.nix" --run "python3 $tracking/finish-e-generator-pin1.py"
