#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
nix eval --impure --json --file tests/nixos-container-persistence-eval.nix > "$record/persistence-eval-rerun.json"
ruby -rjson -e 'File.write(ARGV[1], JSON.parse(File.read(ARGV[0])).fetch("shellFixture"))' "$record/persistence-eval-rerun.json" "$record/persistence-activation-snippet.sh"
bash tests/nixos-container-persistence-shell.sh "$record/persistence-activation-snippet.sh"
error_log=$(mktemp)
trap 'rm -f "$error_log"' EXIT
source <(sed -n '/^for release /,$p' tests/nixos-container-eval.sh)
