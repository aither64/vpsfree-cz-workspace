# Review reconciliation

Initial reviewed heads: codex-web bba2ae1, dev-workspace774c208,
organization d0ebe39, workspace bfc80f2. All four required lanes completed with
fresh gpt-5.6-sol/xhigh reviewers. General/architecture used collaboration;
risk/scope used fresh ephemeral read-only Codex CLI sessions after tool capacity
refused additional fresh collaboration agents. No nested reviewers.

| Finding | Lanes / retained severity | Resolution status |
| --- | --- | --- |
| Receipt can shadow an older-generation canonical session | Risk / Blocking | Resolved in runtime1de0a78: explicit conflict reconciliation, pre/postbinding rollback and exact fork boundary regressions; no false adoption of receipt completion. |
| Terminal receipts consume lifetime limit; deleted slugs remain reserved | All / Important | Resolved in runtime1de0a78: bounded terminal retry cache, lifecycle-aware companion retirement, deleted slug reuse and preserved unfinished attempt identity. |
| Exact fork journal recovery still needs live source | Risk / Important | Resolved in runtime1de0a78: established exact journal authority restored; archive/delete source regressions pass. |
| Git rename analysis silently stops above1000candidates | General, scope, risk / Important | Root uses complete detection with existing subprocess deadline;1001modified-renames regression passes. |
| Authority-wide ledger grows to64MiB and rewrites all history | Architecture, risk; scope advisory / Important | Resolved in provider4dde3c6: bounded hot state, compact per-turn history and per-thread async durable ownership; stress/restart tests pass. |
| Global history/recorder locks delay unrelated sessions/events | Architecture; risk advisory / Important | Resolved in provider4dde3c6: per-thread history synchronization and durable writers, snapshot aggregation outside event locks, stalled writer/RPC isolation and resumed pagination tests pass. |
| Optional timing makes ordinary transcript fetch full history | Scope / Important | Resolved in provider4dde3c6: latest20 transcript, internal full timing metadata, unused public arrays removed. |
| Typed-kind whitelist/export probing can silently drift | Architecture / Advisory | Resolved in runtimea21676e/provider0522aa2: direct required export and normalized-activity renderer selection. |

The timing persistence repair and mixed-generation conflict handling change the
new design. Rerun the affected review lanes on committed deltas before long
integration. Narrow ready-retention and rename corrections are directly checked;
no full lane rerun is needed merely to confirm those line-level corrections.

Original finding reports remain immutable evidence of their reviewed heads.
Final commit IDs, focused results, decisions and delta-review outcomes will be
recorded below when ready. Full packaged/live/upgrade/rollback acceptance remains
pending; passing original-head feature CI does not validate later remediations.

All initial findings have focused remediation evidence. General, architecture and
risk follow-up reviews are running from review-delta-packet.md; scope follows
when a review slot is free. These reruns assess the new persistence/recovery
design, rather than mechanically confirming earlier requested changes.

## Follow-up findings

- General rerun complete: Blocking plan-source recovery boundary. The destination
  can be canonical-ready before receipt evidence, and an archived/deleted source
  then prevents exact start-journal recovery. Creation owner is extending the
  existing destination journal authority pattern; fresh-source validation stays.
- General Important (also architecture lead): no-watch reads retain full history
  entries indefinitely, while recorder summary caches retire and archived browser
  polling repeats every5seconds. Scope of repair will include cache ownership and
  stopping continuous archived polling. Architecture/risk reports are pending.
- Root confirms monitor currently retains an established subscription after a
  later VerifyThread failure. Narrow cleanup at that failure boundary is needed.
- Scope rerun will use final repaired commits rather than review an intermediate
  cache ownership design. No long integration/deployment has started.

- Architecture rerun completed with4Important: history cache ownership, authority-
  wide backfill fan-out, retained timing files, and duplicated strict fork-journal
  schemas. Risk completed with1Important archived canonical receipt shadowing and
 1Advisory on retained timing files. Final reports remain unchanged evidence.
- Root fixes monitor fan-out with four shared, cancellable slots for worker
  verification/subscription/history and browser history reads. Queued notifications
  remain coalesced and independently observed. A40-worker startup test proves the
  bound, cancellation and progress; three-repeat activity race suite passes4.590s.
  Root also drops existing observation after VerifyThread fails and stops
  successful noninteractive timing polls. These are committed in0cb6b89.
- Creation owner removes the Go fork-journal schema duplicate. Validated retry
  arguments go to the CLI, which alone distinguishes exact destination-journal
  recovery from fresh-source validation under its locks. It also handles archived
  canonical destinations through exact evidence or a nonblocking archive notice.
- Provider owner adds explicit history cache read/watch refs; completed unowned
  caches retire, and at most8 unpinned incomplete backfills retain retry progress.
  Active and queued readers pin the same gate through last unsubscribe.

### Persistent history retention decision

The coordinating review reconciles the retention severity as Advisory. Existing
`dev-session delete` deliberately archives the Codex thread and moves tracking/
creation state into private recovery storage (libexec/dev-session1542-1592 and
retire_portal_thread4822). A deleted portal name therefore does not mean that
its conversation history is purged. Retaining timing keyed by the original
thread identity is consistent with that recovery model and the requested retained
archive totals; name reuse resolves its new manifest thread and cannot select
the old thread's timing. The recorder stores bounded metadata per turn, without
prompts/answers, and never rewrites the full authority history.

There is a real inode/disk cost (one small summary file per observed turn), so
this is retained as an operational limitation. An automatic deletion sweep or
quota would introduce a new cross-component recovery/expiry contract not present
in the approved plan and could discard requested historical totals. No automatic
expiry is added in this initiative. A later explicit purge/retention feature
should own conversation recovery and timing together. This decision follows the
actual retained-data contract, not a vote between reviewer severities.

