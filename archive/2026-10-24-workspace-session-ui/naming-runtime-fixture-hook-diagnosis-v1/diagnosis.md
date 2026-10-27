# Naming fixture hook diagnosis — static only

The source indicates a fixture composition defect: hook clearing happens inside
an injected builder, while the retained extension appends its migration symlink
in an outer `overrideAttrs`. The empty-hook acceptance invariant remains required.
No inspector, runtime, extension, workspace, binding or earlier receipt changed.

## What actually failed

Outer67455 / v3 settled runner1 in8.942s. The flat `01-evaluate.json` records
Nix exit1 in7.011s; its flat stderr identifies original inspector line106:
`assert fixture.postInstall == "" && fixture.postFixup == "";`.
Function application now works. Stdout is empty. Final current and both final
file guards exited0; all three recorded owned groups were confirmed empty.
No derived JSON, availability gate, recursive inspection or builder ran.
Neither hook's complete value nor any current package/fixture output identity
has been observed. The conjunctive failure alone does not identify the operand;
in particular it does not prove that `postFixup` was forced.

## Ownership and ordering

1. The original selection context selects workspace0c's actual composed
   `packages.x86_64-linux.vpsfree-dev-workspace`, then passes that package into
   runtimec31's naming-test constructor with its separate root test nixpkgs.
2. Runtime `nix/workspace-portal.nix:270` calls `buildGoModule`. Its application
   `postInstall` starts at339 and installs resources/wrappers; its `postFixup`
   starts at490 and checks installed commands, catalogs and native version.
   Those application hooks belong to the actual application package.
3. Extension767 `flake.nix:94–164` calls runtime `lib.mkPackage`, then wraps the
   result in `overrideAttrs`. At158–164 it unconditionally appends an install
   command for `$out/libexec/vpsfree-dev-workspace-migrate`. That product
   extension behavior is not itself evidence of a production bug.
4. Workspace0c `flake.nix:54–66` applies an argument override adding the workspace
   update skill. It does not clear or introduce install/fixup hooks there.
5. Runtime `nix/tests/naming-runtime.nix:28–51` calls `package.override` with a
   replacement `buildGoModule`. The replacement clears `postInstall` and
   `postFixup` in the builder's input attributes, then overrides `goModules`.
   There is no final hook clear outside the composed `package.override` result.
6. Retained a5cc `lib/customisation.nix:162–191` explains argument re-entry and
   preservation of `overrideAttrs` across `override`: the outer attribute overlay
   is replayed around the re-called function. Its stdenv implementation applies
   an overlay to prior derivation attributes. Under that composition behavior,
   the extension append is applied after the inner fixture hook clear.

This ordering explains a nonempty fixture install hook and fits the observed
failure. It does not justify allowing an arbitrary nonempty hook: even the
extension symlink command targets a libexec directory that a test-binary-only
fixture is not required to create. No build ran, so that is a source-level risk,
not a reported build failure. The design explicitly requires only the test
binary and excludes application post-install activation/wrapper checks.

## Evidence limits

The inspected customisation/stdenv source is retained test-root nixpkgs a5cc;
the composed package originates under workspace-root nixpkgs d58. No d58 source
path was guessed, scanned or retrieved. The a5cc implementation supports the
ordering analysis but is not an independently inspected certificate of d58.
The extension source pointer lfmic comes from the retained selected-profile
input graph, with the same767/NAR lock in retained candidate metadata and the
accepted final binding. This task hashes those local records and source bytes;
it does not calculate a new source NAR or treat an old package derivation's
hooks as current fixture values. Exact source excerpts and hashes are in
`evidence.json`.

## Proposed next bounded step

`observe-hooks.nix` is a new, unexecuted diagnostic expression. It imports the
unchanged selection context, so source, lock, selected-head, provenance and
fixture-constructor prerequisites remain active. It returns only selection
identity plus package/fixture hook strings and derivation/output path strings,
including the hooks exposed in `drvAttrs`. It uses null for absent attributes
and never normalizes nonempty strings or changes package attributes.

`observation-proposal.json` retains actual v3's modern eval options and exact
binding, changing only `--file` and its applied function expression. Offline,
no substitution, empty builders, max-jobs0 and IFD=false are unchanged. This is
not a new execution runner or release. Parent/architect must accept the
observation and separately release a fresh bounded utility with the existing
finite group settlement and mandatory finalization guards before it can run.
Returned derivation paths would be observed metadata, not availability proof.
All original inspector assertions remain unchanged and must later pass in
full before build admission; the diagnostic output cannot replace that gate.

If observation confirms the indicated outer append, refer the fixture boundary
to architect/lead for a final composed-fixture hook-clear design. Keep builder
argument injection for test compilation and exact compiler/modules/pin/review
inputs. No such source fix, v4 packet, assertion relaxation or retry is prepared
or authorized here. Package/fixture values and output identities stay null.

All prior failures and packets remain frozen. All build, VM, native, provider,
real-account, deployment, integration and lifecycle gates remain held.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
