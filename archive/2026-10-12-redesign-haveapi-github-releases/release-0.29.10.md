# HaveAPI 0.29.10 release execution

Requested 2026-10-19: real patch release to test the accepted GitHub Actions
process. User selected automation-only 0.29.10 and instructed implementation.
Existing master merge approval remains scoped to master; this follow-up prepares
the supported release branch and real version. Human approval of the release
environment remains a separate workflow step owned by the user.

Baseline: haveapi-0.29 and v0.29.9 point at
784e113c216b16586c482e710ee4a0e0a04e6f8e. All three gems, npm and Packagist
report 0.29.9. PHP mirror master matches its v0.29.9 tag at
7fa4e35a9d9cb462320a4b2f2786bf84b8e024f2. Neither source nor mirror has v0.29.10.
Master is c14e7d3158b91c134c2817b489cd29772fc09f82. Release branch contains
example-validation fixes/tests absent from master; retain them.

Status: tag and artifacts preserved, approved publishing attempt failed before
any registry/PHP writes. A corrected 0.29.11 successor is being prepared; the
0.29.10 approval does not approve that new version. See state.md for current work.

Worktree: worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release.
Branch: 2026-10-19-haveapi-0.29.10, registered as haveapi-release. Original merged
feature ref/worktree preserved. Exact head b27a031fa03d8d985a3abd2679ce2fc14fe53602.
Four logical commits: 974e57b toolchain, 41e37c2 implementation, c59483e adapted
docs, b27a031 version/changelog. The original two backports retain provenance.
The branch's existing Node/PHP server-shell dependencies and all runtime fixes
and tests are retained. No Elixir change or migration.

Official action release APIs were checked; all existing pins are latest except
the Nix installer. Its latest v31.11.2 fixes Nix security issues; its SSH-read tag
SHA 448cde739abec1eaf0646249e3d25bb8d9bc7702 replaces the two old installer pins.
All helper code otherwise matches the master implementation. Detailed comparison:
release-backport.range-diff; final branch diff: release-final.diff.

The initial worktree checkout reported a hook signature refusal after creating
the owned checkout. Configuration/custom hooks matched the inspected master
version; installed and signed them in the repository Nix shell. No hook bypass.
Fresh Luna/low setup utility first used the wrong CWD for current, then correctly
resolved the same unstarted operation from the tracking directory. The dependency
setup loaded overcommit/rubocop but its rspec probe failed because the old root
Gemfile had no rspec dependency. The intended implementation backport adds that
dependency; the next Nix entry installed it, and both helper suites passed.
No application test failure was ignored or blindly retried.

release-quick.sh/status: 0. Metadata, 21 helper examples normally and under
GITHUB_RUN_ID=123, Ruby lint (244 files, no offenses), shell syntax, runtime-byte
comparison after version normalization, Git whitespace and actionlint passed.
All four commits passed installed hooks. Reviewer0 assigned the exact committed
base/head with all four lanes at retained settings; see release-review-packet.md.

Retained reviewer0 accepted the exact final range, full history and no-migrations
conclusion without findings; see release-review.md. Lead independently verified
native turn/model/effort. A fresh Luna/low verification utility completed local
component/package checks and all eight CI workflows with status 0 (about 3m).
Counts: server 365, Ruby client 47, Go generator 9 examples; JS 43; PHP 51 tests,
144 assertions. Package/manifest/npm/extracted-gem checks passed. The generated
PHP test cache was removed and tracked checkout is clean. See
release-verification-summary.md and release-ci-results.json for exact runs.

Final pre-tag inspection rechecked exact head and byte-identical reviewed diff
(SHA-256 fa41f5ceccc77099d05d894badf860f0f4fb3d5e572b81964306961a23539408), clean
tree, unchanged remote release branch and absent v0.29.10. All four commits remain
the reviewed inventory, with no obsolete history or migrations. The user's
explicit patch-release request, 0.29.10 scope choice and implementation direction
cover the planned release-branch advance and new tag. Publication still waits for
human approval in the protected environment; required reviewer aither64 and
self-review policy were rechecked read-only.

