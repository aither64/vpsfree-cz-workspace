# Portal message recovery rollout

Prepared at provider 57dd01b1d860181e12aa7ccb37ecdeae8b2c08c5,
runtime fac4e6a3d2169dd81d0ae9bb891e7f8ca62114de,
configuration 8f21fc55a410dceeef2c37818f891aefd7e9e1bd,
workspace 32f9c8866ea19511174e9cb74d2f0b327ca5d4df.
Native Codex remains 0.163.0; no migrations. No intermediate feature deployment.

Source review, quick checks, provider packaged checks, native fixtures,
generic runtime build and real-browser delivery/composer/recovery checks passed.
Configuration built generation 2026-10-24--22-56-18. Copy-only preparation passed.
Composed application built successfully:
`/nix/store/fsp42gfclql2pjm0l8gq77m8qicl4f0z-dev-workspace-0.2.0`.
Runtime CI creation/archive passed; fast-job attempt 2 is running after the
recorded existing cancellation/disconnect test-ordering failure. No activation yet.

Baseline system/profile and read-only portal/thread evidence: live-before.json.
Native Codex PID 3387667 since 2026-10-18; tmux PID 435397 since 2026-09-11.
Original confctl thread 01a14bb2-e3ad-7922-a5c9-bc1d07d5cbb8 remains idle with
latest turn 01a16f7d-c2ab-70a0-adcc-0332889da697. Never resend its message.

Activation: acquire vpsfree:aitherdev, dry-activate and no-reboot confctl switch
with health checks and auto-rollback, then ordinary claimed workspace-host
switch from exact workspace source. Verify both live-system and profile paths.
Use supported forward profile recovery if needed; preserve all journals/claims
until effects are settled. Before release prove complete remote integrated lineage.

Live browser verification uses installed HTML and assets over the portal socket.
All submission endpoints are intercepted with disposable browser state; no
mutation reaches the original session. It checks the original stale-banner
scenario, per-message unknown preservation, explicit replacement and retry state
across reload in Chromium and Firefox. Read-only live thread continuity is
checked separately. Exact script: live-browser.cjs.

System candidate:
`/nix/store/11fsqwpxi3i9v9n15nb40ng8gwz7m624-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
Both configuration and workspace lock graphs select runtime fac4e6a3 and provider
57dd01b; extension remains 767dfd58. Final sources are clean, evidence in
predeploy-source-identity.json. Complete feature series is final-series.txt.

The live-browser check was executed before deployment and failed at the exact
banner-clearing assertion, reproducing the user report against old installed
assets. See live-browser-before.log. No original-session messages were sent.

## Final source set after cancellation review

Earlier prepared candidates above are superseded and were never activated.
Final heads are in final-heads.json: provider872c7ad, runtime1b562996,
configuration9351b6a3, workspace00265c87. No source or pin intermediates deployed.
Final independent review has no findings; final full verification is running.

## Final startup correction

The earlier candidate was never activated. A browser check exposed initial Send
enabled before asynchronous script initialization. Initial Send now stays
disabled until its durable submit handler is installed. Review startup-review-report.md
has no findings. Final source set supersedes the earlier entries:
provider872c7ad, runtime10bb0475, configurationd12a7737, workspaceb1b86b2b.
Complete identities and series: final-heads.json. Provider/native exact checks
passed unchanged provider; remaining candidate batch is running.

## Activation started

Final artifact copies completed. Machine claimfaea8db4-b766-42de-a7bd-cb99bb2e1eca
was briefly waiting during payload collection; authoritative status now held.
No other active machine holder. System generation2026-10-24--23-56-19 activation
started with dry-activate-first, no reboot, health checks and auto-rollback.
Log system-activation.log. Exact candidates in deployed-candidates.json.
Profile switch follows only after confctl completes successfully and both live
system/profile paths are confirmed. Creation CI rerun observed independently.

System activation exit0; both configured health checks passed. Live system and
system profile both resolve to the exact candidate n6b9dmmaw83zx80paglrisy0w5rwnfw8.
Ordinary workspace-host switch is now running under the same held machine claim.
See profile-activation.log. Do not release until profile/live checks and integration.

## Successful rollout and integration

System/profile activation and live checks passed. Installed assets match exact
reviewed source; original thread/native/tmux continuity preserved. Chromium and
Firefox installed-browser scenario passed after correcting only its models stub.
Every final exact deployed head is now remote master, with unchanged extension
also integrated. See integrated-lineage.json and live-verification-passed.json.
Machine claim released normally after these proofs. No reboot or native upgrade.

Final feature CI40134903928/attempt2 and full master CI40137122653 passed,
including creation, archive and host activation/recovery checks. Provider master
CI40137101265 passed. All observers completed; temporary targets removed and
no own claims remain. Initiative lifecycle complete; session stays open.
