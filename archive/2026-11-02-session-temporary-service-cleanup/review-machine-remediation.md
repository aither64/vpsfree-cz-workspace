# Machine review M1 closure

M1 is CLOSED by lead direct inspection under mandatory-change-review step 9.
The immutable independent [review-machine.md](review-machine.md) applies to
runtime30d3, extensionf8da and workspace48b. Its SHA256 remains
963a7c6eb2abe1159bddec406bfe39111a0c5ecc089bec2f025f0865ca81adfa.
It found no Blocking or separate Advisory issue and requested this exact narrow
ordinary-I/O correction. No automatic reviewer rerun is needed.

Corrected runtime head: `71428083c58a42aa9415ad173d19963574b92651`, tree
`d251f64e0cf9734967ad29fe42d9637a4e2ddbd6`. The original four commits are exact
and range-diff equal; only the fifth machine commit was folded. Reviewed30d3,
its x28 source/root and tested fixup87e726e9 remain retained. Final tree equals
the tested committed fixup. No obsolete fixup remains in the five-commit series.

Lead read the complete four-file committed delta (157 additions/10 deletions).
One Store read_retained_file boundary invokes the existing strict private reader,
returns explicit presence plus parsed value, treats only ENOENT as absence and
maps other SystemCallError to the existing owner error code5. Both ledger and
claims readers and compatibility guards use that boundary. A small claims_record
tuple preserves the original claims error wrapper and validation. Present null,
malformed JSON and dangling symlinks cannot become empty state. Genuine absent
stores remain supported. No record write, schema/API change, collector, new
capability or unrelated inventory hardening was introduced. The diagnostic
received the required main-agent wording pass; existing recovery guidance remains
accurate, so no new product-documentation change is needed.

Causal red on reviewed30d3 demonstrates actual ordinary-uid inaccessible root
false absence, raw I/O failure and skipped dangling claim symlink. Final focused
results: owner8/138, adjacent claims5/23 and host1/84, totaling14tests/245assertions,
with no skips. They cover inaccessible coordination root and state ancestor,
lstat/read EACCES/EIO, absent/null/malformed/symlink controls, terminal/empty
schema2 gates and actual prepare_profile/activate_candidate/candidate _activate
refusal before profile, quiesce or service configuration effects. Retained bytes
are unchanged. Two Ruby syntax and whitespace checks pass.

The earlier host assertion expected a direct Errno cause after the original
claims error wrapper had been preserved. Its failing evidence remains in
machine-retained-io-final-quick.log. The assertion now follows the existing
wrapper to the typed cause; final-host.log passes with unchanged product code.
Lead inspected these actual results and independently verified all three red/
final log hashes against [machine-retained-io-final-receipt.json](machine-retained-io-final-receipt.json).
This is a scoped set of successful final checks, not a claim that the earlier
combined command wholly passed.

Lead independently matched all679 final Git bytes/symlink targets/executable modes
to both clean worktree and `/nix/store/64gqydr0pg2gfynml4c9h49gfsqx4irx-source`,
recomputed NAR `sha256-N7T9/uPWHxvifkg+5uLUnKy8w4SAHoGKDm4x6Ql8oI4=`, and
checked the file-manifest hash, exact four-path delta, tested/final tree equality,
unchanged lock and original-four range. Full9-node graph/inputs and source root
are bound by the receipt. No native/package/Playwright/deployed acceptance follows
from this focused closure.

The requested refusal restores the reviewed boundary without expanding design.
The independent review source gate is clear. B must rebind the exact final
committed composition before provider publication/final graph certification.
Existing authorized postreview checks and publication may then proceed; final
pins and expensive downstream preparation still wait for exact runtime acceptance.
Default integration and session lifecycle actions remain unauthorized.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/

## Required packaged test registration follow-up

After source publication at7142, A's required aggregate-membership check found
machine_identity_test.rb absent from the existing fixed suites map. The lead
released the minimum correction. Final runtime is now
`63e40687977d0cf4c047898203cf41f90da1a9fe`, tree
`edc8d68217b07a2003e5eeeda904b611bc038e40`. The complete committed7142→63e delta
is one added `machine_identity = 1;` line in nix/ruby-checks.nix. No test logic,
runner, product, API, schema or reviewed behavior changes. The same four original
commits remain exact, with only the owning fifth folded; published7142/ref/source
and tested fixup683e83cd remain retained. Final tree equals that tested fixup.

