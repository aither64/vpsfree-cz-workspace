# HaveAPI 0.30.1 release and approved integrations

**Updated scope, 2026-10-24:** use
[integration-backport-release-preparation.md](integration-backport-release-preparation.md)
for the authorized default integration, remaining backports and 0.30.1 metadata
preparation. It supersedes this record's older frozen-source/order and tag-based
verification assumptions. Publication/tagging remains unapproved; original
artifact/recovery safeguards below remain applicable. The completed six
backports are reused, not replayed.

**Publication held by subsequent user instruction.** The
[dependency-refresh addendum](dependency-refresh-addendum.md) governs new source
work and verification. Preserve this plan's artifact/recovery safeguards, but
do not resume versioning/tag/publication from the old grant. Patch8270b is frozen
at VERSION0.30.0; new dependency development starts from merged090a in a separate
worktree after lead grant.

Architect brief, 2026-10-23. The user authorized **HaveAPI 0.30.1 publication**,
first integrating the reviewed fixes into HaveAPI `master`, and separately
integrating the regenerated vpsAdmin Rust client into its `main`. This supersedes
the earlier development-only hold for these exact purposes. No new Rust crate
version/publication, schema refresh, credential/configuration change or deployment
is authorized. The existing protected GitHub environment approval remains part
of execution; another conversational publication permission is unnecessary.

## Frozen inputs and fresh observations

Fresh canonical SSH reads and the public GitHub release GET on 2026-10-23 at
approximately 19:55 UTC established:

| Repository/ref | Exact observed revision |
| --- | --- |
| HaveAPI master and newest supported `haveapi-0.30` | `b64fb25bea8d8222fb3263b99956c0b61438a859` |
| HaveAPI reviewed fixes | `090a188cb4ef3477324718627f4ae3415d1c0975`, tree `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2` |
| Annotated `v0.30.0` | object `81a896f97b75781f62c5850a6e8df7932c92782b`, peeling to b64fb25 above |
| `v0.30.1` | absent; recheck immediately before tag creation/push |
| vpsadmin-rust-client main | `945af6a97717a7a6373507bbc9592d5cd53727c2` |
| Reviewed regenerated client | `ff876abe17e3301da62c1b6afbda055ec89db9d2`, tree `322fa86ba290b5936a327c21371c94f96f86b249` |

Canonical SSH remotes are `git@github.com:vpsfreecz/haveapi.git` and
`git@github.com:vpsfreecz/vpsadmin-rust-client.git`. The public 0.30.0 release is
complete (`draft=false`, `prerelease=false`, eleven assets); its original run
39849807897/artifact 12455689943 and all original local/development bytes remain
immutable. Existing four-lane review, eight local/seven CI HaveAPI results and
the downstream four-lane review/eleven local/four CI results remain retained.
See [downstream final handoff](vpsadmin-client-final-CI-receipt.md) and
[0.30.0 destination proof](release-destination-verification.md). These are prior
input evidence, not verification of the forthcoming 0.30.1 final head.

Source authorities: HaveAPI `AGENTS.md`, `doc/agent-instructions/releases.md`,
`development.md`, `Makefile`, `.github/workflows/release.yml`, and
`utils/release/{artifacts,workflow,registry_query,publish,cli}.rb` at 090a.
The unchanged workflow validates newest-release-branch ancestry, remote tag,
shared version, enabled publication and required environment reviewers. No
workflow/action upgrade is part of this release.

## Owners, dependencies and source preparation

**Implementer0 owns all Git/index/hooks in both repositories**, the new patch
worktree, backports and mechanical shared-version metadata. **Lead owns final
CHANGELOG/release-notes prose**, tracking, grants and review/verification launch.
**Implementer2 owns publication/setup-readiness and recovery preparation** from
existing helpers and the tagged artifacts, with no source changes expected.
**Implementer1 owns independent destination verification** against the original
new tagged-run artifacts. No overlapping application edits; architect edits
these design records only. Lead coordinates any additional defect before edits.

1. Owner0 integrates reviewed HaveAPI 090a to fresh `master` with ordinary
   fast-forward and hooks, SSH push and remote ancestry proof. Independently
   integrate downstream ff876abe to fresh `main` with the same short procedure.
   Preserve downstream pin090a, crate0.1.0, saved schema and package bytes. It
   does not need to repin/regenerate for HaveAPI's patch version. Use one
   repository claim at a time only for final target check/merge/push/proof;
   release before CI, records or subsequent preparation. Any moved baseline or
   conflict returns to unlocked preparation and equivalence/review assessment.
