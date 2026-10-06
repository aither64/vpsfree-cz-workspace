# Backup namespace and placement: complete branch review packet

Status: intended source is committed and quick owning verification passed.
Independent final review is complete with no findings in all four lanes; see
[final report](storage-profile-backup-placement-review-result.md). No runtime
or default integration clearance follows.

## Requested review

Review the COMPLETE provider range
`0ff827df13e82dfab4b536ff29979280f264e8f5..e33b8d0075fb37c49c91a4fcc68251a1e1815545`,
tree `e71ffb04e6f657be6d2c55676dd9ad7317a8ff3b`, all four HIGH-risk lanes:
general, architecture/repetition, scope/proportionality and risk/compatibility.
Read canonical mandatory-change-review plus every lane reference. Perform the
review directly, independently, read-only; no nested reviewers or settings override.

Session `2026-09-23-storage-redesign`, tracking in this directory. [Plan](plan.md),
[state](state.md), [architect briefs](design.md),
[exact inventory](storage-profile-backup-placement-inventory.json),
[entire final diff](storage-profile-backup-placement-complete.diff).
Affected repository/worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile`.
Actual enabled companion Admin:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadmin`
at `290f1ef07972e53c2b5154dbfa8b088802bde619`, unchanged tracked/index.

## Intended outcome and acceptance

New member NAS roots use stable `nas-<user-id>` names. Compatible sole legacy
numeric roots are strictly reused without rename. A current locking canonical
backup-path guard refuses competing catalog owners before physical command or
Plan enrollment staging can commit, across User/VPS/CatchUp and Plan calls.

Optional `storageProfile.vpsBackupFilesystem` preserves omitted v1 behavior.
Opt-in emits strict profile2 and a separate typed inspection2 contract. Source
Pool identity determines placement; empty hypervisor sources use the distinct
VPS destination, NAS stays on legacy. Sole valid existing copies on either
allowed VPS destination preserve their DIP/history/retention and Plan/task
identities. Missing preferred readiness does not invalidate existing reuse.
Refuse foreign, multiple, closed, role-drift, unowned pending and aliased copies;
no fallback, second copy, relocation or adoption. One owning selector serves
registration/CatchUp and confirmed guest selection; short admission ends before
SSH or physical waits. Provision enumerates all selected roots, and host
preflight validates exact typed desired/loaded routing before effects.

## Complete commit history and migration inventory

Exactly two independently useful owning commits:

1. `bd5bf53c9ba24ab6f37272ed928baa6a0b49e6ca` — namespace prevention.
2. `e33b8d0075fb37c49c91a4fcc68251a1e1815545` — opt-in placement preserving copies.

The earlier bd5 review is supporting evidence, not final whole-branch clearance.
Review BOTH commits and the entire final diff. Naming/prevention and placement
do not supersede one another. Their owning tests/docs belong with each policy;
Nix producer/helper/host inspection/provision/guest selector changes together
implement one placement contract. Fixture booleans/symbol corrections and the
pinned-Nix metadata envelope correction were completed before their owning
commits; no fixup commits or obsolete iteration are retained. Independently
conclude whether the full history contains obsolete approaches or unnecessary
compatibility paths. Consumed0ff/77dd/cd81 remain preserved in the base.

Complete final diff: ten paths, 1150 additions/72 deletions; binary/full-index
SHA256 `21f496e15576d841272fa5af6928e696a09fa6c5706ce9148aa5f03d30cd0c94`.
Exact ten final source hashes, full messages and inventory are supplied.
Flake inputs/lock and API harness are unchanged.

Explicit NO SQL MIGRATIONS in this provider range. Intentional persisted NAS
naming and profile2/inspection2 are not a no-format-change claim. Omitted-v1
reading remains supported; maintenance2/applied1/masks1/preserving-seed1 and
canonical schema1/policy3 are unchanged. Companion Admin290f's additive
foundation20260924210000 and captureindexes20260926100000 are outside the range:
previously published, disposable-tested and retained-consumed, never rewritten.
Actual blobs independently reread by lead: foundation
`7d929052f314d5a821b2ce65345680c0740b1b0c`, captureindex
`d60868e615024c70fb4b87b736a2466ceb8349db`, core schema
`e9aa952df7b94451c5491c965d22962265c8f545`.
Require an explicit whole-history and migration/format conclusion.

## Verification evidence and limits

