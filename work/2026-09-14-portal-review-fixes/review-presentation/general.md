# General review

## Findings

No Blocking or Important findings.

### G1 — Advisory: a successful status read erases a failed Keep open save

Runtime commit `774db1205a0cd653b687cec34e788eabd6a9f1c1`,
`portal/internal/web/static/app.js:1487` and `:1493` (with `:1455`).

When the hold POST fails but the following GET succeeds, the catch briefly
shows the save error and its diagnostic. The unconditional `loadAutoArchive()`
then calls `renderAutoArchive()`, which clears both. The checkbox correctly
returns to the server's saved value, but the operator loses the explanation
for the rejected change. This regresses the previous behavior, where the
save error remained visible.

A focused Node VM check using the actual archival UI block, a rejected POST,
and a successful GET confirmed the final state: `savedHold: false`,
`statusHidden: true`, empty status text, `detailsHidden: true`, and empty
diagnostic. No browser or long integration test was run.

Consider preserving the mutation error and its raw diagnostic while updating
the authoritative settings from the reconciliation GET. Clear it on an explicit
retry or later settings reload. Extend the existing `failHold` browser case to
assert the error after the GET completes; it currently checks only the checkbox.

## Scope and history

Reviewed the packet, initiative plan/state, relevant local instructions, and
committed follow-up deltas:

- Runtime `b837f0d` → `774db12`: `28a49ea` sticky headings, `88955af` compact
  sidebar, and `774db12` archival presentation. Each has one logical behavior
  with its supporting coverage and an explanatory commit body.
- Organization extension `f6050a4` → `109e9de`: runtime input revision and
  matching lockfile only.
- Workspace `1c3f3e1` → `a24742a`: organization/runtime input revisions and
  matching lockfile. The intervening shared-master tracking commit is outside
  implementation scope.
- Provider remains `882c88c`, unchanged.

The optional comparison callback has a default and remains internal. Sidebar
navigation retains explicit accessible names; the shared index layout retains
its narrow-screen override. Sticky headings remain constrained by their file
sections. The archival adapter preserves raw command/error text through
`textContent`, leaves the API and stored data untouched, and makes the merged
rule conditional. The package pin chain matches the reviewed revisions.

## Verification and residual gaps

Reviewed the new projection/browser coverage and the existing editor reveal,
session-template, shared limits-template, archival API, and CLI state contracts.
`git diff --check b837f0d 774db12` passes. The focused failed-save check above
was the only executable behavior probe added during this review; project code
was not edited.

Chromium/Firefox acceptance, packaged checks, CI, and deployed inspection are
intentionally pending this review. Confirm the index page's narrow limits
popover as well as session comparisons during acceptance: its shared CSS moved,
but the new presentation fixture exercises session pages only. Visual sticky
boundaries, long-path geometry, and browser scroll timing still depend on the
planned browser runs.
