# Verification result

Exact tested revisions: workspace `1deb88301418722ed1aebeaa2bebafd9b2e007d8`; runtime `f05f50eed6dbfa2794502653176f0bbbbf20f1fa`; configuration `f9a6996153daec9e20a3feb58e05981b5907ef7b`.

## Command 1

- Working directory: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/workspace`
- Command: `nix build --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-reboot-recovery-fix/candidate-profile --print-build-logs .#packages.x86_64-linux.default`
- Started: 2026-10-30T22:26:37Z; finished: 2026-10-30T22:37:03Z
- Exit status: 0; elapsed: 626 seconds
- Complete output: [verify-1.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-reboot-recovery-fix/verify-1.log)

## Command 2

- Working directory: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/dev-workspace`
- Command: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-recovery-boot`
- Started: 2026-10-30T22:37:03Z; finished: 2026-10-30T22:52:06Z
- Exit status: 0; elapsed: 903 seconds
- Complete output: [verify-2.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-reboot-recovery-fix/verify-2.log)
- Bounded evidence: the full log contains `AssertionError` traces in VM scenarios and a provider `403`; the Nix command nevertheless exited 0.

## Command 3

- Working directory: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/vpsfree-cz-configuration`
- Command: `nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev`
- Started: 2026-10-30T22:53:46Z; finished: 2026-10-30T22:54:55Z
- Exit status: 0; elapsed: 69 seconds
- Complete output: [verify-3.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-reboot-recovery-fix/verify-3.log)

## Command 4

- Working directory: `/home/aither/workspace/ai/vpsfree.cz`
- Command: `gh run watch 41137347714 --repo aither64/dev-workspace --exit-status --interval 30`
- Started: 2026-10-30T22:54:58Z; finished: 2026-10-30T22:54:59Z
- Exit status: 0; elapsed: 1 second
- Complete output: [verify-4.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-reboot-recovery-fix/verify-4.log)
- Run conclusion: `success`; read-only metadata confirms `headSha` `f05f50eed6dbfa2794502653176f0bbbbf20f1fa`, status `completed`.
