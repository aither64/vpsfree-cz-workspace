# NixOS OSVM roots were recreated on every start

The vpsAdmin development-cluster restart retained node container disks but lost
all services MySQL VPS rows. OSVM NixosMachine.prepare_disks unconditionally
removed services-root.img and copied the clean base image again; retaining the
file after stop did not provide persistence. The services root and /var/lib/mysql
were on the same ext4 disk. The affected data was an owned disposable fixture.

The companion OSVM commit e6c4c5cfa adds opt-in preserve_root_disk support with
atomic initial copies. The development runner opts in and rejects older drivers.
Ordinary test machines retain the fresh-image default. A complete existing root
needs no conversion. Update running NixOS VMs before restarting with changed
configuration so the selected direct-boot closure is on their retained roots.
Do not restart retained data through an old provider/driver that recreates roots.
Final live results: work/2026-09-11-devcluster-packaging-investigation/live-validation.md.
