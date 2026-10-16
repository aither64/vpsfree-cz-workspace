# Independent review of impermanence persistence

The user explicitly requested GPT-6 Astra/xhigh assessment of the whole
persistence mechanism, including inherited mount promotion, host/image
responsibilities and upstream impermanence, rather than only the newest fix.
Fresh standalone reviewer `/root/astra_persistence_review` was launched with
`model=gpt-6-astra`, `reasoning_effort=xhigh`, fresh context and read-only
instructions. This honored the explicit request without reconfiguring retained
reviewer0 or asking architect0 to independently review its own design.

Reviewed product head: `20b803f349d68b1bb5619058ccc025e16baafd29`, tree
`5f1773c9811935622b1914adcd266000b42273df`. The reviewer read actual upstream
NixOS/impermanence sources and the existing runtime receipts; it ran no tests
and changed no files, refs or runtime state. The collaboration launch settings
are the model/effort evidence; the reviewer had no separate introspection API.

## Findings

1. **Important: selection omits valid persistence declarations.** Exact
   `/var/lib/nixos` and `/var/log` systemd binds enable the guard, while a sole
   `/var` or `/var/lib` bind or direct `fileSystems` declaration can leave users
   before specialfs. Pinned impermanence explicitly recognizes allocation-state
   ancestors (`nixos.nix:598`). This is source-established missing coverage,
   not a newly reproduced failure or a rejection of the supplied-layout passes.
2. **Advisory: bootstrap source metadata is permanent.** The adapter creates
   missing sources as root/0755. Pinned `create-directories.bash:46-53` applies
   configured metadata only when the source is absent. Actual fresh runtime
   `testct-a498` requested0710 but retained `0:0:755:384` in machine-shell.log
   near5283. Snapshot equality alone accepted the initial value. Documentation's
   later-metadata promise was misleading; custom owner and mode need an owner.
3. **Advisory: recursive directory preparation might use scoped mkdir-p.** This
   was conditional on equivalence. Architect0's follow-up found different
   missing-parent behavior under inherited default ACLs; the accepted refinement
   keeps the existing helper rather than changing that metadata contract.

## Architectural conclusion

Keep guest-owned persistence, host-provided storage and upstream global early
mount ordering. The absence of initrd, LXC's existing proc mount, impermanence's
after-users source creation and NixOS's continuing ERR trap explain why a bare
dependency edge is insufficient for both fresh sources and failed mounts.
The whole-value specialfs seam is awkward but proportionate at the supported
pins. Moving guest persistence policy into osctld, forcing another account
backend/fixed IDs, changing only the proc guard or adding another mount
framework would not provide a simpler compatible solution.

The minimum invariant is that the first legacy allocator invocation sees the
intended state, fresh sources can initialize, failed required mounts cannot
masquerade as fresh state, and repeated activation preserves existing state and
mount relationships. The scope gap, metadata ownership and missing tests should
be refined within that adapter. There are no migrations or coordinated host
updates. Rollback can restore the ordering defect; drifted identities need
separate recovery.

## Accepted disposition

The user chose root/0755 defaults, custom owner AND mode pre-provisioning, then
approved the implementation plan. Architect0 recorded the accepted brief in
`design.md` (initial revision SHA256
`c80fea979d8fe48c48d98b78a81b21dd8ea596e31d0c45e8eda296abdb1382b9`).
It covers effective state-covering mounts and required predecessor membership
using existing `utils.fsBefore`, checked bind/nonbind handling, precise source
metadata policy, and twelve registered runtime cases. No new mount sorter,
phase, replay or metadata repair is authorized. Instruction amendments are
separately being restored at the user's direction.

This supplemental assessment does not replace committed final review of the
refinement or its new-head runtime acceptance. Earlier20b eight-case/image
success remains exact prior evidence. Integration, deployment, production KB
publication and lifecycle closure remain unauthorized.
