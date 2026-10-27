# Generator, release workflow and client README handoff

## Performance comparison correction — merged

HaveAPI/master now contains reviewed commit
`4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`. The user approved integration with
“merge it”; implementer0 fast-forwarded from `18b45aed` and pushed normally over
SSH with ordinary hooks. The lead independently verified remote HEAD/master and
the retained feature at `4d36efcf`. Source/target are clean and the repository
claim is authoritatively released. [Integration receipt](performance-response-integration-result.json).

Responses may differ between revisions; timing and allocation limits remain
enforced. Independent review had no findings. All ten exact-head feature CI
workflows passed, including all 14 measured performance cases. Original retained
samples also passed a separate 14-case reanalysis; their historical failed run
and report remain unchanged. [Feature CI](performance-response-feature-ci-result.json),
[replay](performance-response-replay-result.json).

New master CI has seven passes and three active workflows at its first bounded
snapshot: Rust, server RSpec and performance. No current failure observed; no
rerun or waiting campaign. Older vpsAdmin broad CI also remains pending at the
latest read. Merge work is complete, CI assessment remains. Session stays active
and open; no release, deployment or lifecycle action occurred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/

## All five repositories integrated

The user approved merging all session feature work. Every final feature head is
now integrated into its remote default branch:

| Repository | Default | Integrated head |
| --- | --- | --- |
| HaveAPI | master | `18b45aed` |
| vpsAdmin | master | `08c3bd7e` |
| vpsadmin-go-client | master | `73f164dd` |
| vpsadmin-rust-client | main | `80be1c1a` |
| vpsadmin-typescript-client | main | `149c72f1` |

The lead independently verified fresh SSH default and feature refs against the
full intended commit IDs and confirmed clean source worktrees. All merges used
fast-forward Git operations, ordinary hooks and non-force pushes. Every merge
claim is released. Feature refs and prepared recovery worktrees remain available.
No package release, deployment or session lifecycle action occurred.

The exporter was rebased over one disjoint WebUI dependency update. Its patch is
byte-for-byte identical to reviewed `7456c7ea`; the lead independently rebuilt the
expected tree and matched integrated `08c3bd7e`. The old exporter is an equivalent
predecessor, not literally an ancestor of the integrated successor. The saved
schema still records its actual capture revision, and the TypeScript generator
pin is unchanged. [Equivalence certificate](vpsadmin-rebase-equivalence.json).

Rust and TypeScript post-merge CI passed, and publishing jobs were skipped. Go
has no configured workflows. vpsAdmin lint passed; broader CI `40531100170` is
still running. Ten HaveAPI workflows passed. Performance run `40529570313` failed
because four HTML responses contain the intentional 12-byte TypeScript SDK phrase
addition. The response-identity comparator stopped before timing classifications,
so no timing pass or regression is established. No benchmark policy, baseline,
budget or refs were changed, and the run was not retried.

All requested merges are complete. Post-merge CI remains under assessment, so the
session stays active and open. [State](state.md), [CI results](ci-results.md),
[fresh remote proofs](integration-remote-verification.json).

## Previous completed documentation milestones

## Member-focused wording correction

Allthree READMEs now address ordinary members directly, without automatic-owner,
internalnodepool or administrator-role commentary. Actual inputs, defaults,
resource units, quota/availability, IPcounts and deletion outcomes remain useful
and accurate. All45 fencedblocks/38examples and allnonREADMEobjects unchanged.

Final published/clean heads: Go `73f164dd5eeebfc494705ae27981d30872fa88c3`, Rust
`80be1c1a90b7009f8ddecf6a7fe042b506de8b42`, TS
`149c72f11acef67224a47ed77711a3abb805fbd4`. Sameparents/owningdocsamends,
complete1/1/3series, no migrations/obsolete/repeatedstreams. Lead directprosepass,
staticchecks and independent reviewer0 generalreview passed without findings;
no repeatcompilation of unchanged examples.
[Review](vps-readme-member-focus-review.md),
[packet](vps-readme-member-focus-review-packet.md).

