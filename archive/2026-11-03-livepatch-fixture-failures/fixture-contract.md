# Fixture and normal-package contract diagnostic

Owner: implementer3, retained `gpt-6.1-sol` / `xhigh`. This is source analysis,
not independent change review or an implementation. Session/environment identity
matches `2026-11-03-livepatch-fixture-failures` and
`/home/aither/workspace/ai/vpsfree.cz`. The assigned vpsAdminOS worktree was
clean at canonical staging `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
No checks, builds, reruns, source/pin edits or Git mutations were performed.
The historical producer, actual module bytes and complete input graph belong
to the other diagnostic packages; their results are not independently claimed
here.

The smallest correction must stabilize the **normal .95 module producer** and
retain the fixture's independent expected hash and direct producer linkage.
Freezing only an archived corrected test module would let qualification pass
for old bytes while the normal package drifts. The present fixture deliberately
detects that mismatch.

## Producer and consumer map

Paths below are relative to the assigned vpsAdminOS worktree.

| Surface | Source evidence | Contract |
| --- | --- | --- |
| Normal module producer | `os/modules/services/livepatches/default.nix:13-45,59-81,176-204,423` | Current patch registry and payload produce `system.build.livePatches`, including `lib/modules/6.12.95/extra/livepatch_7.ko`. `dontStrip = true` protects livepatch relocation symbol indexes. |
| Normal CI package | `flake.nix:335-346,437`; `.github/workflows/ci.yml:140-153` | `ci-livepatch-6_12_95` uses the shared .95 boot-base configuration and normal service producer; CI caches/uploads that package. |
| Corrected fixture | `tests/fixtures/livepatch/default.nix:8-18,47-49` | Independently pinned SHA256 `573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`; checks the normal producer's module, then symlinks that module. It does not restore archived v7 bytes. |
| Workflow preparation | `.github/workflows/ci.yml:418-443` | Unsets ad hoc module/name/example overrides, reads the source hash pin, builds corrected/v5/v6 fixtures, exports their paths and the expected corrected hash. Every lifecycle matrix row goes through this preparation before its selected tests. |
| Main and qualification | `tests/suite/kernel/livepatch-6.12.95-common.nix:1-39,476-480,2150-2163`; `livepatch-qualification.nix:70-96` | Main and every qualification instance share the environment-selected corrected module and exact predecessor hashes. Nix assertions and guest checksum checks bind the bytes. Qualification disallows partial example filtering. |
| Intel TUN and perf | `tests/suite/kernel/livepatch-tun-intel.nix:5-30`; `livepatch-perf-v7.nix:4-11,63-94` | TUN inherits the main contract and selects exactly one example. Perf consumes the same corrected path and independently supplied expected hash, checks it in the guest, then loads `livepatch_7`. |
| NFS and SCTP | `tests/suite/kernel/livepatch-nfs-transition.nix:22-39`; `livepatch-sctp-common.nix:26-58` | Qualification mode consumes corrected bytes and directly imports the fixture hash; requires the `livepatch_7` name. Explicit single-series mode is a separate diagnostic path and does not establish ordinary qualification. SCTP baseline has no candidate. |
| Fragment witness | `tests/suite/kernel/livepatch-inet-frag.nix:4-8,41-44` | Requires the corrected module to match the fixture hash; uses exact frozen-kernel/pinned-module offsets. |
| Normal lifecycle | `tests/suite/kernel/livepatch-lifecycle.nix:62-76,168-172,210-265`; `livepatch-lifecycle/6.12.95.nix` | Loads candidate directly from the guest's `/etc/livepatch-store-path`, checks name/vermagic and logs SHA256. The candidate SHA is a witness, not an independently pinned assertion. Exact archived v5/v6 predecessors remain separate. |
| Boot identity | `tests/suite/kernel/livepatch-kernel-identity.nix`; service producer `:365-373` | Normal utility operations require both the configured boot-image path and byte-identical kernel notes. Tests verify refusal preserves active protection, successful matching load/unload, and insertion-failure propagation. |

The fixture and flake package invoke the same service implementation through
the same boot-base module. This is source-level linkage; exact derivation/path
or byte equality between those evaluation entry points still needs acceptance
evidence. The lifecycle SHA witness alone cannot establish that equality.

## Invariants the correction must preserve

1. **Independent qualification identity.** Keep the corrected hash a reviewed
   source constant. Never compute the expected checksum from the candidate at
   test execution, skip the check, or accept another digest just to prepare the
   fixture. A changed candidate requires an explicit candidate/qualification
   decision and revalidation of disassembly-sensitive witnesses.
2. **Frozen ABI is stronger than a version.** The existing boot archive retains
   shipped kernel bytes and full `vmlinux` DWARF. Same-version rebuilds generate
   a different signing certificate/build ID. Preserve original image/notes
   guards, config, import CRC compatibility, and restored binary bytes
   (`os/packages/linux/boot-6.12.95/README.md`). No guard bypass, stripping or
   rebuilding the boot kernel to satisfy the fixture.
3. **Freeze producer inputs, retain current payload.** The current service only
   overrides .95 `dev`/config and prefixes its boot compiler for kpatch's command.
   Its kpatch-build package, outer stdenv/compiler dependencies, native inputs
   and builtin-ZFS preparation are still selected elsewhere in the normal
   configuration (`default.nix:12,29-40,81,150-157,176,186,203`). These are contract
   surfaces, not a causal attribution to a particular changed input. The exact
   historical closure is architect/other-package evidence.
4. **Released migration anchors remain exact.** Preserve v5 SHA256
   `b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
   and shipped-v6 SHA256
   `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`,
   their archives, names and independent v5-to-v7/v6-to-v7 instances on both
   vendors. Migration tests must exercise those artifacts, not current-source
   rebuilds. Downgrade insertion remains rejected while v7 stays active.