Lead directly inspected the line, the actual existing runner result24tests/
251assertions in26.861585s without failures/errors/skips, and the timing manifest:
all24discovered, selected and executed identities are identical and unique,
coverageComplete=true. The actual Nix aggregate derivation's JSONv4 inputs.drvs
explicitly includes ruby-machine_identity-0's49dz7s... derivation. Nix parse and
check-map evaluation pass. Initial lead receipt-reading assumptions about the
manifest field/derivation JSON shape were corrected read-only; no source or
validation command was retried. This conventional registration adds the already
reviewed tests to the already reviewed runner. No new design/boundary needs an
automatic full independent reviewer rerun; this mechanical wiring correction is
directly verified before resuming the required exact-head checks.

Lead matched all679Git bytes/modes/symlink targets to the clean final worktree and
`/nix/store/sq02l707g48gdxn4y7xpgk4ga8r558ii-source`, independently rehashed NAR
`sha256-tKwf2dJ9X4mXBy07rWphtiGNMmpEuyAzcJIo3ortS4U=`, verified one-path delta,
tested fixup tree equality and unchanged lock. M1 remains closed; its source and
focused proof are unchanged. B's final exact63e composition rebind is required
before replacing publication/CI; old7142run41687690414 is not final evidence.
Cancel only superseded active same-feature runs after the new remotehead proof.
No local browser/native long check, downstream pin, build/copy, machine claim,
activation, default integration or lifecycle action has run for this follow-up.

## Pre-VM fixture and generic-source follow-up

Postpublication runtime7142 and63e Check failures were inspected, not retried as
infrastructure problems. No VM had run. The unchanged generic-source check rejected
the site-specific example/vector in generic runtime docs/tests. An explicit packaged
archive-recovery fixture omitted the already installed new helper in both its copy
and symlink lists. The collection-generation fixture injected a test engine but
not that engine's store; the real-host store now validates its fixture-local remote
and raised before the lock assertion. Its timeout was a consequence of that exit.

Lead released the conventional four-path docs/tests-only correction and directly
changed the documentation identifiers to a generic configuration example. Final
runtime is `5f7b13fd32f85ac0f502b42642578b19bbefc67e`, tree
`ed7fa726e39020ad5eded519b8d70f6114254044`. The complete63e→5f7 delta is11additions/
10deletions: docs/coordination.md, test/machine_identity_test.rb,
test/workspace_coordination_test.rb and test/workspace_host/archive_recovery_test.rb.
All libexec/portal/nix/flake files are byte-identical to63e. Lead read the complete
diff, confirmed existing deadline and lock assertions unchanged, checked both helper
dependency lists and the existing fixture store injection, and independently
computed generic vector SHA2565d7b9846f8019fea13e81daa5cd4ae6a65c2c1fb79aed4eba1a7d4eea1b6848d.
Concrete site profile/display proof remains with the consuming workspace. There is
no product, schema/API, validation-ban, timeout or accepted-boundary change.

Focused causal red/green evidence is retained. Lead inspected the actual green
log: complete machine shard24/251, packaged-layout1/3, collection-generation1/4,
total26tests/258assertions without failures/errors/skips, plus three Ruby syntax
checks. The original generic-source ban built successfully as its tiny check,
drvxklg4swv32akbacplb0a5b44wpwwaiqf; no package or native build is implied. Initial
CI/focused failures and benign busy Nix evaluation-cache diagnostics are preserved.
This is a directly verified correction of the reviewed tests/examples and fixture
construction, not a new design requiring an automatic full reviewer rerun.

Lead matched all679Git bytes/modes/symlink targets to the clean final worktree and
`/nix/store/nh39qmqwl5gj27w95qq5axr62bckrl6r-source`, independently rehashed NAR
`sha256-XE72HTS5wHHHvDfFm9J+N0NfdHIcQedWWBsEdv4uFJI=`, checked exact four paths,
production/Nix equality, tested fixup0f5eab49 tree equality and unchanged lock.
The original four commits and all reviewed/published predecessor refs/sources stay
retained. The source gate is clear for B's exact5f7 local-composition rebind, then
the already released exact-head publication/verification package. M1 remains closed.
The sole active utility observes extensionf8da CI41689335044; no duplicate observer.
Actual runtime package/native/Playwright proof and final downstream pins/deployment
remain outstanding. No operational approval beyond existing user scope is inferred.

## Activity consumer navigation correction

