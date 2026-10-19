#!/usr/bin/env bash
set -u
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-08-remove-software-pins-support/confctl
task_records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-08-remove-software-pins-support
git rev-parse HEAD > "$task_records/initial2-source.txt"
git status --short >> "$task_records/initial2-source.txt"
nix develop -c bundle exec rspec > "$task_records/initial2-rspec.log" 2>&1
rspec_result=$?
printf '%s\n' "$rspec_result" > "$task_records/initial2-rspec.exit"
nix eval --json .#moduleOptions > "$task_records/initial2-options.json" 2> "$task_records/initial2-options.log"
options_result=$?
printf '%s\n' "$options_result" > "$task_records/initial2-options.exit"
git status --short >> "$task_records/initial2-source.txt"
if [ "$rspec_result" -ne 0 ] || [ "$options_result" -ne 0 ]; then
  exit 1
fi