Original selected-Admin complete disposable harness passed89/0 (122.857s),
focused pure7/69 and storage-profile host8/132 with zero failures/errors
(137.658s), and existing full-flake checks exit0 (1122.582s, full commands45/545).
Nine source files remain byte-identical to that successful batch. Only the
Nix smoke metadata reader was corrected after the original KeyError env:
Nix2.34.8 emits strict integer4 + derivations envelope. No format fallback,
profile contract change, alternate source or scenario was introduced.

The corrected run was cancelled at the user's pause: stage1 -15/770.019s,
driver1/770.627s, watcher770.755s/parity1, no-build unrun. Preserve it as
incomplete, not a test failure or completed pass.

On user continue, fresh Luna/low utility completed selected-Admin290f smoke
exit0/1203.510s then provider no-build exit0/11.881s: total0/1216.065s/parity1.
Actual omitted-v1 and active/retired-v2 services producer/marker projections,
invalid-root/topology refusals, both network/default/override selections and
both packaged runners built/loaded. No VM closures or cluster operations.
Evidence `/tmp/storage-profile-placement-resume-checks-20261006.8iin6afb/`.
The aggregate combines exact unchanged-nine-file earlier passes with fresh
corrected-smoke/no-build proof; it is not a fresh four-stage rerun. Commands,
timings and artifact references are in the inventory. Lead accepted statuses,
read milestones, source/index/HEAD/inputs parity and committed exact tested bytes.
Reviewer must not rerun tests/builds or read private logs/config/credentials.

## Consumers, documentation and compatibility

Provider owns profile/module/helper, immutable test.nix wrappers, host inspect/
preflight, provision and owning payload reader. Actual Admin290f owns Dataset
hooks, admission, Plan/Transfer/catalog/explicit DIPs; Node ordinary create-p
and destructive rollback are unchanged. Discover representative consumers from
actual source/imports/pins, including organization-tools immutable provider copy.
Current public shared workspace master5561663 still selects provider0ff with
nested generic4c3ea2/Codex3d07; root67505/i95b selected proof is historical.
No new consumer pin/package/activation/guest delivery has occurred. Provider's
own defaults API5c76/OS158 remain disabled; enabled verification uses Admin290f.

Lasting explanation is the owning `dev-clusters/vpsadmin/README.md`: NAS naming/
refusal and Optional VPS backup placement; repository README links this guide.
Lead owns the final prose pass. Session design/state hold individual failed
trial/delivery facts. Reusable pinned-Nix lesson is separately documented at
`notes/vpsfree-dev-workspace/2026-10-05-nix-derivation-metadata-envelope.md`.

Every API/Supervisor/scheduler/task writer must load compatible helper/config
before relying on placement. Old v1 writers can stage legacy choices; there is
no universal old-writer fence. Exclude/settle them during delivery. Active-v1
rollback after v2-only copies is unsupported; preserve enabled compatible
retired selections and all copies. Canonical host/runtime/migration boundaries
are unchanged; no host-migration/maintenance VM rerun or CI wait is requested.

## Boundaries and unresolved runtime work

Exact two-component root grammar remains; no overlap engine/history registry,
ID-based source classification, new CLI, generic/OSVM/Admin/Node changes,
namespace migration, rename/adoption/physical recovery, repair command or second
engine. Catalog guard cannot certify unknown physical paths or old unmanaged
writers. Existing retained NAS DIP5/VPS DIP12 alias remains held and refuses
reenrollment. Scheduler stopped; all old/new admitted objects/evidence retained.
Current presence/GUID/catalog do not certify historical NAS integrity.

Future G1b/G2 ownership/exclusion, authenticated approval/action journal,
complete dependency/lifetime/physical evidence and direct withdrawal approval
remain unimplemented/unreleased. Parallel architect design-only refinement is
not implementation or operation authority. New destination availability is
unproved. No retry/new fixture ID, cancel/unlock/delete/rename/adoption,
retirement/scheduling restart, quiet/strict/APPLY, default integration or package
activation is authorized by this review. Publication/composed pin/package proof,
external-idle activation, actual services/writer delivery and later approved
recovery/payload/history/rotation/automatic/repeat/retirement remain separate.

## Reviewer selection

HIGH: persisted naming/configuration/inspection, admission/path ownership,
placement, mixed-version deployment and rollback. All four lanes apply.
Eligible retained independent reviewer0: review/read_only, gpt-6.1-sol/xhigh,
thread01a0d230-7536-7ee0-b212-90b3f6847ec0. Recheck same-session roster/readiness
before assignment; retain saved settings without override/fallback. Report
findings by lane/severity with exact source references and evidence limits.
