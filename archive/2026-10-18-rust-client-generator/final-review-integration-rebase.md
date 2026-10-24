# Final affected review: integration rebase and client provenance

No Blocking or Important findings. One Advisory documentation finding was
reported and resolved through the lead's accepted narrow correction. No
unresolved finding remains. Fresh verification of HaveAPI's changed Nix/Ruby
inputs still gates integration; this review does not claim those checks passed.

Reviewed on 2026-10-21 by retained independent `reviewer0`, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, model `gpt-6.1-sol`, effort `xhigh`,
saved access `read_only`. The live same-session roster confirms identity,
review purpose, ready state and settings. No override, fallback, source
authorship or subreviewer. `dev-session current` from the bound tracking
directory prints `2026-10-18-rust-client-generator`; both environment identity
variables are absent, consistent with the trusted workspace/thread binding.

Applied mandatory-change-review and all four lane references to the affected
HaveAPI baseline integration, and general/history/provenance assessment to the
mechanical client refresh. Risk remains High for the existing authentication
and cross-project protocol boundary. Read applicable workspace/repository
guidance, the complete [packet](review-packet-integration-rebase.md), its three
HaveAPI proof files, client provenance records, prior five review reports and
the refined fresh-verification plan. Prior source reviews remain preserved;
unchanged source was not audited again.

## Finding and disposition

**D2: Advisory, general lane — stale shared-toolchain claim.** At reviewed
client `56c4c9d78bc36ccedb5d4173832a61176d24c8d2`,
`docs/development.md:11` says its `fe13242281a...` Nix pin is shared with
HaveAPI's generation environment. Recorded HaveAPI `68cc80b...` now uses
`02c087f3fe6...`; the client intentionally retains its own generation pin.
The text could direct maintainers to assume toolchain equality that no longer
exists. No dependency bump or generator change is required.

The lead accepted the finding, changed only the two lines to state that the
client retains its own pin, and directly accepted that narrow remediation.
It is folded into the original package commit in final client
`945af6a97717a7a6373507bbc9592d5cd53727c2`. The final range-diff confirms that
bounded wording change. No additional source review or verification rerun was
performed merely to confirm the correction.

## HaveAPI baseline and lane conclusions

Reviewed old `526648131af45df68c25ac0042a52f22c7a81df5..9e4c29a0412a25256ce944641f60ba13e9f03c2b`
against final
`7835acafdda19779815a0f1ba905d78e0085456d..68cc80b012b7a6b9bcdf35c008c338cbc3f4c000`.
Final tree is `ba13c1b6183ba225af5ca12e023827e95aeba621`.
Independently reconstructed complete Git tree maps, actual range-diff and
stable patch IDs, rather than accepting the packet's booleans:

- The same 60 feature paths remain. All 56 non-overlap feature entries match
  the previously reviewed head, including modes and blobs.
- All non-overlap upstream entries are preserved: 183 extant files plus 24
  removed source paths remain exactly as upstream. No unexplained tree delta
  exists outside the upstream changed-path set.
- The complete `clients/rust` subtree is unchanged at
  `820fa957687faeae3e30e4c0725012955b5f98b6`. Server Ruby source, Ruby client
  library, generator/runtime and their locks retain their reviewed bytes.
- Runtime and integration stable patch IDs remain respectively
  `9e95bfe266bc0d720ee7c9435827738273db2be4` and
  `1f40718e4469c6d53d991c398b3659d47b163448`. The generator range-diff changes
  only upstream context and the component-shell list resolution.

General: inspected both upstream and final diffs for all four overlaps.
`Makefile` retains Python checks, JS lock/version handling and existing release
targets while adding the separate Rust checks/version substitutions.
`README.md` retains current Python/TypeScript descriptions and the Rust guide
link. The development list retains both Python and Rust shells. `flake.nix`
retains upstream Ruby 3.4, Python tooling and shell behavior while adding the
same reviewed Rust component shell. No conflict marker, lost upstream behavior
or changed Rust application contract was established.

Architecture/repetition: the Rust shell continues to use the existing
`rubyShell` owner. The rebase does not duplicate environment, protocol or
publication orchestration. The updated Ruby client test-support bundle
selection is upstream-owned and preserved; Rust's own locked parent/child
bundle activation remains unchanged.

Scope/proportionality: the sole manual resolution combines two real component
entries. No fallback, compatibility shim, new release mechanism or unrelated
feature edit was added. Already integrated upstream work remains baseline
history rather than being rewritten into this feature.

Risk/compatibility: runtime/authentication/wire bytes and generated public
interfaces are unchanged. No new credential exposure, retry behavior, state
transition or deployment ordering was introduced by the resolutions. The
material boundary is toolchain execution: HaveAPI now inherits nixpkgs
`02c087f3fe673c9e317f206a627cb6b910336dbe` and Ruby 3.4 rather than the old
pin/Ruby 3.3. This requires fresh scoped verification, despite source equality.

## Client provenance and retained input boundary

The original affected review inspected frozen client `56c4c9d...`, tree
`da0004a40271d5f91dce8c7ab8e2f1751e38af49`. Actual comparison from reviewed
`091bd70954d270f3e575a71a8a5a1884eed2eccd` changes exactly one provenance
line, rebinding HaveAPI `9e4c29a...` to `68cc80b...`. All 709 other tracked
files match, including all 687 Rust files under `src`, schema, manifest,
configuration, locks, tests, examples and workflows. The later D2 correction
adds only the two-line documentation replacement; final tree is
`c993cef64194e86bac41c073409d345846eecf8a` at `945af6a...`.