Actual5f7 backend browser check passed all four desktop/mobile×root/member variants
and its complete32manifest in54.27s. The separate activity consumer failed on a
hidden retry control after opening Settings. Shipped template/handler source shows
General is the default subtab and retry policy belongs under existing Automation.
B's committed fixup `ad0770a8ce6bb3b70645dc196386106a049072e8`, tree
`fd80694f0e28bf619fb297c5826b845f9bffc2d9`, adds exactly three existing Automation
subtab clicks to portal/internal/web/retry_activity_browser_test.cjs. It changes no
product, assertion, scope, geometry, keyboard behavior, deadline or API. The final
unsupported-policy check now runs in the correct pane rather than passing through
a hidden ancestor.

Lead read the complete one-file3line delta and inspected structured receipt plus
actual log/file hashes. The exact Go TestQuestionBrowser/retry_activity_browser_test.cjs
passes desktop and mobile in24.913s; each manifest records10thread reads,
3preference writes,2actions and screenshots. Committed tree equals tested tree,
no owned process remains. Evidence: runtime-activity-harness-correction/receipt.json
and runtime-activity-harness-correction.md. Backend was not repeated because its
inputs were unchanged. This conventional test navigation correction is directly
verified without an automatic full source review rerun. A later consolidates it
into the capacity verification commit, preserving all original refs/source evidence.

Separate current5f7 CI failure did not reach VMs. Two existing deletion-location
regressions now hit M1's strict ENOTDIR refusal before the expected existing
DevSession location validator. Architect is confirming a fresh-only read-only
preflight before the coordinator read, preserving M1 and saved-journal recovery.
No core edit is certified by this activity closure. A owns that dependent fix,
with focused general/risk independent review after committed quick checks.

## Plan-delivery compact-authority test correction

Exact60aCI41702635860 failed all three required jobs in their common package
build, before VMs. Actual completed job/full logs showed only
TestPlanDeliveryManagedHTTPFreshAndPreparedRestart's four subcases failing an
obsolete one-snapshot assertion. Focused immutable60a reproduction failed in0.876s;
HTTP202/original single native send had already succeeded and accepted history
was compacted into ManagedTurn as designed. No product change was justified.

Final runtime is `1e138a552c1cc355d0b05a9d47a25d8e391aa85c`, tree
`9ee815831e1a15981e50c1b5c87185892ac8cf82`. Lead read the complete one-file delta:
portal/internal/web/plan_delivery_test.go,36additions/4deletions. It strengthens
original UUID/text/single-send checks, replaces the stale snapshot representation
with exact Scope/epoch/Binding/ManagedTurn equality, native item ID/client UUID,
count1/emptycontext and canonical seed/input SHA256 digests. The tuple is derived
from known fixture values and actual temporary socket identity, not stored digest
or production managed-prefix helpers. Existing planDigest is a plain SHA256 wrapper;
no managed algorithm is called as its own oracle. Expected epoch2/3 preserves the
existing settings-refusal invalidation. Remaining receipt-first replay, ack,
restart, mode/settings and no-extra-send assertions remain and execute.

Focused four-case green1.618s and owning related PlanDelivery selection8top-level/
19leaf cases5.024s pass, no failures/skips; gofmt/diff checks pass. Lead inspected
actual results and independently matched all three red/green/related log hashes
and source manifest in runtime-postreview-60a2438f/plan-delivery-remediation-receipt.json.
The fixture uses explicit temporary state/native.sock/fake transport and an absent
provider catalog. This verification did not use an installed helper/live endpoint.

Lead independently matched all679Git bytes/modes/symlink targets to clean worktree
and `/nix/store/zk1c2zfpq7syi9ickxz8r67x4frgdd1r-source`, rehashed NAR
`sha256-X1vYLOEeYw5T/Qjdi/28RZNVyfxeN7h+B7b0rj6OVOQ=`, checked testedfixup91d88c6c
tree equality and unchanged lock. First3 remain exact; only capacity fourth3cf36879
owns the assertion correction, machine fifth is range-diff equal to reviewed60a.
No product Go/Ruby/Nix/schema/API/epoch/compaction/policy or new imports change.
The strict assertion correction preserves the already reviewed contract, so direct
narrow inspection/checks suffice without an automatic full reviewer rerun.
Historical incident evidence limits remain unchanged, not certified away.

All earlier refs/source roots/failedCI/incident evidence are retained. B must rebind
actual1e138 composition before exact feature publication and fresh required
package/nativeCI. No native VM success or overall package pass has been claimed;
final pins/expensive preparation, deployment/default integration/lifecycle remain
subject to their existing gates and separate authorization.
