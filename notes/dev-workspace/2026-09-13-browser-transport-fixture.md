# Delay the fixture server when testing browser response ordering

In the plan-decision Selenium acceptance, replacing window.fetch after page load
did not intercept portal recovery requests: the initialized client retained its
original fetch function. The wait for the injected release callback timed out,
without exercising the intended race. Hold the response in the owned fixture
server instead, expose status/release endpoints that emit no conversation event,
and release only after the transcript has observed the request. This exercises
the actual client transport. Related initiative: work/2026-09-12-portal-file-uploads.

Verification: the server-held recovery test passed without a subsequent event.
Observed receipts intentionally hide their duplicate receipt banner; to test a
visible accepted receipt, hold transcript correlation as well as acknowledgement.
