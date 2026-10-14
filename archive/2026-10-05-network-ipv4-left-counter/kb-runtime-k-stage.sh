#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
cd "$repo"
test "$(git rev-parse HEAD)" = a50f8c1a11ea642edf823f04521f9eaa97132fd2
test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter-kb-runtime
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsfree-kb-contracts.git
test -z "$(git diff --cached --name-only)"
sha256sum --check "$tracking/kb-runtime-k-final2-source.manifest" >/dev/null
sha256sum --check "$tracking/kb-runtime-k-final2-source.sha256" >/dev/null
diff -u "$tracking/kb-runtime-k-final2-source.status" <(git status --porcelain=v1 --untracked-files=all)
for check in quick3-toolchain quick3-syntax quick3-runtime quick3-closure quick3-driver quick3-connection-artifacts quick4-nix-json quick5-toolchain quick5-parse quick5-driver quick5 quick6-toolchain quick6-syntax quick8-syntax quick8-profile quick8-scenarios quick8-export quick8; do
  test "$(cat "$tracking/kb-runtime-k-$check.exit")" = 0
done
git fetch origin master
git merge-base --is-ancestor origin/master HEAD
git log --oneline HEAD..origin/master >"$tracking/kb-runtime-k-source-default-comparison.log"
mapfile -t paths <"$tracking/kb-runtime-k-final2-source.paths"
git add -- "${paths[@]}"
python3 - "$tracking" <<'PY'
import pathlib, subprocess, sys
t=pathlib.Path(sys.argv[1])
planned=(t/'kb-runtime-k-final2-source.paths').read_text().splitlines()
actual=subprocess.check_output(['git','diff','--cached','--no-renames','--name-only','-z']).decode().split('\0')[:-1]
if len(planned)!=54 or len(set(planned))!=54 or set(actual)!=set(planned):
 raise SystemExit('staged path set differs')
PY
git diff --cached --check
git diff --cached --exit-code -- flake.lock captures.json contract screenshots
sha256sum --check "$tracking/kb-runtime-k-final2-source.sha256" >/dev/null
git diff --cached --binary >"$tracking/kb-runtime-k-source-staged.diff"
git diff --cached --stat >"$tracking/kb-runtime-k-source-staged.stat"
git write-tree >"$tracking/kb-runtime-k-source-staged.tree"
cat "$tracking/kb-runtime-k-source-staged.stat"
