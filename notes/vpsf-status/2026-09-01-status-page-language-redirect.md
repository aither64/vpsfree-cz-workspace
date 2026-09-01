# Status page integration checks need an explicit language

Initiative:
`work/2026-09-01-security-advisory-lists`

Command:
`./test-runner.sh test status-page`

Symptom:
An HTML assertion against `/` timed out even though the status service was
running and `curl` returned successfully.

Cause:
The root path redirects to `/?lang=en`. The test helper did not follow
redirects, so it repeatedly inspected only the small `Found` response body.

Fix:
Request `/?lang=en` directly when an integration example needs to inspect the
rendered English index page.

Verification:
The focused security-advisory VM example passed after using the explicit
language URL.
