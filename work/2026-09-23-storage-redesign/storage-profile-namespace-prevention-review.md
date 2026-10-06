# Profile backup namespace prevention: final review packet

## Assignment

Independent final committed-deliverable review, HIGH risk, all four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Retained reviewer0: review purpose/read-only, gpt-6.1-sol/xhigh, roster23,
thread01a0d230-7536-7ee0-b212-90b3f6847ec0. No settings override or fallback.
Read the canonical mandatory-change-review skill and all four lane references.
Review directly; no nested reviewers, authorship, tests, builds or operations.

Session: 2026-09-23-storage-redesign, trusted workspace
/home/aither/workspace/ai/vpsfree.cz. Verify current from literal tracking CWD
and both absent or exact environment identities before using owned records.
Read workspace AGENTS and applicable required routes; read provider AGENTS,
README and the actual Admin consumer guidance and relevant sources.

## Requested outcome and accepted boundary

Prevent newly upgraded profile writers from putting distinct logical NAS/VPS
owners into the same catalog-known physical backup path. New member NAS roots
use nas-<user-id>; numeric VPS roots stay owned by Admin. Reuse sole compatible
legacy/canonical NAS roots without rename/replacement. Refuse pending,
ambiguous or incompatible NAS roots. Under existing storage admission use a
current locking catalog read of node + Pool filesystem + Dataset.full_name,
including pending claims/duplicate Pool aliases and excluding only a validated
same copy. Refusal must roll back owning User/VPS/CatchUp staging before queued
create/Plan metadata commits. Plan add/verify uses the same owner guard; normal
del retains metadata unregister validation. No lock or transaction over waits.

Accepted scope is catalog-known claims through upgraded profile writers.
Unknown physical targets and old/unmanaged writers remain outside its guarantee.
No universal physical-ownership claim, new registry, Node create/rollback
semantics, or public arbitrary rename/detach repair is introduced. The existing
retained alias is NOT repaired by this change. No payload retry or populated
trial is authorized while that alias remains.

## Complete branch and final diff

Provider worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile
Branch: 2026-09-23-storage-redesign-storage-profile.
Base and fetched origin/master: 0ff827df13e82dfab4b536ff29979280f264e8f5.
Head: bd5bf53c9ba24ab6f37272ed928baa6a0b49e6ca.
Tree: ce5f7ba58990cfd1280fd96aa33a05a6dde90391.
The complete unmerged history is ONE normal new commit:
bd5bf53c9ba24ab6f37272ed928baa6a0b49e6ca vpsadmin: separate member NAS backup namespaces.
Prior0ff/77dd/cd81 are merged, published and consumed; none was amended.
All fixture corrections are folded into this new owner; no additional fixup or
transitional implementation remains. Assess that conclusion independently.

Final diff: three paths,348 insertions/9 deletions.
Full-index binary SHA256: d50e7c56b06a3d417d70d675c85d38d13c5f052b5972995023a09f3c59f39013.
Full files and diff are recorded in:
[Inventory](storage-profile-namespace-prevention-inventory.json) and
[Complete diff](storage-profile-namespace-prevention.diff).
Exact file SHA256:

- helper: be9b474ca0591ff022802df64e6db556f573bd3961237093f1b999fc9beb19dc
- spec: 42dd482395ef7cc80da1b3d34c42aa5e2ec5b74b36e59129a94de81a47cdc709
- README: ece8d1995f79239840f76bc67d7caf5748ed4b09c4819555c6458ab3b3aa4947

One commit bundles the naming/legacy reuse and shared-path refusal with its
regressions and durable compatibility explanation: these jointly prevent the
demonstrated collision while preserving existing identities. No input updates,
generated files, source moves or independently reversible feature is bundled.

## Migrations, state and compatibility

