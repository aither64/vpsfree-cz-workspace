#!/usr/bin/env bash
set -euo pipefail
unit=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-declared-payload-diagnosis
[ "$(cat "$unit/quick/eval.status")" = 0 ]
[ "$(sha256sum tests/suite/dist-config/nixos-persistence-upgrade.nix | cut -d ' ' -f 1)" = 685d34b22f83d2a354989c48927feb7f1ac722d15903d2f343021d24a700b3eb ]
for script in "$unit/quick"/*.rb; do ruby -c "$script" > "$script.syntax.log"; done
printf '0\n' > "$unit/quick/ruby.status"
code=0
overcommit --run > "$unit/quick/hooks.log" 2>&1 || code=$?
printf '%s\n' "$code" > "$unit/quick/hooks.status"
[ "$code" = 0 ]
[ -z "$(git diff --cached --name-only)" ]
printf '0\n' > "$unit/quick/source-checks.status"
