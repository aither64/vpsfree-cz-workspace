# New/refreshed notification tabs

User requirement: notifications use the current worker on a new or refreshed
page while other portal tabs remain open. User explicitly excludes preservation
of old-tab notification behavior. No session or subscription data reset.

Current consumed source4ed9af55/workspace750ab33c/configurationc90e56d5 and their
sealed receipts/evidence stay preserved. Source correction is a separate owning
commit; superseded consumer selections will be preserved under exact refs before
consolidating final own input updates. Existing held reservation1956d2a0 covers
authorized redeployment. No default integration or lifecycle action is requested.

- [x] Current source cause identified: no install skipWaiting, waiting copy.
- [x] Architect design.md addendum: automatic activation; no tab-close workflow.
- [x] Implementation and main-agent copy pass.
- [x] 37Node,2Go,4syntax/diffPASS; separate source e208027f committed.
- [x] Independent affected source/7history/no-migrations review; narrow Advisory directly remedied at46975718.
- [x] Exact46975718 real-browser regression PASS31s: Firefox+Chromium oldactive/waiting takeover with retained tab/draft; Chromium synthetic Test correlation.
- [x] Published source46975718 and final consumer selections workspacebce98429/config40172e5f.
- [x] Complete downstream composition/history/no-migration review PASS no findings.
- [x] FullflakePASS14m33s/recovery462.54s; same-head CI38760306881 fastPASS, hostskipped.
- [x] Exact preparation recovered from GC interference; machinePASS100s/profilePASS5m44s.
- [x] Ordered machine81c0f179/profile7ec26475 succeeded; independent live/served proof PASS.
- [ ] User Firefox/macOS actual display and click acceptance.

This fixes worker activation without asserting a cause for the preserved Linux
Firefox display rejection or the physical macOS symptom. Keep tests and platform
appearance separate. Stop at any new failed check and preserve its evidence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/

Final outcome: notification-activation-acceptance.md/json. Scope correction
deployed; physicalFirefox/macOS display/click remains separate. No ownedrun
remains; keep session/reservation and unmerged heads.
