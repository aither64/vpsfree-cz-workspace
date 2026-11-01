# Final operator wording

Parent writing pass: vpsfree-user-facing-writing and humanizer-en applied to the settled design and E0 draft. E0 retains the source writer and applies the replacements below. If a statement disagrees with actual behavior, report the discrepancy before committing.

## Runtime updates

Replace the sentence beginning “which rebuilds the machine config” after the update commands with these paragraphs:

Creation and ordinary updates select vpsAdminOS from `worktrees/<slug>/vpsadminos`
when that checkout exists. Otherwise, they use the canonical repository's local
`origin/staging` ref. The command does not fetch the ref automatically. Both OS
inputs use this selection for guest builds and revision metadata.

An update preserves the recorded host path exported at `/mnt/vpsadminos` and the
host QEMU and virtiofsd paths established at boot. Selecting a newer OS for the
build does not retarget the export. If the export points to a worktree, its contents
still follow that worktree. Every other requested topology or layout change must
match the retained configuration.

A `services` update builds only the services payloads, copies and switches the
services system, then completes the existing API restart and node refresh. A named
node or storage update switches only that guest. `all` updates the configured
targets sequentially and records each completed target. These switches leave the
running kernels in place. A retained cold start validates the requested layout
and boots the proved applied payloads with their recorded export and host tools.
The reused NixOS root disk keeps its recorded `rootDisk.image`.

Each requested target needs its own validated applied proof. Guests outside the
update retain their descriptors and proof status; an unproved peer does not block
a proven target. `all` requires proof for every target it updates. A retry uses
the target's prior applied VM metadata and a newly selected build candidate.
Missing or unproved target context, or a conflicting pending operation, refuses
before the build or credential preparation. Use the existing residency recovery
procedure only when historical evidence supports it. Another guest's proof cannot
establish this target's context; resetting the cluster is not a recovery step.

## Build candidates and retained boot selections

Replace only the opening sentence “`result-config` describes the full build candidate.” with:

`result-config` describes the configuration built for the operation. An ordinary
update includes new payloads only for its selected targets and retains the other
guests' applied descriptors.

In the cold-start paragraph, replace the sentence beginning “NixOS updates may change” through “must remain exact.” with:

Ordinary NixOS updates may change toplevel/kernel/initrd while preserving the
reused disk's recorded `rootDisk.image`; direct vpsAdminOS updates may change
toplevel/kernel/initrd/squashfs. Spin, boot options, resources, preserved disk
fields, networks and shared mounts must remain exact. The separate maintenance
copy-only procedure below retains its existing source-image rules.

Replace the paragraph beginning “Fresh creation records a pending boot” with:

Fresh creation records a pending boot before starting guests and establishes
residency after full boot proof. Legacy images remain readable, but an ordinary
update refuses a target without validated applied proof. Existing residency
recovery may establish that proof when historical evidence supports it. Cold
start requires proof for every guest. A build, image age, stale readiness file
or another guest's proof cannot establish the missing context. This requirement
does not change the stored envelope format.

## Portal retained-start introduction

Replace “which reuses the saved topology and network and follows normal build/boot behavior from the session's selected sources.” with:

which reuses the saved topology and network, validates the requested layout against
the session's selected sources, and boots the proved applied payloads.

## Bounded diagnostics

Use these fixed strings without interpolating private/user input:

- Applied VM context is unknown; use residency recovery only with supporting historical evidence.
- The requested update target is absent from the applied topology.
- Applied VM context is unproved for the requested target.
- Another applied operation remains uncertain.
- The retained selection is incomplete or pending.
- The recorded OS source export is unavailable.

Nix projection rejection:

The requested configuration changes the retained VM topology or layout.

Normal output when using retained context:

Builds use the selected OS source. /mnt/vpsadminos and host VM tools keep their recorded boot paths.