The workspace package advanced externally during verification. Lead read the new
selected coordination guide at zylvmqsls49lbf4937lq434m52sfyhfg; execution access
and retained Luna/low watcher policy remain unchanged. Its installed catalog
covers HaveAPI master, not this separately named release-branch operation.
The release follows the repository's SSH fast-forward/tag procedure, without
changing the master registration or workspace catalog. No deployment or machine
reservation is involved. The original master integration remains complete.

A fresh detached target worktree at work/<slug>/release-target was created from
origin/haveapi-0.29, then fast-forwarded to the reviewed head with the declared
Nix/Bundler hook environment. No hook bypass or merge commit. The branch and
annotated v0.29.10 tag were pushed atomically over SSH. Fresh remote inspection:
release branch and peeled tag b27a031fa03d8d985a3abd2679ce2fc14fe53602;
annotated tag object cd6a5f4c248de748d1b40bd54aeceedb4ebb743c. All source tags and
accepted package versions remain immutable. Target worktree is retained and
must not be staged with the session evidence. Master was not changed.

## First tag attempt: activation variable missing

Run 39291918638 (v0.29.10, exact b27a031 head) failed in build step 5,
Check publication setup. Failed logs show HAVEAPI_RELEASE_ENABLED empty and
`Release failed: Set HAVEAPI_RELEASE_ENABLED=true only after completing release setup`.
Publishing was skipped; dependency/test/package stages and artifact upload had
not run. This is a detected operator-setup gap, not a package/test failure.
Preserved evidence: release-tag-attempt1.json, release-tag-attempt1-failed.log,
release-tag-attempt1-watch.log; observer status 1. Fresh Luna/low utility did not
retry or diagnose; lead read the full failed step and exact source/run metadata.

Lead attempted `gh variable set HAVEAPI_RELEASE_ENABLED --repo vpsfreecz/haveapi
--body true` under the declared Nix tools environment. GitHub rejected it with
HTTP 403, Resource not accessible by personal access token. No variable changed.
Asked the user asynchronously to set the repository Actions variable (not only a
release-environment variable) from their authenticated CLI or repository settings.

After correction, rerun failed jobs in this same run. It failed before any
artifact upload, so the documented artifact recovery contract permits that early
build retry. Do not retag, rebuild an accepted package or prepare another version.
Actual publication still requires the human protected-environment approval.

## Second tag attempt

The user asked where to set the variable, received the repository Settings path,
then replied "done". Before rerunning, lead confirmed attempt 1 remained terminal
failure, the feature checkout was clean, and source branch/peeled tag still match
b27a031 with annotated object cd6a5f4c248de748d1b40bd54aeceedb4ebb743c.
Requested `gh run rerun 39291918638 --repo vpsfreecz/haveapi --failed` after the
known setup cause was corrected. No source change, retag or registry write.
Fresh Luna/low utility observes attempt 2, with an explicit attempt guard to
avoid accepting a stale attempt-1 status. Original failure evidence is retained.

Attempt 2 reached approval-required with successful build/test/package/upload and
verification. Observer exit 0, incomplete publication, with lead-acknowledged
handoff; release-tag-attempt2-watch.log/status and release-tag-attempt2.json.
Pending-deployment API identifies release with required reviewer aither64.
No approval was submitted by the lead. Original artifact ID 12206004265 was
downloaded, retained locally, and verified by the release CLI with its actual
GITHUB_RUN_ID, source b27a031, version/tag 0.29.10. Manifest hash and complete
approval evidence: release-tag-approval.md. Next user action is Approve and deploy
in the run; next lead action is publication monitoring and receipt/index checks.

## Approved publishing attempt failed before registry writes

User aither64 approved attempt 2 in the protected release environment (API proof:
release-tag-approvals.json). The publishing job created a draft Release, then
failed at utils/release/publish.rb:196: nil.fetch after the published-only tag
endpoint returned 404 for that draft. RubyGems credentials and all registry/PHP
publication steps were skipped. All three exact gem-version endpoints and npm
returned 404 after the failure. No blind rerun or source/tag replacement.
Evidence: release-tag-attempt2-final.json and
release-tag-attempt2-publish-failed.log. The new implementation finds authorized
drafts through paginated list releases; official API contract:
https://docs.github.com/en/rest/releases/releases . The exact source, tag, draft
and original download release-tag-artifacts/ remain preserved.
