# 2026-10-29-workspace-resource-monitoring

## Goal

I'd like to extend dev-workspace portal with system resources. It could monitor machine cpu / memory / disk usage. It'd be cool if we could see how much each session is using -- we'd need to scope sessions to cgroups, I suppose. It'd be ok if it worked only on new sessions. so e.g. in the Settings tab, I could see resource usage of the current session... and we could have some compact global counters with system resource usage which could be expanded on click.

Most importantly, I'd like to handle issue with limited disk space. When usage of the workspace filesystem would get over 90 %, all active sessions with medium to large disk usage should be sent an authoritative message to pause work, clean up data it no longer needs, e.g. temporary files, superseded builds, disk images, etc., then resume work. idle sessions would return to being idle. this would have to be rate-limited, so that we don't spam sessions if they are unable to free space.

also count session disk usage only in regular intervals, some sessions have a lot of files and we don't want unnecessary IO.

suggest a solution.

## Affected repositories

- `dev-workspace`: expected owner of host collection, session accounting,
  disk-pressure orchestration, and portal presentation. Architect to verify
  whether any shared `codex-web` interface changes are necessary.
- Current authorization: implement a disposable demonstration and complete the
  design, per the user's latest instruction. No production deployment, default
  branch integration, or session lifecycle action is requested.

## Approach

- Design owner: retained `architect0` (Astra/xhigh, workspace-write).
- Inspect current runtime and propose the smallest compatible extension.
- Separate cheap host/process samples from periodic session filesystem walks.
- Treat disk pressure, message delivery and resuming prior activity as explicit
  design responsibilities; preserve existing ownership and recovery contracts.
- Save proposed design and evidence in [design.md](design.md).
- Demonstrate one stock host Codex App Server with per-session container
  `exec-server` environments. Keep one auth owner; do not patch/rebuild Codex,
  copy credentials, or use the live conversation service for test fixtures.
- Demo uses a synthetic local model backend and private native state where
  possible; real command/edit routing, isolation, shared Nix daemon/store and
  shared bare Git/private worktrees are acceptance targets.

## Decisions

- Per-session cgroup metrics may be available only for newly launched sessions.
- Existing sessions should still be eligible for path-based disk accounting.
- Cleanup instructions must never confer archive/delete/stop authority or permit
  deletion of another session's files, active recovery data or shared store data.
- User accepted all runnable sessions receiving pressure cleanup, with measured
  >=5 GiB used for priority rather than eligibility; hourly minimum cooldown,
  6 h/24 h backoff after no reclaim. Busy sessions resume; idle return idle.
- Shared bare repositories and shared host Nix daemon/store are requirements.
- Preferred candidate is one host App Server/login plus a stock executor inside
  each session container. Native environment selection is experimental and
  must fail closed. Host App Server and shared-service costs stay shared.
- Proposed policy defaults remain recommendations for the user's assessment,
  rather than already implemented behavior.

## Compatibility and deployment

- Assess shared App Server/terminal process boundaries, delegated build daemons,
  mixed old/new sessions, additive state and API fields, and rollback behavior.
- Disposable fixture creation/teardown is authorized as part of the demo;
  no live session/package migration or deployment is authorized.

## Documentation

- Readers: user assessing the proposal and future implementers.
- This session's design is planning evidence. Product behavior and operations
  documentation will belong in the runtime repository if implementation proceeds.

## Testing plan

- Demonstration: host prerequisites, actual stock protocol, container execution,
  file edits, missing-executor refusal, team/fork/resume selection, shared Git
  and host Nix, volume allocation and reclamation where available.
- Commit demo and pass focused quick checks before mandatory independent final
  review; run long/uncertain native/container integration only afterward using
  a fresh verification watcher. Preserve limitations and raw evidence honestly.