2. Create a registered, clean patch feature worktree under
   `worktrees/2026-10-22-haveapi-release/haveapi-0-30-1`, registered name
   `haveapi-0-30-1`, branch
   `2026-10-22-haveapi-release-0.30.1`, based on fresh `origin/haveapi-0.30`.
   Lead accepted this spelling on 2026-10-23 because the registration tool
   rejected dotted name `haveapi-0.30.1` before creating any ref or registration.
   The branch spelling and exact b64 base above are unchanged. Owner0 may continue
   without further approval and will report the stable registered path before
   lead's prose edit; this is not a claim that registration is already complete.
   This tool-compatibility correction changes no source, verification or
   publication boundary. Preserve the original HaveAPI/followup/downstream trees
   and artifact directories. Apply these six commits with `git cherry-pick -x`
   in order after master integration, as the repository patch procedure requires:

   ```text
   cbf6a3f0b34f15e2bb4224872b46c423d7d02313 Fiddle dependency/smoke
   431d7ffed098c7403d3d0555b3b93c4a3ab8b3e3 scoped generated naming lint
   01a30a39cdfc0d81e2eca62dcce912c165d891fa JS tooling/ES5 helpers
   412511176d7f54a96d48bc0995b202f335d1be4f JS import graph
   c424c579a314593e25cfe661374caafb9ab78a4c registry confirmation
   090a188cb4ef3477324718627f4ae3415d1c0975 generated JS bundle/declarations
   ```

   Before versioning, require the backported source tree to equal tree e947
   above; retain exact source/backport SHA pairs, `range-diff`/patch IDs and all
   six provenance trailers. Preserve the generated commit and logical boundaries.
   A conflict or non-equivalent tree is a stop for design/review, not permission
   to quietly rewrite the accepted fixes. No duplicate backports onto master.
3. In the new worktree's declared Nix environment, prepare the frozen Rust
   bundle using `nix develop .#client-rust -c true` unless already prepared;
   setup uses a fresh policy utility if its duration is uncertain. Then run
   `make version VERSION=0.30.1` in the top-level Nix shell. No dependency/input
   upgrade, native bundle borrowing or hand-edited generated output.
4. Lead writes `# <actual release date> - version 0.30.1` in CHANGELOG.md.
   Describe only fixes since 0.30.0: bounded strict registry confirmation and
   recovery diagnostics; maintained JS documentation/build tooling, bundled
   helpers and removed import cycles while preserving ES5/public declarations;
   explicit generator Fiddle dependency and scoped nested-resource lint
   allowances. Do not reannounce 0.30.0 features or claim all warnings vanished.
   Generated release notes come from this section; no separate manual asset edit.
5. Owner0 commits version metadata plus lead's CHANGELOG as a separate final
   `Version 0.30.1` commit with hooks. Source patches stay separate. Shared
   metadata need not be copied back to development master for this patch release.

Expected metadata boundary: `VERSION`; server/Ruby-client/Go-generator/Rust-
generator `lib/**/version.rb`; server/Go/Rust gemspec HaveAPI-client requirements;
Rust `Gemfile.lock` local versions/requirement; JS `package.json`, both root
`package-lock.json` version fields, `src/haveapi/client.ts` and generated
`dist/haveapi-client.js`; PHP `composer.json`/`src/Client.php`; Python
`pyproject.toml`/`uv.lock`; the ActiveRecord example Gemfile; `CHANGELOG.md`.
Review lock diffs as version-only local package changes; stop on unrelated
dependency resolution. Private Rust Cargo harness/version and downstream crate
stay unchanged. A normal JS build must reproduce the committed bundle; all
declarations remain those of the reviewed fixes. No manual dist repairs.

## Quick, final review and longer verification gates

After complete metadata/prose, run `make release-check` and `make release-test`
in the top-level Nix shell, inspect exact source equivalence outside the named
metadata boundary, all shared-version fields and lock diffs. Commit every
intended change before independent final review. Supply reviewer0 the full
b64-to-new-head series, six source/backport correspondences, final diff, new
CHANGELOG, prior review/quick receipts and explicit **no migrations** inventory.
Review covers release metadata/history and preservation of accepted fixes and
publication safeguards; retain the same reviewer and relevant four-lane
concerns for this irreversible publication boundary. Earlier 090a review is
supporting evidence, not review of a partly committed new release.

