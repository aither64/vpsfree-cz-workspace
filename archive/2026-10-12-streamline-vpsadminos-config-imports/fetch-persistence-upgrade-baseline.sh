#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos || exit 1
nix develop --profile result/config-imports-dev-shell --command bash -c 'nix flake metadata --json github:vpsfreecz/vpsadminos/1150e37b1cc997b1728f2fda806a3433ef55b798 > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-upgrade-baseline.json' > "$record/persistence-upgrade-baseline-fetch.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-upgrade-baseline-fetch.status"
exit "$status"
