# Development-cluster acceptance

Only initiative `2026-09-11-devcluster-packaging-investigation` was used. The
password-reset session and its cluster state were not changed. Branches remain
unmerged; this session remains open. Single topology and bridge networking are
the acceptance configuration.

## Final revisions and installed package

- Organization extension: `19238ca67ad822b362ae60f0cf7e7b4b27d60397`.
- Workspace pin: `7f083fb38d7c24f910e9de54da4c1f49ff504d8e`.
- vpsAdminOS / OSVM: `e6c4c5cfa27ce3b139bba6475be80cfead4b8df4`.
- Unmodified vpsAdmin validation source: `8d0ccafd5b307115ddc4b1f24152ba30ed52e893`.
- Installed user profile: `/nix/store/qvdcxfks49mhgpamiy07qr0h95skzpia-dev-workspace-0.2.0`.

The generic runtime and its dependency graph remain unchanged. No system
configuration was deployed. The runtime state/socket contract is byte-identical
to the predecessor. Router, portal, Codex, tmux and reconciliation services passed
post-switch health checks; the internal portal responds with its expected
unauthenticated HTTP401. The previous profile remains available, subject to the
persistent-root rollback constraint below.

## Checks and review

All four mandatory review lanes and required remediation reruns passed with no
remaining findings. Final follow-up reviewers used gpt-5.6-sol/xhigh.

- Full local organization flake check: passed.
- Provider command regressions: 11 tests / 139 focused assertions; 138 assertions
  in the Nix sandbox because of the lock timing assertion. No failures.
- Shared runner contract: 3 tests / 7 assertions, passed.
- OSVM specs: 111 examples, passed; normal hooks passed.
- Workspace deployment contract: 3 tests / 14 assertions, passed.
- Packaged smoke: both providers, bridge/local, defaults/overrides (8 cases),
  plus both runner builds and actual Ruby loading, passed.
- Organization CI34631425856: passed at the final commit; see ci-result.json.
- OSVM RSpec and RuboCop CI: passed. Broad OS VM CI34630335805 is not green:
  its suite failed three scripts outside the changed NixOS driver; Intel
  livepatch remains running. See ci-investigation.md and ci-evidence.txt.

Both Linux6.12.109 kernels were substituted from configured binary caches.
No local kernel source compilation was performed. Shared certificates cover the
configured domains; no forced credential replacement was used.

## vpsAdminOS: passed on final package

Stable helper start/status/SSH, osctld and tank pool health passed. Created Alpine
container packaging-smoke and exercised start/stop/start. Host marker
`/tank/devcluster-packaging-marker` and container marker `/root/packaging-marker`
survived a changed-hostname update and whole-VM stop/start.

Repeated start with the final installed runner and OSVM input, explicitly using
`--network bridge`. Start returned0. Hostname dev-os1-updated and both retained
markers passed; the retained container started successfully. Final stop returned0; the VM is stopped and its disk is retained.

## vpsAdmin: passed on final package

All four VMs previously passed service health: MySQL, API, supervisor, both DNS
bind/nodectld units, node osctld/nodectld and tank. Seeded API node101 query and API
VPS creation/start/stop/start passed. Actual all-VM configuration update passed,
including a nodectld setting change. A second update copied and activated all
final selected closures before retained-root shutdown.

Live testing discovered and drove fixes for three additional startup/lifecycle
issues: SSH readiness, osctld pool readiness, and OSVM's unconditional NixOS root
replacement. The old root replacement erased the disposable services database
while retaining node container3. That orphan remains as evidence. Created new
API-managed VPS1, hostname packaging-smoke, and verified its database row, host
marker and container marker after the final configuration update and before stop.

Final bridge start returned0 with automatic SSH readiness, service-seed wait,
and osctld pool preparation; no manual refresh was needed. API VPS1 and hostname
survived. Host and VPS1 markers survived. All services and the active tank pool
passed health checks, with the final selected node/services closures active.
All three NixOS root image inodes/sizes remained unchanged. The retained VPS1
then passed API stop/start, and both markers passed again without being rewritten.
Final cluster stop returned0 through the existing120-second timeout fallback;
all four disk images remain retained. An idempotent second stop clears stale
PID/readiness markers. This is a completed stop, with the graceful-stop limit
recorded separately below.

An additional OS start omitted --network and selected local mode; it was stopped
and repeated on bridge. The accompanying vpsAdmin start was already on bridge but
was unnecessarily interrupted while diagnosing the differing defaults. Cleanup
needed TERM to its verified owned node QEMU after services shutdown left boot's
clock service waiting on DNS. This interrupted attempt is excluded from normal
lifecycle acceptance; no disk reset occurred. The final retention checks also passed after that interruption. Detailed commands and guards are recorded in state.md.

## Compatibility and separate limitations

The original password-reset OSVM revision lacks preserve_root_disk. Its attached
OS source needs the companion e6c4c5cfa change (or a compatible backport) before
vpsAdmin can start with the new provider. That session was left untouched.
Standalone vpsAdminOS keeps the earlier supported overlay/gem interface.

Retained NixOS roots must receive changed system closures through update while
running before booting a changed configuration. Do not restart these roots with
an older runner/OSVM combination that unconditionally replaces them. Existing
complete roots need no data conversion; explicit reset remains destructive.
No production daemon/schema/protocol change or coordinated node update is required.

The unchanged generic dispatcher discards piped SSH stdin; acceptance used safely
quoted command arguments instead. The disposable services CLI fixture needs the
actual API URL and matching auth entry. DNS nodectld can consume its90-second
systemd stop timeout during ordinary shutdown. The provider allows120 seconds
for the sequential cluster shutdown, so it can terminate the runner/remaining
VMs and leave stale PID/readiness files; a second stop clears those files. Provider network defaults differ:
vpsAdmin defaults to bridge; standalone OS defaults to local. Pass --network bridge
explicitly. These observations are recorded as separate reusable notes.
