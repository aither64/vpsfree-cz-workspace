# NixOS test address override priorities

The mx2 isolated test's network helper assigns IPv4 addresses with
`lib.mkOverride 20`. A sender-specific two-address list using `lib.mkForce`
(priority 50) lost to that stronger helper, leaving only the first address.
A bound SMTP client then failed with `OSError: [Errno 99] Cannot assign
requested address` before the intended DNSBL test reached Postfix.

Use a deliberately stronger priority for the complete sender address list
(`lib.mkOverride 10` here), check the evaluated addresses, and assert the
required source address in the guest before using it. `mkForce` is not stronger
than every explicit override; lower numeric priority wins. Preserve the network
restrictions and untrusted-source role when fixing fixture plumbing.

Evidence: [mx2 verification](../../work/2026-11-01-mx2-nixos-migration/state.md),
failed batch3 log and dedicated-address remediation receipt. This is a test
fixture lesson, not a production mail policy change.
