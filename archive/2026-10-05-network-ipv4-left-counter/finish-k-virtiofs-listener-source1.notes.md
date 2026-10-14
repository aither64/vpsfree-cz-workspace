Source-only virtiofs listener draft at K492

The shared adapter retains only transient path authority; only the listening
descriptor is explicitly mapped to fd3. Parent listener/log closure is protected
through child acquisition and PID retention. Cleanup validates all recorded
paths before deleting any, rechecks each adjacent to unlink, closes proof FDs,
and refuses a subsequent deletion attempt after unsafe-path refusal. Retired
absent paths never reacquire deletion authority. No old pidfile is unlinked.

The only flake change exposes the existing guest-pinned pkgs.virtiofsd as
VPSADMIN_KB_VIRTIOFSD. The tool-shell daemon is not substituted. Both old machine
classes use the same adapter; PreparedDisks and every original test/helper byte
are preserved. The public-stop fixture uses an owned Ruby process for the VM
transport while retaining the actual pinned OSVM QEMU reaper and daemon wait.

The root paragraph matches the source. All focused cases are drafted and UNRUN.
Root owns normal consolidation/publication, hosted exact K/E checks, affected
committed review, packages and fresh capacity admission. G13 retention is the
lead's explicit disposition, not a successful stop or source cleanup claim.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