All3 exactleasefeaturepushes/freshSSH/default/cleantracking proofs passed;
defaultbranches unchanged. Rust40526005081 and TS40526154339 succeeded at exact
finalheads, TSpublish skipped; Go has no workflows. No remaining work/blocker
for this correction. Ready, awaiting merge approval. No API/VPSaction, release,
defaultmerge, deployment or sessionlifecycle action occurred; session stays open.

## VPS lifecycle extension

The requested lifecycle guide is implemented and locally checked in all three
READMEs. It preserves the standalone read-only quickstart, then walks through
location/template selection, alternative default/configured creation, returned
VPS ID inspection/rename, separate power choices and member deletion. Resource
units, quota/default/IP allocation semantics and background completion are
explained together with the examples. All38 final code fences compiled without
execution or API requests; no SDK/runtime/generated/package changes.

Current amended heads: Go `51b86a59dc378eab1d84249094e27c80bdaf4d08`, Rust
`020f4ddb229d7892c76cf10e89ee7a792fddf9ad`, TypeScript
`a8966789bd24914daebd9fc0e33a51f76480c4ba`. All clean; parents preserved,
complete1/1/3series, old reviewed/published heads retained. Reviewer0's final
general documentation/history review passed with no findings. All three reviewed
heads are published with fresh SSH/default/clean proofs; defaults unchanged.
[Review](vps-lifecycle-readme-review.md), [packet](vps-lifecycle-readme-review-packet.md).
Go has no configured workflows. TS40523115572 and Rust40523070025 passed at
the exact final heads; the TS publish job was skipped. No implementation, review,
publication or CI work remains for this request. Ready, awaiting merge approval.
No release/default integration/deployment/session lifecycle action authorized.

## Previous completed README alignment

The user-requested Go/Rust/TypeScript README alignment is implemented, compiled
and independently reviewed. The guides share a read-only authenticated VPS
listing, separate inspection and hostname-only rename examples, and comparable
authentication/error/development sections. TypeScript's requested opening
version/private-publication wording is removed; maintainer guidance is now in
`docs/development.md`. Rust's obsolete links and Go's broken examples are fixed.

All 13 exact final code fences compiled without execution or API calls. Reviewer0
completed general documentation and complete1/1/3history review, no Blocking or
Important findings. Its single Go metadata-wording Advisory was narrowly amended
and directly verified with all six fences unchanged. [Full review](vps-client-readme-review.md),
[closure](vps-client-readme-disposition.md). No generated/runtime/package/release
metadata changed, no migrations or new pin stream.

Final documentation heads: Go `bb1bc9622fff5a95b9c922c5b419949235a0305f`,
Rust `2aad8d47c68d53ce1cb7e8669e083f96dc868a8c`, TypeScript
`e116b3e87ce73386b64d8291cffa1f24bb38b718`. All three are published/clean,
with fresh SSH proof and unchanged default branches. Go has no workflows;
TS run40516963287 and Rust40516988544 both passed at their exact heads; the
TS publish job was skipped. No README implementation, review or CI work remains.
This current checkpoint supersedes only the SDK
head/readiness statement in the earlier completed generator/release checkpoint
below. No actual release, default integration, deployment or lifecycle action.

## Earlier completed generator/release checkpoint

Implementation, quick checks, independent review and package acceptance are complete. Final feature branches are published and clean. All final-head CI passed, and no release has been made. The branches are ready, awaiting merge approval. The session remains active and open.

| Repository | Reviewed base/default | Published feature head |
| --- | --- | --- |
| HaveAPI | master `029f79b31cec93167f07e43e571c36b5f42d5b80` | `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875` |
| vpsAdmin | master `898e2881e8230d24fb06baee1c58737ae55e0009` | `7456c7eaae11cee0c76a984b1386a94656510f88` |
| vpsadmin-typescript-client | main, genuine empty root `6c67b3c6e10e4096f6717345026371a89691f62a` | `2dab582881c4af8d8b3f932d9f2308e133d8d925` |

All use branch `2026-10-26-typescript-client-generation`. Exact leases, fresh SSH feature/default proofs and clean tracking passed. No repository claim or machine reservation is held. Defaults are unchanged.

