# General review

Reviewed the complete committed functional ranges:

- `vpsadmin`
  `791ab3aa89e2f613979da6090b89785c78245db5..8769884ae69b03c22d8532fd09acf6de85542015`
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..4dc2706df6332d235cad18c1202602004b75d63c`

The review covered the commit series and final trees against `plan.md` and
`review-packet.md`, including repository guidance, aggregation SQL, credential
and password-recovery lifecycle paths, built-in and organization templates,
migration/schema changes, focused specs, selective CI mapping, and delivery
assertions. The later configuration-pin commits are outside this functional
phase.

## Findings

No Blocking, Important, or Advisory findings.

The vpsAdmin commit has one coherent report-feature purpose. Its four indexes,
schema representation, aggregation, built-in renderer, focused regression
coverage, selector mapping, and delivered-message assertions support that same
behavior and are explained by the commit message. The organization-template
commit is a clean consumer commit. Both messages follow their repository
conventions, and both ranges pass `git diff --check`.

The implementation preserves the rolling half-open event window, computes
overall distinct users independently of authentication-type rows, includes
unexpected stored session types in created totals, and treats permanent and
administrator-created sessions as overlapping active subsets. The active query
matches the relevant token and OAuth2 refresh expiry comparisons and account
flags without changing authentication behavior. Recovery classification uses
the deadline applicable at the report cutoff, gives completion precedence,
keeps early invalidation separate from expiry, and excludes pending attempts
from unfulfilled counts. The HTML renderer escapes database-derived mechanism,
reason, and fallback labels. Both new templates omit all added sections when
used with an older generator payload.

## Residual risks and test gaps

- The long `alerts/lifetime-and-daily-report` integration scenario has not run
  yet. Its committed assertions cover delivery and the presence of every new
  text section, while the focused RSpec rendering covers populated, empty, and
  old payloads in both text and HTML.
- Active-state totals are several eager queries rather than one database
  snapshot. A session or account changed during the short aggregation interval
  can make the current-state rows differ slightly from one another. Period
  events still use the one captured cutoff, and recovery terminal states retain
  timestamps that are compared to that cutoff. No concurrency regression
  measures this small snapshot-consistency window.
- Production-table query plans, report runtime, and live index-creation impact
  have not been measured in this functional phase. The focused checks establish
  query semantics and reversible schema shape; deployment compatibility and
  migration operational risk belong to the separate risk/compatibility review
  and later configuration validation.
