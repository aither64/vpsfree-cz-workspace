# Scope and proportionality review

Lane: scope and proportionality. Reviewer model/effort: gpt-5.6-sol,
`xhigh`. Reviewed the complete committed series at the packet's exact bases and
heads in `codex-web`, `dev-workspace`, `vpsfree-dev-workspace`, `workspace`, and
`vpsfree-cz-configuration`, including the initiative plan/state, repository
guidance, commit series, implementation, tests, documentation, and dependency
pins.

## Findings

### Important: the required comparison capture is scoped away from workspace feature integration

Commit `38988f6e856757d93aa878c6b9680ade24db7789` adds the final comparison
capture rule only under "For feature work in the independent project
repositories" (`workspace/AGENTS.md:118-137`). The same file explicitly says
that the preceding top-level workflow is complete for workspace changes and
that the later rules apply only to independent repositories
(`workspace/AGENTS.md:55-87`). The workspace-specific flow therefore still
goes directly from final rebase/review to `git merge --ff-only` without the
capture (`workspace/AGENTS.md:65-74`).

This leaves one of the five current registered consumers outside the policy
that the review packet says must require final capture. An agent following the
workspace instructions can integrate a final workspace head without running
`capture-comparison`; after the default branch reaches that head, the portal
can only use an incidental automatic observation or the original-base fallback
(`dev-workspace/portal/internal/repository/review.go:243-291`). A rebase can
make that fallback differ from the intended final comparison, which is exactly
the failure the new workflow is meant to prevent.

Add the explicit capture command, including the requirement to repeat it after
any head change, to the top-level workspace feature workflow before its
fast-forward integration step. Keep the independent-project rule for the
separate bare-repository workflow.

## Proportionality assessment and residual gaps

The remaining mechanisms are supported by current consumers and the accepted
contract: the optional App Server flag delegates indexed lookup to Codex while
workspace-specific consistency policy stays in `dev-workspace`; the receipt
projection and tab-local draft preserve the requested creation state; the
cluster cache, busy result, concurrent shutdown, and bounded timeouts address
the observed multi-window and cumulative-shutdown failures; and explicit plus
supplementary comparison capture uses the existing private store without a new
session schema. The commit split is coherent, and no obsolete implementation
branch, speculative compatibility shim, broad lifecycle redesign, or
disproportionate test suite was found in the reviewed heads.

Long browser, packaged, and live cluster checks remain appropriately deferred
until the mandatory review findings are reconciled. This lane did not run them.
