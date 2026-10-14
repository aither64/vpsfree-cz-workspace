#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
cd "$repo"
test "$(git rev-parse HEAD)" = a50f8c1a11ea642edf823f04521f9eaa97132fd2
test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter-kb-runtime
test "$(git write-tree)" = "$(cat "$tracking/kb-runtime-k-source-staged.tree")"
test ! -e "$tracking/kb-runtime-k-source.sha"
sha256sum --check "$tracking/kb-runtime-k-final2-source.manifest" >/dev/null
sha256sum --check "$tracking/kb-runtime-k-final2-source.sha256" >/dev/null
git diff --exit-code
git diff --cached --check
python3 - "$tracking" "$repo" <<'PY'
import hashlib, os, pathlib, subprocess, sys
t=pathlib.Path(sys.argv[1]);r=pathlib.Path(sys.argv[2])
for name in ['OVERCOMMIT_DISABLE','SKIP','HUSKY','HUSKY_SKIP_HOOKS','PRE_COMMIT_ALLOW_NO_CONFIG']:
 if name in os.environ: raise SystemExit('hook control environment requires inspection: '+name)
for name in ['.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml','.lefthook.yml','.husky']:
 if (r/name).exists(): raise SystemExit('unexpected declared hook framework')
value=subprocess.run(['git','config','--get','core.hooksPath'],capture_output=True,text=True)
if value.returncode != 1: raise SystemExit('unexpected hook path configuration')
hooks=pathlib.Path(subprocess.check_output(['git','rev-parse','--git-path','hooks'],text=True).strip())
if any(p.is_file() and not p.name.endswith('.sample') for p in hooks.iterdir()): raise SystemExit('unexpected active hook needs inspection')
for line in (t/'kb-runtime-k-final2-source.sha256').read_text().splitlines():
 expected, absolute=line.split('  ',1)
 relative=str(pathlib.Path(absolute).relative_to(r))
 blob=subprocess.check_output(['git','show',':'+relative])
 if hashlib.sha256(blob).hexdigest()!=expected: raise SystemExit('staged bytes differ: '+relative)
if subprocess.check_output(['git','ls-files','--stage','--','lib/dev-cluster.cjs']): raise SystemExit('deleted legacy client remains staged')
message=(t/'kb-runtime-k-final2-source.message').read_text()
if any(len(line)>80 for line in message.splitlines()): raise SystemExit('message line exceeds 80 columns')
PY
git commit -F "$tracking/kb-runtime-k-final2-source.message"
test "$(git rev-parse HEAD^{tree})" = "$(cat "$tracking/kb-runtime-k-source-staged.tree")"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
git rev-parse HEAD >"$tracking/kb-runtime-k-source.sha"
git rev-parse HEAD^{tree} >"$tracking/kb-runtime-k-source.tree"
git log --format=fuller 873758fd6aec0c03f50a94600e0ceab97946f255..HEAD >"$tracking/kb-runtime-k-source-history.log"
git diff --binary 873758fd6aec0c03f50a94600e0ceab97946f255..HEAD >"$tracking/kb-runtime-k-source-full.diff"
cat "$tracking/kb-runtime-k-source.sha"
