# Scope and proportionality review: pool readiness and persistent NixOS disks

Lane: scope and proportionality
Organization range: `9e8783d68fdf40de04683e419d4f373bc27e3730..19238ca67ad822b362ae60f0cf7e7b4b27d60397`
vpsAdminOS range: `3eaf7b7320754715b38fc629e7f0ce23d13402cd..e6c4c5cfa27ce3b139bba6475be80cfead4b8df4`

## Findings

No Blocking, Important, or Advisory findings.

Both mechanisms are bounded extensions of the accepted live lifecycle
acceptance. The osctld readiness change extends the existing node-side pool
wait with one additional read-only state predicate and a process-level deadline;
it does not retry or generalize the later filesystem, device, or nodectld
mutations. The actual remote-script tests are proportionate to the demonstrated
socket/pool race and cover both delayed readiness and the permanent-failure
boundary.

The persistence behavior is split at the appropriate ownership boundary.
vpsAdminOS OSVM exposes one generic, default-off `preserve_root_disk` constructor
option for persistent custom NixOS runners. Its ordinary test-driver behavior
remains fresh by default, and explicit disk destruction still resets both root
and additional disks. The organization runner owns the provider policy by
enabling the option only for its NixOS service and DNS guests. This avoids a
provider copy or override of OSVM's protected disk-preparation internals. Using
the same atomic replacement path for initial and default fresh copies is the
smallest way to ensure that a failed copy cannot later be mistaken for a
retained root.

The raised input minimum is necessary because silently falling back to the old
fresh-root behavior would repeat the observed data loss. The preflight check is
performed before machine construction and PID publication, the packaged smoke
input pins the exact companion revision, and the standalone vpsAdminOS-only
provider does not acquire the new requirement. The provider and OSVM
documentation accurately bound the feature: existing complete images require
no conversion, configuration closures must be copied and activated while the
VM is running, and restarting retained disks through an older runner can erase
them. An offline closure installer or disk migration layer would be a material
and unnecessary expansion of this repair.

## Residual limits and test gaps

- A preserved root is accepted based on path existence. Completeness and the
  presence of the newly selected direct-boot closure are an operator contract;
  pre-existing partial images and offline configuration changes are outside the
  documented supported boundary.
- Rollback can read the unchanged disk format, but starting a retained NixOS
  root with an older provider/OSVM combination remains destructive. Recovery
  therefore requires keeping the new runner path or returning to the previous
  configuration before boot, as documented.
- The exact cross-repository heads have not yet completed the planned live
  stop/start retention proof. Unit and command tests establish local policy and
  failure behavior, but the API database row plus guest and host markers still
  need the packet's final live acceptance.
- The three-minute pool wait is tested with a shortened real `timeout` wrapper;
  the literal 180-second wall-clock path is not exercised. The fixed bound and
  one-second kill grace are directly inspectable and avoid adding a production
  timing interface solely for tests.
- The organization flake uses an exact feature revision while the companion
  OSVM change is unmerged. Integration must retain an input that contains
  `e6c4c5cfa` or a compatible successor; restoring branch tracking before that
  ancestry exists would violate the documented minimum.
