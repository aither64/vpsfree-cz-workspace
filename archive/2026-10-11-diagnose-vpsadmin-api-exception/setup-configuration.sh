#!/usr/bin/env bash
set -eu
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/vpsfree-cz-configuration
nix develop -c bash -c 'set -e; export GEM_HOME="$PWD/.gems"; export PATH="$GEM_HOME/bin:$PATH"; export BUNDLE_GEMFILE="$PWD/Gemfile"; NIX_ENFORCE_PURITY=0 bundle install'
