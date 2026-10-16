# Release-aware NixOS guest compatibility imports

Accepted implementation brief, revised 2026-10-15. Design owner: `architect0`.
The user authorized implementation through the lead. This document records the
accepted decisions before application edits; verification below is planned
unless explicitly identified as completed evidence.

## Scope and ownership

Streamline the NixOS guest compatibility interface in `vpsadminos`, including
generated guest flakes and documentation. Stable guests should retain the same
import while changing their nixpkgs release. Explicit release imports must use
literal NixOS release strings without transforming dots into underscores.

The architect owns this brief and consequential design revisions. The
implementer owns application changes assigned by the lead. The lead owns
plan/state, the initial tracking commit, worktree and branch orchestration,
bilingual KB candidates, verification coordination, review and publication.
Refer material deviations to the lead before implementing them.

The original import design used canonical `origin/staging` commit
`1150e37b1cc997b1728f2fda806a3433ef55b798`. The current persistence revision uses
the exact reviewed source and evidence recorded below. No configuration-repository change
is expected. Final review expanded the scope to a narrow
`vpsfree-kb-contracts` companion change: bind both Impermanence pages to the
existing `datasets.create.open` path and reconcile the required annotation
metadata. The lead owns the paired KB markup and refreshed release manifests;
`implementer0` owns the contract bindings and minimal related metadata. This
revision does not change the guest-module architecture or technical APIs.

The user subsequently approved correcting the impermanence defect exposed by
runtime CI and required establishing its root cause. The bounded correction
below supersedes the original prohibition on raw compatibility changes for
this defect only. It is a separate logical baseline-fix commit. It does not
change the import interface, guest pins, stateVersion or KB scope. The lead
accepted the compatibility-preserving callback revision below, superseding
mechanism B and its non-root backing requirement. The user authorized this
revision and normal test organization. After the independent whole-approach
review, the user authorized the effective-mount selection and verification
revision below. This is the current persistence design. The lead retains
implementation assignment and the separate instruction rollback/history work;
checks remain planned unless explicitly recorded as completed.

## Public interface

`containerStable` is the canonical spelling in generated stable templates and
KB examples. `container` remains an equivalent selector alias.

| Export | Accepted behavior |
| --- | --- |
| `nixosModules.containers."26.05"` | Exact versioned stable compatibility module |
| `nixosModules.containers.${nixpkgs.lib.trivial.release}` | Explicit lookup using the guest nixpkgs input |
| `nixosModules.containerStable` | Select a known stable module using the guest module-system `lib.trivial.release` |
| `nixosModules.container` | The same selector as `containerStable` |
| `nixosModules.container_26_05` and other existing underscore exports | Retained exact version aliases |
| `nixosModules.containerUnstable` | Existing explicit unstable module |
| `nixosConfigurations.container` and `containerStable` | Existing latest-stable module, independent of guest release |
| `nixosConfigurations.containerUnstable` | Existing explicit unstable module |

The grouped release map contains exactly these existing releases initially:

| Release key | Retained alias | Existing stable module filename |
| --- | --- | --- |
| `22.11` | `container_22_11` | `vpsadminos-22.11.nix` |
| `23.05` | `container_23_05` | `vpsadminos-23.05.nix` |
| `23.11` | `container_23_11` | `vpsadminos-23.11.nix` |
| `24.05` | `container_24_05` | `vpsadminos-24.05.nix` |
| `24.11` | `container_24_11` | `vpsadminos-24.11.nix` |
| `25.05` | `container_25_05` | `vpsadminos-25.05.nix` |
| `25.11` | `container_25_11` | `vpsadminos-25.11.nix` |
| `26.05` | `container_26_05` | `vpsadminos-26.05.nix` |

Retained release exports do not imply current upstream security support for
those releases. Do not add `containerAuto`, flat release exports or an automatic
fallback to unstable.

## Release map and selection invariants

Maintain one explicit internal release map to the existing versioned files.
Expose that map as `nixosModules.containers` and derive every underscore version
alias from it. The error's supported-release list also comes from the map.
Do not independently maintain three lists of releases, aliases and error text.

Both modern generic aliases reference one module selector with this shape:

```nix
{ lib, ... }:
{
  imports = [
    (releaseModules.${lib.trivial.release} or (throw unsupportedReleaseMessage))
  ];
}
```

The error must identify the unsupported release, list the known stable releases,
and advise updating the vpsadminos input or explicitly selecting
`containerUnstable` when using unstable. Failure occurs during evaluation before
building or activation. Direct lookup of a missing grouped key may retain Nix's
ordinary missing-attribute error; the actionable error is the selector contract.

Use the `lib` supplied by the guest's module evaluator. Do not choose from
vpsadminos's captured nixpkgs library, `pkgs.lib`, `config.system.nixos.release`,
`config.system.stateVersion` or another `_module.args` value. Imports are
collected before configuration options can be evaluated. The built-in `lib`
argument is available at that stage; option-dependent imports can recurse.
`system.stateVersion` controls persisted-behavior compatibility and is not the
current guest software release. No new module option or special argument is
needed.

Do not infer unstable from `lib.trivial.version` containing `pre`. The inspected
stable flake input at `7993f34ee47e28a3d607a525aadc6c94b73be728` reports
`release = "26.05"` and `version = "26.05pre-git"`: nixpkgs uses `pre-git`
when the source lacks `.version-suffix`. Stable-only selection means that the
selector returns only a versioned stable module. It does not prove branch
provenance: an unstable snapshot reporting a known release number will also
select that stable module. Unstable users must explicitly import
`containerUnstable`.

Preserve the original latest-stable binding for the two legacy
`nixosConfigurations` aliases: it imports `stable/vpsadminos.nix`. This is an
intentional distinction from the release map, not a second version table. Do not
derive legacy latest stable from a caller's release or an overrideable flake
input. The unstable binding remains independent as well.

## Grouped-map convention and validation

