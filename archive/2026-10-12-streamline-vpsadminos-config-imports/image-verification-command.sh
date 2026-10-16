#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
export VPSADMINOS_CONFIG="$record/image-host-metadata.nix"
image_state_dir=$(cat "$record/image-state-dir")
cd "$source" || exit
for image in nixos-26.05 nixos-26.05-impermanence nixos-unstable nixos-unstable-impermanence; do
  ./test-runner.sh test --state-dir "$image_state_dir" --test-config "$record/image-test-config.nix" --fresh --jobs 1 "image-scripts/test@$image" > "$record/image-$image.log" 2>&1
  status=$?
  printf '%s\n' "$status" > "$record/image-$image.status"
  if [ "$status" -ne 0 ]; then exit "$status"; fi
done
