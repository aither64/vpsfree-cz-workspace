# Native subscription-read fixture boundary

Clean final **`1038d4abdde8b115c21b5940b14be637cfa967b6`**, tree `087795d04b26ed65588df8fdbca938a79a39f2f7`.
Owning eighth **`fe72f3c043bd7101544bc4639d98211ec9202202`**; unchanged ninth replay **`1038d4abdde8b115c21b5940b14be637cfa967b6`**.
Exact197/eighth2f6c refs and all prior immutable packets/failure/diagnostic/gate
artifacts preserved BEFORE edits. First seven deployed objects remain unchanged.

Only notifications_browser_test.cjs changed. A small page-local function catches
only native getSubscription invocation/await and accepts only a DOMException named
AbortError, InvalidStateError, NotAllowedError, NotSupportedError, SecurityError
or native UnknownError. Other exceptions fail fixed safe wording. Registration
lookup/presence and JSON serialization remain outside that catch. Serialized JSON
stays solely in page memory. Only finite read/category/engine and comparison
booleans return/log; an unavailable pair reports identityVerified:false, never
subscription absence. Both lookups require a present registration and compare
that exact object after sound save. Chromium must remain readable.

Direct source inspection of outcomes (not new native execution):

| Before/after native read | Firefox | Chromium |
| --- | --- | --- |
| Both readable, equal serialized identity (including actual null) | Pass comparison | Pass comparison |
| Both unavailable, same recognized native category | Identity UNVERIFIED; comparison permitted | Fail |
| Readable/unavailable change | Fail | Fail |
| Unavailable category change | Fail | Fail |
| Readable identity change | Fail | Fail |
| Missing/replaced registration | Fail | Fail |
| Non-DOMException or unrecognized native name | Fixed safe failure | Fixed safe failure |
| Lookup/serialization failure | Fails outside catch | Fails outside catch |

Zero register/disable POSTs still independently asserted. No permission grant,
Firefox mock, generic other-success path, loop, timeout or product behavior
change. The entire suffix from retained Settings setup is byte-identical,
including navigation boundary, lifecycle/controller/capability, saved sound,
reload/shared/keyboard, subscription, correlation/options/click, draft/URL and
final-zero assertions. All other tracked blobs equal197.

Quick **PASS**: fixture syntax, all **53 existing Node actual-module contracts**,
working-tree and197->final diff checks. See native-read-quick-status.json and
numbered logs0–3 (all with notification-controls- prefix). No mirrored helper
test framework, unchanged Go or native/browser run. New exact-head fixture is
**UNRUN**, awaiting retained affected committed review. The197 diagnostic only
located the outer snapshot137:20; its inner cause/category remains unproved.
No retrospective ordinary-run, physical macOS sound/display/focus or full-flake
acceptance claim follows from this adaptation.

Exact delta in `notification-controls-native-read.patch`; complete nine commits
in `notification-controls-native-read-series.txt`. Freeze.json binds final
source/blob hashes and unchanged product equality. Ninth stable patch ID remains
**`936d8a9b985a4f827b1ad03f85b0be742140cd62`**, range-diff equality recorded. Original bodyfiles and normal hooks
used without bypass. No schema, private format, API, protocol, dependency or
migration changes. Existing source/review/history boundaries retained; only this
new fixture delta needs affected review. Historical wrappers retain exact heads.

**HOLD source/publication/pins/browser/long/provider/network/host/lifecycle.**
Lead owns review, the next finite fixture/fallback and operations.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
