# HaveAPI 0.32.0 committed deliverable: final review packet

Requested outcome: prepare HaveAPI 0.32.0, then regenerate vpsAdmin Go/Rust/TS
clients and publish only clients with meaningful changes. User said `proceed`
after the plan. This review covers the completed HaveAPI preparation package;
SDK deliverables will receive their own final review when complete. No review,
CI or implementation approval grants integration/publication permission.

## Exact scope

- Session: 2026-10-30-haveapi-client-releases.
- Repository: haveapi; canonical SSH origin git@github.com:vpsfreecz/haveapi.git.
- Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/haveapi.
- Base/target: master at 7edb003dd5d5a058b3308510bb8a5f60387ad654.
- Final committed head: f0465630595b4fd120561337b3d1d7fa96cbe221.
- Complete series: one commit, `release: prepare HaveAPI 0.32.0`.
- Final diff: 18 files, +50/-17; coordinated versions/internal constraints and
  changelog only. Inspect actual full diff and history independently.
- Migration inventory: none; no merged/released/deployed/external migration
  lineage or temporary compatibility paths introduced.
- Repeated update streams: one synchronized version/internal dependency stream,
  one final update; no superseded pin commits or follow-up fixes retained.
- Commit grouping: coordinated release metadata and its changelog describe one
  release; no functional source fixes are bundled.

## Acceptance and verification

Read plan.md, design.md (including candidate-to-release correspondence),
haveapi-preparation.md and the exact HaveAPI local AGENTS/routed release and
development procedures. Source-of-truth raw quick/hook logs and identities are
linked from haveapi-preparation.md under haveapi-logs/.

Owner reports passing make release-deps, make version VERSION=0.32.0,
make release-check, explicit cli check-clean --master, git diff --check,
Overcommit pre-commit/commit-msg hooks, and postcommit check-clean --master.
All ten prepared external dependency graphs stayed unchanged; ignored library
locks remain untracked and retained as exact local verification inputs.
Lead inspected complete commit/stat/version diff and applied the required
user-facing writing skills directly to the changelog before commit.

Feature push intentionally deferred because release.yml runs the full release
build/test batch on VERSION pushes. No long integration/release tests have run;
post-review exact-head CI will supply that gate. Do not run long tests yourself.
Candidate is clean; SDK readers may use source/locks read-only, never mutate it.

## Compatibility and publication boundaries

Maintained Ruby gems, npm/browser client, Python wheel/sdist and PHP mirror share
0.32.0; Elixir excluded. Existing protocol stays 2.0 and SDK API stays7.0.
TypeScript SDK retains published runtime0.30.2; Go/Rust copy runtime. Generated
SDK payload/version decisions are outside this completed package review.
HaveAPI source already on master contains the docs/OAuth/examples/formatter
changes summarized in changelog; the previous v0.31.2 release has backport
ancestry. Inspect preparation evidence for release-delta coverage and avoid
claiming that v0.31.2 literally descends from current master.

No server deployment/configuration update is proposed. Optional docs OAuth
operator setup belongs in existing doc/documentation-oauth.md. Package pins,
input sources and final release source/artifact correspondence are in design.
No new persistence format, schema or coordinated node upgrade is introduced.

No default writes, tags, registry publication, PHP mirror writes or protected
environment approval authorized. Exact release candidate must receive full
release CI/package checks after review. Registry/environment checks so far do
not prove trusted publisher/deploy-key validity or reserve package versions.
Preserve tags/original retained artifacts in partial publication recovery.

## Independent reviewer and lanes

Risk: high, because this prepares coordinated public package releases and
cross-project internal constraints with later irreversible publication.
Selected eligible independent retained reviewer: reviewer0, gpt-6.1-sol/xhigh,
read_only, ready, exact saved settings verified without overrides.
Read mandatory-change-review SKILL.md and general, architecture, scope and
risk lane references. General covers metadata/changelog/history; architecture
covers cross-project dependency/version contract; scope covers minimal release
prep; risk covers package compatibility, artifact provenance and recovery gates.

Assess directly; report concrete findings/severity or no findings. Require
explicit full-series/history, repeated-stream and no-migrations conclusions.
No nested reviewer. Do not edit source or approve integration/publication.
Write haveapi-final-review-result.md and report_to_lead.
