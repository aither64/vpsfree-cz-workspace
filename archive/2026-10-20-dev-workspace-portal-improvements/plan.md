# 2026-10-20-dev-workspace-portal-improvements

## Current follow-up: generic reservation documentation

Approved user plan: delete the aitherdev-specific coordination document, preserve
its concrete host deployment steps in the existing provider deployment guide,
and replace copied workspace reservation rules/host examples with generic links.
B docs/coordination.md and its shared generated CoordinationInstructions remain
the generic policy owner for every configured machine. Automatic release after
verified deployment and integration remains unchanged. Existing documentation
links/instruction checks and focused final review suffice; no binary, pin, build,
profile/system deployment, reservation or new framework belongs in this cleanup.

The update skill’s required-procedure reference to the removed runbook is part
of the same relocation. Final cleanup heads: workspace9f6968eb and configuration
c1057731; one append commit each, no migrations or input updates. Focused checks
passed; retained reviewer0 completed general/architecture review with no findings.
Integration uses retained workspace/configuration master approval. No new package
or machine deployment is needed; existing generic runtime remains selected.

## Current follow-up: automatic machine release

The original portal work is reviewed, merged, deployed and accepted; master CI
passed. The user then requested: “release should be automatic after deploy and
merge”. This supersedes earlier three-condition retention decisions.

Release the session-owned machine claim promptly once deployment/effect
verification has succeeded and the complete deployed feature lineage is
integrated into approved remote defaults. Do not wait for separate UI acceptance
or release direction. Preserve unfinished-effect reconciliation, exact ownership
and released-state verification, merge authorization and independent session
lifecycle boundaries. Claim755 is already released; source work holds no machine.

