#!/usr/bin/env bash
# Synthetic excerpt for filtering only; never execute this fixture.
set +e

#### Activation script snippet: specialfs
specialfs() {
  source /nix/store/fixture-source-of-special-mounts.sh
}
specialfs

#### Activation script snippet: users
/nix/store/fixture-update-users-groups.pl
test -e /var/lib/nixos/uid-map
test -e /var/lib/nixos/gid-map

#### Activation script snippet: persistence
test -d /persistent
mount --bind /temporary-source /temporary-target

# This unrelated source invocation must be excluded.
source /nix/store/fixture-setup.sh
#### Activation script snippet: complete
