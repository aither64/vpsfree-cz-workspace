# Visibility review findings and dispositions

Reviewer0 completed all four lanes on V d7d7fb668, W e4c49bcd, C74a1a6ac
and K1f8817e5: zero Blocking, one Important and one Advisory finding. Root
records disposition here; the original report stays separate from the focused
remediation evidence.

## Important: prior network write test assumes old list visibility

General lane, V d7d7fb668, api/spec/api/resources/network_write_spec.rb:130-141.
The original feature regression expects Network.Index(enabled:false) to return
a disabled network for a member. The accepted follow-up intentionally returns
empty, while preserving direct Show and denying writes.

Root confirmed the contradiction. Implementer0 changed only the example name
and list assertions. Show200/statefalse and forbidden write403 coverage remain
byte-identical. The whole file passed in both core and full modes: 29 examples each, no failures,
pending examples or outside errors, with identical scoped example IDs. Scoped
Ruby syntax and lint also passed. Native JSON and exit receipts are under
`visibility-review-fix-quick1-*`.

Normal hooks passed when folding the assertion correction into the owning
visibility commit, now cc3337d0a2699a8b28a0327bbee5ef62f3fbe166. Root
verified the old-to-new diff changes only the example name and list assertions;
Show/write checks, production, fixtures, docs, schema and migrations are unchanged.
C b217e0f0a74b45fe2a95fcc79c2eb646f21248ce and K
609fd8a0070235339a4ddb567d905e466776d6a8 refresh only their exact pins.
Their full generated diffs and lock graphs were inspected, W and unrelated inputs
are preserved, and the fresh exact-source KB static check passed.

The Important finding is resolved under mandatory-change-review step 9. This
requested narrow fix adds no design or public-contract change; another reviewer
turn is not required. All intended changes are committed and clean, and longer
integration verification may proceed. This clearance does not certify deployment,
bitmap captures or the accepted Advisory limitation below.

## Advisory: shared suggestion capability lookup can outlive outer timeout

General lane, W e4c49bcd, useProgressiveSuggestedIpQueries.ts:60-67 and
src/lib/api/ipAddresses.ts:96-99. Source inspection confirms the 12-second
request signal is applied only after awaiting shared OPTIONS capability data.
The capability adapter supplies no signal, so a stalled request can keep
suggestions pending beyond the timeout. No runtime reproduction is claimed.

Accepted as a recorded availability limitation in this backend-only follow-up.
It is not an admission or permission bypass. W source and its agreed pin remain
unchanged, avoiding expansion into request/cancellation semantics during the
Index policy change. A focused later correction should bound the shared lookup
or each waiter, preserve deduplication and visible errors, and test stalled
OPTIONS. This finding does not authorize a new W rebase/deployment or certify
its current-release readiness; upstream branch reconciliation is separately
needed before integration. No blanket HTTP timeout policy is proposed.
