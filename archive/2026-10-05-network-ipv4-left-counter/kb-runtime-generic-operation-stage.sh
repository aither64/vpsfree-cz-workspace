#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
base=e3315a483f3d3536d492ecbe40f2655449cf630f
branch=2026-10-05-network-ipv4-left-counter
case "${1-}" in commit|publish) operation=$1 ;; *) exit 64 ;; esac
prefix=kb-runtime-generic-operation-$operation
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_BIN BUNDLE_WITH BUNDLE_WITHOUT
export GEM_HOME="$(ruby --disable-gems -rrubygems -e 'print Gem.default_dir')"
export GEM_PATH="$GEM_HOME"
test "$GEM_HOME" != "${GEM_HOME#/nix/store/}"
cd "$repo"
test "$(git symbolic-ref --short HEAD)" = "$branch"
test "$(git remote get-url origin)" = git@github.com:aither64/dev-workspace.git
test "$(git remote get-url --push origin)" = git@github.com:aither64/dev-workspace.git
test -z "$(git diff --cached --name-only)"
sha256sum --check "$tracking/kb-runtime-generic-quick4.sha256"
sha256sum --check "$tracking/kb-runtime-generic-quick4-source.sha256"
for check in toolchain syntax commands; do
  test "$(cat "$tracking/kb-runtime-generic-quick4-$check.exit")" = 0
done
test "$(cat "$tracking/kb-runtime-generic-quick4.exit")" = 0
git fetch origin +refs/heads/master:refs/remotes/origin/master
git rev-parse refs/remotes/origin/master >"$tracking/$prefix.default.sha"
git merge-base --is-ancestor refs/remotes/origin/master HEAD
if test "$operation" = commit; then
  test "$(git rev-parse HEAD)" = "$base"
  diff -u "$tracking/kb-runtime-generic-quick4-source.status" <(git status --porcelain=v1)
  diff -u "$tracking/kb-runtime-generic-quick4-source.diff" <(git diff --binary)
  # This repository declares no hook framework. Normal git still executes any
  # installed hooks; no configuration override or bypass is supplied.
  for declaration in .overcommit.yml .pre-commit-config.yaml lefthook.yml lefthook.yaml .husky; do
    test ! -e "$declaration"
  done
  {
    printf 'Declared hook framework: none\n'
    git config --get core.hooksPath || test "$?" = 1
    hooks=$(git rev-parse --git-path hooks)
    printf 'Effective hook directory: %s\n' "$hooks"
    for hook in "$hooks"/*; do
      case "$hook" in *.sample) continue ;; esac
      if test -f "$hook" && test -x "$hook"; then printf '%s\n' "$hook"; fi
    done
  } >"$tracking/$prefix.hook-context.log"
  git add -- libexec/workspace-host test/workspace_host/commands_and_locks_test.rb docs/workspace-portal.md
  diff -u <(printf '%s\n' docs/workspace-portal.md libexec/workspace-host test/workspace_host/commands_and_locks_test.rb) <(git diff --cached --name-only)
  diff -u "$tracking/kb-runtime-generic-quick4-source.diff" <(git diff --cached --binary)
  git diff --cached --check
  git commit -F "$tracking/kb-runtime-generic-commit.message"
  test "$(git rev-parse HEAD^)" = "$base"
  test -z "$(git status --porcelain=v1)"
  diff -u "$tracking/kb-runtime-generic-quick4-source.diff" <(git diff --binary "$base" HEAD)
else
  test -z "$(git status --porcelain=v1)"
  test "$(git rev-parse HEAD)" = "$(cat "$tracking/kb-runtime-generic-operation-commit.head")"
  test "$(git rev-parse HEAD^{tree})" = "$(cat "$tracking/kb-runtime-generic-operation-commit.tree")"
  test "$(git rev-parse HEAD^)" = "$base"
  test "$(cat "$tracking/kb-runtime-generic-operation-commit.exit")" = 0
  # The lead supplies this exact remote lease from an independent read. It is
  # either a full SHA or the literal 'absent'; absence is never presumed.
  expected=$(cat "$tracking/kb-runtime-generic-publication-remote.expected")
  observed=$(git ls-remote --heads origin "refs/heads/$branch")
  if test "$expected" = absent; then
    test -z "$observed"
  else
    test "${#expected}" = 40
    test "$observed" = "$expected"$'\t'"refs/heads/$branch"
    git merge-base --is-ancestor "$expected" HEAD
  fi
  printf '%s\n' "${observed:-absent}" >"$tracking/$prefix.remote-before.sha"
  git push origin "HEAD:refs/heads/$branch"
  test "$(git ls-remote --heads origin "refs/heads/$branch")" = "$(git rev-parse HEAD)"$'\t'"refs/heads/$branch"
fi
git rev-parse HEAD >"$tracking/$prefix.head"
git rev-parse HEAD^{tree} >"$tracking/$prefix.tree"
git diff --binary "$base" HEAD >"$tracking/$prefix.diff"