## Final architecture and scope pass (runtime8760619/providerbdd79be)

- Architecture Important: passive reconnect restoration bypasses the consumer
  admission limit, and duplicate same-thread browser reads can occupy every
  authority slot while waiting on one history gate. Accepted; root's3d0ca04
  admits one thread before the global slot (40duplicate-reader race regression).
  Provider-local passive RPC/reconnect admission is being repaired separately.
- Scope Important: failed/paused creation receipts can survive an explicit
  completed destination deletion and recreate that deleted session on retry.
  Accepted. Existing completed-removal recovery metadata must supersede older
  accepted requests, including queued retries; absence alone cannot establish
  deletion. Preserve exact retired receipt identity for concurrent stale workers.
- Both Advisory: an archived-conflict notice survives revival. Use historical
  wording so the notice remains accurate through the supported lifecycle.
- Both reviewers independently support the retained timing decision after
  inspecting delete/archive ownership. Per-turn disk/inode use remains the
  recorded Advisory cost. Do not add an unrelated conversation purge contract.

Further affected-lane review will assess the committed admission/deletion design
against generation cancellation, explicit name reuse, and additive rollback.
The already-reviewed feature scope and immutable original reports remain intact.

The focused scope lane passed with no findings. Architecture cleared the passive
admission design and found one Important cleanup gap: deletion-terminal paused
and failed receipts retire only on exact-slug access, so enough untouched records
can fill the global512-entry capacity. Accepted; apply the existing locked
retirement operation during startup/capacity reclamation and verify unrelated
new-session admission plus retention of inconclusive/live attempts. This reuses
already-reviewed behavior and needs focused verification, not another reviewer
rerun merely to confirm the requested call-site repair.

Architecture's capacity finding is fixed in cfad68e, reusing locked retirement
during startup loading and capacity checks. Focused Go race tests pass28.965s,
covering512 cached receipts, startup with513 receipts, unrelated name admission,
and protected unresolved/running/lock-held/journal-owned records.

Risk found an Important causal-ordering flaw in comparing acceptance and deletion
wall clocks: backward corrections can allow stale retry; future deletion times
can prevent fresh reuse. Accepted. Replace creation's time ordering with the
existing completed deletion operation identities. The proposed fixed-size
snapshot belongs only to this unreleased private receipt/binding format; the
installed predecessor has no asynchronous receipt flags or readers (verified
with git grep at runtime base bcbaf825). Strict manifests/lifecycle/start/fork
journals remain unchanged. No compatibility path for undeployed intermediate
feature revisions is required. The next implementation must eliminate the
timestamp fallback and preserve exact worker/receipt identity under locks.

## Final causal deletion replacement

Admission architecture's capacity finding is fixed by invoking existing absent
receipt retirement during startup and capacity reclamation. Focused tests cover
512 stale receipts,513 startup records and protection of running, unresolved,
locked and journal-owned work. No new cleanup framework was added.

Admission risk's clock-order finding is fixed in runtimef2512c1 (creation commit
169af2f): freeze SHA-256 of verified sorted unique completed deletion operation
IDs under the destination runtime lock; require the exact current private
receipt at every CLI destination lock. Missing/replaced requests reject and
ordinary cache retirement removes their private files. Wall-clock comparison,
mtime fallback and a separate retired-ID mechanism were removed. The existing
exact-operation CompletedRemoval behavior remains.

Ruby40tests/495assertions and focused Go race tests pass; current runtime CI
34699256023 is green. Architecture/risk independently review this new design
from the committed causal packet. General/scope are not rerun merely to confirm
unchanged behavior or the reduction of mechanisms. No long acceptance has run.

Final causal architecture and risk reviews completed on f2512c1/eaf4a21/8456d09
with no findings (fresh gpt-5.6-sol/xhigh). All mandatory lanes are satisfied.
Residual very-large deletion recovery enumeration latency is unbenchmarked;
this is an operational scaling gap, with bounded receipt capacity regression
coverage and no arbitrary retention/purge change. Runtime CI34699256023 and
organization CI34699288252 both pass on exact final heads. Long packaged, VM,
browser, live App Server and rollback acceptance is now authorized to start.

Browser acceptance found the activity GET missing from the legacy session API
forwarder. Runtime8d3d44c adds one existing-route mapping and its contract case.
Root verified it reaches the reviewed capability/identity resolver, with no
new public design or mutation path. Focused checks pass; actual browser timing
is being rerun. No unaffected reviewer lane is restarted.

Installed check-codex found incomplete scanner inputs despite passing source
coverage. Runtimef5d5878 copies all reviewed provider production sources into
a private directory and validates installed coverage. It changes only package
assets and the checker's private file path. Root's staged complete source set
passes the selected0.154experimental schemas; installed check follows rebuild.
No provider/runtime API or persistence design changed.

## Deployed plan-goal normalization

Real acceptance found a trailing-newline mismatch between the frozen portal
goal and Ruby read_goal. Runtime d3bfd0f aligns only derived goal hashing with
the exact CLI strip semantics, preserving the captured plan and all other
identity checks. Its regression invokes Ruby and recovers an older raw frozen
receipt through ordinary GET without CLI resubmission. Focused race checks
passed in 1.912 s and 32.353 s.

Fresh general and risk reviews (gpt-5.6-sol/xhigh) completed with no findings.
Reports: review-goal-general.md and review-goal-risk.md; exact scope and
consumer pins are in review-goal-normalization-packet.md. Architecture and
scope are unchanged by this bounded alignment of an existing contract.
Remaining validation is the installed package and same retained real fixture,
including unchanged receipt/thread/attempt and single initial submission.
