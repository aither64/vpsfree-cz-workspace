---
lifecycle: active
---

# 2026-10-18-portal-message-recovery

## Status

- Phase: implementation complete and quick checks passed; preparing commits, matching pins and independent review.
- Portal code, documentation and regression tests are implemented; no deployment or integration yet.
- Integration authorized for dev-workspace/master, workspace/master and vpsfree-cz-configuration/master after successful deployment verification.

## Phase checklist

- [x] Investigate behavior and settle user choices.
- [x] Implement and complete quick checks.
- [ ] Commit intended deliverable and independent final review.
- [ ] Longer checks and CI.
- [ ] Deploy and verify aitherdev.
- [ ] Integrate exact final heads and complete handoff.

## Next actions

Commit initial tracking, register isolated worktrees and implement from the
lead-owned design brief. No session closure or archival is authorized.

## Documentation

## Repositories

## Commands run

## Results

Initial inspection: exact-text send matching leaves earlier unknown attempts
unresolved after revised wording. Index payload warnings bypass the shared
notice controller. Approximate timestamps use turn timing while asynchronous
rollout metadata supplies exact item times.

## Open questions

## Cleanup

## Implementation checkpoint

- Worktrees: worktrees/2026-10-18-portal-message-recovery/{dev-workspace,workspace,vpsfree-cz-configuration}; branches use the same slug.
- Source base: dev-workspace 705301228f726bcc9c5e0b516abc03f6f6c995cf; configuration base 30a20d0ea78afb9854be0845b68a1974ec069b2d. Workspace helper started at then-remote master; rebase onto current shared master before review.
- Quick checks: Nix Node syntax and Go tests TestIndexStatusDistinguishesColdLoadingFromRefreshFailure and TestShippedBrowserClientMatchesSessionAPI passed (1.081s). The latter includes actual shared refresh-controller fake-clock contracts.
- Test environment: set DEV_WORKSPACES_CODEX_PROVIDERS to an absent path beneath Nix's TMPDIR; otherwise /etc/dev-workspaces/codex-providers.json is discovered and unnamed test workspaces fail provider-state identity validation. Unsetting the variable retains that host default and is insufficient.
- Configuration worktree post-checkout initially lacked hook gems; retrying native registration from its Nix development shell succeeded. Hooks remain enabled.
- Timestamp grace uses one shared notice for the current thread's metadata-loading episode, retaining exact times by stable entry identity. This avoids a timer/listener for every transcript item.

## Native coordination ownership handoff

The external conversation continues to own implementation and operations. Native
coordinator admission requires a retained conversation, so normal startup will
create an idle native owner from the committed tracking snapshot. Its initial
instruction forbids edits, mutations, delegation and session closure. This
checkpoint is the required genuine coordination-identity handoff, not a routine
per-command tracking commit. No roster member or implementation assignment is
being added.

Final portal head before review: 7ec8bf528e0030c9df3a43d8aed19d5e1ada3474.
Quick checks passed again after history consolidation (1.042s). The source has
four focused commits, with each behavior and the combined browser regression
separate. There are no migrations. Configuration pin iterations are consolidated
to one generated commit; workspace uses one nested-runtime pin commit.

The stale source CI cancellation request returned HTTP 403 (token cannot cancel
Actions runs). Do not repeat that unauthorized request or cancel current-head
runs. Aitherdev is reserved by 2026-10-18-provider-switch-redesign; prepare and
verify independently, then queue through the coordinator without bypassing it.
