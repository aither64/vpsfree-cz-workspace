# Load browser acceptance modules through the page

A Firefox Selenium execute_script call that dynamically imported conversation.js
created a WebDriver sandbox module instance. The shared client then failed with
`fetch called on an object that does not implement interface Window` even
though the normal portal import worked. The controller's generic error was not
a product network failure.

Serve the acceptance bootstrap as a JavaScript resource and append a
`script type=module` with its src. Its imports run in the ordinary page global.
Instrumenting client methods exposed the exact error; the existing HTTP
endpoints returned 200. Related: work/2026-09-13-portal-recovery/.
