#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-e-review-ci2
for suffix in log exit current.json; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
nix shell --inputs-from 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=f6d2c080469b224ac77765aecd76a6d531358363' nixpkgs#gh --command bash -ec '
 tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
 bash "$tracking/kb-runtime-e-review-cancel-ci2.sh"
 gh run list --repo vpsfreecz/dev-workspace --branch 2026-10-05-network-ipv4-left-counter --limit 30 --json databaseId,headSha,headBranch,status,conclusion,url,workflowName >"$tracking/kb-runtime-e-review-ci2.current.json"
'
