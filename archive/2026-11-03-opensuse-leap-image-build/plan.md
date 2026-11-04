# openSUSE Leap 16.1 container image

Add an openSUSE Leap 16.1 container image build definition in vpsadminos and
register it in the image repository configuration. All changes belong to
vpsadminos (default target: staging): image-scripts/images/opensuse-leap-16.1/
build.sh and config.sh, os/configs/image-repository.nix, and the required
tests/distributions.nix registration. Preserve existing images and follow the
Leap 16.0 conventions; move latest/stable tags to 16.1.

User clarified that the existing opensuse-leap builder must move from Leap15.5
to16.0. Update that shared builder, use it for16.1, and remove the separate16.0
builder added during the earlier interpretation. Older Leap builds also use the
updated environment; existing containers are unaffected. Reassess supported
consumer build checks and cached name-derived builder reuse before retesting.

Architect0 owns upstream investigation and the design/verification brief.
Implementation packages will be assigned after their file boundaries and
dependencies are settled. Implementers own changes, quick checks, commits and
follow-up fixes; reviewer0 independently reviews the final committed series.

Verify official upstream bootstrap inputs, inspect nearby image definitions,
run repository hooks and focused checks, then independent review before the
longer image build/boot test. Publish feature branches over SSH. Default-branch
integration and production deployment need separate explicit direction.

This is intended as an additive image change: no database, API, protocol or
existing container state migration. No coordinated node upgrade is expected.
Confirm supported bootstrap/runtime behavior in design and tests. Image builder
sources must support the new image before its repository job is activated;
rollback disables the new registration without modifying existing containers.

Readers are image maintainers and repository operators. Keep temporary upstream,
review and test evidence in this session; update project documentation only if
the new version needs lasting guidance beyond its conventional build definition.

## Additional requested milestone: openSUSE device units

User explicitly asked for the root cause and a real fix of openSUSE's existing
expected-failure device-unit test. Do not extend the expected-failure exception
to16.1. Architect0 owns the separate device-unit-design.md brief; implementer1
owns diagnosis/fix/tests/docs/commits after implementer0's shared-builder handoff.
Initial evidence is an inactive eth0 device unit and an archive containing rules
but no udev daemon/tools. Missing explicit udev under --no-recommends is a
hypothesis until RPM/runtime evidence and a package-only clean-boot experiment
establish causality. Preserve tenant isolation; no privilege expansion or host
kernel change without evidence. Accept only actual eth0 and dummy0 assertions
passing in rebuilt supported images, with final review and bounded relevant
checks. Keep this milestone separate from the original image/builder work.

## Delivered source outcome

The controlled experiment proved missing udev processing; explicit udev and removal of the obsolete exception are now committed. All four rebuilt images passed15/15 and all nine candidate-backed focused cases passed. User approved merge when done, and the exact reviewed/tested head `742eb30cb1a8b6766c85e915d26b0400e38244b1` was fast-forwarded and SSH-published into staging. See integration-result.md and state.md for proof and pending CI/publication limits. Production publication and existing-container changes were not performed.
