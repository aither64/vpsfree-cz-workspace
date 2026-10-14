#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(pwd -P) == /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts ]]
[[ $(git branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
[[ $(git rev-parse HEAD) == 873758fd6aec0c03f50a94600e0ceab97946f255 ]]
[[ -z $(git diff --cached --name-only) ]]
[[ $(cat "$tracking/visibility-review-fix-source-pins.exit") == 0 ]]
sha256sum --check "$tracking/visibility-review-fixed-kb-candidate.sha256"
sha256sum --check "$tracking/visibility-final-operation.sha256"
sha256sum --check "$tracking/visibility-review-fix-operation.sha256"
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
for framework in .overcommit.yml .pre-commit-config.yaml lefthook.yml lefthook.yaml .husky; do
  test ! -e "$framework"
done
node -e 'const p=require("./package.json"); if (p.husky || p["lint-staged"] || p.scripts?.prepare) process.exit(1)'
python3 - <<'PYHOOK'
from pathlib import Path
import subprocess
configured = subprocess.run(['git', 'config', '--get', 'core.hooksPath'], capture_output=True, text=True)
assert configured.returncode == 1 or (configured.returncode == 0 and not configured.stdout.strip()), 'Inspect custom hooksPath before commit'
hooks = Path(subprocess.check_output(['git', 'rev-parse', '--git-path', 'hooks'], text=True).strip())
assert not [p.name for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')], 'Inspect undeclared active hooks before commit'
PYHOOK
python3 - <<'PY'
import subprocess
allowed = {'flake.nix', 'flake.lock', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml'}
changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
changed.update(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())
assert changed and changed <= allowed, sorted(changed - allowed)
PY
git add -- flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml
git diff --cached --check
git diff --cached --binary >"$tracking/visibility-review-fixed-kb-staged.diff"
cmp "$tracking/visibility-review-fixed-kb-candidate.diff" "$tracking/visibility-review-fixed-kb-staged.diff"
git commit -F "$tracking/commit-k.message"
[[ -z $(git status --porcelain) && $(git rev-parse HEAD^) == 873758fd6aec0c03f50a94600e0ceab97946f255 ]]
[[ $(git rev-list --count 873758fd6aec0c03f50a94600e0ceab97946f255..HEAD) == 1 ]]
git rev-parse HEAD >"$tracking/visibility-review-fixed-kb-final.sha"
git log --format=fuller 873758fd6aec0c03f50a94600e0ceab97946f255..HEAD >"$tracking/visibility-review-fixed-kb-final-history.log"
git diff --binary 873758fd6aec0c03f50a94600e0ceab97946f255..HEAD >"$tracking/visibility-review-fixed-kb-final.diff"
