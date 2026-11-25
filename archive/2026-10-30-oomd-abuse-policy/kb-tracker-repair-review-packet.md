# KB tracker repair — committed final review packet

Owner3, 2026-10-31. Source frozen for retained reviewer0; no publication,
complete-suite run or fresh guest has started. Lead assigned all four lanes at
HIGH risk with saved gpt-6.1-sol/xhigh settings. Authentication, persisted process
proof, mixed-version handling and release authority make this high risk.

## Requested outcome and scope

The user authorized “well find the root cause and fix it”. The accepted actionable
contract is [kb-tracker-repair.md](kb-tracker-repair.md), especially “Frozen process
receipt and readers”; [design.md](design.md) is aligned. Plan/state remain owned by
the lead in this session. The demonstrated host mechanism is executable-link
EACCES across the installed bridge helper's legitimate credential transition.
Historical PID2989738 remains unidentified. The repair separates strictly
authenticated control from proved, wait-only descendant lifetimes and prevents
tracker errors from certifying readiness or complete shutdown.

Acceptance requires deterministic strict-control/lifetime/versioning/failure
controls, then independent safety review, complete affected suites and actual
normal bridge start/capture/stop proof. The original four PNGs remain outstanding:
getting-started/vps-list and restore-backups/playground-vps-list, CS and EN.
No reduced fixture, helper whitelist, EACCES ignore, permission/root change,
OSVM fork, force operation, old receipt conversion or extra runtime capability.

## Exact source and history

