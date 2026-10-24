# Deployment smoke procedure and rollout status

Owner: implementer0; lead executes after architect compatibility/order acceptance
and activation. This document does not authorize activation or merge. Updated
coordination rules use short repository merge locks only; independent preparation
has no repository claim. Lead retains the separate machine reservation through
activation and live acceptance. Baseline phase has now run once and passed exit0/5.094s against predecessor6bbj.
The after phase remains pending deployment. Evidence: verification/deployment-smoke/
before.log and before-result.txt; private identity snapshot continuity-before.json.

The original tested composition is B `db25364`, A `852e8c5`, C `3de65bbd`;
[verification-summary.md](verification-summary.md) retains its exact evidence.
The deployment refresh B is `f8f2938b4e2cfd6e5b82657d08f014357817808f`,
which preserves installed runtime `9686464`. Lead must substitute its final
C/package receipts, not deploy an older composition. No source pin is
proof of the installed executable. Architect owns that mapping and deployment order.

## Read-only host and routing checks

Run from this session tracking directory. Capture before/after results under
`verification/deployment-smoke/`. Do not capture environment, credentials, full
process arguments, native logs, prompts, submission records or entire HTTP bodies.

```sh
dev-session current
workspace-host status
systemctl --user show workspace-router.service --property=ActiveState,SubState,MainPID,FragmentPath
```

Use the workspace name printed by `workspace-host status` for the exact root
`/home/aither/workspace/ai/vpsfree.cz` (do not guess it). Set `PORTAL_SMOKE_NAME`
from that registration and `PORTAL_SMOKE_HOST` to its canonical hostname:

```sh
systemctl --user show "workspace-portal@$PORTAL_SMOKE_NAME.service" "workspace-codex@$PORTAL_SMOKE_NAME.service" --property=ActiveState,SubState,MainPID,FragmentPath
curl --fail --silent --show-error --max-time 10 --unix-socket /run/dev-workspaces/router.sock -H "Host: $PORTAL_SMOKE_HOST" http://localhost/healthz
curl --silent --show-error --max-time 10 --cacert /var/lib/dev-workspaces/public/ca.pem --output /dev/null --write-out '%{http_code}\n' "https://$PORTAL_SMOKE_HOST/healthz"
```

Expect active/running units, router health `{"ok":true}`, and unauthenticated
HTTPS 401 with successful CA/hostname verification. The last command does not
send a credential. Authenticated checks follow below. Router success alone does
not certify nginx/TLS/authentication or exact application source selection.

## Disposable browser and bounded authenticated GETs

Candidate [deployment-smoke.cjs](deployment-smoke.cjs) uses the existing pinned
Playwright/Chromium environment. It creates an ephemeral browser context with
JavaScript disabled: viewing the real HTML/CSS cannot mount receipt acknowledgement,
queue reconciliation, notifications, streams or conversation controllers. Its
explicit API requests are GET only. Password is read in memory from the existing
private password file; never passed as a command argument or printed. Lead supplies
the configured Basic Auth username. Browser certificate errors are ignored only
for this inspection; the CA-verified HTTPS command above is required separately.

Verified against the actual host declaration: Basic Auth user is `aither`;
password path is `/var/lib/dev-workspaces/password/password`; public CA path is
`/var/lib/dev-workspaces/public/ca.pem`. The registry is schema 1 with a workspaces
array; the exact root selects `vpsfree-cz` and canonical hostname
`vpsfree-cz.workspace.aitherdev.int.vpsfree.cz`. The current profile link resolves
to `/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0`.
Unprivileged access to the password directory is denied. Parent privilege
preflight `sudo -n true` failed with a password requirement; no credential was read.
Do not retry that probe or select sudo mode in the current context. The mode is
prepared for an explicitly available authorized context only; it calls only `sudo -n cat --` on that fixed file,
captures stdout/stderr privately in memory, and prints a generic access error on
failure. It does not fall back, copy the password, run the browser as root or alter
permissions. Direct mode supports an already authorized readable file via
`PORTAL_SMOKE_PASSWORD_FILE`; it never automatically switches to sudo.

