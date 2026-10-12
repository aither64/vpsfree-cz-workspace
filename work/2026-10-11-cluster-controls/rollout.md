# Cluster controls: aitherdev rollout

Host and application deployed and verified. The user authorized the approved
plan. No default branch integration is authorized.

## Selected sources

Runtime: bc6b841be0bf83ad84f47daa2e0c064f477bdf23.
Extension: 7157c8098dcf60127aa4df823fab82b4185ad22a.
Workspace/configuration feature worktrees: worktrees/2026-10-11-cluster-controls/.
Exact feature heads and full series: final-heads.md; original review packet:
review-packet.md.

Both runtime selections match. Only the two intended workspace source nodes
and configuration's devWorkspace node changed; sibling selections preserved.
The composed deployment contract passed.

## Before rollout

Application: /nix/store/sfsck9wxbhkrzl5qygcxxm096bmhdg5v-dev-workspace-0.2.0.
System: /nix/store/2049p019hn0vl21j2a45n8hi1wa2gndz-nixos-system-aitherdev-26.05.20261010.6fcc160.
workspace-portal@vpsfree-cz.service and workspace-router.service are active.
Inventory confirms cz.vpsfree/machines/aitherdev is the exact confctl target.

## Planned execution and recovery

After independent review and package/browser checks, build the exact host with
confctl; dry-activate, then switch with health checks. Switch the application
with the installed workspace-host switch --source pointing to the composed
workspace feature worktree. Keep logs/status via a transient user service and
a fresh verification watcher. Check selected profile, portal/router health,
authenticated shipped assets and an owned disposable bridge cluster.

Workspace package transitions are forward-only. Preserve the previous source
and generation for diagnosis; recovery repeats the candidate switch or selects
a newer compatible package. Do not attempt workspace-host rollback to an older
package or bypass a refused transition. System activation retains confctl's
normal rollback/health-check behavior. No disk/state migration is introduced.

Stop and investigate an unexpected local kernel build before continuing.
Live Stop/Start validation must compare a known file's contents before/after;
Release must remove only this initiative's disposable cluster.

## Execution

All local checks and CI passed before the host build. The first build stopped
at its confirmation prompt without deployment; the corrected --yes run passed.
The exact configuration head is 4d0ff7cdb4e56f89cf27bb53a433124736f7e410.
Confctl built generation 2026-10-11--23-28-41 for the exact aitherdev target.
Evidence: host-build.log and host-build.status (0). The retry watcher's own
wrapper log was empty because the prepared script redirects to these files;
the primary verified the actual log and status directly after completion.

Parent-launched deployment unit: cluster-controls-deploy-20261011.service,
invocation ab50951eb4c24418af127c8b17eeb79c. The fresh deployment_watch watcher
reports host-dry, host-switch and workspace-switch status 0, with 2 host health
checks passed and 0 failed. The new selected generations are:

- System: /nix/store/ccgznwp2rv7bkpvxgp0rvw334dkhy48r-nixos-system-aitherdev-26.05.20261010.6fcc160.
- Application: /nix/store/hw9v17h981wwqflqxiy87ym7l4x8qi7c-dev-workspace-0.2.0.

The unit's final verification stopped because its inherited groups could not
read the root-owned portal password. The current tool shell has the configured
owner group; no file permissions or password were changed. A separate inline
verification passed (verify-live.status 0): authenticated HTTPS HTTP 200/TLS 0,
app.js and style.css exactly match the reviewed source, and portal/router are
active. Credentials stayed in shell memory and curl stdin.

Disposable-cluster validation runs under the declared owner group so its
authenticated portal requests can read the existing password. The first
attempt reached initial readiness, then failed on the verification script's
missing SSH -- separator. Its unit exit stopped the runner, retaining disks and
configuration. Corrected verification uses normal retained Start with the
saved single/bridge selection; no reset or source changes.

Corrected verification unit: cluster-controls-live-retry-20261011.service,
invocation 2a508ae6d44447018e6865b55752915f, launched once by the fresh
Luna/low live_cluster_retry watcher after completing the required reads.
Installed catalog digest remains
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd;
utility model/effort and behavior were resolved from that catalog. This tool
API exposes model/effort but no custom native-role selector, so this is a
catalog-policy fallback rather than a claim that a native TOML was loaded.

