# Devcluster resolver

- Date: 2026-05-30
- Initiative: `work/2026-05-30-dev-vpsadmin-clusters`
- Symptom: authoritative DNS in a devcluster could render correct primary and
  secondary zones, but BIND notify behavior failed when nameserver names only
  existed in `/etc/hosts`.
- Cause: BIND's own notify target lookup is DNS-based. `/etc/hosts` made
  ordinary libc lookups work, but `host ns-public.aitherdev.int.vpsfree.cz`
  returned NXDOMAIN inside the DNS VM.
- Fix: `dev-clusters/vpsadmin/default-config.json` now has configurable
  `resolver` settings. The default `cluster` mode runs dnsmasq on the services
  VM, serves all generated devcluster host records, and forwards other lookups
  to `resolver.upstreamNameservers`. Other VMs point at the services IP.
- DNS detail: the vpsAdmin DNS-server Nix test module accepts `forwarders`,
  and devcluster DNS VMs set BIND forwarders to the services resolver. This
  lets named resolve SOA/NS notify targets without adding explicit
  `also-notify` to generated zones.
- Verification: the running bridge cluster transferred a PTR update from hidden
  primary `172.16.106.61` to secondary `172.16.106.62` without `also-notify`;
  both servers reached SOA serial `4`, and `check_reverse_records` reported
  `2 records ok`, `0 dns errors`, `0 records incorrect`.
