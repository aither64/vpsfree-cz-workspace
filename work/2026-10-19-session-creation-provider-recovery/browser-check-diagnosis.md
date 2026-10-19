# Browser check completion

The corrected whole Go suite passed on 3c0b459 (87.052s), but the conditional
browser test stopped at an existing unmocked-admission assertion before reaching
the new selection check. The exact failure was CDP Network.getResponseBody at
creation_settings_browser_test.cjs:282:57, while calling response.text for the
successful POST after its page navigated. Chromium no longer retained that
previous document's response body. Original failed logs/results are preserved.

Runtime commit a857242 fixes only that test observation. It still submits the
real form and observes the real 202. It then obtains authoritative status from
the actual API using the exact clientRequestId in the submitted request body,
and verifies that identity before checking redirect and recovery. No /sessions
interception, product behavior or admission guarantee was removed.

The actual browser test passed on a857242 in 23.115s. It proves all three
provider choices through real admission plus durable status, then selects the
displayed error text, waits at least two status polls, checks text node identity
and selection, and verifies clipboard contents after Copy error. Repeated TLS
handshake diagnostics come from the existing self-signed fixture; the test
completed successfully. No browser/page errors were accepted.

The production code and Ruby tests are unchanged from accepted 3c0b459. Exact
final package/CI checks still apply. Dependency pin streams are regenerated as
single updates from their original bases; superseded unmerged pin refs remain
retained solely for review/evidence, with no intermediate activation or consumer.
