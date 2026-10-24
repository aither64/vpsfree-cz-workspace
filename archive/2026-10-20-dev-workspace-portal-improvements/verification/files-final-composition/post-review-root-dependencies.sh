#!/usr/bin/env bash
set -euo pipefail
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-final-composition/guards.py
root_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-final-composition/operation-roots
mkdir -p "$root_dir"
test -d /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0
nix-store --add-root "$root_dir/dependency-0" --indirect --realise /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0
test -d /nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1
nix-store --add-root "$root_dir/dependency-1" --indirect --realise /nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1
test -d /nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
nix-store --add-root "$root_dir/dependency-2" --indirect --realise /nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
test -d /nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0
nix-store --add-root "$root_dir/dependency-3" --indirect --realise /nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0
