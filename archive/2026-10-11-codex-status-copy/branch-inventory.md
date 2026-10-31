# Complete final branch inventory

## dev-workspace

Base 17222c374bf48c65edc36895e07408c65f1e7b53; final head 356f6a9930bb8b0749079069038c67695404e825.

```
356f6a9930bb8b0749079069038c67695404e825
portal: keep activity status compact and timers steady

Shorten the work-row labels while retaining full hover and accessible
descriptions. Keep message and tool counts on the right beside elapsed
time.

Reserve the timer width and use tabular digits so ticking seconds and
unit transitions do not shift the counters. Preserve activity, freshness
and attention rules; this changes no backend or persistent format.

```

 docs/workspace-portal.md                           |  30 +++---
 portal/internal/web/browser_contract_test.cjs      |  31 +++++--
 portal/internal/web/presentation_browser_test.cjs  |   7 +-
 portal/internal/web/static/app.js                  |  51 ++++++++---
 portal/internal/web/static/style.css               |   7 +-
 portal/internal/web/team_activity_browser_test.cjs | 102 ++++++++++++++++-----
 portal/internal/web/templates/session.html         |   6 +-
 7 files changed, 173 insertions(+), 61 deletions(-)

## workspace

Base 37fb70827b23a131104493c21f183ce4fe8f48a5; final head 0835fb7f4e99fc8c9e36c5892e340c4bf7d5c16f.

```
0835fb7f4e99fc8c9e36c5892e340c4bf7d5c16f
workspace: select compact and steady Codex status row

Select the portal with short activity labels and a stable timer width.
Preserve the extension and provider inputs while matching the aitherdev
host runtime selection.

```

 flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)

## vpsfree-cz-configuration

Base b2d8c1b787284a4e2973fe5f3609aadca9cf03d0; final head b18412bfdbec545312469f581f2991bcf6c237d5.

```
b18412bfdbec545312469f581f2991bcf6c237d5
inputs: set devWorkspace to 356f6a99

devWorkspace: 17222c37 -> 356f6a99
git log for 17222c374bf48c65edc36895e07408c65f1e7b53..356f6a9930bb8b0749079069038c67695404e825
> 356f6a9 portal: keep activity status compact and timers steady

```

 flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)

## History, correction and migration disposition

One coherent bounded UI commit includes supporting contracts/docs; one exact
pin update per consumer stream. No superseded commits, unused compatibility
paths or migrations remain. Previous exact deployed heads are retained in each
repository under tag dev-deployed/2026-10-11-codex-status-copy-v1; this is source
retention for the live development rollout, not a release. Rollout evidence stays
in rollout.md. The follow-up removes only the rejected separator, its styling
and update logic, adjusts existing tests/docs and bumps browser asset versions.
Timer width/tabular digits and activity semantics remain. Each pin stream is
consolidated; config changelog matches the true base-to-final pin. Scheduled
upstream config updates remain in the base. No migrations: migration release,
deployment and external-consumption provenance are inapplicable.
