# KVM firewalld alternative

## Goal

Determine with a maintained vpsAdminOS-backed article test whether firewalld
provides a materially simpler persistent dual-stack port-forwarding setup for
the KVM KB article. Add and stage the alternative only if the stock uplink-zone
rich-rule design passes the acceptance gate.

## Affected components

- `vpsfree-kb-contracts`: firewalld fixture, KVM runtime test, article registry,
  and, after the gate passes, Czech and English KVM article sources.
- KB staging: reviewed candidates at `navody:vps:kvm` and `manuals:vps:kvm`.

No vpsAdminOS framework, vpsAdmin, deployment configuration, screenshots, or
production KB content is changed.

## Approach

1. Add an independent `kb/kvm#networking-firewalld` scenario using libvirt's
   supported native nftables backend and permanent rich `forward-port` rules
   on the VPS uplink zone. Do not use a custom policy, `--direct`, raw firewall
   rules, hooks, parsers, or services.
2. Verify exact-address IPv4/IPv6 TCP and UDP forwarding, outbound NAT, invalid
   and removed rules, kernel nftables state, libvirt zone integration, reloads,
   service and network restarts, and a complete VPS restart.
3. Accept the alternative only when it works with the Debian package-managed
   firewalld service, libvirt's supported firewall backend and stock zone model
   without recovery commands.
4. If accepted, document firewalld as the shorter option for users who want it
   to manage their VPS firewall and retain the existing hook for other users.
5. Validate the complete managed KVM article contract, push only the feature
   branch, and stage checksummed Czech and English candidates without production
   promotion.

## Compatibility and deployment

This is an optional documentation and test addition. It changes no API,
persisted format, protocol, NixOS/vpsAdminOS option, or running infrastructure.
The existing hook and routed-network instructions remain supported. Mixed
versions and rollback are therefore not applicable; rejecting the gate leaves
production and staging unchanged.

## Verification

- `nix develop --command bin/check`
- `./test-runner.sh test --fresh 'kb/kvm#networking-firewalld'`
- mandatory fresh-context reviews before long integration runs
- full `tag=kb-runtime && kbArticle=kvm` runtime filter
- GitHub `Check` and `Managed article runtime` workflows
- staged release manifest verification for both real page IDs

## Outcome

The acceptance gate rejected the proposed alternative. Libvirt's NAT network
deliberately rejects new inbound forwarding before firewalld's rich-rule accept
path. Debian's legacy libvirt iptables backend made the observed result depend
on firewall registration order; switching libvirt to its native nftables
backend does not solve the conflict because libvirt's reject chain runs before
firewalld's forwarding chain.

A design based on libvirt `forward mode='open'` could instead move inbound
filtering and outbound masquerading entirely into firewalld. That is a
different firewall ownership model, not a simpler drop-in replacement for the
documented libvirt NAT network, so it is outside the accepted design. The test
candidate is reverted and neither KB source nor staging is changed.
