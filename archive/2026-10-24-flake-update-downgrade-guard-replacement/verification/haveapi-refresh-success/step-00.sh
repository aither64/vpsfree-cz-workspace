set -euo pipefail
cp flake.lock "$RUNNER_TEMP/flake-update-baseline.lock"
echo "UPDATE_OLD_LOCK=$RUNNER_TEMP/flake-update-baseline.lock" >> "$GITHUB_ENV"
