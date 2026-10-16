#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
worktree_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports
cd "$worktree_root/vpsfree-kb-contracts" || exit
nix develop --profile result/config-imports-dev-shell --command bash -c 'ruby tools/check-kb-annotations.rb && ruby tools/test-kb-annotations.rb && ruby tools/check-contract.rb' > "$record/kb-contract-static.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/kb-contract-static.status"
nix develop --profile result/config-imports-dev-shell --command bin/check > "$record/kb-contract-bin-check.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/kb-contract-bin-check.status"
cd "$worktree_root/vpsadminos" || exit
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file tests/nixos-container-templates-eval.nix > "$record/final-amended-template-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/final-amended-template-eval.status"
exit "$status"
