# Postactivation acceptance checklist

Prepared 2026-10-22 for the lead. This is a source-backed execution plan, not an
acceptance receipt. No service, HTTP, native, provider or browser probe was run
while preparing it. Identity/guidance reads and selected-profile symlink
inspection were the only live setup observations. Do not use other sessions as
fixtures. Lead owns operations, required writing and user acceptance.

Scope: installed predecessor
`/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0`, final B
`d819ad044ef7fcc7bb4a111dc7676fe251383249`, W
`ebf6ab35c7754f9ac2e5474959259fdcef24a7c8`, A
`c1f415ad5602c23e6443cced73cb59267a796f05`, C
`81d0e68c52762d3804e00e4c4ef99a421bafc05f`. These identities supplement the
[build brief](verification-build-brief.md) and
[generation/health receipts](confctl-generation-receipts.md); do not replace the
exact completed system/profile artifact receipts. The predecessor's installed
host script and service units support the common service/socket checks below.
Its runtime contract has no `turnRetryStateSchema`; retry UI/API acceptance is
for the final package only, not a predecessor prerequisite.

## Read-only checks for the lead after authorized activation

Run as the owning user on aitherdev. Use the existing registered `vpsfree-cz`
workspace. Default runtime paths below come from the selected host command;
if deployment has an explicit runtime override, use its retained receipt instead
of guessing a new path.

```sh
SLUG=2026-10-22-codex-thread-retries
WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
WS_NAME=vpsfree-cz
RUNTIME="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}/dev-workspaces/$WS_NAME"
CANONICAL=vpsfree-cz.workspace.aitherdev.int.vpsfree.cz
ALIAS=vpsfree-cz-workspace.aitherdev.int.vpsfree.cz

readlink -f /home/aither/.local/state/dev-workspaces/profile
systemctl --user show --no-pager \
  workspace-router.service workspace-coordinator.service \
  "workspace-portal@$WS_NAME.service" "workspace-codex@$WS_NAME.service" \
  "workspace-tmux@$WS_NAME.service" \
  -p Id -p ActiveState -p SubState -p MainPID -p ExecMainStartTimestampMonotonic \
  -p ExecMainStatus -p NRestarts
stat -Lc '%n device=%d inode=%i ctime=%z' \
  "$RUNTIME/app-server.sock" "$RUNTIME/tmux.sock"
```

Require the selected profile to equal the built candidate receipt. All five
services should be active/running with successful main status. Compare native
Codex and tmux PID/start-time/socket identities with the lead's preactivation
receipt; they should survive this switch when the unchanged native launch tuple
selects live activation. Portal/router/coordinator restarts are expected. A PID
alone is insufficient identity proof. A mismatch needs diagnosis, not automatic
resume/restart. Do not print process arguments/environments or terminal content.

The following bounded GETs test the local portal and routing only. Local sockets
deliberately bypass nginx authentication/TLS and cannot establish external access:

```sh
curl --fail --silent --show-error --max-time 10 \
  --unix-socket "$RUNTIME/portal.sock" http://localhost/healthz
curl --fail --silent --show-error --max-time 10 \
  --unix-socket /run/dev-workspaces/router.sock \
  -H "Host: $CANONICAL" http://localhost/healthz
curl --silent --show-error --max-time 10 --output /dev/null --dump-header - \
  --unix-socket /run/dev-workspaces/router.sock \
  -H "Host: $ALIAS" "http://localhost/$SLUG/"
```

The first two must return HTTP 200 with `{"ok":true}`. The alias must return
308 with `Location: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/`.
`/healthz` is unconditional once the handler is serving: it does **not** prove
native connection, naming, provider availability or controller admission.

Coordinator observation is supported without advancing jobs or acquiring claims:

```sh
DEV_SESSION_SLUG="$SLUG" DEV_SESSION_WORKSPACE="$WORKSPACE" \
  dev-session coordination status "$SLUG" --as-is --json --portal
```

Use only this session-scoped status, or authenticated
`GET /api/sessions/2026-10-22-codex-thread-retries/coordination`.
Require valid status plus active coordinator service; a read of durable status
alone does not prove worker progress. Preserve the exact held machine claim and
ordinary uncertainty/forward-recovery rules. Do not exercise acquire, release,
reconcile, recover or lifecycle commands as health probes.

