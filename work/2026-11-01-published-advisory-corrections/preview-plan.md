# Session preview: legacy PHP and React WebUIs

Prepared 2026-11-02 for the user's explicit request to start this session's
development cluster. This is a launch/connection brief, not deployment to shared
production, integration approval or authorization to reset/stop/remove anything.
The lead owns final usability acceptance and the user-facing explanation.

## Selected setup and owners

Use the installed `vpsadmin-devcluster` provider and the existing session config:
`.dev-clusters/vpsadmin/clusters/2026-11-01-published-advisory-corrections/config.json`.
Inspection found stopped/not-ready state with config and socket identity only:
no disks, applied selection, runner, saved topology or network. Preserve it.
The architect's initial `urls` invocation initialized these two files; the lead
accepted that initialization under the user's START authorization. Do not reset.

- Implementer0 owns config preflight and the one integrated backend/guest launch.
- Implementer1 verifies the React input, packaged frontend/BFF, OAuth and modern
  browser flow after that launch. No independent npm/Vite/BFF server is needed.
- Both report exact source/runtime evidence to the lead; only one owner runs a
  cluster mutation at a time. No application source edits are needed.
- Use a fresh session-pinned Luna/low verification watcher for the long operation.
  Implementer0 owns the mutating start command; the watcher observes its private
  log/status and reports, without retry, deploy, reset or cleanup authority.

Select `single` with `bridge`: services plus node1, default `br0`. The inspected
host has br0 up; implementer0 has confirmed KVM and bridge-helper access. React
requires bridge; local mode is rejected by the supported provider. **The copied
site defaults additionally enable two optional authoritative DNS guests.** For
the requested smallest two-guest advisory preview, set only `dns.enable=false`
in this fresh own config before first boot, preserving every other value.
The separate services resolver remains enabled and supplies cluster host records;
authoritative DNS zone testing is not part of this preview. If the lead retains
the default DNS setting instead, record the actual four guests and extra memory
rather than calling it a two-guest cluster. No existing disk/data is affected.

Keep `newWebui.enable=true`, `mail.capture.enable=true`, the existing domains,
plugins and ordinary seed. No custom preview framework, auth bypass or physical
host deployment. The standard seed supplies `test-admin`, two test members,
node/pool/network/resource fixtures; it does not promise populated advisory or
VPS history. Users can create synthetic advisories through either UI. If a
pre-populated example is desired, implementers may prepare a clearly named
session-only advisory through the ordinary guarded API/UI after readiness;
do not import production content or run broad test-suite setup against this DB.

## Exact sources and preflight

From `/home/aither/workspace/ai/vpsfree.cz`, verify session/environment identity
again and that these registered own worktrees remain clean at:

| Input | Expected HEAD |
| --- | --- |
| `worktrees/2026-11-01-published-advisory-corrections/vpsadmin` | `49f5a29e5a7d85559d06d31496acb5c08895bcda` |
| `worktrees/2026-11-01-published-advisory-corrections/vpsadmin-webui` | `1c8478bceb3943645ec06ccde895ee4b0985873f` |

The installed provider selects the exact same-session API path and overrides its
`vpsadminWebui` flake input with the same-session modern path. It sets
`webuiSourceKind=worktree`, the Git revision and dirty flag. Missing modern path
would select its old pinned `534caa83...`; reject that result. No fetch/default
branch substitution or changing source HEADs for preview. PHP is live-mounted
from the API worktree, so preserve its clean bytes during use.

There is no own OS checkout. The ordinary provider resolves canonical local
`repos/vpsadminos.git` ref `refs/remotes/origin/staging`; inspection saw
`823d7b7a84277edfd77f474fc1640a1cf756e8f7`. Record the actual resolved OS input
and complete built config/closure graph at execution; do not silently claim the
API repository's lock supplies this override. Do not fetch/move that ref for this
preview. Stop unexpected local kernel builds and report the cache/input issue.

Historical modern frontend/BFF acceptance passed, but the previously recorded
frontend store path is now absent. Normal provider realization is expected;
do not assume those old paths exist or splice mismatched packages together.
Retain the actual paired package source/provenance and output paths. If path-input
packaging reports unknown Git metadata, distinguish it from the provider's
worktree attestation and prove the actual source bytes; never label unknown
metadata as a clean built release. Escalate a substantive source mismatch.

## Launch and verification commands

Run from the workspace with the existing verified environment, or explicitly:

