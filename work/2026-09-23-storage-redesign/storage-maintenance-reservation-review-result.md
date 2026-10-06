# Complete Admin branch: independent final review

Review completed on 2026-10-06 by retained reviewer0, ready/review/read_only,
gpt-6.1-sol/xhigh, thread `01a0d230-7536-7ee0-b212-90b3f6847ec0`.
The reviewer verified the session identity and roster23, read the canonical
skill and all four references, and inspected source directly without
authorship, delegation, tests, private artifacts or runtime operations.

## Scope and evidence

All four lanes were classified HIGH: general; architecture/repetition;
scope/proportionality; risk/compatibility. The primary complete range was
`c4d9b50f4e74417ed37b5fe410cca3ec1addc24e..edc26498f4875340de6a2484b230fb6e8865d492`,
tree `a09dd851695e7139aeb431b2bd2dfef15579d7e3`: 24 commits, 214 paths,
25,317 additions and 455 deletions. Full binary/index diff SHA256:
`e7b4b84f2c45c99b2ddc925acd910a6e25a33695cca1068015f3bdc936887b4e`.
The reviewer inspected the complete series, messages, final diff and actual
API/Node/journal/capture/planner/RPC/Plan/scheduler, WebUI, Nix, CI and docs
consumers. Earlier reviews supplied context and did not replace this inspection.

The final direct-remediation head is
`425d399afb3876bde4f3f4023f3810a45bee6f3f`, tree
`c0babd3297b9c0bbab2eb35b322ca902ca675bdd`: 24 commits, 214 paths,
25,320 additions and 455 deletions. The reviewer independently matched its
complete diff SHA256
`ab5ea0b9b10dc698520e7af29a07bc7434b6e662a13c5f7ed51a5078b1740114`.
Primary review provenance remains edc plus the explicit step9 disposition.

## Findings and lead decisions

1. **Important, general, resolved:** the original endpoint manifest omitted
   three advertised maintenance actions. The requested correction added only
   those three covered scopes. Reviewer inspected the exact one-file edc..425d
   delta, unchanged owner message/parent and manifest SHA256
   `ec79801a5962be80a21063c4ab32ad08a4d44347cbe098472d941a3f2b233ceb`.
   Lead verified the existing full-plugin endpoint gate: one example, zero
   failures, pending or outside errors; wrapper exit0/54.508s/parity1 and
   cleanup1. Normal owning amend passed0/72.166s with hooks enabled. No new
   runtime/design/interface was introduced. Skill step9 applies; no lane rerun.

2. **Advisory, architecture/general, accepted for follow-up:** retained offline
   `api/lib/vpsadmin/storage_reconciler/comparator.rb` repeatedly scans SIPB,
   selected-DIP and filesystem collections. At lines111–120, 20k backup SIPs
   against 20k SIPBs imply roughly400m iterations. Lines552–553/587–589 rebuild
   selected DIPs per SIP; lines386–387 scan filesystem identities per expected
   filesystem. This is source-derived cost, without a measured failure or
   executable authority. Lead defers a representative measured cohort and
   one-time indexes that preserve duplicate arrays to a separate comparator
   unit. It does not block this reservation unit or add a physical trial gate.

No remaining Blocking or Important finding was found after direct remediation.

## Distinct lane conclusions

- **General:** singleton/current-row serialization binds acquisition, UUID
  replay, lookup and abandonment. Run and pointer commit or roll back together;
  both actors remain audited and frozen mode/epoch remain unchanged. Exact
  stale/malformed/unknown bindings refuse. Tests include separate connections,
  races, rollback/savepoints, disconnected creator and unstable status.
- **Architecture:** StorageMutationAdmission and the retained run model own
  reservation; HaveAPI exposes bounded summaries. The Pool array has a concrete
  scalar-resource framework limitation and is revalidated under catalog locks.
  There is no second ownership/reconciliation engine. The comparator Advisory
  remains as recorded above.
- **Scope:** the new runtime/schema/API/spec/doc unit is one API-only owner.
  It adds no physical dispatch, exclusion, approval, G2 action, TTL, cancel or
  alias repair. Observer and constructor-only strict paths retain their limits.
- **Risk:** current direct active administrator, nondelegated session and action
  authorization constrain mutation. UUID/epoch/revision/digest CAS and copied
  actor audit constrain replay/abandonment. Unknown handoff contracts refuse;
  read_write and upgraded staging refuse any owner pointer. Status is DB-only
  and nonrepair; requested raw catalog paths are not public summary output.

## Whole history and migration conclusion

Reviewer independently range-diffed consumed148ef..290f against c4d..5dd:
21 equivalent commits and two documented upstream-context unions. All24
ordered commits are coherent. The omission fix is folded into its unpublished
reservation owner. No fixup, obsolete sudo freeze launcher, transitional OS
actor migration, duplicate input stream or unsupported shim remains. Retained
follow-ups were published/externally consumed and must not be rewritten just
to shorten the series. Legacy capture reading supports real sealed evidence.

There are **three migrations**, not a no-migration clearance:

| Migration | Exact blob | Provenance |
| --- | --- | --- |
| 20260924210000 foundation | `7d929052f314d5a821b2ce65345680c0740b1b0c` | Feature-published and externally consumed at Admin290f; preserved |
| 20260926100000 capture indexes | `d60868e615024c70fb4b87b736a2466ceb8349db` | Published/external consumption preserved |
| 20261006120000 reservation | `f3bbc80fa31967566536f57dc4e70815ebadea01` | New additive step; disposable generation/spec use only at review |

Reviewer matched these blobs and predecessor schema
`e9aa952df7b94451c5491c965d22962265c8f545`. The180-table final schema matches
the retained run and nullable unique restrictive pointer. It converts no
existing control/audit data and infers no ownership. Down refuses any used run
or pointer before DDL. No stale-schema existence guards or transitional
migration remain; existing exact fresh-schema singleton bootstrap is retained.

## Compatibility and remaining acceptance

Intentional persisted/API contract1 is API-only: reserved/revision1 to
abandoned/revision2, immutable bounded catalog scope/digest, copied actors and
singleton pointer. It is not physical dependency proof or handoff authority.
Deploy migration first, converge compatible API/Supervisor/task/admin readers
and exclude old unfreeze writers before relying on ownership. Old setters
ignore the pointer. Active-reservation rollback is unsupported; retain audit
schema once used and compatible readers. Current retained Admin290f and its
provider composition do not load the new owner. OS input8d05 is unchanged in
the reservation branch; OS source replay is a separate unit.

All numeric passes, hook and cleanup evidence are supplied lead/watcher results.
Reviewer ran no tests/builds/Nix/network/private/runtime operations. There is
no new reservation VM rollout, writer-convergence, package/delivery or physical
acceptance. Global ResourceLock/correlated capture cost remains unmeasured;
timeouts fail incomplete. Original broker/API500/runner-loss and live-transfer
crash causes remain unresolved. Alias disposition, NAS history, preferred-root
availability, payload/history/scheduling/repeat/retirement and physical exclusion
remain held. Strict production dispatch, identity/scopes, node_quiet,
repair_ready and APPLY remain off. This report authorizes no default merge,
deployment, retry, cleanup, cancel, unlock, retirement or physical repair.

[Original packet](storage-maintenance-reservation-review.md),
[final source inventory](storage-maintenance-reservation-final-inventory.json),
[state and current next action](state.md).
