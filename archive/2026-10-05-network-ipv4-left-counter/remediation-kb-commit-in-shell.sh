#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(pwd -P) == /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts ]]
[[ $(git branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
[[ $(git rev-parse HEAD) == 873758fd6aec0c03f50a94600e0ceab97946f255 ]]
[[ -z $(git diff --cached --name-only) ]]
[[ $(cat "$tracking/remediation-pins-kb-static-check.exit") == 0 ]]
sha256sum --check "$tracking/remediation-kb-candidate.sha256"
sha256sum --check "$tracking/remediation-pin-operation-freeze.sha256"
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
for framework in .overcommit.yml .pre-commit-config.yaml lefthook.yml lefthook.yaml .husky; do
  test ! -e "$framework"
done
node -e 'const p=require("./package.json"); if (p.husky || p["lint-staged"] || p.scripts?.prepare) process.exit(1)'
python3 - <<'PY'
import subprocess
allowed = {'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'}
changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
changed.update(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())
assert changed and changed <= allowed, sorted(changed - allowed)
PY
git add -- flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml
git diff --cached --check
git diff --cached --binary >"$tracking/remediation-kb-staged.diff"
git commit -F "$tracking/commit-k.message"
[[ -z $(git status --porcelain) ]]
git rev-parse HEAD >"$tracking/remediation-pin-k.sha"
git log --format=fuller 873758fd6aec0c03f50a94600e0ceab97946f255..HEAD >"$tracking/remediation-pins-kb-final-history.log"
