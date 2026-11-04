# TypeScript history correction

The user challenged the combined TypeScript commit. The lead and owner accepted
that tests, generated inputs/output and release metadata were independently
reviewable. The earlier package-lock/tooling-hash coupling rationale did not
justify bundling these scopes. No product content or design changed.

Repository `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`, target
`main`, feature `2026-11-03-vpsadmin-client-sync`. Base remains
`d354491537f8b654b4d2c33a705cad84474f95d6`.

Old full range:
`d354491537f8b654b4d2c33a705cad84474f95d6..a4fc2449a1b5255b93b0c669ea9c454fac990536`.
New full range:
`d354491537f8b654b4d2c33a705cad84474f95d6..2256ea46a8d8d135f352a524fbf048869d6eddf4`.

| Commit | Reviewable scope |
| --- | --- |
| `d73eb93b27125932b5eaa09b3462ade12fa84765` | One consolidated schema/provenance/input/generated refresh, existing snapshot inventory docs and generator pin; 17 files |
| `96c884b884fd8267f3f9b5b5d9ce26ccbfb8741e` | Handwritten published-runtime/strict declaration consumer coverage, including schema-hash expectation; 2 files |
| `2256ea46a8d8d135f352a524fbf048869d6eddf4` | Package/lock version 0.4.0, changelog and README release example; 4 files |

Generated refresh comes first because the consumer coverage uses the newly
emitted operations. Release metadata remains last. The existing generator pin
contains the final package-lock hash; this input-identity entry belongs to the
single generated/input refresh. The release commit supplies that exact final
lockfile version. No intermediate pin, snapshot or generated updates were added
merely to make intermediate wrapper verification succeed. Final consistency is
unchanged. No dependency/runtime update, obsolete content, transitional
compatibility path or migrations exist. Historical plugin migration arrays are
provenance inputs, not new client migrations.

## Content and history proof

Both old/new final commits have Git tree
`c85e30b1fc1ae27bba9c08884e11fa78bbb15f7b`.
`git diff --exit-code OLD NEW` passed with no output. Exact immutable blob/tree
identity establishes unchanged final content, not a new executed test result.
Complete range-diff retained in
[typescript-history-range-diff.txt](typescript-history-range-diff.txt);
[typescript-history-proof.json](typescript-history-proof.json) binds ranges,
commit list and old archive identity. Range-diff reflects the single commit
being partitioned into three; it does not claim one-to-one patch equivalence.
The old reviewed commit remains anchored by local branch
`2026-11-03-vpsadmin-client-sync-reviewed-a4fc244`.

Reconstruction used exact old blobs in the owned worktree, ordinary Git commits
with hooks enabled and messages from files. No code edit, regeneration, setup,
local build or test suite was repeated. Commit whitespace checks passed and
final worktree is clean. User-authorized force-with-lease against exact old
remote head succeeded; fresh SSH remote feature equals the new final head and
remote main remains the base. No superseded queued/in-progress same-branch CI
runs existed; completed old run 41665146322 was retained, not cancelled.

Captured feature comparison again with explicit unchanged base/new head via
`dev-session worktree capture-comparison`. Prepared native detached integration
target remains clean at original base, with no default mutation, claim or merge.

## Verification and archive boundaries

Old local checks and [typescript-checks-result.md](typescript-checks-result.md)
remain evidence for exact old head `a4fc2449a1b5255b93b0c669ea9c454fac990536`.
Original tested command is preserved byte for byte as
[typescript-checks-tested-a4fc244.sh](typescript-checks-tested-a4fc244.sh).
Current [typescript-checks.sh](typescript-checks.sh) template has a new-head gate
and fresh potential archive directory, is shell-syntax checked, and has **not**
been run for the history split. No Nix verification is justified solely by tree
equality. Original pinned graph remains committed in the identical final tree:
`flake.lock` uses nixpkgs `3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`, NAR hash
`sha256-rZLrzrC6i+jnTAlvPZHogKDulY7WWDEv9hJeHieO7Zw=`; toolchain and generator
identities are unchanged. Original command/log paths and exact source inputs
remain in the original receipts.

Old archive and receipt in `typescript-release-a4fc244/` remain immutable and
bind old tested head, tag null. SHA256 remains
`e3c1cee328c8c0bb6826c209bee971d5e6939d2acbeebf9938fc6f032db95326`.
Do not relabel or publish that tarball as new-commit provenance. Actual new-head
CI [41667969378](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41667969378)
was triggered by the force-push and must pass before readiness. Native CI/tag
workflow supplies its own exact-head/tagged archive and receipt; no local rebuild
is needed merely for the history change.

Lead owns the independent review of this complete three-commit series and the
remaining CI-only observation. Rust verification currently occupies the one
watcher slot; no duplicate utility was launched. No default integration, tag,
publication, Phase 2 rules or lifecycle/cleanup action performed.
