---
lifecycle: active
---

# Portal performance implementation

## Status

Phase: integration and deployment preparation. Source and pins published;
focused Go/browser and semantic-lock checks pass. No deployment yet.
No retained roster; lead owns design and code.
Created managed session 2026-10-15-portal-performance-fix in
/home/aither/workspace/ai/vpsfree.cz with lead 01a14155-d18d-7512-85a3-c3105dd6fa7d.
Bootstrap conversation explicitly waits while the initiating conversation works.
Explicit literal environment identity matches dev-session current.

- [x] Diagnosis and approved plan.
- [x] Create managed implementation initiative and technical brief.
- [x] Implement, document and quick-check source changes.
- [x] Publish and independently review complete committed branches.
- [ ] Longer checks and exact configuration/application builds (application passes).
- [ ] Merge all four final heads to remote master.
- [ ] Deploy system then profile and verify acceptance.
- [ ] Prove integration and release aitherdev reservation.

## Repositories and next actions

codex-web, dev-workspace, workspace and vpsfree-cz-configuration.
Feature branches/worktrees use the initiative slug; shared root stays master.
Final branch inventory: final-heads.json. Review packet: review-packet.md.
Next: preserve the preceding rollout baseline, complete remaining master merges,
prepare aitherdev system/profile, deploy, live-verify and release.

## Authorization and documentation

plan.md records the user's explicit merge, deployment and release direction.
design.md owns implementation/verification details.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-15-portal-performance-fix/

## Commands, risks and cleanup

Initial start without --goal-file refused before creating a session. An explicit
waiting bootstrap goal created a valid managed lead. The prior threadless
investigation is not reused. No machine reservation acquired yet.
Preserve unrelated shared index/files. Ownership caching must fail closed on
identity changes; history backfills must not block watches or fabricate counts.

## Implementation checkpoint

Source work in the two registered worktrees: shared file cache/recovery-owner
index, isolated two-connection history pool, resumable count projections and
finalized-prefix aggregation, lineage append cache and explicit stale/backoff.
Focused catalog, activity, attention, history and command compilation checks
passed against a temporary local Go module replacement. The source and dependency pins are now committed and published; full review,
long checks and rollout remain. The original local-module check was superseded
by successful checks using the final published module.

Tests using the operator host need DEV_WORKSPACES_CODEX_PROVIDERS pointed at
an absent temporary path: the real /etc catalog otherwise makes unconfigured
fixture servers fail provider identity validation. No production configuration
was changed. Large regression tests are reserved for post-review verification.

The reusable client adds optional history-reader injection; existing consumers
keep their existing transport when absent. The actual portal explicitly shares
the isolated pool between both clients. This preserves public compatibility
while enabling the fix in every deployed portal path.

Final review inputs and final heads are recorded in review-packet.md and
final-heads.json. Catalog duplicate recovery ownership invalidates immediately
on atomic publication. Rebased over current naming runtime/master; original
Codex patch range-diff equivalent before protocol corpus coverage correction.
No migrations. One final pin per dependency stream.

Aitherdev currently has a foreign held reservation owned by
2026-10-15-aitherdev-disk-retention; prepare independently and queue without
bypassing it. No reservation acquired by this initiative yet.

Independent reviewer /root/final_review uses catalog fallback gpt-6-astra/xhigh
(no retained roster), all four lanes, high risk. Provider final CI
38810176011 passes. Runtime CI 38810388440 still running at 862c9dcf.

Review complete: review.md has no Blocking, three Important and one Advisory.
All addressed within the reviewed design; direct focused verification passes.
See review-remediation.md. Provider remediated head 523865195522ad6f4804613e6f54823ddf447924.
Final downstream pin refresh and longer verification now follow.

All review fixes are committed and downstream pins republished; final-heads.json
has current complete ranges. Quick checks pass against actual module 5238651;
matching locks pass at runtime 12291233. Original reviewed refs are retained.
Long verification batch: verify-remediated.sh (composed package, provider race
checks, focused real Chromium/Firefox presentation/team/history browser paths).

Long-check monitoring fallback used because native collaboration tools were
unavailable at launch. Composed package and provider race checks running under
parent-owned handle. Playwright dependency prepared, but extraction script
expected an older wrapper form; it stopped before browser tests. Inspected the
actual immutable wrapper and launched only the browser check with its exact
NODE_PATH/browser paths (browser-remediated.log). No source change.

