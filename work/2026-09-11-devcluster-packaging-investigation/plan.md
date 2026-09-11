# Repair and validate both development-cluster providers

## Goal and decisions

Implement the accepted September 11 plan: fix packaged configuration and runner
assets, update the vpsAdminOS runner dependency interface, and stop startup and
updates on prerequisite failures. Deploy the repaired user-profile package and
validate both providers. Keep feature branches unmerged and the session open.
The password-reset session is read-only and must not be retried or reset here.

## Affected components

- vpsfree-dev-workspace: provider package, nested flakes, shell commands,
  regression tests, packaged Nix smoke app/CI, and provider documentation.
- workspace: dedicated feature worktree containing the extension revision pin.
- vpsadminos: opt-in NixOS root preservation in OSVM, tests/documentation, and
  an isolated live validation worktree. No production OS/kernel behavior change.
- vpsadmin: unmodified isolated validation input.
- Generic dev-workspace and system configuration remain at their existing revisions.

## Implementation

1. Install host-provided defaults as each packaged provider's default-config.json
   and copy the canonical Ruby runner library inside each flake under shared/.
2. Build both runners through one shared constructor using the exported
   vpsAdminOS overlays.all and vpsadminosRubyGemConfig dependency interfaces.
3. Preserve existing lock/environment semantics; explicitly propagate errors
   through credentials, configuration builds, start, update, copies,
   activations and refresh. Never use an old result-config after a failed build.
4. Add tests through actual locked commands and a devcluster-check flake app
   evaluating the installed nested flakes using locked test-only inputs,
   building/loading both runners without building or booting VM closures.
5. Update provider documentation to use installed stable commands and describe
   host-supplied defaults and failure behavior. Apply the writing skill directly.

Use separate functional commits for packaged assets, OS dependency compatibility,
failure propagation with focused tests, and expanded Nix verification/CI.
Keep generated dependency changes in their owning coherent commit.

## Compatibility and rollout

Preserve CLI arguments, default/override merge semantics, retained VM disks,
configuration/state schemas, socket identities, package-generation gates,
locking, and ownership. No production API, database, protocol, NixOS module, or node change is made.
The development OSVM API adds a default-off preserve_root_disk keyword. No
coordinated node update is required. Old packages can read cluster metadata,
but starting retained NixOS roots through the old runner can overwrite them.
Keep the new provider and compatible OSVM input together for VM startup.

Pin the reviewed extension in the workspace feature branch, retain other inputs,
build and check the deployment contract, and use workspace-host switch --source
with that feature worktree. Retain the previous profile for supported runtime
rollback, keeping clusters stopped if the target lacks persistent-root support.
Do not merge, archive, delete, or deploy system configuration.

## Verification and acceptance

Run quick syntax, focused Ruby and package verification, commit all intended
changes, then perform the mandatory general/architecture/scope/compatibility
review using gpt-5.6-sol at xhigh. Resolve findings before full flake checks,
branch CI and long integration tests. Investigate failures before reruns.

Test both providers through the real lock wrapper: credential/build/copy/activate
failures stop subsequent work, preserve previous state, and release locks;
success retains environment exports. Cover failed builds with absent and existing
result-config, defaults and per-cluster overrides, both network modes and both
runner loads from the packaged source snapshots.

After review/CI, deploy the candidate profile and run each provider sequentially
with single topology and explicit bridge networking. Verify address availability
and binary cache coverage first; no force/IP takeover or unintended kernel build.
Validate readiness/status/SSH, API/database/nodectld/osctld and a VPS operation
for vpsAdmin, and osctld/container creation/start/stop for vpsAdminOS. Exercise
update, stop, restart and retained-data markers for each. Stop only this
initiative's clusters at handoff; retain their disks and feature branches.

## Review decisions

Use the exported vpsAdminOS overlays and one shared organization-side Nix runner
builder, copied into each packaged provider flake with the shared Ruby library.
The upstream test-runner package does not expose an alternate-entry-point builder;
keep that constructor here without changing the upstream runner package interface.
Both providers require the overlay/gem interface from vpsAdminOS6f9b2c755 or a
compatible newer source. vpsAdmin additionally requires the persistent-root OSVM
API introduced by e6c4c5cfa. Update or backport the missing interfaces into older
development worktrees before start/update. No running machine coordination or disk
conversion is required. The runner reports the missing interface explicitly.
Also check post-build readiness/socket/log preparation failures and keep config
replacement on the destination filesystem.

