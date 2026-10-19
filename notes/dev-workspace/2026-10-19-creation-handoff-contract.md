# Test session creation past HTTP admission

An explicit provider selection was accepted and persisted by the portal, but
the destination then failed with `direct team creation request is no longer
current; start a new request`. Ruby's schema-3 receipt reader did not allow the
Go producer's `provider` field, and start did not forward provider intent into
its receipt preparation call. Plan requests also carried a destination-settings
flag absent from that reader.

The earlier shipped-browser HTTP test deliberately held the naming boundary. It
proved real form parsing, acceptance, replay and saved input, but stopped before
the creation handoff. Those checks could pass while the actual initializer
rejected the saved request. Keep admission coverage and exercise the next owned
boundary too: `TestCreationReceiptRubyInitializerContract` serializes real Go
receipts, passes them through Ruby's real receipt preparation, then rereads the
binding in Go. It covers standalone/direct new, plan and fork shapes, inherited
and explicit providers, retry and changed-provider refusal. A Ruby full-start
case also checks provider forwarding and one root/initial turn on replay.

The real-browser check separately found a CDP observation race in an existing
assertion: navigating away can retire the POST response body before
`response.text()` or `response.json()` reads it. Observe the actual 202 response,
then query the durable status endpoint using the exact submitted request ID.
This preserves real HTTP admission without requiring an old document's body to
remain in Chromium's resource cache. Keep mocked failure status after the real
admission checks when testing selection/clipboard rendering.

The full source Go suite passed after applying the existing short-TMPDIR and
host-catalog isolation guidance. The final browser check passed, including text
selection across two status polls and Copy error clipboard contents. Original
failed runs and diagnoses remain with the initiative; no blind rerun was used.

Related initiative: `work/2026-10-19-session-creation-provider-recovery/`.
Runtime receipt correction `8920252`, selectable errors `3c0b459`, browser
observation correction `a857242`; project contract in
`dev-workspace/docs/session-preparations.md`.
