# Archive browser diagnostic evidence delta

Committed and normal SSH-published `e515437822e6a2ee7e61be7b613d1e058dad56d7`.
Exact affected range: `915b904101eca8170652a8dd198f63e3e3aae967..e515437822e6a2ee7e61be7b613d1e058dad56d7`.
Checked/final tree: `66fa5b4445a2408372b40d9a07fa7a2728b04e11`.
Exact delta: `package-b-archive-diagnostics-final.diff`; result:
`package-b-archive-diagnostics-result.json`. Independent affected-lane review
remains pending; no long diagnostic VM run has been launched.

Lead-authorized diagnostic follow-up after B `915b9041`. Only application path:
`test/archive_lifecycle_browser.cjs`. The prior attention-test commit and exact
A4300 client/dependency files remain unchanged. This collects evidence for an
unproved pre-existing stall and claims no archive/naming behavioral fix.

Original failure/cause limits: `package-b-archive-flake-diagnosis.md`.
Original B4c6 full log and helper preserved in
`package-b-archive-original-4c6b9f1.log`,
`package-b-archive-original-helper.cjs`, with identity/SHA-256 in
`package-b-archive-original-evidence.json`. Pre-diagnostic915 review packet is
preserved in `package-b-before-archive-diagnostics-915b904/`.

Added only monotonic request start/headers/finish/failure timing, resource type,
path/status, bounded inflight evidence, independent goto outcome and current
pending phase. Failure-only page snapshot adds readyState, bounded resource
completion/size timings and structural control state. Limits:120 network rows,
20 page errors,20 console locations,40 inflight/resources and10 controls;
explicit dropped/omitted counts distinguish missing data from absent requests.
HTTP URLs retain only pathname (max200 characters); non-HTTP payload URLs are
not emitted. Page errors retain allowlisted names, console diagnostics retain
only type/location, and network failures retain only allowlisted net::ERR_*
codes. No request/response body, headers/cookies, auth secret, raw console
payload or DOM HTML is read into diagnostic output. Existing non202 response
text and failure outerHTML dumps become status/structure-only evidence.

The exact original Promise.all operation-response predicate and hydration/assertion
policy remain. No timeout/synchronization/production behavior changes. The one-
second evaluation cap is confined to failure diagnostics; evaluation, timeout
and serialization failures cannot replace the original thrown failure. Normal
archive/revive/retry receipt output/actions remain unchanged.

Quick evidence: `package-b-archive-diagnostics-quick.log`; session-only checker
`package-b-archive-diagnostics-check.cjs` executes actual helper in a VM with a
fake Playwright boundary (no browser, network, credentials or registered state).
Three success action paths and five failure scenarios validate completion vs
headers/pending resources, caps/overflow counts, query/console/body/password
canary exclusion, and preservation of the original error through failed/hung/
unserializable diagnostics. Syntax and git diff checks pass in repository Nix.
No long/integration/native/live run or CI rerun was launched.

Lead assigns affected-lane independent review of the committed delta before a
fresh watcher runs the targeted session-archive-lifecycle VM. If the enhanced
trace does not establish cause, preserve the failure and return it for diagnosis;
do not increase timeouts, weaken hydration or claim the stall fixed. No product
documentation change is useful for this fixture-only evidence capture.