5. **Qualification includes state and recovery.** Retain task/CPU/memory/age
   shapes, callbacks with independent expected counts, workload progress,
   preexisting-state/data witnesses, health checks and bounded activation and
   disable. Failed activation must leave its predecessor enabled. Do not force
   or reverse a failed qualification to make progress; retain diagnostics and
   normal VM teardown (`qualification.rb:12-34,220-311,384-557`;
   `livepatch-6.12.95-common.nix:2225-2243`). Passing fixture preparation does not
   establish transition success or deployment qualification.
6. **Keep the scope on .95.** Other kernel lines retain their own development
   outputs and build tools. Native .110 continuity has no v7 candidate. Preserve
   ordinary registration and AMD/Intel selectors; no global input rollback or
   changed default kernel is needed for this correction.

## Recommended correction boundary

Use one immutable .95 **module-build input set**, established from the producer
that actually yielded the independently expected corrected bytes. Wire it into
the normal `system.build.livePatches` producer, so the fixture and normal CI
package inherit the correction together. Keep current local patch and kpatch
recipe sources explicit, alongside the fixed boot ABI. A historical package-set
lock must not accidentally import an old livepatch payload or merely reuse the
older boot-kernel recipe's input set without proving it matches this candidate.

The smallest likely source boundary is:

- `os/packages/linux/boot-6.12.95.nix`: expose the required immutable build inputs
  alongside the existing ABI/compiler contract. The module-build input root may
  differ from its already pinned boot-kernel recipe. Architect0 decides whether
  separating that root into a new sibling helper is clearer; no new general
  freezing framework is needed.
- `os/modules/services/livepatches/default.nix`: apply that input set to all
  byte-affecting .95 producer stages, including kpatch-build and preparation,
  while preserving current payload selection and other kernel lines. Preserve
  the existing scoped compiler behavior or demonstrate its replacement avoids
  the documented builtin-ZFS preparation failure; do not broaden PATH blindly.
- `tests/configs/vpsadminos/livepatch-6.12.95-boot-base.nix`: reconcile comments
  `:9-10,40-41` with the shared producer freeze. The guest still restores exact
  boot outputs and the candidate still comes from current OS payload sources.
