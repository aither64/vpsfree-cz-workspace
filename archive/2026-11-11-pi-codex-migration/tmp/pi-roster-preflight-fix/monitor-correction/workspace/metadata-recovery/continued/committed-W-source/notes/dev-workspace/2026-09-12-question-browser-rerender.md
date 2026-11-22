# Question choices replace the browser form

The real question acceptance test selected an option, then read buttons from
a saved Selenium form element. The selection rerendered the form and raised
StaleElementReference. Reacquire the current form/action, or perform the lookup
and click in one synchronous browser script, instead of retaining DOM nodes
across the choice update. The controlled browser already verified answer
submission and fixed action geometry separately.

Keep the owned portal connection alive while recovering this browser failure.
The harness finally block closed it with a question pending. Codex retained the
exact active waiting turn after restart, and activity still reported waiting,
but the new portal connection did not receive the original interactive request.
The real answer/closed-wait subcheck could not finish and remains unverified.
After identity checks, the test interrupted only its exact owned turn and
continued the independent old/new package check. No additional question was
sent to disguise the missing coverage.

Related initiative: work/2026-09-12-portal-review-experience/.
