#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
case "${1:?Missing commit split}" in
  v-api)
    repo=vpsadmin
    branch=2026-10-05-network-ipv4-left-counter
    previous=c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
    plan=commit-v-api
    ;;
  v-webui)
    repo=vpsadmin
    branch=2026-10-05-network-ipv4-left-counter
    previous=$(cat "$tracking/source-commit-v-api.sha")
    plan=commit-v-webui
    ;;
  w)
    repo=vpsadmin-webui
    branch=dev/network-enabled
    previous=02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51
    plan=commit-w
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
  # No hook framework is declared in the reviewed WebUI checkout. Stop if a
  # framework appears; installed Git hooks still run normally during commit.
  for framework in .overcommit.yml .pre-commit-config.yaml lefthook.yml lefthook.yaml .husky; do
    test ! -e "$framework"
  done
  node -e 'const p=require("./package.json"); if (p.husky || p["lint-staged"] || p.scripts?.prepare) process.exit(1)'
fi
python3 - "$tracking" "$plan" "$repo" <<'PY'
import subprocess, sys
from pathlib import Path
tracking, plan, repo = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
allowed = set((tracking / (plan + '.paths')).read_text().splitlines())
if repo == 'vpsadmin':
    for split in ['commit-v-api', 'commit-v-webui']:
        allowed.update((tracking / (split + '.paths')).read_text().splitlines())
changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
changed.update(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())
assert changed <= allowed, sorted(changed - allowed)
PY
sha256sum "$tracking/$plan.paths" "$tracking/$plan.message"
git add --pathspec-from-file="$tracking/$plan.paths"
python3 - "$tracking/$plan.paths" <<'PY'
import subprocess, sys
from pathlib import Path
expected = set(Path(sys.argv[1]).read_text().splitlines())
staged = set(subprocess.check_output(['git', 'diff', '--cached', '--name-only'], text=True).splitlines())
assert staged and staged <= expected, sorted(staged - expected)
assert all(Path(path).is_file() for path in expected)
PY
git diff --cached --check
git diff --cached --stat
git diff --cached --binary >"$tracking/source-$plan-staged.diff"
git commit -F "$tracking/$plan.message"
git rev-parse HEAD >"$tracking/source-$plan.sha"
git show --format=fuller --stat HEAD
