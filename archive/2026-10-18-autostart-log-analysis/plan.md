# osctld autostart descriptor-limit race

## Latest scope decision

Osctld subsequently merged into remote staging at60f9ed1c under explicit user
direction. No deployment. The requested swap plan is superseded by confirmed
colleague branch fix/kernel-stability-20261018, which pins the repaired kernel
and adds large-swap tests. Stop our duplicate swap work; see
[confirmation](colleague-swap-confirmation.md). Original scope follows as history.

## Original goal and authorized endpoint

Implement the accepted osctld-only plan and deliver a tested, independently reviewed, published feature branch. User explicitly deferred swap and histfile, selected reviewed branch rather than rollout, then requested implementation. No default-branch integration, deployment, service restart or node reboot is authorized by this task.

## Scope and design

- Affected project: vpsadminos, based on refreshed origin/staging (d531fc90888e3eabf17889b0dff94c648866cea4 at setup).
- Architect0 owns design.md: require child descriptor cleanup and existing setup to complete before parent applies target prlimits and releases workload execution. Handle handshake failures without leaks/hangs and preserve existing FD/IO/socket/cgroup/identity semantics.
- Implementer0 owns SwitchUser source and deterministic real-fork specs, comments/docs, quick checks, source commits and follow-up fixes.
- Implementer1 owns one focused packaged-osctld VM regression and registration, quick evaluation and test commits/follow-up fixes.
- Source and VM files are independent. Serialize staging, commits, fetch/rebase, packaging metadata and publication; no broad start-error or retry redesign unless a demonstrated correctness dependency is accepted by lead.

## Acceptance and checks

- Controlled >1024 inherited descriptors plus target NOFILE=1024 reproduces old race and proves corrected cleanup-before-prlimits ordering.
- Child setup failure, parent prlimit failure and closed handshake must release peer, close owned FDs and reap only owned helper without hanging. Existing retained-FD, socket, duplex and IO/GC tests pass.
- Focused RSpec/lint/hooks and Nix evaluation pass; intended source/tests/docs are committed before mandatory independent final review of complete base-to-head history and diff.
- After review, one watcher-owned VM run proves packaged helper limit ordering, parallel container autostart, running state, console/exec and clean stop. Kernel stays unchanged/cached; stop unexpected kernel builds.
- Final feature branch is published with exact heads, review and verification evidence; no PR required, no merge.

## Compatibility and recovery

Private parent/child protocol within one daemon, no external API/schema/on-disk format changes or migrations. Existing container limits remain unchanged; no kernel changes or fleet-coordinated update. Rollback reads existing state but reintroduces the race. Future rollout should record CT intent/queue, use normal supported osctld update/restart, then retry only confirmed intended-running stopped CTs; avoid forced pool trigger. Rollout remains separate.

## Documentation and evidence

Operator/developer context and future rollout checklist live in design.md and state.md. Preserve prior timestamped investigation evidence. Add only useful lasting invariant comments/project documentation. Apply dev-session-documentation and dev-session-handoff skills. Session remains open.
