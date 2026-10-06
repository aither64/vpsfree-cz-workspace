# Upload improvements: completed aitherdev rollout

Status: deployment and all four default-branch integrations passed. Final master
CI also passed; no deployment, integration or verification operation remains running.

User authorized deployment through vpsfree-cz-configuration followed by default
branch integration. The later instruction required natural completion of busy
Codex threads and checks about every 15 minutes. No thread interruption, force
activation, package downgrade, cluster mutation or session deletion was used.

## Exact deployed outputs

- Host generation: 2026-10-04--22-50-54.
- Active host: /nix/store/ihrndjkq7sh2i6ldl5kh4m6cvbb192di-nixos-system-aitherdev-26.05.20261003.825e202.
- Selected and serving application: /nix/store/jq982nq0jxfhmr4jxyvkglnyy77n1kxf-dev-workspace-0.2.0.
- Runtime: 3edc605d81a30a4d49560426e0128b388b856493.
- Provider: 3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c.
- Configuration pin: e179a58ee3f7ceb4cf0b253d368c8ad94967b2d5.
- Workspace pin originally built/deployed at 88c0b957a1e870e4ce36a1743f72b529ba4825e1;
  final identical patch after clean rebase: 88a75655ce6f4151f932df1d5204845edd8ea968.
- Installed extension cd81e83f91a552eb0138e58cb76312784a2988df is preserved;
  only its nested generic runtime is overridden.

## Execution and evidence

Both builds passed, followed by dry activation and host switch. Confctl health
checks passed 2/2. Existing configuration-base updates included Apache 2.4.69 and
Linux 6.18.55; the kernel came from the official cache, with no source build or
reboot. Host/helper logic and the user unit contents were unchanged by the pins.
Password metadata stayed unchanged. The public CA copy was republished normally
by existing host reconciliation; persisted credentials remained intact.

The guarded user-profile unit refused the active storage-redesign Codex thread
and retried at approximately 15 minute intervals. The final attempt began at
03:26:37 CEST on October 5 and completed at 03:27:57, exit 0, phase activated,
systemd inactive/dead with successful result. Total launcher elapsed time was
4 hours 23 minutes 55 seconds. The busy thread finished naturally. Full retry
and terminal evidence is retained in profile-switch-2.log and its result.

Read-only serving checks passed over authenticated TLS: six CSS/JS assets match
reviewed source bytes and the index uses current cache versions. Exact selected
package and actual portal executable match. Router, portal and Codex services
are healthy. Registration, own tmux identity, root/member identities and retained
model/effort/access/catalog settings are unchanged. No live draft or upload was
created; acceptance used the already-tested local desktop/mobile fixture.
See deployment-verification.md.

While waiting, shared master advanced only through coordination checkpoint
09da5e10. Rebase retained an identical pin patch and Nix evaluation yielded the
exact deployed package. Final comparisons were captured, then all four defaults
were fast-forwarded and pushed over SSH in order: codex-web, dev-workspace,
vpsfree-cz-configuration, workspace. integration-proof.json proves every exact
local/remote feature head is merged into its remote master. Temporary target
worktrees were removed; registered feature worktrees and branch refs remain.
Shared master and unrelated working files/index were preserved.

Setup refusals before package selection were resolved without bypassing checks:
configuration hooks needed the pinned gems; transient-unit PATH needed Git;
direct team idle checks needed the host-selected Codex home. During integration,
confctl's tools shell also required execution from its configuration repository,
rather than supplying its flake path from the workspace root. Hooks stayed active.
Reusable tooling notes are in notes/dev-workspace/2026-10-04-workspace-pin-tooling.md.

No migration or new API shape was introduced. Mechanical generated/dependency
pin commits qualify for the review skill exemption; unchanged application heads
passed independent final review. Supported workspace recovery remains forward-only.
