# HaveAPI default integration, 0.30 backport and 0.30.1 preparation

Current execution brief, 2026-10-24. The user explicitly directed merging the
completed fixes, including dependency updates, into defaults, then backporting
to 0.30 and preparing 0.30.1 with a refreshed changelog date. This authorizes
HaveAPI/master integration and supported release-branch preparation. It does
**not** authorize a tag, GitHub Release, registry upload, PHP mirror update,
Rust crate release or deployment. No second merge-permission request is needed
within this named scope. The former publication grant remains held.

This brief supersedes stale source/order/verification assumptions in
[release-0.30.1-plan.md](release-0.30.1-plan.md); preserve that plan's immutable
artifact and recovery rules. Architect edits records only. Source implementation
and exact-head checks must finish before integration.

[Version-sensitive verification](release-version-sensitive-verification.md)
records the accepted exact 18-path version boundary, owner1's ignored/combined
lock rebinding, minimum actual 0.30.1 Rust/Go profile checks and applicability of
pre-version evidence. Do not rerun the fixed-4dc0 model comparison unchanged
after versioning or relax its comparator for expected release metadata.

## Retained inputs and history boundary

These are retained/local-object observations, not fresh remote checks:

| Ref/input | Exact revision/state |
| --- | --- |
| Completed 0.30.0/newest cached release branch `haveapi-0.30` | `b64fb25bea8d8222fb3263b99956c0b61438a859`; published tag/artifacts immutable |
| Already integrated fixes / cached remote master | `090a188cb4ef3477324718627f4ae3415d1c0975`, tree `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2` |
| Reviewed dependency refresh | `4dc0f7e11c494d1a0dc852dabcc312411699fcab`, directly after 090a; retained final review and all 10 CI reported complete |
| Profiles feature | `2026-10-24-haveapi-client-example-profiles`, based on 4dc0; final source head not yet frozen/reviewed |
| Existing patch feature | `2026-10-22-haveapi-release-0.30.1` at `8270b519a2ea1d60735634d34cc1a451a3e904b4`; exact 090a tree; still VERSION 0.30.0 |
| Downstream Rust | `ff876abe17e3301da62c1b6afbda055ec89db9d2` already merged into main; retains generator 090a, crate 0.1.0 and its saved schema |

The registered patch worktree is
`worktrees/2026-10-22-haveapi-release/haveapi-0-30-1`; its current on-disk
CHANGELOG still begins `# Thu Oct 22 2026 - version 0.30.0`.
No 0.30.1 section is present there. Owner0 must reconcile any lead-owned draft
before editing. Local bare master 7835acaf is stale and is not an integration
baseline. Owner0 supplies fresh remote master/release/newest-branch facts,
clean tracked/index state and ancestry before operations. An attempted
coordination-only message requesting retained facts was rejected by a transient
same-session writer lock; no Git action or probe resulted.

Existing six source/backport pairs already verified by
`release-0301-source-20261023T201151Z/preversion-equivalence.json`:

| Master source | Existing patch |
| --- | --- |
| `cbf6a3f0b34f15e2bb4224872b46c423d7d02313` Fiddle | `587a04d0f88705724f88686002bde99a2a0b03cb` |
| `431d7ffed098c7403d3d0555b3b93c4a3ab8b3e3` Rust naming lint | `40471f2ed2fc394d941dd8b15cc7377187c8812c` |
| `01a30a39cdfc0d81e2eca62dcce912c165d891fa` JS tooling/helpers | `e3648859bb0d1520993c092efc75ec9146a98081` |
| `412511176d7f54a96d48bc0995b202f335d1be4f` JS module graph | `73df386699a03adb307f1c612763e944f48e0c9b` |
| `c424c579a314593e25cfe661374caafb9ab78a4c` Registry confirmation | `e406ae4c4f683398dd0f6bcc74d3d898bbc93163` |
| `090a188cb4ef3477324718627f4ae3415d1c0975` Generated JS | `8270b519a2ea1d60735634d34cc1a451a3e904b4` |

Do not replay these commits. Preserve their genuine `cherry-pick -x` trailers.
The first tooling update is already merged history, and 090a is an explicitly
retained downstream generator source boundary; it must not be rewritten into
4dc0. Its provenance-mapped release backports preserve that boundary. The later
4dc0 refresh is one coherent new update. Consolidate obsolete interim profile
fixes/update streams before final review, without falsifying trailers or
rewriting merged/default history. The final reviewer must explicitly assess
this retained history rationale and confirm no migrations/state transitions.
There is no new downstream repin/regeneration scope.

