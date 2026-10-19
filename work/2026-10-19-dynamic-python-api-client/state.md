---
lifecycle: active
---

# Dynamic Python HaveAPI client

Phase: implementing required independent-review corrections.
Implementation and quick checks pass; long integration, CI and publication remain.
No merge, release, deployment or session closure is authorized.

## Phase checklist

- [x] Verify identity, retained roster and workspace/repository guidance.
- [x] Architect design and concrete implementation contracts.
- [x] Implement sync/async client, tests, tooling, docs and publishing workflow.
- [x] Consolidate complete history and pass final quick checks.
- [ ] Independent final review and accepted remediation.
- [ ] Generic server, standalone package and real vpsAdmin integration.
- [ ] Publish feature branch and resolve CI.
- [ ] Ready for use; merge and actual registry release remain separately gated.

## Current branches and evidence

HaveAPI worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi`

- Branch: `2026-10-19-dynamic-python-api-client`.
- Base/fetched origin/master: `c58704a08451a231fdf6c6123437133422af46dc`.
- Final review head: `05e6236c7a9570d51f4330183141ff3ac290e9b1`.
- Tree: `28e19ad0a6b4e5f4615ac63422ce7167555edbd6`.
- Seven logical commits; 60 files +9583/-17. Clean tree/index, diff check passes.
- Complete series/consolidation/dependency/migration inventory in
  [review-packet.md](review-packet.md). No migrations or published consumers.

Read-only vpsAdmin reference worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference`

- Branch: `2026-10-19-dynamic-python-api-client-vpsadmin-reference`.
- Base/head: `fb2f51222503a45f2e5a42af505f719e44279ed0`; source clean.
- Declared API environment dependencies installed. HaveAPI released 0.29.12
  verified; api/Gemfile.lock SHA256
  `6739fbace7ff7d723c3e5e5fb0ae3aa8c4369d67c7cc7eef9604edca7d9f36e4`.
- No database/HTTP integration run yet; no node VM needed for API-only checks.

## Verification completed

Final reviewed-head quick checks, reported by implementer1 and accepted by lead:

- `nix develop .#client-python -c clients/python/utils/check.sh`: locked sync,
  Ruff formatting/lint 36 files including release helpers, strict mypy 18 source
  files, 187 unit tests pass (1.14s).
- Top Nix `make release-check release-test`: shared 0.29.0 metadata, 34 RSpec
  examples (1.18s), six offline artifact-validation tests (0.026s) pass.
- RuboCop seven owned Ruby files, shim/bridge syntax and shell syntax pass.
- All commits pass normal hooks; signature verification remains enabled.
- Generic integration ten cases and vpsAdmin five scenarios collect without
  running server/database fixtures. Examples import with network disabled.
- Genuine public vpsAdmin subset fixture parser passes; provenance includes
  URL/time/pruning and original/derived hashes, no authenticated data.

## Independent review

Assigned reviewer0 at exact final head, verified ready/independent/read-only,
`gpt-6.1-sol` / saved `xhigh`, thread
`01a155f8-f45b-72c3-97c3-a6149b4b489d`. Reviewer confirmed identity/guidance and
all four lane references. Original-head review completed through lead messaging;
faithful lead summary in [review.md](review.md), full report in conversation.

Changes required: Blocking R1 HTTPX query order, R2 DELETE JSON, R3 shared auth
policy; Important R4 lossless GET boundary, R5 no-show binding; advisory
unknown-type wording. Lead accepts all fixes, no finding waived.

Architect settled server-authoritative JSON DELETE and GET lossless whitelist
with real Rack evidence, no server/protocol changes. impl0 owns R2/R4/R5;
impl2 owns R1/R3; impl1 owns actual generic GET/DELETE/Rack regressions and
boundary documentation. All granted edits, no Git slot until single all-source
readiness pause. Changed public encoding boundary receives affected-lane
rereview after committed quick checks; narrow binding fix directly inspected.

