# Verification notes

The browser regression uses the actual portal template, CSP, JavaScript, CSS,
upload service and SSE endpoint. Controlled thread/pending API responses avoid
opening or changing a live Codex conversation.

Harness corrections made while establishing coverage:

- The connection warning intentionally has a ten-second grace period. A five-
  second assertion was too short; the test now allows fifteen seconds.
- A finite synthetic event-stream response immediately disconnects. The fixture
  now uses the actual SSE endpoint with an open event channel, and notifies it
  through an isolated fixture endpoint. Repeated focus events were also unsuitable
  for forcing snapshots because the synchronizer coalesces/throttles them.
- Optional notes require an option to represent an answer under existing wizard
  semantics. The multiple-question case now selects an option before typing its
  associated note; the product's answer encoding was not changed.
- The upload server initially retained the generic fixture's configured origin,
  while the browser used an ephemeral localhost origin. Its exact-origin rejection
  was correct. The fixture now configures both conversation and upload handlers
  for its actual HTTPS origin (required by the upload contract) and uses the ordinary browser request without overrides.

Product issue found by the browser test:

Disabling a focused answer button moved focus to the body. Restore that control
when the request settles if the user has not focused anything else; the pending
refresh can then transfer focus when removing the question. Disabling Interrupt
at turn completion similarly transfers focus into the current view before the
question is removed. Both paths are part of preserving focus for the new layout.
