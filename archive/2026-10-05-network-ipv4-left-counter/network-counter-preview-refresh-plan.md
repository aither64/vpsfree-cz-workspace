# Manual interface preview refresh

The user requested a running cluster for UI review. Preserve the existing
session-owned single topology on br0 and its database/disks, OAuth credentials
and sessions. Do not stop/reset it or activate new workspace packages.

After current-head hosted quick checks and independent source review, refresh
only services through the installed public provider:

    vpsadmin-devcluster update 2026-10-05-network-ipv4-left-counter services

This is the manual preview deployment requested for interface inspection, not
local CI or a verification-suite launch. No local API/PHP/React/VM/config12 tests
or KB captures are selected. No production service or default branch is changed.
Unexpected local kernel compilation must stop and be investigated. Quiet work
is not a generic timeout. A copy/activation/refresh failure retains the pending
same-target journal and existing state; diagnose it without resetting disks,
rotating credentials or selecting another target.

Selected clean sources must be Vcc8e9e7e and Wce856841.
The latter includes the shared viewport-safe inventory descriptions. Record the exact built
services toplevel and distinguish it from activation: success requires the
public update's resident-closure/current-system/GC-root proof and completed
service restart plus normal Node refresh. Public status is selected-build
metadata only. Check both HTTPS endpoints with the cluster CA, then leave the
cluster running. Login details remain in the portal's Development clusters
panel, never in public artifacts.

Source preparation inspection: current tasks/gem_updates.rb `vpsadmin:gems`
refreshes dependency lock/gemset metadata; it does not compile changed API source.
The modified API model/resource files remain direct `vpsadmin-source` inputs to
packages/api/common.nix, which copies api/plugins from the source. No new runtime
file, Gemfile or gem declaration changed in this refinement; fresh default81
already owns its packaged dependency update. Do not introduce unrelated floating
gem updates to make source edits visible. If the public update reports a genuine
packaging prerequisite, investigate that concrete failure before any generator.

The preview stays at its earlier selected sources until this operation succeeds.
The two pending CS/EN KB PNGs require a separately supported owned capture route;
manual preview success does not establish generated-artifact freshness.

Read-only public services SSH preflight on 2026-10-08 found 7.3 GiB free
on its retained 12 GiB root. This is an observed preflight, not proof of the
new closure size or successful copy/activation. A fresh public SSH observation before review completion confirmed the same7.3 GiB free. Credentials and config are not exported.

Before refresh, public SSH confirmed the services running closure:
/nix/store/739wspgj34k40cwk4j72pxwhdwi331a3-nixos-system-vpsadmin-services-26.05pre-git.
This records the predecessor only; it does not imply automatic rollback after a database migration. Affected review cleared with no new findings. Root launched the supported public services-only update; fresh Luna/low utility network_counter_preview_refresh2 owns monitoring of its private log/exit. Completion/activation is not yet claimed.

Outcome: the supported update completed exit0. Live current-system matches the exact candidate; applied pending is null, final API/React source proof matches, both CA-verified UI endpoints return200 and the API/UI/scheduler/supervisor units are active. Expected normal node runtime refresh completed. See network-counter-preview-refresh2-result.md/json; the cluster is left running. No local CI, default integration, production deployment or KB write occurred.
