# 2026-06-10-vpsadminos-nftables-bug

## Goal
Investigate a temporary mitigation for CVE-2026-23111 on vpsAdminOS systems
running vulnerable 6.12 kernels before all machines can be upgraded to
6.12.70 or newer.

## Affected repositories
- `vpsadminos`: already contains kernel packaging and an eBPF livepatch
  framework under `os/livepatches/ebpf`.

## Approach
- Prefer upgrading affected machines to a fixed kernel where possible.
- For a temporary eBPF LSM mitigation, use the `lsm/netlink_send` hook:
  `security_netlink_send()` is called after userspace netlink data has been
  copied into a kernel skb and before dispatch to the kernel netlink receiver.
- Match `NETLINK_NETFILTER` traffic and parse nfnetlink/nf_tables message
  headers.
- Preserve container nftables functionality by tracking only risky verdict
  maps/sets:
  - On `NFT_MSG_NEWSET`, remember sets created as `NFT_SET_MAP` with
    `NFTA_SET_DATA_TYPE == NFT_DATA_VERDICT`.
  - On `NFT_MSG_NEWSETELEM`, mark the set risky only if the operation adds a
    `NFT_SET_ELEM_CATCHALL` element with verdict data that references a chain
    (`NFT_JUMP` or `NFT_GOTO`).
  - Keep the risky mark conservatively until set/table teardown or kernel
    upgrade. Unmarking on element deletion is optional and only safe if the
    parser can model transaction aborts accurately.
  - Deny `NFT_MSG_DELSET`/`NFT_MSG_DESTROYSET` for a risky set only when the
    batch contains more than that single real operation. A lone deletion batch
    should commit rather than abort and should be allowed.
- Consider coarser fallbacks only if the parser is not acceptable:
  `lsm/socket_create` can deny `AF_NETLINK`/`NETLINK_NETFILTER` sockets from
  non-initial user namespaces, and `lsm/capable` can deny `CAP_NET_ADMIN` in
  non-initial user namespaces.

## Compatibility and deployment
- The precise `netlink_send` policy should leave host-root firewall management
  in the initial user namespace unaffected.
- Container nftables functionality should be largely preserved. The expected
  breakage is limited to batched atomic changes that delete a tracked risky
  verdict map/set together with other operations. A standalone delete of the
  risky map/set can remain allowed.
- `socket_create` would break all netfilter netlink use from affected
  containers. `capable` would break many unrelated `CAP_NET_ADMIN` operations
  in user namespaces, not just nftables.
- vpsAdminOS enables `CONFIG_BPF_LSM` for kernels >= 6.12.33, covering the
  available vulnerable 6.12.48, 6.12.58 and 6.12.59 kernels.

## Testing plan
- Unit-test parser logic with representative nfnetlink batches:
  fixed-kernel-safe operations, direct/non-batch messages, malformed lengths,
  `NFT_MSG_NEWSET`, catchall verdict `NFT_MSG_NEWSETELEM`,
  `NFT_MSG_DELSET`, and `NFT_MSG_DESTROYSET`.
- VM-test on a vulnerable 6.12 kernel that:
  1. a process in a user namespace can perform ordinary nftables operations;
  2. a standalone delete of a tracked risky verdict map succeeds;
  3. a multi-operation batch deleting a tracked risky verdict map is denied;
  4. host-root nftables operations still work;
  5. the eBPF livepatch is skipped automatically on kernels >= 6.12.70.
