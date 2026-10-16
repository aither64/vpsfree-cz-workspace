# Abort in the activation shell: its ERR trap alone permits later users.
vpsadminosMountPersistedState() {
  local source="$1" target="$2" options="$3" ancestor="$1" backing rootBacking sourceBacking mountStatus mounted=false
  while [ ! -e "$ancestor" ]; do
    ancestor=$(dirname -- "$ancestor") || return 1
  done
  [ -d "$ancestor" ] || { printf 'vpsAdminOS: state source ancestor is not a directory: %s\n' "$ancestor" >&2; return 1; }
  backing=$(findmnt --noheadings --output ID --target "$ancestor") || return 1
  rootBacking=$(findmnt --noheadings --output ID --target /) || return 1
  [ -n "$backing" ] && [ -n "$rootBacking" ] && [ "$backing" != "$rootBacking" ] || {
    printf 'vpsAdminOS: state source requires an available non-root backing mount: %s\n' "$source" >&2
    return 1
  }
  if [ -e "$target" ]; then
    if mountpoint -q -- "$target"; then
      mounted=true
      [ "$source" -ef "$target" ] || {
        printf 'vpsAdminOS: state destination has a different mounted source: %s\n' "$target" >&2
        return 1
      }
    else
      mountStatus=$?
      # util-linux returns 32 for a directory that is not a mountpoint.
      [ "$mountStatus" -eq 32 ] || return 1
    fi
  fi
  # mkdir -p leaves existing parents and their metadata untouched.
  if [ ! -d "$source" ]; then
    mkdir -p -m 0755 -- "$source" || return 1
  fi
  sourceBacking=$(findmnt --noheadings --output ID --target "$source") || return 1
  [ "$sourceBacking" = "$backing" ] || return 1
  if "$mounted"; then
    mount -t none -o "remount,$options" -- "$source" "$target" || return 1
  else
    if [ ! -d "$target" ]; then
      mkdir -p -m 0755 -- "$target" || return 1
    fi
    mount -t none -o "$options" -- "$source" "$target" || return 1
  fi
  mountpoint -q -- "$target" && [ "$source" -ef "$target" ] || return 1
}
if ! vpsadminosMountPersistedState '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/run.w0gigqry/fresh/backing storage/missing/var/lib/nixos' /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/run.w0gigqry/fresh/target-state bind,x-gvfs-hide; then
  printf 'vpsAdminOS: persisted state unavailable; refusing user allocation\n' >&2
  exit 1
fi

if ! vpsadminosMountPersistedState '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/run.w0gigqry/fresh/backing storage/missing/var/log' /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/run.w0gigqry/fresh/target-log bind,x-gvfs-hide; then
  printf 'vpsAdminOS: persisted state unavailable; refusing user allocation\n' >&2
  exit 1
fi

