# B F1 history-read remediation

Final exact B feature head: **d617ef3968280e9955da85e2d7464a47030e7087**.
Base/default: **968646471b1190c16a8cf60ff50736cd0525fa3f**, unchanged by SSH proof.
Clean worktree confirmed after exact-lease SSH publication. This is the narrow
remediation requested by the completed four-lane review of B133d23f5; it does
not claim long package/browser acceptance or deployment.

## Correction and checks

History now owns its exact read-cycle object. Suspending clears that slot,
loading, owned deadline and retry timer immediately. Current results and errors
must match slot/generation/thread/repair version; retired finally only finishes
its own read. Resume schedules one bounded authoritative gap/citation repair
without the previous 100ms busy loop. A canceled manual older read can be retried;
loaded history/cursor and existing failure context remain retained. Only a current
successful read clears failure context. Genuine current deadline and401/403
failures remain visible; access errors do not automatically retry. No mutation
replay, paging contract, schema, authority or durable submission change.

The actual shipped-function deterministic fixture settles old SUCCESS and old
FAILURE after a successor starts, for interrupted older and repair reads. It
checks successor loading/controls/timers, no old rendering, coalesced resume,
manual retry/failure retention, citation backoff and current timeout/access errors.
A disposable negative control using reviewed133 app reproduces the old retained
boolean slot; its expected exit1 is saved in
[reviewed-negative-control.log](reviewed-negative-control.log) and
[structured result](reviewed-negative-control.json).

The first new fixture run found an old deadline remained until old finally;
the final suspension now explicitly finishes that owned deadline immediately.
Assertions were retained. The final focused batch passed:

```sh
nix develop --no-update-lock-file -c bash -c 'set -e
node --check portal/internal/web/static/app.js
node --check portal/internal/web/read_cycle_browser_test.cjs
node --test portal/internal/web/read_cycle_browser_test.cjs portal/internal/web/codex_providers_browser_test.cjs portal/internal/web/attention_browser_test.cjs
'
```

PASS **104/104,7.856s**, [Node log](node.log).

```sh
DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json \
nix develop --no-update-lock-file -c go -C portal test -mod=readonly ./internal/web \
-run 'TestShippedBrowserClientMatchesSessionAPI|TestSessionPageUsesPersistentSidebarAndSectionPanels|TestAutomaticArchivalPageIsSeparateFromIndex|TestCitation|TestUserMarkdown|TestPendingRevisionForwarding|TestSubmissionNoticeFollowsOriginalAttempt|TestAddMemberCapturesAndRetainsSelection' -count=1
```

PASS **1.459s**, [Go log](go.log). Syntax/full-range whitespace passed. Ordinary
hooks retained; no declared hook framework or bypass. No full/browser/package
run or CI wait. Source checks ran before autosquash; the final tree equals the
exact tested pre-fold tree, so no duplicate checks were needed after textual
cache-line conflict resolution.

## Exact reviewed-to-final proof

Reviewed safety ref:
`refs/safety/2026-10-20-dev-workspace-portal-improvements/reviewed-133d23f5`
retains **133d23f5d341808559b08a533409e748d6a400aa** and its exact tree. The
[reviewed15-group inventory](reviewed-series.json) and
[reviewed full series](reviewed-series.patch) are retained.

Final tree **d106cd39731c93473229f8625c0c158c7f677fee** equals both the saved
passing pre-fold tree and a fresh disposable-index reconstruction of reviewed133
plus only [the bounded six-file fix](fix.delta.patch). The final effective delta
is [effective-fix.diff](effective-fix.diff), byte-for-byte the saved fix. It contains:

- History cycle ownership/retirement in app.js.
- Shipped-function deterministic history regressions.
- app cache52→53 in the three existing templates and its existing focused test.

No new visible string or guide prose was needed; `docs/workspace-portal.md`
already documents these paused-read and retry guarantees. No notification source
or behavior changed. Final templates retain **app53/store4/browser6**.

