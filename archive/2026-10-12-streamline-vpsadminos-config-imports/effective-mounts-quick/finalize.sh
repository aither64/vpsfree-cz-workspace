#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
out="$record/effective-mounts-quick"
[ "$(git rev-parse HEAD)" = f2b1960dc94ed73936b97f961514dbab164bfbe3 ]
[ -z "$(git diff --cached --name-only)" ]
[ "$(cat "$out/status")" = 0 ]
sha256sum --check "$out/source.sha256"
git branch backup/2026-10-15-config-imports-before-effective-mounts HEAD
overcommit --sign
git add -- docs/containers/nixos.md os/lib/nixos-container/stable/vpsadminos-25.11.nix os/lib/nixos-container/stable/vpsadminos-26.05.nix os/lib/nixos-container/stable/vpsadminos.nix os/lib/nixos-container/unstable/vpsadminos.nix tests/fixtures/nixos-persistence-guests.nix tests/nixos-container-modules-eval.nix tests/nixos-container-persistence-check.nix tests/nixos-container-persistence-eval.nix tests/nixos-container-persistence-shell.sh tests/suite/dist-config/nixos-persistence-upgrade.nix
git write-tree > "$out/expected-tree"
git commit --amend -F "$out/persistence-message.txt"
git branch backup/2026-10-15-config-imports-effective-mounts-technical HEAD
[ "$(git rev-parse 'HEAD^{tree}')" = "$(cat "$out/expected-tree")" ]
GIT_SEQUENCE_EDITOR="$out/reword-selector.py" git rebase -i 4c25fa5f9d1dda58aa0d7019fe351356e6f66c05
[ "$(git rev-parse 'HEAD^{tree}')" = "$(cat "$out/expected-tree")" ]
[ -z "$(git status --porcelain)" ]
git rev-parse HEAD > "$out/committed-head"
git log --format=fuller 4c25fa5f9..HEAD > "$out/committed-history.txt"
