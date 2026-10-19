# Independent final delta review

Reviewed the complete `dev-workspace` branch from
`7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03` through
`499cb2b35ff87c0c2182b8f2a4d9a6427c7c3e3c`, including the new retirement
correction and the delta from the original reviewed head `a373216`.

## Blocking

None found in this delta.

## Important

1. **The fork still reuses an inherited follow-up marker.**
   `test/creation_acceptance_browser.cjs:87` calls
   `followup("CREATION_FOLLOWUP_" + name)`. Both the initial source creation
   and `browser("fork", "explicit", ...)` use `name == "explicit"`. The fork
   copies the source's completed user/assistant exchange containing that marker.
   The new same-turn assertion at lines 67–71 can therefore pass on the copied
   exchange before the fresh submission is visible, or fail with two matching
   user items after the new submission appears. Original finding 5 is only
   partially resolved. Generate and record a fresh destination-specific marker,
   assert it is absent from the destination transcript before sending, and retain
   the exact single user item, same turn, completed status and expected-provider
   reply checks. The lead's proposed UUID marker and pre-send absence check
   directly address this finding without changing the accepted design.
   Commit: `1fb4442fc8b558f53a025266fe96794d3e347e63`.
   Lanes: general, risk.

## Advisory

2. **The barrier publishes its pathname before its JSON payload is complete.**
   `test/creation_transport.py:38` uses `Path.write_text` for `send-accepted`,
   while `nix/tests/session-creation.nix:293` waits only for the file to exist
   and immediately decodes it. Opening the file creates it before the write,
   so the VM controller can observe an empty/partial payload if the writer is
   descheduled at that point. Publish the short record through a temporary file
   and rename, or make the wait predicate require a complete parseable record.
   This is a limited fixture reliability issue, not a runtime persistence flaw.
   Commit: `1fb4442fc8b558f53a025266fe96794d3e347e63`.
   Lanes: general, architecture.

## Original finding reconciliation

Original findings 1, 2, 3, 4, 6 and 7 are addressed by focused inspection:
solo null members are normalized; each endpoint's actual destination contract
is respected; successful forks require absence of the temporary journal and
read the real receipt/completion evidence; the post-send barrier is cleared
and bound to the actual initial prompt, root, turn and cwd; attachment delivery
is inspected in the native initial item and the referenced file's bytes; and
the schema-6 fixture creates two retained reviewers with distinct identities.
Finding 5 remains subject to the Important correction above.

The `repos/` setup correction and durable-status lookup after accepted POSTs are
bounded test fixes. The request-ID path reads the actual serialized form ID;
fork/plan use exact mutation routes and their submitted destination. These reads
do not stub creation, fabricate completion or bypass the shipped serializer.

## Retirement change: all four lanes

No production correctness or safety defect found in `499cb2b`.

General: both retirement discovery paths call the new helper, preserving their
existing cwd, `vscode` source, archive state, limits, sorting, cursor handling
and indexed-versus-scan selection. The helper also preserves the shared client's
rejection of missing/null `data`. Candidate ambiguity, exact-root checks,
archive-state proof, idle verification and final archival remain in their
existing owners. The focused regression tests exercise active indexed lookup
and archived lookup for an alternate-provider identity.

Architecture: the pinned codex-web `ThreadListOptions` has no provider filter.
The small private query is appropriate to this workspace-owned retirement policy
and is shared by its two local callers. It preserves the existing response
contract without introducing a parallel general client or changing dependencies.
The same helper is used by `RecoverArchivedThread`; that consumer also benefits
from observing alternate-provider roots and conflicting active identities.

Scope: this addresses the handoff's observed failure and the accepted ordinary
fixture-deletion gate. It adds no native patch/rebuild, package interface,
generalized framework, persisted format or session-team change. It does not
authorize another action against the already removed user request.

Risk/compatibility: the selected stock native schema in
`/tmp/creation-native-schema-g9qkb9rz/v2/ThreadListParams.json` explicitly defines
a present empty `modelProviders` array as including all providers. The emitted
non-nil empty Go slice has that representation. The broader discovery strengthens
cross-provider ambiguity detection; it does not authorize archival based solely
on a list entry. Rollback retains the same state formats, although the older
query can again refuse retirement of an alternate-provider root. The new
documentation describes supported behavior and keeps rollout-specific evidence
in session records.

## Complete branch history and verification boundary

The final series has three coherent commits:

- `98ae6b38b2830b612f68d3d5a84f96c1d7caf5ca`: journal reader correction and
  real producer/consumer contract regression, unchanged from the first review.
- `1fb4442fc8b558f53a025266fe96794d3e347e63`: packaged whole-process acceptance,
  its direct review fixes, CI and related documentation.
- `499cb2b35ff87c0c2182b8f2a4d9a6427c7c3e3c`: retirement provider discovery,
  focused regression and provider documentation.

The former acceptance head was replaced by its consolidated final form; no
obsolete approach, superseded intermediate fixup or transitional compatibility
path remains in the current series. Fold the narrow marker correction into its
acceptance owner. **No migrations. No repeated dependency or generated-pin update
streams.** There are no new schema versions or migration provenance obligations;
the packet records these feature commits as unmerged and undeployed. Consumer
pins are still deferred. The supplied base is the merge base, the source tree
is clean, and whole-range `git diff --check` passes.

The packet reports the retirement quick checks passing in 5.117 seconds. Since
the changed helper is also used by archived recovery, include the existing
`TestRecoverArchivedThread*` cases in the next focused quick pass; the reported
`TestRetir|TestRequireThreadArchived` selection does not include them. Source
inspection found their expected request semantics preserved.

The running VM uses immutable head `1fb4442`, so its result cannot validate
`499cb2b` or the remaining marker correction. After reconciliation and quick
checks, verify the final packaged source, the old-reader runtime negative
control, and the actual deployed creation/follow-up matrix. No integration,
deployment or conditional merge readiness is established by this report.

Reviewer remains `/root/creation_final_review`, catalog-selected
`gpt-6-astra` / `xhigh`; no nested agent. Session identity and both environment
markers match the bound session, and the live roster is null. Reused the
previously read mandatory review skill, all four lane references and applicable
workspace/repository procedures. Read the full delta packet, updated design
and plan, original review/reconciliation, actual delta, surrounding consumers,
tests and native schema. No source edits, long tests, lifecycle mutations,
deployment or integration were performed. Only this requested report was added.