[Current design](design.md#automatic-machine-release-policy) assigns B generated
lead/member coordination instructions and guides to implementer0, C/site guides,
existing consistency tests and matching new runtime/channel pins to implementer1.
The lead applies the English writing pass and coordinates final independent
review, then the smallest normal package build needed to deliver the corrected
future developer bindings and installed guide. No daemon, timer, new API/schema,
roster change, host-system deployment or browser/native verification campaign.

Existing merged history and rollout receipts remain immutable. The new policy
and sole pin streams append to merged B/C/config. Complete new ranges/final diffs
and no-migration provenance go to the retained independent reviewer after commits
and quick checks. Subsequent merge/profile selection retain their separate
required authorization. Acquire only near actual activation; release promptly
after both prerequisites. Leave the session open and retain branches.

## Goal

I'd like several dev-workspace portal improvements:

- Upon loading the index page, I see "Session status is loading" at the top for >5 seconds. I shouldn't see such things, it is distracting. It should take so long and don't bother me unless there's a problem.
- codex output sometimes shows "Older history is unavailable on this server" at the top, overlapping the content. is it using the shared fetch timeout? It shouldn't bother me.
- the portal sometimes fails to submit my inputs to codex, opens alert window with 502 error
- I'd like codex output to use different colors for messages between team members, so that it differs from my own messages and messages meant to me. The filter at the top (All/Messages/Activity) should allow me to hide team communication.
- use markdown to format messages entered by the user
- links to workspace files in codex messages should have target=_blank
- links to workspace files aren't real links, I can't do "Open in new tab"
- the file content viewer should allow me to easily copy all content to clipboard or to download the file
- in artifact list, the list of artifact names is too distinct and uses too much space. make it more compact, like a file tree view... some sessions have hundreds of artifacts
- artifact viewer should also allow me to copy content to clipboard, Download button can be more compact, just an icon, like for copy
- maybe artifact list should scroll independently from the content viewer, since when the list is too long, I have to scroll to top after clicking on selected artifact

- Temporary message bubbles: replace the large Dismiss button with a compact X
  icon on the right, preserving dismissal behavior and accessible labeling.

- Team catalog: default to Full team with two implementers; add Full team
  variants with three, four, five and six implementers. Keep the existing
  session roster and retained member settings unchanged.

- Add-member form: preserve selected role/model/reasoning across sequential
  additions without refetch/reset delay. Fast Add clicks must use the displayed
  captured values and cannot submit a transient low-effort default.

## Affected repositories

- `dev-workspace`: portal loading, submission integration, file and artifact UI.
- `codex-web`: shared Codex history, message rendering and filters.
- `workspace`: team catalog/defaults/capacity/docs/checks and final package source
  pins after implementation packages.
- Configuration pins and deployment are outside the current implementation scope.

## Approach

Architect investigates current behavior and writes the technical design before
implementation. Two retained implementers own independent packages, including
source, tests, technical docs, quick checks, commits and review fixes. The lead
coordinates scope, tracking, acceptance and user-facing wording. Final committed
heads receive independent review before long integration checks. Publish feature
branches; default-branch integration requires explicit user direction.

## Decisions

- User confirmed the larger teams keep the current models and efforts. Catalog
  IDs are delegated (2), delegated_3, delegated_4, delegated_5 and delegated_6;
  both defaults select delegated. Friendly labels include implementer counts.

- Suppress routine loading/capability noise while keeping actionable failures.
- Diagnose intermittent submission errors; preserve input and prevent duplicate
  turns rather than adding blind mutation retries.
- Make workspace links native anchors, and large artifact catalogs compact with
  independently scrollable navigation and accessible copy/download actions.

## Compatibility and deployment

Preserve persisted sessions and existing Codex protocol contracts. The accepted
[design](design.md) defines additive browser/server interfaces, mixed-version
fallbacks and forward recovery. No database or state migration is intended. Deployment is
not yet requested; keep the selected runtime usable and unchanged during tests.
No lifecycle cleanup is authorized.

## Documentation

Readers are portal users and maintainers of the shared Codex browser module.
Durable behavior and failure semantics belong in the owning repository docs;
this directory holds design, checks, review and eventual rollout evidence.

## Team catalog extension

Architect defines catalog IDs/labels, native capacity and runtime compatibility
before a separate implementer-owned workspace package. Existing Full team keeps
its identity and two implementers; new variants reuse role settings and differ
by implementer count. New-session defaults change without rewriting live rosters.
The architect found
schema-6 already supports counts and snapshots. Counts N=2..6 need N+2
specialist slots; derive the catalog maximum (8). Direct retained teams declare
zero native child-thread registration requirement; this change does not restart
or reconfigure the current session. The new default also selects Sol/xhigh for
standalone mandatory-review fallback; saved reviewers retain their settings.

## Testing plan

Use repository Nix environments and targeted regression checks for loading and
history, submission failure/recovery, team filtering, Markdown, native file links,
copy/download, and large artifact navigation. After quick checks and independent
review, use a fresh policy utility watcher for long or uncertain checks.

## Aitherdev deployment authorization

User: “we've updated session coordination rules, so familiarize yourself with it,
then you can proceed with aitherdev deployment.” This authorizes prepared aitherdev
deployment/profile activation and necessary matching host contract work, not
default-branch integration. Read updated workspace and selected-runtime guide.
Develop/build without repository claims; reserve only the machine near activation.
Architect checks current installed provenance/forward compatibility first; preserve
the newly selected runtime's coordination behavior. Keep session open and use
forward recovery; no archive/delete/stop authorization.

Deployment outcome: authorized aitherdev rollout completed and live verified
2026-10-21, exact A852/Bf8/C530/config450. Matching system generation then composed
user profile selected without reboot; conversation/roster/native continuity and
index/source/catalog/naming-process readiness passed. Machine claim explicitly
released. See deployment-rollout.md/deployment-receipt.json. Default integration
still requires separate explicit repository/target direction; session remains open.


## Authorized follow-up: Files, 50-tab Firefox and coordination

The user authorized implementation of the final follow-up plan. Replace the
specialized artifact UI with a lazy eligible session-files tree and ordinary
source viewer; preserve explicit publication compatibility and file boundaries.
Fix demonstrated passive-read/stream fanout, current-cycle cancellation/recovery,
provider single-flight, JSON body abort handling, upload metadata recovery and
pending-question invalidation without sacrificing timely controls. Include
team-statistics freshness/recovery and real Firefox50-tab acceptance. Preserve
true failures and instrument unproven incident latency rather than hiding it.

Implement browser-wide durable disable/registration-epoch fencing, dynamic
registered-repository merge identity without per-repository redeployment, and
generic holding policy for every deployed machine through integrated feature
lineage, user acceptance and explicit release direction. No merge approval is
implied. Architect-owned details and ownership live in design.md/state.md.
First execution acquired machine-only755910ab-a78b-4d30-a057-03b555b336db HELD.

Compatibility: keep supported deployed A852/Bf8/C530/config450 sources/receipts;
public optional SSE control invalidation and registration-bound Push remain
additive; no native Codex upgrade, persistent ledger rewrite or new repository
registry. Candidate capability must protect active dynamic claims. Deployment
is forward-only from the currently selected profile; preserve all retained
settings and durable writes. Exact final graph follows final A→B→C/config.

## User-directed targeted performance verification

On2026-10-21 the user withdrew further native50-tab testing as too heavyweight,
requested smaller targeted performance regression checks, and asked that the
work be finished and deployed by morning2026-10-22. This supersedes the earlier
mandatory50-tab acceptance gate. Preserve its failed/partial receipts without
claiming complete stress or durable-send acceptance.

Use existing fast component tests for freshness, singleflight, retry/backoff and
hidden scheduling, plus one short two-real-Firefox-tab read-budget test under
[the bounded brief](design.md#targeted-read-performance-replacement). Observe
one existing5s polling interval, zero hidden requests, foreground progress and
SSE/read bounds, one wake and the existing503retry gate. No discard/send/soak,
new performance framework or host tuning. After committed quick checks and
focused final review, run only this new scenario and final composed package
verification, reusing unchanged targeted/notification results with exact source
provenance. Then perform the authorized user-profile-only forward deployment
and live continuity checks. No default integration or lifecycle action.

Follow-up deployment outcome:2026-10-21 23:50CEST, finalAea64/Bbc40/C40b0/config5a524 source graph, profilef5h selected, systemjwnd unchanged. Package/CI/review/targeted2tab/livecontinuity passed. See followup-deployment.md and exact receipt. Session/machine remain open/held; no merge or lifecycle authorization.

## Authorized Files correction (2026-10-22)

User approved the refined plan: restore treeleft/contentright with independent
scrolling, renderedMarkdown/images and rawMarkdown toggle; icon-only Raw/Preview,
Copy, Download; ordinary clicks select inline, modifiednative links remain.
Browse all regular ownsessiontracking files including ignored, without Git or
registration eligibility; preserve confined nofollow/special/Gitinternals
protection and bounds. Deprecate artifactadd to successful informative no-op;
preserve manifestshape/oldentries/links, no writes during browsing.
Resolve current work/archive root and test stablelinks/content/downloadbytes
through DISPOSABLE actualarchive/revive, including ignored/unregistered files.
This authorizes implementation/review/focusedchecks/pins/profiledeployment; no
real session lifecycle, default integration or machine release. Native50 remains
cancelled. Architect0 records concrete interfaces/owners before UI/backend edits.