The grouped map is a documented extension to the usual convention that each
`nixosModules.<name>` is one importable module. Each release leaf is a module;
`nixosModules.containers` itself is a lookup map and must not be imported.
Generic consumers that import every value of `nixosModules` cannot assume this
new member is a module. Do not introduce `__functor` or another callable wrapper
to disguise the map.

In [Nix 2.34.8's checker](https://github.com/NixOS/nix/blob/2.34.8/src/nix/flake.cc#L449),
the module check only forces each top-level value; its
[output traversal](https://github.com/NixOS/nix/blob/2.34.8/src/nix/flake.cc#L661)
does not validate nested release leaves. A successful flake check therefore
cannot replace focused leaf/module evaluations. The pre-existing
`nixosConfigurations` exports are module functions rather than evaluated system
configurations; a full flake check can fail on that independent convention
mismatch. Record the baseline instead of changing legacy exports to make the
whole check pass.

## Files and implementation boundaries

| File or area | Intended change |
| --- | --- |
| `vpsadminos/flake.nix` | Central map, grouped export, derived underscore aliases and shared stable selector; preserve legacy latest-stable and explicit unstable bindings |
| `os/lib/nixos-container/stable/minimal.nix` | Generate `vpsadminos.nixosModules.containerStable` instead of a baked underscore release name |
| `os/lib/nixos-container/stable/impermanence.nix` | Use the same canonical stable import |
| `os/lib/nixos-container/template-flake.nix` | Change only if necessary; its existing module-name renderer already accepts `containerStable` |
| `tests/nixos-container-modules-eval.nix` or a focused equivalent | Export, selector, release-compatibility and template checks |
| Existing standalone/template test helpers and CI | Wire focused evaluation into CI and cover the relevant generated configurations |
| Project guest documentation, linked from `mkdocs.yml` | Public import contract, selection and failure behavior, standalone route and legacy distinction |
| The four raw compatibility files named below, bounded activation tests and `docs/containers/nixos.md` | Separate baseline correction for allocation-state visibility, declared backing checks and recovery limits; preserve root-backed layouts |
| `vpsfree-kb-contracts/contract/navigation.yml` | Add the Czech and English Impermanence page bindings to the existing `datasets.create.open` path |
| `vpsfree-kb-contracts/contract/kb-annotations.yml` | Record two creation tags per Impermanence language and one English Features tag, replacing its obsolete exception |
| `vpsfree-kb-contracts/contract/kb-navigation-inventory.yml` | Reconcile affected Impermanence discoveries for creation instructions in steps 3 and 5 and English Features |

Use a small test-only fixture definition with pinned nixpkgs revisions for
historical real-release evaluations. Do not update production inputs or introduce
unrelated lockfile churn to obtain fixtures. Record fixture provenance and
separate source-fetch failures from evaluation failures.

Keep unstable templates explicitly on `containerUnstable`. Except for the
approved allocation-state visibility correction below, preserve stable and
unstable base-module behavior, compatibility option settings, persistence
configuration, stateVersion, and the generated lockfile structure. Stable image
generation may still use its known latest-stable module internally; the emitted
guest import must choose again when the guest evaluates a different release.

All existing versioned, stable and unstable raw compatibility files must remain
self-contained. Do not replace their contents with relative companion imports:
users can download only one file. Preserve the root
`os/lib/nixos-container/vpsadminos.nix` assertion unchanged. No daemon, host
configuration, image-release bump or downstream configuration migration is in
scope.

## Cause-driven impermanence correction

This is the current accepted design following the independent whole-approach
review and the user's instruction to implement the plan on 2026-10-15. It
retains guest-owned persistence, host-provided storage and the upstream global
mount sequence. It replaces the exact-systemd-target selection at
`20b803f349d68b1bb5619058ccc025e16baafd29` with selection from the effective early
mount set. It also replaces the incorrect promise that impermanence later
applies custom source metadata. Earlier mechanism B, its separate mount phase
and non-root storage requirement remain superseded. Healthy unprivileged
containers must not acquire a new storage policy or guest block device.

### Established cause and prior evidence

The original failure remains documented in
[impermanence-root-cause.md](impermanence-root-cause.md), with independent
[allocator and map evidence](implementer-ci-v2-causal-evidence/diagnosis.md).
These are causal and historical records; this section owns the current
implementation contract. Diagnostic source
`4a40154539bf6dc73d391c30326af255b4dc15b2`, image workflow `38562488356`, showed
fixture IDs changing from 995:993 to 996:996 on restart while the eventual
visible/backing maps retained 995:993. Payload bytes, numeric ownership and
machine-id survived. Users ran before specialfs; LXC's proc mount skipped the
earlier stage-2 mounts. The maps became visible after allocation used ephemeral
state. Live switches saw already-mounted maps. The four raw modules were
unchanged from baseline `1150e37b` to the diagnostic revision.

The [eight-case runtime acceptance receipt](full-upgrade-acceptance/receipt.md)
records success at exact `20b803f349d68b1bb5619058ccc025e16baafd29`, tree
`5f1773c9811935622b1914adcd266000b42273df`. Its attempt record is
`runtime-attempt.e9j2hj27`, with retained state `/tmp/ni.im81pfm8`. All eight
registered cases, six image cases and RSpec passed for that head. This evidence
covers the represented exact state/log bind layouts, including healthy adoption,
root-backed sources, declared backing and failure cases. It does not cover the
ancestor/direct-filesystem selection gap or validate the unimplemented revision.

Pinned impermanence explicitly recognizes `/var/lib/nixos` ancestors and direct
filesystem declarations in
[its source](activation-pinned-source-excerpts/impermanence/nixos.nix), lines
598–606. Therefore `/var` or `/var/lib` alone can supply allocation state.
Selecting only exact `/var/lib/nixos` and `/var/log` entries from `systemd.mounts`
misses valid layouts and may omit both the dependency and checked callbacks.

### Files and implementation boundary

Apply the correction to these four self-contained files:

- `os/lib/nixos-container/stable/vpsadminos-25.11.nix`
- `os/lib/nixos-container/stable/vpsadminos-26.05.nix`
- `os/lib/nixos-container/stable/vpsadminos.nix`
- `os/lib/nixos-container/unstable/vpsadminos.nix`

Latest stable must remain byte-equal to versioned 26.05. Keep the root guard
assertion and retained 22.11–25.05 files unchanged. No companion imports,
selector/API change, guest input pin/stateVersion change, forced account
backend, allocation algorithm change, host change or UID/map/ownership repair.
This revision belongs to the independent baseline persistence correction,
separate from release selection. The lead owns history and instruction rollback
planning; the six instruction paths are not part of this design edit or product
behavior revision.

Use the existing focused tests and fixtures:
`tests/nixos-container-persistence-{eval.nix,shell.sh,check.nix}`,
`tests/fixtures/nixos-persistence-guests.nix`, and
`tests/suite/dist-config/nixos-persistence-upgrade.nix`. Update
`docs/containers/nixos.md` for the broader mount coverage, precise failure
boundary and metadata policy. Add only the inert mock field described below to
`tests/nixos-container-modules-eval.nix`. Preserve the existing pure flake check,
CI wiring, suite registration and lightweight selector/template/standalone/
unknown-release route. No new runner, framework or production input is needed.

### Effective selection and activation dependency

Keep the existing complete `boot.specialFileSystems` promotion unchanged.
Select from `builtins.attrValues config.boot.specialFileSystems` after module
merging; the pinned option's `apply` already removes disabled entries. For each
effective mount, select it when its `mountPoint` is not `/` and is a
component-aware ancestor of, or equal to, `/var/lib/nixos` or `/var/log`.
Ordinary selected paths are `/var`, `/var/lib`, `/var/lib/nixos` and `/var/log`.
`/variable`, `/var/lib/nixos-other` and `/var/log-old` do not match. Use the
effective `device`, `mountPoint`, `fsType`, `options` and `depends`; do not
retain an original systemd declaration when an effective override differs.
Direct `fileSystems` and `boot.specialFileSystems` declarations participate on
the same terms as already-promoted systemd binds.

Root `/` is not a selection seed: it is already active when activation starts
and must not enable this adapter in every ordinary container. Root-backed state
sources remain valid. Normal `/proc`, `/sys`, `/dev` and `/run` entries do not
seed selection because they do not cover a state path. Do not blacklist types:
an explicitly configured tmpfs at `/var` affects allocation visibility and
requires ordering/checking, without any claim that tmpfs is durable.

Only when legacy allocation is enabled (`!systemd.sysusers.enable` and
`!services.userborn.enable`) and this selected set is nonempty, define the whole
`system.activationScripts.specialfs` value with `lib.mkOverride 90`, structured
`text`, and `supportsDryActivation = false`. Add the native
`users.deps = [ "specialfs" ]` edge while preserving existing dependencies and
allocator text. Guard the whole contribution so alternative backends' empty
string users value receives no structured fields.

Source `config.system.build.earlyMountScript` exactly once in that snippet.
Its existing global `utils.fsBefore` order and cycle behavior stay authoritative.
The existing stage-2 path and proc guard remain untouched. Source preparation
happens inside the selected bind callback at its normal place in that sequence;
there is no second replay, mount phase or sorter. Do not promote a manual,
noauto or lazy declaration that is outside the effective early set.

No-relevant-mount and sysusers/userborn configurations retain upstream activation
behavior. Guest `mkForce specialfs` remains effective and owns its custom shell
semantics. The completed
[whole-value probe](specialfs-value-probe.json) on exact 25.11, 26.05 and unstable
established priority 90 composition, source-once, dependency order, dry omission
and guest-force precedence. Do not repeat rejected type/apply/string-composition
probes; test the finished behavior through normal checks.

### Required predecessor membership and checked dispatch

A dependency edge orders snippets but does not make a failed prerequisite stop
allocation: NixOS's ERR trap records failure and continues. Presence also cannot
prove that an earlier failed remount succeeded. Derive a finite required set
from the selected state mounts and their transitive predecessors under the
existing `utils.fsBefore` relation over the effective early entries.

Use a standard finite closure keyed by effective `mountPoint` (for example
`lib.genericClosure`), starting with selected mounts and adding each existing
entry `a` for which `utils.fsBefore a b` holds for a visited entry `b`. Deduplicate
by that key; cycles must terminate this membership calculation and remain an
upstream mount-order error. This set answers only which existing callbacks must
fail closed. It must not order, schedule, replay or introduce any mount. It
covers source and destination ancestry and explicit `depends`, including a
backing bind whose own source resides on another early mount.

Dispatch from the effective entry and its configured tuple, not original
`what`/`where` plus `fsType == "none"`. Identify directory binds from `bind` or
`rbind` option tokens, retaining the configured tokens and all other options.
Handle callbacks as follows:

| Entry | Required behavior |
| --- | --- |
| Selected directory bind | Validate required backing availability; prepare only missing source/target directories; validate live directory identity; check configured bind/remount and final mountpoint/identity |
| Selected non-bind filesystem | Never create or compare the device/UUID/network source as a directory; prepare only an absent target, preserve existing metadata, check configured mount/remount and final exact mountpoint |
| Required predecessor | Preserve its existing mount/remount type/options and position, but explicitly propagate failed preparation/mount/remount; do not create missing source directories; verify exact mountpoint and directory-bind identity where applicable |
| Unrelated early mount | Retain the ordinary upstream callback behavior |

Root and pseudo-filesystem entries may be required predecessors without becoming
selection seeds. Keep their native mount handling; do not add non-root or
durability checks. Checked directory targets retain existing owner/mode/content;
only missing targets receive normal defaults. No unrelated callback gains a
blanket failure policy. Document the small upstream callback's maintenance
responsibility near its copied shell body.

Every failed required callback or state prerequisite explicitly exits the parent
activation shell before legacy users. Propagate helper failures explicitly; do
not rely on `set -e` inside conditionally called functions. Dry activation does
no preparation or mount work. This guarantees no legacy allocation in the failed
activation, not that every stage-2 path or later service universally stops on a
nonzero activation status.

### Directory identity and storage limits

Before selected source creation, effective early mountpoints covering that
source must already be present as exact mountpoints. Use path components,
including `/`, rather than guessed first components. A declared covering
`bind`/`rbind` requires both source and target to resolve to directories and
`[ "$backingSource" -ef "$backingMountPoint" ]`. Do not create an absent
backing source. The same identity rule applies to checked directory-bind
prerequisites; it catches a different live bind surviving an ordinary remount.
A directory alias resolving to the same object is valid. Failure must precede
selected-source creation and allocation, even when a mountpoint already exists.

For a selected bind with an already-mounted destination, require source/target
identity before remounting. A mismatch is refused without stacking, replacing
or unmounting the live bind. For an unmounted target, create only missing
directories and perform the configured bind. Check the mount command, exact
mountpoint and directory identity afterward. Preserve quoted arguments and
configured source, destination, type and options. An ancestor bind needs only
its own source prepared; the real legacy allocator creates `/var/lib/nixos`
inside the mounted ancestor. Do not add a separate map-directory initializer.

For non-bind filesystems, check the actual mount/remount result and exact
mountpoint; do not apply directory `-ef` to a block device, UUID or network
source. This retains the upstream source-mount contract without promising
universal device identity validation. Directory identity likewise does not
prove recursive mount-tree equivalence or future durability.

The supplied `/persistent` is an osctld host dataset bind, not a guest block
device. Sources on persistent `/` or custom binds remain supported. Undeclared
host storage retains its prior availability contract: stale directories exposed
by an absent undeclared host bind can look identical to a valid root-backed
layout. Mount IDs, device IDs, directory existence and map presence cannot prove
intended durability. Do not add a storage policy, impermanence-schema probing or
heuristic to conceal that limit. Earlier unrelated callbacks may already have
run before a failure; no claim of an entirely inert failed activation is made.

### Fixed bootstrap metadata and directory helper

The user chose root/0755 defaults for absent selected bind sources and parents.
Preserve every existing source's owner, group, mode, content and identity.
Custom source owner **and mode** must be pre-provisioned; do not resolve
not-yet-created users, record newly created paths for later repair, or add a
metadata phase.

Pinned impermanence's
[create-directories.bash](activation-pinned-source-excerpts/impermanence/create-directories.bash),
lines 46–53, applies requested source ownership/mode only if the source is
absent. Lines 58–60 then copy existing source metadata to the target. It does
not later apply a configured 0710 mode to a source this adapter created as
0755. The retained fresh runtime observation is `0:0:755:384` in
`/tmp/ni.im81pfm8/os-test-dist-config__nixos-persistence-upgrade-8c45b496/machine-shell.log`
near line 5283. Update the product guide accordingly; the former later-metadata
promise is superseded.

Retain the current bounded recursive directory helper. It validates existing
paths/symlinks as directories and uses explicit `mkdir -m 0755` at each missing
level. A scoped `(umask 0022; mkdir -p -m 0755 -- "$path")` is not fully
equivalent: `-m` applies to the final operand, while missing parents can inherit
default ACL permissions. Do not silently change those parent semantics or add
creation tracking/chmod to justify a simplification. Existing helper directory,
symlink, lookup and creation error cases remain applicable.

### Adoption and rollback

Healthy guests adopt by changing only the vpsadminos input/module source and
activating with unchanged nixpkgs, stateVersion, accounts and storage layout.
Ancestor and direct-filesystem layouts gain the missing ordering and failure
checks. Previously concealed failures of required mounts deliberately stop
allocation. There is no host/node coordination, on-disk format change or data
conversion. Older generations can read the maps and payload, but rollback
restart can reintroduce the old ordering defect.

This is prevention, not recovery for already-drifted identities. Legacy
allocation prefers existing passwd/group IDs and may overwrite a surviving map
on a later switch. Preserve and compare damaged accounts/maps/data before a
separately authorized recovery; do not imply that this correction repairs them.
No production deployment, integration or KB publication follows from this brief.

### Pure checks and selector mock

Keep `checks.x86_64-linux.nixos-container-persistence` as the normal pure
entrypoint, with explicit source, release fixtures, library/system and old
source arguments. Force every evaluation assertion and run command doubles
against generated callbacks/global fixture calls. No guest boot or real mount
belongs in the check. Keep shipping tests independent of session paths,
`builtins.getEnv`, `VPSADMINOS_PERSISTENCE_BASELINE`, `priorV2` and CWD flake lookup.

Reuse the immutable old source
`1150e37b1cc997b1728f2fda806a3433ef55b798`, NAR hash
`sha256-PdZ1g1KtuxL/3T1E01jKhj3Npmkd4G8EJIzS0OSiaMA=`, already recorded in the
repository fixture and [fetch receipt](persistence-upgrade-baseline.json).
Do not refetch metadata, copy obsolete raw modules or add a production input.
Keep the actual pinned 25.11, 26.05 and unstable fixtures, and stateVersion 22.11.

On all three release fixtures, add impermanence-only `/var` and only `/var/lib`
cases, direct `fileSystems` bind/non-bind cases, effective-entry override and
disabled/near-prefix/root-only controls. Ancestor cases must have neither exact
`/var/lib/nixos` nor exact `/var/log` bind in the merged early set. Force
source-before-real-allocator, selected callback and required-membership behavior.
Cover bind/rbind classification, explicit dependencies, transitive predecessor
failures and unchanged unrelated callbacks. Keep source-once, global order/cycle,
standalone-copy, latest-file equality, mkForce and dry assertions.

Replace the existing direct-filesystem exact-baseline assertion with the
intended checked-before-users assertion and effective source/type/options
checks. Retain exact baseline equality for ordinary configurations with no
relevant mounts and for alternative backends. In
`tests/nixos-container-modules-eval.nix`, add only
`moduleArgs.config.boot.specialFileSystems = { }` to the inert mock. Effective-set
selection forces that field while raw leaves are serialized. Preserve existing
selector assertions, empty fileSystems/systemd.mounts and mock earlyMountScript.

Make the existing shell fixtures layout-aware: their rewritten paths, expected
mount calls and bind doubles currently assume two exact targets. Add distinct
non-bind doubles without inventing a generic mount simulator. Cover fresh and
existing sources, mode 0710 preservation, default 0755 parents, matching live
binds/no stacking, wrong ancestor/backing bind, mountpoint-present remount
failure, source/target lookup and mkdir failure, missing/transitive required
backing and explicit dependency failure. A non-bind case must never mkdir its
device string or run directory identity on it. A wrong backing case creates
no selected-source child. Keep the existing helper's injected dirname failure
as well as real file/dangling-link/creation failures. A shell allocator marker
proves local control flow only, not absence of real guest allocation.

### Layout-aware registered runtime suite

Extend the existing registered `dist-config/nixos-persistence-upgrade` suite,
using its make-test/tank host, cached closures, `testScripts` and RSpec structure.
Keep its `ci` tag and standard runner discovery. The acceptance matrix has
exactly twelve scripts: the existing eight plus three adoption layouts and one
fresh ancestor case. There is no new runner, framework or release/layout
cross-product.

| Script | Required path and result |
| --- | --- |
| `upgrade-25.11` | Existing supplied-hostbind healthy old-to-new adoption using actual 25.11 |
| `upgrade-26.05` | Existing supplied-hostbind healthy old-to-new adoption using actual 26.05 |
| `upgrade-unstable` | Existing explicit-unstable adoption using the pinned actual unstable release |
| `root-backed-26.05` | Existing persistent-root/custom source without another mount or block device |
| `declared-backing-26.05` | Existing declared backing bind before source preparation |
| `dependent-mount-26.05` | Existing selected state bind followed by dependent `/usr` in global order |
| `storage-failures-26.05` | Existing faults plus real ancestor, non-bind and required-remount controls below |
| `fresh-26.05` | Existing empty exact source; explicit initial root:root:0755 and preserved later identities |
| `ancestor-var-26.05` | Only `/var` supplies state/log coverage; no exact state/log bind; healthy adoption and restart |
| `ancestor-var-lib-26.05` | Only `/var/lib` supplies allocation state; no exact state/log bind; healthy adoption and restart |
| `direct-filesystem-bind-26.05` | Direct `fileSystems` state bind with no systemd exact state/log declarations; healthy adoption and restart |
| `fresh-ancestor-26.05` | Candidate first boot with absent `/var/lib` ancestor source and no exact state/log bind; first allocation writes through the ancestor |

For each adoption case, boot the old module, establish healthy maps through its
normal live switch, create an owned payload, then add an earlier-sorting account
through an old-module switch. Capture both accounts' actual IDs and saved maps.
Change only the compatibility source at the adoption boundary; switch candidate,
repeat its live switch, restart and compare independently. Keep guest inputs,
stateVersion 22.11, account definitions and storage unchanged at that boundary.
Do not manufacture the known-failing old restart, seed IDs, rewrite maps or
chown old data to manufacture a pass. Existing fixture creation of a new owned
payload is distinct from data repair. Fresh cases start under the candidate,
then perform the same account-insertion/live-switch/restart challenge.

`tests/fixtures/nixos-persistence-guests.nix` must provide explicit layout data:
mounted source/target pairs, allocation-state backing path and expected source
metadata. Ancestor fixtures replace the exact state/log entries rather than
adding an ancestor alongside them. Independent payload and machine-id
persistence can remain. Pre-provision custom 0710 source directories before old
initialization where required, while no accounts/maps/data exist.

The suite's current snapshot hard-codes `/var/lib/nixos` and `/var/log` as exact
mountpoints for count, options and identity. Replace those checks with declared
layout pairs. Still compare live `/var/lib/nixos` maps and directory identity
with the actual allocation-state backing path. For an ancestor layout, check
the ancestor mount identity/options and exactly one mount and assert zero exact state/log
mountpoints; do not substitute mere `findmnt -T` presence. Check log storage only
where declared. Preserve machine-id, both accounts' UID/GID and map entries,
payload bytes and numeric owner, source inode and metadata, matching live mount
and no-stacking assertions. Do not require unrelated map entries to remain
unchanged if upstream legitimately adds accounts.

Assert values as well as snapshot equality: fresh prepared sources are
root:root:0755 despite a configured 0710 request; pre-existing custom sources
retain 0710 and their owner/group/inode; the separately provisioned payload
directory retains 0750 and its expected account ownership. Add its mode to the
snapshot rather than inferring it from payload file ownership. Apply matching
metadata checks to the fresh ancestor source. No repair or deferred metadata
tracking is permitted.

Add these bounded controls within the existing storage-failures script/private
mount-namespace mechanism, without extra suite scripts:

- Ancestor bind failure and conflicting ancestor mount, with no exact state/log
  declarations, must stop before real user allocation.
- Direct non-bind mount/remount failure must stop before real allocation. Add a
  positive direct non-bind activation control, such as tmpfs at `/var/log`,
  proving the real mount precedes real Perl allocation while healthy allocation
  state remains outside that temporary log mount. This is visibility/order
  coverage, not a claim that tmpfs survives restart.
- A required backing remount failure must stop allocation even if its exact
  mountpoint remains present. Include declared/transitive dependency coverage
  in pure/shell tests so ordinary unrelated mounts are not made fatal.

Run complete generated activation in the disposable fixture, using a live,
complete bounded shell trace and a positive real allocator control. Negative
traces must show the actual failed operation, explicit exit 1 and no executed
Perl `update-users-groups.pl`. Retain the original allocator. Compare
passwd/group, saved maps and payload snapshots independently and check that
wrong backing receives no new source children. A missing allocator line alone
or a shell-only marker is insufficient evidence. Keep synthetic credentials
and retain diagnostics in the runner's owned attempt.

The nominal image called 25.11 still uses the shared stable builder and is not
historical guest evidence. The three existing core adoption scripts plus the
three-release pure matrix supply that coverage. Reuse immutable closures and
unique containers per script; all twelve share the existing host fixture under
normal runner semantics. Actual execution remains after committed final review
and quick checks, through the lead's watcher.

### Commands, discovery and verification order

From the vpsadminos repository, planned quick/local checks are:

```sh
nix build .#checks.x86_64-linux.nixos-container-persistence --no-link
nix develop --command bash tests/nixos-container-eval.sh
nix develop --command overcommit --run
./test-runner.sh ls 'dist-config/nixos-persistence-upgrade*'
```

The check is already discoverable in normal flake `checks` and built by
the existing CI build job beside the lightweight evaluator. Full `nix flake check`
is not the acceptance command because the unrelated legacy
`nixosConfigurations` convention remains. The registered suite and `ci` tag
make upgrade variants part of normal native CI; the workflow already accepts
`test_suite=ci` and a `test_pattern` for targeted dispatch. No new workflow or
imported action is required. Discovery must show all twelve variants, not
only the outer suite name.

After all intended changes are committed, quick checks pass and independent
final review accepts the revised whole branch, run through the lead's fresh
verification watcher. Prepare a unique short state root for each attempt;
do not put it under the absolute worktree path. Attempt 2 failed before boot
with a 173-byte Unix socket path against a 108-byte limit. The runner still
uses `<state-dir>/socks`, and osvm's hashed socket basename does not shorten
that prefix. The prior attempt using `/tmp/ni.4HJNv7`, recorded in
`image-state-dir` and `image-state-ownership.json`, establishes the short-path
route; retain that existing attempt and allocate a new directory for a new run.

The following is planned parent preparation, not an executed command. From the
owned vpsadminos worktree, after verifying the exact reviewed source is clean:

```sh
persistence_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
persistence_attempt=$(mktemp -d "$persistence_record/runtime-attempt.XXXXXX") || exit 1
persistence_state_dir=$(mktemp -d /tmp/ni.XXXXXX) || exit 1
printf '%s\n' "$persistence_state_dir" > "$persistence_attempt/state-dir"
{
  printf 'session=%s\n' '2026-10-12-streamline-vpsadminos-config-imports'
  printf 'workspace=%s\n' '/home/aither/workspace/ai/vpsfree.cz'
  printf 'uid=%s\n' "$(id -u)"
  printf 'source=%s\n' "$PWD"
  printf 'head=%s\n' "$(git rev-parse HEAD)"
  printf 'tree=%s\n' "$(git rev-parse 'HEAD^{tree}')"
  printf 'state_dir=%s\n' "$persistence_state_dir"
} > "$persistence_attempt/ownership"
```

The parent records the chosen pattern and exact invocation with this receipt,
then prepares and freezes `host-metadata.nix` inside that attempt record for the
actual tested source. Supply its full real revision, honest version suffix and
`revisionDirty = false` only after the clean-source proof. Do not reuse the
older image metadata's revision for a new source. The existing
`image-test-config.nix` contains only `{ }`; use that public `--test-config`
route so `VPSADMINOS_CONFIG` reaches the host test configuration, including
template instances. This changes host identification only, not guest inputs or
test behavior.

For each chosen pattern, the prepared watcher command is:

```sh
persistence_pattern='dist-config/nixos-persistence-upgrade#*'
VPSADMINOS_CONFIG="$persistence_attempt/host-metadata.nix" \
  ./test-runner.sh test --state-dir "$persistence_state_dir" \
  --test-config "$persistence_record/image-test-config.nix" \
  --no-destructive --jobs 1 "$persistence_pattern"
```

Use the full upgrade pattern above and the two final image patterns
`image-scripts/test@nixos-26.05-impermanence` and
`image-scripts/test@nixos-unstable-impermanence` as their authorized attempts.
`dist-config/nixos-persistence-upgrade#upgrade-26.05` remains a focused
development/retry alternative, not an extra run after a successful full suite.
Allocate and record a fresh short state root for each new attempt. A deliberately
grouped sequential image attempt may share its recorded root, as the earlier
image script did; retries must preserve earlier results. The parent retains
ownership, cancellation handles, exact-source provenance and watcher receipts.
Retain the short state directory and logs per attempt; `--no-destructive` keeps
managed disks as evidence. Do not reuse a shared default, overwrite
`image-state-dir`, install a cleanup trap or authorize cleanup/lifecycle work
through these examples. No duplicate runtime is needed merely to confirm path
length or host metadata forwarding.

Reuse existing cached host/guest closures. Keep long tests out of the pure
flake check. Reuse the six passing image results as prior evidence; run the final
changed impermanence paths and any ordinary smoke checks justified by generated
script differences. Stop unexpected local kernel builds under the normal
verification policy. No Nix, runtime, source edits or verification launches are
performed by the architect while recording this brief.

## Documentation and KB work owned by the lead

Prepare both languages of Impermanence and User Data, plus brief main NixOS page
guidance: six full-page KB candidates in one bilingual guarded release bundle.
The confirmed public-text inventory found `replaceStrings` only in the two
Impermanence pages. Both User Data pages use `nixosConfigurations.container` with
nixpkgs 24.11. Replace these examples with `nixosModules.containerStable` while
preserving their nixpkgs release, stateVersion and unrelated configuration.

Main guidance introduces `containerStable`, grouped literal/dynamic release
lookup, and explicit `containerUnstable`. Explain that existing stable imports
can stay unchanged across supported nixpkgs upgrades, while unknown releases
require an updated compatibility map. Do not imply that normal NixOS upgrades
should change stateVersion.

These pages remain unmanaged by `vpsfree-kb-contracts/contract/pages.yml`.
Preserve real page IDs, translation tags and DokuWiki syntax; examples in both
languages must retain equivalent machine-significant content. The lead applies
`vpsfree-user-facing-writing` and prepares localized revision summaries, staging
and verification through the guarded KB workflow. The owning-project
documentation remains the durable public API reference.

Final review found a Blocking baseline annotation issue in both Impermanence
pages. Each language needs two paired `<vpsadmin-nav>` creation tags: one around
the step-3 instruction to create the `nix` subdataset in VPS details, and one
around the step-5 instruction offering creation of another persistent-storage
subdataset. Use `id="datasets.create.open"`, preserving visible wording and
keeping unrelated explanation outside each semantic span. Extend that existing
navigation path's page lists only with:

- Czech: `navody:distribuce:nixos:impermanence`.
- English: `manuals:distributions:nixos:impermanence`.

The contract checker requires every path/page pair to have a binding or truthful
exception. Record `count: 2` for `datasets.create.open` on each Impermanence
page in `contract/kb-annotations.yml`. The English Features instruction also
requires one `vps.features.open` tag and a `count: 1` binding replacing its
obsolete annotation exception; its navigation page binding already exists.
For the final candidate corpus, replace the two step-3 discovery exceptions in
`contract/kb-navigation-inventory.yml` with `paths: [datasets.create.open]`, add
the creation path to each step-5 discovery while preserving its existing mount
path, and classify the English Features discovery with `vps.features.open`.
Reconcile text, paragraph index and derived discovery ID only where the accepted
candidate changes require it; preserve the complete page-ID inventory and
unrelated classifications. At inspected contract base
`ce2c8cd9358c3636e5d39343e595df813a0b197f`, these step-3 discoveries were
`ff6424ee5947162c` (Czech) and `99e0a207d925d665` (English). Candidate-derived
identity is authoritative if the final text or paragraph position differs.

This companion change adds no controls, navigation paths, WebUI behavior,
screenshots, managed-page sources, runtime fixtures or `contract/pages.yml`
entries. Do not change vpsAdmin, its pinned revision, source fingerprints,
capture provenance or unrelated annotations to accommodate it. The existing
navigation contract already defines the control and path; only page coverage
and its bounded reconciliation metadata change.

## Compatibility, rollout and recovery

This intentionally changes modern `nixosModules.container` and `containerStable`
from latest-stable imports into release-aware selectors. Older known guests can
receive different, release-appropriate compatibility settings. Unknown old,
future or custom releases now fail early, including configurations that formerly
worked accidentally with latest stable. Explicit version aliases and legacy
`nixosConfigurations` aliases retain their prior behavior.

The canonical configuration repositories currently consume the legacy exports:
`vpsfree-cz-configuration/profiles/ct.nix` uses `nixosConfigurations.container`;
`vpsadminos-org-configuration/profiles/ct.nix` uses `containerStable` under the
same legacy namespace. No downstream change is needed. Preserve these targets
even though the corresponding modern generic names now mean something else.

There is no database schema, migration, seed, API, generated client, CLI,
Terraform, daemon protocol or on-disk format change. The import change affects
Nix evaluation and generated guest configuration; the separately scoped baseline
fix changes guest activation as described above. The companion change
records coverage of an existing documented WebUI action. They require no
coordinated update of hosts, all running machines or all nodes; guests adopt
independently when their configuration is rebuilt. Existing generated files
are copied only when absent, so this does not rewrite existing guest
configurations.

New grouped imports require a vpsadminos revision containing the new interface.
An old vpsadminos pin still accepts `containerStable` but retains its old
latest-stable semantics; using that spelling alone does not prove automatic
selection is active. Publish the implementation before member-facing guidance
claims that behavior. Generated locks must reference a revision that contains
the advertised exports and selector. Implementation authorization does not
authorize default-branch integration or production KB publication; the lead
handles their separate required approvals.

Refresh the six-page candidate indexes, checksums, localized revision summaries
and per-language release manifests after reconciling these annotations. Retain the
immutable fetched production source revisions and contents as the concurrency
baseline. Record the exact reviewed contract revision with candidate-validation
evidence. Publish the companion branch through the ordinary explicit integration
gate; do not infer merge approval from resolving the review finding.

Adding navigation bindings does not make these pages managed or require new
managed-page/test provenance. Existing `datasets.create.open` rendering is
reused, so no plugin/configuration deployment is introduced by this design.
Verify its rendering in both staged pages and preserve the source-revision
guards. Use the installed schema-5 release workflow required by workspace
instructions even though the inspected contract workflow's examples still
mention schema 4. Production promotion requires approval of the refreshed exact
staged manifests; any previously reviewed candidate digests are superseded.

Migrate imports with the guest nixpkgs pin and stateVersion unchanged, then
compare evaluation before activation. Reverting vpsadminos below the new API
also requires reverting any grouped imports. To recover former latest-stable
behavior for a modern generic import, restore the previous vpsadminos pin or
choose an appropriate existing explicit module. Retain prior NixOS generations.
No new persisted state is introduced by this import change, so rollback needs
no data conversion. A separate guest NixOS upgrade retains its ordinary
release-specific rollback constraints and is not performed by this initiative.

## Acceptance criteria and quick checks

Run known quick evaluations in the repository's declared Nix environment after
implementation. These are substantive behavior tests, not textual mirrors of
the alias definitions. If a check's duration becomes long or uncertain, use the
prescribed watcher rather than treating it as an inline quick check.

1. Inventory all eight exact grouped keys and all eight underscore exports.
   Every old/new explicit pair selects equivalent module behavior. Both generic
   modern names use the same stable selector; no `containerAuto` is introduced.
2. Exercise every known release through a small selector matrix, plus unknown
   old/future/malformed values. Unsupported values produce the actionable
   message. A stable `26.05pre-git` version never triggers unstable selection.
3. Perform actual NixOS evaluation with pinned real 24.11, 25.11 and 26.05
   nixpkgs. Within each release, compare grouped leaf, underscore alias,
   `containerStable` and `container` configurations and, where practical,
   toplevel derivation paths. Force enough configuration to catch incompatible
   options, including the release-dependent resolved settings. Do not claim
   historical compatibility from evaluations against modern option declarations.
4. Keep vpsadminos's own input at 26.05 while evaluating a 24.11 guest. It must
   choose 24.11. Exercise distinct caller and captured input libraries so a
   closure over the wrong nixpkgs cannot pass accidentally.
5. With an old `system.stateVersion` such as 22.11, select by the guest software
   release and leave stateVersion unchanged. Selection must remain independent
   of config options; no config-dependent import recursion is acceptable.
6. Reuse one unchanged `containerStable` import across real 24.11, 25.11 and
   26.05 evaluations. Change only the guest nixpkgs fixture, retain stateVersion,
   and compare each result with its matching explicit release module. This is
   the release-upgrade acceptance test; changing the import would invalidate it.
7. Compare legacy generic exports against the raw latest-stable module using
   the same compatible fixture, and legacy explicit unstable against the raw
   unstable module. After the separate baseline correction, use its corrected
   raw files as the reference: import-route equivalence remains required, while
   the intended early persistence behavior differs from baseline. Do not expect
   legacy latest stable to equal automatic selection on an older release.
8. Evaluate explicit unstable with its own pinned unstable nixpkgs. Preserve the
   copied-single-file standalone check, and cover stable/unstable with matching
   inputs rather than relying solely on the existing stable-only evaluation.
9. Parse/evaluate all four generated guest flakes and lock relationships:
   stable/unstable, each ordinary/impermanence. Stable emits `containerStable`;
   unstable emits `containerUnstable`. Confirm pinned revisions provide those
   exports. Exercise grouped quoted and interpolated leaf syntax separately.
10. Wire the focused release evaluator into CI. Nix's shallow module check is
    insufficient. Run formatting and declared hooks, project documentation
    checks, and validate the six KB candidates' examples and language parity.
11. Validate the contract companion in its pinned Nix environment: the two
    navigation page bindings, count-2 creation bindings in both languages,
    count-1 English Features binding, and affected discovery records must agree.
    Plan the scoped static annotation check and the full-corpus annotation check
    through `ruby tools/check-kb-annotations.rb`, respectively without candidate
    arguments and with the complete immutable `--source-index` plus final
    `--candidate-index`. A two-page subset cannot satisfy the complete-page
    identity contract. Also plan `ruby tools/test-kb-annotations.rb` and
    `ruby tools/check-contract.rb`. Retain the repository's mandatory static
    `bin/check` as a baseline check under its normal policy. Do not refresh
    unrelated fingerprints, media or annotations to turn a baseline failure
    green. The lead and implementer coordinate exact candidate paths and record
    scoped results separately from full-corpus and repository baseline results.
12. Manually verify both creation instructions, in steps 3 and 5, in each
    language: each needs its own well-formed, nonempty paired tag with the
    existing creation path. Verify the English Features instruction has one
    Features tag and that existing mount tags remain intact. Independent lexical
    discovery is not sufficient evidence of complete annotation. In staging,
    check these rendered paths, translation links and updated revision summaries.
    No capture regeneration or new runtime suite is required by these
    binding-only changes.

The lead reports the current full-corpus annotation count comparison differs
only on two pre-existing IP-address pages outside the six candidates:
`navody:vps:ip_adresy` and `manuals:vps:ip_addresses`, where
`networking.host-addresses.add` is expected once but occurs zero times. Record
that full-corpus failure separately from the scoped companion validation. Do not
edit those pages, reduce their expected counts, filter them out of the complete
inventory or broaden this initiative to hide the mismatch. This reported count
comparison is not a claim that later full-corpus validation stages have passed.

An isolated output-shape check may complement the module tests. Any full flake
check should distinguish the known legacy `nixosConfigurations` convention issue
from a regression. No unrelated output-schema cleanup is required.

## Longer verification and review ordering

After the intended substantive deliverable is committed and quick checks pass,
the lead runs mandatory independent final review, including the complete branch
history and an explicit no-migrations conclusion. Routine design planning does
not itself trigger that review. Long integration tests follow final review.

The earlier KB review report confirmed its then-current application source.
The declarative narrow fix for B1 and the message-only
validation paragraph for I1 may be verified by the lead without an independent
review rerun. Record the exact committed fixes and verification in the review
reconciliation before proceeding to long tests; keep the unrelated annotation
baseline failure distinct. This document assigns no new reviewer and starts no
verification run; the lead retains orchestration. That earlier finding
reconciliation does not accept the subsequently revised persistence code or
upgrade suite: those require the committed-deliverable review gate above.

Use a fresh policy-selected Luna/low verification watcher for authorized builds,
image tests and uncertain-duration waits. Run the four relevant VM image cases:

- `image-scripts/test@nixos-26.05`
- `image-scripts/test@nixos-26.05-impermanence`
- `image-scripts/test@nixos-unstable`
- `image-scripts/test@nixos-unstable-impermanence`

Verify generated locked guest flakes build, `nixos-rebuild switch` succeeds, and
boot, networking, DNS and restart still work. For impermanence, verify a known
persistent payload, UID/GID assignments and machine-id survive rebuild/restart.
Use current RSpec-style integration assertions for any new VM coverage. Stop and
investigate unexpected local kernel builds under the verification procedure.
No full host suite is required unless changed scope or failures justify it.

Changes under `os/lib/nixos-container` already select NixOS images in image CI;
flake-export-only changes do not trigger that image workflow. Ensure the four
targeted checks run regardless of path-filter behavior. An image named 25.11 is
not sufficient historical-module coverage: the inspected image builder selects
the shared stable flake package without changing its stable nixpkgs pin.

## Evidence and current limits

Read-only source tracing established the exports, template behavior, standalone
constraint and downstream legacy consumers. Small in-memory `evalModules`
experiments verified grouped leaf selection, use of a caller lib reporting
24.11 with an underlying 26.05 library, unchanged mock old stateVersion, and
unknown-release failure. Importing the grouped parent failed as expected;
config-dependent imports produced infinite recursion. The pinned stable input's
`26.05pre-git` metadata was evaluated directly.

These experiments establish the design mechanics only. They are not real
multi-release NixOS, template build, runtime, deployment or KB publication
evidence. Current implementation, committed-deliverable review and acceptance
results are recorded by the lead in `state.md`; the planning experiments do not
substitute for those results. The contract guidance and checker were inspected
read-only for this scope reconciliation; no contract checks were run by the
architect.
