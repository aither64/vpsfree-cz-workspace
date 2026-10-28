---
lifecycle: archived
---

# HaveAPI release versioning correction

## Current result

Requested implementation and integration are complete. HaveAPI remote `master`
and retained feature branch both point to the exact reviewed final head
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`; master VERSION is `0.31.0`.
All local checks, independent final review, eleven feature CI workflows and
eleven new master CI workflows passed. No blockers or remaining implementation,
review, verification or integration work. Session remains open; no lifecycle
operation or cleanup was requested or performed.

## Phase checklist

- [x] Investigate the master/release mismatch and record evidence.
- [x] Accept user's policy: master X.Y.0, patch versions on release branches.
- [x] Implement metadata, guard, fixture repair and owning release documentation.
- [x] Pass quick checks and declared hooks; commit complete intended changes.
- [x] Independently review full history/diff, consolidation and migration lineage.
- [x] Pass broader local tests; publish exact reviewed feature; pass feature CI.
- [x] Record explicit HaveAPI/master integration approval.
- [x] Fast-forward, SSH push, prove exact remote head and release merge claim.
- [x] Pass all new master-push CI and verify exact final integrated ancestry.
- Deployment/new package publication: not requested or performed.

## User scope and team

Initial request: investigate why master remained 0.30 despite released 0.31.
User corrected the first proposal: master carries the latest major/minor base
with patch zero; release branches own patches. That policy superseded the initial
full-version floor/0.31.2-on-master proposal before implementation. User then said
"implement it" and, after verified delivery, "all right, merge it", authorizing
HaveAPI / refs/heads/master integration only.

Exact session/environment binding verified for
`2026-10-28-release-versioning-audit` in `/home/aither/workspace/ai/vpsfree.cz`.
Architect0 (Astra/xhigh) owned investigation/design; implementer0 (Sol/xhigh,
workspace_write) owned the complete execution package and follow-up checks;
reviewer0 (Sol/xhigh, read_only) independently reviewed all four required lanes.
Fresh pinned Luna/low utilities monitored dependency preparation, check batches,
feature CI and master CI. Lead owned acceptance, writing, records and the approved
merge claim/critical section. Member settings were retained; no member added,
replaced or reconfigured. The single narrow package needed no second implementer.

## Repositories and exact history

Canonical: `repos/haveapi.git`, `git@github.com:vpsfreecz/haveapi.git`.
Registered branch: `2026-10-28-release-versioning-audit`, target `master`.
Feature worktree: `worktrees/2026-10-28-release-versioning-audit/haveapi`.
Prepared target: `worktrees/2026-10-28-release-versioning-audit/haveapi-merge-target`.
Both worktrees and feature refs are retained.

Base: `2f5156262baaf137800c17a9321e617c2b5df1d5`.
Final/integrated head: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.

1. `29fae9e00bdc0f340196cda953c5c7b2408aec21`: maintenance fixture isolation.
2. `ae909bef9ee27d01d5497f4b511e27b72f6dd60e`: coordinated 0.31.0 metadata/notes.
3. `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`: master-version policy enforcement.

24 files +375/-51; final comparison saved before integration. Independent review
found no obsolete history, repeated update streams, external dependency/action/
Nix input updates or migrations. Released c9124da1 fixture adaptation is a content
port with master's necessary optional Rust setup retained, not literal original
release-commit ancestry. No rebase/equivalence substitution or source follow-up
after review. Fresh remote proof at 11:41:28 UTC shows master and feature exactly
at final head; fetched origin/master agrees and exact-head ancestry passes.
Feature checkout is clean; lead rechecked the fetched refs, ancestry and VERSION.

## Checks and review

Full evidence: [implementation-evidence.md](implementation-evidence.md).
Independent report: [review.md](review.md); packet: [review-packet.md](review-packet.md).
Reviewer found no Blocking, Important or Advisory findings across general,
architecture/repetition, scope/proportionality and risk/compatibility. Risk was
classified conservatively high for publication-gate/recovery correctness.

- Quick checks: 65 metadata/policy and 18 lineage examples, changed-Ruby lint,
  Overcommit hooks, committed check-clean/check-clean --master/release-check pass.
- Broader local checks: 236 release Ruby examples, six Python tests and
  172 deterministic performance examples pass (143-second batch).
- All eleven feature CI runs pass, including full packaging/component tests/
  smokes and measured quick performance, 14/14 cases.
- All eleven NEW master push runs pass on the exact final head, event created
  2026-10-28 11:31:52 UTC, completed 11:39:45 UTC (7m53s).
- [Master release build](https://github.com/vpsfreecz/haveapi/actions/runs/40680667625)
  verifies the master event routes to check-clean --master and reports metadata
  valid at 0.31.0. Packaging/tests/smokes pass; publishing is skipped.
- [Master performance](https://github.com/vpsfreecz/haveapi/actions/runs/40680667726)
  compares actual pre/post merge commits: 14/14 cases and 14 each wall-time,
  CPU-time and allocation classifications pass; zero inconclusive/no-work cases.
- No CI failure, retry, cancellation, unexpected kernel build or active run.

Initial unsigned-hook setup was resolved through inspected normal Overcommit
installation/signing, without bypass. An initial lineage NameError was diagnosed
as loss of master's optional Rust constant setup; preserving it before maintenance
overrides fixed the test. The corrected run and later suites pass. Failure and
successful rerun logs remain in implementation evidence. No blind retry.

## Integration and resource release

[Integration receipt](integration.md) records approval, selected package/catalog,
prepared target/hooks, exact critical-section checks, commands and remote proof.
Claim `897accbe-acc0-4d47-91a8-5f5682d2482c`, owner
`fe298727-7c7c-46c0-9ca8-b4086616205f`, held only HaveAPI from 11:31:15 UTC.
Normal fast-forward and non-force SSH push succeeded with hooks. Exact local and
remote effects were reconciled; authoritative held status checked before release.
Release and subsequent authoritative released-state proof (revision 2) completed
at 11:32:05 UTC, before records or CI. No claim remains; no machine reservation.
No merge conflict, hook intervention or uncertain command effect remains.

## Documentation, compatibility and tracking

HaveAPI `doc/agent-instructions/releases.md` owns the master-first major/minor
process, patch-branch policy, detached master checks, fresh refs and original
published-artifact recovery. Lead checked restored notes/errors/policy using the
user-facing-writing skill; no editorial rewrite was needed. Existing tags,
packages and their original recovery tooling were preserved. No API, protocol,
schema, persistent-state, fleet or configuration change; source package identities
and constraints advance together. [Plan](plan.md) and [design](design.md) retain
scope and rationale; raw logs/artifacts are disposable supporting evidence.

Initial tracking commit `abdc82d25f893f39d53b9e093a511cc58ad3707a` preceded code
commits. Later tracking updates remain in the working tree under the normal
short-session cadence. Only owned records were edited; shared master and unrelated
work were preserved. No session archival, deletion, stop, finalization, worktree
removal or delayed cleanup was performed. No further action is required for the
requested correction and merge.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-release-versioning-audit/).
