#!/usr/bin/env bash
set -euo pipefail
here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
[ "$#" -eq 3 ] || exit 2
run_dir=$(realpath -- "$1")
parent_mount=$2
parent_user=$3
case "$run_dir" in "$here"/run.*) ;; *) exit 2 ;; esac
[ "$(readlink /proc/self/ns/mnt)" != "$parent_mount" ]
[ "$(readlink /proc/self/ns/user)" != "$parent_user" ]
[ "$(id -u)" = 0 ]
[ "$(findmnt --noheadings --output PROPAGATION --target /)" = private ]
printf 'Private mount namespace: %s\nUser namespace: %s\n' \
  "$(readlink /proc/self/ns/mnt)" "$(readlink /proc/self/ns/user)"
cat /proc/self/uid_map
for tool in findmnt mountpoint mount; do
  [ "$(type -t "$tool")" = file ]
  command -v "$tool"
done
root_id=$(findmnt --noheadings --output ID --target /)
fixture_id=$(findmnt --noheadings --output ID --target "$run_dir")
printf 'Root mount ID: %s; fixture mount ID: %s\n' "$root_id" "$fixture_id"

mount_count() {
  # Targets use no whitespace, so mountinfo's escaped column is literal here.
  awk -v target="$1" '$5 == target { count++ } END { print count+0 }' /proc/self/mountinfo
}

activate() {
  local case_dir=$1 output=$2
  set +e
  (
    set +e
    umask 0022
    _status=0
    _localstatus=0
    trap '_status=1 _localstatus=$?' ERR
    . "$case_dir/activation.sh"
    printf 'Allocator control-flow marker; no account allocation performed.\n' > "$case_dir/$output.marker"
  ) > "$case_dir/$output.log" 2>&1
  activation_status=$?
  set -e
  printf '%s\n' "$activation_status" > "$case_dir/$output.status"
}

expect_failure() {
  local case_dir=$1
  activate "$case_dir" activation
  [ "$activation_status" != 0 ]
  [ ! -f "$case_dir/activation.marker" ]
}

