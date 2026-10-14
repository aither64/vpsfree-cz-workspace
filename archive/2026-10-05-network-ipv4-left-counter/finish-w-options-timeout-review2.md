# Independent committed issue30 review packet

Initiative:2026-10-05-network-ipv4-left-counter. This is the isolated W timeout
unit, not a certification of the unfinished K/E shutdown draft or real runtime.
The user authorized implementing issue30 while finishing this session.

## Requested outcome and accepted limits

Prevent stalled shared capability discovery from keeping free-IP suggestions
loading past their existing caller budget. One12-second budget spans metadata
and GET; expiry/cancellation settles the caller and prevents late work/results.
Shared capability discovery/cache continues for other callers. Explicit retry
gets a new budget and may rejoin pending shared discovery. Successful old-API
metadata keeps compatibility; metadata errors are never a fallback or empty pool.
Manual filters use their separate list. Per-query budgets are not a whole-page
12-second guarantee. Assignment discovery and shared adapter transport are
outside this fix.

Accepted detailed design:design.md4148, with the timing-only supersession in
finish-options-timeout-source-start1.json. Project contract/prose lives in
API_CONTRACTS.md, WORKFLOWS.md, REQ-050 and the dated work-log entry.

## Exact source and complete history

Repository:vpsfreecz/vpsadmin-webui; worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-timeout
Branch:dev/ip-suggestions-timeout, PR39 targets main.
Base7152729dcde326e00d16b5af0a46d0f60b431dbb.
Headcce681424b866f6a51cbc0a1e4daa226ed33fc07.
Treee0b483400db14813088ddfba35d31b0088b382ad.

The full base-to-head inventory, binary diff and fuller chronological history
are finish-w-options-timeout-review2.inventory.json / .diff / .history. One
logical owner commit includes the hook correction, its existing tests and four
owning documentation paths. No fixup, merge, superseded approach, pin stream,
compatibility shim, migration or persisted-schema change occurs. Earlier
availability PR19 was already merged; its history is preserved and is not part
of this branch delta. The initial freeze plus the two-path test-fix1 freeze match the committed
application; initial root prose remains exact. The initial untracked log moved
only in Git's diff ordering when staged.

## Owning consumers and scope

useProgressiveSuggestedIpQueries is imported by actual admin/IpAddressesPage.tsx.
It uses the existing shared QueryClient capability key and unchanged
ipAddresses API adapter. fetchAssignableIpAddresses is a separate direct
capability consumer and remains unchanged. Sampling/query plan, request limits,
server enabled filtering, local disabled guard, manual page, routes, dependencies,
locks, workflows, structural ledger/baseline, compiler adoption and catalogs
remain unchanged. The browser addition is in the already adopted
network_availability spec; deferred environment-filter spec remains unchanged.

There is no backend, auth, schema, allocation policy, deployment or KB-image
change. Older APIs still omit unsupported network_enabled after successful
metadata. Rolling back restores the older loading behavior without converting
data or changing query keys. QueryClient's observer/cancellation semantics remain
owning; local deadlines do not cancel/invalidate shared metadata.

## Verification gate

Hosted evidence is pending at packet preparation. Do not assign final review
until root appends native exact-head quick/source results. No local CI or suite
was run under the accepted user override. The two existing PR workflows select
ci:quick/ci:tests/build/Chromium-script and desktop/mobile smoke with separate
WebKit touch coverage. Browser results are synthetic fixtures, not live API or
PHP KB screenshot proof. The existing automated PR workflows are not new manual
VM/integration admission. Required committed review precedes any later real work.

## Review selection

Overall session risk remains HIGH; this bounded frontend unit is MEDIUM and
changes shared async/cancellation behavior. Assign retained independent reviewer0
Sol/xhigh/read_only without settings override, all four lanes:GENERAL,
architecture/repetition, scope/proportionality, risk/compatibility. Read the
mandatory-change-review skill and every selected reference; inspect code/tests,
actual QueryClient consumers and full history/migration inventory independently.
Do not execute tests, CI waits/reruns, source/tracking/Git writes, runtime or
lifecycle actions. Report concrete findings and precise evidence limits; state
whole-branch obsolete-history and no-migration conclusions.

The source review is not merge, deployment, cleanup or real-runtime acceptance.
Current K/E prospective source work and all incomplete retained campaigns remain
outside this packet. Root owns later finding disposition and operational gates.

## Prior exact-head failures and bounded correction

At the preserved failed447 head, CI37973893175 stopped at TypeScript checks
before units: QueryOptions does not expose staleTime. Smoke37973893363 failed
all four new EN/CS desktop/mobile cases before capability discovery while the
page clock remained paused. Root inspected native hashes/logs and the Loading
snapshot. The corrected tests check real cache expiry with retained query objects
and advance the clock in the initial poll. Product hook/adapters are unchanged
by this correction. Native passes at447 were build, Chromium script and separate
WebKit cases; they are not fresh cce results. See failure1 and test-fix1 controls.
Current cce checks and image production are pending; no final review assigned yet.

## Exact native quick gate available at assignment

CI37977641165 succeeds for cce68142: required quick checks, all296 unit files/
1794 tests, production build and Chromium script regression. The owning hook
file passes all28 cases. E2E type coverage47 checked/209 deferred is unchanged
in this patch. Existing act() and production chunk-size warnings remain.
Native checkout is the GitHub synthetic PR merge; its fetched Git object has
parents7152729d/cce68142 and exactly the feature treee0b48340. See
finish-w-options-timeout-ci2-acceptance.json for full hashes and object proof.
No local suite was run. Smoke37977641093 remains watcher-owned; its outcome
and images are not acceptance claims at assignment. Final source review can
proceed now; root retains the browser and operational gates separately.
