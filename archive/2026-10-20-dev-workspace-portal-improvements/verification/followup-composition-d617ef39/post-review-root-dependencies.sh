#!/usr/bin/env bash
set -euo pipefail
root_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/operation-roots
mkdir -p "$root_dir"
test -d /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0
nix-store --add-root "$root_dir/dependency-0" --indirect --realise /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0
test -d /nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1
nix-store --add-root "$root_dir/dependency-1" --indirect --realise /nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1
test -d /nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
nix-store --add-root "$root_dir/dependency-2" --indirect --realise /nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
test -d /nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0
nix-store --add-root "$root_dir/dependency-3" --indirect --realise /nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0
test -d /nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0
nix-store --add-root "$root_dir/dependency-4" --indirect --realise /nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0
test -d /nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0
nix-store --add-root "$root_dir/dependency-5" --indirect --realise /nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0
test -d /nix/store/4nvdi78v3rx435p09bk9hxmnp0z0ig7w-xauth-1.1.5
nix-store --add-root "$root_dir/dependency-6" --indirect --realise /nix/store/4nvdi78v3rx435p09bk9hxmnp0z0ig7w-xauth-1.1.5
test -d /nix/store/iyzy0zy23i1njxar2sd1hr4hmk56dalh-xvfb-run-1+g87f6705
nix-store --add-root "$root_dir/dependency-7" --indirect --realise /nix/store/iyzy0zy23i1njxar2sd1hr4hmk56dalh-xvfb-run-1+g87f6705
