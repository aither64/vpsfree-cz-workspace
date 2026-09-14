# Exercise question refreshes with the real event stream

For portal browser tests, a finite fulfilled SSE response represents a disconnect,
and repeated focus events are throttled. Use the real SSE endpoint with an open
fixture event channel, and trigger snapshots through a test-only notification
endpoint. Allow for the existing ten-second connection-warning grace period.

Configure both conversation and upload handlers for the ephemeral HTTPS fixture origin; the upload handler rejects HTTP origins.
Keeping the generic test server's original origin caused correct upload rejection;
trying to overwrite browser Origin headers did not fix that mismatch.

The resulting fixture verifies question/composer transitions, failed answers,
focus, uploads and responsive layout. Related initiative:
`archive/2026-09-14-portal-planning-question-controls/`.