Real Chromium/Firefox presentation, team activity and paged-history fixtures
pass on remediated runtime 12291233 (browser-remediated.log/status). Provider
focused race checks pass. Composed package still runs session regressions.

Composed application package passed. Runtime final CI 38812023592 passed.
Selected native schema validates the full corpus and item anchors. A read-only
new-reader probe of the real large conversation is backfilling correctly so far
(native-history-probe.jsonl), with subsecond per-observation progress.

Provider final pre-merge audit: c9aa6dc2..52386519, one coherent commit;
remediation changes match review.md I1/I2/A1 and added focused verification,
no migrations, no superseded pin stream. Full CI/race checks pass; comparison
captured. Integrating this dependency first does not change the preceding
rollout's pinned c9aa6dc2 source or reservation. Other merges await its final
baseline so they preserve the deployed retention changes.

## Integration e26cca5e-a674-4e0f-b212-476ae0f030cb

Requested exact feature heads are integrated. See integration/e26cca5e-a674-4e0f-b212-476ae0f030cb/summary.md
and integration/e26cca5e-a674-4e0f-b212-476ae0f030cb/result.json for operation receipts. Feature refs and session retained.

Provider merged by native coordinator: master/remote exact
523865195522ad6f4804613e6f54823ddf447924, job
f3917dca-7ee5-498c-b8c7-6b5044e3b032 applied/verified. Integration run
e26cca5e-a674-4e0f-b212-476ae0f030cb completed and native deliveries settled.
Other three feature branches remain unmerged. The machine is still reserved
by the preceding retention initiative.

Read-only real native history probe completed successfully: 162 observations,
14,198 tool calls, 2,349 sent + 1,244 received messages, countsComplete=true.
Per-observation p95 0.467 s, max 0.906 s; no RPC/transport failure. This was
the existing large conversation, without resuming/sending/subscribing. Detailed
evidence: native-history-probe-result.json and .jsonl. Initial unobserved timing
is correctly unclassified. The application has not been deployed yet.

The successful composed build output was unrooted (--no-link) and was
collected during the preceding owner's authorized host GC before a later
path-info query. Build/test evidence remains valid for exact derivation
nnbbvgcdbbjpy6x5968v99bpjqzzgzwz. Deployment preparation must realize and root
its final artifact; do not claim the earlier output is retained. Retain a
profile/output root for the next build.

Aitherdev preceding owner released (ledger924). Runtime patches rebased
cleanly/identically onto integrated retention 2370232f, new head2b22de8d.
Config/workspace pins regenerated once atop integrated retention policy;
final-heads.json updated. Focused checks, hooks and deployment-lock contract
pass. The original native collaboration reviewer cannot be addressed through
current tools; a fresh read-only standalone Astra/xhigh CLI reviewer is running
general/risk affected lanes on the final composition. Catalog/roster rechecked
(no roster; same saved default review role). No source design change.

Final composition review accepted with no remaining findings in general/risk
lanes; prior architecture/scope remains applicable. Native reviewer thread
01a14196-4c7c-7552-9a2e-91cdbc1d068d verified gpt-6-astra/xhigh/read-only in
composition-review-identity.json; report composition-review.md. Exact current
branch histories/pins and no-migration conclusion confirmed. Final package/CI
verification launched from clean current heads with a retained output root.

Final pre-merge check: all exact heads/series/diffs still match final independent
composition review; no superseded pin commits or migrations. Comparison captures
complete for remaining three repositories (one transient session lock was retried).
Final composed package and CI pass; final-verification.json freezes evidence.
Proceed with integrate-first native driver; do not edit its sealed review or
verification evidence. No completion section: retain reservation for acceptance.

Native final integration preparation stopped before submitting jobs because
shared workspace master contained unpublished ordinary archive-only commit
1a5e443d (145 paths, exclusively work/archive of that completed initiative).
Published that existing linear tracking commit unchanged over SSH; no foreign
records or index edited. Current workspace feature now needs certified refresh
over that tracking-only baseline. Resuming the same native run first.

Ordinary retry confirms cached workspace expectedHead prevents reaching its
installed certified refresh after the archive-only baseline advance. Prepared
recovery is a one-run operator loader, not an installed product change. It calls
only the existing native refresh/proof/publication, updates that derived cache,
and stops before submission for comparison capture. Ownership/generation, all
requests/reviews/approvals/snapshots and native execution guards remain intact.
The exact completed procedure and loader will receive final independent review
before execution. Ruby syntax passes; no recovery mutation executed yet.
