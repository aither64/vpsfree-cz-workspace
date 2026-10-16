# Notification activation: narrow Advisory remedy

Frozen clean final head `469757183ba9491d642b56e91658dc64e390647b`.
Unchanged parent/deployed head `4ed9af55127743b7564cb4dd01d10c9f7fee5120`;
first six commit objects unchanged. Reviewed e208 preserved before amendment at:
`refs/session-evidence/2026-10-14-i-d-like-the-dev-workspace/notification-activation/reviewed-e208027f`.
Original packet remains hash-identical and the review boundary/report is retained.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

The lead accepted reviewer0's Advisory for direct step9 verification. Explicit
action invalidation now replaces canceled readiness progress with the existing
approved unconfirmed/limited message. A canceled old observation remains unable
to publish. Test and Disable no longer leave indefinite Updating text; Enable
uses the same action invalidation. No update loop, new copy, protocol, persisted
field, cleanup or deadline change. No docs change needed.

Only client browser-notifications.js and owning attention_browser_test.cjs changed,
29insertions/6deletions. notification-activation-remedy.patch is the exact
reviewed-e208->final delta. Original seventh message/rationale retained with normal
git commit --amend -F body-file; no hooks bypass. The first six deployed objects
were not amended.

Quick declared Node24.19.0 checks only:

- actual-module Node38namedPASS,0failures/skips,2.279s;
- changed client and contract syntax PASS;
- git diff --check PASS.

Logs/status and quick-results are under notification-activation-remedy-*.
The new contract covers Test/Disable during both activation and capability waits,
then advances beyond the old10sdeadline and asserts no Updating text, no lingering
observers and no update loop. All37earlier contracts remain. No unchanged Go,
real browser, native/provider/network/host/daemon/queue/lifecycle check ran.
No source publication/pins/operations. Lead owns direct narrow verification and
later finite checks; no confirmation-only reviewer rerun requested.

The old22file notification-activation artifact manifest still passes unchanged.
No old bundle/packet retargeted or rewritten. One amended inventory/delta plus
focused logs is sufficient; original inventory holds full behavior/compatibility/
prepared two-tab fixture details. The actual browser fixture remains UNRUN.

No API, server/private format, browser schema, migration, dependency or vendorHash
change. Original notification/helper/receipt/capability-journal lineage unchanged.
Old loaded tab semantics are intentionally outside the narrowed notification
requirement. Original failed browser ordering and physical Firefox/macOS causes
remain unproved.

Final seven-commit series over integrated832d9f1:

```
96717cdeb5f733391846a95d78c117068ce77de8 portal: show session attention and deliver background Web Push
bb9e6291bec10227c961c36559fba406938f1eaa provider: retain bounded failure context before compensation
6e1d9a191724d376cad2a71f234f0e4d1c01f36f processgroup: make descendant exit assertions identity-aware
867682c3df251fbe6941ff9a667539ae1af790ec portal: move browser notifications into the workspace menu
012f6184faa62b7d476555058f1473adcd908528 portal: report correlated browser notification test outcomes
4ed9af55127743b7564cb4dd01d10c9f7fee5120 portal: remove the redundant session attention status row
469757183ba9491d642b56e91658dc64e390647b portal: activate notification workers while tabs stay open
```

Delta SHA256: `afcef50212bae33c3743dcb99fd7fdbb0655b6a479beedb0a2d52769b909af80`.
Client SHA256: `f52cc86cd86bb2a092bffe69f0956573e9ccb818bb82bc22a596fe03e841b415`.
