---
lifecycle: active
---

# Current phase: 0.30.0 released and verified; development follow-up design

HaveAPI 0.30.0 preparation is implemented, independently reviewed and verified.
The feature branch is published. The user now explicitly approved integration
and making the release; [authorization](release-authorization.md) records its
HaveAPI-only scope. Integration and official branch/tag creation succeeded at the exact reviewed
head. The tagged build passed; publication attempt 1 failed after the official PyPA
upload step reported success. Diagnosis and original-artifact verification are
running before any retry. The session remains open. Previous preparation handoff: [final-release-handoff.md](final-release-handoff.md).

## Exact source and phase checklist

- Repository: `vpsfreecz/haveapi`, SSH `git@github.com:vpsfreecz/haveapi.git`.
- Branch: `2026-10-22-haveapi-release`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Reviewed base: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`.
- Integrated remote master: `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Final local and remote feature head: `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Final tree: `05384a632290653cb4560c7451b3897acd5956c8`.
- Official `haveapi-0.30` and peeled `v0.30.0` both point to that final head;
  annotated tag object `81a896f97b75781f62c5850a6e8df7932c92782b`.
- 22 logical commits; final commit message exactly `Version 0.30.0`, no body.
- Tracked source clean, index empty; known unrelated caches preserved.

- [x] Implement release tooling, all requested examples and optional Go/Rust profiles.
- [x] Remove filesystem documentation panels while preserving the separate project.
- [x] Complete owner quick checks and all mandatory commit hooks.
- [x] Consolidate complete branch history and independently review final committed source.
- [x] Build final artifacts, verify manifest and all 12 retained file hashes.
- [x] Pass installed dynamic wheel/sdist/npm and Rust acceptance with reviewed input equivalence.
- [x] Compile and execute all 16 rendered Go programs at the exact final head.
- [x] Pass all ten CI workflows at the exact final head; publish feature branch over SSH.
- [x] Obtain explicit HaveAPI/master integration and release authorization.
- [x] Finish fresh target/publication preflight and integrate with hooks/remote proof.
- [x] Pass all ten post-integration master CI workflows at exact `b64fb25b`.
- [x] Create official `haveapi-0.30` and annotated `v0.30.0` at the integrated source.
- [x] Build and retain the original tagged candidate; verify manifest/catalog SHA-256.
- [x] Diagnose publication failures and complete publishing from the original retained bytes.
- [x] Verify registry hashes, PHP mirror/Packagist and GitHub Release results.
- [ ] Implement publishing confirmation/build-warning fixes on the separate development branch.
- [ ] Commit, independently review, verify and push the development branch; do not merge or release.

## Accepted verification

Final [independent review](go-query-final-review.md): no Blocking, Important or
Advisory findings. Retained reviewer0, thread
`01a16406-faaa-7cd0-bde3-c20802c18a72`, project
`01a16406-fa76-7532-9ee4-a890352500df`, saved and actual
`gpt-6.1-sol` / `xhigh` / `read_only`; no overrides, fallback or nested agents.
General, architecture/repetition and scope/proportionality lanes pass. Earlier
high-risk URL/authentication/compatibility conclusions are retained through exact
unchanged-source proof. Full 22-commit history, consolidated update streams and
final diff assessed: no obsolete approaches, redundant updates or migrations.
Inventory and equivalence: [go-query-final-receipt.md](go-query-final-receipt.md).

At exact final `b64fb25b`, the artifact/Go batch passed exit 0 in 24.24 seconds:
manifest verification, extracted Rust generator/runtime packaged smoke, dedicated
Go preflight, and all 16 rendered Go programs compiled and executed. See
[result](go-query-verification-result.json), [log](go-query-verification.log),
[exit](go-query-verification.exit) and
[final 12-file SHA-256 inventory](final-artifacts-b64fb25b-sha256.json).
Artifacts remain in the HaveAPI worktree's `dist/`; prior artifact sets and
failed execution evidence remain preserved under their original identities.

Installed npm plus Python wheel and sdist acceptance passed all six variants
(36 programs and 42 logs per distribution), including sync/async no-token
challenge flows, at actual `3fb91caf783eaeacf49bf3647b8409d536339d71`.
See [wheel result](go-final-acceptance-results/dynamic-wheel/result.json) and
[sdist result](go-final-acceptance-results/dynamic-sdist/result.json).
Rust root/mounted, async/blocking, development 1.99 and MSRV 1.95 acceptance
passed at actual `48543f8cd254eb0fc087931a5dc98ea730fd94af`, 26 programs per
mount, exit 0 in 915.38 seconds; [result](rust-documentation-verification-result.json).
These are retained executions at their actual heads, not final-head reruns.
The reviewer independently reconstructed 748 unchanged tracked entries, nine
matching dependency locks, and all 310 original Rust input objects plus both
flake inputs. See [input equivalence](go-query-final-input-equivalence.json)
and [Rust equivalence](go-query-final-rust-input-equivalence.json).

All ten automatic CI runs are completed/success at exact `b64fb25b`, freshly
confirmed at `2026-10-22T19:57:51Z` in
[go-query-ci-status.json](go-query-ci-status.json). Release build
`39843638181` and Rust `39843638091` succeeded. No dispatch, rerun, publication
job or tag action was needed. Fresh SSH remote proof confirms feature `b64fb25b`
and unchanged master `a32b15e`; [push receipt](go-query-push-ci.md).
No verification or Git operation remains running.

## Remaining scope and owners

Lead owns authorized integration/publication coordination. Sole Git owner
implementer0 owns clean target preparation and serialized Git operations;
implementer1 owns read-only publication preflight. No application source changes
are assigned. There are no outstanding implementation/review/test findings.
The user confirmed both new RubyGems/PyPI publishers are configured and npm is
established. Some GitHub setup metadata remains unreadable to the API credential;
[release-checklist.md](release-checklist.md) records the exact publisher tuples
and access gaps. The workflow will check activation and publishing credentials.
Remote master now equals the reviewed final head. Merge claim
`a30d80f5-7287-4586-9bdd-67afc2b84d32` was released and verified at
20:30:34 UTC. [Integration execution](release-integration-execution.json) records
ff-only merge, normal SSH push and exact remote proof. Official branch/tag atomic SSH push passed;
[release tag execution](release-tag-execution.json) proves exact refs. Tagged
publication and destination verification remain. A fresh Luna/low utility owns
release/master/release-branch CI observation, with no approval/retry authority.
Tagged release run: [39849807897](https://github.com/vpsfreecz/haveapi/actions/runs/39849807897),
exact event `push`, tag `v0.30.0`, source `b64fb25b`. No deployment or lifecycle action is authorized.

Project documentation was completed with the implementation and reviewed.
This update reconciles session evidence only. Earlier state is preserved intact
in [state-before-final-release-handoff.md](state-before-final-release-handoff.md);
its pending/failed statuses describe historical checkpoints.
Reusable Go fixture lessons are in
[the workspace note](../../notes/haveapi/2026-10-22-go-documentation-fixture-build.md).

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Tagged release attempt 1

Exact tagged run `39849807897` build job `120072628557` succeeded. The protected
environment was approved by account `aither64`; the lead did not issue an API
approval. [Approval history](release-publication-approval-history.json). Publish
job `120075071682` successfully prepared draft assets, configured RubyGems OIDC,
staged missing Python files and ran the official PyPA upload step. Its final
helper failed with `PyPI publication is incomplete; upload the retained Python
artifacts first`. This is a failed/possibly partial release, not completion.
[Failed step log](release-publication-watch-39849807897-failed.log).

Original retained artifact ID `12455689943`, `release-39849807897`, archive digest
`sha256:38a9e7e0308acd56ff3637a5c28df8660d70cdec648912b0511266a6db7fb26c`
is downloaded into `official-release-39849807897/`, separate from every earlier
artifact set. All ten catalog SHA-256 values and manifest schema/source/version/
tag/run identity match; eleven files retained. Manifest SHA-256
`f75323d63fec4f3b88a70845bffc39ca4440dd0b7fd94000f95054708e0a7890`.
[Original candidate inventory](release-official-candidate-inventory.json).

Owner1 diagnoses PyPI upload/verification from original logs and official metadata;
owner2 maps other actual destinations read-only. No rerun, tag movement, rebuild,
registry or source correction is authorized by those packages. No release runner
remains active; lead owns the read-only local artifact verifier handle. Preserve
the original tag, artifact and draft assets under the repository recovery contract.

## Recovery attempt 2

[Diagnosis](release-publication-failure-diagnosis.md) confirms both Python uploads
returned 200 and are now public with original hashes. [Other destinations](release-partial-destinations.md)
remain unpublished. The lead accepted the original tagged artifact after full
verification and authorized one failed-publish-only rerun under the repository's
recovery contract; [decision](release-publication-recovery-decision.md).
`gh run rerun 39849807897 --failed` exited 0; exact source/tag unchanged, attempt 2
waits on protected environment `release` ID `24722193856`. No rebuild or new tag.

GitHub reports `current_user_can_approve=true`, but the approval POST returned
HTTP 403 `Resource not accessible by personal access token`. This credential
cannot approve the deployment. [Pending state](release-publication-attempt2-pending.json),
[request](release-publication-attempt2-approval-request.json),
[refusal](release-publication-attempt2-approval-response.json). The user has been
asked to approve through the existing run's Review deployments UI. This is an
API capability blocker, not renewed release authorization or an automatic
approval-review rejection. Do not bypass environment protection or read credentials.

The user replied **Approved in GitHub** for attempt 2. Fresh exact-run status
confirms `in_progress`, attempt 2, unchanged `v0.30.0`/`b64fb25b`. A fresh
Luna/low utility observes only this recovery attempt; no further retries granted.

## Recovery attempt 2 result

Attempt 2 failed after all four RubyGems uploads reported success. The first
three gems were confirmed; `haveapi-rust-client` confirmation did not become
complete within the helper's 12 reads/5-second polling window. Original artifact
ID `12455689943` is unchanged and its creation timestamp remains 20:37:43 UTC.
Python existing hashes were verified and the PyPA upload step was skipped.
No npm/PHP/public GitHub completion was reached. [Failure log](release-recovery-watch-run39849807897-attempt2-log-failed.txt),
[final observer result](release-recovery-watch-final-result.json). The fresh
watcher has exited; no workflow/local verification remains active.

Owner2 now owns a single read-only official gem metadata/hash pass and diagnosis
against the original tagged artifact. No further rerun, source/tag change or
registry mutation is authorized by that assignment. Preserve both failed attempts.

## Newly authorized development follow-ups

After 0.30.0 is resolved, fix registry confirmation and the original tagged build
warnings on a new development branch. No further release without explicit user
approval; no default integration for this follow-up is authorized. Architect0
owns full-output investigation/design now, with no application edits. Separate
branch/worktree and implementation packages follow the design and release
resolution. [Follow-up plan](release-followups-plan.md). The npm upload has not
been reached because ordered publishing stopped at gem confirmation.

## Recovery attempt 3

All four gems now have public metadata matching the original run manifest.
Rust's direct public gem download also matches the original 44,544-byte payload.
[Visibility controls](release-rust-metadata-visibility.md),
[lead normal canonical GET](release-rust-metadata-lead-normal-read.json).
The exact earlier cache response cause remains bounded by the recorded evidence.

Lead authorized one failed-job-only resume with the original tag/artifact after
that confirmation; [decision](release-publication-attempt3-decision.md). Attempt 3
of run `39849807897` waits on the same protected `release` environment; user
was asked to approve because the current API credential cannot do so. No source
change, rebuild, new tag/release, overwrite or configuration change. A fresh
Luna/low operation watcher observes only this attempt, log
`release-attempt3-watch-native.jsonl`. No further retry is preauthorized.

User confirmed **Approved in GitHub** for attempt 3. Fresh utility continues
observation; final destination verification follows terminal result. The later
source fixes remain development-only and do not change this release.

## Attempt 3 success

Exact tagged run `39849807897`, attempt 3, is completed/success at immutable
`v0.30.0`/`b64fb25b`. Publish job `120082754287` succeeded; build is represented
as successful job `120082756581`, with original artifact `12455689943` still
sole/unexpired. GitHub Release is public with eleven uploaded assets. The fresh
watcher exited; [result](release-attempt3-watch-result.json). No command remains
active from that batch. Owner1 now performs the single read-only final registry/
PHP/Packagist/GitHub asset verification against original tagged bytes; this is
required before calling the release verified. Source follow-up remains separate.

## Release resolved; follow-up boundary

Lead accepts [final publication verification](release-destination-verification.md)
and [18/18 machine-readable checks](release-destination-verification.json).
HaveAPI 0.30.0 is public and verified at all destinations, including npm. Public
Release `421179188` published at 20:58:50 UTC with eleven original matching assets:
https://github.com/vpsfreecz/haveapi/releases/tag/v0.30.0 . PHP mirror master/tag
`397c95ff71ded9db98b214d58ea14a61c9973442` records exact HaveAPI source `b64fb25b`,
36 normalized files match the official PHP tar, and Packagist 0.30.0 references
that commit. Four gem SHA-256, npm SHA-512 integrity and both Python hashes match
the original tagged-run manifest. Verification finished at 21:03:40 UTC; no
publication operation remains running. All previous failure/partial states are
historical and retained. No further release without fresh user approval.

The newly authorized development follow-up now proceeds separately. Architect0
finishes the full warning/publication-confirmation brief; implementer0 prepares
`haveapi-followups` worktree/`2026-10-22-haveapi-release-followups` branch. No
follow-up app edits have started. This initiative remains active for that work.
