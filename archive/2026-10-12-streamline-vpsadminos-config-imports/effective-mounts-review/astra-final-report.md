**Blocking: none.**

**Important — I1: Fresh-directory metadata does not fully implement the accepted root:root/0755 policy.**  
*Lanes: general, risk/compatibility. Owner: persistence commit `bf74af0b76accdf844ad6ffbea75db6c409f386e`.*

The [directory helper](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos/os/lib/nixos-container/stable/vpsadminos-26.05.nix:95), identical in all four raw modules, uses only `mkdir -m 0755`. GNU mkdir preserves inherited directory setgid semantics. Under an existing parent owned by group 1234 with mode 2775, a newly created source can therefore be **0:1234:2755**, rather than **0:0:755**. The [GNU documentation](/nix/store/yin1xr0wd8g6v2gfs49haribk664vp7c-coreutils-full-9.11-info/share/info/coreutils.info:16534) explicitly documents this behavior, including `mkdir -m 0755`.

This contradicts the fixed metadata decision and [product guidance](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos/docs/containers/nixos.md:136). Impermanence will preserve that source metadata afterward. Existing fixtures use ordinary parents, so their passing metadata assertions do not cover this case.

Enforce the chosen ownership and complete mode on newly created directories only, preserving existing directories and explicit failure propagation, or record an explicit decision accepting and documenting inherited metadata. A focused setgid-parent case should accompany enforcement. This is established by source and documented tool semantics; I ran no reproduction and claim no demonstrated identity drift or data loss.

**Advisory: no additional findings.**

The whole mount approach is otherwise sound within its stated boundaries. Guest compatibility is the appropriate owner: host storage provisioning remains unchanged, while the adapter addresses absent initrd mounting, LXC’s pre-mounted proc, fresh source preparation, and NixOS activation’s continuing ERR trap. Effective ancestor/direct-filesystem selection closes the original coverage gap. The finite predecessor closure determines checked membership without replacing upstream ordering or cycle handling. Required operations explicitly abort before legacy allocation; unrelated callbacks retain upstream behavior. Bind identity checks, non-bind dispatch, dry activation, alternative backends and guest overrides are coherently handled.

The four self-contained copies are justified by standalone downloads. Latest stable equals 26.05; the four persistence changes are identical. The recursive-helper retention is justified by the documented parent-ACL distinction, independently of I1.

I independently verified these clean identities:

| Repository | Reviewed HEAD | Tree |
|---|---|---|
| vpsadminos | `bf74af0b76accdf844ad6ffbea75db6c409f386e` | `822fe1de775fb57c592d8cef884ff016695a6ac2` |
| workspace | `c0d19e269fe5d34d4680c0988711061eb0faf959` | `6b06b7a1ed77edf59d05caf978c56050fe8c75c5` |
| vpsfree-dev-workspace | `767dfd587e346168e1443e65ccdb67ce748f3fe3` | `80181fb9f3805e99734b85edfdbcdd022f5e4b67` |
| vpsfree-kb-contracts | `2d11b2cc8445a695e7862af18ca0a70598afb38b` | `dce630658c0f71f5b037bfec317763abf2c9315b` |

The complete product range starts at `7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8` and contains exactly selector v5 `b2669ce00d440c1e05eb07b0e5bb4d201f3e5161`, then persistence v8 `bf74af0b76accdf844ad6ffbea75db6c409f386e`. The 24-path live diff matches the packet hash. Selector patch equality and persistence patch equality across the final rebase are verified.

**Whole-branch/history conclusion:** the two logical owners are appropriate; caused repairs are folded in. No obsolete separate mount phase, non-root restriction, instruction owner, fixup or WIP remains. There are **no repeated production dependency/input/generated-update streams** and **no migrations**—including no map-format or transitional conversion. Earlier publication and disposable testing do not require retaining superseded shipping commits.

Workspace and extension ranges are empty against their recorded fetched defaults; all six restored instruction blobs match the restoration proof. KB identity is unchanged above `ce2c8cd9358c3636e5d39343e595df813a0b197f`; its completed content/history conclusions remain applicable and were reused.

Documentation placement is appropriate: lasting behavior, adoption and recovery limits are discoverable in the product guide; execution history remains in session records. Apart from I1, the compatibility account matches implementation: independent guest adoption, unchanged formats/stateVersion, no coordinated host update, no repair of already-drifted IDs, and rollback potentially restoring the old ordering defect. Undeclared host-storage availability and arbitrary non-bind durability remain explicit limits.

Original final receipts confirm all stage statuses zero, three-release assertions, 483 shell scenarios, twelve generated Ruby scripts, hooks and discovery. Relevant upstream activation/mount/allocator sources remain unchanged at the final stable pin. These establish local checks, **not revised guest acceptance**.

**Runtime-phase conclusion:** I1 requires a fix or explicit recorded disposition before advancement. After that disposition, the approach can proceed to the planned runtime phase under the root lead’s acceptance. The revised twelve-case runtime and image checks remain pending; prior `20b803f` results remain revision-scoped. This report claims no overall-green CI, merge, deployment, production publication or session closure. I made no edits, ran no tests/Nix evaluation/build/runtime, and performed no ref, team or lifecycle mutations.