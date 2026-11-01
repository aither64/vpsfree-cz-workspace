# Operator prose for parent pass

Place after Runtime Updates commands:

Creation and ordinary updates select vpsAdminOS from the session's own worktree when present, otherwise from the canonical repository's locally fetched origin/staging ref. The update does not fetch that ref or fall back to an older OS. The selected source supplies guest build inputs and revision metadata. Running guests keep their recorded /mnt/vpsadminos export and host QEMU/virtiofsd paths; selecting new build inputs does not retarget that export. Every other requested topology/layout change still refuses.

A services update realizes only services payloads, switches only services, and keeps the existing API restart and node refresh. A named node or storage update switches that guest; all switches the configured targets sequentially and records each completed target. These switches do not replace a running kernel. A later retained cold start uses proved applied payloads, while checking the requested layout with current build inputs and preserving the boot export and host tools. The existing NixOS disk retains its original rootDisk.image.

Each requested target requires existing validated applied proof. Unproved peers remain unchanged and unproved; all requires proof for every target it switches. Same-target retries retain prior applied VM metadata and use a normally selected new candidate. Missing, unproved or conflicting context refuses before building or preparing credentials. Use existing explicit residency recovery only when historical evidence supports it; do not reset or infer context from another guest.

Replace old legacy paragraph claim “Existing legacy images without the envelope remain readable and target-updatable” with a precise qualification: old retained images stay readable, but an ordinary update of an unproved target is refused until supported residency recovery establishes that target's context. Cold start still requires all targets proved. No schema migration is introduced.

Current bounded diagnostic strings for build-context (no user input is interpolated):
- applied VM context is unknown; explicit residency recovery required
- update target is not in the applied topology
- applied VM context is unproved for the requested target
- another applied operation remains uncertain
- retained selection is incomplete or pending
- recorded OS source export is unavailable

Nix projection rejection: Requested configuration changes the retained VM topology or layout

Fixed normal output when a retained context is used:
OS build inputs follow the current selector; /mnt/vpsadminos and host VM tools keep their recorded boot paths.

Technical facts only; E0 retains source writer. Please return settled wording before final commit; independent implementation and focused checks continue.
