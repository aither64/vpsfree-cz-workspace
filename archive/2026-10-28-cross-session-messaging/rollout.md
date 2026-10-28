# Prepared aitherdev rollout

User authorized deployment and explicitly requested queueing when available.
No default-branch integration is authorized. Machine is vpsfree:aitherdev;
configuration selector is cz.vpsfree/machines/aitherdev.

System activation succeeded and both system links were verified. The machine
claim is held by this session; application activation remains pending. Final
review, verification and deployment builds passed within the recorded scope. All source heads and the exact verification batch are in state.md
and final-verification-brief.md. Both locks select runtime e9153e61.

Predecessor paths, captured before activation:

- predecessorSystem: `/nix/store/lg62jfx2ym8vyiviwwwa924crnivqk0f-nixos-system-aitherdev-26.05.20261026.718f670`
- predecessorSystemProfile: `/nix/store/lg62jfx2ym8vyiviwwwa924crnivqk0f-nixos-system-aitherdev-26.05.20261026.718f670`
- predecessorWorkspaceProfile: `/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`

Read the selected coordination guide and configuration's
`docs/operations/codex-providers-aitherdev.md`. Keep the system generation and
profile roots for diagnosis and forward recovery. Preserve auto-rollback for
the system; do not reboot. Acquire the exact machine claim immediately before
prepared activation. Recheck its held state and the final source identities.

Deploy the built generation with confctl dry-activate, inspect its effects, then
switch using the same generation, --yes --no-reboot and normal auto-rollback.
Verify both live system and system profile identities before application change.

The predecessor reporting policy cannot parse the new registration. From the
composed workspace, execute its reviewed candidate:
`nix run .#workspace-host -- switch --source "$PWD" --from-candidate`.
Pass both exact session identity variables and DEV_WORKSPACE_CLAIM_ID. Honor
lifecycle/active-thread refusals and retain original recovery state. Selection
is forward-only. Do not force a service restart.

After selection, verify portal health and Sessions filter asset, tool registration,
naming and conversation continuity. Use dedicated disposable session fixtures for
two-way delivery, stopped-recipient hold/resume and revoke behavior; do not send
test traffic to unrelated user sessions. Browser/package tests additionally cover
amber styling, filtering, authorization and lifetime checks.

Retain the deployed machine claim until deployment effects are verified and the
complete feature lineage is integrated into explicitly approved defaults. Do
not merge simply to release ownership. Keep branches and session active.

## Prepared artifacts and acceptance gate

All required checks are covered; verification-reuse.md records the exact CI
archive/creation proof and the local archive-startup timeout limitation. Recovery
boot and host-module VMs passed locally, as did the new Chromium/Firefox test.
- Profile: /nix/store/a3r70kgqaf46185cjmjgalza67vpg0hd-dev-workspace-0.2.0
- Profile derivation: /nix/store/7xb8zyd1g0cv5xvlsnlw2lll07c4bn33-dev-workspace-0.2.0.drv
- System: /nix/store/zyz7pvg8mzq1aiifhxpg6yhl7nknph4j-nixos-system-aitherdev-26.05.20261026.718f670
- System derivation: /nix/store/qrpc5d5d820shffhk7v22sisamj55q5p-nixos-system-aitherdev-26.05.20261026.718f670.drv
- Confctl generation: 2026-10-28--13-13-38
Copy-only completed successfully. Exact predecessor paths still match before
activation; machine status is free. Claim request is deployment-claim-request.json.

## System activation result

Claim fa940f15-f440-4c6b-a002-ad1e40af47d6 is held by owner
c0daeb41-eb62-4be8-91bd-ac41a4c2ef3d for machine:vpsfree:aitherdev.
Dry activation passed. The ordinary no-reboot switch returned 0 in 33.80s;
both live system and system profile resolve to the expected zyz7pvg8 output.
See deployment-system-switch-result.json and deployment-system-switch.log.
The application still selects the predecessor profile; activate the reviewed
candidate next. Retain this claim pending verified deployment and authorized
integration.

## First application activation

The candidate switch exited 1 in 105.72s before selection because a retained
team member was active. Its guard reported unsupported execution-status shape;
read-only activity confirmed working/inProgress. The ordinary failure path
restored its terminal client and portal. healthz returned ok; the selected
profile stayed pjmi2cz75 and the native daemon was not restarted.
The private codex/pending record retains candidate a3r70kgq and registration
digest bb8682a4c2776964f731b469f33bccac740bb1dde59fa9e0b8eefa14d4a7b354.
Do not clear that record or force a restart. Wait for idle, then retry the same
candidate command under the held claim. No deployed communication acceptance
is claimed yet.

