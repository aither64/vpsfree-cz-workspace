# Campaign form rendering review

The committed delta from 4d53fa157 to fa3670345 adds a page-local reset of four
XTemplate variables after rendering the campaign settings and member retention
forms. It also checks the unique settings form and the first address's exemption
action in the browser scenario. The owning WebUI commit was amended.

Risk was classified high conservatively because broken exemption form boundaries
could affect protection from release. All four standalone reviewers used
`gpt-6-astra` with `xhigh` reasoning and fresh context:

- General: no findings. Independently reproduced the stale wrappers with actual
  XTemplate rendering and verified the reset preserves completed form content.
- Architecture: no findings. The local helper matches the existing security
  advisory page pattern and does not change the shared template interface.
- Risk and compatibility: no findings. CSRF fields, action and address ID remain
  in their own rendered forms; authorization and persisted state are unchanged.
- Scope: no findings. Four variables, two callers and two browser assertions are
  proportionate to the observed problem.

PHP syntax and the capacity contract test passed. The actual review-cluster page
now has one settings form, all exemption forms, and the member retention form.
Real OAuth logins passed for the administrator and both members. The updated
isolated browser scenario passed at 14:44 CEST, including VM teardown
(1242.72 seconds total; browser example 435.37 seconds). Its immutable Playwright
suite, campaign form, API models and API library match the final source byte
for byte. Final live logins and
screenshots were also checked after the services update to aa9ac1e3a.

After review, upstream master advanced to ff5d5e591 through the documentation
directory rename and a PHPUnit dependency update. The series was rebased to
`aa9ac1e3af0acde65e15fd2c9758d1613689fed0`; range-diff shows only the relocation
of the two new documents and their index additions from doc/ to docs/. API,
node, form and browser code are byte-identical to the reviewed head. The WebUI
contract test also passes with upstream PHPUnit 13.3.4. No additional review lane
is required for that mechanical rebase.
