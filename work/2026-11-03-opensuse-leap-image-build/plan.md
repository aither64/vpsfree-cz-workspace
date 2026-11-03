# openSUSE Leap 16.1 container image

Add an openSUSE Leap 16.1 container image build definition in vpsadminos and
register it in the image repository configuration. Preserve existing images and
follow the current openSUSE conventions. The architect will identify whether the
repository registration belongs to vpsadminos or a site configuration repository.

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
