# 2026-11-23-stable-kernel-update

## Goal

Update the stable vpsAdminOS kernel to 6.12.119. Rebase the OS change onto current `staging` and, in a separate commit, make JSON `ct top` exit when its event monitor permanently loses coverage.

## Affected repositories

- `vpsadminos` (`staging` baseline): stable selector and new immutable Linux/ZFS catalog entry in the per-version layout, plus JSON `ct top` and its restart regression coverage.
- `linux`: downstream source stack and verified version-branch publication if the target is not already supplied by an appropriate exact head.
- No OpenZFS source change, downstream deployment pins, or machine changes are requested.

## Approach and decisions

Follow [update-kernel](https://github.com/vpsfreecz/vpsadminos/tree/staging/skills/update-kernel) and the [kernel update process](https://github.com/vpsfreecz/vpsadminos/blob/staging/docs/os/kernel-updates.md). Replace the stable selector with 6.12.119, retaining existing entries and leaving unstable unchanged. Start from the packaged stable source rather than a moving Linux ref. Account for all downstream commits and package layers; keep one final OS pin using the exact Linux commit and the GitHub archive-byte hash.

The [reconciliation brief](design.md#reconciliation-on-staging-82866bed--current-implementation-brief) defines the required new catalog layout and separate userspace commit. The exact Linux version ref is already published; do not rewrite it. The user approved merge after CI for the original kernel scope, then approved implementing the material userspace addition; obtain explicit integration approval for the widened series. No deployment authorized.

## Compatibility and deployment

Keep the predecessor's ZFS pairing and kernel/package options where compatible; inspect both ZFS build paths. Rebuild external modules against the new identity; do not reuse livepatches bound to older identities. No migration or new pool features are planned. Keep existing catalog entries and boot generations available; no coordinated rollout is planned.

## Documentation

Use the existing kernel update runbook. Record exact refs, the per-patch disposition, package-layer decisions, checks and recovery limits in the session tracker. Update the `osctl` manual for JSON stream termination and compatibility. Existing `nodectld` and `osctl-oomd` relaunch on EOF; document that unsupervised JSON clients must handle stream termination. Interactive Top and ordinary partial JSON samples retain their behavior.

## Testing plan

Verify ancestry and patch correspondence, immutable source/archive identity, selectors and applicable ZFS paths, Nix formatting and hooks. After independent review of committed Linux and OS ranges, build the exact kernel CI closure and run focused VM checks that actually boot the target. The Linux version ref was promoted after original verification. The changed OS input lock requires fresh exact-head closure and native restart/NFS/ZFS evidence. Check a healthy JSON sample followed by EOF/status 1 on permanent monitor loss, safe client cleanup and a fresh epoch on relaunch; verify packaged nodectld recovery separately without changing its code or command line. Passing CI for the exact final head remains required for integration.