Independent committed-byte reconstruction confirms:

- Generator digest:
  `b2f1408d9a53eda4bdf33054f4293e5e1ae712d69c66863e6c0ee71902bcfc13`.
- Runtime digest:
  `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`.
- Schema digest:
  `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`.
- Ruby lock digest:
  `7ab15ed0bf0ded01fbb03f2f8e6b4ad73ef2806b1ee9199acea8a5269080b2f1`.

All 686 ownership-manifest file hashes and copied runtime bytes match actual
committed source. The retained baseline's 710 file hashes match its actual Git
objects. The client matrix and actual-client-test objects in the prior input
receipt still match the final client. HaveAPI's actual-vpsAdmin wrapper,
fixture and runtime objects also match that receipt; its old HaveAPI flake
objects do not, and are not claimed reusable.

The actual-server launcher explicitly enters the supplied vpsAdmin source's
own `.#api` shell and the client's own Nix shell. Its retained acceptance may
therefore remain scoped to those previously proven unchanged source/lock/Nix
inputs; it does not establish new HaveAPI Ruby 3.4 generic-server acceptance.
No whole-matrix reuse follows from tree equality or provenance rebinding.

## Complete final histories, migrations and repeated streams

Independently inspected complete commit lists/messages, final diff inventories
and actual range-diffs, including ancestry from registered initial HaveAPI
base `c14e7d3158b91c134c2817b489cd29772fc09f82`. That base remains an ancestor;
the 22 subsequent upstream commits are already baseline history. Exactly three
feature commits follow current target `7835acaf...`:

1. `77dd0418e8c90a189f1de24aaa186d544706ea59`: embedded runtime.
2. `03c765bda560ff0ced1e051de2367cc46e3b3de9`: generator, tooling and docs.
3. `68cc80b012b7a6b9bcdf35c008c338cbc3f4c000`: protocol acceptance fixtures.

The client retains Git's empty-tree neutral root
`b67a3ba5eef89b2bd6533050aa8769aaa0574114` and exactly four logical commits:

1. `3353620fcd796976563be444d8241f4d867b1398`: handwritten package/schema/tests,
   including final provenance and the D2 correction.
2. `38750a527961b817a8e51e8638abc4b8305b5a54`: generated source/runtime.
3. `f5f28cbb4e4db51b21e0c0ae8c7784f2e289fd5a`: library-user README.
4. `945af6a97717a7a6373507bbc9592d5cd53727c2`: guarded Actions publication.

**Obsolete-history conclusion:** no abandoned approach, transitional shim,
separate fixup or superseded correction remains in either final feature
series. The runtime/generator/fixture and handwritten/generated/documentation/
workflow splits remain coherent. Prior review findings are folded into their
owning commits. The current rebase adds no design or public-contract expansion.

**Migration conclusion: no migrations.** Neither complete feature diff
introduces a database or persisted-format migration. Generated API migration
actions are ordinary bindings. There is no intermediate schema version,
merged/released/deployed migration or consumed state requiring retention.
Existing disposable test database bootstrap is not a feature migration.

**Repeated-update conclusion:** no repeated dependency/input/channel,
lockfile, schema-capture, generated-output or provenance update stream remains
in either unmerged series. Client provenance refresh and D2 wording are folded
into the original package commit; generated patch bytes remain unchanged.
The upstream Nix update is already integrated baseline history and is not a
redundant feature update. Retaining the old `9e4c29a...` source ref for the
previously published client pin preserves an exact consumer reference, not an
extra update commit in the new series. No release/state exception is needed
to retain superseded feature updates.

## Remaining verification and disposition

Read the three final hook logs: applicable pre-commit and commit-message hooks
pass. The packet also records Ruby 26-file syntax, Nix parsing and whitespace
passing with Ruby 3.4.11/Overcommit 0.73.0. The old Cargo store executable was
garbage-collected; no current formatter/compiler pass is inferred from that
failed launch or from historical formatting evidence.

The [refined verification plan](artifacts/approved-default-integration/fresh-verification-plan.md)
appropriately requires exact final-head HaveAPI CI for the new Ruby unit/lint,
current formatter/runtime default/blocking/Clippy and generated root/mounted
server acceptance. Exact client CI verifies its own pinned compiler/MSRV and
generation against the rebound HaveAPI source. A fresh local watcher supplements
those gates with tool identities and extracted-gem/full saved API 7.0
reproduction. These results remain pending; old green SHAs are not substitutes.
Unchanged actual-vpsAdmin acceptance retains only its bounded input evidence
described above. No repeat production GET smoke is required by this rebase.

Affected-lane and complete history/provenance review is complete for HaveAPI
`68cc80b...` and final client `945af6a...`, with D2 closed through the lead's
narrow-fix policy. The lead owns fresh verification acceptance, final current
target checks and approved default-branch integration. The user's current
direction explicitly holds releases: no tag, release dispatch, registry setup
or publication is part of this review.

Only this review report was written. No source, Git or session-state mutation,
test/build, server, CI, registry or lifecycle action was performed. The session
remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>
