#!/usr/bin/env bash
set -o pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-autostart-log-analysis/vpsadminos/osctld
nix develop ..#osctld --command bundle exec rspec spec/osctld/switch_user_spec.rb
