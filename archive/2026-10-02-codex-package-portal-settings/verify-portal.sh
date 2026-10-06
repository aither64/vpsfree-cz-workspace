#!/usr/bin/env bash
set -euo pipefail
set +x
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
source_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings/dev-workspace
log="$tracking/verification-portal-1.log"
status="$tracking/verification-portal-1.status"
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
date -u
test "$(<"$tracking/system-switch.status")" = 0
test "$(<"$tracking/workspace-switch-retry.status")" = 0
portal_password=$(</var/lib/dev-workspaces/password/password)
[[ "$portal_password" =~ ^[[:xdigit:]]{64}$ ]]
portal_url=https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz
portal_get() {
  # Keep the existing host credential on stdin, never in argv, logs or files.
  printf 'user = "aither:%s"\n' "$portal_password" |
    curl --config - --cacert /var/lib/dev-workspaces/public/ca.pem \
      --fail --silent --show-error --max-time 15 "$@"
}
portal_get --output /dev/null \
  --write-out 'PASS: authenticated stable portal URL, HTTP %{http_code}, TLS verification %{ssl_verify_result}\n' \
  "$portal_url/2026-10-02-codex-package-portal-settings/"
assets=$(mktemp -d /tmp/codex-package-live-assets.XXXXXXXX)
for asset in app.js style.css; do
  portal_get --output "$assets/$asset" "$portal_url/static/$asset"
  cmp "$assets/$asset" "$source_root/portal/internal/web/static/$asset"
  printf 'PASS: live %s matches the reviewed source\n' "$asset"
done
unset portal_password
if rg --quiet --fixed-strings 'Codex settings have unsaved changes' "$assets/app.js"; then
  printf '%s\n' 'FAIL: removed dirty notice remains in deployed JavaScript' >&2
  exit 1
fi
printf '%s\n' 'PASS: removed Codex dirty notice is absent from the live controller'
date -u
