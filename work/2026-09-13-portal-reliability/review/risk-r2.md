# Risk and compatibility review rerun

Lane: risk and compatibility. Reviewer model/effort: `gpt-5.6-sol`, `xhigh`.
Reviewed the targeted remediation packet, commit series, repository guidance,
provider and consumer implementations, representative tests, package pins, and
the bounded auth-email recovery path. The workspace-only branch was rebased
without an implementation change after the packet was written, so the exact
reviewed workspace head is `037bf6873b0d013afa1bf90aa31093ff1584647c`.

Exact reviewed heads:

- codex-web `6335da93acdcc82cc26200d2fbc7f479655aa7c3`
- dev-workspace `3a1cd051826cf0dd16127f660ced9ef63aa6a51a`, plus the
  direct remediation `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a`
- vpsfree-dev-workspace `fcc63b20e194e200b56cf0d05b69244b8c4cc53a`
- workspace `037bf6873b0d013afa1bf90aa31093ff1584647c`
- vpsfree-cz-configuration `3de09ed5d43174712f41745ef7cc06b454f840e3`

## Finding

### Important, resolved: reset absence did not retire the provider's cached observation

At dev-workspace `3a1cd051826cf0dd16127f660ced9ef63aa6a51a`,
`portal/internal/web/server.go:884-890` skipped provider inspection when reset
had removed the provider state directory. That correctly rendered the complete
cluster section as absent, but it also bypassed the only
`StatusCache.observe(..., found=false, ...)` path that deleted the cached
observation (`portal/internal/cluster/status.go:102-121`). A successful
`releaseProvider` did not evict it either.

If the same session then started a new cluster, the recreated state directory
made `MayExist` true while the provider lock was held. Reserved busy exit 75
caused the cache to restore the previous running observation. Old readiness,
services, commands, and credentials could therefore reappear with the changing
notice for the duration of the new mutation, despite the intervening
authoritative reset.

Commit `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a` resolves the finding by
forgetting each provider whose state is authoritatively absent and forgetting
the released provider after successful reset. It checks every provider even
when another provider still exists. The regression covers running -> busy ->
absent -> recreated/busy -> stopped, and a separate provider test covers
per-provider eviction. This is a narrow cache-lifetime correction and does not
change the provider or persisted-state contract; focused cluster and web tests
passed.

## Other assessed boundaries

No other Blocking, Important, or Advisory findings remain in this rerun.

- The generic runtime owns and publishes busy exit 75 and the 180-second portal
  release ceiling. The organization package consumes that exact published
  contract, owns `shutdown.json` with 120/10/20-second phases, validates the
  150-second sum below the portal ceiling, and packages the budget file beside
  both the shared shell runtime and each provider runner. The Go portal and
  provider pins resolve to the same runtime head.
- The new contract fields are additive metadata. Old generic, Ruby, and shell
  readers ignore them; the new organization provider deliberately fails closed
  without the matching new runtime. Persisted cluster schema, transition policy,
  process ownership, and socket identity are unchanged. Existing old runners
  retain their loaded code and remain stoppable by the matched wrapper. Rolling
  back loses the improved presentation and concurrency but can still read the
  existing state.
- The shared server-rendered cluster template makes each details response
  authoritative for cards and absence. Browser replacement keeps the outer
  delegated handler, restores the selected service tab when it still exists,
  and continues to route copy, reveal, tab, and release controls through
  delegation. With the cache eviction above, a completed reset cannot later
  resurrect its previous credential-bearing observation.
- The bounded auth-email recovery remains compatible with the reviewed changes.
  The installed private CLI retains current profile generation and token
  validation and the shared transition lock; only its portal command points to
  the candidate Go binary. Existing receipt/evidence binding and journal goal
  digest preserve the accepted request, the creation lock serializes retries,
  and the initial-submission ledger prevents a completed send from being
  repeated. The candidate uses the authoritative upstream thread listing with
  the 180-second command allowance. Normal portal-driven creation nests that
  command under 210-second child-process and 240-second receipt deadlines,
  leaving 30 seconds at each layer for persistence and reconciliation. No
  index, rollout, or alternate identity data is consulted.

## Residual validation gaps

- Exercise the packaged portal and both packaged providers with real OSVM
  shutdown, forced reaping, cleanup, and the 180-second outer cancellation.
- Complete the planned browser/live cross-window run for running, busy, stopped,
  absent, and recreated states, including service-tab and delegated-control
  behavior after section replacement.
- During the one-time auth-email recovery, verify that the retained original
  request is submitted exactly once before performing the normal profile switch.
  Preserve the previous profile and system generations for rollback.
