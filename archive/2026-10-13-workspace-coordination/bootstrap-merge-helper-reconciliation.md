# Dated integration helper checks

Astra/xhigh design accepted in bootstrap-merge-lead-acceptance.md. Implementation
uses selected Host admission and Engine APIs; no owning runtime edit or installed
permission change. Initial draft checks pass 7 tests / 40 assertions, using real
ordinary workers on private Git repositories, including shared-root master with
unrelated staged and unstaged content preserved. Fixtures cover exact preparation
and completed execution retries, approval-only interruption, condition/evidence/
generation refusal, other pending owner work and claim-without-request recovery.

The first check invocation used relative draft paths from runtime CWD; copied no
code and exited on missing test file. The accidentally created empty directories
were removed precisely. Logs retained. The first shared-root fixture omitted the
machine's updated configurationRepository catalog mapping; corrected fixture
matches the workspace registration/catalog and all seven checks pass. No production
failure or unexplained rerun. Existing runtime tests own FIFO, capacity, hooks,
worker/recovery interruption and mixed-version formats; the helper does not copy
those mechanisms. Final committed helper and installed-runtime fixture checks
remain after the frozen creation-fix rollout. Source-only application derivation
identity is captured before modification and must match after the helper commit.

The same seven checks also pass with Host/Engine/Worker reloaded from the exact
candidate package m12vcm73v1ld944ay9j284r5ikyi9x2n (7/40). The retained owning test
fixture loads its source setup before the installed classes; Ruby warns about
constant redefinitions. Actual production method bodies come from the installed
package, and fixture overrides are limited to private paths and dispatch, not
helper or merge behavior. Warnings and full log retained. This explicitly covers
the selected package interface used by the source-only route.
