# 2026-10-12-streamline-vpsadminos-config-imports

## Goal

NixOS VPS (containers) on vpsAdminOS need to import vpsadminos.nix from vpsAdminOS into their configuration, since it contains settings needed for our environment. Different NixOS releases have different options, sometimes incompatible, so the users must import the right version of that config for their system. I'd like you to check if it is streamlined as much as possible, e.g. I guess we could import configs based on the user's nixpkgs release version. Do we do it currently?

## Affected repositories

- `vpsadminos`: flake module exports, stable guest templates, focused evaluation
  tests/CI, and owning-project documentation.
- Czech and English KB pages: NixOS, Impermanence, and User Data. These six pages
  are unmanaged; no KB contract repository change is needed.

## Approach

Implement the accepted plan (user: "Implement the plan", 2026-10-14). Architect0
records the design and verification brief before implementer0 edits application
files. The lead prepares bilingual KB candidates and coordinates verification,
review, publication of the feature branch, and the guarded KB review workflow.

One release registry drives the grouped exact-release exports, old underscore
aliases, and the release-aware stable selector. Stable templates import
`nixosModules.containerStable`; selection occurs when the guest evaluates its
nixpkgs, rather than when the image is built.

## Decisions

- Use the upstream default branch, `staging`, rather than the older `master`.
- Expose `nixosModules.containers."26.05"` and dynamic lookup by release string.
- Both modern `container` and `containerStable` select a registered stable
  release using the guest module-system `lib.trivial.release`. No containerAuto.
- Retain all eight underscore exports (22.11 through 26.05).
- Unknown releases fail during evaluation with actionable instructions. Unstable
  remains explicit through `containerUnstable`; do not guess from version suffix.
- Preserve legacy `nixosConfigurations` semantics and standalone compatibility
  files, including the root assertion file.
- Update six KB pages. Search found the conversion only in bilingual
  Impermanence; bilingual User Data has a related legacy module import.
- Initial metadata refusal is resolved: the ordinary manifest is now schema 1,
  creation ready; architect assignments succeeded during planning.

## Compatibility and deployment

The intentional semantic change is confined to modern generic stable imports:
they previously used the latest stable file and will select the guest's release.
Old/future/custom unregistered releases will fail rather than receive a fallback.
Explicit versioned imports and legacy configuration exports retain their targets.

No persisted-state, database/schema/seed, API/client/CLI/Terraform, daemon
protocol, host or node change is needed. No coordinated all-machine update is
required. Guest configuration settings are unchanged within each selected
release module; system.stateVersion and persistence configuration stay intact.

Adoption is per guest through its input update/rebuild. Existing configuration
files are written only when absent and are not rewritten. Public KB examples
must wait for availability of the new exports in the public default source.
Rollback below the new interface reverts imports and vpsadminos pin together;
existing NixOS generations remain available. This work does not authorize
integration into staging or production KB publication; these have explicit
approval gates. No production guest or host deployment is planned.

## Documentation

Owning-project guest documentation explains automatic, exact-release and
unstable imports, supported registry keys, errors, legacy exports, and the
standalone-file path. Link it from the docs index. KB prose is maintained by the
lead with the user-facing writing skill; preserve page IDs, language mappings,
code semantics and unrelated content. Prepare six complete candidates and
localized summaries in one bilingual review bundle. Session records own branch
and rollout evidence, review packet, verification results and approval status.

## Testing plan

Quick checks: all release keys/aliases, pure selector matrix and actionable
unknown-release errors, real guest evaluations for 24.11/25.11/26.05, old
stateVersion and differing host-input/guest releases, release upgrade without
editing import, explicit unstable, four generated flakes/locks, standalone-file
evaluation, KB example syntax, documentation and declared hooks. Focused leaf
tests are required because flake checking does not descend into the grouped map.

Commit all intended source/documentation and candidate changes, inventory final
base-to-head history/diff and migration provenance (none), then assign reviewer0
the mandatory final review before long integration tests. Preserve narrow-fix
review policy. A fresh Luna/low watcher launches/monitors the four current
stable/unstable ordinary/impermanence image cases; verify rebuild, network/DNS,
restart, persistent data and stable UID/GID/machine-id for impermanence. Stop an
unexpected local kernel build under the verification procedure. No full host
suite is needed unless evidence justifies it.
