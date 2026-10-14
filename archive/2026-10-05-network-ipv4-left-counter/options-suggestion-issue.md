Progressive IP suggestions can stay pending beyond their request timeout
when shared capability discovery stalls.

At ce856841a65d72648d03b6cba1748dd7dd9af048,
`useProgressiveSuggestedIpQueries` creates a 12-second abort signal, then
awaits the shared `ip-address-index-capability` query. Its
`fetchIpAddressIndexCapability()` OPTIONS request does not receive that
signal. Only the subsequent address GET does. A stalled metadata request can
therefore keep the active suggestion queries pending and prevent progression
to later locations after the timer has expired.

This is supported by source inspection, not a browser reproduction. Server
allocation checks remain enforced; the issue concerns optional suggestion
loading and progression.

To reproduce, use a cold capability cache, hold the
`OPTIONS /ip_addresses?method=GET` response open, open the admin IP page and
enable suggestions. Check whether loading and progression remain pending
beyond the intended request bound.

Expected behavior: suggestions are best effort and settle after a bounded
wait. Manual filtering remains usable. Preserve shared capability caching;
one suggestion caller timing out must not cancel discovery for every caller.

Regression coverage should distinguish stalled OPTIONS from stalled address
GET, include cache-hit and unmount cases, and check that later location batches
can progress after a bounded failure. The suitable timeout and retry behavior
can be decided when implementing this issue.
