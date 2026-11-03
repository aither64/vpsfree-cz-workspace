# Fedora 45 container image

## Goal and scope

Add a Fedora 45 image build script for vpsAdminOS and register it in the
container image repository configuration, following the existing Fedora images.
Publish reviewed feature branches. Default-branch integration requires separate
explicit user direction; no deployment or image publication is currently planned.

## Affected repositories

- `vpsadminos`: image script and image metadata/test discovery as required.
- Container image repository configuration owner: architect to identify from
  canonical source before expanding the affected repository set.

## Approach and ownership

1. Architect `architect0` verifies live upstream RPM names, existing conventions,
   configuration owner, and verification requirements; records `design.md`.
2. One implementer owns the narrow execution package through source edits,
   quick checks, hooks, commits, publication, and review fixes. Split only if
   independent repositories justify parallel packages.
3. Lead accepts evidence and assigns retained `reviewer0` for final independent
   committed-branch review before the image integration test.
4. Fresh verification utility runs the Fedora 45 image test and any relevant CI.

## Compatibility and recovery

Prefer additive Fedora 45 support; retain existing supported Fedora images and
avoid unrelated release updates. No schema, protocol, or persistent-state changes
are expected. Existing image consumers should continue using their selected
versions. Reverting the new registration and script restores the prior source
configuration; deployment ordering and image publication remain outside scope.
The design will identify any actual incompatible prerequisite before execution.

## Documentation

Readers are image maintainers and repository operators. Use existing build/image
metadata as the primary durable explanation; update project documentation only
where the new release requires instructions. Keep upstream evidence and check
results in session records, with the final handoff linked from state.

## Acceptance and testing

- Fedora 45 metadata/build files follow existing stable Fedora conventions.
- Release RPM filenames are verified using live upstream HTTP listings.
- The image repository config includes Fedora 45 for the expected architecture.
- Required hooks, syntax/evaluation checks and independent final review pass.
- Run `./test-runner.sh test image-scripts/test@fedora-45` after review,
  using the repository environment and delegated long-check policy.
- No unexpected local kernel build, unrelated distro edits or unapproved merge.
