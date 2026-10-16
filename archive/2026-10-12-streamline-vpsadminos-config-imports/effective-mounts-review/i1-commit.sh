#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
[ "$(git rev-parse HEAD)" = bf74af0b76accdf844ad6ffbea75db6c409f386e ]
[ -z "$(git diff --cached --name-only)" ]
[ "$(cat "$record/effective-mounts-i1-quick/status")" = 0 ]
sha256sum --check "$record/effective-mounts-i1-quick/source.sha256"
git branch backup/2026-10-15-config-imports-before-i1 HEAD
git add -- os/lib/nixos-container/stable/vpsadminos-25.11.nix os/lib/nixos-container/stable/vpsadminos-26.05.nix os/lib/nixos-container/stable/vpsadminos.nix os/lib/nixos-container/unstable/vpsadminos.nix tests/nixos-container-persistence-shell.sh tests/suite/dist-config/nixos-persistence-upgrade.nix
git write-tree > "$record/effective-mounts-review/i1-expected-tree"
git commit --amend -F "$record/effective-mounts-review/persistence-v9-message.txt"
[ "$(git rev-parse 'HEAD^{tree}')" = "$(cat "$record/effective-mounts-review/i1-expected-tree")" ]
[ -z "$(git status --porcelain)" ]
[ "$(git rev-parse HEAD^)" = b2669ce00d440c1e05eb07b0e5bb4d201f3e5161 ]
git rev-parse HEAD > "$record/effective-mounts-review/i1-final-head"
git rev-parse 'HEAD^{tree}' > "$record/effective-mounts-review/i1-final-tree"
