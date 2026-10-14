#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
cd "$repo"
test "$(git rev-parse HEAD)" = 9fe491218e35a3250f2a72c203c2cecc3cb7ae16
test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
test "$(git remote get-url origin)" = git@github.com:aither64/dev-workspace.git
test ! -e "$tracking/kb-runtime-d-go-source.sha"
test -z "$(git diff --cached --name-only)"
sha256sum --check "$tracking/kb-runtime-d-go-final1-source.manifest" >/dev/null
sha256sum --check "$tracking/kb-runtime-d-go-final1-source.sha256" >/dev/null
diff -u "$tracking/kb-runtime-d-go-final1-source.status" <(git status --porcelain=v1 --untracked-files=all)
for check in toolchain formatting focused web; do test "$(cat "$tracking/kb-runtime-d-go-quick1-$check.exit")" = 0; done
test "$(cat "$tracking/kb-runtime-d-go-quick1.exit")" = 0
git fetch origin master
git merge-base --is-ancestor origin/master HEAD
git log --oneline HEAD..origin/master >"$tracking/kb-runtime-d-go-default-comparison.log"
python3 - "$tracking" <<'PY'
import os, pathlib, subprocess, sys
t=pathlib.Path(sys.argv[1])
for name in ['OVERCOMMIT_DISABLE','SKIP','HUSKY','HUSKY_SKIP_HOOKS','PRE_COMMIT_ALLOW_NO_CONFIG']:
 if name in os.environ: raise SystemExit('hook control environment requires inspection: '+name)
for name in ['.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml','.lefthook.yml','.husky']:
 if pathlib.Path(name).exists(): raise SystemExit('unexpected hook framework')
if subprocess.run(['git','config','--get','core.hooksPath'],capture_output=True).returncode!=1: raise SystemExit('unexpected hook path')
hooks=pathlib.Path(subprocess.check_output(['git','rev-parse','--git-path','hooks'],text=True).strip())
if any(p.is_file() and not p.name.endswith('.sample') for p in hooks.iterdir()): raise SystemExit('unexpected active hook needs inspection')
if any(len(line)>80 for line in (t/'kb-runtime-d-go-final1-source.message').read_text().splitlines()): raise SystemExit('message width')
PY
git add -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go
python3 - "$tracking" "$repo" <<'PY'
import hashlib,pathlib,subprocess,sys
t=pathlib.Path(sys.argv[1]);r=pathlib.Path(sys.argv[2])
expected=(t/'kb-runtime-d-go-final1-source.paths').read_text().splitlines()
actual=subprocess.check_output(['git','diff','--cached','--no-renames','--name-only','-z']).decode().split('\0')[:-1]
if len(expected)!=2 or set(actual)!=set(expected): raise SystemExit('staged path mismatch')
for line in (t/'kb-runtime-d-go-final1-source.sha256').read_text().splitlines():
 digest,absolute=line.split('  ',1)
 relative=str(pathlib.Path(absolute).relative_to(r))
 if hashlib.sha256(subprocess.check_output(['git','show',':'+relative])).hexdigest()!=digest: raise SystemExit('staged byte mismatch')
PY
git diff --cached --check
git diff --cached --binary >"$tracking/kb-runtime-d-go-staged.diff"
git write-tree >"$tracking/kb-runtime-d-go-staged.tree"
git commit -F "$tracking/kb-runtime-d-go-final1-source.message"
test "$(git rev-parse HEAD^{tree})" = "$(cat "$tracking/kb-runtime-d-go-staged.tree")"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
git rev-parse HEAD >"$tracking/kb-runtime-d-go-source.sha"
git log --format=fuller e3315a483f3d3536d492ecbe40f2655449cf630f..HEAD >"$tracking/kb-runtime-d-go-source-history.log"
git diff --binary e3315a483f3d3536d492ecbe40f2655449cf630f..HEAD >"$tracking/kb-runtime-d-go-source-full.diff"
cat "$tracking/kb-runtime-d-go-source.sha"
