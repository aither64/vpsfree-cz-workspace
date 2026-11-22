# Implementer1 plan presentation checkpoint

Active package, not complete. Isolated worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace-pi-plan-presentation`.
Branch `2026-11-11-pi-codex-migration-pi-plan-presentation`, literal base
`42acdec08d4f24ea38574ef0a93c3beec3bad56a`/tree7c875. Supported
`dev-session worktree add ... --name dev-workspace-pi-plan-presentation --branch ... --base42 --no-fetch`
completed/joined87270 and registered new alias; old R registration and tree untouched.
Never edit/run mutation in old roster-preflight-fix R or frozen C/W/H refs.

Read full accepted design18023-18187, revised retention18084-18103 and18195-18243,
and accepted completion amendment18246-18331. Main supplied final status strings
and docs prose in latest assignment. No pending design blocker. Original held
request investigation is architect/main-owned; no live reads/actions by implementer.

Current WIP (no source commit/staging/check batch yet): pi_plan.go adds optional
per-proposal HTML via renderTextMarkdown port; pi_workflows.go supplies real
server renderer. Web-only wrapper preserves full Snapshot/text/IDs/digest; no
store/controller/native/schema change. pi_plan_test.go adds actual two publications
and captured acceptance, sanitized markup/exact CRLF Unicode/order/plain fallback,
private bytes and policy/mode no-effect proof. Needs gofmt and finite quick batch.

app.js extracts existing sanitized-HTML/plain-text/table DOM helper, injects it
through createPiWorkflowPage, imports pi-workflow-ui.js?v=2, gives new proposals
root and reuses existing ResizeObserver for normal follow. session.html uses same
compact action markup for both backends and separate plan-proposals inside
conversation scroller/outside entries+composer. style.css adds uncapped body styles;
session template app?v78/style?v29. Need inspect other affected cache refs.

pi-workflow-ui.js reuses common Implement/New/Keep nodes, hides unsupported Pi New,
renders every proposal in stable scoped tuple-keyed articles, no fake history. Old
bodies survive dismiss/capture/accept/amend/refresh; destroy clears only scoped
content and retains shared static bar markup. Each receipt uses exact tuple and
original acceptance ID; lookup only existing API. Consent visibility separates
unattempted decision/capture-inflight from settled receipt. Main-authored phase
strings applied. Controller pi-plan.js untouched. Review status/check loading and
error projection source carefully; no new native behavior permitted.

UI quick fixture currently partially updated: FakeElement IDs/query helpers,
common plan bar and new proposals root; old pre assertions replaced; teardown
expects static bar retained. Need complete phase/local unknown/retention/remount,
read error/stale/exact lookup tests and actual composer wiring. Also extend existing
pi_workflows_browser_test.cjs only if relevant (complete existing small suite runs).
Prepare desktop/mobile Codex/Pi presentation case in existing TestQuestionBrowser/
question_browser_test.cjs BEFORE committed review, but DO NOT execute hydrated run.
Source-fit its exact env flag/selector/dependencies first.

docs/pi-questions.md: main stale intro/Native ports and publish_plan versus policy,
retention/composer/phase paragraphs applied. Remaining stale integration sentence
has an extra redundant gate phrase to clean. Existing identity sentence says
digest of exact "displayed" bytes, which may need main-approved "original" wording
now display HTML differs; report factual copy mismatch before silently editing.

Next: finish meaningful fixtures/browser preparation/docs/cache, bind Nix shell to
THIS isolated worktree (not original R), derive pinned CODEX_WEB_SOURCE via flake,
one finite declared Go -mod=readonly + complete two small JS suites + syntax/cache
batch. Read fake/SDK gates before execution; no skipped coverage accepted. Use
fresh installed Luna/low utility if uncertain duration; known quick inline.
Preserve failures; rerun only affected scopes after concrete fit. Normal focused
commit(s) with hooks, clean/index-empty release and compact full-series provenance
from prior complete116/9241 plus literal42. Main invokes retained review before
any long browser. No push/pin/CI/build/deploy/lifecycle/real target action.

Guidance: identity current verified, vars absent; roster68 Sol/xhigh/workspace_write.
Root/Repo AGENTS, full brief and owning pi-questions docs read; sessions, Git,
commits, verification, documentation, team, monitor procedures from same context
reused unchanged; KB and lifecycle read for worktree registration. No utility/check
currently active. All team message handles50318/39863/93266 and creation87270 joined.
Reporting connector refuses retained identity; authorized same-session CLI fallback
from implementer1 with new stable message UUID, exact retry, serialize slug commands.
