#!/usr/bin/env bash
set -eu
root=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-04-upload-display-limits
records="$root/work/$slug"
cd "$root/worktrees/$slug/codex-web"
test "$(git rev-parse HEAD)" = 3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c
nix flake check --print-build-logs > "$records/packaged-codex-web.log" 2>&1
cd "$root/worktrees/$slug/dev-workspace"
test "$(git rev-parse HEAD)" = 3edc605d81a30a4d49560426e0128b388b856493
nix flake check --print-build-logs > "$records/packaged-dev-workspace.log" 2>&1
nix shell --inputs-from . nixpkgs#nodejs nixpkgs#chromium -c env \
 PLAYWRIGHT_MODULE=/nix/store/2xc3ahwfjaa3k3wpn4gslgws25swsyd7-playwright-core-1.59.1 \
 CHROMIUM_EXECUTABLE=/nix/store/789yhb4v2kq51jwl4acmmjvxs7mfrlhv-chromium-152.0.7977.75/bin/chromium \
 CODEX_WEB_SOURCE="$root/worktrees/$slug/codex-web" \
 node test/creation_browser.cjs > "$records/creation-browser.log" 2>&1
