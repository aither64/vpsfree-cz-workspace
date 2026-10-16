#!/usr/bin/env bash
set -euo pipefail
# Dependency-only packaging derivation, no application/integration tests.
nix build --no-link --print-out-paths --impure --expr 'let f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace"; in f.packages.x86_64-linux.default.goModules.overrideAttrs (_: { outputHash = "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="; })'
