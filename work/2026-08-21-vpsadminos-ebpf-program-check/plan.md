# 2026-08-21-vpsadminos-ebpf-program-check

## Goal

Retire `cifs_spnego_guard` on kernels which contain the upstream CIFS SPNEGO
description validation, and make successful eBPF livepatch reloads reconcile
the attached programs to the complete new configuration. Update the staging,
OS-staging, and production configuration channels to the tested feature
revision without deploying Nodes or merging either default branch.

## Affected repositories

- `vpsadminos`: change the eBPF generation handoff, add the CIFS guard upper
  kernel bound, and cover registry and runtime lifecycle behavior.
- `vpsfree-cz-configuration`: pin the `staging`, `os-staging`, and `production`
  vpsAdminOS channel inputs to the reviewed feature revision through
  `confctl`.
- workspace coordination repository: document that unexpected local kernel
  rebuilds are bugs to investigate and that additional required kernel outputs
  must be published by the vpsAdminOS builder.
- `linux`: read-only evidence for the upstream and stable CIFS fix; no local
  worktree or source change.

## Approach

1. Keep the attach-first generation handoff, but after a complete successful
   load remove every older generation instead of only same-named replacement
   pins. An empty desired set is a successful generation which removes all old
   links. Failed new loads retain and report the previous generation.
2. Give `cifs_spnego_guard` the exclusive upper bound `6.12.92`, matching the
   first stable release containing upstream commit
   `3da1fdf4efbc490041eb4f836bf596201203f8f2`.
3. Split generic lifecycle reconciliation and the program-specific retirement
   into two focused vpsAdminOS commits. Link the upstream commit in the CIFS
   retirement commit message.
4. Add Nix registry coverage and an RSpec-style VM lifecycle test which
   switches from a configured program set to an authoritative empty set and
   verifies the load-failure preservation path.
5. Retain the plain pre-ZFS kernel development output in the CI toplevel so the
   vpsAdminOS runner publishes this existing build input to the binary cache.
   Do not retain the plain runtime kernel output, which consumers do not need.
6. Push the vpsAdminOS feature head, then use one generated `confctl` commit to
   pin `staging`, `os-staging`, and `production` to it. The production update
   intentionally includes the accepted existing 32-commit staging delta.
7. Run the mandatory fresh-agent review after intended commits and quick
   checks, before long VM and configuration builds. Push feature branches only.

## Compatibility and deployment

There is no API, schema, persisted-state, on-disk format, protocol, or public
option change. Existing generation paths remain readable across old and new
closures. A successful new reload becomes authoritative and removes old links;
an activation failure still leaves the previous generation attached and logs
the error. Rolling back to an older closure can safely reattach the redundant
CIFS guard. Nodes can update independently and no coordinated fleet reboot is
required. This initiative updates configuration pins but does not deploy them.

## Testing plan

- Run the focused registry suite for the 6.12.92 exclusive bound.
- Add and run a VM lifecycle suite covering an empty desired set, old link
  destruction, generation metadata cleanup, continued service health, and
  failed activation preserving the old link IDs.
- Wait for the vpsAdminOS action runner to publish the pre-ZFS kernel
  development output before rerunning the lifecycle VM. Treat any subsequent
  local kernel compilation as a cache bug and investigate it.
- Run active Overcommit hooks in both repositories.
- After mandatory review, evaluate staging Node
  `cz.vpsfree/nodes/stg/node1`, build managed OS-staging consumer
  `cz.vpsfree/containers/int.vpsfbot`, and evaluate production Node
  `cz.vpsfree/nodes/prg/node25`. Full Node builds require the external initrd
  host key; `org.vpsadminos/int.gh-runner1` is unmanaged and therefore excluded
  by `confctl build`.
- Monitor GitHub Actions for both pushed feature branches and investigate any
  failure before handoff.
