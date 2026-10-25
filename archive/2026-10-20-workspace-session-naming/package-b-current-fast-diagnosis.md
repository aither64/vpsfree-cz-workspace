# Current-head fast CI failure

Historical B4c6 failure diagnosis. Its approved test-only correction is now
published as `915b9041`; quick evidence and pending review are recorded in
`package-b-attention-review-brief.md`. The source/proposal notes below preserve
the original diagnosis boundary.

B `4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`, Check `39820766257`,
fast job `119971119612`. Full original output is
`package-b-current-fast-failed.log` (SHA-256 in the JSON record), ANSI-stripped
readable output is `package-b-current-fast-sanitized.log`, and the compact
failure is `package-b-current-fast-excerpt.log`. Artifact inventory is empty.

The failed derivation `/nix/store/vb7ars9dr6rp2697pj26vifjrq0xl8ma-dev-workspace-0.2.0.drv`
reached package `checkPhase`, specifically `node --test internal/web/attention_browser_test.cjs`.
This was not a vendor hash, Go compilation, native naming or protocol failure.
The dependent agent-team-catalog derivation then failed because that package
failed. Other package variants passed the same browser test seven times in the
same log; one run failed in 7.202947 ms, before any Disable action.

The test at line 1611, “Disable fences a delayed old Enable across tabs before
local storage or unsubscribe side effects”, fails its line-1619 registration
setup assertion: `typeof release` is `undefined`, expected `function`.
It polls at most 100 `setImmediate` turns, which does not guarantee the real
asynchronous setup reached the deferred registerResponse. The registration path
first performs endpoint cleanup; `subscriptionSelector` awaits real
`crypto.subtle.digest`. Scheduling/crypto latency is consistent with the short
failure and other passes. The exact internal pending await was not captured by
CI, so that part is an inference. The fixed-iteration readiness assumption is
visible directly in the test and is sufficient to correct independently of
which preceding asynchronous step is delayed.

The test and all notification production scripts are byte-identical to base
`bf6d4b0c49600c15e17fe71248807ef43424e932`; the last owning test commit is
`8f67718a6c226f151dbc1719d857c77383495d18`. No A/C or naming contract is implicated.

Proposed smallest test-only correction: resolve an explicit stage-reached
Promise when the existing permission/register callback installs `release`.
Await a race between that signal and the Enable action (so premature action
completion still fails the existing assertion), with a Node test timeout.
Keep all existing cross-tab, storage, subscription and production crypto checks.
Do not add retries, increase the polling count or change production behavior.
Source/ref remains frozen pending lead release; no checks/reruns were launched.

Retrieval detail: `gh run view --job --log` refuses while the overall workflow
is still active even when the job is complete. The REST
`repos/aither64/dev-workspace/actions/jobs/119971119612/logs` endpoint supplies
the completed job immediately. This gh version requires
`gh api --allow-escape-sequences` when downloading ANSI-containing raw logs to
a file; sanitize before displaying excerpts. Neither API call reruns CI.