```sh
env DEV_SESSION_SLUG=2026-11-01-published-advisory-corrections \
  DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  vpsadmin-devcluster start 2026-11-01-published-advisory-corrections \
  --topology single --network bridge
```

This is fresh creation, so do not use `--existing`, `--force`, copied-config or
maintenance commands. Preserve failed-operation evidence and inspect before any
retry. The standard command performs seeding, node refresh and exact guest boot
proof; its readiness is stronger than a page responding during boot. Log output
can include development login values, so keep the raw log private and summarize
only status/provenance in tracking. The provider's native runner log is under
the exact session cluster directory.

The provider checks active session/lifecycle locks and exact runner/socket
ownership. Start refuses an already-running own runner and, without `--force`,
a responding configured services IP (`172.16.106.53`). This is the supported
address-conflict guard, **not** proof of a global atomic route reservation.
Honor refusal; do not stop another frontend, force startup or inspect another
session's files. No repository merge or physical-machine deployment claim is
required for this isolated standard devcluster launch.

After the command completes, use the ordinary interfaces:

```sh
vpsadmin-devcluster status 2026-11-01-published-advisory-corrections --json
vpsadmin-devcluster ssh 2026-11-01-published-advisory-corrections services -- readlink -f /run/current-system
vpsadmin-devcluster ssh 2026-11-01-published-advisory-corrections services -- systemctl is-active vpsadmin-api.service vpsadmin-supervisor.service container@webui.service container@newadmin.service container@mailer.service
vpsadmin-devcluster cert show-ca
```

Record selected `result-config`, applied config/proofs, full running system and
package paths, API source49f5 and modern source1c847/clean/worktree labels. Status
labels describe a selected build, so compare actual running closure and served
modern `/build-info.json`; inspect BFF package metadata through the actual
running service package. Do not substitute an old acceptance receipt for runtime
proof. Record exact failed phase/remaining owned operation on refusal or failure.

## URLs, authentication, mail and acceptance

These are configured internal/VPN preview URLs; availability is established only
after startup and browser checks:

| Service | URL |
| --- | --- |
| Legacy PHP | `https://webui.aitherdev.int.vpsfree.cz/` |
| Modern React | `https://newadmin.aitherdev.int.vpsfree.cz/` |
| API | `https://api.aitherdev.int.vpsfree.cz/` |
| OAuth provider | `https://auth.aitherdev.int.vpsfree.cz/` |
| Captured mail | `https://mailpit.aitherdev.int.vpsfree.cz/` |

The browser needs VPN/internal DNS routes to the services IP and trust in the
workspace devcluster CA. Use `cert show-ca` for its path/fingerprint; do not
disable TLS checks to call the preview usable. Normal session portal cluster
links/credential fields expose the synthetic test-admin and Mailpit access.
Keep passwords, OAuth secrets, tokens and raw session responses out of this plan,
tracking and screenshots. The lead can direct the user to the portal credentials.

The provider creates a separate nondefault modern OAuth client with callback
`https://newadmin.aitherdev.int.vpsfree.cz/oauth/callback`; it preserves the PHP
client. Its three private runtime credential files stay in this own cluster's
`webui-credentials/`, mounted read-only into services. The BFF listens on loopback
3001 inside newadmin, behind private nginx18082 and the services HTTPS edge,
and retains `/var/lib/vpsadmin-webui/sessions`. No hand-created secret, environment
token injection or standalone credential flow is needed.

Implementer1 verifies public `/healthz`, `/config.json` and `/build-info.json`
without dumping session tokens, then normal Login → owned auth service → callback
→ authenticated admin flow. Confirm API7.0, actual HTTPS API/CORS, correct current
test-admin identity, no production host requests, and logout/re-login. Verify
legacy login and both advisory management routes against this same DB. Check
published/retracted edit controls, explicit retract/delete confirmation, and
separate announcement controls; use only identified synthetic objects for writes.
Mail capture is on inside the mailer container; confirm no external SMTP route
and no new captured message from silent correction. Any explicit test announcement
is session-only and captured by Mailpit. No production mail or deletion.

Lead acceptance reports both working UI links, portal login location, exact
sources and any DNS/CA limitations. Explain corrections versus announcements,
the newly editable CVEs/node membership/time, and retract versus hard deletion.
Leave the cluster running with its data for the user's trial. START supplies no
authority for later stop, reset, release, cleanup, merge or session archival.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
