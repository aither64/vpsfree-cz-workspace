# Archive browser fixture provenance

Related initiative: work/2026-09-16-archive-retirement-timeout.

The real-browser archive test initially saw an empty thread identity even though
its portal manifest contained one. The shared newTestServer fixture has no
VerifyThread callback; normalizeInteractivity therefore intentionally removes
Codex identity from rendered pages. Supply a fixture verifier that checks the
expected thread and canonical working directory, and assert the rendered identity
before browser assertions. Keep the archived page read-only.

The first browser launch also referenced a previously realized, unrooted Nix
Playwright output which no longer existed. Rebuild pinned Playwright tools and
keep temporary Nix out-links until the browser run completes. Do not change the
project dependency pins to fix local tool availability.
