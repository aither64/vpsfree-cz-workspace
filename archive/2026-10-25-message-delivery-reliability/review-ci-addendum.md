CI 40181256989 on runtime 9bf42821 failed its package prerequisite, so VM tests
never executed. Complete failed log: /tmp/message-delivery-reliability-2026-10-25/runtime-ci-failed.log.

Three test fixture failures:
- auto_archive_test.go:45 hardcodes app.js?v=59, while the actual bundle is v60.
  The independent asset-version test already enforces the current minimum.
- composer_handoff_contract_test.cjs and submission_notice_contract_test.cjs
  extract production functions into an isolated VM and omit deliveryRetries.
  Both throw ReferenceError before exercising their intended receipt behavior.

Parent is correcting only these three test fixtures: require a versioned app
asset without duplicating the version constant, and provide null deliveryRetries
in the existing isolated contexts. No application behavior changes. Focused
checks are running. This will be folded into the browser commit, final pins
refreshed and consolidated, and exact final heads provided. Continue reviewing
the current substantive design; inspect the narrow fixture diff if useful.
