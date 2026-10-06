# Final independent Admin handoff review

Reviewer0 completed all four HIGH lanes on the complete committed range
c4d9b50f4e74417ed37b5fe410cca3ec1addc24e..543a7979a1f17c68fe2c33eaccecf1bf864de3ba,
tree e8bbbadc65c6e8734c55723f2056ed2614d323c2. Saved reviewer identity:
roster23, review/read_only, gpt-6.1-sol/xhigh,
thread01a0d230-7536-7ee0-b212-90b3f6847ec0. Exact session/current and absent
identity environment pair verified independently. Canonical skill, all four
references and applicable workspace/Admin procedures read. No override,
fallback, authorship, nested delegation, tests, Nix/build/evaluation, network,
DB, private artifacts, runtime actions or mutations.

## Findings

1. **Important — risk/compatibility and general; OPEN on543.**
   storage_mutation_admission.rb:309-315 current-locks User/UserSession but its
   latest requested ObjectState lookup is an ordinary SELECT through
   lifetimes.rb:398-403. In an established outer REPEATABLE READ view, the
   requires_new savepoint retains that view. A separately committed requested
   suspension/soft-delete can be hidden while User.object_state remains active
   pending deferred confirmation. The common actor helper can authorize mode,
   catch-up, reservation or handoff despite current requested ineligibility.
   Origin a561366c, reused by543. Existing direct User-state and current Pool
   regressions do not cover it. Requested remediation: canonical current
   locking latest-state lookup under the held User lock and a genuine old-view/
   concurrent requested-state regression proving AuthorizationRefused without
   run/control/audit changes. No remote exploit or runtime incident is claimed.
2. **Advisory — general and architecture; accepted by lead separately.**
   Offline comparator has repeated whole-catalog scans at comparator.rb:111-128,
   382-388 and per-DIP tree lookups. Origin4de65ba8. A20k SIP/20k SIPB input can
   require about400m predicates in the first loop; capture scale evidence does
   not benchmark comparison. Representative replay measurements and duplicate-
   preserving indexes are the appropriate follow-up. No measured failure or
   physical gate is inferred.

No Blocking finding and no other Important finding. Publication is held for
finding1. The canonical current-read source assessment is pending; no code
remediation is yet accepted.

## Distinct lane conclusions

- **General:** complete27-commit history/messages and220-path diff inspected.
  Handoff preserves UUID/pointer/epoch/scope/acquisition, exact replay makes no
  write/catalog refresh, changed bindings refuse, same-epoch status detects
  change, and contract2 abandonment/unfreeze refuse. Important actor snapshot
  gap and accepted comparator Advisory remain.
- **Architecture/repetition:** API owns finite maintenance tuples and shared
  admission/status. SQL constraints are the separately tested persistence
  boundary. API/Node paired journals/receipts, signed5290/5291 and offline
  duplicate-aware ProofPlanner retain their distinct owners. No additional
  Blocking/Important architecture finding.
- **Scope/proportionality:** one coherent17-path contract2 persistence/reader/
  action/spec/docs unit; no physical interval, termination, recovery, approval,
  APPLY, TTL or implied expiry. Supported old captures and contract1 history
  have real consumed-state reasons. No scope finding.
- **Risk/compatibility:** actor-read Important. Other direct-admin/session/CAS/
  singleton/catalog/audit/rollback and CHECK/downgrade rules match the API-only
  boundary. No production strict or physical authority is added. Old setters,
  SQL, old Node and independent osctld remain outside universal fencing.

## Complete history and migration lineage

Independent complete binary/full-index diff SHA256
9d49249be30944553a82437f83deadfacf97773009eef09cdb0b50605bd5f7f3;
unit0879360d0783047aa71dd4b7af0d297f97fb51ff9ddf3584d37b74f52dcfcb0a.
All220 blobs/hashes and27 ordered commits match the inventory,27015+/457-.
Tracked/index clean; declared PHP cache untouched/unread. No remaining fixup,
removed privileged launcher, abandoned operational freeze workflow, unused APPLY
path or obsolete transitional schema. Supported legacy reads and distinct
consumed OS8d05/800 checkpoints remain justified; no unsupported history
consolidation is indicated.

Four additive migrations, with all predecessor blobs exact:

| Version | Blob | Recorded consumption |
| --- | --- | --- |
|20260924210000|7d929052f314d5a821b2ce65345680c0740b1b0c|Published/external historicalAdmin290f|
|20260926100000|d60868e615024c70fb4b87b736a2466ceb8349db|Published/external historicalAdmin290f|
|20261006120000|f3bbc80fa31967566536f57dc4e70815ebadea01|Feature425d/disposable; no master/live/external schema|
|20261006130000|f3ca91a407512529f7c0213a1778d487f86f6ad5|New disposable generation/spec; not published/live|

Schema13be672017a1ee5427966ed2e91a833602409a52/SHA2030ff5c matches migration,
callers and inventory. New130000 validates predecessor before DDL, adds only five
nullable audits and one CHECK replacement, refuses down on contract2/unknown/
stray audit. Reservation down retains any audit/pointer. No existence shim,
state adoption, redundant migration or consumed rewrite. Foundation upgrade
singleton and separate fresh-schema bootstrap remain; status/admission do not
lazy-seed.

## Consumers, rollout and proof limits

Reviewer inspected actual HaveAPI/WebUI/scheduler/admin/Plan/provider, Node
journal/receipt/status/remote-chain, signed capture and cold offline consumers.
Provider default API remains5c76; current root/retained source proof is older
than543. Current OS pin800 and its followed nixpkgs triples are source selection,
not package/guest/reader convergence. Optional maintenance imports stay opt-in.

Migrations precede compatible readers; converge/exclude old admission/unfreeze
writers before relying on ownership. Old425d rejects contract2 with its pointer
interlock retained; older setters/direct SQL/Node are not universally fenced.
Keep schema and compatible readers after audit exists. No downgrade, relabel,
pointer clearing or old-code operational rollback is supported. Signed5290/5291
mixed-version endpoints and old offline manifest readers retain their recorded
fail-incomplete and software rollback limits.

All numerical passes are parent/watcher evidence, not reviewer executions.
API102/0,migration8/0,endpoint1/0 carry only through the equivalent final actor
conditional; final lint10/0 each and selector20/89/0 plus normal543 hooks pass.
No one-batch six-stage pass is claimed. Broad flake baseline overlays.list stays
blocked. Global retained ResourceLock selector fanout remains separately
unmeasured; capped failures are incomplete evidence.

Contract2 invocation stays held until supported termination/recovery/physical
contracts. Earlier generation VM proves its bounded config/key/system/storage/
RPC scenario, not containment/reap or production boot persistence. No alias/NAS
history/destination/scheduling/retirement acceptance, default merge, package/
pin delivery, activation, retry/unlock/cleanup, identity publication, production
strict, node_quiet, repair_ready or G2/APPLY clearance follows. Cluster remains
STOPPED and all objects/evidence are held. Session active/open.
