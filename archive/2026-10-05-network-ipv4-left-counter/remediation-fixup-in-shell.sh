#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
for step in ruby-syntax-lint legacy-browser-syntax api-chown react-units react-quick; do
  [[ $(cat "$tracking/remediation-quick2-$step.exit") == 0 ]]
done
sha256sum --check "$tracking/remediation-source-freeze2.sha256"
sha256sum --check "$tracking/remediation-commit-freeze.sha256"
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
split=${1:?Missing split}
case "$split" in
  v-api)
    repo=vpsadmin
    branch=2026-10-05-network-ipv4-left-counter
    previous=6b3628af665049dc095ba985ef0fbe8a22286863
    ;;
  v-webui)
    repo=vpsadmin
    branch=2026-10-05-network-ipv4-left-counter
    previous=$(cat "$tracking/remediation-fixup-v-api.sha")
    ;;
  w)
    repo=vpsadmin-webui
    branch=dev/network-enabled
    previous=811742f50cce2b7724784d0a674c8d4d5dcb6273
    [[ $(cat "$tracking/remediation-final-docs.exit") == 0 ]]
    ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo" ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git rev-parse HEAD) == "$previous" ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
[[ -z $(git diff --cached --name-only) ]]
if [[ $repo == vpsadmin ]]; then
  test -f .overcommit.yml
  [[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
  [[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
  for hook in pre-commit commit-msg; do
    hook_path=$(git rev-parse --git-path "hooks/$hook")
    test -x "$hook_path"
    rg -q 'Overcommit hook integration' "$hook_path"
  done
else
  for framework in .overcommit.yml .pre-commit-config.yaml lefthook.yml lefthook.yaml .husky; do
    test ! -e "$framework"
  done
  node -e 'const p=require("./package.json"); if (p.husky || p["lint-staged"] || p.scripts?.prepare) process.exit(1)'
fi
python3 - "$tracking" "$repo" "$split" <<'PY'
import subprocess, sys
from pathlib import Path
tracking, repo, split = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
plans = ['v-api', 'v-webui'] if repo == 'vpsadmin' else ['w']
allowed = set()
for plan in plans:
    allowed.update((tracking / ('remediation-fixup-' + plan + '.paths')).read_text().splitlines())
changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
changed.update(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())
assert changed <= allowed, sorted(changed - allowed)
if split == 'w':
    assert 'docs/work-log/2026-10-06-network-availability.md' in changed, 'Final checked evidence is not reconciled'
PY
plan="$tracking/remediation-fixup-$split"
sha256sum "$plan.paths" "$plan.message"
git add --pathspec-from-file="$plan.paths"
python3 - "$plan.paths" <<'PY'
import subprocess, sys
from pathlib import Path
expected = set(Path(sys.argv[1]).read_text().splitlines())
staged = set(subprocess.check_output(['git', 'diff', '--cached', '--name-only'], text=True).splitlines())
assert staged and staged <= expected, sorted(staged - expected)
PY
git diff --cached --check
git diff --cached --binary >"$tracking/remediation-fixup-$split-staged.diff"
git commit -F "$plan.message"
git rev-parse HEAD >"$tracking/remediation-fixup-$split.sha"
git show --format=fuller --stat HEAD
