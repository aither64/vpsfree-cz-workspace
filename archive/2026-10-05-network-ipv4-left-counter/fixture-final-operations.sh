#!/usr/bin/env bash
# Preparation artifact: execute only after the lead inspects this frozen packet.
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
if [[ ${DEV_SESSION_SLUG+x} || ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
fi
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
operation=${1:?Usage: publish-v|publish-w|cancel-v|cancel-w|config|kb V_SHA W_SHA}
shift
case "$operation" in publish-v|publish-w|cancel-v|cancel-w|config|kb) ;; *) exit 2 ;; esac
[[ ! -e "$tracking/fixture-final-$operation-wrapper.log" && ! -e "$tracking/fixture-final-$operation-wrapper.exit" ]]
set +e
(
  set -euo pipefail
  source "$tracking/fixture-final-common.sh"
  run_step() {
    local name="$1" directory="$2"
    shift 2
    local step_result=0
    [[ ! -e "$tracking/fixture-final-$name.log" && ! -e "$tracking/fixture-final-$name.exit" ]]
    (cd "$directory" && "$@") >"$tracking/fixture-final-$name.log" 2>&1 || step_result=$?
    printf '%s\n' "$step_result" >"$tracking/fixture-final-$name.exit"
    printf '%s: exit %s\n' "$name" "$step_result"
    return "$step_result"
  }
  case "$operation" in
    publish-v)
      run_step source-publish-v "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin \
        --command bash "$tracking/fixture-final-publish-in-shell.sh" v "$v_sha" "$w_sha"
      ;;
    publish-w)
      run_step source-publish-w "$worktrees/vpsadmin-webui" nix develop \
        --command bash "$tracking/fixture-final-publish-in-shell.sh" w "$v_sha" "$w_sha"
      ;;
    cancel-v|cancel-w)
      mode=${operation#cancel-}
      run_step "superseded-ci-$mode" "$tracking" nix shell nixpkgs#gh \
        --command bash "$tracking/fixture-final-cancel-ci.sh" "$mode" "$v_sha" "$w_sha"
      ;;
    config|kb)
      verify_published_source v
      verify_published_source w
      case "$operation" in
        config)
          pin_repo=vpsfree-cz-configuration
          base=cde8451718d75929c931db63626b48f7de92fc4f
          old=a6243f09265398368e07695dd531e4a0e312350b
          count=2
          ;;
        kb)
          pin_repo=vpsfree-kb-contracts
          base=873758fd6aec0c03f50a94600e0ceab97946f255
          old=8c396b88ff10bf71c47e2364e7ea1ee34f20d184
          count=1
          ;;
      esac
      pin_root="$worktrees/$pin_repo"
      [[ $(git -C "$pin_root" branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
      [[ $(git -C "$pin_root" rev-parse HEAD) == "$old" && -z $(git -C "$pin_root" status --porcelain) ]]
      [[ $(git -C "$pin_root" remote get-url origin) == "git@github.com:vpsfreecz/$pin_repo.git" ]]
      [[ -z $(git -C "$pin_root" ls-remote --heads origin refs/heads/2026-10-05-network-ipv4-left-counter) ]]
      [[ $(git -C "$pin_root" rev-list --count "$base..$old") == "$count" ]]
      git -C "$pin_root" merge-base --is-ancestor "$base" "$old"
      git -C "$pin_root" fetch --no-tags origin refs/heads/master:refs/remotes/origin/master
      git -C "$pin_root" merge-base --is-ancestor origin/master "$base"
      python3 - "$pin_root" "$base" "$old" "$operation" <<'PY'
import subprocess, sys
repo, base, old, mode = sys.argv[1:]
allowed = {'flake.nix', 'flake.lock'} if mode == 'config' else {
    'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'
}
commits = subprocess.check_output(['git', '-C', repo, 'rev-list', '--reverse', f'{base}..{old}'], text=True).splitlines()
for commit in commits:
    parents = subprocess.check_output(['git', '-C', repo, 'show', '-s', '--format=%P', commit], text=True).split()
    assert len(parents) == 1, 'Unexpected merge in pin-only history'
    changed = set(subprocess.check_output(['git', '-C', repo, 'diff', '--name-only', parents[0], commit], text=True).splitlines())
    assert changed and changed <= allowed, sorted(changed - allowed)
PY
      for suffix in original-history.log original.diff original-head.sha original-tree.sha; do
        [[ ! -e "$tracking/fixture-final-$operation-$suffix" ]]
      done
      git -C "$pin_root" log --format=fuller "$base..$old" >"$tracking/fixture-final-$operation-original-history.log"
      git -C "$pin_root" diff --binary "$base..$old" >"$tracking/fixture-final-$operation-original.diff"
      git -C "$pin_root" rev-parse HEAD >"$tracking/fixture-final-$operation-original-head.sha"
      git -C "$pin_root" rev-parse 'HEAD^{tree}' >"$tracking/fixture-final-$operation-original-tree.sha"
      # Drop only the inspected unpublished pin series; no reset or stash.
      run_step "$operation-return-base" "$pin_root" nix develop --command \
        git -c rebase.autoStash=false rebase --onto "$base" "$old"
      [[ $(git -C "$pin_root" rev-parse HEAD) == "$base" && -z $(git -C "$pin_root" status --porcelain) ]]
      run_step "$operation-generate" "$pin_root" nix develop --command \
        bash "$tracking/fixture-final-pin-in-shell.sh" "$operation" "$v_sha" "$w_sha"
      python3 - "$pin_root" "$base" "$operation" <<'PY'
import subprocess, sys
repo, base, mode = sys.argv[1:]
allowed = {'flake.nix', 'flake.lock'} if mode == 'config' else {
    'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'
}
changed = set(subprocess.check_output(['git', '-C', repo, 'diff', '--name-only', base], text=True).splitlines())
assert changed and changed <= allowed, sorted(changed - allowed)
PY
      ;;
  esac
  sha256sum --check "$tracking/fixture-final-operation-freeze.sha256"
) >"$tracking/fixture-final-$operation-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/fixture-final-$operation-wrapper.exit"
printf 'Fixture final %s exit %s\n' "$operation" "$result"
exit "$result"
