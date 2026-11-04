# Phase 2 final committed documentation review packet

Outcome: institute the user-approved client synchronization and release rules after all three Phase 1 releases are public. All intended changes are committed; quick checks pass. No runtime, API schema, generated output, dependency, package version, workflow, script or deployment changes.

## Exact repository ranges and full series

### vpsadmin / master

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin`. Clean exact head independently checked by lead.
Base `942c6eaed41331f823d8e0f670ed239e2b308440` -> head `4ac49f49e63545200df8afa920c6eafda8722523`.

Complete series:

4ac49f49e63545200df8afa920c6eafda8722523 docs: require generated client synchronization

Final diffstat:

```text
AGENTS.md                 |  1 +
 docs/api-schema-export.md | 72 ++++++++++++++++++++++++++++++++++++++++++++---
 2 files changed, 69 insertions(+), 4 deletions(-)
```

### vpsadmin-go-client / master

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-go-client`. Clean exact head independently checked by lead.
Base `7bc136e1d72f15174229bea2bb7de284174512f2` -> head `af9a819ca35f6de5556092679b4df7cb72e7aa89`.

Complete series:

af9a819ca35f6de5556092679b4df7cb72e7aa89 Link Go maintenance to generated-client synchronization

Final diffstat:

```text
AGENTS.md | 4 ++++
 README.md | 5 +++++
 2 files changed, 9 insertions(+)
```

### vpsadmin-rust-client / main

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-rust-client`. Clean exact head independently checked by lead.
Base `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f` -> head `823a4f8450fce4947310fc81bcdebdca91d9ffae`.

Complete series:

823a4f8450fce4947310fc81bcdebdca91d9ffae docs: link generated-client synchronization requirements

Final diffstat:

```text
docs/development.md | 14 +++++++++++++-
 1 file changed, 13 insertions(+), 1 deletion(-)
```

### vpsadmin-typescript-client / main

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-typescript-client`. Clean exact head independently checked by lead.
Base `c53cb4dabb0b3aac8d05834478872d2cfa698fa7` -> head `2da950a98fa13468b36d03b13fb5e81cca206e0e`.

Complete series:

2da950a98fa13468b36d03b13fb5e81cca206e0e Document generated client synchronization and release version policy

Final diffstat:

```text
docs/development.md | 6 ++++++
 docs/releasing.md   | 6 ++++++
 2 files changed, 12 insertions(+)
```

### haveapi / master

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/haveapi`. Clean exact head independently checked by lead.
Base `f29c1e4675bc1f79641faa619b8c68ecec923c71` -> head `dd200cc862b402c31f68a230de990de083efe306`.

Complete series:

dd200cc862b402c31f68a230de990de083efe306 docs: route vpsAdmin downstream client synchronization

Final diffstat:

```text
AGENTS.md                             |  1 +
 doc/agent-instructions/development.md | 18 ++++++++++++++++++
 2 files changed, 19 insertions(+)
```

### vpsadmin-webui / main

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-webui`. Clean exact head independently checked by lead.
Base `1c8478bceb3943645ec06ccde895ee4b0985873f` -> head `85f4f8e3820a1063058de9e12b1131eba486628f`.

Complete series:

85f4f8e3820a1063058de9e12b1131eba486628f Document the generated SDK release prerequisite for WebUI changes

Final diffstat:

```text
AGENTS.md                                          | 11 ++++++++++
 WORK_LOG.md                                        |  6 ++++++
 docs/design/HAVEAPI_CLIENT.md                      | 19 +++++++++++++++++
 .../2026-11-03-generated-sdk-release-rule.md       | 24 ++++++++++++++++++++++
 4 files changed, 60 insertions(+)
```

### workspace / master

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/workspace`. Clean exact head independently checked by lead.
Base `7205352c95218562fe0b37dff8b4a3dbf0962eec` -> head `c39ba90b81cd0e1cc3adfe8b728340445100b806`.

Complete series:

c39ba90b81cd0e1cc3adfe8b728340445100b806 Route vpsAdmin client checks through the canonical sync procedure

Final diffstat:

```text
docs/agent-instructions/projects.md     | 3 +++
 docs/agent-instructions/verification.md | 6 ++++++
 2 files changed, 9 insertions(+)
