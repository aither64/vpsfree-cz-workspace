# Architecture and repetition review

Lane: architecture and repetition. Reviewer model/effort: gpt-5.6-sol,
`xhigh`. Reviewed the complete committed series at the packet's exact bases and
heads in `codex-web`, `dev-workspace`, `vpsfree-dev-workspace`, `workspace`, and
`vpsfree-cz-configuration`, including repository guidance, provider and consumer
implementations, tests, documentation, and dependency pins.

## Findings

### Important: supplementary comparison writes can make repository reads and the required CLI capture fail spuriously

Commit `f371105cf1d19e8f7fa7fd09aced419e15478c3b` adds automatic comparison
observation to three independent read paths. The single-repository state API
returns an error when the observation cannot be saved
(`dev-workspace/portal/internal/web/repository_review.go:258-265`), the batch
state API reports a per-repository error
(`dev-workspace/portal/internal/web/repository_review_batch.go:83-95`), and the
session status path starts the same write concurrently for every repository
(`dev-workspace/portal/internal/web/server.go:913-925`). The shared writer calls
`flock(LOCK_EX|LOCK_NB)` and immediately returns `EWOULDBLOCK` when another
request or the CLI owns the lock
(`dev-workspace/portal/internal/web/repository_comparisons.go:74-98`). The
explicit `capture-comparison` command uses that same nonblocking writer
(`repository_comparisons.go:266-303`).

A normal portal refresh, repository-review head poll, and required pre-merge CLI
capture can therefore race on the same head. While one writer is fsyncing, a
second status request reports an unavailable repository even though Git is
healthy, or the explicit capture aborts and has to be retried. A transient
private-store write error also breaks the state API although the packet calls
automatic observation supplementary. This couples a best-effort durability
improvement to repository visibility and makes the required integration step
depend on background browser traffic.

Give explicit capture a context-bounded serialized writer (or an equivalent
retry), and keep automatic observation failure off the repository-read result
path while logging it. Prefer one owner for triggering background observation
instead of repeating it in the summary, single-state, and batch-state handlers.
Add a concurrency contract test covering automatic observation against an
explicit capture.

### Important: exit 75 is an undeclared cross-project cluster-provider protocol

The generic portal now treats any helper `status` exit code 75 as a successful
"changing" observation
(`dev-workspace/portal/internal/cluster/status.go:234-255`). The organization
helper produces that value through a literal `flock -E 75`
(`vpsfree-dev-workspace/dev-clusters/lib/runtime.sh:797-850`). Both sides have
focused tests, and the matched dependency pins are correct: organization head
`a23002ffe2e89f5ecbf35913d074fae2695c8c11` pins generic runtime
`f371105cf1d19e8f7fa7fd09aced419e15478c3b`; the workspace profile pins the
organization head; the configuration host module pins the same generic runtime
head.

The extension interface itself still declares only provider ID, label, and
executable. Its documentation says helpers own the `status` protocol but does
not define the special result
(`dev-workspace/docs/workspace-portal.md:79-104`). A future provider cannot
discover how to report a transition, and a helper that uses the conventional
temporary-failure exit code 75 for a real status failure will be silently
misclassified as a benign mutation. The behavior is consequently encoded in
two language-specific magic numbers instead of an authoritative extension
contract.

Define and document the provider status result contract in the generic owner,
including stdout/stderr requirements and the reserved busy result. Give the
value a named meaning in both implementations and keep the existing provider
and representative consumer tests tied to that contract.

### Important: shutdown safety depends on an unverified timeout hierarchy across three layers

The complete stop budget is repeated as related constants in separate
components: the Ruby runner allows 120 seconds for `stop` and ten seconds for
forced reaping
(`vpsfree-dev-workspace/dev-clusters/lib/devcluster_runner.rb:129-146`), the
shell wrapper waits 150 seconds based on those internals
(`vpsfree-dev-workspace/dev-clusters/lib/runtime.sh:463-471`), and the generic
portal kills the whole helper process group after 180 seconds
(`dev-workspace/portal/internal/web/server.go:1745-1780`). The focused runner
tests exercise injected short timeouts, but no executable contract checks the
default `120 + 10 < 150 < 180` relationship or accounts for the sequential
finalize/cleanup work after guest reaping.

If the provider later lengthens the graceful or forced phase at its owner, the
unchanged shell wrapper can kill the runner during reaping or cleanup; if its
wrapper budget grows, the generic portal can kill the reset helper first. That
is coordinated maintenance across a provider implementation, its shell
wrapper, and a generic consumer for a destructive operation.

Make the provider package own and test its runner/wrapper deadline relationship,
and declare the maximum release duration at the cluster-provider boundary (or
use a documented generic ceiling that does not mirror current provider
internals). Add a contract test for the packaged provider/consumer budgets so a
one-layer timeout change fails before deployment.

### Advisory: the pre-validation plan prompt duplicates the canonical prompt rule and already differs at the boundary

`creationReceipt.status` reconstructs a plan request with an inline string
concatenation
(`dev-workspace/portal/internal/web/creation_store.go:69-87`), while validation
constructs the same request separately and applies `normalizedCreationGoal`
(`dev-workspace/portal/internal/web/creation.go:499-510`). For an approved plan
ending in ASCII whitespace, the copy shown before validation includes those
bytes; after validation and in the goal passed through `dev-session`, the same
receipt shows the stripped form. The panel can therefore change the supposedly
retained initial request as initialization crosses validation.

Use one plan-to-initial-request function for both status projection and
validation, with a test that compares the pre-validation copy, validated
receipt, and submitted goal for boundary whitespace.

### Advisory: server and browser cluster-state presentation rules have already drifted

The server template gives the warning badge class only to `stale` state
(`dev-workspace/portal/internal/web/templates/session.html:108-111`), while the
refresh path gives it to both `stale` and `unavailable`
(`dev-workspace/portal/internal/web/static/app.js:1536-1545`). A real provider
failure thus renders differently on the initial response and after the first
details refresh. Derive presentation from one state value, for example through
a data attribute and CSS, so adding or renaming a provider state does not
require matching conditionals in Go templates and browser code.

## Residual validation gaps

The provider and consumer pins form the intended one-way dependency chain, and
the changed shared boundaries have focused tests on both sides. The pending
packaged creation browser acceptance and live matched provider/portal exercise
remain useful because this review did not run long integration tests. No
architecture finding was identified in the optional codex-web
`UseStateDBOnly` field itself: the generic provider owns the additive wire
option and protocol corpus, while workspace-specific index health policy stays
in its actual consumer.
