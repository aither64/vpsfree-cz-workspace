# 2026-10-17-aitherdev-disk-usage

## Goal

Identify what is consuming disk space on aitherdev and attribute large consumers
to Unix users, development sessions, projects, or services where evidence allows.
The user requested diagnosis; deletion, garbage collection, session lifecycle
cleanup, and service interruption are outside this investigation.

## Affected repositories

No application repository changes are planned. The coordination workspace owns
this investigation's plan, state, and evidence.

## Approach

Measure filesystem capacity, allocated directory sizes, large files, Nix store
retention, temporary artifacts, caches, logs, and development-session storage.
Trace the largest consumers using metadata and process ownership. Do not read
credentials or expose full process command lines or unrelated private content.

## Decisions

Use a separate coordination-only initiative because `dev-session current` found
no conversation-owned session and no environment binding was present. The
initiative was created with `--no-codex --no-attach` to avoid starting another
coding agent during a disk-pressure investigation. It has no retained team.

## Compatibility and deployment

Read-only host inspection changes no persistent formats, schemas, protocols,
APIs, configuration, package generations, or deployment order. Other sessions'
records, worktrees, processes, and GC roots must remain untouched. Root-only
directories may limit attribution; report that explicitly if access is absent.

## Documentation

Keep measured findings in this initiative's state and linked evidence. The
audience is the host operator. Application documentation changes are unnecessary
for a host-storage inventory.

## Testing plan

Cross-check `df` with allocated-block directory measurements, distinguish sparse
file apparent size, avoid double-counting filesystem mounts and hard links, and
record measurement time. These are diagnostic reads, not builds or tests. No
independent change review is required for investigation and tracking alone.
