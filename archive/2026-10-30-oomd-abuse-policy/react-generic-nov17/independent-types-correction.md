# Independent draft typecheck correction

Initial pinned application typecheck exited2 after73.008s. It found only three
TS2769 errors in VpsIncidentSettingsEditor.test.tsx: a Playwright-style exact
option was incorrectly passed to Testing Library getByRole. The role query
accepts name and already matches a string name exactly; removing the unsupported
option preserves assertion strength and actual intended matching behavior.
No product, API, SDK or mutation behavior changed. The initial native19671 log,
exit and exact command receipt remain unchanged; first-failure stop meant locales
and docs did not run. The two-file5-test pass remains its original runtime scope,
not final SDK/type proof. Fresh type acceptance is pending; do not infer it from
this mechanical source correction or a syntax-only check.