## This session's conversation continuity

```sh
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries
dev-session current
DEV_SESSION_SLUG="$SLUG" DEV_SESSION_WORKSPACE="$WORKSPACE" \
  dev-session team list "$SLUG" --as-is |
  jq '{rootThreadId:.roster.rootThreadId,
       members:[.roster.members[] | {address,threadId,state,model,reasoningEffort,access}]}'
tmux -S "$RUNTIME/tmux.sock" display-message -p -t "=$SLUG" \
  '#{session_id} #{session_name} #{@dev_session_codex_thread} #{@dev_session_codex_version} #{@dev_session_codex_pane}'
```

Compare root/member thread IDs and retained model/effort/access with the
preactivation receipt, and tmux session/pane IDs with this session's retained
authority. No attach, pane input, capture-pane, session start or recovery is
needed. Roster `ready` is retained identity, not proof of live native activity.

Supported scoped GETs, available via existing authenticated browser or the
owning user's local portal socket:

| Read | Meaning / expected evidence |
| --- | --- |
| `/api/sessions/2026-10-22-codex-thread-retries/team` | Same retained root/member identities/settings; do not publish the returned instructions. |
| `/api/sessions/2026-10-22-codex-thread-retries/team-stats` | Per-member snapshot and state; require matching thread IDs and fresh observations. Stale/refreshing/missing snapshots are incomplete evidence. |
| `/codex/conversations/2026-10-22-codex-thread-retries/activity` | Root activity metadata, including thread/current-turn ID, latest-turn status and freshness. |
| `/codex/conversations/2026-10-22-codex-thread-retries/thread/page` | Current root history page; verify retained history visually without exporting prompts. |
| `/codex/conversations/2026-10-22-codex-thread-retries~ADDRESS/activity` and `/thread/page` | Same for an exact ready retained address from this roster; never substitute a native child. |

For a metadata-only receipt, for example:

```sh
curl --fail --silent --show-error --max-time 15 \
  --unix-socket "$RUNTIME/portal.sock" \
  "http://localhost/codex/conversations/$SLUG/activity" |
  jq '{threadId,currentTurnId,latestTurnStatus,currentState,observedAtMs,stale,refreshing}'
```

These reads may refresh observation caches; they do not send a model turn or
activate a cold conversation. The existing session is doing real work, so turn
completion/new authorized input can legitimately advance the latest turn during
the switch. Correlate such changes with existing work instead of requiring the
latest turn to remain fixed. Empty/cold/stopped/unknown state is not repaired for
acceptance. Conversation rendering alone does not prove active execution or
absence of an unmanaged native writer.

## Authenticated browser and naming boundary

Use the lead/user's already authenticated browser at:

- Canonical: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
- Alias: https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

Verify TLS trust, successful existing Basic Auth, alias redirect to canonical,
loaded scripts/styles, conversation reconnect and the same root/team history.
Select a retained member through the existing selector (`?member=ADDRESS`).
An unauthenticated 401/redirect or local-socket success is not authenticated UI
acceptance. Do not read password/htpasswd/token/key files, put credentials in
commands, copy auth headers or create another credential. This architect has no
browser/computer tool attached; web-search and Sites tools are not authenticated
portal inspection. Browser acceptance therefore remains with the lead/user.

Naming has no dedicated readiness endpoint in the inspected interface. The
portal starts a separate pinned child under its service, with a private
`$RUNTIME/naming-*/app.sock`; the ordinary `app-server.sock` is not its endpoint.
A filesystem-only infrastructure observation is:

```sh
find "$RUNTIME" -maxdepth 2 -type s -path "$RUNTIME/naming-*/app.sock" -print
```

An existing socket is not proof of a live listener, valid provider authentication
or a successful naming result. There is no source-backed model-free command here
that certifies end-to-end naming. Record this limitation and retain the existing
isolated naming test evidence. Do not create a session, submit naming input, read
naming process arguments or contact its provider for this checklist. Naming
failure's documented neutral-name fallback is distinct from naming readiness.

## Retry observations and acceptance limits

Final B/A supports these exact routes for the root ID `$SLUG` or a ready member
ID `$SLUG~ADDRESS`:

| Interface | Classification |
| --- | --- |
| `GET /codex/conversations/ID/retry` | Read-only status; safe for later lead observation. |
| `POST /codex/conversations/ID/retry/enabled`, body `{"enabled":false}` or `true` | Durable preference mutation; **not** authorized as a live acceptance probe here. |
| `POST /codex/conversations/ID/retry/cancel`, body `{}` | Durable cancellation mutation; **not** authorized here. |

```sh
curl --fail --silent --show-error --max-time 15 \
  --unix-socket "$RUNTIME/portal.sock" \
  "http://localhost/codex/conversations/$SLUG/retry" |
  jq '{enabled,class,phase,attempt,nextAttemptAtMs,serverNowMs,cyberUsed,cyberLimit,reason}'
```

- In the root and ready retained-member conversations, verify **Auto retry** is
  visible and checked by default unless an existing persisted opt-out applies.
  Native children are outside scope. A first GET with no record returns default
  enabled but blocked/admission-held; it does not enroll or prove a durable
  enrollment watermark. The background controller owns enrollment.
- Observe current status/reason and any naturally occurring countdown against
  `serverNowMs`/`nextAttemptAtMs`; check **Cancel retry** visibility without
  clicking it. An idle conversation cannot demonstrate countdown behavior.
  Do not induce a capacity/cybersecurity error or submit another task.
- Old-failure exclusion is primarily covered by the reviewed state/controller
  tests and successful isolated native campaign. The public status does not
  expose the private baseline watermark. If this session already has a failed
  preactivation turn, correlate its retained turn/history with the absence of an
  automatic continuation after enrollment; no such case means live exclusion
  remains unexercised. Do not infer proof from a checked checkbox alone.
- Opt-out persistence, cancel races, restart reconciliation, retry timing and
  quota are synthetic/fixture evidence until specifically exercised under
  separate authorization. Preserve native run 4 and full-test receipts; do not
  repeat their campaign against this registered workspace. A persisted existing
  opt-out can be observed without toggling. Refreshing the page is a read; changing
  settings, clicking Send/Stop/Resume/Cancel or toggling retry is a mutation.
- Ask the user to accept the observed UI and behavior on the exact deployed
  aitherdev environment. Tests, health receipts and an engineer's visual check
  do not substitute for that acceptance. Keep the machine held until integrated
  feature lineage, user acceptance and explicit release direction all exist.

## Source authority

Line references are to frozen B/A/C above; links are immutable:

- [B host service configuration/status/runtime paths](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/libexec/workspace-host#L1285), lines 1285–1313 and 3318–3326; installed predecessor `.workspace-host-wrapped` has the same service names/status interface and `instance_runtime` at3305.
- [B router](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/cmd/workspace-portal/router.go#L84), exact-host route/308 redirect; [B health](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/internal/web/server.go#L915).
- [B scoped coordinator GET](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/internal/web/coordination.go#L14); [B team reads](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/internal/web/team_stats.go#L20); [B conversation IDs](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/internal/web/member_conversation.go#L18).
- [B naming child](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/cmd/workspace-portal/naming_runtime.go#L20) and [authoritative naming/fallback contract](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/docs/session-preparations.md#naming-and-reservation). The shorter portal guide's older retry-naming prose is not evidence that naming failure blocks ordinary creation.
- [C canonical hostname/alias](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/81d0e68c52762d3804e00e4c4ef99a421bafc05f/cluster/cz.vpsfree/machines/aitherdev/dev-workspace-site.nix); [B host authentication contract](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/docs/workspace-portal.md#host-module).
- [B retry read/no enrollment](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/portal/internal/web/turn_retry.go#L62), [B recovery/enrollment contract](https://github.com/aither64/dev-workspace/blob/d819ad044ef7fcc7bb4a111dc7676fe251383249/docs/turn-retry-recovery.md), `TestTurnRetryHTTPAuthorityPreferenceAndNoReadEnrollment`, `TestNewFailuresAndActiveEnrollment`, and `TestNativeTurnRetryController`.
- [A retry wire shape](https://github.com/aither64/codex-web/blob/c1f415ad5602c23e6443cced73cb59267a796f05/conversation/retry.go#L20) and [A visible controls](https://github.com/aither64/codex-web/blob/c1f415ad5602c23e6443cced73cb59267a796f05/conversation/assets/retry.js).
