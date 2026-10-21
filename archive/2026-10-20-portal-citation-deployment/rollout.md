# Citation deployment on aitherdev

Current phase: deployed, live-verified and merged. All required CI, including master-only host/boot checks, passed. All final resource claims
were released. User authorization covered rebasing, aitherdev deployment and
conditional integration after verification; no reboot or session closure occurred.

## Executed final rollout

Final source: client5797219, runtime52dcd471, workspace0ea56824,
configuration86e19685; extension remains767dfd5 and native Codex0.163.0.
Affected final review accepted; branch runtime CI39495715721 passed. Both fresh
artifacts built/copied, then system and profile activation passed in99seconds.
Exact final artifacts: [title-artifacts.json](title-artifacts.json).

Live original response acceptance passed: unchanged recorded text, numbered
PyPI links with title hovers, portable Copy Markdown, preserved table/code and
historical paging. Browser blocked all HTTP writes, including expected automatic
queue reconciliation attempts. [Browser result](final-live-browser-result.json)
and [continuity](final-live-continuity.json) retain evidence. TLS health also
passed using the configured development CA and owner credential in memory.
Native executable, process ID, socket and existing tmux sessions survived both
application switches; no reboot or turn submission occurred.

All four final heads were integrated into remote master by fast-forward-only
merges and SSH pushes: [integration result](integration-result.json). Required
configuration hooks and environment ran. The first integration attempt stopped
before configuration Git execution because of the shell working directory;
resumed with exact remote proof, preserving the two earlier successful merges.
Temporary target worktrees were removed; feature and deployed predecessor refs
remain. Both repository/machine claims were explicitly released.

Post-merge runtime CI39498997537 passed all four jobs, including the
master-only host/boot checks. Earlier preparation and first-rollout records below
are historical, with all failures and corrected verification retained.

## Current claims rollout

Source branches: `2026-10-20-portal-citation-investigation`. Deployment workspace
and configuration branches: `2026-10-20-portal-citation-deployment`; both match
the exact final source heads. See source `rebase-final-inventory.json`.
Client 5797219, runtime d245416, workspace 8d3b692b, configuration f14ed596.
Extension remains 767dfd5 and Codex remains 0.163.0.

1. Complete affected-change/history review and exact-head CI. Run packaged
   verification and build system/application from final committed sources.
   Use confctl build, then deploy --copy-only with the named generation.
   The application is built independently with nix build --no-link.
2. Request machine-only claim `vpsfree:aitherdev` using managed deployment
   owner. Confirm held status before activation. Baseline at 20:18 UTC:
   system/live profile w7abv0q..., application i2q0yyj.... Refresh before switch.
3. Run confctl deploy with the exact generation, dry-activate-first, enabled
   auto rollback and no reboot. Verify live/system profile identities.
4. Run ordinary workspace-host switch --source for the clean composed
   deployment workspace tree, passing held claim and exact paired identity.
5. Verify app/system sources, router/portal/coordinator health and unchanged
   Codex executable/process/socket and tmux continuity. Read original HaveAPI
   response in browser without sending any turn; check PyPI numbered links,
   title hover, table/code preservation, copied Markdown and paged repair.
6. On successful verification, reacquire repository claims; capture final
   comparisons and integrate all four reviewed branches into master by
   fast-forward-only merges and SSH pushes. Preserve unrelated shared files
   and all feature refs. Release machine/repository claims after effects verified.

Recovery follows current configuration operations guidance and installed claim
and coordination operations guides. Keep machine claim through diagnosis.
System ambiguity requires inspecting both live and system-profile paths and
confctl rollback status before another action. Application recovery is forward
only through supported workspace-host journals; never select an older package.

## Historical preparation-only phase

## Reviewed source

| Component | Revision |
| --- | --- |
| codex-web | `8c616f768b38179754f5b3bf4f974906ee9f1a8e` |
| dev-workspace | `f92f63c76194555a6f3f320e0ddbe03300ff71d7` |
| workspace | `fe1a94f5832317f1133135854827fe14effd8c8d` |
| vpsfree-cz-configuration | `e43cc01f4cb596206d4fc686ae42df2f2d42dad3` |
| vpsfree-dev-workspace | `767dfd587e346168e1443e65ccdb67ce748f3fe3` |

Final Astra/xhigh review accepts all four exact ranges and all four lanes;
histories are consolidated, deployed baseline preserved, and there are no
migrations. See review-baseline-refresh-astra-result.md. Both source CI runs pass:
client 39439556309 and runtime 39439858211 (fast/archive/creation; host skipped).
ci-summary.json binds their exact heads. Composed workspace/configuration locks
select the same runtime and preserve the extension and unrelated inputs.

Source branches belong to 2026-10-20-portal-citation-investigation. This managed
owner has its own matching workspace/configuration branches at the exact reviewed
commits. The application comes from its user profile. The system is built from
the exact final configuration commit because confctl embeds its revision.

## Preparation and retained ownership

Managed owner: `70774b4b-7e59-433d-9332-a059fce51ea0`.
Preparation requests: machine-refresh-request.json and profile-refresh-request.json.
They bind checksummed final review, source inventory and completed CI evidence.
The parent completed sequential coordinator prepare calls from the configuration Nix
shell with its installed ignored Bundler gems. The fresh Luna/low utility observed
only. Results are machine-refresh-result.json and profile-refresh-result.json;
refresh-preparation-result.json records process exit status and timing.

