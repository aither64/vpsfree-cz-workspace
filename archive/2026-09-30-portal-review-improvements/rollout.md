# Aitherdev rollout record

This record describes the individual aitherdev rollout for the portal review
initiative. Reusable deployment and recovery behavior remains in the owning
project documentation.

## Deployed card-summary composition

Production UI plus its workflow-focus correction are committed/published at
generic `1227f5c2`, extension `074926d3`, workspace `cd2875f3`. Focus fix `6245`
and its five cache references are separate published ancestors; no consumed
history was rewritten. Independent affected-lane recheck cleared the finding.
The first full Go/browser stage failed in the archive-page Firefox fixture;
all six question-browser cases passed, including workflow focus in both engines.
Later flake/build/protocol stages did not run. Fixture-only correction `869b8d47`
is committed/published and cleared by bounded independent review; it is the
separate generic verification head and does not advance consumer inputs.
The fresh Luna/low verification operation completed all nine stages with status0
(170/324/514/254/7/4/47/447/5s). Full logs/status are retained under
`/tmp/portal-archive-fixture-final-869b8d47/`. Candidate
`/nix/store/z20g487rcankkgaprsrdya5na079i1rl-dev-workspace-0.2.0` is now built
and explicitly rooted; its derivation is
`/nix/store/ad34hy4q21lj2kppdddj7256glpm6djr-dev-workspace-0.2.0.drv`.
Candidate/current protocol checks use the same exact Codex0.159.2 binary and
current same-account model evidence is reusable. Cache references are reviewv9,
appv19, CSSv3. Generic verification869 remains separate from runtime1227.

The authorized idle-gated switch completed successfully in70s, selecting z20
from clean workspacecd2875. Parent verified selected path and portal executable;
portal/Codex/router are active and the live model catalog has exactly one visible
gpt-6.1-sol with high/xhigh among9 models. Runtime is generic1227, extension074,
workspacecd287; optional verification869 is not a runtime repin. Active portal
PID3043113 executes z20/bin/workspace-portal.

The requested live-only v4 probe passed with true exit0/status0 in10s, following
bounded transport and teardown corrections to the ephemeral probe. Six frozen
history summaries, desktop/mobile one-column layout, action spacing, empty
staged/unstaged snapshots, retained history through details refresh, reload reset,
app19/review9/css3 and no page errors are verified. All sampled workflow cards
were unavailable, so populated counters/run-link focus and changed-file previews
were not exercised live; retain the successful predeployment fixture proof and
this separate sampling limit. Evidence is
`/tmp/portal-card-summary-live-only-cd2875-v4/{log,status,elapsed}`.
The original combined batchstatus1 and v3's terminated status143 remain separate;
neither becomes an all-stage pass. The profile switch was not retried.
Shared DNS/configuration remains prepared but unpublished and defaults unmerged.

## Previous verified rollout

The previous selected portal runtime was generic `e64a9fda` / extension `362ebd4` /
workspace `aca3b39d`, package `bpzvfhdnrj3clw9zfd1qhrhw7fjksyvb`. Generic final
verification head `618df553` adds optional fixture corrections without a
consumer cascade. Independent review, full Go/browser, generic/workspace flakes,
candidate build/protocol, real-editor harness, exact CI and live acceptance all
passed. Shared DNS publication and default integration remain unapproved.

## Previous rollout revisions

- Unselected configuration candidate: `d24b251531a9a482b8f1b5dd81540da85981189f`
- Deployed workspace composition: `aca3b39d400b5d1d6d51e42550421f8362684ee0`
- Deployed generic portal: `e64a9fda4f5fb3595ce194cc55359ab61f5d8b3a`
- Deployed extension: `362ebd4759d090805cd95a800e7131edb930b604`
- Codex package input: `af40d966859ec4075ecc172dbb39e53f474dc5d9`
- vpsAdmin API: `5c76e3290481b297dcd0baa76d246133f0353d8f`
- vpsAdmin WebUI: `534caa83a5f97d2b40b4a126886649b14dc9e8d3`

The previous rollout runtime revisions were generic `e64a9fda`, extension `362ebd4` and
workspace `aca3b39d`. Configuration `d24b2515` remains an unselected DNS
candidate. Generic final branch head `618df553` contains only separately
reviewed verification-fixture corrections, so the deployed runtime keeps its
reviewed generic input. The Origin-label and React-container autostart
corrections are selected in the user profile and cluster. The internal-DNS
candidate is committed but publication to its four shared consumers remains
unapproved.

