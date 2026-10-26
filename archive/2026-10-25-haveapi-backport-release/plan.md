# HaveAPI 0.30.2 backport and release

## Goal and scope

Backport all applicable improvements from HaveAPI master to the maintained 0.30
series and publish release 0.30.2. Only HaveAPI project code is in scope; no
consumer pin updates or production deployments are requested.

## Approach and ownership

- Architect0: inventory master versus 0.30, assess compatibility and release
  procedure, write design.md with implementation boundaries and verification.
- Implementer0: backport functional changes, tests and technical documentation
  from the approved design; own commits, checks and review fixes.
- Implementer1: independent release preparation/verification package identified
  by the architect; serialize overlapping edits and Git operations.
- Reviewer0: independent final committed-deliverable review after quick checks,
  including complete history and migration provenance, before long checks.
- Lead: tracking, acceptance, user-facing writing and release coordination.

## Compatibility and deployment

Preserve the 0.30 public contracts and component version compatibility. Assess
persisted state, schema/migrations, Ruby dependencies, API/client/CLI contracts,
mixed versions and rollback before implementation. No system deployment is
planned. Determine whether every master change can safely enter a patch release;
record adaptations or any material incompatibility rather than silently omitting it.

## Release and integration

The user explicitly requests release 0.30.2. The canonical target is `haveapi-0.30`; publish all maintained components
through the tagged GitHub Actions workflow after its protected approval gate. The user request authorizes maintenance-branch integration and documented PHP
mirror publication; User correction explicitly requires the tooling/CI fixes to integrate HaveAPI
master first, then be backported to haveapi-0.30 with -x. Original nine changes
already exist on master. Preserve original C/evidence; publish only final successor.
Prepare and review all release artifacts before publication. Preserve feature refs
and leave this session open.

## Documentation

Readers are maintainers and HaveAPI consumers. Keep release notes and lasting
behavior changes in HaveAPI documentation; design, coverage, commands, release
receipts and temporary verification evidence belong in this session.

## Verification

Follow HaveAPI instructions and Nix environment; retain hooks. Inventory complete
source changes and backport coverage. Run focused quick checks and package/version
checks, commit intended deliverables, run independent final review, then longer
supported tests and CI through a fresh utility watcher. Verify published refs and
package versions after authorized publication.

## User correction: master first

User explicitly directed: “the fixes should go to master first and then be
backported”. This authorizes HaveAPI master integration for the necessary
performance/CI corrections. Author/review/check them on a separate same-session
master feature; integrate master before -x backport. Reconstruct release with
A plus final upstream fixes and one .2 metadata commit. Old reviewed C and its
artifacts are superseded evidence, never a release source. Retain old/new ranges
and equivalence/change evidence; no published default history or tags rewritten.

## Current performance acceptance (user steering)

User wants obvious regressions across all request categories, not fine timing on
noisy hosted workers. Accepted design current section supersedes all prior
mandatory precise quick/weekly pass gates. Deterministic correctness/auth/output/
counts/allocation/provenance remain blocking. Timing ordinary/noisy/inconclusive
is informational; gross median >=10x AND +1s blocks; any representative request
>30s runaway fails with diagnostics/owned cleanup, setup separate. Existing API/
SQLite/OPTIONS/HTML suite plus one larger full Rust-profile HTML smoke. No new
framework/calibration/reference change. One representative exact-head hosted
master and final release gate with applicable component/build CI, master first
then -x backport and separate .2 metadata.

## Latest acceptance overrides coarse proposal

10x/1s policy rejected by user and superseded. Accepted latest design targets1s
common baseline-driven request batches (cap20k, bounded calibration<750ms), short
warmups,3self/5paired quick with4agreement; meaningful20% regression budget and
50ms batch detectable floor/count. Existing calibrated budget bytes remain.
Large64x4x2x4 Rust full-page admin/member workload enters paired mechanism, no
invented allocation calibration. Live+replay injected25-50% regression must fail;
actual duration/count/signal receipts required.30s runaway safety supplementary,
all workloads. No endless retries/mandatory weekly precision campaign.

## Outcome

HaveAPI0.30.2 is published and verified on RubyGems, npm, PyPI, GitHub and
Packagist. Master fixes enteredmaster39e98020 first; finalmaintenance321ce825
contains exact-xbackports and separate.2metadata. PHPmirror a02dd250 is the
exactoriginaltagartifact. See state.md and tag-v0.30.2/publication-final-receipt.json.
No remaining release work. Session stays open without lifecycle/cleanup action.
