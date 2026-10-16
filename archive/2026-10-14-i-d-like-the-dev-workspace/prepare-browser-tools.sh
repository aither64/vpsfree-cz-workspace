#!/usr/bin/env bash
set -euo pipefail
nix build --no-link --impure --expr 'let f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace"; p = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in p.playwright-test'
