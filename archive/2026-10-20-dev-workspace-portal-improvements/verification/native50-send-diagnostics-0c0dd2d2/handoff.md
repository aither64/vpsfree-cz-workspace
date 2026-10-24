# Native Firefox send diagnostics handoff

Published clean B `f00e67833dce74621b3f20643273364c9cbbbc10` over ordinary
SSH, exact lease `0c0dd2d22ce4e03c22a7bd0c471267deb6ee3a2a`.
Remote master remains `968646471b1190c16a8cf60ff50736cd0525fa3f`.
B source/index/Git ownership is returned to the lead.

Only `portal/internal/web/firefox_tabs_acceptance.cjs` and
`portal/internal/web/firefox_tabs_test.go` differ from the original head:
35 insertions, 6 deletions. Payload-free pre-click/failure telemetry retains
mutation totals, send availability, nonempty/expected-draft booleans, form
validity/submitting, bounded submit/invalid event counters and receipt state
category counts. The existing fixture status adds last message handler status,
loss attempted/injected and hijack-error booleans. No message or attempt IDs,
text, storage, profile details or credentials are emitted.

Native click, Retry original predicate, all acceptance deadlines, 50 native
tabs, 35-second foreground, hidden-zero, 10-second pending gate and final
2 POST/1 dispatch/1 journal assertions remain unchanged. No product change,
behavioral fix, acceptance result or incident-wide recovery claim is made.
The prior failure cannot establish submission or loss injection; these fields
are for the parent's one fresh diagnostic run after affected inspection/review.

## Quick evidence

The existing `quick.log` records successful repository-Nix commands:

```sh
node --check portal/internal/web/firefox_tabs_acceptance.cjs
gofmt -w portal/internal/web/firefox_tabs_test.go
test -z "$(gofmt -l portal/internal/web/firefox_tabs_test.go)"
go -C portal test -mod=readonly ./internal/web \
  -run '^TestFirefoxFixture(JournalReconcilesOriginalAttempt|Readiness)$' \
  -count=1 -v
git diff --check
```

Both focused Go tests pass; package duration 0.388s. Ordinary Nix git commit
and autosquash completed without bypasses; no declared hook framework or active
pre-commit hook is present. No browser, package, full suite, probe, CI query,
cancellation, dependency/pin update, deployment or lifecycle action was run.

## Exact source/history evidence

`source-proof.json` binds passing and reconstructed tree
`f15121d901667e1af0c50d462445208ed4e8ee66` to the final head.
The original head plus saved `diagnostics.patch` reconstructs that exact tree;
all 527 other blob/mode entries are identical, including all product files,
other fixtures and the sole A dependency. Eighteen logical groups remain;
only native fixture group 13 changes patch ID, all 17 others are stable.
The original head is retained under the explicit before-native50-diagnostics
safety ref; `safety-refs.txt` inventories retained refs. Old receipts and failed
launchers were not changed. `series-{before,after}.txt`, `range-diff.txt`,
`patch-ids.json`, `final-delta.patch` and `base-to-final.patch` preserve the
complete history and source boundaries. No migration or schema change occurs
in this diagnostic delta. Existing branch-wide migration/design dispositions
remain with the lead's retained independent review packet.

No product documentation update is useful for temporary fixture telemetry;
this evidence packet records its purpose and limits. The lead owns shared
state/portal tracking and the next affected review/runtime action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