[Full range-diff](range-diff.txt) maps all15 groups. The lifecycle fix is folded
into **8cd67fe835ef4470a3df0545161d2d11f5a7c6a7**, replacing bd46c6e.
**13/15 stable patch IDs match** the reviewed range. Notification group
f0e52bd has a different patch ID solely because adjacent unchanged template
context says app53 instead of app52. Its per-path added/removed lines are
identical to cb12f4c; [context proof](notification-context-proof.json) records it,
and all final notification non-template blobs match reviewed133. These were the
only two cache-line textual conflicts; they added no semantic changes.

The sole dependency group4a2fadd and all five Go/Nix pin files are byte-identical
to the reviewed range, selecting **A6e32a9043ee6367d92bfaf8d3ebdf48036e275f9**.
No lock sibling, Codex version, interim pin, C/config file or source guard was
changed here. Imp1 owns final downstream sole pins and browser guard updates.

There are **no migrations** in the whole branch; none merged, released,
deployed or externally consumed. Immutable capability and reserved gate remain
nonmigration additions. The prior deployed f8/A852 safety refs and receipts are
untouched. Bf8 remains a preserved deployed nonancestor after prior accepted pin
consolidation; this fix does not claim literal deployed ancestry/integration.

Complete final inventory:

| Group | Exact head | Purpose |
| --- | --- | --- |
| 1 | `4a2fadd106d5eb9a7dcd92fb7ab28fb8cbd94458` | deps: update shared conversation presentation helpers |
| 2 | `db1e91ebd008f479cc1021b25e9756c588c5949a` | team: project full-team names from actual implementer counts |
| 3 | `b006196781869aec5d267b790ef0a839e4aa57dd` | portal: add authorized file downloads and source copy actions |
| 4 | `54169426248448119fd257ffbf3d652b1f3b5172` | portal: keep large artifact catalogs compact and stable |
| 5 | `7d9392e6643e8d856688ee1dc08ba86146f41ddc` | portal: publish session membership before optional enrichment |
| 6 | `5a764b28d654c9b00538f333fd550067da7a121d` | portal: retain member settings through sequential additions |
| 7 | `0ce92e8619f6b1ae9afbe8b6016ba8949c89036c` | portal: present team messages and decorated Markdown |
| 8 | `cee4cca19ad2fcf98ffb1317aff7876d784e26b5` | portal: show delivery recovery beside the composer |
| 9 | `1f162c38138b35bfe9b75b2b7a1af2f18f34e513` | portal: browse eligible session files in a lazy tree |
| 10 | `8cd67fe835ef4470a3df0545161d2d11f5a7c6a7` | portal: retire paused read cycles and recover on tab resume |
| 11 | `79c398104a4b99c9dd1952be92c54f1ee4f9d661` | coordination: derive claims from registered repository identities |
| 12 | `e2ff4d10d237a555e86780162e25425bf005d156` | portal: measure read stages without logging session content |
| 13 | `3435e1be56cc938ff297acad85b3d184879daf33` | test: prepare ordinary Firefox acceptance across fifty native tabs |
| 14 | `f0e52bd23c37a9c13bb8c4987008b829716728cb` | notifications: drop deliveries from disabled browser epochs |
| 15 | `d617ef3968280e9955da85e2d7464a47030e7087` | coordination: retain deployed machines through explicit user release |

[Final mapping](final-series.json), [complete series](final-series.patch),
[complete base-to-head diff](final-diff.patch), [names](final-names.txt) and
[diffstat](final-stat.txt) bind the entire branch, including notification/policy.
[SSH proof](remote-proof.txt) and [same-feature CI snapshot](branch-runs.json)
record publication. [Cancellation record](cancellation.json) lists only
superseded active same-feature jobs selected for cancellation; current-head and
other branches are untouched. No blind rerun was used.

Lead/reviewer authorized direct focused verification under mandatory-review
step9 for this bounded requested correction. There is no new design/public
contract boundary requiring automatic full rereview. Lead retains acceptance.
Machine claim and session remain unchanged/open; no live, lifecycle, merge or
deployment action occurred. B is clean and handed back for the explicit owner
transfer to imp1; implementer0 stops B writes and retains routed diagnosis.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
