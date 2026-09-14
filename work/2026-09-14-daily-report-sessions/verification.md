# Verification

Tested source revisions:

- vpsAdmin: `9456fae6f181cef2e8982eed462e873095fd49da`
- Notification templates: `08402ffd8010384f950b1ec4a1b95de8e5410ba3`
- Configuration: `5036135728832d5c375705e3b69949c33460ff7e`

| Check | Result |
| --- | --- |
| Report aggregation and actual text/HTML rendering | 17 examples passed |
| Migration up/down with row preservation | 1 example passed |
| RuboCop and commit hooks | Passed |
| Migration spec coverage | Passed |
| CI selector | 16 tests / 55 assertions passed |
| Notification template flake check | Passed |
| Delivered-mail integration | Passed, including every new report section |
| API1 and API2 configuration builds | Passed; exact input revisions in build-results.json |
| Mandatory functional and configuration reviews | No Blocking or Important findings |
| API CI | All 27 jobs passed |
| Migration, lint, i18n, libnodectld and template CI | Passed |
| Full VM CI | Queued on shared runners at handoff |

The renderer checks populated, empty, and older payloads, plus HTML escaping.
Fixed-time examples cover token/refresh expiry, account restrictions, permanent
credentials, auth splits, distinct users, and recovery terminal-state precedence.
The delivered integration report records 36 HTTP Basic sessions from one user,
with zero active sessions, demonstrating the immediate-close semantics.

Synthetic EXPLAIN selects the new indexes; production index-build costs were
not measured. A later deployment must run the migration explicitly because
API database autoSetup is disabled. No live systems were changed.

Remote checks and any outstanding queued run are recorded in state.md.
