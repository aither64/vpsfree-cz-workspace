#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
out="$record/persistence-declared-payload-diagnosis/quick"
mkdir -p "$out"
[ "$(git rev-parse HEAD)" = edb90d2fe2190d88d8b9d2d21bd0def79eedc898 ]
[ -z "$(git diff --cached --name-only)" ]
[ "$(sha256sum tests/suite/dist-config/nixos-persistence-upgrade.nix | cut -d ' ' -f 1)" = 685d34b22f83d2a354989c48927feb7f1ac722d15903d2f343021d24a700b3eb ]
status=1
trap 'printf "%s\n" "$status" > "$out/status"' EXIT
nix eval --impure --json --file "$record/persistence-declared-payload-diagnosis/verify-inputs.nix" > "$out/inputs.json" 2> "$out/eval.log"
printf '0\n' > "$out/eval.status"
python3 "$record/persistence-declared-payload-diagnosis/compare-inputs.py"
for script in "$out"/*.rb; do ruby -c "$script" > "$script.syntax.log"; done
overcommit --run > "$out/hooks.log" 2>&1
printf '0\n' > "$out/hooks.status"
[ "$(sha256sum tests/suite/dist-config/nixos-persistence-upgrade.nix | cut -d ' ' -f 1)" = 685d34b22f83d2a354989c48927feb7f1ac722d15903d2f343021d24a700b3eb ]
[ -z "$(git diff --cached --name-only)" ]
status=0