Verification proportionality adjustment, 2026-10-23: use the annotated-tag
workflow as the authoritative full campaign for the new version. Do not repeat
the full local followup batch or dispatch another build-only workflow merely
because the release metadata changed. Existing automatic branch/default CI can
run normally; retain its evidence without manufacturing additional campaigns.
The final matrix is:

| Gate | Required evidence and timing |
| --- | --- |
| Fresh quick checks | `make release-check`, `make release-test`; exact shared versions and only expected local-package lock changes |
| Source equivalence | Six backports and pre-version tree exactly equal 090a/e947; final diff limited to precise 0.30.0-to-0.30.1 substitutions and lead CHANGELOG; clean tracked source/index |
| Final committed review | Complete b64-to-final-head series, provenance trailers, final diff, metadata/prose, accepted source mapping and no migrations, before release publication/tag campaign |
| Existing source-only extended checks | Retain 090a local/CI receipts, including explicit Rust1.95 NAME_LINT and maintained documentation task; reuse only under the unchanged-input proof below |
| Ordinary automatic branch/default CI | Preserve normal feature publication and collect naturally triggered results; do not dispatch duplicate checks or demand redundant full build completion solely to start the equivalent tag campaign |
| Authoritative 0.30.1 long check | Fresh annotated-tag run, exact final source and original artifact ID; all existing build/test/package steps must succeed before protected-environment approval |
| Publication and independent proof | Strict fixed-helper confirmation and original-artifact destination checks described below; unchanged hash/source/recovery gates |

The tagged workflow itself executes:

```text
make release-deps
bundle exec rake i18n:health
make release-test
make release
make test
ruby utils/release/cli.rb smoke-npm dist
(cd clients/python && uv run --locked python utils/package_smoke.py)
ruby utils/release/cli.rb verify dist
```

This rebuilds the version-sensitive JS bundle, declarations and all maintained
packages; make release includes the retained Rust gem/Fiddle smoke, and make
test includes ordinary runtime/default/blocking/generated-client protocol and
documentation checks. The workflow intentionally reruns release-test at the
tagged head; no workflow alteration is requested. Inspect full logs and actual
warning inventory. The Python package_smoke builds temporary packages and is
not an installation check of the original retained wheel. No local compiler,
package or live-server campaign is additionally required for version-only work.

The separate 090a Rust1.95 NAME_LINT proof is reusable because this patch changes
only the generator version/manifest identity and local Ruby package versions:
IR/naming/templates, eight runtime files, generated fixture/schema/config,
private Cargo manifest/lock, formatter/compiler/input pins and integration
runner must all remain unchanged. The added gem dependency and exact Fiddle
resolution also stay fixed and are retested by the new retained-gem smoke.
The JS documentation task/alias tooling likewise remains unchanged and its
content checks run again within the tag suite. Retain the actual prior tool/input
receipts, not just tree equality, and explicitly describe these as 090a results
reused for unchanged code rather than a fresh 0.30.1 MSRV/task run. Source digest
changes caused by generator VERSION alone do not change generated Rust APIs.

Any non-version lock/dependency change, source/template/fixture/toolchain change,
unexplained bundle drift or newly failed automatic check invalidates the relevant
reuse. Stop for bounded diagnosis, then select only the affected extra check and
review; do not add a blanket full campaign or ignore a known failure. Preserve
tracked/index cleanliness, frozen known-cache inventories and original artifacts.
Lead uses the fresh watcher policy to monitor actual automatic/tag CI, not to
launch the superseded local batch from the older followup verification plan.

Owner0 publishes the reviewed patch feature normally. After the quick checks,
equivalence proof and committed final review, fast-forward shared `haveapi-0.30` from the
prepared feature under the short HaveAPI claim and record remote proof. Recheck
latest supported line, tag absence and exact final head, then create/push one
annotated `v0.30.1` at that head; no existing tag moves. The tag must be contained
by remote haveapi-0.30 before the tagged helper runs. A safe non-force atomic
release-branch/tag push can satisfy this ordering if prepared by owner0. Do not
leave a claim held for CI or environment approval. No new release tag is pushed
while this release is unfinished. Before environment approval reconcile any
known automatic-CI failure, including a distinct lane absent from release.yml;
do not relabel it harmless because the tagged build passed. Successful older
or branch build artifacts never substitute for the tag run's original files.