The configuration's ordinary Overcommit checkout hooks remain active. The first
ambient-shell attempt failed before building; rerunning the retained checkout
hook with the declared Nix/Bundler environment passed. The current prepare calls
start with that environment. No hook, admission check or ownership guard is bypassed.

The immutable adapter's prepare branch builds, copies and observes. Dry activation,
no-reboot switch and system-profile publication belong to its separate activation
path. No approvals, submitted jobs or reservations are created by this preparation.
The browser optional-question initiative held aitherdev for review at the last
observation; do not bypass its ownership.

## Current sealed artifacts

| Operation | Snapshot | Artifact |
| --- | --- | --- |
| System | `sha256:c636ea38c3a04c64cae406aac8f276193bc6ffba0f36dec1754712bbe5e68514` | `sha256:bdc4475d18271c531b5e838997c41c40fc98e81bc901ff79850fea4d156438b3` |
| Application | `sha256:2da656a50bc00bd25b7761e8d5180e8d3032bce9bf617d13711a3b98dcef1f45` | `sha256:31247cc8d966547feaa0bd879dd7fb5100a86aa32077104dd16651257720d8a1` |

Built system: `/nix/store/3q60cficds03fm1pj25ifaa4nzcn3s9j-nixos-system-aitherdev-26.05.20261019.f3a73bc`.
Built application: `/nix/store/0kiknnxh7qzlrjjk6admwnyxfim0rhjl-dev-workspace-0.2.0`.
System generation: `2026-10-20--17-06-00`.
Codex remains `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex`.

prepared-summary.json binds sources, snapshots, artifacts, derivations and
checksummed review/CI evidence. Both operations exited 0; final live-after-refresh.json
matches both sealed baselines. System live/profile remains 2fn0j9v and application
pys2l19 with token 1708fb6e5f914f34f0ba44c9c7a0f88fcb14efa5f26f272db3b2705c9f28eba1.
No current deployment has been submitted. Final coordinator revision 5703 shows
no owned jobs/reservations and the other initiative's deployed_review reservation.

## Activation after explicit direction

1. Read authoritative coordinator status, both system live/profile paths and the
   selected application token. Refresh any expired or stale preparation. Check
   every source and artifact identity against the accepted reports and CI receipts.
2. Record actual user deployment direction for the named machine and actions.
   Approve the exact snapshots and request `vpsfree:aitherdev` near submission,
   through ordinary coordination. Preserve all source integration obligations.
   Activation must wait for the existing reservation to be released normally.
3. Submit machine_activate, then dependent profile_activate under the same
   reservation. The confctl adapter performs dry activation immediately before
   its no-reboot switch. Do not use direct deployment around coordinator ownership.
4. Verify both system paths, selected application package, runtime composition,
   router/portal access, Codex/tmux continuity and reservation ownership.
5. Open the original HaveAPI conversation read-only. Confirm numbered PyPI source
   links with title hovers, intact Markdown/table presentation and ordinary source
   links in copied text. Check older pages and refresh. Do not send a new turn.
6. Keep the reservation during user review and any authorized iteration. Release
   only through the supported finish/archival policy and its required proofs.

Deployment direction does not authorize any master integration. No source or
configuration branch may be merged without its explicit direction. Keep both
initiatives open unless their lifecycle is separately requested.

## Recovery and expiry

Follow configuration docs/operations/workspace-coordination-aitherdev.md and the
selected runtime's coordination/coordination-operations guides. Reconcile the
exact original attempt after an interruption or ambiguous result. Preserve
journals, receipts, logs and roots. Check /run/current-system and
/nix/var/nix/profiles/system because live switch and profile publication can diverge.
Preserve confctl auto-rollback. Application selection is forward-only: recover
the admitted candidate or a reviewed compatible successor. Do not blindly replay,
reboot, force-release ownership or select an older application.

Unused preparations expire after seven days; status reads do not renew them.
A change of selected package, profile token, live system, catalog or relevant
source invalidates its bound baseline and requires appropriate refresh.

## Historical preparations

Initial reviewed source 4b73d71/52f87e1/bbd090ee/39949743 passed CI and both
preparations. During acceptance, another deployment selected the newer application
pys2l19 with token 1708fb6e5f914f34f0ba44c9c7a0f88fcb14efa5f26f272db3b2705c9f28eba1;
those initial snapshots are stale. machine-prepare-result.json and
profile-prepare-result.json remain historical evidence only. The initial system
snapshot was 8bb85e86a05a051d090526d9dc64e00e3d9615cfc922f307f53971a0981d2121,
and the profile snapshot was 2b4a152876e88c79656e59f2bb3ce8968a7d252ee1808175e4741d31b15b1f26.

All 502 tracked files of the newer deployed runtime exactly matched 6865e00.
The current candidate preserves its optional-question/receipt changes and the
shared absent-delivery fix. Cache versions advance to conversation v17/app v47.
The host baseline also advanced externally to 2fn0j9v during the initial build;
no system/application activation was performed by this initiative. Historical
baseline observations and artifact JSON remain alongside this record.

Reviewer reconnect errors initially hid real backend work. The client was resumed;
a default-model completion was explicitly qualified. Final acceptance was then
completed under verified Astra/xhigh. review-blocker.json now records resolution;
no account/provider configuration changed and no account input is required.
