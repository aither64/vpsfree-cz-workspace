# Operator deployment runbook: newadmin.vpsfree.cz

Status: the user reports that the initial WebUI is deployed at
`https://newadmin.vpsfree.cz`. This runbook covers the current follow-up for
OAuth session IP and User-Agent metadata as well as the earlier console CSP,
credential and monitoring changes. The user performs production activation.
Record the running generation and verify the operator prerequisites before
changing it.

Prepared heads: WebUI `534caa83a5f97d2b40b4a126886649b14dc9e8d3`
and configuration `a433690828a23c13a8ccb3df0c07b9f2d915f0ca`. Both
development branches are published; the configuration lock selects that exact
WebUI revision. Independent whole-branch reviews, WebUI packages and ordinary
HTTPS VM, pinned UI-host build, Prometheus fixture and
[WebUI CI](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/36575754287)
passed. These results do not constitute production activation or live-browser
acceptance. The last publicly inspected frontend reported the older WebUI
`b86e202d`; confirm the actual running revision before activation.

## Target and responsibilities

- VPS: `30431`, private IPv4 `172.16.9.170`.
- Hostname: `vpsadmin-webui1.int.vpsfree.cz`.
- Confctl machine: `cz.vpsfree/vpsadmin/int.vpsadmin-webui1`.
- Public origin: `https://newadmin.vpsfree.cz`.
- Edge: `cz.vpsfree/containers/prg/proxy`, private IPv4 `172.16.9.140`.
- Expected service: `vpsadmin-webui-bff.service`, one process on loopback 3001.
- Fixed state root: `/var/lib/vpsadmin-webui`; account/group `vpsadmin-webui-bff`.
- Sessions: `/var/lib/vpsadmin-webui/sessions`, private and persistent.

Agents prepare code, review, builds and isolated tests. The operator supplies
the private files, keeps the existing OAuth registration, checks the VPS,
activates systems and verifies production behavior. No change to the legacy
public UI is needed.

The requested Kerry deploy key is authorized only by the new UI-host generation.
Use an already authorized SSH key or console access for its first activation;
the new key cannot bootstrap its own authorization. After activation, verify
its fingerprint `SHA256:OealF7ki4iyhmZ5Ogp74K/cP9hsDEgMC6n5YV6j3xeA`
authenticates on `vpsadmin-webui1.int.vpsfree.cz` with Kerry's normal admin
identity. The old Kerry key remains authorized. Rolling back to a generation
without the new key removes that access again.

## What to put in /private/

Before activating the credential-capable generation, provide these **three
separate regular UTF-8 files** on the UI VPS:

| File | Contents |
| --- | --- |
| `/private/vpsadmin-webui/oauth-client-id` | The registered OAuth client ID only |
| `/private/vpsadmin-webui/oauth-client-secret` | The current OAuth client secret only |
| `/private/vpsadmin-webui/session-secret` | The **same effective session signing secret** used by the running generation |

The files contain raw values, with at most one final newline. Do not include
`KEY=`, shell quotes, `export`, JSON or comments. This is a direct cutover:
the new service neither reads `/private/vpsadmin-webui.env` nor falls back to
secret environment variables. Keep the old environment file privately available
until the new generation is verified, because a rollback to the deployed older
generation still requires it. Keeping it does not expose it to the new service.

Check the existing `/private` path, mount and parent permissions before creating
anything. `/private` and `/private/vpsadmin-webui` should be root-owned private
directories (0700); each file should be a root:root regular file (0600), with
no symlink in the path. Use your normal private secret management or root-only
editor workflow to populate them without putting values into shell command
arguments, shell history, Git, Nix, build output or this session. Systemd reads
the source files as root and gives the unprivileged BFF private copies under
`$CREDENTIALS_DIRECTORY`; the BFF account needs no access to `/private`.

After preparing the files, this metadata-only check shows their types, owners
and modes without printing values:

```sh
sudo stat -c '%n %U:%G %a %F' /private /private/vpsadmin-webui \
  /private/vpsadmin-webui/{oauth-client-id,oauth-client-secret,session-secret}
```

Confirm both directories are `root:root` mode `700` and all three files are
regular `root:root` mode `600`. Use `namei -l` and the mount inventory to check
the path components; stop if the existing path has an unexpected symlink or
mount rather than changing it automatically.

| Value | Where it comes from | Persistence/rotation |
| --- | --- | --- |
| OAuth client ID | Dedicated vpsAdmin OAuth client for newadmin | Public identifier; must match the registration |
| OAuth client secret | Secret supplied when creating that client; at least 32 UTF-8 bytes with varied characters for production startup | Update registration and service together; keep outside Git/Nix store |
| Session signing secret | Independent cryptographically random secret | Preserve the running value; changing it invalidates signed browser sessions |

