---
lifecycle: active
---

# Proactive swap removal from 6.12.113

Current phase: implementation preparation. User authorized implementing the final plan and vpsAdminOS staging integration after quick checks and independent review. No kernel builds/boot/runtime/full-CI wait are pre-merge gates.

## Phase checklist

- [x] Verify exact session identity/environment and retained Full-team roster.
- [x] Resolve .113 patch inventory and final user decisions.
- [ ] Refresh architect-owned design.md and commit substantive initial plan/state.
- [ ] Reconstruct/publish Linux feature head (implementer0).
- [ ] Clean DAMON options and retire experimental tooling (implementer1).
- [ ] Commit exact final .113 kernel pin/hash and pass quick checks (implementer1).
- [ ] Independent final review of committed complete deliverables (reviewer0).
- [ ] Merge reviewed OS branch into remote staging (lead/coordinator).
- [ ] Kernel build/boot/runtime: subsequent user staging validation, not run here.

## Ownership and repositories

Architect0 refreshing final brief. Implementer0 will own Linux worktree/source/history; implementer1 will own OS cleanup, technical docs, quick checks and final pin. Both are ready with saved workspace_write access; settings retained. Lead owns tracking, acceptance and coordinated integration; no application edits by lead. No feature worktrees registered yet.

OS baseline: 60f9ed1c153a734880e002b63d6ab7ed5fe87d0e (staging). Original .113 source: 11058eb4fe1cba30653e8e643546c13bc8bcd792. Upstream base: 7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e. Prior local-source gap was resolved by architect read-only HTTP/API inspection during planning; implementer must acquire exact source normally for execution. Partial-clone reads use GIT_NO_LAZY_FETCH=1 to avoid accidental lazy fetches.

## Final decisions and approval

- Latest 6.12.113 only; remove entire experiment including custom DAMON NUMA/quota controls.
- Retire experimental QEMU/tests/entry points; no legacy fixture support and no new normal-reclaim tests.
- No backward compatibility or rollback requirements: user confirms never deployed.
- Preserve all other kernel/ZFS pins and frozen outputs; upstream DAMON and unrelated product/safety patches remain.
- User: "I'd prefer if we could merge this after quick verification ... boot ... on staging nodes"; selected "staging (Recommended)" for vpsAdminOS merge target; subsequently "Implement the plan". Scope: vpsadminos refs/heads/staging only, new Linux feature publication. No existing Linux release/default ref rewrite, machine deployment or reboot approval.
- Mandatory final independent review remains required after exact committed deliverables and quick checks. Full CI may trigger but is not awaited. Build/boot/runtime acceptance remains pending for user.

## Verification and next action

No source changes or implementation checks yet. Initial root inspection confirms shared master, empty staged index, no declared root hook framework or pre-commit hook. Preserve all unrelated shared files/index. Next: finish brief + initial tracking commit, then assign both ready implementers.

## Documentation and session

See [plan.md](plan.md) and [design.md](design.md). Initial tracking commit pending. No lifecycle/cleanup action authorized; leave session open.
