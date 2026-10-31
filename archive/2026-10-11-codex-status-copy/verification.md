# Verification evidence

Final heads: runtime f145d3b8, workspace 51683b15, configuration 01c8350d.
Final batch `/root/monitor_status_copy_release` completed `verification.sh` in
approximately 14 minutes, exit 0, phase complete, atomic `verification.status` 0.
Final comparisons were captured for all three repositories; heads match the inventory.

## Completed checks

- JS syntax, pure browser contracts through the actual Go harness, whitespace,
  Nix parse, semantic lock/deployment checks and declared hooks passed. Last quick
  focused Go check: 1.063s.
- Final team activity browser script passed in Chromium and Firefox at 1280px
  and 420px. Counter/timer geometry stays unchanged at 8/9/10/11/59/60 seconds,
  minute/hour boundaries and long elapsed values. The simulated one-second tick,
  short/full labels, peer freshness and separator visibility passed.
- The other seven browser scripts passed with identical product code in the
  preceding runs; only fixtures changed. Presentation script passed in attempt 2.
- Runtime Nix checks `package`, `host-package-contract` and `generic-source` passed.
  Full Go and packaged Ruby tests completed. Quiet packaged Ruby periods resumed
  normally; no timeout or retry was used.
- Final `bin/check-dev-workspace-deployment` passed against both absolute consumer
  worktree paths. Only the intended runtime nodes changed.

## Final batch results

Workspace `nix flake check --print-build-logs` passed all checks. `nix build
.#default` produced retained candidate package
`/nix/store/amvgyanpyfm37f12k1w9w5azhv4r8naa-dev-workspace-0.2.0`. Its full runtime
contract and native executable match the installed package/root. Configuration
`nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev` passed
39/39 derivations, generation `2026-10-11--17-23-39`, with no unexpected kernel
compilation. Final-head runtime CI run 38149254563 succeeded. Superseded run
38148908217 also succeeded; it is recorded separately, not used as final-head
proof. No cancellation or escalation occurred.

## Browser fixture corrections and superseded CI

Independent review's sole Advisory found Playwright clock installed after native
clock/interval capture. Install immediately before reloading the geometry document;
earlier cases retain real time. The final fix is test-only.

Attempt 1 (169s, exit 1): all eight browser scripts ran; presentation and team
activity fixtures failed while the other six passed. Presentation's answer fixture
raced a 5s activity poll against a 5s assertion; force fresh activity before the
tab assertion. Consecutive roster focus events could overlap an in-flight details
read; wait for authoritative option values while requesting a fresh read.
Evidence: `verification-attempt1.log`, `.status`, `.phase`.

Attempt 2 (77s, exit 1): presentation passed; Chromium geometry/tick checks passed.
The final absent-count assertion saw the previous active transcript because focus
updates activity before the separate transcript poll. Reload matching idle
activity/transcript. Evidence: `verification-attempt2.*`. Atomic status was written
as `verification.status`; the watcher report's `verification.atomicstatus` name
was incorrect. Neither failure required a product change or a blind rerun.

Older runtime CI 38147695334 (ccc8d6cf) and 38148335763 (59a99ce4) passed.
Superseded in-progress CI cancellation attempts returned HTTP 403: API token lacks
cancellation permission. Observe their outcome without changing credentials;
superseded success does not count as final-head proof. Workspace and config have
no branch-triggered workflows. Final authoritative run: 38149254563 on f145d3b8.

## Deployed live checks

Host/profile deployment passed, followed by exact served asset/template, package,
health and process-continuity checks (`post-deploy-result.json`). Fresh utility
`/root/monitor_status_copy_live` ran GET/HEAD-only live browser checks in 24s, exit 0,
at 1280px and 420px. Lead/reviewer0/architect0 were idle while implementer0 worked;
all displayed “implementer0 is working” on one row with attention hidden. Full
hover/accessible details and no document overflow passed. Screenshots inspected.

Fresh utility `/root/monitor_status_copy_active` ran the active-member view in 8s,
exit 0. Working, separator and narrow geometry passed. The inspected wide image
shows 6 messages, 38 tool calls and 11m 58s this turn; the narrow image keeps the
single row and timer readable, ellipsizing counts to fit. This JSON does not record
counts or measured coordinates; the utility's claim that there were no counters
is unsupported by that JSON and contradicted by the screenshot. The script's
2.1s x-position assertion is conditional on unchanged nonempty counters; controlled
browser fixtures are the primary proof across ticks and elapsed-unit boundaries.
Evidence: live-status-result.json, live-status-implementer0-result.json, atomic
live-status.status/live-active.status (both 0), and status-*.png.