Both secret values must satisfy the BFF's production strength check: at least 32
UTF-8 bytes, varied characters and no placeholder prefix. A short or placeholder
value prevents the service from listening. The cutover reuses the deployed
values; do not rotate either secret as part of this change.

The BFF rejects missing, weak, malformed, oversized or unreadable credentials
before it listens. Preserve the exact effective values from the deployed
generation, particularly the session secret. Verify file types, ownership and
modes with metadata-only tools such as `namei -l` and `stat`; do not print file
contents during verification. Back up the files through the normal private
secret process.

The selected deployment does **not** need a VPS API administrator token, database
password, Redis password or production user credential on this host. End users
authenticate through OAuth. Existing edge ACME/DNS secrets remain owned by those
systems; do not copy them to the UI VPS. If a required site profile has additional
baseline secrets, list them separately after inspecting that profile.

## OAuth client registration

This section records the initial registration contract. The credential-file
cutover reuses the already registered client ID and secret; it does not call
for a new OAuth client or secret rotation.

For an initial deployment, create a dedicated client through the existing
supported vpsAdmin administration workflow/API. Do not edit the database
directly. The inspected
`Oauth2Client.Create` contract accepts these relevant fields:

| Field | Value or instruction |
| --- | --- |
| `name` | A recognizable name such as `vpsAdmin WebUI (newadmin)` |
| `client_id` | Use the identifier stored in `oauth-client-id` |
| `client_secret` | Supply a newly generated secret through the private workflow; save it immediately |
| `redirect_uri` | Exactly `https://newadmin.vpsfree.cz/oauth/callback` |
| `authorization_start_uri` | `https://newadmin.vpsfree.cz/oauth/login` for password-recovery return flow |
| `authorization_start_requires_user_action` | False for the automatic login-start route, if supported by the deployed API contract |
| `is_default` | False; preserve the current default client |
| `issue_refresh_token` | True for the planned persistent BFF login flow |
| Token lifetime fields / `allow_single_sign_on` | Use the site's intended policy; record it and verify it against the actual deployed API |

The API hashes the client secret and its normal output does not return the secret
back. Do not rely on retrieving it after creation. Confirm password-recovery and
SSO options exist on the deployed revision before registration. Existing source
configuration alone is not proof of deployment/schema state.

The module derives these public service settings from the site configuration:

```ini
BFF_RUNTIME_MODE=production
NODE_ENV=production
PUBLIC_ORIGIN=https://newadmin.vpsfree.cz
API_URL=https://api.vpsfree.cz
API_VERSION=7.0
OAUTH_AUTHORIZE_URL=https://auth.vpsfree.cz/_auth/oauth2/authorize
OAUTH_TOKEN_URL=https://auth.vpsfree.cz/_auth/oauth2/token
OAUTH_REVOKE_URL=https://auth.vpsfree.cz/_auth/oauth2/revoke
OAUTH_REDIRECT_URI=https://newadmin.vpsfree.cz/oauth/callback
OAUTH_SCOPE=all
OAUTH_TYPE=web_server
PASSWORD_RECOVERY_URL=https://auth.vpsfree.cz/oauth2/password-reset
HAVEAPI_AUTH_HEADER=X-HaveAPI-OAuth2-Token
HAVEAPI_META_NAMESPACE=_meta
LEGACY_WEBUI_URL=https://vpsadmin.vpsfree.cz
SESSION_STORE_PATH=/var/lib/vpsadmin-webui/sessions
SESSION_COOKIE_NAME=vpsadmin_webui_session
PORT=3001
```

The NixOS module sets `BFF_RUNTIME_MODE=production` and the explicit
`PUBLIC_ORIGIN` in the service environment. The production BFF validates all
listed public settings, the exact callback origin/path, the three matching
OAuth-provider origins, bounded numeric settings, both strong secrets and the
writable session directory before opening its listener. It does not fill in
missing production settings from legacy defaults. The module creates the
persistent session directory and grants access before service startup; systemd
supplies only the three private credential files listed above. No raw secret is
assigned to the service environment or an `EnvironmentFile`.
The state root and session path are fixed by the module; the site must not set
`services.vpsadmin-webui.stateDirectory`, including an explicit old default.
The module does not set the optional `DOMAIN`; if supplied elsewhere, it must
equal the public origin's host. `BFF_RUNTIME_MODE=legacy-test` is only for
isolated fixtures and cannot run with `NODE_ENV=production`.

