# Blocked HTTP probes can outlive request cancellation

Initiative: `work/2026-10-03-automatic-session-slugs/`.

The native isolation fixture used `http.Client{Timeout: 100 * time.Millisecond}`
with the default transport to prove that nftables blocked a synthetic endpoint.
Later deny-counter increments appeared between utility leaves. Their packet
ownership is not yet proven.

Go 1.26.7's `net/http/transport.go:1523-1529` detaches dialing from request
cancellation so an eventual connection can serve another request. Cancelling
the waiting request does not cancel that dial (`wantConn.cancel:1390`).
`CloseIdleConnections:909-917` can cancel pending dials that no longer have a
waiting request. A short HTTP request timeout alone therefore does not establish
that a blocked connectivity probe has finished all network activity.

For this fixture, the architect selected one owned `net.Dialer.DialContext`
against the synthetic literal IPv4 endpoint, with the same 100 ms budget. It
returns synchronously and closes any connection before control startup. Keep
the allowed-provider connectivity probe, require a positive deny-counter change
for the blocked dial, and retain every later strict fixed-baseline assertion.
The correction removes a concrete possible producer; it does not attribute
earlier packets or justify ignoring residual increments. At corrected4651d764,
all35 actual native leaf records kept deny samples2->2 with no unavailable
sample. The run still failed separate tool/persistence gates, so this is
counter-stability observation, not a complete isolation pass.
