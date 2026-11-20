---
lifecycle: active
---

# 2026-11-20-nixos-channel-fix-status

## Status

- [x] Checked published `nixos-26.05`: `3457b69ac4aba6d9ea9a743370af160fb502db29` lacked both fixes.
- [x] Initial `release-26.05` check: `42c043a7e428a1f2097b62683609383288601b53` includes #590478; Ruby #590275 remained on `staging-26.05`.
- [ ] Prepare the one-time confctl pin update and verify the generated diff.
- [ ] Independent review and feature-branch publication.

| Package | Owner | Dependencies / acceptance | Status |
| --- | --- | --- | --- |
| Confirm exact release target, channel mapping, and checks | architect0 | Read-only preflight | Assigned via same-session messaging |
| Generate and verify the one-time pin | Pending assignment | Initial tracking commit, supported worktree registration, and accepted brief | Waiting for preflight |

## Repository and scope

Only `vpsfree-cz-configuration` is affected. Do not change `vpsadminos-org-configuration` or the normal `nixos-stable` source. No default-branch integration or deployment is approved.