The configured root transport is now proven with a read-only UID/system-link
probe: `root@172.16.106.40`, port 22, existing
`/home/aither/.ssh/id_ed25519`, `BatchMode=yes`, `StrictHostKeyChecking=yes`,
`IdentitiesOnly=yes`, `ConnectTimeout=10`. Parent explicitly selects `ssh` mode.
Only then does the smoke reader execute that fixed SSH argv with the fixed remote
command `cat -- /var/lib/dev-workspaces/password/password`; stdout/stderr stay in
private pipes and the password stays in memory/httpCredentials. An SSH failure
prints a generic access error without raw child stdout/stderr. No key, SSH trust,
service or permission change is made. This reader has not been executed separately.

Set these exact non-secret inputs before each phase:

```sh
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
export PORTAL_SMOKE_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
export PORTAL_SMOKE_SHARED_SOURCE=/home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261020220147-852e8c510915
export PORTAL_SMOKE_AUTH_USER=aither
export PORTAL_SMOKE_PASSWORD_READ_MODE=ssh
export PORTAL_SMOKE_PASSWORD_FILE=/var/lib/dev-workspaces/password/password
```

Lead also sets `PORTAL_SMOKE_PACKAGE` to the exact selected package path from its
activation receipt, `PORTAL_SMOKE_HEAD` to the exact clean B head, and
`PORTAL_SMOKE_AUTH_USER` from the host declaration. The script refuses a profile
or checkout mismatch. Use the known realized Node executable; if pressure GC
removed the pinned browser/module output, resolve it before execution through the
fresh utility, without changing package selection or silently substituting tools.

Authenticated execution is ready for the parent's explicitly selected, proven
root-SSH route. Do not invent a transport or change sudo/auth/key configuration. The public CA-verified 401 and
router health probes remain usable without credentials. Once the explicit reader
is available, exact argv is once before and once after activation (fresh policy
utility per run):

```sh
cd "$PORTAL_SMOKE_SOURCE"
nix develop --command node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/deployment-smoke.cjs before /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-smoke/continuity-before.json
nix develop --command node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/deployment-smoke.cjs after /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-smoke/continuity-before.json
```

Create the evidence directory first with mode 0700. Retain private snapshot mode
0600; it contains only root/conversation IDs, model/effort and a roster hash.
Before capture requires the current selected package as `PORTAL_SMOKE_PACKAGE`;
after requires the candidate. Use separate logs/results for before and after,
with exact package/source/argv, exit and elapsed time. Baseline execution is recorded above; the after phase is still prepared only.
Parent-owned activation stays outside utilities.

Expect 200 for authenticated health, index, current-session HTML, team GET and
`/api/sessions/<slug>/thread/page`. Index `progress=1` reads published snapshots
without triggering enrichment. History read validates the same root, but does
not send/acknowledge/restore a turn. Only counts/identities/hashes are logged;
no message text is retained. Retained roster (including saved settings/instructions)
and root model/effort must match the before snapshot. In-progress conversation
activity can append history; counts need not remain constant. No full ledger is
read or written. Incidental server read caches/attachment decoration are existing
GET behavior, not submission or roster mutation.

After activation, compare served app/CSS and all selected shared module assets
byte-for-byte with the accepted source, check app cache v50, Team/inline notice
DOM, shared helper exports and citation asset. Verify both installed team defaults
`delegated`, counts 2–6 and Full-team labels. These static/GET observations complement
the passing disposable interactions; they do not repeat Send/Add/lifecycle tests.

## Naming continuity without a naming turn

Record the portal and ordinary Codex PID/unit identity before and after. For the
portal's `MainPID`, a bounded descendant walk may read only `/proc/<pid>/exe`,
`/proc/<pid>/comm`, and the fixed model-catalog argument (never dump full cmdline
or environ). Confirm one existing owned naming child refers to the selected
`share/workspace-portal/codex-models.json`, and hash that immutable file. A package
activation may legitimately replace the portal/naming child; it must not replace
or retarget the retained same-session root/roster. Architect/lead assess that order.

Exact immutable catalog evidence command (no naming call):

```sh
sha256sum "$PORTAL_SMOKE_PACKAGE/share/workspace-portal/codex-models.json"
```

There is no read-only public naming health endpoint. Child/catalog presence and
existing-session route/history continuity establish serving-process readiness,
not successful new naming. Do not call `/sessions`, naming/preparation/fork/plan
creation, Retry, Add member, Send, acknowledgement, queue, reset, lifecycle or
restart commands. Do not create a real session to fill this evidence gap.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