Go, Rust and TypeScript now share schema capture and support fetch/save followed by offline generation. Capture supports public access, Basic with an environment-held password, and an existing HaveAPI token. Go's legacy invocation remains supported. Generic generator guides include capture, generation and usage; the root README distinguishes dynamic JS/TS discovery from concrete TypeScript generation. vpsAdmin-specific acquisition instructions remain downstream. Ruby documentation has a separate optional generated-TypeScript profile/tab using current authorized samples and the existing runtime.

The release follow-up adds the TypeScript generator as a fifth gem in HaveAPI's existing release pipeline and adds a conventional npm workflow to the generated client. Both use trusted publishing and retained validated artifacts. The npm job refuses invalid package/version/tag/license prerequisites and repeated tag builds, while preserving retries of the failed publishing job against its original artifact. No token fallback, version bump, tag, registry setting or upload was introduced.

RubyGems supports a pending publisher for the new generator gem. Current npm documentation requires the package to exist before trusted-publisher setup; first npm bootstrap and ownership remain a separately authorized maintainer prerequisite. The SDK remains private `0.0.0`, with licensing unset. Publisher activation, environment protection and a later release require deliberate preparation and separate authorization.

HaveAPI's complete five commits separate shared capture, Go/Rust CLI integration, the complete modular TS generator, generated documentation, and release enablement. The client's two commits separate the initial reproducible SDK from release automation; its final producer pin/digest/manifest are consolidated into the initial commit. The exporter is unchanged. Independent reviewer0, retaining gpt-6.1-sol/xhigh/read_only settings, explicitly concluded no obsolete history, repeated update streams or migrations. [Release review](release-workflow-review.md) and [unified generator review](unified-generator-review.md).

The release review found two Important defects in archive listing parsing and tagged rerun recovery. Both requested narrow fixes were folded into the release commit and directly verified: six regressions, workflow lint, and a positive full archive consumer passed. [Finding closure and artifact hashes](release-review-disposition.md). All 674 generated TypeScript modules, schema, provenance and locks remain unchanged. Final manifest SHA256 is `48a6471ce38c767b17b174c76c56add6006350d4b01226542eab3498f2877727`.

Quick checks passed across the shared core, all three generators, documentation adapters/server profiles and release tooling. Actual capture and rendered programs passed against published runtime 0.30.2 at root and mounted URLs. New release acceptance passed extracted TS/shared Ruby gems and the retained npm archive's ESM, strict types, executor and receipt checks. No database export or unchanged rendered-wire suite was repeated for release preparation.

Corrected release version preparation passes all213Ruby and6Python tests. The Makefile clears inherited Bundler lock state; its real version regression injects that state explicitly. Final HaveAPI18b45aed and client2dab582 preserve the previously tested generator/gem/runtime inputs and release patch. The client differs only in its producer revision; the lead independently reconstructed both commit trees.

All seven final CI workflows passed, including the corrected full release build and SDK validation. Both protected publish jobs were skipped. Performance40405397920 compared the genuine f02eca2e→18b45aed push pair: all14cases passed timing/correctness/allocation classification, with zero regressions or inconclusive cases. [CI evidence](ci-results.md). Prior failed runs retain their original scope and are not relabeled as passes. No benchmark, baseline, budget or ref manipulation occurred.

No implementation, review, artifact or CI work remains for the current request. The user still owns integration approval for HaveAPI/master, vpsAdmin/master and client/main. A future actual release requires separate authorization and the package/version/license/trust prerequisites described above. Keep all feature branches and the active/open session. No lifecycle action or deployment is authorized; WebUI adoption remains deferred to the separate runtime upgrade integration.

Project guidance: HaveAPI `clients/{go,rust,typescript}/README.md`, `doc/client-examples.md` and `doc/agent-instructions/releases.md`; vpsAdmin `docs/api-schema-export.md`; generated-client `README.md` and `docs/releasing.md`. [State](state.md), [plan](plan.md) and [design](design.md) retain decisions and earlier receipts.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/