Repository: git@github.com:vpsfreecz/vpsfree-kb-contracts.git. Worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsfree-kb-contracts`.

- Base/default: ce2c8cd9358c3636e5d39343e595df813a0b197f.
- Reviewed pin parent: 7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d.
- Repair head: dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d.
- Repair/final tree: fb6bd22aed441103b6a907c7ed481d4f6679cb2c.
- Fresh SSH origin fetch before commit retained unchanged default and remote feature7bdee.
  Repair is local only pending review; worktree and index are clean.

Complete base-to-head series, in order:

1. 7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d — Pin shared incident escalation for VPS list captures.
2. dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d — Separate descendant lifetime tracking from runner control identity.

Direct repair:12files937 additions/201 deletions. Full range:17files945/209.
The first commit is the one consolidated five-file app pin stream; the second is
one coherent runtime producer/readers/tests/documentation change. No obsolete
repair iteration, fixup or repeated pin stream is in the final series. Old interim
pin receipts/refs remain evidence outside the final series. No migrations;
process receipt schema2 is an intentional versioned format, with no data conversion.
The app remains f60d41a453b1703e42de4341285bdc6ba339aff0, OS input remains
6bdf458fd9105379860234ff33d352e55844f08f; all five pins and the complete lock are
byte-identical to7bdee. No dependency refresh in this repair.

The normal commit ran through the pinned Nix shell with exit0 and no bypass.
This repository declares no hook framework; core.hooksPath is unset. Commit
message was supplied with `git commit -F`, wrapped to80 columns.
[Committed provenance](kb-tracker-repair-evidence/committed-provenance.json),
[direct repair patch](kb-tracker-repair-evidence/repair.patch),
[full final diff](kb-tracker-repair-evidence/full-series.patch), and
[exact final file hashes](kb-tracker-repair-evidence/quick-input-identity.json).
Original7bdee base/head/tree and retained backup ref are in
[original-range.json](kb-tracker-repair-evidence/original-range.json).

## Producer, boundary and consumers

- `cluster/lib/kb_process.rb`: stable boot/PID/start/PPid samples, all-task ancestry
  admission and reparented-lifetime revisit; one ProcessReceipt schema boundary.
- `cluster/lib/devcluster_runner.rb`: schema2 writes and monotonic first-parent
  graph; first-error latch, same-mutex ready publication/withdrawal, supervised
  tracker and existing one-shot graceful drain/reapers. Errors never complete.
- `cluster/lib/kb_runtime.rb`: process_record, live?, ready?, status, authenticated
  control, gone? and shutdown handoff all use explicit receipt dispatch.
- `tools/verify-live-lease.cjs`: inline Ruby calls that same validator; JS retains
  strict control/version and monotonic lifetime/parent observations. It confers
  no signal/release authority.
- `tools/runtime-verify.rb`: validates the actual retained complete process receipt
  and expects schema2 from the current producer.
- `tools/fixtures/fake-kb-runner.rb` and corresponding runtime/machine/verifier/JS
  tests emit or validate the same receipt; control and ready marker remain schema1.
- `tools/fixtures/schema1-process-reader.rb` contains byte-exact old7bdee reader
  method excerpts, including shutdown-exit handoff. Original-source extraction
  identity is recorded in
  [old-reader-excerpt-proof.json](kb-tracker-repair-evidence/old-reader-excerpt-proof.json).

Search of cluster/tools/lib/runner identified no further production process-proof
reader. `vpsfree-dev-workspace` canonical master pins KBce2c8cd9 and wraps its public
runtime/status API in `dev-clusters/kb/lib/provider.rb`; it does not parse process
receipts. No extension pin or source changes are included. State/launch/artifact,
public CLI, socket peer/control protocol and immutable guest proof are unchanged.

## Compatibility, retained failure and documentation

Schema2 has control/descendants and omits runner/children. Full tuple control and
socket authentication remain strict. Lifetime records authorize only waiting and
refusal, never a signal or deletion. Ancestry is anchored, acyclic and unique;
legitimate exec/UID changes do not end a proved lifetime. Missing/unreadable proof
refuses. Polling cannot reconstruct descendants that escape before observation.

New readers explicitly accept valid schema1 under its original strict semantics
and refuse incomplete/malformed/mixed/unknown forms. Exact old-source controls
refuse schema2 ready/control/gone/shutdown handoff before socket action. A new run
must finish under its owning source before rollback. No historical conversion or
release authority was added.

Old instance f66a2056-c6e7-4300-904a-c7d2758addae/run
ea841826-207a-4419-8e21-ea61bf3ea678/artifact
18190571-ae21-4206-94ef-c774e04f188c is immutable and unchanged. Old public start
returned0/false-ready; the one authorized public stop returned1 after900.30199s.
All four QEMU exits were0,29 recorded PIDs absent, but incomplete proof and exact
claim/socket remain. No repeated stop/reset/claim cleanup or new runtime occurred
during repair. Relevant native receipts are in
[kb-capacity-evidence](kb-capacity-evidence/) and the current architect brief.
Mechanism proof is [helper-proc-diagnostic.json](kb-capacity-evidence/helper-proc-diagnostic.json).

`cluster/runtime-contract.md` documents lifetime/control authority, versioning,
rollback ordering, tracker supervision and retained failures; its README link
already makes it discoverable. Neutral technical English was checked directly
under vpsfree-user-facing-writing/humanizer-en, preserving all machine markup.
No KB member pages or screenshots changed yet.

## Quick verification and limitations

Commands ran in the pinned shell before commit; final staged file hashes and tree
are bound above. Functional producer/reader code remained unchanged through these
focused passes. Later additions were only the concurrent/normal-exit controls and
the old handoff test, checked separately. This is scoped quick evidence, not an
exact-head complete-suite or real-runtime claim. Tool identity: Ruby3.4.9,
Node24.18.0; shell derivation and actual executable paths are in
[pinned-shell-derivation.txt](kb-tracker-repair-evidence/pinned-shell-derivation.txt)
and [tool-identities.log](kb-tracker-repair-evidence/tool-identities.log).

| Scope | Actual result / evidence |
| --- | --- |
| Ruby9 files + Node2 syntax; lifetime/receipt controls | Process group12/76 PASS in focused-first.log; actual helper exe-EACCES negative, same-UID exec positive, graph/reuse/root/parent/version/schema1 controls |
| Runner first focused batch | Five of six cases passed; join injection timed out. Full batch remains FAILED; see diagnosis below |
| Corrected join; lease; verifier suffix | PASS1/20 +11 JS cases +2/38; focused-suffix-corrected-result.json/log |
| Concurrent-ready failure, unexpected tracker exit | PASS2/33; concurrent-exit-result.json/log |
| Unexecuted all-task discovery + quiesced/late-child/unknown-namespace runner checks | PASS6/65 +6/347,18.185s; compatibility-result.json/log and fresh Luna/low watcher receipt |
| Engine handoff/complete refusal/control peer/readiness/capture loss | PASS7/102; engine-focused-result.json/log |
| Final exact old reader incl handoff, with legacy ready marker | PASS1/5; old-reader-final-result.json/log |
| Whitespace and committed file identity | git diff --check PASS; clean committed tree equals staged quick-input identity |

All evidence paths in that table are beneath `kb-tracker-repair-evidence/`.
The initial process test failures and join diagnostic attempts remain retained.
The join fixture used bare `raise` on a Thread singleton: Ruby dispatched
Thread#raise into the already-ended tracker. A bounded standalone negative/positive
control showed Kernel.raise instead reaches the joining caller. Only that fixture
was corrected; its requested production error path passed thereafter. No source
failure was relabeled green.

The earlier full7bdee source checker FAILED on unchanged post-stop argv metadata;
its accepted PIN-ONLY baseline exception, diagnostic pass and suffix pass remain
[kb-source-check-disposition.md](kb-source-check-disposition.md) and
[kb-shared-source-review-packet.md](kb-shared-source-review-packet.md). Hosted
ordinary source41187229857 and Managed41187229710 passed7bdee, not this repair.
No full bin/check pass or runtime/capture proof is claimed fordc608.

After independent review: affected complete source suites via fresh watcher,
follow-up findings as required, publication/CI coordination, fresh native capacity
and disjoint resource admission accounting old retained extents, immutable source
and all-running-closure attestation, healthy normal bridge start/stop and the four
approved captures. Strict exported inventory/visual acceptance/media commit and
exact final strict hosted Check remain required. No production writes, merge,
deployment or session lifecycle action is authorized.

Review should explicitly conclude all four lanes, complete-series consolidation
and no-migration lineage. Owner3 retains source/Git/runtime execution; lead owns
review coordination and release decisions.

## Final consolidated source delivery

Original review dc608 and narrow K1 successor21d remain retained under review
refs. Reviewer0 completed all four lanes with K1 sole Important; lead inspected
and closed K1 under step9, no contract expansion or confirmation-only rerun.
Coherent final source56d716e0806fe9c5167f4b55750e5532767ae0ba has EXACT tested
21d tree9bf384bc70f34d8ec34d0216bfda85c7b3a376c6. Final series is unchanged
consumed7bdee pin plus one corrected runtime commit; no migrations/input change.
Full source bin/check --allow-missing ran once through fresh catalog Luna/low and
PASSED exit0/458.308s on that clean exact head/tree. Original failed7bdee evidence
and scoped exception remain separate. No full groups were run separately again.

Fresh SSH fetch/default proof and exact7bdee lease publication succeeded; remote
feature56d/defaultce2 independently confirmed. Capture-comparison recordedce2→56d.
Full final histories/range-diff/tree equality and publication logs/proof are in
kb-tracker-repair-evidence/fold-provenance.json, fold-range-diff.txt,
final-history.txt, full-source-result.json/full-source.log, publication-result.json
and publication-after.txt. Exact-head ordinary Check41198860086 and Managed
41198859903 automatic runs are delegated to one fresh watcher; not terminal proof
yet. Generic package preparation is independent; new bridge/capture awaits
remaining-growth accounting and fresh admission. Old failed runtime untouched.
