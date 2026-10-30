# Independent final source review

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh/read_only; no overrides, nested
agents, source/session writes, builds, evaluations, VMs or tests launched.
Returned to lead for saving. Reviewed exact base
846bb469505789ba0b2a405fa5905ba6d8253006 through head
9bea27c93beb22d08c3be2eb481bce4ef57300a6, tree
04b33b688828b55c8d91deef51c49392de78495c.

## Findings

1. **Important: recorder can report success before its last BPF events and
   losses are accounted for.** Commit9bea27c9,
   tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.c407-419; supporting
   hotplug-recorder.bpf.c50-65,147-150.

   Shutdown updates state.enabled to zero, consumes the ring and snapshots
   counters/missed hits, and only afterwards destroys kprobe/raw-tracepoint
   links. The map update is not a quiescence barrier. A CPU127/remote invocation
   can pass the enabled check and reserve an event before disable, remain in
   flight through consume/statistics snapshot, then increment emitted and
   submit afterwards. Recorded bytes and snapshotted counters can agree, so
   report_losses succeeds, but the late event is discarded when ring/object
   are freed. Missed probes can also change after snapshot. This violates
   rejection of incomplete capture and can hide the final scheduler operation.

   Establish and demonstrate producer quiescence before final drain/stable loss
   accounting, retaining authoritative final missed-probe evidence. Failure or
   inability to obtain it must remain nonzero. A flag plus one consume is
   insufficient. This is experimental-tool correctness, not ordinary
   qualification behavior or evidence of a kernel cause.

2. **Important: retained commit descriptions omit required validation
   provenance.** All eight commits274e826da through9bea27c93;
   docs/os/patch-series-policy.md90-98, especially97, requires every meaningful
   retained commit to explain validation performed.

   Complete Git bodies and final-review-series.txt explain problem/behavior but
   none records checks actually performed and outcome. For examplec2c5 omits
   177example/sixfilelint evidence;9bea describes runtime prerequisites but not
   successful C/BPF compilation/help/argument checks. Session evidence exists;
   this is durable provenance, not failed checks.

   Add truthful concise validation/results and relevant unexecuted runtime
   limits to logical owners' descriptions using existing history procedure.
   Preserve split/source-tree equivalence for message-only changes and fold
   recorder repair into its owner; no mega-commit or chronological fixups.

No Blocking finding established. Important findings require fixes or explicit
recorded disposition before proceeding. This report does not declare readiness.

## Independent scope and evidence

Reviewer independently checked history/messages/each commit's path ownership,
complete changed source/spec/docs, adjacent import/monitor/DB/GC/start/custom
boot and test/template consumers. Live head/tree matched packet and status/index
were clean. Saved final-review.diff byte-equals exact Git diff, SHA256
72f807b635645ee46f542ff62b93b1a08eb182af5a70b55e6a4fc04e56eb66d4.
Eight commits,25paths,3537insertions/89deletions.

Read mandatory-change-review/allfour references, session/documentation/Git
procedures, local AGENTS/patch-series policy, plan/state/current design top,
packet/series/diffstat and relevant checks/evidence. Both DEV_SESSION variables
absent; dev-session current from trusted bound session confirmed exact slug.
Source review is neither architect acceptance nor runtime certification.

## Whole history, migrations and repeated streams

Eight semantic owners are coherent:

- 274e826da: future writer persistence and focused real-reader tests.
- c2c5a006b: existing-state authenticated recovery plus inseparable import
  publication/GC refusal safety, tests and docs.
- 405a80285: standalone predecessor DHCP fixture/safe retention tests.
- 87e6bd4a5: first-switch capture and diagnostic registration/docs.
- 595bafea9: independent historical default selection change.
- 4de50f004: focused production-origin v1/v2 validation/docs.
- 81235fe74: qualification cumulative health checkpoints.
- 9bea27c93: standalone experimental recorder/docs.

Writer and reader are independently useful future-write/existing-state fixes.
Historical scheduling and production scenario are independent behaviors, not
repair clutter. Shared catalog/common/docs paths do not imply redundancy.
Historical diagnostics remain manual evidence tools; existence does not
authorize another historical boot. Rejected uncommitted historical assertion
expansion is absent.

**Whole-history conclusion:** no obsolete unmerged approach, fixup/WIP residue,
reverted experiment or transitional compatibility shim remains. Logical
ownership sound subject to validation provenance and folding recorder repair.

**Migration conclusion: no migrations.** No schema/new persisted format/version;
repair changes existing YAML dataset/cleanup values and preserves IDs. No
transitional or merged/released/deployed/external migration boundary to retain.

**Repeated-update conclusion:** no repeated dependency/channel/input/kernel-pin
or generated-artifact update stream. No dependency/flake-lock/kernel/channel
pin changes. New immutable diagnostic predecessor/target/production baseline
have distinct roles rather than successive updates; no redundant intermediate
pin retained.

## Architecture, compatibility and scope

Recovery uses existing ProcessIdentity descriptors/duplicate installation,
saved ID/GC/live private-root checks and final rechecks before persistence/
publication, preserving unknown top-level fields/GC bytes. DB event-after-insert
is reconciled by exact object identity; published ownership survives attachment
errors. Manipulation exclusion covers synchronous publication/monitor/console.
GC inhibition reaches common sink for prune/queued frees. Tests cover malformed/
ambiguous ownership, preparation changes, descriptor/lease rejection and
pre/post publication failures. No additional concrete data-loss or authorization
regression found in those paths.

Production scenario independently observes saved/live/GC ownership and payloads,
new writer/reloads. Fixed stable production source/two modes fit scope. Keep
independent observations separate from implementation adoption oracle.

No generic runner/flake-exported framework API or cross-project protocol change;
templates/catalog use existing interfaces, no downstream pin/coordinated node
update. Existing YAML old-reader-loadable; rollback loses authenticated recovery
and pool fence as documented, not schema migration. Diagnostics standalone/opt-in
without weakened confinement/warnings. No disproportionate framework/registry or
maintenance-significant duplicate policy found.

## Verification limits and gates

- Writer23/0, reader177/0 and sixfilelint support source review; DHCP16/0,
  production38focused+41static, formatting/syntax and recorder C/BPF/CLI checks
  are bounded quick evidence. Reviewer did not rerun or infer runtime success.
- Publication/unfiltered CI held: threecatalog0 do not complete selector gate.
  outPath coercion then missing localpath.rev failed tools. Finish corrected
  immutable Git/source/NAR/full-input binding and native selector over retained
  catalogs. Successful4de supplement only proves that checkpoint, not later
  final package/runtime.
- Before production VM: actual production/candidate service/wrapper/resolved-gem
  and changed-file byte proof for exact candidate; store path/version insufficient.
  Then v1/v2 runtime must prove repair/no-rewrite/new writer/payload/retirement.
  Failed postimport capture does not establish these.
- Original DHCP denial untraced/unreproduced; successful NNP/filter pairs under
  new diagnostic image/ptrace, incomplete lifecycle. No confinement repair or
  natural network/Podman pass follows.
- Recorder verifier/attachment/count/loss and warning attribution unproven;
  compilation does not close gaps, experimental label does not excuse race.
- No default integration/deployment/historical boot/cleanup/lifecycle authorized.

Reviewer kept all source/session files unchanged. Portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
