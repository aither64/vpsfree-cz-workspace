---
lifecycle: active
---

# Idle coordination workers

Implementation and independent review are complete. Final feature branches are published. Package/systemd, isolated native delivery, composed application, exact aitherdev configuration and CI checks passed. Live activation is blocked by managed session startup. No master integration is authorized.

## Phase checklist

- [x] Investigation, user-selected design and committed initial plan.
- [x] Runtime implementation, workspace policy and matching configuration pin.
- [x] Quick checks and independent whole-branch review; all findings fixed.
- [x] Full runtime package, host contract and real user-manager fixture.
- [x] Final runtime CI: run 38961125758, success at ced8e76e.
- [x] Isolated native delivery and final consumer builds.
- [ ] Live deployment and end-to-end acceptance; valid managed owner required.
- [ ] Integration; separate explicit approval required.

## Identity and ownership

This conversation created 2026-10-16-idle-coordination-worker through dev-session start --no-codex --no-attach. It has no inherited session binding, retained team roster or native lead. Lead owns design/implementation. No other session's ownership, branches, records or reservations were adopted. Stable URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-16-idle-coordination-worker/

## Final published branches

All use branch 2026-10-16-idle-coordination-worker and worktrees beneath worktrees/2026-10-16-idle-coordination-worker/.

| Repository | Base | Final head |
| --- | --- | --- |
| dev-workspace | 2483b4eba6d3388bcbed0659f089f0e6edbe11bf | ced8e76ec73fbc4809ac30af60903874590b82f6 |
| workspace | 9a74012ceed39027a5a0a0c7cc88fb3706510aaf | 65926d048fc110b5c55b6eef793d5caa71c857f1 |
| vpsfree-cz-configuration | 9105d416f1a5c7df55d6d7f49bb94aa83659b1b5 | b2c39068b062f82c7842eb02ad6eec223c185ba6 |

Runtime is one feature commit. Workspace is one policy commit and one runtime input update. Configuration is one generated confctl channel update, regenerated on upstream's unrelated vpsadminWebui pin advance. Both consumers select final runtime ced8e76e with hash sha256-y4AuZ5Qkmu2r5/eVnl3ZHLaq2RWIDzhgcSTCyAwcGdQ=. Extension remains 767dfd587e346168e1443e65ccdb67ce748f3fe3. final-pin-proof.json verifies all other lock nodes/inputs unchanged. Final deployment contract passed; comparison captures refreshed. All feature worktrees are clean. No intermediate feature revision was deployed or released.

## Review and quick verification

Independent reviewer /root/final_review, gpt-6-astra/xhigh, read-only standalone fallback from installed default review-purpose policy, catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd. No eligible retained reviewer. All four lanes at committed heads 4fd9128d / 2a03ea91 / 752edf11. No Blocking, three Important, one Advisory. All addressed: failed-command vs admission contention, host preparation error translation, schema-2 GC compatibility, complete generation-token handover. Lead also corrected pause/claim acknowledgment ordering and paused display.

Focused results after fixes: integration 32 runs/158 assertions; admission 4/13; schema-1/schema-2 GC focus 3/16; browser 13 tests; Go package metadata selection passed. Whole-branch history coherent, pin streams consolidated, no database migrations. Journal schema 2 introduced directly with schema-1 manual support and unchanged schema-1 ledger/snapshot/attempt/adapter contracts. Narrow remediations stay within reviewed boundaries and are verified directly per mandatory-change-review steps 9-10; no confirmation-only reviewer rerun.

Original report: [review-report.md](review-report.md). Dispositions and diagnosed verification failures: [review-remediation.md](review-remediation.md). Original committed ranges/diffs: [review-packet.md](review-packet.md). Final ranges: [final-heads.json](final-heads.json), PROJECT-final-series.txt, PROJECT-final.diff and remediation range-diffs.

## Longer verification

Fresh Luna/low watchers ran the runtime verification batches. Final runtime package and host-package-contract passed. Systemd fixture passed: 1 run/5 assertions after fixing its phase/event observation race. Exact runtime artifact initially built at /nix/store/3vzmicdbbvbrimsksv451x4xryi4lnqq-dev-workspace-0.2.0 was subsequently collected while unrooted; same final source rebuilt successfully with a retained result link, without source changes. Native fixture initially omitted client_version; helper correctly refused incomplete provenance. Corrected session-local fixture passed with actual native 0.163.0: two idle threads, one wakeup each, retained settings, retry deduplication across native restart, no idle provider requests. Original failure evidence preserved.

Fresh watcher delegation became unavailable after the completed batches; visible parent-monitoring fallback applies under dev-session-monitor. Remaining independent checks use bounded logs and status files, no repeated test retries without diagnosis. Workspace application/deployment-contract/instruction builds and exact configuration build passed. Aitherdev generation 2026-10-16--22-29-04 is built; no activation. No check remains running. Detailed evidence: [verification.md](verification.md). No activation command runs. CI is green; superseded run 38960251749 cancellation was attempted but refused HTTP403 by GitHub token permissions. Current successful run untouched.

## Deployment blocker and next action

Managed startup of earlier attempted 2026-10-16-idle-coordination failed twice through supported startup/retry: materialized Codex thread has no initial user request. Retained empty thread 01a14636-8439-7061-b4f7-e16f991829d4 and creation.state creating remain preserved. A separate authority send also refused an active writer; no bypass or journal edits. Tracking-only initiative has no managed conversation owner, so cannot submit approved live coordination/deployment. All independent build/native checks are complete. Restore supported managed startup before preparing system/profile activation under one vpsfree:aitherdev reservation. Do not adopt another owner's reservation.

User direction Implement the plan covers implementation and planned deployment through vpsfree-cz-configuration. It supplies no default-branch integration approval. Keep initiative active, refs and worktrees retained. No archive, delete or stop authorized.

## Documentation and recovery

Runtime docs/integration.md owns background CLI, state/notification behavior and schema upgrade constraints; docs/coordination.md and coordination-operations.md own scheduling and recovery. Workspace docs/coordination.md and routed Git/verification guidance direct agents to end turns after background submission. Configuration docs/operations/workspace-coordination-aitherdev.md was checked and remains applicable. [design.md](design.md) and [plan.md](plan.md) preserve rationale. [rollout.md](rollout.md) records this rollout separately.

Background completion keeps lifecycle active for lead review. Pause/lifecycle fencing stop future admissions; existing claims retain ordinary uncertain-effect recovery. First journal-2 upgrade requires pending manual journal-1 integrations to settle. Retained journal-2 records prevent a downgrade to journal-1 packages even after completion. System activation precedes user-profile selection, both under the same reservation; application stays in its user profile.

Shared workspace master advanced after review with another session's committed tracking records. This checkpoint preserves them and all unrelated index/files. The workspace feature remains at its verified published head; a later explicitly approved integration must refresh/rebase against then-current master and apply the existing certified-equivalence/review rules. This handoff does not claim immediate fast-forward readiness.
