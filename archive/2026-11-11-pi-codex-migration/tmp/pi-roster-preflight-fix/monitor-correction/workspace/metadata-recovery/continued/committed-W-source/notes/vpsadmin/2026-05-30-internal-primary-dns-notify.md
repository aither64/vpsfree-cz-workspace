# Internal Primary DNS Notify

- Date: 2026-05-30
- Project: vpsadmin
- Initiative: `work/2026-05-30-dev-vpsadmin-clusters`
- Symptom: a fresh devcluster hidden primary served a new PTR record, but the
  public secondary stayed on the old zone serial and returned NXDOMAIN until a
  later transfer.
- Cause: the devcluster nameserver names were present in `/etc/hosts`, but not
  in DNS. On the primary VM, `getent hosts
  ns-public.aitherdev.int.vpsfree.cz` returned `172.16.106.62`, while `host
  ns-public.aitherdev.int.vpsfree.cz` returned NXDOMAIN. BIND notify target
  resolution is DNS-based, so `notify yes`/`notify-to-soa yes` could not find
  the SOA/NS target by name.
- Why this differs from production: production `ns3.vpsfree.cz` and
  `ns4.vpsfree.cz` are real resolvable names, so ordinary BIND notify behavior
  can work there. The devcluster used fake lab names for the same topology
  without adding those names to DNS, so the hidden primary had no DNS-resolvable
  target to notify.
- Rejected workaround: rendering `also-notify { <secondary-ip>; };` for
  internal primary zones made the devcluster work, but it encoded a
  devcluster-specific resolver failure in `libnodectld`. The Ruby change and
  generated gem pin updates were reverted.
- Fix: make devcluster resolver behavior configurable. The default
  `resolver.mode = "cluster"` runs dnsmasq on the services VM, serves all
  generated devcluster host records from `config.json`, and forwards other
  lookups to configurable upstream nameservers. DNS VMs use the services VM as
  both `/etc/resolv.conf` resolver and BIND forwarder, so BIND can resolve SOA
  and NS names through DNS instead of relying on `/etc/hosts`.
- Verification: bridge devcluster primary `named.conf` contains no
  `also-notify` lines and retains `notify yes`/`notify-to-soa yes`. After a PTR
  update, the secondary BIND log showed notify from `172.16.106.61`, transfer
  of serial `4`, and transfer status `success`; both DNS servers answered the
  new PTR and `check_reverse_records` reported `2 records ok`, `0 dns errors`,
  `0 records incorrect`.