Forced certificate-set replacement remains a separate hardening task. The existing
cert init/import --force path and encrypted-CA fallback can lose the old files on
a late replacement failure. This initiative guarantees failure propagation to
start/update, not transactional credential replacement. Live acceptance reuses the
existing valid shared certificate set and does not force replacement.

## Live startup follow-up

The first vpsAdmin boot exposed an SSH readiness race: osvm's shell-ready marker
precedes the node bridge address/sshd, so automatic pool refresh failed with SSH 255
(No route to host). Add a bounded 120-second SSH probe before services seed checks
and each node refresh. Retry only SSH transport failures from harmless `true`
probes; execute each seed/refresh action once and propagate its failure. Keep the
existing runner-ready definition, lifecycle locks and generic runtime unchanged.
Add a command regression for transient node SSH 255 and review before redeployment
and repeated startup acceptance. Continue diagnostics on the already booted cluster
using the previously reviewed package while this narrow follow-up is prepared.

## Persistence extension after live restart

The final bridge restart proved SSH waiting works, then exposed osctld socket/pool
readiness. The new node wait observes both ZFS import and osctld active state before
any filesystem/device mutation, with a180-second process timeout and one second
forced-kill grace. Actual remote-script tests cover delayed and never-ready pools.
Focused command suite11/139 passes. Initial new test failed only because the fake
nodectld socket was absent; fixed the fixture to model it without writing host /run.

The same restart exposed a distinct data-loss behavior in upstream
osvm/lib/osvm/nixos_machine.rb: prepare_disks unconditionally deletes and recopies
the NixOS root disk. Services MySQL had no VPS rows after reboot while node CT3
retained its files. Only this initiative's disposable data was affected. The
password-reset session remains untouched.

Extend the affected vpsAdminOS repository from validation-only to an implementation
branch: add an opt-in preserve_root_disk keyword on NixosMachine, default false for
ordinary isolated tests. Copy new roots atomically, continue preparing extra disks,
and retain explicit destroy/reset behavior. The organization runner requests this
option for NixOS guests and refuses an OSVM input lacking it before any VM starts.
This intentionally raises the vpsAdmin provider's OS input minimum to the new
feature revision. Pin it in packaged smoke inputs; current/older standalone OS
provider sources still use the previous overlay minimum. Keep all branches unmerged.
No production daemon, schema, protocol, kernel or coordinated node update changes.
The generic workspace runtime remains unchanged.

For retained NixOS roots, configuration closures must be copied/activated with
update while the VM is running before restarting with a changed configuration.
Do not restart existing NixOS disks using an older provider/OSVM combination: its
fresh-image policy can erase them. No root data conversion is required; existing
complete images are reused. Follow-up tests will create a new API VPS record in
the fresh fixture database and prove both its row and container data survive a
full stop/start. The earlier orphan CT3 is retained as evidence, not reset.

Publish reviewed OSVM feature first, update organization test pin and consumer pin,
then deploy the user-profile package. Use the already reviewed deployed provider
for independent configuration-update checks while preparing this fix; do not run
the new runner before mandatory review.

## Final acceptance and scope decisions

The final installed package passed both providers' live bridge lifecycle/data
checks; clusters are stopped with disks retained. Organization CI, packaged
smoke, OSVM unit/lint checks and both driver integration tests passed. Broad OS
CI is not green: inspected artifacts show baseline livepatch/NFS fixture failures
and an Alpine package setup failure; current NFS cleanup also faults in unchanged
kernel code. Intel livepatch testing remains outside the changed NixOS driver
path. Record all CI state explicitly; do not widen this repair into kernel, NFS
or livepatch test changes or use a blind rerun to claim success.

The existing vpsAdmin120-second stop fallback is shorter than sequential DNS
service shutdowns. It stops the owned processes but can leave stale PID/readiness
files, cleared by another stop. Retention passed after such a stop. Improving
graceful shutdown remains a separate follow-up. No cluster data reset is needed.
