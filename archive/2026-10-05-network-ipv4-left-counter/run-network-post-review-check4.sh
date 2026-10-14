#!/usr/bin/env bash
# Prepared command artifact. The lead must clear the complete final committed
# deliverable through independent review before a fresh watcher executes this.
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
if [[ ${DEV_SESSION_SLUG+x} || ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
fi
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
mode=${1:?Usage: run-network-post-review-check.sh MODE V_SHA W_SHA C_SHA}
v_sha=${2:?Missing reviewed V head}
w_sha=${3:?Missing reviewed W head}
c_sha=${4:?Missing reviewed config head}
for revision in "$v_sha" "$w_sha" "$c_sha"; do [[ $revision =~ ^[0-9a-f]{40}$ ]]; done
for entry in "vpsadmin:$v_sha" "vpsadmin-webui:$w_sha" "vpsfree-cz-configuration:$c_sha"; do
  repo=${entry%%:*}
  revision=${entry#*:}
  [[ $(git -C "$worktrees/$repo" rev-parse HEAD) == "$revision" ]]
  [[ -z $(git -C "$worktrees/$repo" status --porcelain) ]]
done
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  printf 'Starting %s\n' "$name"
  (cd "$directory" && "$@") >"$tracking/post-review4-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/post-review4-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
case "$mode" in
  sql-admission)
    [[ -z ${DATABASE_URL-} ]]
    test ! -f "$worktrees/vpsadmin/api/config/database.yml"
    run_step sql-admission "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#api --command bundle exec rspec spec/models/ip_ownership_concurrency_spec.rb --tag network_admission
    ;;
  vm-routes|vm-export|vm-migration|vm-restore|legacy-admin-cluster)
    case "$mode" in
      vm-routes) selector=network/network-interface-routes-and-host-ips ;;
      vm-export) selector=network/export-lifecycle ;;
      vm-migration) selector=vps/migrate-with-data-check ;;
      vm-restore) selector=storage/restore-after-reinstall-with-descendants-remote ;;
      legacy-admin-cluster) selector=webui#admin-cluster ;;
    esac
    if [[ $mode == vm-routes ]]; then
      # Same committed source and selector: retain the already-passed inventory.
      [[ $(cat "$tracking/post-review-vm-routes-inventory.exit") == 0 ]]
    else
      run_step "$mode-inventory" "$worktrees/vpsadmin" ./test-runner.sh ls "$selector"
    fi
    # UNIX sockets have a 108-byte path limit. Keep this owned isolated test
    # state short, private and unique; retain its exact path with the evidence.
    state_root=$(mktemp -d /tmp/n6-XXXXXXXX)
    [[ -d $state_root && ! -L $state_root ]]
    [[ $(stat -c %u "$state_root") == $(id -u) && $(stat -c %a "$state_root") == 700 ]]
    [[ ! -e "$tracking/post-review4-$mode-state.path" ]]
    printf '%s\n' "$state_root" >"$tracking/post-review4-$mode-state.path"
    printf '%s\n' "session=$DEV_SESSION_SLUG workspace=$DEV_SESSION_WORKSPACE V=$v_sha W=$w_sha C=$c_sha selector=$selector state=$state_root uid=$(id -u)" >"$tracking/post-review4-$mode-ownership.txt"
    run_step "$mode" "$worktrees/vpsadmin" ./test-runner.sh test --jobs 1 --stop-on-failure --state-dir "$state_root" "$selector"
    ;;
  react-desktop|react-mobile)
    if [[ $mode == react-desktop ]]; then project=chromium; else project=mobile-chrome; fi
    run_step "$mode" "$worktrees/vpsadmin-webui" nix develop --command env CI=1 E2E_BASE_URL=http://127.0.0.1:15173 E2E_START_SERVER=1 E2E_RECORD_ARTIFACTS=1 node scripts/playwright.mjs test e2e/specs/admin/network_availability.spec.ts --project="$project" --workers=1 --retries=0 --reporter=line --output="$tracking/post-review4-$mode-results"
    ;;
  react-build)
    run_step "$mode" "$worktrees/vpsadmin-webui" nix develop --command npm run build -- --outDir "$tracking/post-review-react-dist"
    ;;
  config-build)
    run_step "$mode" "$worktrees/vpsfree-cz-configuration" nix develop --command bash "$tracking/build-network-affected-configs.sh"
    ;;
  *) exit 2 ;;
esac