## Owner packages and order

1. **Profile implementers + owner0:** finish source, docs and quick checks in
   `haveapi-client-example-profiles`. Inventory the complete 090a-to-final
   series, including 4dc0 and profiles, then perform committed final independent
   review before the affected longer tests/CI. Existing 090a/4dc0 review supports,
   but does not replace, final profile and whole-series review.
2. **Owner0, sole Git:** publish the complete reviewed feature head normally,
   complete its required checks and capture its comparison. Integrate that
   cumulative head to fresh HaveAPI/master by fast-forward, preserving 4dc0 and
   all prior refs. One integration can cover dependencies+profiles; do not
   cherry-pick already ancestral 4dc0 again. Use the short repository-claim
   procedure (fresh target, hooks, SSH push, remote ancestry proof), then release
   before CI/records. On a moved target, repair/rebase unlocked; prove equivalence
   or obtain affected review/checks for actual changes.
3. **Owner0, patch source only after master proof:** reuse the existing patch
   worktree and start from its reconciled 8270b head. Confirm newest supported
   release branch is still `haveapi-0.30` and its current history is compatible.
   Append `git cherry-pick -x 4dc0f7e11c494d1a0dc852dabcc312411699fcab`, then each
   intended final profile commit in original order from integrated master.
   Stop for unexpected conflict/content changes; do not rewrite source under
   the guise of mechanical backporting. Retain source/backport SHA mapping,
   trailers and range-diff/patch-ID evidence.
4. **Pre-version proof:** with unchanged target b64, the patch's full tree must
   equal the accepted integrated source tree. If the target acquired other
   changes, first account for that scope explicitly; do not waive equality or
   silently backport unrelated commits. Preserve the comparison before version
   changes make source tree equality impossible.
5. **Owner0 mechanical versioning + lead prose:** prepare the patch worktree's
   declared dependencies, then run `make version VERSION=0.30.1` from the
   top-level Nix environment. Lead writes the new CHANGELOG section dated
   `# Sat Oct 24 2026 - version 0.30.1` (refresh to the actual preparation date
   if the work crosses another day). Keep the 0.30.0 section/date untouched.
   Commit version/changelog separately as the final `Version 0.30.1` commit
   after checks/hooks. Do not copy patch release metadata back to development
   master or bump its development line without a separate reason.
6. **Final candidate gate:** quick checks and complete committed release-range
   review, then final-head build-only verification. Publish the patch feature
   branch normally. Once green, owner0 may fast-forward the authorized
   `haveapi-0.30` branch to the prepared candidate under the same short claim
   procedure and prove remote ancestry; no tag is created. Preserve automatic
   target CI evidence and report 0.30.1 as prepared, not released.

Owner2 coordinates dependency/setup and retained package validation when
assigned; a fresh policy watcher runs long work. Owner1 may independently check
final source/metadata/artifact identity. Lead owns scope, prose, review packets
and candidate acceptance. Architect owns this execution design, no application
or Git operations. No concurrent edits to version files/CHANGELOG/index.

## Actual versioning boundary

At 4dc0, `Makefile:version` updates:

- `VERSION` and server, Ruby client, Go and Rust
  `lib/haveapi/**/version.rb` files.
- `servers/ruby/haveapi.gemspec`,
  `clients/go/haveapi-go-client.gemspec`,
  `clients/rust/haveapi-rust-client.gemspec` HaveAPI-client requirements;
  `clients/rust/Gemfile.lock` through `bundle lock --local`.
- `clients/js/package.json`, both root identity/version entries in
  `package-lock.json`, `src/haveapi/client.ts`, and
  `dist/haveapi-client.js`. The maintained target performs the version
  substitution; normal build must reproduce the bundle. Do not hand-repair
  generated output. Type declarations should remain source-equivalent.
- `clients/php/composer.json`, `clients/php/src/Client.php`.
- `clients/python/pyproject.toml` and `uv.lock` via `uv lock`.
- `examples/servers/ruby/activerecord_auth/Gemfile`.

Prepare the locked Rust bundle first with the documented component setup unless
already ready in this exact worktree. Do not borrow another worktree's native
bundle. `uv lock` is not permission for unrelated upgrades: inspect diffs and
stop on non-version dependency/input changes. Preserve JS's new 4dc0 dependency
lock exactly apart from package version fields. Rust's private runtime harness
version/Cargo lock and downstream crate version are independent and unchanged.
CHANGELOG is authored by lead; release notes derive from its new section.

