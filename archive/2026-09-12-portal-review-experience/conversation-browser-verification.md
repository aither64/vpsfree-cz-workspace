# Conversation browser acceptance

Passed with Firefox155/Selenium4.40 against the actual portal HTTP handlers
and committed runtime8d3d44c, using controlled Codex data. This validates the
browser/handler contract; live Codex question timing is checked separately.

- Messages is the initial view. All renders a typed search link and expandable
  subagent details. A100-message transcript provides realistic scrolling.
- Work status shows3messages and7tool calls; totals show1minute working and
  2minutes10seconds completed waiting.
- The question footer remains outside the scrolling answer body at1440x1000,
  1280x720,1024x600,390x844,390x600 and780x422. Actions and composer stay within
  the viewport, with no horizontal document overflow. Both questions submit.
- Archived timing is fetched once, remains frozen after16seconds, and shows
  neither an open trailing wait nor an unavailable-update warning.

The first run exposed the missing activity GET alias in the portal session API.
Runtime8d3d44c fixes it through the existing shared conversation resolver. The
next run verified all active behavior but the archived fixture client rejected
its second thread ID. Correcting the fixture to use its declared identity
validator made the full run pass; no production archive fix was needed.

Structured geometry/results and seven screenshots are in artifacts/conversation/.
Root visually inspected desktop and390x600 captures. The temporary HTTP server
was stopped after acceptance.
