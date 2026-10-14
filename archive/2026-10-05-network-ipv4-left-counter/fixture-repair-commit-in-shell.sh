#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
for step in ruby-syntax-lint api-core api-full react-quick; do [[ $(cat "$tracking/fixture-repair-quick2-$step.exit") == 0 ]]; done
(cd "$tracking" && sha256sum --check "$tracking/network-fixture-repair-freeze2.sha256")
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do [[ -z ${!bypass-} ]]; done
mode=${1:?Missing repository}
case "$mode" in
v)
  repo=vpsadmin
  branch=2026-10-05-network-ipv4-left-counter
  old=30603a832d2848207bd7319c79c6b0388bc8646a
  base=c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
  count=2
  paths=(api/spec/models/ip_ownership_concurrency_spec.rb)
  [[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
  [[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
  for hook in pre-commit commit-msg; do
    hook_path=$(git rev-parse --git-path "hooks/$hook")
    test -x "$hook_path"
    rg -q 'Overcommit hook integration' "$hook_path"
  done
  ;;
w)
  repo=vpsadmin-webui
  branch=dev/network-enabled
  old=b3b756a7b45864459bd39481a0d5245886777660
  base=02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51
  count=1
  paths=(e2e/specs/admin/network_availability.spec.ts docs/work-log/2026-10-06-network-availability.md)
  [[ $(cat "$tracking/fixture-repair-final-docs.exit") == 0 ]]
  for framework in .overcommit.yml .pre-commit-config.yaml lefthook.yml lefthook.yaml .husky; do test ! -e "$framework"; done
  node -e 'const p=require("./package.json"); if(p.husky || p["lint-staged"] || p.scripts?.prepare) process.exit(1)'
  ;;
*) exit 2 ;;
esac
[[ $(pwd -P) == "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo" ]]
[[ $(git branch --show-current) == "$branch" && $(git rev-parse HEAD) == "$old" ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
[[ -z $(git diff --cached --name-only) ]]
python3 - "${paths[@]}" <<'PYGUARD'
import subprocess,sys
changed=set(subprocess.check_output(['git','diff','--name-only'],text=True).splitlines())
changed.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],text=True).splitlines())
assert changed and changed <= set(sys.argv[1:]), sorted(changed-set(sys.argv[1:]))
PYGUARD
git add -- "${paths[@]}"
git diff --cached --check
git diff --cached --binary >"$tracking/fixture-repair-$mode-staged.diff"
git commit -F "$tracking/fixture-repair-commit-$mode.message"
[[ -z $(git status --porcelain) ]]
tree=$(git rev-parse 'HEAD^{tree}')
git rev-parse HEAD >"$tracking/fixture-repair-$mode-fixup.sha"
GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false rebase -i --autosquash "$base"
[[ $(git rev-parse 'HEAD^{tree}') == "$tree" && $(git rev-list --count "$base..HEAD") == "$count" ]]
[[ -z $(git status --porcelain) ]]
if [[ $mode == v ]]; then git diff --exit-code "$old" HEAD -- api/db/migrate api/db/schema.rb; fi
git rev-parse HEAD >"$tracking/fixture-repair-source-$mode.sha"
git log --reverse --format=fuller "$base..HEAD" >"$tracking/fixture-repair-$mode-history.log"
git range-diff "$base..$old" "$base..HEAD" >"$tracking/fixture-repair-$mode-range.diff"
