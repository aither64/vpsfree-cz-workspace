# Requested actor-state review disposition, 2026-10-07

## Scope and conclusion

The primary independent review remains the complete HIGH, all-four-lane
`c4d9b50f4e74417ed37b5fe410cca3ec1addc24e..543a7979a1f17c68fe2c33eaccecf1bf864de3ba`
review by retained `reviewer0` (`gpt-6.1-sol`, saved `xhigh`, read_only).
The original report and inventory are preserved. Its requested-state Important
is **resolved** at `32d7f0ac01e6a409b6bdcc05df8cdc33b4cefd50` by lead inspection
and focused checks under mandatory-change-review step 9. There is no remaining
Blocking or Important finding. No independent review rerun is claimed.

The exact five-path remediation is
[remediation.diff](storage-maintenance-handoff-current-actor-remediation.diff),
SHA256 `03840a894592353ca256310345ec2cd41468a10dd9bd62990bd8cb711a3b371f`.
The final [inventory](storage-maintenance-handoff-current-actor-final-inventory.json)
contains 27 commits, 222 paths, 27300 additions and 461 deletions. The amended
owning unit has 19 paths, 1543 additions and 97 deletions. Its parent remains
published `6cd9f9a62cfe470d18694116cc60efc9555dc876`; the original unpublished
543 head is retained under a backup ref.

## Finding and verified remedy

The ordinary latest ObjectState query could miss a separately committed pending
suspension or soft deletion inside an older outer REPEATABLE READ view, while
confirmed User state remained active. The canonical lifetime reader now offers
Boolean `lock: false`, retaining its default query, exact class/row filter and
`created_at DESC, id DESC` ordering. Storage admission requests the current
locking read beneath its existing singleton, User and UserSession locks. A
missing requested-state row remains distinct from a present invalid/nil state;
only an explicitly active request is eligible. Ordinary authentication policy
and lifecycle writer locking remain unchanged.

Parent inspection verifies the bounded change, exact source freeze and protected
worker/cleanup preservation. All ten real older-RR/concurrent-request cases pass
for suspended and soft_delete across freeze, unfreeze, catch-up, reserve and
handoff. They demonstrate the old ordinary view, then current refusal without
control/run/audit changes. The 15 reader/ordering/strict-state cases also pass.
This meets the review's requested correction without changing schema, stored
contract, public wire format or lock order. Step 10 reruns are not triggered.

## Evidence

Fresh owning checks passed: wrapper 0/513.868s, driver 505.897s, waited1,
source parity1 and cleanup1. Four API/model files ran 127 examples, zero
failures/pending/outside errors (native465.596s, seed40690). Component and root
lint each checked the three changed Ruby paths with zero offenses. The existing
migration8, endpoint1, selector20/89 and generated-schema/locale evidence carry
only through exact unchanged bytes; those checks were not rerun.

The normal unpublished amend passed 0/63.289s; actual child 0/49.774s,
driver56.370s, cleanup1, waited1 and parity1. Every declared precommit and
commit-message hook passed, with no hook warning. A nonfatal Nix dirty-tree
warning is recorded separately. Final tracked/index state is clean. Parent
verified all3248 source hashes, outside-five3243 byte/stat entries, foreign PHP
cache preservation and original disposable DB/commit child PID absence. No
signals or pruning occurred. Complete results are linked in
[check-result.json](storage-maintenance-handoff-current-actor-check-result.json).

All four additive migration blobs and core schema remain exactly the primary
reviewed versions. At primary review, the new handoff migration had disposable generation/spec
use only; the later feature publication is recorded below. No live/master/
external schema consumption is inferred. The original history/no-obsolete/migration conclusions remain valid
with this explicit five-path disposition. The retained comparator CPU Advisory
is accepted as a separate offline liveness limit; measurement/indexing is future
work, and supplies no physical gate or repair authority.

## Delivery and limits

Feature publication passed0/14.241s with exact6cd->32d readback and saved
comparison; masterc4d is unchanged. CI metadata remains unawaited. The new
handoff migration is now feature-published, with no live/master/external schema
consumption. See [publication-result.json](storage-maintenance-handoff-current-actor-publication-result.json).
Current locking reader and
admission caller must reach every API worker together before relying on the
check; older workers/rollback retain the eligibility gap. The retained cluster
remains stopped. Contract2 invocation still requires separately supported
termination/recovery and physical contracts. No default merge, package/live
activation, containment/reap, alias/NAS history, destination availability,
scheduler release, G2 or APPLY authority follows. Broad flake validation retains
its reproduced baseline overlay failure.
