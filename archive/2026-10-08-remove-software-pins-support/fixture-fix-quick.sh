#!/usr/bin/env bash
set -u
fix_records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-08-remove-software-pins-support
bundle exec rspec > "$fix_records/fixture-fix-rspec.log" 2>&1
fix_status=$?
printf '%s\n' "$fix_status" > "$fix_records/fixture-fix-rspec.exit"
[[ $fix_status == 0 ]] || exit "$fix_status"
bundle exec rubocop > "$fix_records/fixture-fix-rubocop.log" 2>&1
fix_status=$?
printf '%s\n' "$fix_status" > "$fix_records/fixture-fix-rubocop.exit"
exit "$fix_status"