NO SQL migrations in this complete provider range. No wire/schema/CLI/module,
maintenance/applied/mask/seed/canonical-runtime version change. Persisted root
naming for NEW NAS is intentionally changed; existing objects retain names and
are read through the validated legacy path. Inherited maintenance2/applied1,
canonical schema1/policy3 and config/hold contracts stay unchanged.

Actual Admin consumer remains290f1ef07972e53c2b5154dbfa8b088802bde619. Its two
previously published and externally consumed additive migrations are outside
this range and untouched: foundation20260924210000 blob
7d929052f314d5a821b2ce65345680c0740b1b0c; capture20260926100000 blob
d60868e615024c70fb4b87b736a2466ceb8349db. Core schema blob remains
e9aa952df7b94451c5491c965d22962265c8f545. No historical migration rewrite or
new schema acceptance is claimed. Require an explicit whole-history and
migration-lineage conclusion, including no new migrations.

Every profile-writing API/Supervisor/task process must load the new helper
before enrollment. An active old helper cannot recognize prefixed roots and
may create another numeric root. Supported software rollback requires a
compatible preserving retired selection(enable:true,enrollment:false) and
normal metadata retirement first. This is a documented operator restriction,
not an old-writer fence or authority to retire the current aliased cluster.

## Actual owners and consumers

Provider storage_profile.rb owns policy/hooks/CatchUp/Plan registration;
Admin290f owns admission, transactions, catalog/full_name and Node parameters.
Inspect actual TransactionChain.fire2/use_in/do_append, User/VPS/Dataset Create,
DatasetPlans registration/locking and Confirmable contracts. Node ordinary
Dataset create uses create-p; Tree create and destructive rollback are unchanged.
The actual acceptance Guest resolves NAS by member/configured Pool, not numeric
name, so no fourth fixture path or ID workaround is needed.

Consumer workspace master/feature67505d97 selects provider0ff with explicit
generic3ed/Codex3d07 override; the new feature is not selected or delivered.
Provider organization-tools packages its relative helper through CLUSTER_DIR;
Nix/test.nix services config/helper and immutable guest SEED_FILE boundaries
remain. Inputs/defaultAPI5c76/OS158, follows and all lock bytes are unchanged.
Enabled retained trials use compatible Admin290f and the selected OS sources;
disabled defaults are not newly claimed to support the enabled profile.
Future feature publication/generated consumer pin/package checks/external-idle
activation/ordinary services delivery remain separate actions; no new default
integration or deployment approval is inferred.

## Documentation and rationale

Owning README Storage profile section explains namespace, current-read refusal,
compatibility/update/rollback and existing-alias limits without relying on this
session. Lead applied the writing skill to final technical prose. Root README
links to the cluster guide. Session design section
“Backup namespace collision: prevention and retained recovery boundary,
2026-10-05” records scope/verification/recovery decisions. Current plan/state
remain active. The separate reusable investigation note is linked from plan;
individual rollout evidence stays in storage-profile-rollout.md.

## Local verification and failed attempts

Member syntax on helper/spec and owned diff --check passed. Parent verified
exact frozen bytes/index, complete final diff and commit/source parity. No
hook framework/active executable hooks is declared in this provider; no hook
was bypassed.

Fresh Luna/low final batch passed exit0/104.756s/source_parity1 at exact final
three bytes against actual Admin290f. Stage1:88.605s,64 examples/0 failures.
Exact initial cwd is registered Admin root; the API shell enters api itself:

    nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadmin#api -c /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile/dev-clusters/vpsadmin/tests/run-storage-profile-api-specs.sh

Stage2 from provider root: nix flake check --no-build, exit0/15.518s.
The existing harness refuses inherited/configured DB before API helper, uses
owned automatic disposable DB and controlled RSpec options. No live DB or Node
execution. The inventory64 includes prior48+14 transactional+2 autocommit.
Actual User/VPS/CatchUp and Plan staging rollback is covered; equal-ID positive
VPS example captures real nested backup staging then a finite local sentinel
rolls back before unrelated VPS commands. Existing reader ownership/READ
COMMITTED/isolation/disconnect/reap/cleanup gate remains; during_staging:true
is explicit only for the new staged-current-read checks. No physical transfer
or ownership/disposition acceptance follows from the AR tests.

