#!/usr/bin/env bash
# Layout-specific doubles run generated callbacks. The allocator marker proves
# shell control flow only; registered VM tests use the real account allocator.
set -euo pipefail
snippet=$1
early_mounts=$2
mode=$3
fixture_root=$(mktemp -d)
trap 'rm -rf "$fixture_root"' EXIT
bind_state=true
exact=false
configured_target=/var/lib/nixos
case "$mode" in
  declared|undeclared|filesystem) exact=true ;;
  var) configured_target=/var ;;
  var-lib) configured_target=/var/lib ;;
  nonbind) bind_state=false; configured_target=/var/log ;;
esac
scenarios=(fresh existing_metadata matching_live failed_bind failed_remount failed_mount_lookup wrong_result failed_mkdir dangling_target)
if "$bind_state"; then scenarios+=(missing_parents wrong_live source_file parent_file failed_lookup dangling_source); fi
case "$mode" in
  declared|filesystem|transitive) scenarios+=(missing_backing failed_required_remount) ;;
  undeclared) scenarios+=(root_backing absent_undeclared) ;;
esac
case "$mode" in declared|transitive) scenarios+=(matching_backing wrong_backing missing_backing_source) ;; esac
if [ "$mode" = transitive ]; then scenarios+=(missing_transitive); fi
if [ "$mode" = explicit ]; then scenarios+=(missing_dependency failed_unrelated); fi
for scenario in "${scenarios[@]}"; do
  case_root="$fixture_root/$scenario"
  backing="$case_root/backing storage"
  host="$case_root/host storage"
  bridge="$case_root/bridge"
  dependency="$case_root/dependency"
  target="$case_root/state_target"
  log_target="$case_root/log_target"
  mkdir -p "$host/bridge"
  case "$mode" in declared|transitive) ln -s "$host" "$backing" ;; *) mkdir "$backing" ;; esac
  if [ "$mode" = transitive ]; then ln -s "$backing/bridge" "$bridge"; source="$bridge/state"
  elif "$bind_state"; then source="$backing/nixos"
  else source="$case_root/device-file"; touch "$source"
  fi
  log_source="$backing/log"
  before_metadata=
  case "$scenario" in
    missing_parents) source="$(dirname "$source")/new-parent/state" ;;
    existing_metadata)
      if "$bind_state"; then metadata_path="$source"; else metadata_path="$target"; fi
      mkdir "$metadata_path"; chmod 0710 "$metadata_path"
      printf 'existing data\n' > "$metadata_path/payload"
      before_metadata=$(stat -c '%u:%g:%a:%i' "$metadata_path") ;;
    matching_live|failed_remount)
      if "$bind_state"; then mkdir "$source"; ln -s "$source" "$target"; else mkdir "$target"; fi
      printf 'matching data\n' > "$target/payload"
      touch "$case_root/mounted-state" ;;
    wrong_live)
      mkdir "$case_root/wrong"; ln -s "$case_root/wrong" "$target"; touch "$case_root/mounted-state" ;;
    source_file) touch "$source" ;;
    dangling_source) ln -s "$case_root/absent" "$source" ;;
    dangling_target) ln -s "$case_root/absent" "$target" ;;
    wrong_backing)
      mkdir "$case_root/wrong backing"; rm "$backing"; ln -s "$case_root/wrong backing" "$backing" ;;
    missing_backing_source) rmdir "$host/bridge" "$host" ;;
    missing_transitive) rmdir "$host/bridge" ;;
    parent_file)
      if [ "$mode" = transitive ]; then rm "$bridge"; touch "$bridge"
      elif [ -L "$backing" ]; then rm "$backing"; touch "$backing"
      else rmdir "$backing"; touch "$backing"
      fi ;;
    failed_mount_lookup) mkdir "$target" ;;
  esac
  rewrite() {
    sed -e "s|/fixture/backing storage/nixos|$source|g" \
      -e "s|/fixture/bridge/state|$source|g" \
      -e "s|/fixture/backing storage|$backing|g" \
      -e "s|/fixture/host storage|$host|g" \
      -e "s|/fixture/bridge|$bridge|g" \
      -e "s|/fixture/dependency|$dependency|g" \
      -e "s|/fixture/device-file|$source|g" \
      -e "s|/fixture/unrelated|$case_root/unrelated|g" \
      -e "s|\"$configured_target\"|\"$target\"|g" \
      -e "s|'$configured_target'|'$target'|g" \
      -e "s|\"/var/log\"|\"$log_target\"|g" \
      -e "s|'/var/log'|'$log_target'|g" "$1"
  }
  # Filter fixture calls; host /proc,/sys,/run paths are never touched.
  awk '/^specialMount "\/fixture\// || /^specialMount "fixture-/ || /^specialMount .* "\/fixture\// { print }' "$early_mounts" > "$case_root/selected.sh"
  expected_calls=$(wc -l < "$case_root/selected.sh")
  rewrite "$case_root/selected.sh" > "$case_root/mounts.sh"
  rewrite "$snippet" | sed -E "s|^[[:space:]]*source .*|source '$case_root/mounts.sh'|" > "$case_root/activation.sh"
  bash -n "$case_root/activation.sh"
  bash -n "$case_root/mounts.sh"
  set +e
  (
    set +e
    umask 0077
    _status=0
    trap '_status=1' ERR
    mountpoint() {
      local path="${*: -1}"
      if [ "$path" = / ]; then return 0; fi
      case "$path" in
        "$backing") [ "$scenario" != missing_backing ] || return 32; return 0 ;;
        "$bridge") return 0 ;;
        "$dependency") [ "$scenario" != missing_dependency ] || return 32; return 0 ;;
      esac
      [ "$scenario" != failed_mount_lookup ] || return 1
      if [ "$path" = "$target" ]; then test -f "$case_root/mounted-state" || return 32
      elif [ "$path" = "$log_target" ]; then test -f "$case_root/mounted-log" || return 32
      else return 32
      fi
    }
    dirname() { [ "$scenario" != failed_lookup ] || return 1; command dirname "$@"; }
    mkdir() {
      [ "$scenario" != failed_mkdir ] || return 1
      if ! "$bind_state" && [[ "$*" == *"$source"* ]]; then return 1; fi
      command mkdir "$@"
    }
    mount() {
      printf '%s\n' "$*" >> "$case_root/mount-calls"
      local from="${*: -2:1}" to="${*: -1}" options="$4"
      if [ "$to" = "$backing" ]; then
        [ "$scenario" != missing_backing ] && [ "$scenario" != failed_required_remount ]; return
      fi
      if [ "$to" = "$bridge" ]; then return 0; fi
      if [ "$to" = "$dependency" ]; then [ "$scenario" != missing_dependency ]; return; fi
      if [ "$to" = "$case_root/unrelated" ]; then [ "$scenario" != failed_unrelated ]; return; fi
      [ "$scenario" != failed_bind ] && [ "$scenario" != failed_remount ] || return 1
      if [[ "$options" != remount,* ]]; then
        if "$bind_state"; then
          rmdir "$to" || return 1
          if [ "$scenario" = wrong_result ]; then ln -s "$backing" "$to" || return 1
          else ln -s "$from" "$to" || return 1
          fi
        elif [ "$scenario" = wrong_result ]; then return 0
        fi
        if [ "$to" = "$target" ]; then touch "$case_root/mounted-state"; else touch "$case_root/mounted-log"; fi
      fi
    }
    . "$case_root/activation.sh"
    touch "$case_root/allocator-reached"
  ) > "$case_root/output" 2>&1
  status=$?
  set -e
  case "$scenario" in
    fresh|missing_parents|existing_metadata|matching_live|matching_backing|root_backing|absent_undeclared|failed_unrelated)
      [ "$status" = 0 ] && [ -f "$case_root/allocator-reached" ] || { cat "$case_root/output"; exit 1; }
      if "$bind_state"; then [ "$source" -ef "$target" ]; else [ -f "$source" ]; fi
      if "$exact"; then [ "$log_source" -ef "$log_target" ]; fi
      [ "$(wc -l < "$case_root/mount-calls")" = "$expected_calls" ]
      if [ "$scenario" = matching_live ]; then
        if ! "$bind_state"; then expected_options=defaults,mode=0755
        elif [ "$mode" = rbind ]; then expected_options=rbind,x-gvfs-hide
        else expected_options=bind,x-gvfs-hide
        fi
        [[ "$(grep -F -- " $target" "$case_root/mount-calls")" == *"remount,$expected_options"* ]]
        [ "$(grep -Fc -- " $target" "$case_root/mount-calls")" = 1 ]
        [ "$(cat "$target/payload")" = 'matching data' ]
      fi ;;
    *) [ "$status" != 0 ] && [ ! -f "$case_root/allocator-reached" ] || { cat "$case_root/output"; exit 1; } ;;
  esac
  if [ "$scenario" = existing_metadata ]; then
    [ "$before_metadata" = "$(stat -c '%u:%g:%a:%i' "$metadata_path")" ]
    [ "$(cat "$metadata_path/payload")" = 'existing data' ]
  fi
  if [ "$scenario" = fresh ]; then
    if "$bind_state"; then [ "$(stat -c '%a' "$source")" = 755 ]; fi
    [ "$(stat -Lc '%a' "$target")" = 755 ]
  fi
  if [ "$scenario" = missing_parents ]; then
    [ "$(stat -c '%a' "$source")" = 755 ]
    [ "$(stat -c '%a' "$(dirname "$source")")" = 755 ]
  fi
  case "$scenario" in
    wrong_backing|missing_backing|failed_required_remount|missing_dependency) [ ! -e "$source" ]; [ ! -e "$host/nixos" ] ;;
    missing_backing_source) [ ! -e "$host" ] ;;
    missing_transitive) [ ! -e "$host/bridge" ] ;;
    wrong_live) [ ! -e "$source" ]; [ "$target" -ef "$case_root/wrong" ] ;;
    failed_remount) [ -f "$case_root/mounted-state" ]; [ "$(cat "$target/payload")" = 'matching data' ] ;;
  esac
  printf 'PASS %s %s\n' "$mode" "$scenario"
done
