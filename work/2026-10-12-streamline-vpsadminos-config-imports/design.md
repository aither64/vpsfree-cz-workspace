# Release-aware NixOS guest compatibility imports

Accepted implementation brief, 2026-10-14. Design owner: `architect0`.
The user authorized implementation through the lead. This document records the
accepted decisions before application edits; verification below is planned
unless explicitly identified as completed investigation.

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

Application source was inspected at canonical `origin/staging` commit
`1150e37b1cc997b1728f2fda806a3433ef55b798`. Reconcile relevant upstream changes
when preparing the implementation worktree. No configuration-repository or
`vpsfree-kb-contracts` feature change is expected.

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

Use a small test-only fixture definition with pinned nixpkgs revisions for
historical real-release evaluations. Do not update production inputs or introduce
unrelated lockfile churn to obtain fixtures. Record fixture provenance and
separate source-fetch failures from evaluation failures.

Keep unstable templates explicitly on `containerUnstable`. Preserve stable and
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

These pages are unmanaged by `vpsfree-kb-contracts/contract/pages.yml`. Do not add
contract-repository changes or screenshot scope. Preserve real page IDs,
translation tags and DokuWiki syntax; examples in both languages must retain
equivalent machine-significant content. The lead applies
`vpsfree-user-facing-writing` and prepares localized revision summaries, staging
and verification through the guarded KB workflow. The owning-project
documentation remains the durable public API reference.

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
Terraform, daemon protocol or on-disk format change. The change affects Nix
evaluation and generated guest configuration only. It requires no coordinated
update of hosts, all running machines or all nodes; guests adopt independently
when their configuration is rebuilt. Existing generated files are copied only
when absent, so this does not rewrite existing guest configurations.

New grouped imports require a vpsadminos revision containing the new interface.
An old vpsadminos pin still accepts `containerStable` but retains its old
latest-stable semantics; using that spelling alone does not prove automatic
selection is active. Publish the implementation before member-facing guidance
claims that behavior. Generated locks must reference a revision that contains
the advertised exports and selector. Implementation authorization does not
authorize default-branch integration or production KB publication; the lead
handles their separate required approvals.

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
7. Compare legacy generic exports against the original raw latest-stable module
   using the same compatible fixture. Compare legacy explicit unstable against
   the original raw unstable module. Do not expect legacy latest stable to equal
   automatic selection on an older release.
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

An isolated output-shape check may complement the module tests. Any full flake
check should distinguish the known legacy `nixosConfigurations` convention issue
from a regression. No unrelated output-schema cleanup is required.

## Longer verification and review ordering

After the intended substantive deliverable is committed and quick checks pass,
the lead runs mandatory independent final review, including the complete branch
history and an explicit no-migrations conclusion. Routine design planning does
not itself trigger that review. Long integration tests follow final review.

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
evidence. Implementation, committed-deliverable review and the acceptance
checks above remain to be completed and recorded by the lead.
