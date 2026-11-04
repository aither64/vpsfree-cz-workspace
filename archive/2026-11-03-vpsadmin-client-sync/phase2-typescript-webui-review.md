# Phase 2 TypeScript and WebUI final documentation review packet

Complete committed package for lead-assigned independent documentation/history
review under mandatory-change-review. No feature publication/PR/automatic CI yet;
those follow this final review gate. No local broad tests or builds needed for
the prose-only scope.

## Requested outcome and boundaries

Architect-owned Phase 2 brief is [design.md](design.md), “Phase 2 execution
packages and acceptance”. Implementer2 owns TypeScript contributor/release
links and WebUI maintainer/design/work-log instructions. Canonical API workflow
belongs to implementer3; other language/workspace consumers belong to their
assigned owners. No API/SDK runtime, generated content, app/dependency/version,
workflow/test, WebUI WIP, deployment or integration change in this package.

Accept the five scenarios: API schema changes assess/update all clients through
the canonical procedure; behavior-only changes can retain source-tied no-op
proof; ordinary source sync does not require publication; dependent WebUI merge
requires an actually published matching SDK with registry manifest/lock/provenance
and no temporary override; TypeScript defaults to next minor with explicit user
version/bump override. Backend capability readiness stays separate. No automatic
CI enforcement claimed.

## Exact repositories, bases, heads and full unmerged series

| Repository | Phase 2 base | Final head / complete unmerged series |
| --- | --- | --- |
| `vpsadmin-typescript-client` target `main` | `c53cb4dabb0b3aac8d05834478872d2cfa698fa7` | `2da950a98fa13468b36d03b13fb5e81cca206e0e` — Document generated client synchronization and release version policy |
| `vpsadmin-webui` target `main` | `1c8478bceb3943645ec06ccde895ee4b0985873f` | `85f4f8e3820a1063058de9e12b1131eba486628f` — Document the generated SDK release prerequisite for WebUI changes |

Each has exactly one coherent documentation/instructions commit; no superseded
approaches, repeated input/dependency/generated update streams or migrations.
TypeScript's prior Phase 1 commits are released and merged, immutable and outside
the unmerged Phase 2 range. Plugin migration inventories are unchanged historical
provenance, not new migrations. No new branch head is externally consumed,
merged, deployed or published yet.

Worktrees under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/`:
`vpsadmin-typescript-client` (registered existing dated feature), `vpsadmin-webui`
(new registered `dev/vpsadmin-client-sync-rules`). Both clean. SSH origins are
canonical `git@github.com:vpsfreecz/<repository>.git`.

Complete scoped diffs:

- TypeScript: 2 files/12 additions, `docs/development.md` canonical sync link and
  saved-input/freshness boundary; `docs/releasing.md` minor default/override and
  release-free ordinary synchronization.
- WebUI: 4 files/60 additions, `AGENTS.md` conditional SDK release prerequisite;
  `docs/design/HAVEAPI_CLIENT.md` transport versus generated SDK and final artifact
  requirements; dated `docs/work-log/2026-11-03-generated-sdk-release-rule.md` and
  `WORK_LOG.md` pointer. Existing transport/runtime/version facts unchanged.

## Documentation ownership, writing and checks

Lead directly applied vpsfree-user-facing-writing/humanizer-en and approved exact
full prose before commits. It separately approved the final work-log passed-check facts and stable maintainer-workflow sentence and colon date heading; the audit parser uses ordinary ATX headings
and imposes no em-dash date format. No unapproved prose change followed.

Relative links/anchors: 96 existing/new scoped links passed; canonical external
URL is fixed to
`https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization`.
Owner3's ready candidate was read in full and unique exact heading verified:
`worktrees/.../vpsadmin/docs/api-schema-export.md`, SHA256
`109f3830f889d61785c17831b795ee3a611f624c3a4a25c0707eada31b3c53c2`, base942c6ea.
Final canonical candidate is committed at
`4ac49f49e63545200df8afa920c6eafda8722523` after the lead writing pass; its
unique anchor/hash and meaning were reconciled before consumer publication. Public default may temporarily lack the
anchor; candidate verification is not a claim of default integration.

Quick checks passed: both working/staged `git diff --check`; owned paths only;
WebUI actual Nix-context author/committer identity verified; no declared hook
framework/custom hooks path or active common hooks in either repository.
Ordinary hooks remained enabled; commits used wrapped messages from temp files.

Required WebUI `npm run audit:design-docs` passed after normal locked `npm ci`
through its pinned Nix environment, exit0/23s: 178 documents,76 requirements,
inventory257 routes/65 API modules. Fresh Luna/low utility with exact native
config/full-access-never binding completed; no operation remains and single slot
released. [Audit result](phase2-webui-audit-result.md),
[log](phase2-webui-audit.log), [status](phase2-webui-audit.status).
Initial audit failed missing declared TypeScript in fresh worktree; preserved as
[setup failure](phase2-webui-audit-setup-failure.md), not a source defect. No
source workaround or dependency change. Final changes after successful audit
only replace work-log status with true pass/stable-workflow facts and use a permitted
colon heading; whitespace/link checks cover those tiny edits.

The audit checks links/inventory/requirement mapping, not prose meaning, automatic
release-rule enforcement, API permissions, production compatibility or deployment.
No app tests/new tests, build matrix or manual workflow is justified by docs.

## Publication and integration gates

After independent final documentation/history acceptance, publish both feature
branches. WebUI AGENTS requires a focused PR; prepare a draft PR with REQ-060/068
and audit evidence. Automatic WebUI PR CI/Playwright smoke has no docs-only path
exemption and can be observed, but do not trigger broad/nightly/manual workflows.
TypeScript push starts its existing validation workflow. Use the single utility
policy for long/uncertain CI waits, or bounded final-result reads when already
complete. Preserve exact head/run identities.

All Phase 2 default integrations need fresh named-repository/target user approval;
Phase 1 approval does not cover these commits. No merge, default push, tag,
release, deployment, cleanup or lifecycle action is authorized here. Peers own
separate WebUI adoption and will refresh public main through lead coordination;
no peer WIP/preview/team inspected.

Final narrow work-log reconciliation folded unpushed WebUI head
`3dc264507d167208549e79a18a83d511592bbfe6` into
`85f4f8e3820a1063058de9e12b1131eba486628f`. Only four lines of transient status
wording were replaced with the lead-approved stable workflow sentence; checks,
links, headings and document count unchanged. Focused whitespace/link checks
passed, no audit/setup/suite repeat. TypeScript head remains2da950a.
