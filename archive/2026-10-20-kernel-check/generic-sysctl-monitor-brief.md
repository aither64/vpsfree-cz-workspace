# Generic sysctl v3 monitoring brief — focused passed, CI active

Current source: `846bb469505789ba0b2a405fa5905ba6d8253006`, base
`55c5046514d06fe9398a022c1622bdaae5228841`. Final all-four-lane review is
accepted with no findings; lead released the source/history gate. SSH publication
is verified at this exact head.

Actual batch: fresh native watcher `01a1634c-0553-7530-ba30-b19cfc2307d0`
(`gpt-6-luna`/`low`, danger-full-access/never confirmed in native context).
Old895 CI is terminal/cancelled and all old observer handles are accounted.
Focused wrapper PID `2229812` started 2026-10-22T11:08:31Z; runner entered
`system/sysctl` at 11:08:40Z and ended 11:14:33Z: exact exit 0, native
`expected_success`, eight examples passed. Durable receipts use the prefix
below. This was the sole focused v3 attempt; do not execute the launch again.
The same watcher now owns only existing automatic CI `39767770407` via one
`gh run watch --exit-status`; no terminal CI conclusion is claimed.

## Parent sequence after accepted review

1. Fresh explicit staging fetch and clean exact-head check; normal declared-env
   SSH publication using exact lease against published v2
   `895870606179f0c1170ad92a5fdc49eb2d6d1bbf`. Retain remote branch/base proof.
   Discover only already automatic workflows at v3; never start/rerun one.
2. Preserve available first failures and local native evidence for old895.
   Existing native watcher `01a16333-01c8-7451-afe4-b8c8c406a16b` owns CI
   `39764186292`. After replacement publication, cancel only if that run still
   references exact895 and is queued/running. Use one designated control caller;
   if the owner is blocked, one bounded parent status/cancel reconciliation is
   permitted, with no second observation loop. Account terminal metadata and
   all old handles/processes; obtain the no-active receipt before a new watcher.
3. Resolve the same retained utility policy at launch: digest
   `ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`,
   `gpt-6-luna`/`low`, fresh context, max concurrent one, matching native
   `verification_watcher-low.toml`. Installed `full_access` requires explicit
   `--sandbox danger-full-access --ask-for-approval never`. Record actual native
   identity/model/effort/execution policy. No model substitution.
4. Give one fresh watcher the selected focused command plus exact automatic CI
   IDs below. If a usable watcher cannot launch, visibly use the monitor skill's
   parent fallback. Reconnect errors alone do not establish that nothing ran.
   Check launch events, PID/start/exit files and owned process state before any
   bootstrap stop/fallback. Never launch a second copy of an existing attempt.

## Single fresh watcher assignment

Read `/home/aither/.codex/skills/dev-session-monitor/SKILL.md` and applicable
verification/repository instructions. No nested agents, source/tracking edits,
diagnosis, retries, merge, pins, deployment, host sysctl write or session lifecycle.

- Cwd: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsadminos`.
- Verify `dev-session current`, only the two session identity environment values,
  clean source and exact846bb head. Session is `2026-10-20-kernel-check`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`. Never dump full environment/auth values.
- Existing v3 automatic CI ID: `39767770407`. RSpec only if automatic.
  Observe exact IDs/head, not moving branch latest. No duplicate observer/workflow.
- Run once immediately after binding: `./test-runner.sh test system/sysctl`.
  There is no new full OS/cache prerequisite. Demonstrated exact local kernel
  `/nix/store/4k5kg0x1msvl4kffpr2g7cidpnwbnkhk-linux-6.12.113/bzImage` and
  initrd `/nix/store/i23y4g1swaix7mxqj9s8l1xjaaxiiwj6-initrd/initrd`, unchanged
  recipes and ordinary generated scripts discharge that uncertainty. Full guest
  closure equality is not claimed. Stop/escalate unexpected kernel-image builds.
- Emit timestamped start immediately before launch, then record PID/handle.
  Emit end/escalation immediately, independently of broad CI completion. Distinguish
  boot/shell readiness from executed guest service assertions. No quiet timeout.

Use a simple durable shell wrapper, not a monitoring service/framework. After
verified cwd/head, one launch can use the following ordinary detached wrapper
so loss of client/tool handle does not lose the actual selected-command exit.
Do not execute this snippet if its PID/start/exit/log indicates an existing run;
recover that run instead. Keep every path under this session.

```bash
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/generic-sysctl-focused-vm-846bb4695
nohup setsid bash -c '
  record="$1"
  printf "%s\n" "$$" > "$record.pid"
  date -u +"%Y-%m-%dT%H:%M:%SZ" > "$record.started"
  ./test-runner.sh test system/sysctl > "$record.log" 2>&1
  selected_status=$?
  printf "%s\n" "$selected_status" > "$record.exit.tmp"
  mv "$record.exit.tmp" "$record.exit"
  date -u +"%Y-%m-%dT%H:%M:%SZ" > "$record.ended"
  exit "$selected_status"
' sysctl-verification "$record" > "$record.wrapper.log" 2>&1 < /dev/null &
```

Retain ownership of the wrapper and runner until terminal. PID/start/exit files
and full log are independently accessible if a handle disappears. Do not kill
an active wrapper due to a reconnect or quiet output. For an authorized kernel
build escalation, interrupt only the identified owned runner, preserve evidence
and account its exit; do not relaunch it. Record any missing receipt honestly.

Preserve the native artifact directory reported by test-runner, including full
console, shell, machine, service and runner logs/config/result. Old88486/895
first-failure copies remain untouched. Report selected exit file content and
native conclusion separately, with head, start/end/elapsed and artifact paths.

Continue existing exact v3 CI independently after focused completion. Retain
full available first-failure logs/artifacts; report material observations with
observation timestamps. Never cancel current-head CI or infer green from a
local check. No need to await the broad pipeline for source handoff. Return raw
pass/fail/incomplete and every still-owned operation; parent owns diagnosis.