for scenario in fresh existing_metadata repeat missing_unmounted root_backed conflicting_live readonly_preparation; do
  case_dir="$run_dir/$scenario"
  mkdir -- "$case_dir"
  backing="$case_dir/backing storage"
  state_source="$backing/missing/var/lib/nixos"
  log_source="$backing/missing/var/log"
  state_target="$case_dir/target-state"
  log_target="$case_dir/target-log"
  mkdir -- "$backing"

  case "$scenario" in
    missing_unmounted|root_backed)
      # Authorized read-only root sources, never preparation targets. Prebound
      # disposable destinations provide a second refusal before source mkdir
      # or root binding if the original backing guard unexpectedly passes.
      mount -t tmpfs -o size=8m,mode=0755 tmpfs "$backing"
      mkdir -- "$backing/guard-state" "$backing/guard-log" "$state_target" "$log_target"
      mount --bind "$backing/guard-state" "$state_target"
      mount --bind "$backing/guard-log" "$log_target"
      findmnt --noheadings --output ID --target "$state_target" > "$case_dir/mount-id.before"
      if [ "$scenario" = root_backed ]; then
        state_source=/
        log_source=/
      else
        root_child="/vpsadminos-persistence-${run_dir##*.}"
        [ ! -e "$root_child" ] && [ ! -L "$root_child" ]
        state_source="$root_child/state"
        log_source="$root_child/log"
      fi
      [ "$(findmnt --noheadings --output ID --target /)" = "$root_id" ]
      ;;
    readonly_preparation)
      mount -t tmpfs -o ro,size=8m,mode=0755 tmpfs "$backing"
      ;;
    *)
      mount -t tmpfs -o size=8m,mode=0755 tmpfs "$backing"
      ;;
  esac

  if [ "$scenario" = existing_metadata ] || [ "$scenario" = repeat ]; then
    mkdir -p -- "$state_source" "$log_source"
    chmod 0710 -- "$state_source"
    chmod 0700 -- "$log_source"
    printf 'preserved state\n' > "$state_source/payload"
    printf 'preserved log\n' > "$log_source/payload"
    stat -c '%n %u:%g:%a:%d:%i' "$state_source" "$log_source" "$state_source/payload" "$log_source/payload" > "$case_dir/metadata.before"
    sha256sum "$state_source/payload" "$log_source/payload" > "$case_dir/payload.before"
  fi
  if [ "$scenario" = conflicting_live ]; then
    mkdir -- "$backing/wrong-state" "$backing/wrong-log" "$state_target" "$log_target"
    printf 'conflicting state\n' > "$backing/wrong-state/payload"
    mount --bind "$backing/wrong-state" "$state_target"
    mount --bind "$backing/wrong-log" "$log_target"
    findmnt --noheadings --output ID --target "$state_target" > "$case_dir/mount-id.before"
  fi

  python3 "$here/adapt.py" "$run_dir/input-snippet.sh" "$case_dir/activation.sh" \
    "$state_source" "$state_target" "$log_source" "$log_target"
  bash -n "$case_dir/activation.sh"
  case "$scenario" in
    fresh|existing_metadata|repeat)
      activate "$case_dir" activation
      [ "$activation_status" = 0 ] && [ -f "$case_dir/activation.marker" ]
      mountpoint -q -- "$state_target"
      mountpoint -q -- "$log_target"
      [ "$state_source" -ef "$state_target" ] && [ "$log_source" -ef "$log_target" ]
      [ "$(mount_count "$state_target")" = 1 ] && [ "$(mount_count "$log_target")" = 1 ]
      if [ "$scenario" = fresh ]; then
        [ "$(stat -c '%u:%g:%a' "$state_source")" = 0:0:755 ]
        [ "$(stat -c '%u:%g:%a' "$log_source")" = 0:0:755 ]
      else
        stat -c '%n %u:%g:%a:%d:%i' "$state_source" "$log_source" "$state_source/payload" "$log_source/payload" > "$case_dir/metadata.after"
        cmp -- "$case_dir/metadata.before" "$case_dir/metadata.after"
        sha256sum -c "$case_dir/payload.before"
        cmp -- "$state_source/payload" "$state_target/payload"
        cmp -- "$log_source/payload" "$log_target/payload"
      fi
      if [ "$scenario" = repeat ]; then
        findmnt --noheadings --output ID --target "$state_target" > "$case_dir/mount-id.before"
        activate "$case_dir" repeat
        [ "$activation_status" = 0 ] && [ -f "$case_dir/repeat.marker" ]
        [ "$(mount_count "$state_target")" = 1 ] && [ "$(mount_count "$log_target")" = 1 ]
        findmnt --noheadings --output ID --target "$state_target" > "$case_dir/mount-id.after"
        cmp -- "$case_dir/mount-id.before" "$case_dir/mount-id.after"
        sha256sum -c "$case_dir/payload.before"
        stat -c '%n %u:%g:%a:%d:%i' "$state_source" "$log_source" "$state_source/payload" "$log_source/payload" > "$case_dir/metadata.repeat"
        cmp -- "$case_dir/metadata.before" "$case_dir/metadata.repeat"
      fi
      ;;
    *)
      expect_failure "$case_dir"
      if [ "$scenario" != root_backed ]; then
        [ ! -e "$state_source" ] && [ ! -e "$log_source" ]
      fi
      if [ "$scenario" = root_backed ] || [ "$scenario" = missing_unmounted ]; then
        if ! grep -Fq 'state source requires an available non-root backing mount' "$case_dir/activation.log"; then
          printf 'FAIL %s: backing guard unexpectedly passed; prebound destinations prevented root preparation/binding.\n' "$scenario" >&2
          exit 1
        fi
        if [ "$scenario" = missing_unmounted ]; then
          [ ! -e "$root_child" ] && [ ! -L "$root_child" ]
        fi
        [ "$state_target" -ef "$backing/guard-state" ] && [ "$log_target" -ef "$backing/guard-log" ]
        [ "$(mount_count "$state_target")" = 1 ] && [ "$(mount_count "$log_target")" = 1 ]
        findmnt --noheadings --output ID --target "$state_target" > "$case_dir/mount-id.after"
        cmp -- "$case_dir/mount-id.before" "$case_dir/mount-id.after"
      elif [ "$scenario" = conflicting_live ]; then
        [ "$state_target" -ef "$backing/wrong-state" ] && [ "$log_target" -ef "$backing/wrong-log" ]
        [ "$(mount_count "$state_target")" = 1 ] && [ "$(mount_count "$log_target")" = 1 ]
        findmnt --noheadings --output ID --target "$state_target" > "$case_dir/mount-id.after"
        cmp -- "$case_dir/mount-id.before" "$case_dir/mount-id.after"
        [ "$(cat "$state_target/payload")" = 'conflicting state' ]
      else
        [ "$(mount_count "$state_target")" = 0 ] && [ "$(mount_count "$log_target")" = 0 ]
      fi
      ;;
  esac
  cp /proc/self/mountinfo "$case_dir/mountinfo.after"
  printf '0\n' > "$case_dir/status"
  printf 'PASS %s\n' "$scenario"
done

printf 'All real-mount cases passed; allocator markers prove control flow only.\n'