## Actual publication and confirmation acceptance

Owner2 prepares fresh read-only readiness for enabled publication, protected
`release` environment/reviewers/tag policy and current mirror state using
existing account setup. Record access denial as unknown, not absence. Read no
credential values, upload no secret, change no publisher/registry setting.

The annotated-tag run's build is the authoritative new publication candidate.
It runs the existing workflow's release/core/package checks, retains
`release-<new-run-id>` and verifies its manifest. Branch/local builds are separate
evidence and must never substitute for this artifact. Before approval record
exact tag object/commit, new run ID, original artifact ID, manifest SHA-256,
tools/locks and all file hashes; download and preserve original bytes in a fresh
`release-0.30.1-<run-id>/original-artifacts` session directory. Inspect full build
logs and summary. Existing successful 0.30.0 artifacts are never replaced.

The authorized operator approves only this exact candidate's protected
environment after those gates. Use the existing OIDC job, tools-only Nix shell
and PHP secret reference; no local publisher or spoofed Actions environment.
The workflow retains a draft Release, preflights PHP/all registries, uploads
missing original Python files through PyPA, confirms PyPI, then publishes and
confirms client/server/Go/Rust gems in catalog order, npm and PHP, finishing
GitHub only after strict final confirmation. No packages are built after approval.

Exercise the corrected helper naturally through this actual release: retain
`Registry preflight`, post-upload and final-confirmation logs with package/version,
attempt/status/elapsed/missing fields and permitted cache/Retry-After headers.
Require exact 0.30.1 identities/hashes and each destination's confirmed receipt.
Canonical missing/incomplete reads permit the one same-endpoint cache-distinct
GET; transient read failures use bounded 2/4/8/15/30-second backoff and parsed
Retry-After minimum, never shorter than normal backoff. Preflight is bounded by
60 seconds; confirmation by ten minutes; final registry checks share ten minutes.
Uploads never occur inside the GET retry loop. TLS/auth/schema/identity/platform/
digest conflicts stop. PyPI preflight's positive union affects staging only;
post-upload/final success requires one complete strict response.

No deliberate cache poisoning, delay injection, extra uploads, registry toggles
or stress traffic. A first-attempt successful response proves the real success
path; only naturally observed retries prove a live retry path. Fake-clock/
transport tests remain the failure-path evidence. Do not claim to have reproduced
the 0.30.0 cache incident if this release has immediate metadata visibility.

## Independent destination proof and recovery

After terminal publication, owner1 performs one read-only pass using the NEW
run/head/original artifact set, adapting the existing
[destination verification protocol](release-destination-verification-plan.md)
to 0.30.1. Compare four RubyGems exact name/version/platform and SHA-256 values;
npm identity and retained tarball SHA-512 integrity; PyPI exact wheel/sdist
filenames, uniqueness and SHA-256. Require all eleven public GitHub assets
(ten catalog files plus manifest) and notes to match original retained bytes.
Retain any additional Actions-only smoke receipt without treating it as a public
asset. Check PHP tag/master source trailer and normalized snapshot paths/content/
modes against original PHP archive, then Packagist exact version/source commit.
PHP indexing lag is distinct from upload success. No verification command may
invoke publisher modes or install/run code downloaded from registries.

On any failed/uncertain publication, owner2 diagnoses the precise step and
accepted uploads against original metadata/payload hashes before lead selects
recovery. No automatic rerun/reupload; a missing metadata response is not proof
that an accepted upload failed. Preserve tag, original run/artifact and draft
assets. An explicit justified failed-job rerun uses the SAME run and original
artifact; even rerun-all restores it rather than rebuilding. Conflicts fail,
matching versions skip, partial PyPI staging contains only missing original files.
Never use skip-existing, loosen identity/digest checks, overwrite versions or
move tags. Missing/expired accepted artifacts require original draft assets and
operator-assisted diagnosis, not replacement builds. A source correction needs
a separately authorized future patch release, not mutation of v0.30.1.

Compatibility: no protocol, database, persisted-state, runtime-wire or deployment
migration. Mixed 0.30.0/0.30.1 clients/servers remain compatible; generated Rust
public names stay fixed. Fiddle/libffi affect generation tooling, not downstream
crate runtime. Consumers can select the prior release; public package rollback
does not delete or replace registry bytes. Downstream main integration does not
publish its unchanged 0.1.0 crate.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
