set -euo pipefail
final_lock="$RUNNER_TEMP/flake-update-final.lock"
git show HEAD:flake.lock > "$final_lock"
nix shell "$CONFCTL_FLAKE" -c confctl inputs check-update \
  --old-lock "$UPDATE_OLD_LOCK" --new-lock "$final_lock"
