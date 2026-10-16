# Exact6c browser failure diagnostic — PREPARED, UNRUN

This tracking-only bundle instruments the exact published runtime
`6c7d3851b005b47357e43688efccddde56f4e53b`. No application/test source, commits,
branch refs, browser/display/provider state, or original failure artifacts were
changed. No diagnostic browser run has occurred; `run/` does not exist.

The first failed browser result remains authoritative failure evidence. Its
safe trace has no assertion location. A sound-commit/Playwright checkbox race
is plausible, not established: the client restores the saved checked value
while its write is pending, and installed Playwright 1.59.1 checks checked state
immediately after `_click`. The installed implementation was read at
`playwright-core/lib/server/dom.js` lines654–675. Do not fix or retry blindly.

## Future command — lead acceptance and fresh watcher only

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/notification-controls-browser-diagnostic-6c7d3851/run.sh
```

This runs exactly the original Go `TestNotificationsBrowser` once in the same
cached declared environment with a Node preload. It refuses a changed head,
dirty worktree, changed bundle/source/gate, inherited NODE_OPTIONS, or any
existing `run/`. It preserves the original test exit and writes only NEW paths:

- `run/browser.log`
- `run/browser.status`
- `run/summary.json`

No fullflake, live portal, provider run, credentials, SSH, package/pin change or
lifecycle action is part of this runner. No assertion/action/outcome, permission,
subscription behavior or timeout is changed. The existing fixture keeps its
original context cleanup behavior. Do not invoke the runner before lead accepts
this preparation; lead owns the fresh Luna watcher execution.

## Exact observation boundary

The preload is fixed to one absolute CJS filename and SHA256
`f539862a57cf85b3ce6a6795fed33b289c085b5f10b6d3b3fa1dc37f5025bd32`.
It checks HEAD and file hash, then changes ONLY line5's `safeError` expression
in memory. Every other line and the total line count remain byte-identical.
`adaptation.patch` is the complete virtual change. The loader hook restores
itself before that single targeted compile executes any imports. No tracked
file is written. Original category computation/return is preserved, and observer
or sink failure cannot replace it. No import interception beyond that compile,
new production diagnostic API, action forwarding or mock is introduced.

The observer emits a fixed installed marker, then at most seven error records
(eight total). Each record is <=256bytes and the total <=2KiB. Error records
contain only numeric CJS line/column or null and fixed category
`checkbox_state_unchanged` / `other`. It reads a bounded error message/stack
solely to recognize the exact known checkbox exception and the first matching
exact fixture frame. It never outputs an error message, raw stack/path/URL,
selector, ID, endpoint, key, body, argv or storage. Other fixture bytes and
existing safe-error categories remain unchanged. Columns on the replaced
line5 itself are not original columns; all action/assertion lines remain exact.

The parser labels absent active markers, guard failure, invalid projections or
missing failure location inconclusive. An active marker with no errors is
explicitly distinct from no instrumentation. A passing diagnostic run would
mean only that the failure was not reproduced, not a proved cause or repair.
No acoustic, OS popup or physical Firefox/macOS focus claim follows.

## Static evidence only

`static-check-final.log` proves exact single-line transformation, source parsing
without fixture execution, original safeError return categories, sink isolation,
wrong-head/changed-source refusal, loader restoration and canary/output bounds.
`parser-static.log` covers numeric/enum projection, missing coverage and
invalid/capped input. `static-status.json` binds syntax and preservation checks.
The final source remains clean6c. Prior failed log/status and sealed packet
hashes are retained in `preserved-inputs.json` and verified unchanged.
The initial hash of the lead-owned investigation note is also recorded there;
that mutable note gained a lead-authored API-inspection paragraph during prep.
It was never restored or edited by this work. Only immutable failed log/status
and sealed manifests are preservation fences in the future runner.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
