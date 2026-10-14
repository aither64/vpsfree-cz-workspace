Frozen narrow E test-fixture hostname correction

Hosted CI37678050938 at Ef6d2c080469b224ac77765aecd76a6d531358363
failed organization-source and named only test/fixtures/kb-config.json. Its
copied deployment hostname suffix violated E's existing portable-source rule.

Only that fixture changed: 17 strings replace .aitherdev.int.vpsfree.cz with
.example.test (11 domains, four tmpDomains, two DNS serverName fields). Schema,
keys, non-hostname values, formatting, numeric resources, addresses, credentials,
ports and topology stay exact. No test expectation needs a change: its only
reference is flake.nix's optional testKbSiteConfig.clusterDefaults.kb. Provider
packaging sees portable names through the same immutable config path; application
semantics, selected inputs, guards and production configuration remain unchanged.

Read-only JSON/source inspection passed: parsed JSON, exact replacement-only
bytes and shape, 17 distinct example hostnames, no forbidden content/path name
in tracked E files. This is not local CI, package evaluation or test execution.
The user's no-local-CI constraint was respected. No suite/build/VM/ref/GitHub
operation launched, and no commit or index mutation occurred. Prior checks and
original-snapshot review do not certify this new draft. Parent owns acceptance,
normal history consolidation/publication and hosted evidence.

No product/prose/guard/allowlist/K/D/pin change or broader implementation is
needed. All source and frozen receipts now held for root inspection.
