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
