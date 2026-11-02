# Package B checkpoint

Owner: implementer1, retained gpt-6.1-sol/xhigh/workspace_write.
Identity verified from this tracking directory with `dev-session current`; both
DEV_SESSION identity variables absent. No saved settings were changed.

## Implemented, uncommitted

In the assigned dev-workspace worktree at base
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`:

- One Resources sidebar entry with Clusters/Reservations/Services nested panels.
  Existing child hashes, legacy tab queries, history, reload and keyboard/ARIA
  behavior remain supported. Existing cluster/reservation controls remain.
- Separate compact counts; confirmed zero hides, unknown stays visible, stale
  last-known values (including zero) carry a marker and observation timestamp.
  Reservation counts use the existing complete incarnation-bound holder summary.
- Cluster reader separates proven presence from diagnostic cards and scopes its
  cached observations by session incarnation. Stopped owned clusters count.
- Team counts lead plus all nonremoved roster members, independent of readiness
  and activity. Counts apply with the accepted table refresh, deferring edits.
- Details requests/replies fence exact session observation identity; no new
  poller or read-side lifecycle/activity mutation.
- Portal docs describe count meanings and navigation. Lead applied the required
  writing guidance; all five requested wording edits were applied exactly.

The Services panel still contains a temporary unavailable placeholder. Service
reader/host compatibility/packaging and VM fixtures wait for the architect's
frozen persisted state, public JSON reader and capability contract. No dependent
implementation has begun.

## Quick evidence

Repository Nix shell, `--no-update-lock-file`, readonly Go modules:

- Full `go -C portal test -mod=readonly ./internal/cluster`: passed.
- Focused web tests for count semantics, Team membership, nested template,
  observation rejection, session page/details and asset cache identities: passed.
- Node syntax checks of app/coordination and changed cluster-control browser
  fixture: passed.
- Node resource-count and coordination browser-unit tests: 16 passed.
- `git diff --check`: passed.

Exact observation-header acceptance and rejection roundtrips also pass. Existing Playwright cluster controls now also cover
Resources child navigation/history/reload/keyboard and service read-only DOM;
that long browser suite has not run, per the final-review ordering constraint.

No Git mutation, long/integration/VM check, live session/service inspection,
lifecycle operation, deployment, claim or merge was performed. Implementer0 owns
the Git lane. Lead coordinates any long-check watcher (one utility slot).

## Next action

Receive architect's frozen public reader and package-state compatibility contract;
implement remaining B source/tests/docs, send final service wording inventory,
complete quick checks, request the complete-package Git lane, then hand committed
results to lead for mandatory final independent review.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
