---
lifecycle: active
---

# Message delivery reliability

Implementation and quick checks are complete. Final pins, independent review,
packaged/native verification and deployment remain. No merge approval exists.

- [x] Reproduce the deadline race and establish the pre-transmission boundary.
- [x] Implement transactional storage, recovery, browser retries and plan lifetime.
- [x] Pass library Go/browser and focused portal/archive/profile checks.
- [ ] Finish matching runtime/configuration/workspace pins and publish branches.
- [ ] Independent final branch review and resolve findings.
- [ ] Packaged and applicable native/lifecycle verification.
- [ ] Claim aitherdev, activate, verify continuity and delivery.
- [ ] Revalidate and recover the exact stuck attempt without duplicate submission.
- [ ] Integrate only after explicit repository/target approval; release machine
  ownership only under the installed retention policy.

## Ownership and worktrees

Tracking was enabled by the user after the initial no-tracking implementation.
The failed `dev-session start --no-codex` performed no tracking creation: existing
feature worktrees required an explicit manifest. These new records describe the
current work directly. `CODEX_THREAD_ID` and native `thread/read` independently
identify current conversation `01a17206-ed6f-78b3-b410-c7d6015b6777`, its workspace
CWD and the registered vpsfree-cz socket. No conversation or roster is replaced.

All four worktrees use branch `2026-10-25-message-delivery-reliability` under
`worktrees/2026-10-25-message-delivery-reliability/`. The shared workspace remains
on master and contains unrelated changes that must be preserved.

| Repository | Initial base | Current status |
| --- | --- | --- |
| codex-web | 872c7ad3962f9fa9b17358244e27f3e3fac59fc5 | Published final library 7c84dc4d29566d99d7935627920dd653565aa379 |
| dev-workspace | 10bb047513c82d1310e8fcaa797e8772f948dd8a | Three logical commits; final dependency refresh being consolidated |
| vpsfree-cz-configuration | d12a77374b18e15fe7600f95307114e2e1882828 | Exact runtime channel update pending |
| workspace | b1b86b2b8 | Nested runtime pin pending; rebase before final review |

## Verification and evidence

Full library Go tests passed (codex about 22 seconds); browser retry/generic
contracts passed. Focused migration tests passed after atomic schema bootstrap.
Portal checks against the published library passed for plan dispatch, service
lifetime, typed outcomes, archive recovery, shipped browser assets and versions.
Ruby compatibility checks passed previously (2 runs, 34 assertions); final repeat
is in progress. Native Codex remains 0.163.0.

Logs are currently under `/tmp/message-delivery-reliability-2026-10-25/`; retain
compact evidence in this directory before handoff. Initial failures were diagnosed:
Unix socket fixture path length (set TMPDIR inside Nix), a missing TryLock method
(implemented), typed uncertainty expectations (updated), missing scheduler asset
embedding (fixed), and dependency timestamp timezone (corrected to UTC).

Final vendor hash for runtime:
`sha256-S1+JRkfIWOqNf9wS73W1vJPMzUMhQ1UnWZtQzaXKCO0=`.
Library vendor hash: `sha256-/NKkY+lT/h0ctIdTIkPgEn214M10xd95unGGNgyfK34=`.

The selected profile remains
`/nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0`.
No live migration, state repair or deployment has occurred. See [plan](plan.md)
and [design](design.md) for compatibility, acceptance and original recovery identity.
