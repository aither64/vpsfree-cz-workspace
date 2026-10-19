# Final narrow correction and pins

Reviewed runtime 911ed529 -> 987a01b adds only the required hasOlder: false and
olderCursor: null fields to the optional-question Chromium transcript fixture.
Parent inspected exact diff; corrected actual-template browser test passed.
Runtime package, including Go and browser contract checks, also passed.
No application behavior or accepted contract changed. Mandatory review narrow-fix
policy applies; original independent report remains authoritative.

Workspace rebased cleanly onto 5db0097a (tracking-only baseline updates).
Final workspace/configuration pins select 987a01b, same codex-web 641907fb,
unchanged extension and unrelated inputs. Matching-lock contract passed. Each
complete feature series is one logical commit; all repeated pins consolidated.
No migrations, no prior deployments, no default-branch integration authorized.

Codex-web CI 39320306357 passed. Cancellation of obsolete runtime911 CI
39320488089 returned HTTP403: token lacks workflow-cancel access. Earlier
obsolete f2 CI completed successfully. Final runtime987 CI39321999346 remains
in progress as of last read; no blind rerun.
