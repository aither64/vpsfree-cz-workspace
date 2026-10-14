#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
test ! -e "$tracking/kb-runtime-k-metadata.log"
test ! -e "$tracking/kb-runtime-k-metadata.exit"
test ! -e "$tracking/kb-runtime-k-metadata.path"
set -o noclobber
exec > >(tee "$tracking/kb-runtime-k-metadata.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/kb-runtime-k-metadata.exit"' EXIT
test "$(cat "$tracking/kb-runtime-k-published.sha")" = 93a16d6cecb6bc847ec9335a3f170eb8b301ab56
nix build --no-link --no-update-lock-file --print-out-paths github:vpsfreecz/vpsfree-kb-contracts/93a16d6cecb6bc847ec9335a3f170eb8b301ab56#runtime-source >"$tracking/kb-runtime-k-metadata.path"
cat "$tracking/kb-runtime-k-metadata.path"
