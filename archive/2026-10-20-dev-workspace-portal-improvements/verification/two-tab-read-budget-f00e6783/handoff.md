# Targeted two-tab read-budget handoff

Clean SSH-published B: `bc40cdda2d28c9732396db4163daa244bba79acb`.
Exact publication lease: `f00e67833dce74621b3f20643273364c9cbbbc10`.
Remote default remains `968646471b1190c16a8cf60ff50736cd0525fa3f`.
Implementer2 returns B source/index/Git ownership to the lead.

Implements `design.md#targeted-read-performance-replacement` within only
`portal/internal/web/firefox_tabs_test.go` and
`portal/internal/web/firefox_tabs_acceptance.cjs` (81 additions, one deletion).
`TestFirefoxReadBudget` requires its separate explicit opt-in and selects
`--read-budget`; unknown runner modes fail. The direct early branch creates
exactly two native Firefox tabs and returns through the existing owned cleanup.
The old 50-tab body, budgets and assertions are byte-identical and are not the
selected replacement. No future 50-tab run is requested or authorized.

The new scenario waits for initial transcript/pending/single-SSE readiness,
retains a tab-0 draft, settles background reads before baselining, observes one
5000ms interval under unchanged 200ms hints, checks hidden zero deltas/active
counts over the union of lane keys, foreground transcript progress/one SSE and
pending delta <= 1 + floor(observedWindowMs/15000). One switch back requires real
hidden-then-visible events, retained draft, fresh pending and a new single SSE;
the other tab settles. Existing typed question/removal and 5-second guards
precede one pending503 and subsequent GET within the existing 10-second guard.
Final mutation totals must all be zero. No sends/discards/restoration/soak occur
in this mode; it makes no claim about the separate live transport incident.

## Quick evidence

`quick.log` records repository-Nix PASS for the three existing Node suites
(read_cycle, codex_providers, attention): **107/107**, 7.715s. These include
existing current-function pending freshness/backoff coverage; no duplicate
component tests were introduced. CJS syntax, gofmt/check and diffcheck pass.
Existing Go journal/readiness tests pass (Go package 0.387s); both TestFirefoxTabs
and TestFirefoxReadBudget skip with their opt-ins explicitly absent.
No browser, package/full suite, CI query/wait/cancellation, live/probe, pin,
activation, default integration or lifecycle action occurred. No A files or
checks were changed/run; the unchanged A sync contract suite and retained exact
receipts remain under parent verification ownership.

## Source/history proof

`source-proof.json` binds quick-tested, folded and reconstructed tree
`689be4475db5aae85451e965df7e5a4523021987`. Saved `read-budget.patch` applied to
original f00 reconstructs that tree exactly. All other 527 blob/mode entries are
identical, including product/assets/other fixtures/sole A dependency.
The 18 logical groups remain; only native fixture group 13 changes patch ID,
with 17 other stable patch IDs equal. No new migration/schema/API/wire/cache or
state change is present in this test-only delta. The original f00 safety ref,
earlier refs and all prior failed/partial/quick evidence are retained.
`series-before.txt`, `series-after.txt`, `range-diff.txt`, `patch-ids.json`,
`final-delta.patch`, `base-to-final.patch` and `publication-proof.json` provide
the complete review boundary and publication evidence. Existing whole-branch
migration dispositions remain in the lead's retained review packet.

No project documentation expansion is useful for this narrowly scoped fixture;
the architect brief and this packet record the selected replacement and limits.
Lead owns shared state/portal updates, focused committed-deliverable review,
one short native run and downstream pins. No runtime performance acceptance is
claimed yet. Parent's browser argv, from B portal with prepared display/binaries:

```sh
env -u PORTAL_FIREFOX_TABS_TEST PORTAL_FIREFOX_READ_BUDGET_TEST=1 \
  go test -mod=readonly ./internal/web -run '^TestFirefoxReadBudget$' -count=1 -v
```

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
