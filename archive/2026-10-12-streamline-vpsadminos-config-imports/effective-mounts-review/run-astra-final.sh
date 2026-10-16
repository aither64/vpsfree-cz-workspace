#!/usr/bin/env bash
set -uo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/effective-mounts-review
started=$(date +%s)
status=0
codex exec -m gpt-6-astra -c 'model_reasoning_effort="xhigh"' -s read-only --json -o "$record/astra-final-report.md" - < "$record/astra-final-prompt.txt" > "$record/astra-final-events.jsonl" 2> "$record/astra-final-stderr.log" || status=$?
printf '%s\n' "$status" > "$record/astra-final-cli.status"
printf '%s\n' "$(( $(date +%s) - started ))" > "$record/astra-final-elapsed-seconds"
exit "$status"
