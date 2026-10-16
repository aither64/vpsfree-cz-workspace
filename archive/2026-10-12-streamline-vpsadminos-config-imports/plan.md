# 2026-10-12-streamline-vpsadminos-config-imports

## Goal

NixOS VPS (containers) on vpsAdminOS need to import vpsadminos.nix from vpsAdminOS into their configuration, since it contains settings needed for our environment. Different NixOS releases have different options, sometimes incompatible, so the users must import the right version of that config for their system. I'd like you to check if it is streamlined as much as possible, e.g. I guess we could import configs based on the user's nixpkgs release version. Do we do it currently?

## Affected repositories

- `vpsadminos`: flake module exports, stable guest templates, focused evaluation
  tests/CI, and owning-project documentation.
- Czech and English KB pages: NixOS, Impermanence, and User Data. These six pages
  are unmanaged; no managed-page expansion is needed.
- `vpsfree-kb-contracts`: final review identified a baseline missing dataset-create
  annotation/binding in both Impermanence pages. Add existing-path page bindings,
  expected tag counts, and scoped discovery reconciliation for the candidates.
  No WebUI controls, screenshots, managed pages or production input changes.

## Approach

Implement the accepted refinement (user: "Implement the plan", 2026-10-15).
The independent Astra/xhigh whole-approach review supports retaining the guest
adapter but identified missing ancestor/direct-filesystem coverage. Architect0
records the revised design before implementer0 edits application code. The lead
restores the six instruction files, reconciles the guest guide and logical patch
versions/history, and coordinates final review and exact-head verification.

Retain the original accepted selector plan (2026-10-14). Architect0
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
- Required narrow final-review correction: annotate existing subdataset-create
  instructions in steps 3 and 5 with `datasets.create.open`, count two tags per
  language, and bind both pages; refresh affected
  inventory only. The main technical interface and guest behavior are unchanged.
- Runtime testing exposed an independent impermanence UID-after-restart failure
  on unchanged raw/unstable compatibility paths. Diagnostics are authorized;
  the user now authorizes fixing it in this initiative: "all right, fix it as
  part of our work. find the root cause however, let's not create workaround
  without understanding the issue". Establish the runtime map/mount/activation
  cause before selecting the correction. The prior proposal is a candidate,
  not a prescribed implementation. Architect0 updates the accepted design once
  the cause is established; implementer0 implements a separate logical baseline
  fix with focused regression, final review and runtime verification. Preserve
  dynamic allocation, original numeric ownership and all fixture assertions.
- Cause established by v2 runtime evidence: allocation precedes late exposure
  of intact persistent maps. The accepted revision uses the upstream globally ordered specialfs callback
  to prepare/check effective early mounts covering /var/lib/nixos or /var/log,
  with a native dependency before legacy users. Root is not an activation
  trigger. See design.md for binding, predecessor and filesystem semantics.

## Accepted whole-approach refinement

- Select from effective enabled boot.specialFileSystems after module merging;
  include /var, /var/lib and direct filesystem declarations with component-aware
  matching. Keep upstream global order and source its script once.
- Compute required predecessor membership using the existing utils.fsBefore
  relation. Fail closed for those callbacks without a second sorter, phase,
  replay or runtime failure journal. Unrelated callbacks retain their behavior.
- Check directory-bind identity and mount results; selected binds may prepare
  missing sources. Required predecessor binds do not create missing sources.
  Non-bind filesystems use native mount/remount plus status/mountpoint checks,
  without treating device names as directories or claiming device durability.
- The user explicitly chose root/0755 bootstrap defaults. Custom owner AND mode
  require pre-provisioning; impermanence does not later apply requested metadata
  to pre-created sources. Preserve existing metadata and the recursive helper,
  whose per-parent modes differ from mkdir-p under inherited default ACLs.
- Restore all initiative instruction amendments in product20b803f,
  workspaceabacb121 and extension9d2ae656. Retain exact backups, preserve unrelated
  work, remove instruction-only shipping owners and restore truthful logical
  patch versions/history. Keep selector and baseline persistence independent.
- Preserve the current eight runtime cases; add /var, /var/lib and direct-bind
  adoption plus fresh ancestor initialization. Ancestor fixtures omit exact
  state/log binds. Use layout-owned mount/backing expectations, explicit0755,
  pre-existing0710 and payload-directory0750 assertions. Add real nonbind and
  required-remount refusal controls with unchanged IDs/maps/data.
- Commit with declared hooks and pass normal quick checks, then obtain the same
  independent Astra review of final source/history before long runtime checks.
  Fresh Luna/low utilities own long verification. Prior20b evidence remains
  revision-scoped. Revised acceptance now covers all12scenarios via11proved
  unchanged-input passes and one corrected fresh declared run; see
  effective-mounts-acceptance.md. No merge/deploy/KB publication.

## Compatibility and deployment

The intentional semantic change is confined to modern generic stable imports:
they previously used the latest stable file and will select the guest's release.
Old/future/custom unregistered releases will fail rather than receive a fallback.
Explicit versioned imports and legacy configuration exports retain their targets.

No persisted-state, database/schema/seed, API/client/CLI/Terraform, daemon
protocol, host or node change is needed. No coordinated all-machine update is
required. The selector retains each release module's configuration behavior;
the independent correction changes activation timing in the four supported raw
files. system.stateVersion and map formats stay intact. Selected sources on
persistent root or separate storage remain supported; global mount ordering is
preserved. Declared early covering mounts are checked, while undeclared host
storage remains the host responsibility. Existing metadata is preserved. This prevents new identity drift without repairing affected guests;
an old-generation restart can reintroduce the ordering defect.

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

## Superseded compatibility and instruction revision

The user previously approved this follow-up plan with "Implement the plan".
Its instruction amendments and exact-target selection are superseded by the
2026-10-15 refinement above; its removal of invented backing restrictions and
separate mount phases remains applicable. Revise the
persistence fix to retain existing storage layouts and NixOS's complete mount
order. Non-root backing and split-topology restrictions are superseded. The
whole-value specialfs priority90 seam passed build-free evaluation on real
25.11/26.05/unstable, including dry behavior and guest mkForce precedence.
Architect0 records the implementation brief before implementer0 edits source.

Added affected repositories: workspace instructions (dedicated workspace
worktree) and vpsfree-dev-workspace's maintained review-skill source. Amend
commit policy to require finished behavior/rationale/compatibility without
revision labels, development diaries or temporary validation status. Preserve
true upstream provenance. Tighten review for normal test execution and
unnecessary compatibility restrictions. Rewrite the two current source owners'
messages; retain semantic separation and exact tested-head backups.

Expose focused persistence checks as normal flake checks with explicit inputs,
remove session-specific baseline environment hooks from shipping tests, and
register an RSpec old-to-new upgrade fixture in the ordinary suite. Validate
healthy old IDs/maps through input-only update/switch/restart, positive root
backing and old valid dependent layouts, missing declared backing/wrong live
mount refusal, source metadata and fresh preparation. No new storage policy,
block devices, account repair, persisted format, host coordination or new runner.

Prior29e268350 image workflow38582595251 passed all six cases; that evidence
covers corrected images, not migration from an existing old guest. Revised
product tests still need final committed review and exact-head runtime. Policy
source edits do not authorize package activation, integration or KB publication.
