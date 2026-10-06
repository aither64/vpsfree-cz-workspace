#!/usr/bin/env bash
set -euo pipefail

# Prepare-only session artifact. Execute after independent review, through the
# lead's fresh utility watcher, in the caller's pinned Go/Node/GCC environment.
# All fixtures/source copies/state are disposable. No installed package runs.
if [[ $# -ne 1 || ! $1 =~ ^[0-9a-f]{40}$ ]]; then
  printf '%s\n' 'Usage: bash run.sh <exact-reviewed-dev-workspace-commit>' >&2
  exit 2
fi
artifact_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
workspace_root=$(cd "$artifact_dir/../../.." && pwd)
source_root="$workspace_root/worktrees/2026-10-04-upload-display-limits/dev-workspace"
previous_revision=6a972b9ab01077611b2c60e0fc726c185e050315
current_revision=$1
for command_name in git tar mktemp go gofmt node tee; do
  command -v "$command_name" >/dev/null
done
resolved_revision=$(git -C "$source_root" rev-parse --verify "$current_revision^{commit}")
if [[ $resolved_revision != "$current_revision" ]]; then
  printf '%s\n' 'The current revision must be an exact commit, not a tag.' >&2
  exit 2
fi
git -C "$source_root" cat-file -e "$previous_revision^{commit}"
git -C "$source_root" merge-base --is-ancestor "$previous_revision" "$current_revision"

umask 077
experiment_root=$(mktemp -d /tmp/upload-reader.XXXXXXXX)
trap 'rm -rf -- "$experiment_root"' EXIT
export PREPARATION_FIXTURE_ROOT="$experiment_root/fixture"
export TMPDIR="$experiment_root/tmp"
mkdir -p "$PREPARATION_FIXTURE_ROOT" "$TMPDIR" "$experiment_root/current" "$experiment_root/previous" "$experiment_root/logs"
printf '%s\n' 'disposable-upload-reader-experiment' > "$PREPARATION_FIXTURE_ROOT/upload-reader-experiment.marker"
git -C "$source_root" archive "$current_revision" portal | tar -x -C "$experiment_root/current"
git -C "$source_root" archive "$previous_revision" portal | tar -x -C "$experiment_root/previous"
for tree in current previous; do
  destination="$experiment_root/$tree/portal/internal/web/upload_reader_experiment_common_test.go"
  test ! -e "$destination"
  cp "$artifact_dir/reader_common_test.go" "$destination"
done
test ! -e "$experiment_root/current/portal/internal/web/upload_reader_experiment_current_test.go"
test ! -e "$experiment_root/previous/portal/internal/web/upload_reader_experiment_previous_test.go"
cp "$artifact_dir/reader_current_test.go" "$experiment_root/current/portal/internal/web/upload_reader_experiment_current_test.go"
cp "$artifact_dir/reader_previous_test.go" "$experiment_root/previous/portal/internal/web/upload_reader_experiment_previous_test.go"
gofmt -w "$experiment_root/current/portal/internal/web/upload_reader_experiment_common_test.go" \
  "$experiment_root/current/portal/internal/web/upload_reader_experiment_current_test.go" \
  "$experiment_root/previous/portal/internal/web/upload_reader_experiment_common_test.go" \
  "$experiment_root/previous/portal/internal/web/upload_reader_experiment_previous_test.go"
printf 'previous=%s current=%s\n' "$previous_revision" "$current_revision"
go version
node --version

run_phase() {
  local phase_name=$1 tree=$2 selector=$3
  local phase_log="$experiment_root/logs/$phase_name.jsonl"
  go -C "$experiment_root/$tree/portal" test -mod=readonly -tags=preparation_compatibility \
    -run "^$selector$" -count=1 -timeout=60s -json ./internal/web | tee "$phase_log"
  node - "$phase_log" "$selector" <<'JS'
const fs = require('node:fs'), assert = require('node:assert/strict');
const events = fs.readFileSync(process.argv[2], 'utf8').trim().split('\n').filter(Boolean).map(JSON.parse);
const selected = process.argv[3];
assert.equal(events.filter(event => event.Action === 'run' && event.Test === selected).length, 1, 'selector must execute exactly one test');
assert.equal(events.filter(event => event.Action === 'pass' && event.Test === selected).length, 1, 'selected test must pass');
assert.equal(events.filter(event => event.Action === 'fail' || event.Action === 'skip').length, 0, 'no failure or skip may count as evidence');
assert.equal(events.filter(event => event.Action === 'pass' && !event.Test).length, 1, 'package must pass');
console.log(`Nonzero phase verified: ${selected} (1 test, passed, no skips)`);
JS
}

run_phase current-write current TestUploadReaderExperimentWriteFifty
run_phase previous-reject previous TestUploadReaderExperimentPreviousRejectsFifty
run_phase current-compact current TestUploadReaderExperimentCompactFifty
run_phase previous-accept previous TestUploadReaderExperimentPreviousAcceptsMapping
printf '%s\n' 'Upload reader experiment passed: four nonzero phases; prior full reader rejects 50-file snapshot without state mutation; prior reader accepts normally compacted terminal mapping without state mutation.'
