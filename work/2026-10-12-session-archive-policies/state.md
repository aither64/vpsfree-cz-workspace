---
lifecycle: active
---

# Session archive policies

Phase: implementation, review, verification, deployment and requested archive
finished; ready, awaiting merge approval. No default-branch integration is
authorized. This implementation initiative remains open.

- [x] Explicit archival preserves local work privately and removes owned worktrees.
- [x] Automatic archival retains merged-work requirements and exact target proofs.
- [x] Artifact-caption parsing and validated registration prevent the reported failure.
- [x] Publish consolidated branches and complete independent final review.
- [x] Pass packaged/browser/host checks and exact final CI.
- [x] Deploy aitherdev host and application; verify live operation.
- [x] Archive the selected original session and verify recovery/retirement.
- [x] Curate evidence and finish handoff.
- [ ] Integrate feature branches only after explicit repository/target direction.

## Identity and final branches

Initiative 2026-10-12-session-archive-policies was created separately with
no Codex root/roster. Its complete original environment identity and current
identity were verified. Ordinary lead owns implementation; fresh catalog
utilities monitored only their assigned operations.

All three branches are named 2026-10-12-session-archive-policies. Their clean
worktrees are beneath worktrees/2026-10-12-session-archive-policies/.

| Project | Reviewed base | Final published head |
| --- | --- | --- |
| dev-workspace | 60c679c52c263a0fc7a4b08c5f83a291cfd89191 | 1a27453c0b67c8c24cbe1474d5a05607eb698a9a |
| workspace | shared master e76c0c146a47fc9ce10d4a811610b5a9f6a02bda | d1e5888a9f96e32833d56f5ae18da477df44472b |
| vpsfree-cz-configuration | b17dbea2cb1b9bf93714c929da776a4d4a6618f8 | 1697613eab00a4bb0642b79c355c0b673b758a41 |

History: three logical runtime commits, three owned workspace commits, and one
consolidated configuration pin. Inherited coordination commits are preserved.
Workspace rebase was patch-equivalent. Shared master advanced afterward through
tracking/archive commits, including the actual requested archive; before a later
approved integration, rebase/check against its then-current target under the Git
procedure. No database migrations or obsolete feature iterations remain.

Both consumers select runtime 1a27453c with
sha256-z8n/lDZiB5pwmzZPdCCUiN4ATDAXZHgvmBplIzUvRLo=.
Extension 7157c8098dcf60127aa4df823fab82b4185ad22a, sibling inputs,
codex-web and native Codex 0.160.0 are unchanged. Deployment contract and final
comparison captures passed. Configuration hooks were active and passed.

## Review and verification

Independent reviewer /root/archive_policy_review: gpt-6-astra/xhigh/read_only,
installed default review role fallback because this initiative has no retained
roster. Catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
All required lanes completed; accepted findings were corrected. Final shutdown
context correction passed affected General/Architecture/Risk review with no
findings; unaffected conclusions remain valid. Whole-branch history and repeated
pin streams were assessed explicitly; no migrations.

Focused Ruby/Go recovery, queue, ownership, artifact and real CLI regressions
passed. Final packaged application: 418 Ruby runs/5696 assertions, zero
failures/errors, 13 skips; schema 12/50; provider 127/994, 3 skips; all Go packages
passed. Final application and aitherdev builds passed. Exact CI 38297311907
succeeded. Earlier unchanged VM scenarios and Chromium/Firefox archive (12.78s)
and lifecycle (18.43s) regressions passed. Correction affected only selected CLI
context and regression coverage; no redundant browser/VM rerun was needed.

## Verified deployment and requested archive

[Rollout](rollout.md) records both actual deployments and the first failed archive
attempt. Final system: /nix/store/apsqp7fvi89kjc0fxp7gijq03sr4jm3n-nixos-system-aitherdev-26.05.20261010.6fcc160.
Final user-profile application: /nix/store/yb4mamskfrlzaz71ncp3363bhl4jc6hg-dev-workspace-0.2.0.
Confctl health checks and all five user units passed. Native/tmux PID and socket
continuity were verified against live-before-corrected-deployment.json. Native
restarted before each deployment baseline, during the pause and at 21:18; cause
is not established. Earlier evidence is retained, without a claim of continuity
across those intervening restarts. Temporary application GC root removed after
profile retention was confirmed.

The selected 2026-10-11-diagnose-vpsadmin-api-exception archive completed normally
(exit 0), tracking commit 8df4f006. [Recovery proof](requested-archive-result.json):
schema 3, neutral archived lifecycle, ten complete verified private snapshots,
all checkout paths and Git registrations absent, heads and branches retained,
no pending journals. Parent verified archived portal GET 200/read-only, absent
tmux session and absent runtime authority. No revival or archive of this initiative.

Network-ipv4-left-counter: three freehand artifact caption keys used name instead
of label. This failure predates deployment. Only those three keys were repaired;
unrelated edits were preserved and never staged. Its live page returns 200.
Matching Ruby/Go alias reads plus validated atomic artifact registration and
installed agent instructions prevent this failure mode.

Storage-redesign warning is separate: read-only inspection found eight historical
idle loaded native utility descendants outside its roster triggering the existing
loaded_conversation_residue check. It predates deployment and remains untouched.
No claim that this separate recovery warning is resolved.

## Documentation, evidence and next action

[Plan](plan.md), [design](design.md), [review packet](review-packet.md),
[rollout](rollout.md), [verification history](verification-history.md),
[live deployment proof](live-after.json), [archive proof](requested-archive-result.json).
Runtime docs/dev-sessions.md, session-archive-recovery.md and workspace-portal.md
own behavior and compatibility. Installed documentation skill and workspace
sessions/lifecycle procedures guide artifact registration and archival. Existing
README links reach the contracts; reusable failure lessons are in
notes/dev-workspace/2026-10-12-artifact-captions-and-readonly-notices.md.
Full transient logs are retained locally and excluded from the curated checkpoint.

No implementation, review, verification or rollout work remains. Next operator
action is explicit integration direction for the named repository/target set;
then apply current-target rebase, final history checks and fast-forward-only
integration. Keep this initiative active until every registered final head is
merged and no work remains. Retain feature branches.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-session-archive-policies/
