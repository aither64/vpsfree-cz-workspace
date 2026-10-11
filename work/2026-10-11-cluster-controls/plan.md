# Dev cluster toolbar and credential controls

Implement the user-approved plan: a visible Start/Stop and Release toolbar at
the top of each cluster card beside state and Ready; aligned icon-only Reveal
and Copy credential controls. Normal Start reuses retained disks, topology and
network and builds current session sources.

## Projects and ownership

- dev-workspace owns portal templates, browser behavior, HTTP controls and
  provider status decoding.
- vpsfree-dev-workspace owns vpsAdmin/vpsAdminOS helpers and available actions.
- workspace owns the composed runtime/extension pins and session records.
- vpsfree-cz-configuration owns matching aitherdev host runtime selection.

The initiative was created with dev-session start cluster-controls --no-codex
--no-attach. This external caller has no bound native lead or retained roster;
the primary agent owns design and edits. Mandatory review uses the installed
default-team fallback; long verification uses the site utility watcher policy.

## Accepted behavior

Credential rows use value, reserved reveal slot, copy slot. Reveal toggles the
eye icon and accessible state. Copy reuses the existing SVG and preserves it
during feedback. Connection commands also use copy icons. Toolbar controls
wrap on small screens, display progress inline, preserve the service tab and
update without reloading. Start and Stop need no confirmation. Release confirms
that persistent disks and cluster state will be deleted.

Add start-cluster and stop-cluster POST endpoints accepting kind; retain the
release-cluster route. Providers add start <slug> --existing under their existing
lock, refusing missing retained state and selection. Ordinary CLI defaults stay
unchanged. Opt-in DEVCLUSTER_PORTAL_CONTROLS=1 status metadata advertises available
start, stop and release actions. Busy/unavailable and maintenance status disable
unsafe actions. Reject overlapping portal actions. Bound Start to 30 minutes;
Stop/Release retain the 180-second shutdown budget. Do not cancel accepted work
on a browser disconnect or automatically retry an uncertain response.

## Compatibility and deployment

Keep persisted cluster state, session manifests, lifecycle journals and catalog
schemas unchanged. New readers accept helpers without actions and show only
Release. New helpers emit actions only for the opt-in reader, so old portals
continue to parse ordinary status. Existing disks survive Stop/Start. Providers
remain responsible for source/schema compatibility and maintenance refusals.
Use the ordinary generation, lifecycle and ownership checks; no force flags.

Publish reviewed feature revisions, update the workspace's exact extension and
nested runtime selections, and select the same runtime through configuration's
dev-workspace/devWorkspace channel. Check the deployment contract. Deploy the
host substrate from the configuration feature branch and the application from
its workspace user profile. Record pre/post generations and rollback sources.
No default-branch integration or session archival is authorized.

## Verification and documentation

Use each repository's Nix shell and hooks. Quick checks cover browser syntax,
focused Go/Ruby tests and diff validation. Complete and commit intended changes,
then independent review of complete branch history and final diffs before longer
package/browser checks. There are no migrations. Test credentials, mobile
alignment, service selection, retained topology/network/disks, maintenance,
missing state, failed builds, conflicts, deadlines and mixed provider versions.
Verify deployment with a disposable initiative-owned cluster; never operate on
another session's cluster. Preserve project control contracts in their guides
and individual rollout evidence in this session. Apply user-facing writing
guidance to labels, feedback and confirmation after technical facts settle.

## Goal

## Affected repositories

## Approach

## Decisions

## Compatibility and deployment

## Documentation

## Testing plan
