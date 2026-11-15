# Runtime evidence for failed archival

Collected read-only on 2026-11-11, approximately 18:39–18:46 UTC, by
`implementer0` for package B. No archive retry, service stop, process kill,
lifecycle repair, code change, commit or test suite was performed.

## Conclusions

- Both browser archive requests failed in `lead_fixing_blockers`, before the
  archival executor or registered-service cleanup began. Neither session has an
  archive journal, archive-cleanup sidecar or services-cleanup prelude.
- The preview service was registered correctly. At 18:44:31 UTC the public service
  inventory reported 12 running registered services and `cleanup: null`. The
  listener on port 4567 is one of those exact registered systemd services.
- Preview preparation repeatedly encountered a monitor external-effects fence.
  Its terminal report already says the CI run ended and no operation-owned work
  remained; a fresh GitHub read confirms that exact run/job completed/cancelled.
  Source correlation by architect0 identifies the nonempty `stillRunning` string
  as the fence trigger, even though its text begins `none;`.
- The release request has remained failed at attempt 1 since 2026-11-03. It hit a
  session-lock error while preparing a lead repair, rather than a failed archive
  worker or tracking-Git retry. The exact lock holder at that historical instant
  is unknown.

## Identity and installed package

`dev-session current` printed `2026-11-11-session-archival-failures`; both
`DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` matched the trusted conversation
binding and `/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster
confirmed `implementer0` and `architect0`, their assigned purposes and saved
workspace-write access.

- Current profile: `/home/aither/.local/state/dev-workspaces/profile-231-link`.
- Installed package: `/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`.
- Exact derivation, supplied by architect0:
  `/nix/store/laq7gxhg6cv91cyv873fskhcl9sx07xf-dev-workspace-0.2.0.drv`.
- Its exact source, established by architect0 from derivation `env.src`:
  `/nix/store/pfnyfqh3z37g4dpqq3pw04qhdgg98d55-source`.

The immutable source path identifies the installed contents. Canonical repository
HEAD differs; this report does not claim a Git revision for the installed source
or identify the historical package used on November 3.

## Authoritative browser receipts

Read the two matching records only from
`~/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/lifecycle-operations.json`.

| Session | Start (UTC) | Failure (UTC) | Receipt state |
| --- | --- | --- | --- |
| `2026-11-10-status-theme-responsive-preview` | `2026-11-11T13:27:32.559562629Z` | `2026-11-11T13:30:18.818791299Z` | `archive`, `failed`, `lead_fixing_blockers`, attempt 1 |
| `2026-11-02-haveapi-vpsadmin-release` | `2026-11-03T14:06:34.589783134Z` | `2026-11-03T14:10:17.035836756Z` | `archive`, `failed`, `lead_fixing_blockers`, attempt 1 |

Preview receipt ID:
`2599c6179af844e0d4ba3b6edd00bd5b475edf18caabd4587ec74d7a97429f14`.
Release receipt ID:
`ea0c9a4c926561e2c6332b0067524685558fc69fa0d8434db6885a7fa60f1e75`.

The matching files in the same directory's `archive-preparations/` retain:

- Preview: failed, `round: 3`, `noProgress: 3`, five of six checks passed,
  readiness stage 2, one blocker. Rounds 0–3 each retained five passed checks and
  one blocker. The blocker is `conversation`: monitor
  `7648d2bf-a2b9-493e-8bcf-c1a69d8fc1a0` “retains external work; record exact
  evidence with monitor resolve”. Final error: “Archive cleanup made no
  measurable progress in three repair cycles. Review the lead conversation and
  blockers before retrying.” Despite the wording, no service cleanup began.
- Release: failed, `round: 1`, `noProgress: 0`, five of six checks passed,
  readiness stage 1, total `blockerCount: 2712`. Final error: `session is
  changing: resource temporarily unavailable`. Its accepted lead-repair delivery
  receipt has turn `01a1a1bb-c322-7b82-ab5f-02728550dae7`, message
  `bcf2a9ad-2016-0b45-a4c1-0cf2936ed9a8`, `steered: false`; no transcript was
  inspected. The only saved check-history entry is round 0 with 2712 blockers.

The release metadata retains 128 blocker examples, all `unmanaged_entry`, under
`worktrees/2026-11-02-haveapi-vpsadmin-release/haveapi-rust-source/`: one
`.editorconfig` and 127 `.git/` entries. This is repository-like content beside
managed checkouts. Its author, tracked/untracked status and whether it originated
in automatic repair are **unknown from this metadata**. No peer worktree was
traversed. The count describes the recorded check, not a fresh filesystem scan.

## Preview monitor: finished CI with a retained fence

Read only the exact operation JSON:
`~/.local/state/dev-workspaces/monitor-operations/8a2a555cb2f65b336ae8727305f7aaaac277dbdf66f266adde8c8af18bf12836/7648d2bf-a2b9-493e-8bcf-c1a69d8fc1a0.json`.

- Created `2026-11-10T12:32:05.95037688Z`.
- Source: GitHub Actions, `vpsfreecz/vpsf-status`, `Integration Tests`, run
  `42816255766`, attempt 1, commit `9958b0375eb4d7c655cdc505a76e46ec95301cd4`.
- Terminal report at `2026-11-10T13:59:01.120093832Z`: slot `terminal`, outcome
  `failed`, exit 1, conclusion `cancelled`, elapsed 5,270,000 ms.
- Exact `stillRunning`: `none; observation session 68962 exited 1; GitHub run
  42816255766 attempt 1 is terminal completed/cancelled`.
- Reported evidence identifies job `129830005698`, completed at
  `2026-11-10T13:57:50Z`, and explicitly says no other operation-owned work
  remained running. The utility launch terminated at
  `2026-11-10T13:59:11.457938662Z`, termination `completed`.
- No resolution field is present. This is a historical terminal report;
  native local tool-session `68962` was not independently reattached or probed.

At approximately 18:44 UTC, `gh run view 42816255766 --repo
vpsfreecz/vpsf-status --json databaseId,status,conclusion,headSha,updatedAt,jobs,url,workflowName`
independently returned the same exact head and run, `completed` / `cancelled`.
Its sole job `129830005698` was also completed/cancelled, started
`2026-11-10T12:30:00Z`, completed `2026-11-10T13:57:50Z`.
[Exact run](https://github.com/vpsfreecz/vpsf-status/actions/runs/42816255766).

**Inference supported by source correlation:** this fence is a report-format
classification defect, not evidence that this CI job is still running.
Architect0 traced `monitoroperation/service.go:252`: incomplete outcome **or any nonempty
`StillRunning`** retains the external-effects fence. Terminal failed reports may
legally carry the nonempty field. This report does not authorize clearing it or
infer completion of arbitrary unknown external commands.

## Registered service and port 4567

The first-registration marker
`worktrees/.locks/2026-11-10-status-theme-responsive-preview.services-registration.json`
is `ready`, created `2026-11-10T12:21:56.384050Z`, registry UUID
`8302fcd9-f380-4170-876e-ffb1c9f4e64f`. The exact private registry is
`~/.local/state/dev-workspaces/session-services/vpsfree.cz-8a2a555cb2f65b33/2026-11-10-status-theme-responsive-preview.json`.

`dev-session service list 2026-11-10-status-theme-responsive-preview --as-is
--json` observed at `2026-11-11T18:44:31.318100Z`: `registered: true`,
`count: 12`, `countKnown: true`, every current resource `running`,
`cleanup: null`; nine older resources have retained retirement history.

For the user-reported listener, independent socket/process/systemd reads agree:

- `ss -ltnp '( sport = :4567 )'`: listening on `*:4567`, PID `1129661`.
- Unit `workspace-session-da1562b3-b0c8-4d7b-8ab8-0ab2e84e62b0.service` is
  active/running with `MainPID=1129661`; started `2026-11-11T07:17:40Z`.
- Registry label `status-preview-4567-exact-plain-colors`; invocation ID
  `5bfaa3aee2104fa7aa44372893c8b2a1` agrees with systemd.
- `/proc/1129661/cgroup`, systemd ControlGroup and registry agree on
  `/user.slice/user-1000.slice/user@1000.service/app.slice/workspace-session-da1562b3-b0c8-4d7b-8ab8-0ab2e84e62b0.service`.
- Executable is the session tracking file `vpsf-status-preview-2d448fd`; arguments
  select `0.0.0.0:4567`, data directory `preview-data-7fa5afc`, scenario `mixed`.
  No executable or data contents were read.

Thus missing registration does not explain this surviving service. The archive
request failed before reaching registered cleanup.

## Retry and journal boundaries

For **both exact slugs**, `ls`/file existence checks found none of
`worktrees/.locks/SLUG.archive.json`, `SLUG.archive-cleanup.json`, or
`SLUG.services-cleanup.json`. Exact-slug filtering of systemd archive units found
no matching browser archive worker. `dev-session tracking-sync --status --slug
SLUG --json` returned `[]` for each.

At approximately 18:43 UTC both existing user timers were active/waiting:

- `workspace-auto-archive@vpsfree-cz.timer`, last trigger 18:00:46 UTC;
- `workspace-tracking-sync@vpsfree-cz.timer`, last trigger 18:43:04 UTC.

Their unit definitions call `run-auto-archive` and `run-tracking-sync`,
respectively. Presence of these timers does **not** prove failed explicit
preparation is enrolled in either worker. Architect0's source trace establishes
that failed preparation is excluded from `active()`/restart continuation, while
the fail-fast shared runtime lock error is terminalized. That accounts for the
unchanged release receipt since November 3. No evidence identifies a crashed
archive worker or pending tracking commit for either request.

Bounded portal-journal reads around each receipt's start/failure window returned
routine automatic **turn** retry observation/admission-unavailable messages, not
an archive-executor failure. Those messages concern a different retry mechanism;
they do not establish archival retries. Auto-archive logs can contain multi-session
snapshots, so no unrelated session content is retained here. Durable exact-session
receipts are the decisive evidence.

Relevant installed documentation read: `docs/session-archive-recovery.md`
(readiness, journal and registered-service sections), and `docs/dev-sessions.md`
(monitor, temporary-service and archive sections). They document readiness before
shutdown, cleanup before supporting-file removal, and retrying the original
accepted operation without deleting receipts. Proposed source changes and recovery
acceptance are owned by architect0's design brief (`design.md`, pending when this
runtime evidence was completed).

## Reproduction and limits

All commands ran from `/home/aither/workspace/ai/vpsfree.cz`. The main independent
reads were `dev-session current`, own `dev-session team list ... --as-is`, `jq`
projections of the exact records above, `dev-session service list`, `ss`,
`systemctl --user show` for the exact service/timers, `/proc/1129661/{cgroup,exe,cwd}`,
`gh run view`, exact-slug lock-file checks and per-slug tracking-sync status.
Log reads used only the portal/auto-archive/tracking-sync units, the two failure
windows or relevant slugs; no peer transcript/team/worktree content was inspected.

Remaining unknowns: the November 3 lock holder and historical package revision;
the provenance of unmanaged repository-like content; independent present liveness
of the historical local observation handle. These do not invalidate the proven
preparation failure boundary or the currently terminal CI status. No live retry
or cleanup was attempted, so successful recovery is a proposal, not verified work.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).
