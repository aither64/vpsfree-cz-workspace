#!/usr/bin/env bash
# Sourced only after the outer operation has verified the bound session.
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
v_sha=${1:?Missing selected V head}
w_sha=${2:?Missing selected W head}
[[ $v_sha == be136b6c00f03b85b7a12cc57550b4a1394a94a7 ]]
[[ $w_sha == e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 ]]
[[ $(cat "$tracking/fixture-final-source-w.sha") == "$w_sha" ]]
for receipt in fixture-repair-quick2-wrapper fixture-repair-quick2-ruby-syntax-lint \
  fixture-repair-quick2-api-core fixture-repair-quick2-api-full fixture-repair-quick2-react-quick \
  post-review3-react-desktop post-review3-react-mobile post-review3-react-build fixture-final-docs2; do
  [[ $(cat "$tracking/$receipt.exit") == 0 ]]
done
sha256sum --check "$tracking/fixture-final-operation-freeze.sha256"

select_source() {
  case "$1" in
    v)
      repo=vpsadmin; branch=2026-10-05-network-ipv4-left-counter; default=master
      revision=$v_sha; lease=30603a832d2848207bd7319c79c6b0388bc8646a
      ;;
    w)
      repo=vpsadmin-webui; branch=dev/network-enabled; default=main
      revision=$w_sha; lease=b3b756a7b45864459bd39481a0d5245886777660
      ;;
    *) return 2 ;;
  esac
  repo_root="$worktrees/$repo"
  [[ $(git -C "$repo_root" branch --show-current) == "$branch" ]]
  [[ $(git -C "$repo_root" rev-parse HEAD) == "$revision" ]]
  [[ -z $(git -C "$repo_root" status --porcelain) ]]
  [[ $(git -C "$repo_root" remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
}

verify_published_source() {
  select_source "$1"
  [[ $(cat "$tracking/fixture-final-published-$1.sha") == "$revision" ]]
  [[ $(git -C "$repo_root" ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$revision" ]]
  # The feature ref was rewritten and bare origin may have no fetch refspec.
  # Force only this verified, owned remote-tracking ref; defaults stay guarded.
  git -C "$repo_root" fetch --no-tags origin \
    "refs/heads/$default:refs/remotes/origin/$default" \
    "+refs/heads/$branch:refs/remotes/origin/$branch"
  [[ $(git -C "$repo_root" rev-parse "refs/remotes/origin/$branch") == "$revision" ]]
  git -C "$repo_root" merge-base --is-ancestor "origin/$default" "$revision"
}