Mandatory final review found no Blocking or Important issue at the current
heads or in the bounded fixture follow-ups. Final generic, extension and
workspace flake checks pass at their recorded revisions, and the selected
workspace package is
`/nix/store/bpzvfhdnrj3clw9zfd1qhrhw7fjksyvb-dev-workspace-0.2.0`. Build-only
evaluation also passes for each of the four exact internal-DNS consumers.

The optional fixture corrections through generic `618df553` passed independent
follow-up review, Node syntax, focused browser runs, generic flake checks and
exact-head CI. Extension `362ebd4` also passed the complete packaged cluster
smoke. Detailed results and log paths are in [state.md](state.md).

## Executed system and profile rollout

Fresh Luna/low watchers built only `cz.vpsfree/machines/aitherdev`, dry-activated
generation `2026-09-30--21-42-52`, and switched that same generation. The
running system is
`/nix/store/cb7sziy9ijyf2sxw1ajdbjwrzj2ac591-nixos-system-aitherdev-26.05.20260928.7fc6f2c`
with Codex 0.159.2. Firewall state, system and user units, and the workspace
router/portal/Codex services were healthy after the switch.

The guarded user-profile transition selected
`/nix/store/aidlqw1p8dxijyd35jn7fxr6avzkqvc9-dev-workspace-0.2.0` after an
earlier in-progress-turn refusal. Reconciliation finished successfully and left
no pending marker. The live portal lists exact `gpt-6.1-sol`; an atomic settings
write to that model with xhigh effort persisted on readback. Disposable staged,
unstaged and untracked probes returned immutable comparisons and were removed.

After the final checks, the user ran the verified guarded transition while this
conversation was idle. The selected profile now resolves to
`/nix/store/51i6gp92srgvqcmmwfv8qsg9xq9xfdqf-dev-workspace-0.2.0`, built from
workspace `45cce0a8`. The live portal renders `Origin`, ships Load all diffs and
the atomic settings client, and lists exact `gpt-6.1-sol` with every supported
effort.

## Executed bridge-cluster rollout

A fresh Luna/low watcher started the session's single-node bridge cluster. The
selected result reported clean pinned WebUI revision `534caa83`. The existing
PHP UI was available, while the first React requests returned 502 because
`container@newadmin.service` was inactive, linked and had no install target.
This identified the missing container autostart setting now being corrected in
the unmerged extension feature commit.

A supported manual service restart started `newadmin` for diagnostic acceptance.
The following checks then passed:

- public React routes, health, static asset, config and build metadata;
- cluster-CA trust and expected certificate names;
- legacy PHP availability;
- API CORS for the OAuth token header without credentialed cross-origin use;
- loopback-only nginx and BFF listeners and nginx configuration validation;
- exact clean frontend/BFF build revision and absence of retired secret
  environment names;
- real seeded-user OAuth login and callback, one-use state rejection,
  authenticated session and API access;
- forced access-token expiry followed by refresh and accepted refreshed token;
- stable session identity after a BFF restart;
- two repeated OAuth seed executions;
- logout, anonymous session readback and rejection of the revoked access token.

Credentials, cookies, authorization codes, states and tokens were kept in
mode-0600 temporary files and deleted after the checks. Their values were not
recorded in session artifacts or command output.

## Final runtime activation

A fresh real OAuth login established an authenticated session before the final
update. A fresh Luna/low watcher then ran the selected helper's supported
`update 2026-09-30-portal-review-improvements services`; it completed in about
7m25s and activated services system
`/nix/store/vv7b9mhcrmj1fii3jb6r0k1craclnynq-nixos-system-vpsadmin-services-26.05pre-git`.

Post-update checks prove that the cluster is running, ready, single-node and on
bridge networking. `container@newadmin.service` is active, enabled and wanted
by `machines.target`; it requires and starts after the successful OAuth seed.
The selected source record is the clean session worktree at exact WebUI
`534caa83`. Nginx and the BFF are active, ports 18082 and 3001 remain bound to
loopback, health and legacy PHP return 200, the authenticated session retained
the same session key, and authenticated API and CORS probes return 200. The
path-based local WebUI build reports unavailable embedded Git metadata; the
cluster's immutable selected-result source record remains the authority for
the exact clean worktree revision. Temporary credentials, cookies, states,
codes and tokens were removed after the checks.

