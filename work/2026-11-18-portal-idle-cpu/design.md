# Portal idle CPU fix proposal

Owner: this session's lead (live roster absent). Implementation owner:
`2026-11-11-pi-codex-migration`, using its own design/implementation workflow.
This is a proposal and handoff, not an implemented or tested fix.

## Evidence and source

User-supplied measurements, not repeated here, on installed source
`/nix/store/l8dansm9p6vz9n61f86s60ywmk7cf7zc-source`:

- `workspace-portal@vpsfree-cz`: main process 310% lifetime CPU over about 2.5 h;
  265–345% in ten 1 s samples.
- Two user-mode perf samples (22 s / 30 s): `startMonitorOperations` 32.5–35.3%,
  GC marking 30.4–32.1%, `startCommunication` 5.8–6.4%, maintenance admission
  5.8–7.5% (overlaps callers); about 50% had `encoding/json` on stack.
- Aggregate opens over 10 s: 2,780 operation JSON, 1,082 observer, five
  communication state opens. Opens include all readers; CPU samples are portal-only.
- All 277 operations terminated and deliveries settled; all 99 CI observers had
  accepted terminal events, while 91 still had phase `observing`. All 463 messages
  delivered in a 6.25 MiB communication `state.json`. There were 1,072
  “CI poll owner changed” occurrences in five minutes.

Bounded source inspection confirms repeated full `Store.List`/`ListObservers`
work in delivery selection and observation; `ClaimCIPoll` resolves ownership and
admission before checking existing events. Relevant files (relative to source):
`portal/internal/web/{monitor,communication}.go`,
`portal/internal/monitoroperation/{store,observer_store,observer_service,delivery}.go`,
`portal/internal/communication/{store,service}.go` and nearby existing tests.

## Proposed changes and invariants

1. Derive a disposable in-memory compact work view from fully validated disk
   records. Retain identity/fingerprints and eligibility or pending references,
   not deep JSON clones of settled history. Reuse one immutable selection snapshot
   across monitor delivery, utility observation and CI selection within a tick;
   reuse unchanged validated entries across ticks. Preserve cursors, fairness,
   independent delivery budgets, cancellation and current item/batch limits.
2. Discover names and file metadata each tick; invalidate on create/delete,
   atomic replacement and in-place changes. Include file identity/type, size,
   nanosecond mtime and ctime (and metadata relevant to validation); directory
   mtime or size alone is insufficient. Same-size writes and restored mtime must
   be covered. Validate a changed file with stable before/after identity checks;
   retry or fail closed on concurrent/invalid reads, never serve old eligibility
   as a successful refresh. Revalidate operation/observer pairing when either
   member changes or appears/disappears. Preserve all legacy/Pi parsing and
   validation rules. Cold start/restart performs full discovery. Metadata scanning
   may remain O(history count); warm idle body decoding/allocation must not.
3. Utility observation excludes `terminatedAt` records independently of event
   delivery. CI new-poll selection excludes any record with an event, even if
   phase remains `observing`, before owner lookup/admission or helper work.
   Repeat the cheap event guard on a fresh validated record in `ClaimCIPoll`
   before those expensive steps, and retain locked revalidation before polling.
   Keep undelivered terminal events and outstanding poll/native receipt
   reconciliation in separate actionable sets; event presence only stops new polls.
4. Treat the snapshot as scheduling advice. Preserve fresh authoritative reads
   and existing lock order before mutation, poll start, dispatch, revocation and
   receipt reconciliation. Stale candidates may be rejected safely. Invalid
   changed state must preserve current fail-closed behavior, not disappear from
   work as if settled. Do not let an empty cached selection mask a change.
5. Reuse `communication.Pending` selection when the validated file is unchanged,
   with the same invalidation rules. Retry `pending`/`held`/`submitting` each
   eligible pass even without a disk change: admission/recipient activity can
   change independently. Preserve revocation, saved submission envelopes and
   uncertain-receipt reconciliation; dispatch still rereads under existing locks.

No persistent index/queue, schema migration, broad profiler or new CI lane.
Optimize maintenance validation only if a post-monitor-fix profile still warrants
it. Final helper/type names and adaptation to the migration branch belong to its
lead; these eligibility and authority invariants are the acceptance contract.

## Bounded acceptance and performance checks

Use the existing Nix-backed Go lane (`-mod=readonly` in source checkouts). Add
one deterministic quick regression group through the real worker-pass entry
point used by the ticker; extract a small pass function if needed, without
building a parallel test-only algorithm. Inject clock/counters/fake transport;
use temporary local synthetic fixtures, no live history, network or 2 s sleeps.

- Cold pass validates a settled history, then reset counters and repeat idle
  passes. Require zero full history body reads/decodes, owner lookups/admission,
  utility/native/CI helper calls for terminal-only settled records. Count the
  actual I/O/decoder and action boundaries, not just the cache selector. Include
  settled communication history and CI phase `observing` with terminal events.
- Change one record externally between passes: next tick discovers it and does
  useful work without decoding unrelated history. Cover atomic replacement,
  same-size in-place write (also restored mtime), create/delete, paired observer
  change, restart, and malformed change preserving failure behavior.
- Separate terminal-but-pending delivery and outstanding receipt cases prove
  delivery/reconciliation still run, including unchanged held/submitting state.
  Change owner/admission or revoke between selection and action to prove fresh
  revalidation prevents stale authorization. Existing compatibility tests cover
  legacy/Pi records; extend only gaps touched by this change.

Use operation counts for the regression gate, not timing thresholds. Add a small
and larger fixture benchmark through the same pass (for example 16/8/16 versus
300/100/500 operations/observers/messages). Warm-build once, then run the narrow
benchmark with `-benchmem -benchtime=100ms -count=1` once before and once after;
report ns/op, B/op and allocs/op plus fixture sizes and revisions. Keep the warm
comparison to seconds; stop optional expansion if it grows beyond a few minutes.
No bespoke benchmark framework. One short live sample is optional after the
migration session's normal authorized rollout, not a prerequisite for this handoff.

## Compatibility, delivery and recovery

Disk records remain authoritative and unchanged. Old/new readers and external
writers share existing formats/locks; no API, protocol, client, database or Nix
option changes, and no coordinated machine update. Restart discards the view and
rediscovers records. The fix creates no state an older compatible reader cannot
load; this is not permission to select an older installed package. Preserve the
workspace's existing forward-only package recovery and all uncertain receipts.

Migration lead owns implementation, quick checks, independent final review and
normal authorized rollout/integration. This sender owns no source branch or
machine reservation. The investigating lead verifies the handoff; no need to
wait for implementation or send a second notification.