That attempt failed before guest SSH/network startup had finished. Existing
runner readiness waits for the OSVM control shell; the guest console shows
service and SSH host-key startup at the time of the connection failure.
The failed attempt is preserved as live-cluster-network-wait.*. Verification
now probes SSH/tank readiness before initial file creation and after portal
Start, without retrying Start requests.

Final validation unit: cluster-controls-live-services-20261012.service,
invocation 9bd034544405446eb44013c6fce7ab2a, launched once by the fresh
Luna/low live_cluster_services watcher using the same catalog policy.

The final validation passed with status 0 and phase complete in about 10
minutes. The known file /tank/cluster-controls-check, containing
cluster-controls-disk-retention, survived authenticated portal Stop/Start.
The stopped provider retained single/bridge and advertised Start/Release; after
Start it reported running/ready with Stop/Release. Authenticated portal Release
succeeded and removed the owned cluster directory. The primary verified that
absence and the exact success log. Readiness probes resolved the transient
network/SSH/tank startup lag; no unexpected kernel build or cancellation
occurred. The same retained disks were used until the final Release.

Deployment is ready for use. All four feature branches remain published and
unmerged; the active initiative awaits explicit integration direction. No
archive, delete or session stop was performed.

## Inset Reveal rollout: deployed and verified

User approved embedding the eye inside secret inputs and removing external
placeholders. Generic source 60c679c52c263a0fc7a4b08c5f83a291cfd89191; extension
7157c8098dcf60127aa4df823fab82b4185ad22a unchanged. Consolidated configuration
e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566 and workspace
86d96b2656c89f37cd4d521fb150ebb123efa89c select this composition. Initial deployed
configuration/workspace revisions remain published on rollout-1 refs. Quick checks
and exact deployment contract passed. Generic CI 38216790841 passed.

Prepared inset-checks.sh runs both browser engines at desktop/mobile widths with
long secrets, generic package/host-package contract, composed workspace flake
checks and exact aitherdev confctl build. Independent review gates execution.
Prepared inset-deploy.sh guards both prior generations and exact source heads,
dry-activates/switches matching configuration with health checks, switches the
user-profile application through its stable command, and compares authenticated
assets. Launch under workspace-portal-owner to avoid inherited user-manager
group omissions. Evidence goes to inset-checks.* and inset-deploy.*. No new live
cluster is needed for template/CSS-only behavior; unchanged disk-retention
validation above remains the backend evidence. No default integration authorized.

Independent review passed with no findings; all prepared checks/builds passed
(status 0, about 25m40s). Built aitherdev generation 2026-10-12--10-08-43. Parent
launched cluster-controls-inset-deploy-20261012.service once, invocation
3379efe48b994cd7b6fc3ddb132d6a88. Fresh Luna/low inset_deployment_watch observes
the unit and independent logs/status; it does not deploy. Guards remain the
previous exact system/profile and reviewed source heads.

The rollout passed with status 0 and final phase complete in about 3m49s.
Dry activation, host switch and application switch succeeded; host health checks
passed 2/2. Selected generations:

- System: /nix/store/bz16nqb4iq55kg52nc16621hgx08rkzw-nixos-system-aitherdev-26.05.20261010.6fcc160.
- Application: /nix/store/0yf4aajlf1jp68ab4d0llar89lf91i5x-dev-workspace-0.2.0.

Authenticated HTTPS returned HTTP 200/TLS 0. Live app.js/style.css match reviewed
source, portal/router active. The owner-group launcher avoided the first-rollout
credential-read problem; no credential or file permission changed. Parent checked
actual status, final phase, bounded log evidence and selected generations after
the watcher finished. No operation remains running. Evidence: inset-deploy.log,
inset-deploy.status and inset-deploy.phase.

Ready for use. All four final feature heads remain published and unmerged; user
owns the integration decision. Primary pin streams each contain one final update;
rollout-1 source refs remain preserved. Initiative stays active.