- `os/packages/linux/boot-6.12.95/README.md`: document the separate boot-byte and
  module-input contracts and the normal-package/qualification linkage, or link
  to a sibling helper's explanation if the architect chooses that layout.

Keep `tests/fixtures/livepatch/default.nix` hash/symlink behavior and the current
workflow/test checks. They already enforce the required linkage. No expected
digest, archive, patch registry, payload, workflow matrix or root `flake.lock`
change is justified by this contract analysis. A focused automated equality
check may be useful only if normal/fixture evaluation cannot otherwise share
and retain a clear identity proof; avoid a second fixture-only producer.

## Acceptance checks for an authorized implementation

These are proposed checks, not executed results.

**Quick, before final review:** run the repository's declared formatting/hooks;
evaluate the fixture and `ci-livepatch-6_12_95` producer metadata; inspect their
full derivation/input receipts and prove equivalent module-producing inputs.
The normal package and fixture must use current payload sources with the same
frozen .95 build inputs. Perturbing only unrelated outer package inputs should
leave the .95 module producer unchanged; an explicit current payload/recipe
change must remain visible. Verify another supported kernel's toolchain/ABI
selection is unchanged. Preserve the predecessor constants and all qualification
identity assertions. Obtain the fixture/normal-package byte-equality proof from
already available artifacts when possible; uncached compilation is a longer
check, not a prerequisite hidden inside a quick evaluation.

**Build and identity, after review when required:** build the normal package
(`nix build --no-link --print-out-paths .#ci-livepatch-6_12_95`) and all three
existing fixture attributes (`nix-build tests/fixtures/livepatch -A corrected`,
`-A releasedV5`, `-A shippedV6`, using session-owned output links). Check that
the corrected symlink resolves to the actual normal producer's module, compare
bytes/digests, and preserve independent expected hashes. Check name/vermagic,
all imported symbol CRCs against the frozen SDK, relocation integrity and exact
instruction offsets used by witnesses. Test restoration/build availability in
a cold environment. Stop an unexpected local kernel build; do not replace the
frozen boot bytes with a same-derivation rebuild.

**Longer runtime:** reuse the existing workflow fixture preparation and all nine
AMD/Intel rows, including fresh, scale-aged, low-memory and representative v5/v6
qualification. Keep single-series/example overrides unset. Run ordinary .95
lifecycle v5/v6 cases and `kernel/livepatch-kernel-identity` to exercise the
normal producer; preserve main, perf, TUN, SCTP, fragment and NFS coverage under
their existing selectors. Native .110 continuity must remain unchanged. Use
fresh utility watchers for authorized long/uncertain checks. A green preparation
or one short lifecycle case does not replace the existing qualification matrix.

## Compatibility, rollback and open decisions

This diagnostic changes no software or state. A shared-producer correction
would affect normal .95 build recipes and potentially output paths, not only
tests. If it restores the exact independently pinned bytes, it introduces no
new module ABI/protocol/schema or persistent-format boundary and requires no
coordinated update of all nodes. It still needs cold restoration and mixed
generation/boot identity verification. A new digest is a different candidate,
even when source patches or module name are unchanged; old qualification cannot
be transferred silently.

Source rollback restores the previous recipe. It does not establish safety of
runtime rollback on a live transition. Retain the existing failed-transition
recovery constraints and the documented quarantine; do not recommend module
unload, forced reversal or boot-generation rollback as a wedge workaround.
No deployment is authorized or implied by this proposal.

Architect0/lead must settle the immutable candidate-producing input root and
its restorability from the other packages' evidence; whether that input-only
freeze reproduces the expected digest; the smallest helper placement; and the
exact authorized implementation/verification scope. If restoration cannot
reproduce expected bytes, report the limitation and choose explicitly between
restoring the actual producer artifact with retained source/input provenance
or qualifying a newly identified candidate. An archived test file alone is
insufficient in either case.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
