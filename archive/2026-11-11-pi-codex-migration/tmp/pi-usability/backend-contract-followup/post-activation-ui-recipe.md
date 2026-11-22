# Post-activation UI acceptance: prepared, parked

No live browser request, check, Nix evaluation or build has run for this package.
Execute only after main supplies the exact activated source head/package and
releases this pass. Main owns health, process and workspace-profile continuity.

Use one Chromium instance for two ordinary pages at the existing portal origin:
the current migration session (Codex), then
`2026-11-19-ct-top-full-team-validation-retry-2` (Pi), both lead views.
Recheck each session's manifest/private sensitivity metadata before retaining
results. Keep the result JSON Git-ignored and untracked, even for ordinary data.

## Existing setup

- Reuse the pinned Node/Playwright paths in
  `tmp/pi-aitherdev-live-browser/preparation-receipt.json` and
  `backend-contract-followup/p1-browser-inputs.txt`. Existing Chromium executable:
  `/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers/chromium-1217/chrome-linux64/chrome`.
  No Nix evaluation, dependency install, browser download or local server needed.
- Reuse the private FD/context authentication pattern at
  `tmp/pi-aitherdev-live-browser/retry-original.cjs:25–67`, without printing or
  saving credentials. Do not execute that runner: its scenario includes mutations.
  Use only session-owned browser state; never copy another session's cookies.
- Keep TLS verification enabled. The earlier Chromium profile's CA import was
  not completed (`preparation-receipt.json.chromiumAttempt`); it proves no live
  Chromium TLS acceptance. Use existing trust. If TLS/authentication prevents
  this pass, record that access limit and stop without trust repair or bypass.
- Before either navigation, block browser requests except GET/HEAD/OPTIONS;
  auto-dismiss dialogs, downloads and popups. Record only a blocked-method count,
  never request bodies. No tracing, HAR, video, screenshots or full DOM dumps.

## One read-only pass

1. Match loaded `/static/app.js` and `/static/communication.js` response hashes
   and URLs to the exact released head's asset bytes supplied by main. Retain
   hashes/status only. Do not repeat main's process/profile inventory.
2. On Pi, open `[data-session-tab="team"]`. Read only
   `[data-team-stats] [data-team-metric]` and `.team-coverage` metadata. Confirm
   materialized rows have actual supplied activity/count/time values, with partial
   coverage shown; preserve genuine zero. Never-started rows have no measurement.
   Unsupported/unavailable rows are explicit limits, not invented zero totals.
3. If Pi is actually idle, retain only currentState/stateSinceMs/observedAtMs
   from the page's normal activity responses and `#codex-work-elapsed`. Switch
   conversation → Team → conversation using ordinary section tabs. With the same
   state anchor, the timer must preserve/advance its interval rather than reset.
   If the worker changes state, the observation is stale, or no idle interval is
   available, mark this assertion limited; do not pause/resume or wait for a state.
4. On each lead page, use `[data-transcript-filter="sessions"]`, then `all`,
   then `messages`. For existing retained session rows only, compare entry-key
   identity in memory and read `.message-session-label` separately from content.
   Confirm Sessions/All include each existing session row once, Messages excludes
   it, and its label contains the saved from/to names. Retain only identity hashes,
   counts and label-presence booleans, never message/envelope text. If no relevant
   row is available or the retained reader fails, record the gap without sending
   or starting a history-collection campaign.
5. Check the exact neutral repository empty sentence from the served template or
   released template bytes if these sessions have worktrees. Do not create an
   empty session. Close and join only this pass's browser/context.

Do not click Send, Retry, Resume, Drop, Allow/Revoke, settings, team or lifecycle
controls. No synthetic input or receipt operation. Reuse prior P1 Firefox/source
controls; automatic-send behavior remains covered by the finite source controls.

Expected result is a short single Chromium pass. If execution becomes uncertain,
apply the installed monitor policy before extending it; no silent campaign or
second-browser retry. Save one compact result beside this recipe: released head/
package, asset hashes, sensitivity checks, metric/filter/timer outcomes and limits,
blocked-method count, elapsed time and browser-close result. No new review gate.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
