# Remote-default delta before M8 feature publication

Canonical SSH fetch/readback before and after: master
`4cb66436558d4c494d658042192f7b743eddb54d`, tree
`233a82ee2addc2b5aad5422fc537a48ebfa326f1`; own devdocs ref absent.
Ordinary `git fetch --no-tags origin refs/heads/master` succeeded; FETCH_HEAD
matches. Local branches/worktrees were not moved. Original publication guard
failure remains separately in the parent directory.

Reviewed base `08c3bd7e3cb4dc324a0381df6a1eec190daab1a7` is the direct parent
and merge-base with tested feature `2a4a7bc9f0cf4c625aadb7cfded50dff0890ef68`.
Neither target nor feature is ancestor of the other. The complete added history
is one bot commit, `4cb6643 packages: update gem dependencies`.

All 12 changed files are six packaged lock/gemset pairs. API csv changes
3.3.6→3.3.7; io-console changes 0.9.4→0.9.5 in API, client,
download-mounter, libnodectld, nodectl and nodectld, with corresponding hashes.
Six paths overlap the feature: API/client/download-mounter lock+gemset pairs.
The feature retains both original unrelated versions, so the changed dependency
entries are semantically separate from its HaveAPI selection. No authored
runtime/API/auth/schema/migration/protocol/Nix-module/proxy/deployment contract,
Gemfile constraint, SDK or source pin changes occur in this default delta.

Publishing the exact tested feature can preserve its existing isolated graph;
it does not integrate or replace master. This inspection found no contract
reason requiring a rebase for that publication. Any later integration/rebase
must deliberately incorporate the dependency refresh and re-establish affected
lock/output evidence: old fullff669/services proof cannot be relabelled as proof
of refreshed dependencies. No new gem-version compatibility test was run or
claimed. Lead owns publication disposition; no push/rebase/source edit occurred.

Final tracked source remains clean at exact2a4/tree62c003 and both full API locks
remain `ff66923a174a2462ccc5ff435c7e3e128356f8c9fa20c69a9f6a1d9e0afd9d8d`.
All34 services/package/roots remain valid for that exact graph.

[Exact comparison](comparison.json), [complete commit list](commit-list.txt),
[complete default diff](default.diff), [before](remote-before.txt),
[after](remote-after.txt), [fetch](fetch.log).

Lead accepted this bounded finding and preservation of exact08c3/2a4/old unrelated
versions. Publication is now HELD for architect's final511 successor brief; no
rebase, push or source/metadata change is authorized by this disposition.
