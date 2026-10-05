---
lifecycle: active
---
# KVM firewalld alternative state

## Workspace

- Initiative: `2026-08-11-kb-kvm-firewalld`
- Repository: `vpsfree-kb-contracts`
- Branch: `2026-08-11-kb-kvm-firewalld`
- Worktree:
  `worktrees/2026-08-11-kb-kvm-firewalld/vpsfree-kb-contracts`
- Base: `origin/master` at `3c02342f3b56bc8f746667823bbd36afb0d5d1dd`

## Progress

- Created an isolated development session and feature worktree.
- Source-level investigation selected uplink-zone rich rules instead of a
  custom `ANY -> libvirt` policy, because DNAT occurs before the egress bridge
  is available for policy classification.
- Added the unregistered article-candidate fixture and independent
  `kb/kvm#networking-firewalld` maintained test. The existing hook-based and
  routed-network scenarios are unchanged.
- Mandatory review of commit `cdecab018057db651f2efa45f937d492e3575385`
  found one blocking coverage gap: exact-address forwarding was not tested
  behaviorally against reachable unused addresses in both IP families. The
  reviewer found no other blocking or important issues and considered the
  firewalld/libvirt design sound.
- Follow-up review of amended commit
  `940afef982b24086c20e64b8c1fcef717d8d41ff` found the blocker resolved and
  no remaining blocking or important findings. The reviewer approved starting
  the targeted maintained integration gate.

## Commands and results

- `bin/dev-session start 2026-08-11-kb-kvm-firewalld --as-is --no-attach --no-codex`
  created the isolated session.
- `bin/dev-session worktree add ... vpsfree-kb-contracts ...` created the
  feature worktree from current `origin/master`.
- `nix develop --command bin/check` passed: the article contract now discovers
  six KVM runtime scripts, while the published article still has its original
  five executable samples during the acceptance-gate phase.
- `./test-runner.sh ls --filter 'tag=kb-runtime && kbArticle=kvm'` listed the
  new `kb/kvm#networking-firewalld` script with the five existing scripts.
- After the review fix, `git diff --check`, Nix parsing and
  `nix develop --command bin/check` passed again. The scenario now allocates a
  second public IPv4 address, proves both unused IPv4 and IPv6 control
  addresses answer ICMP, and verifies that neither HTTP nor SSH forwarding
  leaks to those addresses. It also checks for custom firewalld policies,
  direct rules and libvirt hooks.
- The first targeted integration attempt failed before starting any example:
  Nix string interpolation removed Ruby source line-continuation backslashes
  in `firewalld_forward_rule`, producing a `SyntaxError` when the generated
  RSpec script was evaluated. This was a test-definition defect, not a
  firewalld result. Replaced the implicit continuation with an explicit array
  joined by spaces.
- The first behavioral gate run on commit `0205c84` installed firewalld and
  accepted all rich rules. Service/default-zone/libvirt-zone checks and the
  static nftables checks passed. IPv4 forwarding became usable only after
  lifecycle changes; IPv6 requests reached the guest but replies did not reach
  the client. The diagnostics showed that Debian libvirt still used its legacy
  iptables backend while firewalld used native nftables. Their same-stage
  FORWARD base chains made the result registration-order dependent. The full
  VPS restart and guest autostart occurred; its example then failed on the
  same post-restart IPv6 forwarding check.
- Prepared a next gate iteration selecting libvirt's supported native nftables
  backend in `/etc/libvirt/network.conf` before defining or starting any
  networks, then submitted it to mandatory review before another long run.
- A second mandatory fresh-context review of commit
  `df29fed9e5940b26782e91b6ca8f63d3d35f9ebc` found that the native nftables
  backend makes the conflict deterministic instead of resolving it. Libvirt's
  NAT forward chain rejects new inbound traffic before firewalld's later
  `ct status dnat accept` rule can accept it, for both IPv4 and IPv6.
- The reviewer also raised a possible VPS restart timeout. The preserved run
  output disproves that concern: `vpsadminctl --raw vps restart 1` exited with
  status 0 after 322.37 seconds, and the guest, network and firewall services
  returned. The subsequent forwarding assertion failed.
- Rejected the firewalld alternative. Making it reliable would require
  replacing libvirt NAT with `forward mode='open'` and assigning all filtering
  and masquerading responsibility to firewalld. That is not materially simpler
  than the existing documented solution and changes the security ownership
  model.
- Reverted the candidate in commit
  `8eaa29d92d4f710fd8a05a8284d7347f11ec3f25`. The branch retains the reviewed
  investigation history, but its final repository tree is identical to
  `origin/master`.
- Final `git diff --exit-code origin/master...HEAD`, `git diff --check` and
  `nix develop --command bin/check` passed. The restored contract reports five
  KVM runtime tests and five executable samples; all repository test groups and
  the 118-image inventory validation pass.
- Did not push the rejected branch, change either managed article, claim KB
  staging or write to production.
- Removed the abandoned feature worktree. The local branch and its two-commit
  investigation/revert history remain available at
  `refs/heads/2026-08-11-kb-kvm-firewalld`.

## Open work

None. The proposed alternative failed its acceptance gate and was not shipped.
