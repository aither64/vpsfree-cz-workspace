---
lifecycle: archived
---

# 2026-11-12-api-language-evaluation

## Status

- Advisory evaluation delivered: Kotlin first for API/HaveAPI; Rust deserves a realistic comparison if broader language unification is important. C# is a close alternative. No rewrite decision adopted.
- Bound identity verified by dev-session current and matching environment markers. Session remains open for discussion.
- No application changes, feature branches, builds, deployment or integration.

## Phases

- [x] Verify session and scope; read required procedures.
- [x] Inspect representative component contracts and language tradeoffs.
- [x] Accept findings and give recommendation with practical evaluation path.

## Packages

| Package / deliverable | Owner | Dependencies / acceptance | Status / evidence |
| --- | --- | --- | --- |
| Bounded investigation; design.md | architect0 | Canonical repository evidence, current primary language references; decision-relevant shortlist and compatibility constraints | Accepted 2026-11-12 following explicit completion report and lead reading; assigned message 961ce8d2-0716-4f96-b478-86b625b81420 |

## Next actions

- Discuss preferred runtime and desired scope of language unification. A future Kotlin/Rust pilot is proposed, not authorized or started.

## Documentation

- [Plan](plan.md); [accepted investigation findings](design.md). This is investigation/planning, not a completed implementation or substantive project-documentation change requiring automatic final review.

## Repositories

- Canonical bare repositories only for read-only inspection; no registered feature worktrees.
- Examined local snapshots: vpsadmin b4ef8535a629ee8c9cd753afecdb05e0895d0eea; haveapi 7835acafdda19779815a0f1ba905d78e0085456d. Not asserted to be fresh upstream heads.

## Commands run

- dev-session current; matching DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE.
- dev-session team list 2026-11-12-api-language-evaluation --as-is: architect0 design/workspace_write, retained Astra/xhigh; four implementation members remain unassigned because no implementation requested.
- Assignment first rejected a non-UUID message ID before delivery; corrected with stable lowercase UUID above.

## Results

- Source sampling identified shared MariaDB transaction/confirmation contracts, signed command inputs and RabbitMQ communication; preserve these independently of language.
- HaveAPI replacement must account for authorization-filtered discovery and omitted/null/value input states, not only HTTP handlers.
- Lead checked current official Kotlin nullability/sealed/exception docs, Rust enum/Result docs, C# nullable diagnostics, Go FAQ and TypeScript type-compatibility/narrowing docs. Do not assert C# lacks unions: current docs include a version-dependent native union feature.
- Proposed future comparison: identical representative VPS Update workflow in Kotlin and Rust, including permissions, persistence, dispatch, confirmation, retries and rollback; no builds/tests were appropriate or run in this advisory investigation.
- Mandatory final change review not triggered by investigation/findings alone. No branch readiness, deployment or integration claimed.

## Open questions

- API/HaveAPI only versus broader control-plane unification; JVM/.NET preferences; plugin loading and client compatibility requirements; whether a measured pilot justifies rewrite investment.

## Cleanup

- No temporary services or machine claims. Leave session open.
