#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports
cd "$group/workspace" || exit 1
nix shell --inputs-from . nixpkgs#ruby --command ruby test/agent_instructions_test.rb > "$record/instruction-workspace-tests.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/instruction-workspace-tests.status"
[ "$status" -eq 0 ] || exit "$status"
cd "$group/vpsfree-dev-workspace" || exit 1
nix shell --inputs-from . nixpkgs#ruby --command ruby test/skill_policy_test.rb > "$record/instruction-skill-tests.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/instruction-skill-tests.status"
[ "$status" -eq 0 ] || exit "$status"
cd "$group/vpsfree-dev-workspace" || exit 1
nix shell --impure --expr '(builtins.getFlake (toString ./.)).inputs.nixpkgs.legacyPackages.x86_64-linux.python3.withPackages (p: [ p.pyyaml ])' --command python3 /home/aither/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/mandatory-change-review > "$record/instruction-skill-validator.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/instruction-skill-validator.status"
exit "$status"
