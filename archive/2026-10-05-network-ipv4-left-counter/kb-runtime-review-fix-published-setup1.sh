#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-review-fix-published-setup1
head=68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e
for suffix in log exit metadata.path metadata.exit ci.log ci.exit; do test ! -e "$tracking/$prefix.$suffix"; done
test "$(cat "$tracking/kb-runtime-review-fix-publish1.published.sha")" = "$head"
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
nix build --no-link --print-out-paths "github:vpsfreecz/vpsfree-kb-contracts/$head#runtime-source" > "$tracking/$prefix.metadata.path"
printf '0\n' > "$tracking/$prefix.metadata.exit"
cat "$tracking/$prefix.metadata.path"
(set -e; nix shell --inputs-from "github:vpsfreecz/vpsfree-kb-contracts/$head" nixpkgs#gh nixpkgs#python3 nixpkgs#git --command bash "$tracking/kb-runtime-review-fix-k-cancel-ci.sh") > "$tracking/$prefix.ci.log" 2>&1
printf '0\n' > "$tracking/$prefix.ci.exit"
