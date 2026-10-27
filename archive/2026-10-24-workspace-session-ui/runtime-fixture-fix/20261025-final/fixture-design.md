## Targeted quick failures: correct two naming fixtures

Status: source-backed diagnosis complete; owner1's bounded test correction is
ready for lead acceptance before edits. No production change or diagnostic
execution is needed to explain these failures. Keep outer 69439, its CLI 0/
runner 1, all original logs, 745-entry manifest and selected source snapshots.
Pin, negative-pin and request-corpus stages passed; go-web failed and all later
stages were not run. The preguards passed; the final guards were not reached.
The go-web log SHA256 is
`117dc4d5934f470ae25c2546bff59936ea5c611bc2bfcd4dd7994049d97581ca`.
The tested range remains b974..f8a282af7ceae26625366b0659ae3c43fe5d80a5 plus the
five frozen final025 dependency inputs, not a new completed runtime head.

### Causes and preserved behavior

`creation_contention_test.go:41` is unchanged from b974. It installs
`normalSessionName` with a missing socket and no model catalog. In b974 that
adapter returned `errSessionNamingFallback`; the old naming worker substituted
`development-session`. The accepted source takeover removed that fallback.
Current `session_namer.go:42` returns `ErrEphemeralServer` for the empty catalog
before creating a client, and `namePreparation` correctly records utility_error
and stops before reservation. Thus the automatic subcase never reaches the
occupied-name precheck. Its observed failure does not establish a lock-order
regression. The custom subcase passes because it does not call naming.

`session_namer_test.go:179` requests `os.Mkdir(..., 0755)` but does not establish
the actual mode. The exact executed runner (SHA256
`28165bc2d276313002d4fe2d2fba787d7c8165f41a412af5c6e78b663f14bc27`) sets
`umask 077` before both its outer and inner stages. No runtime Go test changes
that mask. Under that setup the requested directory is created as `0700`, which
`modelSessionName` is required to accept. The current adapter checks the naming
root with Lstat and exact `0700` before creating scratch/calling the client; the
lifecycle store's mode repair applies to its parent, not that root. The mock
call is consistent with valid private state, not evidence that an actual `0755`
root bypassed refusal. This is source/control-flow evidence; no surviving
per-test directory mode observation is claimed. The other three unsafe-state
subcases passed.

### Owner1 implementation boundary

Limit application-repository edits to these two tests and their explanatory
comments. Keep the final five dependency edits unchanged. Any production,
package, runner-environment or other-file correction returns to the lead.

- In `portal/internal/web/creation_contention_test.go`, inject the existing
  `Config.SessionNamer` test boundary with valid JSON
  `{"name":"development-session"}`. Remove the missing-socket/normal-adapter
  setup from this successful-name collision fixture. Retain the actual portal
  queue/reconcile shared runtime lock and inode check, automatic `-2` suffix,
  attempt 1, handoff, accepted input and same-receipt replay. Assert the automatic
  base/outcome came from the injected model result, with one call and no extra
  call on replay; the custom collision must still refuse with no naming call.
  Count asynchronous calls safely. Describe generated-name collision selection,
  not a fallback. Existing unavailable-socket/error tests continue to require
  stopped preparation and no generic name.
- In `portal/internal/web/session_namer_test.go`, explicitly chmod only the
  owned `session-naming` test directory to `0755` after creation, check errors,
  and Lstat/assert the actual directory mode before invoking the adapter.
  Keep the never-call mock and `ErrEphemeralIsolation` assertion. Check that
  refusal leaves that mode unchanged. Preserve the other unsafe cases and the
  existing `0700` positive fixture. Do not change the process-global umask, runner
  mask, production check, or expectation to accept an unexpected client call.

These fixes preserve archive-preparation schema 1, occupied-name precheck and
its locked recheck, PLAN source waiting, SQLite/lifecycle contracts, prompt-only
raw 0.164 naming, shared retry proof, private paths, the 30-second budget/two slots,
two-call cap, output validation and manual recovery. Existing product docs
already describe these contracts correctly; no product-doc change is needed.
The fixture comments should explain the independent naming stub and explicit
permission setup.

### Verification, exact inputs and review

Owner1 uses the existing pinned environment and unchanged restricted runner
setup. Rerun the existing go-web selection on the corrected final source under
umask `077`; this includes both failures and the retained naming/error/creation/
archive/PLAN assertions. Also run the unsafe-state test alone in a separate
child shell with umask `022` to prove the fixture sets its intended mode under
both masks; do not mutate a running Go process's mask. Then execute the later
previously unrun targeted stages. Use fresh result paths and guards; no retry
of the old frozen packet. Prior pin/corpus results can be retained only with
unchanged relevant inputs/tool identities. No new client/native repetition is
justified by these two test edits.

The package uses `src = self` and `buildGoModule` inherits that source, including
these tests. Consequently old 995/2r and their successful vendor proof remain
historical after edits; do not relabel them as the final source/derivation.
Owner1 must bind the new complete source, source delta, final goModules
derivation and retained roots, with all module/pin/vendor inputs demonstrably
unchanged. Keep Fx only after verifying the expected output/hash/content; no
hash-discovery build or manual metadata adjustment is needed. The existing
fresh-final-dependency requirement applies to the new requested derivation:
prepare one explicit forced-rebuild verification for the parent's watcher
release, record actual command exits, and use valid-producer/output/source
relations rather than historical registered-deriver equality. Preserve old
receipts and both root sets. This paragraph does not itself launch/release
evaluation, rooting or a build.

After final quick checks and commits, include both fixture corrections and
their causes in the already-required affected runtime review (general,
architecture, scope and risk for the combined b974 integration). Bind the whole
final history, five coherent input changes and new source/derivation; these are
test changes, not a mechanical-pin review exemption. Reuse unaffected client025
and exact-native evidence explicitly. Existing post-review stage06, runtime
creation/naming/archive acceptance and final-output/deployment gates remain;
this diagnosis supplies no acceptance, activation or default integration.