Prior failed batches are retained:64/8 setup failure due missing required
Dataset booleans, then64/3 string-versus-symbol expectations after those
checks. Corrections only add explicit factory-matching boolean values and exact
Confirmable symbol expectations. They change no guard or rollback assertions.
No-build did not run in either failed batch. No flake evaluation warning or
constant-redefinition warning was interpreted as test failure.
Private final evidence(reference only, supplied lead/watcher evidence):
/tmp/storage-profile-namespace-checks-symbols-20261005.2letm09k.
Reviewer need not read private runtime captures or rerun tests.

## Retained failure and residual limits

Prior trial proved NAS Dataset3/user3/DIP5 and VPS Dataset6/user6/VPS3/DIP12
alias in backupPool5/node201. Tree create failed exists; its rollback failed
children; subsequent send/receive members were skipped. Current GUID/presence
and zero locks/confirmations do not establish historical ownership or safe
physical settlement. Original file/fourquota/protectedDB/threeNode preservation
passed separately, not full aliased NAS properties or payload/history.
Scheduler stays stopped; all admitted objects/old faileduser5-chain48/evidence
stay intact. Existing-alias recovery requires its own supported capability,
provenance/disposition decision and authorization. No rename/delete/adopt,
repair/APPLY/unlock/reset/mode change, retirement, scheduling restart or retry.
VPS/NAS full+incremental/history/rotation/automatic/repeat/retirement and broader
storage writer/crash/repair acceptance remain unproved. API500 diagnostics stay
separate/held. No CI wait or new VM scenario is requested by this review.

## Feature publication

After final review, fresh SSH fetch/readback kept provider master0ff unchanged.
No rebase was needed. Normal SSH publication advanced only the retained feature
branch tobd5bf53; exact remote feature/master readbacks match those heads.
The public comparison captured0ff..bd5 before publication. Current-head Check
run37321075184 was in_progress at the one metadata read; no CI was awaited,
and no superseded branch run needed cancellation. Selected/root/defaults and
the retained cluster are unchanged.

## Review disposition

COMPLETE: retainedreviewer0 independently reviewed exact0ff..bd5, treece5f,
all three hashes and complete diff d50e7c56. No Blocking, Important or Advisory
findings in any of the four assigned lanes. Saved review identity, model/effort,
read-only access and independence verified as above. No fallback, overrides,
authorship or nested review. Reviewer independently concluded one coherent
commit, no obsolete unmerged history/shim/fixup/transitional implementation,
and no SQL migrations or new wire/schema/state-version boundary. Consumed
predecessors and the two externally consumed Admin migrations remain unchanged.

The review confirms sole validated legacy/canonical NAS reuse and one shared
current-locking-read guard at new-copy, reused-copy and Plan add/verify staging.
Admission precedes the Plan lock; exceptions roll back the owning User/VPS/
CatchUp transaction before commands commit. Normal Plan del retains its prior
metadata validation. Actual acceptance consumer has no numeric-root assumption.
Coverage includes competing pending/confirmed claims, real staging rollback
and separate-connection admission/current-read visibility; no physical transfer
or historical ownership proof follows. Owning README documents mixed-version/
rollback restrictions and limited prevention scope.

Reviewer treated64/0/no-build0 as supplied parent/watcher evidence and ran no
tests/builds/Nix/network/DB/runtime operations or private artifact reads. Residual
gates are unchanged: normal immutable delivery before relying on new behavior,
separate supported/authorized existing-alias recovery, and incomplete full/
incremental/history/rotation/automatic/repeat/retirement acceptance. Scheduler/
objects/evidence stay held. Source review grants no default integration,
delivery, current-alias recovery or retry authority.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-23-storage-redesign/