No default-branch integration is part of this rollout.

## Prepared internal DNS generations

Configuration candidate `d24b2515` is built for all four independent private
zone consumers. Complete build output:
`/tmp/portal-review-internal-dns-four-builds-d24b251.log`. Each generated BIND
configuration references a rendered zone with serial `2026093000` and exactly
one newadmin CNAME to the existing aitherdev frontend. Validation with that
generation's BIND `named-checkzone` returned OK for all four.

| Target | Built generation | System toplevel |
| --- | --- | --- |
| cz.vpsfree/containers/prg/int.ns1 | 2026-09-30--23-24-31 | `/nix/store/aq3qibcnf3d4byw5c9sfi98d9yf4k1qx-nixos-system-ns1-26.05.20260928.7fc6f2c` |
| cz.vpsfree/containers/brq/int.ns1 | 2026-09-30--23-27-01 | `/nix/store/imcbgk4d5gb12lgm254l4sk8i5fk0v6z-nixos-system-ns1-26.05.20260928.7fc6f2c` |
| cz.vpsfree/containers/prg/int.mon1 | 2026-09-30--23-27-52 | `/nix/store/as30hhqffjmldi8qcjj1w0xdgb359p80-nixos-system-mon1-26.05.20260928.7fc6f2c` |
| cz.vpsfree/containers/prg/int.mon2 | 2026-09-30--23-28-53 | `/nix/store/zxn6i3r0r341lbvn0qbrdh4arngxxhfz-nixos-system-mon2-26.05.20260928.7fc6f2c` |

Dry activation and publication require explicit approval for these exact four
shared hosts. The lead presented the exact d24b CNAME/serial change and all four
canonical target names; the user's answer remains pending. All four recorded
built outputs are still present. Building and validating these
generations did not publish the zone.

## Repository-review follow-up stages on 2026-10-01

The next portal candidate fixes empty comparison responses and presents each
repository as a full-width card with a closed Local commits disclosure. Its
accepted brief is in design.md, “Approved repository-review follow-up”. Generic
`8019b9b7`, extension `361be9c7` and workspace `9818b805` are committed,
published and independently reviewed with no Blocking or Important findings.
At this initial checkpoint, exact-candidate long checks and profile transition
were pending. The preceding `51i6gp92…` profile remained selected.

This lead turn observed another writer perform the publication and downstream
pin commits while implementer0 authored the two generic code commits. The
immutable graph and approved Codex closure were verified; coordination of the
remaining verification/transition owner was pending at that checkpoint.
Publication alone did not select a new profile.

The demonstrated desktop action-row failure is corrected by generic `e64a9fda`.
The dedicated normal-host six-fixture browser/navigation run passed in 84.274s
before commit. Extension `362ebd4` and workspace `aca3b39d` now select that fix;
their generated lock diffs preserve the approved Codex closure. This lead owns
that final cascade and the remaining candidate verification/profile rollout.
Independent affected-lane review passed at e64/362/aca; exact candidate checks
were then pending. Generic verification head `4a1da3c3` added the independently
reviewed optional Keep open fixture correction and leaves those runtime pins
unchanged. Extension CI at362 passed both flake checks and packaged cluster
smoke. The final literal batch has separate stage exit-status records in
`/tmp/portal-review-final-4a1da3c3/` and stops at the first failure.
The earlier batch's zero status is not an all-stage pass: browser failures and
an invalid package lookup are logged, as reconciled in state.md.

Deploy this follow-up through the supported user-profile transition after its
checks pass. Reload the browser to acquire the new markup and versioned assets,
then verify empty staged/unstaged and committed views, visible action errors,
single-column layout and disclosure retention during status refresh. Existing
cluster services and shared DNS are outside this portal-only rollout.

The final literal batch passed full Go/browser, generic and workspace flakes,
candidate build and protocol checks before the standalone editor harness exposed
obsolete fixture expectations. Commit `618df553` corrects only that harness;
independent affected-lane review and complete history/migration conclusions
passed with no Blocking or Important finding. Its committed-head harness has
now passed. Fresh exact generic CI 36860394508 remains under watcher observation.
The exact asset output is rooted separately from the package because the package
embeds the assets and need not retain their build output. No profile activation
has occurred during these checks.

