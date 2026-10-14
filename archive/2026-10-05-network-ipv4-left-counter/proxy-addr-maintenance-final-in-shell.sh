#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
operation=${1:?Missing commit/packages/publish operation}
selected=${2-}
source "$tracking/proxy-addr-maintenance-final-common.sh"
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done

case "$operation" in
  commit)
    [[ -z $selected && $(git rev-parse HEAD) == "$base" ]]
    [[ -z $(git diff --cached --name-only) ]]
    [[ ! -e "$tracking/$prefix-committed.sha" && ! -e "$tracking/$prefix-committed.diff" ]]
    run_step commit-source-guard python3 "$tracking/$prep-guard.py" ready
    run_step commit-hook-guard python3 "$tracking/$prefix-guard.py" hooks
    run_step commit-fetch-main git fetch --no-tags origin refs/heads/main:refs/remotes/origin/main
    [[ $(git rev-parse refs/remotes/origin/main) == "$base" ]]
    git merge-base --is-ancestor refs/remotes/origin/main HEAD
    [[ -z $(git ls-remote --heads origin "refs/heads/$branch") ]]
    run_step stage git add -- "${paths[@]}"
    run_step staged-guard python3 "$tracking/$prefix-guard.py" staged
    run_step staged-whitespace git diff --cached --check
    sha256sum --check "$tracking/$prefix.freeze.sha256"
    run_step normal-commit git commit -F "$tracking/$prefix.message"
    selected=$(git rev-parse HEAD)
    run_step committed-guard python3 "$tracking/$prefix-guard.py" committed "$selected"
    printf '%s\n' "$selected" >"$tracking/$prefix-committed.sha"
    git rev-parse HEAD^{tree} >"$tracking/$prefix-committed.tree"
    git log --format=fuller "$base..HEAD" >"$tracking/$prefix-committed-history.log"
    git diff --binary "$base..HEAD" >"$tracking/$prefix-committed.diff"
    ;;
  packages)
    check_committed_head
    run_step build-bff nix build --no-link --print-out-paths --no-update-lock-file .#bff
    check_committed_head
    run_step build-frontend nix build --no-link --print-out-paths --no-update-lock-file .#frontend
    check_committed_head
    run_step check-provenance nix build --no-link --print-out-paths --no-update-lock-file \
      .#checks.x86_64-linux.provenance
    run_step check-source-contents nix build --no-link --print-out-paths --no-update-lock-file \
      .#checks.x86_64-linux.source-contents
    run_step check-package-contents nix build --no-link --print-out-paths --no-update-lock-file \
      .#checks.x86_64-linux.package-contents
    check_committed_head
    run_step paired-metadata python3 "$tracking/$prefix-guard.py" metadata "$selected"
    ;;
  publish)
    check_committed_head
    [[ ! -e "$tracking/$prefix-published.sha" ]]
    run_step publish-hook-guard python3 "$tracking/$prefix-guard.py" hooks
    run_step publish-fetch-main git fetch --no-tags origin refs/heads/main:refs/remotes/origin/main
    [[ $(git rev-parse refs/remotes/origin/main) == "$base" ]]
    git merge-base --is-ancestor refs/remotes/origin/main HEAD
    [[ -z $(git ls-remote --heads origin "refs/heads/$branch") ]]
    run_step feature-push git push origin "$selected:refs/heads/$branch"
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$selected" ]]
    run_step feature-tracking git fetch --no-tags origin \
      "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$selected" ]]
    check_committed_head
    printf '%s\n' "$selected" >"$tracking/$prefix-published.sha"
    ;;
  *) exit 2 ;;
esac
sha256sum --check "$tracking/$prefix.freeze.sha256"
