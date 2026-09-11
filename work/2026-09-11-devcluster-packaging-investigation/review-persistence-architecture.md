# Architecture and repetition review: pool readiness and persistent NixOS roots

Reviewed these committed ranges using the architecture and repetition lane of
the mandatory change review:

- `vpsfree-dev-workspace`:
  `9e8783d68fdf40de04683e419d4f373bc27e3730..19238ca67ad822b362ae60f0cf7e7b4b27d60397`
- `vpsadminos`:
  `3eaf7b7320754715b38fc629e7f0ce23d13402cd..e6c4c5cfa27ce3b139bba6475be80cfead4b8df4`

## Findings

No Blocking, Important, or Advisory findings.

The ownership split follows the existing component boundaries. OSVM owns how a
`NixosMachine` prepares, retains, and explicitly destroys its writable root
disk. The new constructor keyword is a general-purpose opt-in primitive; its
default keeps ordinary test-runner and QEMU-module consumers on fresh images.
The organization runner owns the persistent-development policy and enables the
primitive only for NixOS guests. It does not copy OSVM's protected disk logic or
encode vpsAdmin data in the upstream component.

The organization runner validates the cross-repository capability before its
machine-construction pass and publishes its PID only after that pass. An older
OSVM therefore cannot start an earlier machine and then fail when the first
NixOS guest receives the new keyword. The `method_defined?` check is acceptable
capability validation at this dynamic worktree/package boundary: the public
reader and constructor option are introduced by one upstream commit, the exact
companion revision is pinned for packaged validation, and an unsupported input
fails closed. vpsAdminOS-only configurations do not acquire an unnecessary
minimum-version dependency.

Root publication is localized and atomic on the target filesystem. OSVM first
keeps the existing additional-disk preparation behavior, then either reuses an
existing opted-in root or copies a complete source image into a same-directory
temporary file and renames it. Default fresh-image consumers retain their old
semantics, while failed initial or replacement copies cannot publish partial
roots. `destroy_disks` remains the one explicit reset boundary for both root and
additional file-backed disks.

The retained-root closure ordering is internally consistent with direct boot.
On first start, the copied image and the kernel, initrd, and toplevel references
come from the same built machine configuration. For a changed configuration,
the provider's existing `update` path copies and activates the selected
toplevel in the running VM; the documented order requires this before stop and
restart. The result-config GC root stays present throughout startup and normal
running; the normal graceful stop path removes it after the runner exits. OSVM
correctly leaves closure copying and activation to the caller instead of turning
a disk-retention primitive into an offline NixOS migration interface.

The node-pool wait also has the right owner. OSVM exposes interactive test
helpers for pool readiness, but the organization refresh runs after the
separate runner has published readiness and must guard its own vpsAdmin-specific
filesystem/device mutations. Reusing the authoritative `zpool` and `osctl pool
show ... state` interfaces in that remote transaction is preferable to adding
runner IPC or broadening generic boot readiness. The wait is bounded and
read-only; all mutations remain after the single readiness gate. The existing
OSVM helper and this shell boundary have different execution contexts, so their
small syntactic overlap is not a shared implementation that can safely be
extracted.

## Residual risks and test gaps

- The cross-project unit tests validate the OSVM behavior and the organization
  keyword contract separately. The packaged smoke pins and loads the actual
  companion revision, but does not start a machine through that exact pair.
  Planned live stop/start acceptance remains the representative consumer test.
- Retained roots intentionally carry no marker for the toplevel closure they
  contain. Changing configuration while the machines are stopped can therefore
  produce a boot failure until the operator restores the prior configuration,
  starts the VM, and applies `update`. The documentation records this accepted
  sequencing contract; the feature is not an offline closure installer.
- Existing root images created by older code are reused based on existence.
  The rollout assumes those images are complete, as stated in the packet and
  documentation. A partial image left by an older interrupted copy has no
  completeness metadata and would need explicit reset.
- The pool tests exercise delayed osctld activation and terminal timeout using
  the actual remote script with command fixtures. Live node acceptance remains
  necessary to validate the packaged guest utilities and real boot ordering.
