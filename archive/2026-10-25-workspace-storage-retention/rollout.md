# Storage retention rollout

Executed on2026-10-25. User authorized tracking, aitherdev feature deployment,
completed recovery-only compaction, unused coordinator expiration and ordinary
Nix GC. Default-branch integration was not authorized.

## Revisions and gates

- Runtime:ec53874b6eea73bf65099cf19aa1a4bc5a3336aa.
- Workspace:564979a0a7475b68747136c848144c1aeb2328ba.
- Configuration:2d33a9ca715d305d7b4003e17bbf3e31f1be1d60.

Independent four-lane review and focused follow-up passed after remediation.
Exact runtime CI40181077743 passed fast, archive/revival and creation jobs.
Composed package, focused maintenance regressions and all5 final workspace Nix
checks passed. Historical deletion was reduced to settled archives; the complete
Nix derivation/input identity remained unchanged (archive-narrowing-build-identity.json).

## Deployment

Machine claim11ac5465-9fbe-42c0-839c-f4cce6c63ac0 was acquired and verified held.
Scoped system build/copy, generation-bound dry activation and no-reboot switch
passed. Configured auto-rollback was preserved. Running system and profile both
select/nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e.
Candidate forward workspace selection passed and selects
/nix/store/xjsni6q4ldh2anc8l1vn6zxjf64m4ska-dev-workspace-0.2.0.
Codex stays0.163.0. Portal health passed; ordinary Codex process/start time and
socket inode are unchanged. Live isolated naming returned workspace-archive-retention
without creating a development session. Final health passed after cleanup.

## Cleanup

Recovery-only preview and apply used the selected policy3 package, transition
exclusion and the authority directory verified against installed registration.
Two completed archives shrank from137306112 to65536 allocated bytes. Unfinished
or nonterminal tracking was skipped. This is the first applied inventory3 state
for this initiative's rollout; future compatibility must retain that boundary.

Coordinator --expire-unused preview completed with retry:false; apply removed
26 worktrees,60 dedicated roots and5 obsolete profile generations, all91 actions,
with retry:false. Process state changed naturally between preview/apply, admitting
one additional no-longer-held checkout. Existing live/recovery guards remained.

Retired5 owned environment/build root links and the completed naming-check binary.
Ordinary Nix GC ran over verified root SSH under /run/lock/nix-store-cleanup.lock;
104 store paths removed,12.3GiB reported freed. No store paths were removed manually.

Available space increased40.08GiB to128.72GiB between before-cleanup.json and
after-cleanup.json. Coordinator source allocation fell28.20GiB; private recovery
fell130.88MiB. Concurrent host activity can make free-space change differ from
individual tool counters. Shared historical archives were not modified.

## Remaining boundary

All feature refs remain unmerged. Configuration upstream advanced to95f10b50 with
automated dependency updates; refresh that feature branch and recheck compatibility
before approved integration. Preserve the intended native Codex/runtime contract.
Historical deletion retains all pending archives and all summaries; rerun safety
preflight at integration time. Claim remains held until verified effects AND
integrated deployed feature lineage satisfy installed policy. No session archive,
delete, reboot or default-branch integration was performed.


## Approved integration and machine release

The user subsequently authorized "ok, merge and release aitherdev". Runtime
ec53874b was fast-forwarded into remote master. Workspace was cleanly rebased
onto concurrent tracking-only mastercb89659d; final heade9144243 was integrated
under the short repository claim and shared tracking/session locks. The15 settled
archive preflight still had zero unfinished-operation overlap;209 unrelated dirty
tracked contents were fingerprinted and preserved. Complete application derivation
and inputs remain identical to the verified deployment.

Configuration was cleanly rebased onto95f10b50 (automated dependency updates).
Final headaca63e8a was independently reviewed in the affected general/risk lanes
and integrated after the refreshed scoped system build passed. Only devWorkspace
changes relative to that target, retaining exactec53874b; its two owned commits
have identical patches and independently reconstructed final tree. Refreshed
upstream includes system-native0.164.0; that whole-system baseline was not activated.
The previously verified system/application with0.163.0 remains installed.

The deployed configuration2d33a9ca is not literally an ancestor ofaca63e8a.
Review and reconstruction prove integrated deployed FEATURE lineage, as permitted
by the installed retention policy. No migration or persistent-format boundary
changed during rebases; schema3 remains supported and consumed.

All exact final feature heads have fresh remote-master ancestry proof in
integrated-feature-proof.json; feature refs remain published. Repository claims
were released promptly after each remote proof. Fresh pre-release health checks
prove the selected system/profile and unchanged ordinary conversation server.
All prior deployment and cleanup commands have known successful effects.
The exact owned machine claim was normally released and reread as released:
released-aitherdev.json. Temporary merge targets were removed; registered feature
worktrees remain. No session archive/delete or reboot was performed.

Final verification completed: refreshed scoped system build and all5 workspace
checks passed; runtime master CI40193848598 passed all jobs, including activation,
renewal, rollback and user-service boot. No operation remains running. All3 exact
feature heads are integrated and all4 resource claims are authoritatively released.
The initiative is complete and remains open for follow-up conversation.