The password-recovery path intentionally has no `/_auth` prefix; the inspected
auth frontend routes it separately. The BFF appends its client ID. Verify all
routes, CORS preflight, passkey handoff and API version against the actual service.
Keep passkeys at the authentication origin; do not change the WebAuthn relying
party merely because the UI uses a new hostname. Expose the legacy UI URL through
the new module/runtime option for remaining legacy links and heatmaps.

## Host baseline before activation

The user identifies VPS 30431 as a fresh NixOS container on vpsAdminOS and
selects 26.05. The host configuration uses `system.stateVersion = "26.05"`, the
existing `environments/base.nix` and `profiles/ct.nix` imports, and channels
`nixos-stable`, `os-staging`, `vpsadmin-webui`. The channel selects current
software; `stateVersion` preserves compatibility with state from the original
installation and must not advance with later channel updates. The older service
hosts' `22.05` values are not this fresh host's baseline.

The initially deployed site feature head `6586b383` sets that value and omits the
obsolete `services.vpsadmin-webui.stateDirectory` option. Keep the module's
fixed state/session paths, account and secret handling. Base/container/shared
modules already supply the established container policy, DNS/SSH and
monitoring/logging; do not copy extra boot/network settings or the blog host's
monitoring exceptions. Use the existing registered site and WebUI checkouts
with clean exact heads. The new host derivation evaluates for `x86_64-linux`;
installed-machine verification below is an activation prerequisite, and
the initial channel lock pins the published WebUI commit `aff1e4b0`. The
seven-machine build passed at site head `6586b383`, and the rendered backend
and edge nginx configurations were checked. The user reports an initial
deployment; its installed generation and any subsequent changes still require
operator confirmation.

## Preflight before any activation

1. Obtain the reviewed UI/configuration revisions, successful build results,
   full release limitations and the final version of this runbook. Confirm the
   published WebUI feature ref contains the **new credential-capable revision**
   and the site's `vpsadmin-webui` channel lock selects its full SHA. Verify
   that the frontend, BFF and module resolve to that one revision. Use
   `confctl inputs channel set --commit vpsadmin-webui vpsadmin-webui
   FULL_COMMIT` in the configuration feature checkout's `nix develop` shell,
   then inspect the generated lock diff and rebuild. Do not deploy floating
   checkout files or a local Nix input override. Integrating a default branch
   remains a separate decision from this rollout.
2. Verify VPS identity/address, SSH access and host key. Confirm the installed
   architecture matches the build target and inspect provisioned container
   interfaces/routes and boot configuration. Confirm the actual first-install
   `system.stateVersion` from the original provisioning/configuration record
   against the candidate's `26.05`; the current channel or `nixos-version` alone
   is insufficient. If it differs, stop activation, reconcile the configuration
   with that original baseline and rebuild. Preserve any required existing
   network configuration; do not invent interface or gateway values.
3. **Before changing the running BFF generation**, inspect the reserved
   `/var/lib/vpsadmin-webui` path and its `sessions/` child using filesystem
   metadata, without printing session contents. Confirm they are absent
   (including no dangling symlink), or are documented state from this BFF,
   owned by `vpsadmin-webui-bff:vpsadmin-webui-bff` with directory mode 0700.
   Inspect path components and resolved mount/source identity, including bind
   mounts and symlinks; neither reserved directory may be a symlink or alias
   legacy PHP state (`/var/lib/vpsadmin/webui`) or unrelated data. Metadata tools
   such as `namei -l`, `stat` and `findmnt -T` help establish this; for an absent
   path, inspect its nearest existing parent and the configured mounts.
   Stop on foreign ownership, unexpected contents/provenance, an alias or an
   unexplained mount. Resolve the collision explicitly before activation;
   do not delete, move or recursively chown the tree as an automatic repair.
   Systemd can change ownership during `StateDirectory` setup, before
   `ExecStartPre` or BFF validation, so a successful application check cannot
   replace this prerequisite. Preserve the existing BFF sessions and signing
   secret; do not recreate the state tree during the credential cutover.
4. Confirm connectivity from `proxy.prg` to 172.16.9.170 and from the UI VPS to
   API/auth/DNS. The backend HTTP listener is private; do not expose the BFF port.
5. Install the three credential source files and verify their path metadata.
   Confirm the values match the running OAuth client and signing secret without
   printing them. Keep the old environment file for old-generation recovery.
6. Save the running system generation ID for the UI host and retain its closure
   and old environment file for rollback. Record the current BFF/frontend build
   revisions and verify its sessions before activation.
7. Preview changes with scoped `confctl deploy MACHINE dry-activate`. This is an
   operator action on real machines, even though it does not activate the result.
   Inspect service restarts/reloads and stop if unrelated changes appear.

## Deployment order

Run confctl commands from the reviewed `vpsfree-cz-configuration` feature worktree
inside `nix develop`. Source integration into master is a separate decision.