Final committed-head real-editor harness at618 passed in49s and exact generic
CI36860394508 concluded success. Separate evidence is in
`/tmp/portal-review-final-618df553/`; batchstatus0,elapsed303s. The normal candidate
switch command and forward recovery conditions are in state.md Next actions.
Run it only when the normal idle guards pass. Do not infer activation from the
checks: selected profile is still51i; live new UI acceptance follows selection.

## Executed repository-review follow-up activation

After the bound conversation became idle, the guarded candidate switch ran from
clean workspace head `aca3b39d` and selected package
`bpzvfhdnrj3clw9zfd1qhrhw7fjksyvb`. A fresh Luna/low observer reported exit 0
after 88 seconds. The transient user unit finished successfully, the portal
restarted as PID 2031444, and the selected package includes Codex 0.159.2.

Live staged and unstaged POSTs for the vpsadmin repository in
`2026-09-23-storage-redesign` both returned HTTP 200 with `files: []` and
zero-file statistics. Chromium acceptance against the live router passed with
no page errors and confirmed one repository per row, all four desktop actions
on one line, no narrow-screen overflow, collapsed history defaults and reload
reset, retained disclosure state during refresh, Origin links, and the Load all
diffs control. The final browser run exited 0 in 8.8 seconds.

No configuration generation was selected and no shared DNS zone was published
by this profile-only rollout. No feature branch was integrated into a default
branch.

## Preselection guarded-switch attempts

The first transient launcher failed before identity/prechecks because its PATH
lacked dev-session (status1/0s). The explicit-PATH v2 launcher ran the normal
candidate switch, which refused quiescing the bound lead thread while its turn
was inProgress (status1/59s). Authoritative before/after selection remains bpz;
z20 remained unselected after these two attempts. Normal guards/restoration were respected. Final evidence
is retained under `/tmp/portal-card-summary-deploy-cd2875{,-v2}/`. Any continuation
must wait for normal idle and preserve the selected profile on another refusal.

## Authorized idle-gated continuation prepared

The latest user authorization covers the profile switch and normal live portal
acceptance on storage-redesign. Architect0 confirmed a bounded public read-only
idle gate. One named transient operation waits for this lead turn to finish,
then runs the same source switch once with all normal guards, actual selected
package/service/model checks, and the prepared live harness. Evidence is retained
under `/tmp/portal-card-summary-idle-deploy-accept-cd2875/`. Until its completed
status and selection were checked, bpz was the last proven deployment. This
prepared continuation subsequently selected z20, as recorded at the top.
The four-host DNS candidate remains prepared but expressly unpublished; no
default integration or other lifecycle/system/cluster action is included.

## Post-deployment acceptance continuation

Latest user instruction: preserve selectedz20 and do not retry the profile
switch. Implementer0 owns only the bounded ephemeral live harness correction,
with the original failed script/log retained. A fresh Luna/low watcher will run
only that corrected normal live probe. Deployed evidence is complete; live card
acceptance is not yet claimed. No shared DNS/configuration/default or session
lifecycle action is included.

## Live-only v3 result and teardown correction

V3 printed complete aggregate `ok:true` acceptance JSON (six frozen summaries,
layout/spacing, retained history, empty staged/unstaged snapshots, reload/assets
and no page errors), then remained alive in proxy teardown. Its six initial
workflow states were unavailable; nonempty counters/run-link focus were not
observed. User-authorized SIGTERM of the watcher's verified owned Node child
completed the operation at status143/751s. Preserve it as incomplete despite the
assertion result. Artifacts are `/tmp/portal-card-summary-live-only-cd2875-v3/`.
A separate ephemeral v4 owns/destroys upstream ClientRequests and awaits proxy
close, preserving all acceptance assertions. One fresh live-only watcher follows
inspection. Selected z20, DNS/configuration hold and unmerged defaults are unchanged.

## Source integration complete; deployment unchanged

Explicit user approval now covers all seven registered repositories/defaults.
Generic869 and extension074 merged unchanged; configuration9824 and workspacec3
are conflict-free, independently reviewed equivalents of d24/cd287 rebased onto
fresh defaults. All seven exact final feature heads are proved ancestors of the
remote defaults. This supersedes earlier "integration unapproved" statements,
which remain dated rollout history. See integration.md and handoff.md.

z20 remains selected; its profile switch was not retried. Shared DNS publication
remains held, and the rebased configuration's newer base lock requires current
DNS consumer checks before any later deployment. The user requests initial CI
URLs/states only; completion is not awaited. No lifecycle action is authorized.
