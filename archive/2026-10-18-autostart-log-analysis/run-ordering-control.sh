#!/usr/bin/env bash
set -euo pipefail

# Run inside the prepared osctld Nix shell after native compilation and the
# focused spec pass. Only the baseline control process loads the old helper.
worktree=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-autostart-log-analysis/vpsadminos
base=d531fc90888e3eabf17889b0dff94c648866cea4
example='waits for cleanup with over 1024 inherited FDs before lowering the child limit'
control_dir=$(mktemp -d /tmp/autostart-order-control.XXXXXX)
trap 'rm -rf -- "$control_dir"' EXIT

cd "$worktree/osctld"
git show "$base:osctld/lib/osctld/switch_user.rb" > "$control_dir/baseline.rb"
cat > "$control_dir/load-baseline.rb" <<'RUBY'
require 'osctld/switch_user'

# Keep the corrected version's private reap helper solely for the spec's
# failure cleanup; replace the implementation under test with the exact base.
load File.join(__dir__, 'baseline.rb')
RUBY

bundle exec rspec spec/osctld/switch_user_spec.rb --example "$example"

set +e
bundle exec rspec --require "$control_dir/load-baseline.rb" \
  spec/osctld/switch_user_spec.rb --example "$example" > "$control_dir/baseline.log" 2>&1
baseline_status=$?
set -e
cat "$control_dir/baseline.log"
if [ "$baseline_status" -ne 1 ]; then
  echo "Unexpected baseline exit: $baseline_status (expected RSpec failure 1)" >&2
  exit 1
fi
if ! rg -q ':applying_limits' "$control_dir/baseline.log"; then
  echo 'Baseline failed without the expected premature-limit ordering evidence' >&2
  exit 1
fi
echo 'CONTROL: corrected helper passes; exact baseline applies limits before preparation.'