The OAuth metadata change is in the BFF, with its matching WebUI package pinned
by this UI-host generation. It needs no edge, DNS or API configuration change.
The earlier credential/CSP changes also affect the UI host; the separate
missing-probe-series alert correction changes monitoring rules and is not part
of this scoped host activation. Verify the three existing credential files and
stable signing key; the exact host build passed, and the operator must first
run the scoped dry activation. Then activate only
`cz.vpsfree/vpsadmin/int.vpsadmin-webui1`:

```sh
confctl deploy cz.vpsfree/vpsadmin/int.vpsadmin-webui1 switch
```

Check the BFF unit and private nginx, then the public static document, session
contract and both iframe integrations. Verify that the served static CSP has the
two exact new `frame-src` origins, with the prior map origin and script policy
unchanged. Run the acceptance checks below without collecting OAuth codes,
cookies, iframe session queries or credentials. The user performs activation;
this session has not run a live login or changed the production systems.

## Post-deployment checks

- External and internal DNS resolve `newadmin.vpsfree.cz` through `proxy.prg`;
  internal DNS resolves `vpsadmin-webui1.int.vpsfree.cz` to 172.16.9.170.
- HTTPS works over the edge's IPv4 and IPv6, with the expected certificate and
  hostname. The private backend has no invented AAAA record.
- `/build-info.json` identifies the intended UI revision; record the BFF package
  revision independently. `/`, a deep app URL, both locale chunks and hashed
  assets load. A missing asset is 404, not HTML.
- `/config.json` has JSON MIME, schemaVersion 1, a bounded public configuration object and no
  credentials; `/config.js` remains available with JavaScript MIME and the same
  public settings for compatibility. `/session.json`
  returns same-origin JSON and no-store; an anonymous response contains no access
  token. `/oauth/` paths never fall through to the SPA.
- In a controlled browser session, login sets a Secure/HttpOnly cookie, callback
  works, refresh preserves the login, logout invalidates it, and password recovery
  and passkey handoff return to the correct origin. Keep tokens/codes out of logs
  and screenshots. Do not use destructive production operations as smoke tests.
- Log out and complete a **fresh** OAuth login from a known client network.
  Inspect the newly created vpsAdmin session record: `client_ip_addr` should
  match that client's observed public address and its User-Agent should be
  exactly `vpsadmin-webui`. `api_ip_addr` can still identify the API-facing
  proxy. Refresh and logout must work. Existing session records are unchanged;
  they cannot prove the new code exchange. The new WebUI's primary session-list
  IP currently prefers `api_ip_addr`; use the expanded fields or API record to
  check `client_ip_addr` without recording a member's address or session token.
- English/Czech language selection, validation, navigation, console and documented
  read-only flows work. Verify important real-API scenarios using an explicitly
  owned test account/environment, not arbitrary member resources.
- The static document's `Content-Security-Policy` includes exactly
  `https://console.vpsfree.cz` and `https://goresheat.vpsfree.cz` in `frame-src`
  alongside the existing map source. Both frames load in a controlled browser
  session. Keep frame paths, session queries and browser tokens out of records.
- Restart the BFF in the agreed maintenance window and verify session persistence.
  Confirm service failure, endpoint and TLS alerts are observable.
- `vpsadmin.vpsfree.cz`, API/auth, existing maintenance routes and the old
  `clankerdev` deployment retain their intended behavior.

Record timestamps, source/configuration revisions, generations, checks and known
limits in a deployment receipt. Do not include cookies, tokens or user data.

## Recovery

For a bad UI release, restore the previously recorded UI/BFF and system
configuration generation through the site's normal confctl generation workflow.
Use the exact recorded generation rather than an assumed previous number. The
credential-capable generation needs the three private source files; the
pre-cutover generation instead needs the preserved environment file. Keep the
same effective signing secret and compatible session directory with its
dedicated owner. Fixing the state path does not change the cookie,
session format or default storage location, and needs no session migration or
reauthentication. An installation using a former custom path requires its own
explicit migration plan; do not silently select, copy or recreate its sessions.
Validate the service after restoration. Test an already-open tab against the
restored immutable asset package; if a chunk is unavailable, reload after
preserving any unsaved work. Do not assume assets from another generation remain
available.

If the state format/signing contract changed, follow that release's explicit
recovery instructions. Do not overwrite current sessions with a stale snapshot
of rotated refresh tokens. Controlled session invalidation and login again may
be required. A UI rollback never reverses completed API operations.

This follow-up does not change DNS or the edge. Verify the public UI, legacy UI,
TLS and monitoring after recovery. Retain the VPS and session records; this
runbook does not call for deleting infrastructure.