```

## Scope, ownership and acceptance

Read plan.md, design.md Phase 2 execution brief, and the four owner packets: phase2-vpsadmin-packet.md; phase2-go-workspace-packet.md; phase2-rust-haveapi.md; phase2-typescript-webui-review.md. Each repository has one coherent docs/instructions commit. No repeated pin/generated streams, superseded implementation or migrations; require independent whole-history/no-migrations conclusions. Phase 1 commits/tags and artifact receipts are immutable and outside new content scope.

Five required scenarios: (1) API schema/output changes assess Go/Rust/TS and update their remote defaults before task completion; (2) unchanged/behavior-only results need evidence against exact API/schema/profile/generator/client identities; (3) ordinary sync alone requires no publication; (4) dependent WebUI merge needs a published matching generated TS SDK, final registry manifest/lock/provenance, no temporary dev override; development feature deps allowed; (5) TS release defaults next minor unless user explicitly specifies version/bump. Distinguish backend availability/permissions and source freshness from saved-input reproducibility. Preserve separate explicit integration/publication/deployment authorization, bounded noncircular integration and no indefinite client follow-up.

Canonical home: vpsadmin docs/api-schema-export.md#generated-client-synchronization, unique heading line101 at committed head4ac49f49, SHA256109f3830f889d61785c17831b795ee3a611f624c3a4a25c0707eada31b3c53c2. Consumers verified exact committed candidate/meaning, public default anchor still prospective. Thin repo-specific links, no copied full workflow or claimed automatic freshness enforcement. No new CI framework. Export safety instructions preserved. Independent export repeat required when exporter/fixture/profile/tooling changes or determinism unestablished, not an unconditional second DB run for every behavior-only change.

Main lead directly applied vpsfree-user-facing-writing/humanizer-en to all new prose before commits; final minor wording corrections retained factual content and machine-significant links/headings. WebUI dated work-log/index required by local repo, stable workflow-status wording avoids claiming review passed before it ran.

## Quick checks and remaining CI

All feature trees clean, exact heads/series/whitespace independently rechecked by lead. Owner local links/anchors and canonical meaning checked; Go command fences unchanged; workspace unique project entries and routing; Rust/HaveAPI links and mandatory hooks; API normal Nixfmt/MigrationSpecs/WebUI+API I18n and commit-message hooks pass. HaveAPI required hook setup51s and normal I18n precommit passed; no bypass. WebUI locked setup+audit:design-docs passed23s,178 documents/76 requirements; scoped96link checks. Missing TypeScript module first audit was setup-only, fixed with normal locked npmci; no app/pin changes.

No long runtime suites selected for these prose-only patches. Go/workspace already feature-published, no workflows. Other feature pushes held before final review because native CI may run broad jobs on AGENTS/docs: Rust full unfiltered matrix; HaveAPI doc/server/performance selection; vpsAdmin API/i18n matrices; required WebUI PR has CI+Playwright smoke. These automatic runs will be observed after review; no optional manual dispatch or workflow edits. WebUI requires a scoped draft PR by its local instructions; no PR yet. No default integration approval for Phase 2 is implied by earlier Phase 1 client approval.

## HaveAPI lineage and workspace baseline

HaveAPI original registered initial base1ef9b204ba45bb261d3334be5c555cc1856b713b is a nonancestor public generator source pin, NOT claimed merged. Native detached dependency worktree haveapi-generator-0.32.2 and public v0.32.2 preserve it; original receipts/manifest initial_base retained. Genuine useful docs commit old1ef..37a8680f507e3f4cc0a65352b9ae06940d902123 was transplanted ONLY onto fresh masterf29..dd200cc8. range-diff equals, patchid0f87a79ec7c6a48e71b56c7b646b0674e5575f78 identical. No version/source-release commit replay or fake merge/unregistration. Final actual docs head must genuinely merge under new approval. Explicit final comparison captured at new base/head.

Workspace actual shared-target feature range7205352..c39ba90 is one9-line docs commit; root master/index and unrelated changes untouched. Native immutable saved comparison succeeded via supported capture command with public base6383e8848c92c06a9d817f8109853b5b61305c89..c39ba90 and label Merge base with locally available origin/master. Explicit720 replacement refused as different capture; existing valid record preserved. Lead path/meta-only diff6383..720 excluding work/archive/notes is EMPTY: intermediate shared trunk content is coordination records, exempt from feature-content review. Do not read peer records. Review actual1commit docs patch and confirm public/shared ancestry metadata. No private helper/metadata overwrite/artificial history rewrite. Shared workspace integration later requires fresh master plus tracking lock inside its short repository claim.

## Reviewer selection and lanes

Independent retained reviewer0, gpt-6.1-sol/xhigh/read_only; verify live same-session roster and exact identity, no override/fallback/nested agents. Read mandatory-change-review and applicable references. Medium overall: bounded reversible cross-project contributor instructions, no software/state change; lanes general (history/docs), architecture (one authoritative cross-project procedure and consumers), scope (cross-repository capability), risk/compatibility (instructions govern integration/publication order and backend readiness). All intended deliverables committed and quick-passed before review. Inspect actual full series, not just final trees or owner assertions; user correctly challenged mixed Phase1 TS history, so logical commit boundaries must be enforced. Return concrete severity findings and explicit obsolete-history/update-stream/migration conclusions. Do not run tests/builds or edit source; return report text for lead to save. No approval to merge/release/deploy/lifecycle.

## Post-review readiness updates

The original packet above is preserved as reviewed. Final independent review
found no findings; see [phase2-review-result.md](phase2-review-result.md), including
two workspace-only general/history addenda. Other six exact ranges are unchanged.
Current accepted workspace range is
`d56f24d9a84b2b2ffa2b8c4833179652016a1f2c..80ec8e0d053e0ab7e202092791b59b4edb63ea55`.
Both rebases preserve the identical one-commit policy patch and preserve earlier
reviewed ranges. Final tree `55442c378a125d8843b904a4cdcb8762fee961f7` was
independently reconstructed by lead and reviewer.

All features are published. Required WebUI draft PR is
https://github.com/vpsfreecz/vpsadmin-webui/pull/127 at exact reviewed85f4f8e.
Nine native workflows are being observed by one fresh Luna/low utility, with
seven successes and two still running at the last checkpoint; exact identities
are in [phase2-ci-runs.json](phase2-ci-runs.json). No manual runtime suites or
workflow changes were added. No Phase2 default integration approval yet.
