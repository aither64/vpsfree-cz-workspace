#!/usr/bin/env bash
# Proposed guest fragment: syntax only, never executed here.
set -e
mountpoint -q -- /guest-backing
test /persistent/backing -ef /guest-backing
mountpoint -q -- /var/lib/preservation-test
test -d /guest-backing/var/lib/preservation-test
test -d /var/lib/preservation-test
test /guest-backing/var/lib/preservation-test -ef /var/lib/preservation-test
source_entries=$(find -H /guest-backing/var/lib/preservation-test -mindepth 1 -maxdepth 1 -print -quit) || exit 1
target_entries=$(find -H /var/lib/preservation-test -mindepth 1 -maxdepth 1 -print -quit) || exit 1
test -z "$source_entries"
test -z "$target_entries"
payload_inode=$(stat -Lc '%d:%i' -- /var/lib/preservation-test)
install -d -m 0750 -o preservation-test -g preservation-test -- /var/lib/preservation-test
test "$payload_inode" = "$(stat -Lc '%d:%i' -- /var/lib/preservation-test)"
test /guest-backing/var/lib/preservation-test -ef /var/lib/preservation-test
