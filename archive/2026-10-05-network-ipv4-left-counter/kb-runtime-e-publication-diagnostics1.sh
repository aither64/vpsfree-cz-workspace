#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-e-publication-diagnostics1
for suffix in log exit repo.json repo.exit rules.json rules.exit; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
nix shell --inputs-from 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=f6d2c080469b224ac77765aecd76a6d531358363' nixpkgs#gh --command bash -ec '
 tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
 prefix=kb-runtime-e-publication-diagnostics1
 set +e
 gh api repos/vpsfreecz/dev-workspace --jq "{default_branch,archived,disabled,permissions,size}" >"$tracking/$prefix.repo.json"
 status=$?
 printf "%s\n" "$status" >"$tracking/$prefix.repo.exit"
 test "$status" = 0 || exit "$status"
 gh api "repos/vpsfreecz/dev-workspace/rulesets?includes_parents=true" --jq "[.[] | {id,name,enforcement,target}]" >"$tracking/$prefix.rules.json"
 status=$?
 printf "%s\n" "$status" >"$tracking/$prefix.rules.exit"
 exit "$status"
'
