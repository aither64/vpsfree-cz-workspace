
for path in /var/lib/nixos/uid-map /var/lib/nixos/gid-map /persistent/var/lib/nixos/uid-map /persistent/var/lib/nixos/gid-map; do
  printf "\nAllocation map %s:\n" "$path"
  if [ -f "$path" ]; then cat "$path"; else printf "missing\n"; fi
done
for path in /var/lib/nixos /persistent/var/lib/nixos /var/lib/preservation-test /persistent/var/lib/preservation-test; do
  printf "\nMount and backing identity %s:\n" "$path"
  findmnt --target "$path" --output TARGET,SOURCE,FSTYPE,OPTIONS
  stat -c "%n owner=%u:%g mode=%a device:inode=%d:%i" "$path"
done
printf "\nPersistent payload backing state:\n"
stat -c "%n owner=%u:%g mode=%a device:inode=%d:%i" /var/lib/preservation-test/payload /persistent/var/lib/preservation-test/payload
printf "\nBoot mount and activation order:\n"
grep -n -E "proc/1|source .*mounts|running activation|systemConfig/activate" /run/current-system/init
mount_script=$(sed -n "s/^[[:space:]]*source \([^[:space:]]*-mounts\.sh\).*$/\1/p" /run/current-system/init)
if [ -n "$mount_script" ] && [ -f "$mount_script" ]; then
  grep -n -E "persistent|var/lib/nixos|specialMount" "$mount_script"
fi
printf "\nUser and persistence activation steps:\n"
grep -n -E "specialfs|Activation script snippet|source[[:space:]]+.*-mounts[.]sh|update-users-groups|uid-map|gid-map|persistent|(^|[[:space:]])mount([[:space:]]|$)" /run/current-system/activate