The changelog should describe all changes since b64: strict publication metadata
confirmation; JS documentation/build/dependency/helper/cycle fixes; declared
Fiddle and scoped generated Rust lint; simplified optional SDK profiles,
server-derived schema and honest optional Git source. Include final implemented
behavior only. Do not reannounce 0.30.0 clients or say publication has occurred.

## Verification matrix

| Gate | Evidence required |
| --- | --- |
| Final feature before master | Profile quick checks, complete committed review/history conclusion, affected longer automatic-schema/auth/Go/Rust/legacy tests and ordinary final-head CI. 4dc0's earlier all 10 CI is retained separately. |
| Backport source | Each old/new `-x` correspondence, exact pre-version tree equality to accepted integrated source, no duplicate fix, explicit no-migration inventory. |
| Candidate quick | `make release-check`, `make release-test`; version paths/lock diffs and source-equivalence outside listed metadata/prose; tracked/index clean with preserved known caches and original artifacts. |
| Version-sensitive profiles | Real server 0.30.1 plus installed Go/Rust generator 0.30.1 accept omitted generator_version. Explicit matching/mismatching versions and legacy forms behave as specified. Do not let fake 0.30.0-only test constants mask default-version errors. |
| Candidate final review | Reviewer gets full b64-to-final range, source mappings, dependency/profile final reviews, version/changelog diff, and preserved history rationale. All intended commits/quick checks complete before long candidate campaign. |
| Candidate full campaign | Prefer the ordinary automatic branch `release.yml` build-only run at the final candidate SHA: locked dependency setup, i18n health, release tests, package build/Rust smoke, full maintained suites, npm/Python smokes, retained artifact verification. It never enters the publish job for a branch. If it is not automatically selected, lead may select one build-only workflow at that exact source, not a tag. |
| Coverage not in aggregate | Use profile's affected installed-render acceptance/permission/mount tests at source head. Rerun only the version-sensitive installed-profile subset on 0.30.1 where the aggregate lacks it. New Rust helper inputs need applicable 1.95 proof; a metadata-only backport does not require a duplicate full MSRV campaign when exact input applicability is established. |
| After target pushes | Fresh remote ancestry/final-head evidence and ordinary automatic checks, without dispatching duplicate local+feature+target full campaigns solely for identical inputs. |

The earlier plan deferred the authoritative full campaign to an annotated tag.
That is no longer the correct preparation gate: no tag is authorized now.
A build-only final candidate run provides the needed package verification.
It does not prove registry authentication, upload or delayed visibility. Label
prior MSRV receipts as prior applicable evidence, never fresh 0.30.1 results.

Read current Makefile/workflow again if profile implementation changes their
targets. A failed check is diagnosed before rerun. Any real code/input drift
after the reviewed source or metadata commit requires affected review/checks,
not an equivalence assertion. Retain all candidate output in a fresh artifact
location; never overwrite original 0.30.0/followup/regeneration artifacts.

## Compatibility, recovery and publication stop

No DB/protocol/state migration is expected. Old file profiles remain valid.
New minimal profiles require new server+optional adapter support; omission of
generator_version defaults to the server's version, so install matching 0.30.1
generator gems with a 0.30.1 server, or an explicit compatible override where
supported. Examples do not select the same version for SDK packages: their
versions remain optional and independent.

Mixed servers can temporarily display different documentation; authentication,
route authorization and client wire behavior must stay unchanged. A rollback
of the API bundle also reverts new-form configuration. No vpsAdmin deployment
is authorized here. The regenerated downstream crate remains pinned to 090a and
needs no update for profile rendering or release metadata.

Preserve published/default history, all original artifact bytes and previous
feature refs. Preparation failure is repaired on the owned feature; it is not
grounds to move a tag, rebuild accepted registry bytes, revert shared history,
skip checks or relax package identity. If later publication is explicitly
authorized, freshly check supported-branch/tag/setup facts, create the annotated
tag, use its original retained artifact set, and obtain the normal protected
environment approval. Diagnose any partial failure before any retry/reupload;
retain the existing strict identity/hash/source and GET-confirmation contract.
No current task runs publish, creates a draft/final release, or touches registry
settings/credentials/PHP mirror.

