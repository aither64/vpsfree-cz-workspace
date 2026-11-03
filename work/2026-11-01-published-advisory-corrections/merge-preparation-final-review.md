# Merge preparation — independent affected final review

Lead-recorded summary of reviewer0's returned report. The full independent
report is retained in native reviewer thread
`01a19801-1fc5-70e3-ba37-8c0952a89392`.

## Findings and disposition

Blocking: none. Important: none.

Advisory A1: preparation receipts incorrectly described all60 diagnostic
observations as HTTP200/successful. Reviewer independently parsed the actual
observations: **60 expected outcomes =48 HTTP200/status:true +12 expected
HTTP404/status:false denials**. All36 counted collection requests succeeded and
returned integer total_count; no HTTP200/status:false occurred.

Accepted. Lead corrects state/handoff wording; implementer0 corrects its technical
receipts and checks any earlier isolated-case wording against existing artifacts.
This is evidence wording, not a source defect. No test or review rerun is needed.

## Reviewer and method

Retained reviewer0, review-purpose/read_only, saved gpt-6.1-sol/xhigh, codex-lb.
Same-session roster/native identity verified; no override, fallback, authorship
or nested reviewer. Session/current matched the trusted binding; both environment
markers were absent in the review shell. No source/session writes, tests, builds,
fetches, integration, deployment or lifecycle action by reviewer.

Risk HIGH. Lanes: general/history, architecture/repetition, scope/proportionality,
risk/compatibility. All skill references read. Scope accepted as the existing
spec diagnostic/assertion, owning KB observation repair and exact-source pins.
Earlier unaffected application/UI review is retained at its proven boundaries.

## Exact complete reviewed ranges

| Repository / target | Base | Final head | Tree |
| --- | --- | --- | --- |
| vpsadmin / master | 1d4869b6e81dd60916ecb96688ca14a192000b1f | ebe0ab51509222fba69a53431ea512cea51e2b6a | b38d589d1c01cc062b24ce985dcf4c973974d42c |
| vpsfree-kb-contracts / master | ce2c8cd9358c3636e5d39343e595df813a0b197f | c46bc3f753439b962ae4e11c59a71e15c0a56b87 | b41ecfb7bf73bd603f1bb6f9bacdfd8fcd8b1c97 |
| vpsfree-cz-configuration / master | c040c14cdbacc07998700b524996a89306188d7f | 2dde37693f6f5a060c0f36073611770478b4c1da | b426c60c8dcfb6d50a6e2b35828be6c5e78e1b95 |

API complete series: A193fe69e720b01626611f2883591c285c2b1d982 then
Bebe0ab51509222fba69a53431ea512cea51e2b6a;26paths,+2194/-155.
KB complete series: f2ae9b28782efc2c8d2a95f9a97de88d2adc9042 then
c46bc3f753439b962ae4e11c59a71e15c0a56b87;6paths,+22/-10.
Config: one generated2dde376 commit;1path,+3/-3.

Reviewer independently verified clean HEAD/tree/merge-base, complete histories,
rebased graph reconstruction, spec-only final delta and B binarypatch equality.
Old feature patch SHA256f395ede1278c8852f16723da2a3eac7219ac0e90403018fc2b911a758ac94b9a;
final spec SHA256cfebebc5735563b96b5f7f251be7bb2e03c2a9f774c89a839a8f676c689715ce
matches executed diagnostic bytes. Prior B patch SHA256
aad87c0de657f9f213045d5b2849f150fa9e357626fcc3d30043d93352e28623.

**NO MIGRATIONS** in all complete ranges, independently checked per commit.
No obsolete implementation, redundant fixup, repeated pin stream or removed
supported schema path. KB pin/helper remain separate coherent units; config
keeps one final generated update with its message/history intact. Old reviewed/
deployed a38c and preceding pins remain evidence refs, not literal ancestors
of rewritten successors. Reconstruction does not establish execution equivalence.

## Accepted source and evidence conclusions

The spec keeps HTTP200, exact rows/counts and adds status:true before interpreting
rows. Diagnostics contain role/static path/state/status/error class and field
names/count metadata, no credentials/report bodies/error-message values. Actual
CVE/update/HaveAPI owners support requested integer total_count; no optional
metadata or count-relaxation explanation was accepted.

The ordered diagnostic passed13/0/0 with exact original13 IDs/order in445.56s
(native408.2166), with A1's response outcomes. Its actual local dynamic bundle
remained9ff97/Ruby3.4.9/Bundler4.0.23/amq2.9/domain_name20261007; this does not
match original hosted9a28/Ruby3.4.12/Bundler2.6.9/amq2.10 or current packaged
inputs. The old failure's missing first response and absent request-exception
records leave its cause UNKNOWN. Reviewer accepted stopping the historical hunt
while requiring stronger diagnostics and exact-final affected execution evidence.
A current reproduced defect must be diagnosed/fixed; no flake or retrospective
green label is justified by a later pass.

KB helper uses supported unauthenticated OPTIONS versions JSON with the existing
caller/deadline/retry/timeout/curl contract. Its native-library focused valid,
14 invalid/default/error, timeout and curl cases passed. Actual KVM execution
is still required. No shared readiness framework or production service change.

Reviewer independently verified KB12-node and config64-node graphs. Only selected
API rev/hash/time/original.rev fields differ as applicable; other nodes/follows,
OS6bdf, page/assets/capture provenance are preserved. Both select exactebe0ab and
narHashsha256-U1u3adrSfTEDFPdi2UGtOrzrASLlqkA8tmbBra3RXYs=.
Config's actual modern source70bd11d remains separately pinned with API following
Services; API channel alone does not select modern1c or certify production rollout.
Unchanged modern1c/client0b retain prior review/check evidence.

Original rollout constraints remain: compatible UI/API pairs and upgraded active
six-guard draft-sync consumers before writes; avoid mixed API pools; preserve
published-only read authority during recovery. Rollback may re-expose retracted
content, does not undo corrections/retraction, and cannot recover deletion.

## Required remaining acceptance

1. Exact-final hosted affected API path/current-input evidence and native result/
   environment artifacts, including the previously failed core case.
2. Strict final KB validation atc46bc; permissive --allow-missing checks do not count.
3. Formerly failed managedKVM with the corrected helper and selected packaged API.

No blanket full/core/native/browser campaign is justified. Reuse unrelated
success only with actual source/runner/guest-input proof. After outcomes, fresh
final target/head checks remain. Review cleared the bounded acceptance gate;
it does not declare merge readiness while required checks are pending.

User authorized preparation only. No merge, deployment, preview update or session
lifecycle permission is supplied. Preview remains a38c/modern1c with data intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
