#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
test "$(git rev-parse HEAD)" = 9b5bb4d61413e1de7702f45b50ef3229d2b93244
test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
test -z "$(git diff --cached --name-only)"
sha256sum --check --quiet "$tracking/kb-runtime-generic-eof-quick4-source.sha256"
diff -u "$tracking/kb-runtime-generic-eof-quick4-source.status" <(git status --porcelain=v1)
test "$(git remote get-url origin)" = git@github.com:aither64/dev-workspace.git
git fetch origin master
git merge-base --is-ancestor origin/master HEAD
python3 - <<'PY'
import os,pathlib,subprocess
for key in ('OVERCOMMIT_DISABLE','SKIP','HUSKY','LEFTHOOK','PRE_COMMIT_ALLOW_NO_CONFIG','GIT_CONFIG_COUNT'):
 if key in os.environ: raise SystemExit('unexpected hook/config override: '+key)
setting=subprocess.run(['git','config','--get','core.hooksPath'],capture_output=True,text=True)
assert setting.returncode==1 and not setting.stdout,'hook path override needs inspection'
paths=subprocess.check_output(['git','ls-files'],text=True).splitlines()
for x in paths:
 if pathlib.Path(x).name in ('.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml') or '/.husky/' in '/'+x:
  raise SystemExit('new declared hook framework')
hooks=pathlib.Path(subprocess.check_output(['git','rev-parse','--git-path','hooks'],text=True).strip())
assert all(p.name.endswith('.sample') for p in hooks.iterdir()),'unexpected non-sample hook requires inspection'
PY
set -o noclobber
git diff --binary > "$tracking/kb-runtime-generic-eof-final-correction.diff"
git rev-parse HEAD > "$tracking/kb-runtime-generic-eof-final-old.sha"
git log --format=fuller e3315a483f3d3536d492ecbe40f2655449cf630f..HEAD > "$tracking/kb-runtime-generic-eof-final-old.history"
git add -- libexec/workspace-host test/workspace_host/commands_and_locks_test.rb docs/workspace-portal.md
git diff --cached --check
git diff --cached --stat
git diff --cached --binary > "$tracking/kb-runtime-generic-eof-final-staged.diff"
