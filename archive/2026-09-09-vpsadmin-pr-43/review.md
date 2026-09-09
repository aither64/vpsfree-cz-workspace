# Review of vpsAdmin PR #43

Reviewed commit `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1` against
`3a64784708faef5e9f4f093255954b14e396904c`.

## Finding

### P3 / Advisory: describe the new from_id cursor requirements

Location: `plugins/payments/api/resources/user_payment.rb:71-73`.

The new implementation looks up `from_id` inside the current authorized,
filtered query and continues after that row in `created_at DESC, id DESC`
order. A nonexistent cursor or one outside the selected filters now returns
an empty page. However, the inherited HaveAPI 0.29.8 OPTIONS description
still says “List objects with IDs greater or lower than this value”. That
promises a numeric threshold and does not describe the new lookup requirement.
For example, an admin sending a numeric upper bound that is not a payment ID
gets no results even when smaller payment IDs exist.

Override the parameter description for this action in English and Czech to
instruct clients to pass the last payment ID from the previous page with the
same filters. Describe the empty-result behavior for an unavailable cursor.

This is a documentation issue. Changing pagination to follow the declared
creation order is the explicit purpose of the PR. The existing WebUI passes
the last returned payment ID, and no inspected consumer relies on arbitrary
numeric thresholds. Do not revert the ordering correction to address this note.

## Review assessment

No Blocking/Important correctness, authorization, migration, or architecture
findings. General, architecture, and scope lanes found no issues. The risk
lane's initial concern about a breaking numeric-threshold contract was
reconciled to the advisory metadata mismatch above after inspecting the stated
PR intent and the existing WebUI caller.

All four reviewers used fresh contexts, `gpt-5.6-sol`, and `xhigh` effort.
No project code was changed, and no GitHub review/comment, push, merge, or
production mutation was performed.

## Verification

- Committed diff whitespace and Ruby syntax passed.
- RuboCop: four changed Ruby files, no offenses.
- Focused payment API spec: 20 examples, zero failures.
- Isolated migration up/down spec: one example, zero failures.
- Combined original suite and seven boundary probes: 27 examples, zero
  failures. Probes covered tied timestamps, resolved associations, timezone
  offsets, standalone bounds, filtered counts, foreign cursors, invalid dates,
  and inverted ranges.
- GitHub PR checks: 63 successful checks, with the PR head unchanged on recheck.

The initial fresh-shell bundle resolved incompatible JSON 3.0.2 and failed
before examples. Seeding the ignored API lockfile from the committed packaged
lock retained JSON 2.21.2 and made the focused suites pass. This is a baseline
development dependency issue, unrelated to the six-file PR diff.

## Residual limits

No production-scale index build timing or query-plan measurement was performed.
Use the normal migration window and deploy the API before its dependent WebUI
Next finance feature. That companion frontend revision was not supplied and
was not exercised. The committed OPTIONS spec checks parameter names rather
than the exact Czech/English text; the locale values were inspected directly.
