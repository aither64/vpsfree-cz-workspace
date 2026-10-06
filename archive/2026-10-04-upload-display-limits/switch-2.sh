#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits
source_tree=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/workspace
predecessor=/nix/store/s7y4bgq7iw0idkv5japb538kfwphk4nf-dev-workspace-0.2.0
portal="$predecessor/bin/workspace-portal"
profile=/home/aither/.local/state/dev-workspaces/profile
log="$records/profile-switch-2.log"
exec >> "$log" 2>&1
finish() {
  printf '%s\n' "$1" > "$records/profile-switch-2.exit.tmp"
  mv "$records/profile-switch-2.exit.tmp" "$records/profile-switch-2.exit"
  exit "$1"
}
assert_sources() {
  test "$(git -C "$source_tree" rev-parse HEAD)" = 88c0b957a1e870e4ce36a1743f72b529ba4825e1 &&
  test -z "$(git -C "$source_tree" status --porcelain)" &&
  test "$(readlink -f /run/current-system)" = /nix/store/ihrndjkq7sh2i6ldl5kh4m6cvbb192di-nixos-system-aitherdev-26.05.20261003.825e202 &&
  test "$(readlink -f "$profile")" = "$predecessor" &&
  test "$(dev-session current)" = 2026-10-04-upload-display-limits
}
while true; do
  date --iso-8601=seconds
  assert_sources || finish 90
  attempt="$records/profile-switch-attempt-2.log"
  "$portal" thread require-idle --codex-home /home/aither/.codex --socket /run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock --thread-id 01a10862-314f-7670-8f7e-6d94c61eb80c --cwd "$records" > "$attempt" 2>&1
  rc=$?
  if test "$rc" = 0; then
    "$portal" team require-idle --codex-home /home/aither/.codex --socket /run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock --user-state-root /home/aither/.local/state/dev-workspaces --workspace /home/aither/workspace/ai/vpsfree.cz --session-slug 2026-10-04-upload-display-limits --root-thread-id 01a10862-314f-7670-8f7e-6d94c61eb80c --cwd "$records" >> "$attempt" 2>&1
    rc=$?
  fi
  if test "$rc" = 0; then
    printf 'switching\n' > "$records/profile-switch-2.phase"
    /home/aither/bin/workspace-host switch --source "$source_tree" >> "$attempt" 2>&1
    rc=$?
  fi
  cat "$attempt"
  if test "$rc" = 0; then
    printf 'activated\n' > "$records/profile-switch-2.phase"
    finish 0
  fi
  if test "$(readlink -f "$profile")" != "$predecessor"; then
    printf 'selected forward package requires recovery\n' > "$records/profile-switch-2.phase"
    finish "$rc"
  fi
  if grep -Eq 'Codex thread .*is not idle.*inProgress|Codex thread .*has pending|Codex thread .*queued messages' "$attempt"; then
    printf 'waiting for busy Codex; next check in900seconds\n' > "$records/profile-switch-2.phase"
    sleep 900
  else
    printf 'refused; requires coordinator diagnosis\n' > "$records/profile-switch-2.phase"
    finish "$rc"
  fi
done
