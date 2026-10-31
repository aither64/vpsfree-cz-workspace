# Complete final branch inventory

## dev-workspace

Base 17222c374bf48c65edc36895e07408c65f1e7b53; final head f145d3b8fa275932ee7837bba33568f29635d36f.

```
f145d3b8fa275932ee7837bba33568f29635d36f
portal: keep activity status compact and timers steady

Shorten the work-row labels while retaining full hover and accessible
descriptions. Separate right-side message/tool counts from elapsed time
only when both are present.

Reserve the timer width and use tabular digits so ticking seconds and
unit transitions do not shift the counters. Preserve activity, freshness
and attention rules; this changes no backend or persistent format.

```

 docs/workspace-portal.md                           |  30 +++---
 portal/internal/web/browser_contract_test.cjs      |  31 ++++--
 portal/internal/web/presentation_browser_test.cjs  |   7 +-
 portal/internal/web/static/app.js                  |  54 ++++++++---
 portal/internal/web/static/style.css               |   8 +-
 portal/internal/web/team_activity_browser_test.cjs | 105 ++++++++++++++++-----
 portal/internal/web/templates/session.html         |   6 +-
 7 files changed, 180 insertions(+), 61 deletions(-)

## workspace

Base 37fb70827b23a131104493c21f183ce4fe8f48a5; final head 51683b15ffb751174c4e0b875cfd4d1612f4755c.

```
51683b15ffb751174c4e0b875cfd4d1612f4755c
workspace: select compact and steady Codex status row

Select the portal with short activity labels, a counter/time separator and
stable timer width. Preserve the extension and provider inputs while
matching the aitherdev host runtime selection.

```

 flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)

## vpsfree-cz-configuration

Base b2d8c1b787284a4e2973fe5f3609aadca9cf03d0; final head 01c8350d0d07b7613c3893e5cd8666bface9c47b.

```
01c8350d0d07b7613c3893e5cd8666bface9c47b
inputs: set devWorkspace to f145d3b8

devWorkspace: 17222c37 -> f145d3b8
git log for 17222c374bf48c65edc36895e07408c65f1e7b53..f145d3b8fa275932ee7837bba33568f29635d36f
> f145d3b portal: keep activity status compact and timers steady

```

 flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)

## History, correction and migration disposition

One coherent bounded UI commit includes supporting contracts/docs; one exact
pin update per consumer stream. No superseded commits, compatibility paths or
migrations remain. No branch was released/merged/deployed before consolidation.
Corrections after independent review are fixture-only; product code is unchanged.
They fix clock initialization and asynchronous fixture-read races. Lead checked
direct corrections and pins under narrow-fix review policy. Each update stream
is consolidated; config changelog matches the true base-to-final pin. Scheduled
upstream config updates remain in the base. No migrations: release, deployment
and external-consumption provenance are inapplicable.