Original review independently accepted full seven-commit history/consolidation,
no repeated dependency stream/obsolete scaffolding and NO MIGRATIONS. No feature
version merged/released/deployed/externally consumed. Release/package source
review found no other must-fix; actual registry/OIDC proof remains unperformed.

R1/R3 source corrections ready: impl2 reports 65 focused tests (0.71s), Ruff five
changed files, strict mypy six C source files. Lead inspected shared raw-query
and ClientState helper diffs; exact narrow fixes match plans. Actual installed
Rack parser on final HTTPX bytes confirms two original rows/Unicode values.
impl2 paused, no Git; core/docs owners still finishing.

Reviewer's one-line Rack check through a development shell unexpectedly started
ignored dependency setup, immediately terminated; no server/integration launched,
original source/index/head stayed clean. Further review avoids setup hooks.

Risk high (auth, credentials, untrusted discovery, public protocol, registry
workflow). Lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility, plus explicit whole-history and no-migrations conclusions.
No long integration launched before this review. Narrow direct fixes are
inspected/tested by lead; rerun only affected lanes when design/boundary changes.

## Backlog and owners

| Owner | Next result | Acceptance/dependency |
| --- | --- | --- |
| reviewer0 | Independent final findings/history conclusions | Complete base-to-head and four lanes; read-only |
| implementer0 | Core/response/paging/operation findings if any | Own source/tests/focused checks/commits |
| implementer2 | Facade/auth/vpsAdmin bridge findings if any | Own source/tests/focused checks/commits |
| implementer1 | Tooling/generic harness/release findings if any | Own source/tests/checks/commits; serialize Git |
| implementer3 | Bounded examples/fixture fixes if any | Exact owned files, saved low effort |
| architect0 | Material design deviations if any | Design record, no application edits |
| lead | Accept reports, tracking, final prose, verification/CI coordination | No source takeover; preserve explicit merge/release gates |

impl0/1/2 are implementing exact review corrections; impl3 is idle.
Git/snapshot commits await all-source readiness; no long integration yet.
User authorized implementation and explicitly added implementer2/3; retained
settings unchanged. Identity verified against thread/environment exact binding.

## Next actions

1. Complete assigned R1–R5 fixes, focused checks and source-ready pause.
2. Commit/fold fixes into owning history and run affected-lane rereview.
3. After review acceptance and clean checked commits, run
   [run-verification.sh](run-verification.sh) through a fresh policy watcher with
   exact reviewed head. It covers actual generic Ruby server, standalone wheel/
   sdist builds and installs, release regressions, guarded actual vpsAdmin HTTP.
4. Fix failures with owners; do not rerun unexplained failures blindly.
5. Publish feature branch over SSH and monitor exact-head CI, then report
   readiness and remaining PyPI setup. No merge/publish-version authorization.

Watcher policy resolved from matching retained/installed catalog digest
`ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`:
`gpt-6-luna`/low, fresh operation, full_access, native utility
`dw_91978c240a6a43c2168b5be643cb58668a0bdf42d703ed0e`, danger-full-access/never.

## Documentation and retained recovery

- [plan.md](plan.md), architect [design.md](design.md), API-only
  [verification-plan.md](verification-plan.md), [review-packet.md](review-packet.md).
- Owning project docs: clients/python README/CONTRIBUTING, root README link,
  development/release guidance. Lead applied required writing pass and reconciled
  vpsAdmin hierarchy, credential handling and synchronous deadline limitation.
- [implementation-checkpoints.md](implementation-checkpoints.md) preserves prior
  implementation/history/hook recovery details without crowding current status.
- Initial tracking commit `3471a1cb`; subsequent records kept under normal cadence.
- Backup feature ref retained at 841ee6b; final diff differs only approved
  three-line Ruff first-party declaration, verified. No ref deletion requested.
- Exact same-session Overcommit recovery stash
  `bd8d94b3b6f40a60a18aa4b30c03193459890495` retained. Narrow owned-path recovery,
  no repo-wide reset/clean/pop. Reusable note:
  `notes/haveapi/2026-10-19-python-uv-tools-on-nixos.md`.
- Session remains open. No lifecycle cleanup requested or performed.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/
