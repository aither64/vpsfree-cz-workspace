# Only missing directories receive root/0755 defaults; keep existing metadata.
vpsadminosPrepareStateDirectory() {
  local path="$1" parent
  if [ -e "$path" ] || [ -L "$path" ]; then
    [ -d "$path" ] || return 1
    return 0
  fi
  parent=$(dirname -- "$path") || return 1
  vpsadminosPrepareStateDirectory "$parent" || return 1
  mkdir -m 0755 -- "$path" || return 1
}
vpsadminosMountRequired() {
  local source="$1" target="$2" options="$3" fsType="$4" selected="$5" directoryBind="$6"
  local backingType backingSource backing mounted=false mountStatus
  shift 6
  # Exact declared early mountpoints must be available, including / when
  # configured. Undeclared host binds retain their existing host contract.
  while [ "$#" -gt 0 ]; do
    backingType="$1" backingSource="$2" backing="$3"
    shift 3
    mountpoint -q -- "$backing" || return 1
    if [ "$backingType" = bind ]; then
      [ -d "$backingSource" ] && [ -d "$backing" ] && [ "$backingSource" -ef "$backing" ] || return 1
    fi
  done
  if [ -e "$target" ] || [ -L "$target" ]; then
    [ -d "$target" ] || return 1
    if mountpoint -q -- "$target"; then
      mounted=true
      if "$directoryBind" && ! { [ -d "$source" ] && [ "$source" -ef "$target" ]; }; then
        printf 'vpsAdminOS: state destination has a different mounted source: %s\n' "$target" >&2
        return 1
      fi
    else
      mountStatus=$?
      # util-linux returns 32 for a directory that is not a mountpoint.
      [ "$mountStatus" -eq 32 ] || return 1
    fi
  fi
  if "$directoryBind"; then
    if "$selected"; then
      vpsadminosPrepareStateDirectory "$source" || return 1
    else
      # A prerequisite bind must not hide unavailable storage with mkdir.
      [ -d "$source" ] || return 1
    fi
  fi
  if "$mounted"; then
    mount -t "$fsType" -o "remount,$options" "$source" "$target" || return 1
  else
    vpsadminosPrepareStateDirectory "$target" || return 1
    mount -t "$fsType" -o "$options" "$source" "$target" || return 1
  fi
  mountpoint -q -- "$target" || return 1
  if "$directoryBind"; then
    [ -d "$source" ] && [ "$source" -ef "$target" ] || return 1
  fi
}
specialMount() {
  local device="$1" mountPoint="$2" options="$3" fsType="$4"
  if [ "$device" = '/fixture/backing storage/nixos' ] && [ "$mountPoint" = /var/lib/nixos ] && [ "$options" = 'x-initrd.mount,x-systemd.requires-mounts-for=/sysroot/fixture/dependency,bind,x-gvfs-hide' ] && [ "$fsType" = auto ]; then
  # Exit the parent activation shell: its ERR trap alone permits users.
  if ! vpsadminosMountRequired "$device" "$mountPoint" "$options" "$fsType" true true filesystem none /; then
    printf 'vpsAdminOS: persisted state unavailable; refusing user allocation\n' >&2
    exit 1
  fi
  return 0
fi

if [ "$device" = none ] && [ "$mountPoint" = / ] && [ "$options" = x-initrd.mount ] && [ "$fsType" = tmpfs ]; then
  # Exit the parent activation shell: its ERR trap alone permits users.
  if ! vpsadminosMountRequired "$device" "$mountPoint" "$options" "$fsType" false false ; then
    printf 'vpsAdminOS: persisted state unavailable; refusing user allocation\n' >&2
    exit 1
  fi
  return 0
fi

if [ "$device" = fixture-dependency ] && [ "$mountPoint" = /fixture/dependency ] && [ "$options" = x-initrd.mount ] && [ "$fsType" = tmpfs ]; then
  # Exit the parent activation shell: its ERR trap alone permits users.
  if ! vpsadminosMountRequired "$device" "$mountPoint" "$options" "$fsType" false false ; then
    printf 'vpsAdminOS: persisted state unavailable; refusing user allocation\n' >&2
    exit 1
  fi
  return 0
fi

  # Keep this fallback aligned with upstream activation-script.nix specialfs.
  # The global earlyMountScript remains responsible for all mount ordering.
  if mountpoint -q "$mountPoint"; then
    local options="remount,$options"
  else
    mkdir -p "$mountPoint"
    chmod 0755 "$mountPoint"
  fi
  mount -t "$fsType" -o "$options" "$device" "$mountPoint"
}
source /nix/store/hj1bphdf5iilj88l9cyd68yr5l093j0b-mounts.sh