## Background queue

The authorized application retry is queued in systemd user service
cross-session-messaging-deploy-20261028.service, invocation
fb84cafbf28241ac8195fc23a1b21cef. It survives this chat turn. The private raw
queued-profile-activation.py driver runs one normal candidate attempt after the
known active member becomes idle, rechecking exact source/system/claim before
execution. It stops on any refusal or changed input. Its observation is only a
wait signal; normal transition guards retain authority.

Read queued-profile-activation-status.json and the unit status first. Activation
output goes to queued-profile-activation.log. Do not relaunch the driver or remove
its exclusive .started marker to obtain another attempt. If a retry is needed,
first reconcile the original selected profile, command result, pending record
and systemd state. A success phase is activated_acceptance_pending: profile and
health checks passed, but deployed communication/naming/continuity acceptance is
still required. Keep the claim until acceptance and explicitly approved lineage
integration are complete. No integration approval has been given.

## Completed activation and outage reconciliation

The queued attempt completed with exit 0 after 210.51 seconds at
2026-10-28T13:54:12Z. The expected a3r70kgq application is selected; both system
links still select zyz7pvg8. The unit is inactive/success, with no pending retry.
Both services restarted at 14:53:54 CET. Registration matches the candidate,
enables session_communication, and the pending Codex record is cleared.

The user observed unavailable portal during the deliberate transition drain.
Stop requested 14:51:01, fully stopped 14:51:30, listening again 14:54:06 CET.
The lead verified healthz ok and router session-page HTTP 200, plus the deployed
Sessions/Communication controls and session CSS. Public HTTPS curl lacked the
private issuer trust; the local router socket supplied the route verification.
Final live A/B messaging, naming and conversation acceptance remains separate.
Keep the machine claim and all source branches; integration is not authorized.

## Feedback application rollout (prepared)

Runtime f199947c, workspace c4cd85c78; matching configuration pin 1aadfca973744b2027a74a27f53c3480b3167b3a.
This is application-only; no system activation. Native Codex0.164.0,
registration semantics and live-switch contracts are unchanged. Existing native
service PID156049, active since14:53:54CET; confirm it survives activation.
Held claim fa940f15-f440-4c6b-a002-ad1e40af47d6 confirmed before preparation.
Build and CI pending, browser and independent review passed. Warn before portal
restart, use ordinary workspace-host switch with exact session identity and
claim, preserve forward recovery on refusal. Check selected profile, health,
read-only existing communication display, naming startup and native continuity.
Keep claim held and branches unmerged; integration is not authorized.

### Feedback activation result

Ordinary claimed switch completed once with exit0 in76.48seconds. Selected
profile `/nix/store/mw2fa43yyjar8hcl5h2zckrjg79rl915-dev-workspace-0.2.0`.
Portal restart interval16:51:58–16:52:15CET, final health OK. Native Codex
PID156049/start14:53:54CET retained, registration digest unchanged, naming child
and socket present. System links unchanged. Live GET-only browser check displayed
8formatted messages in the reported session, labels/status and5sent/2received
counters; no page errors or communication tool rows in Sessions. No test traffic
was sent. CI40712908480 attempt2 and all targeted browser tests passed.
Keep this active initiative and machine claim; default-branch integration has
not been authorized.

## Settings scroll correction rollout

Runtime2caa9419 and workspace58298dc0e, matching configuration43f064ab.
Browser acceptance Chromium/Firefox, independent general/architecture review,
composed profile build and CI40729952642 passed. Ordinary claimed switch
completed once with exit0 in103.68seconds, selected
`/nix/store/cfgd3aqs0s6ahgavyx17m1pc3rnnwww2-dev-workspace-0.2.0`.
Portal active18:10:25CET, health passed. Native process156049/start14:53:54
retained; new naming child3255111 and socket present. System unchanged.
Live GET-only browser check confirms visible tab bar after Automation click
and Back/Forward, zero page errors; screenshot/tmp/settings-scroll-live.png.
No message or Settings mutation was sent during acceptance. Branches unmerged
and machine claim held; integration remains separately authorized.


## Final integration and machine release

The user subsequently approved merging and releasing aitherdev. All three exact
final feature heads are now on their remote master branches. Independent review
accepted equivalent deployed lineage after the workspace/configuration rebases.
The final live profile, system, portal health and conversation process were
verified again. Machine claim `fa940f15-f440-4c6b-a002-ad1e40af47d6` was released
at 2026-10-28 17:28:51 UTC and its released state re-read. Full final heads,
claim proofs, review conclusion and verification reuse are in [integration.md](integration.md).
No further activation was needed. Branches and session are retained.
