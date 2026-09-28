# Operator deployment runbook: newadmin.vpsfree.cz

Status: the WebUI module and site configuration are prepared on their feature
branches, with build evidence recorded in `state.md`. Nothing has been deployed.
The user performs the production actions. Before using these steps, record the
reviewed WebUI and configuration revisions and verify the remaining operator
prerequisites.

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
secrets, creates the OAuth client, checks the existing VPS, activates systems and
verifies production behavior. No change to the legacy public UI is needed.

## What to put in /private/

On the new VPS, provide **`/private/vpsadmin-webui.env`**, owned by `root:root`,
mode **0600**. Keep `/private` restricted according to the site's existing policy.
The system service manager reads this file before starting the unprivileged BFF;
the service user does not need direct access to the directory.

```ini
OAUTH_CLIENT_ID=REPLACE_WITH_REGISTERED_CLIENT_ID
OAUTH_CLIENT_SECRET=REPLACE_WITH_REGISTERED_CLIENT_SECRET
SESSION_SECRET=REPLACE_WITH_A_SEPARATE_RANDOM_SECRET
```

| Value | Where it comes from | Persistence/rotation |
| --- | --- | --- |
| `OAUTH_CLIENT_ID` | Dedicated vpsAdmin OAuth client for newadmin | Public identifier; must match the registration |
| `OAUTH_CLIENT_SECRET` | Secret supplied when creating that client; at least 32 UTF-8 bytes with varied characters for production startup | Update registration and service together; keep outside Git/Nix store |
| `SESSION_SECRET` | Independent cryptographically random secret, e.g. 48 random bytes encoded as hex | Keep stable across redeployments; changing it invalidates signed browser sessions |

Both secret values must satisfy the BFF's production strength check: at least 32
UTF-8 bytes, varied characters and no placeholder prefix. A short or placeholder
value prevents the service from listening. Check the OAuth client's generated
secret meets this contract before registering it; generate a suitable one
through the private workflow if the admin tool allows a supplied secret.

Use systemd environment-file syntax, not shell code: no `export`, command
substitution or shell expansion. Using generated hex values for secrets avoids
quoting ambiguity. Replace placeholders before starting the service.

Before using the example, inspect `/private` and its parent path to confirm the
intended root-owned directory and mount, with no symlink or unexpected writable
parent. An operator can then prepare the initial file locally on the VPS
without displaying the session secret. Run once as root; it refuses to use an
unsafe `/private` directory or overwrite an existing file:

```sh
python3 - <<'PY'
import os
import secrets
import stat
from pathlib import Path

directory = Path('/private')
try:
    directory.mkdir(mode=0o700)
except FileExistsError:
    pass
metadata = directory.lstat()
if not stat.S_ISDIR(metadata.st_mode) or metadata.st_uid != 0 or metadata.st_mode & 0o022:
    raise SystemExit('Refusing unsafe /private directory')
path = directory / 'vpsadmin-webui.env'
fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
os.fchown(fd, 0, 0)
with os.fdopen(fd, 'w') as stream:
    stream.write('OAUTH_CLIENT_ID=REPLACE_WITH_REGISTERED_CLIENT_ID\n')
    stream.write('OAUTH_CLIENT_SECRET=REPLACE_WITH_REGISTERED_CLIENT_SECRET\n')
    stream.write('SESSION_SECRET=' + secrets.token_hex(48) + '\n')
PY
```

Use an available Python interpreter or the site's approved secret-generation
tool, then fill in the client values through a private editor/secret workflow.
Verify `/private` itself remains private under the site's directory policy,
and that the environment file is owned by `root:root` with mode 0600. The
example leaves an existing directory's mode unchanged. Check placeholder
removal without printing file contents.
Never paste the values into this session, a commit, a build command argument or
a deployment log. Back up the file through the normal private-secret process.

The selected deployment does **not** need a VPS API administrator token, database
password, Redis password or production user credential on this host. End users
authenticate through OAuth. Existing edge ACME/DNS secrets remain owned by those
systems; do not copy them to the UI VPS. If a required site profile has additional
baseline secrets, list them separately after inspecting that profile.

## OAuth client registration

Create a dedicated client through the existing supported vpsAdmin administration
workflow/API. Do not edit the database directly. The inspected
`Oauth2Client.Create` contract accepts these relevant fields:

| Field | Value or instruction |
| --- | --- |
| `name` | A recognizable name such as `vpsAdmin WebUI (newadmin)` |
| `client_id` | Choose the identifier and put the same value in the environment file |
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
persistent session directory and grants access before service startup; the
operator's environment file supplies only the three secret-bearing values
shown above. Do not add `SESSION_STORE_PATH` or other public settings to that
file: systemd environment-file assignments override the module's environment.
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

The site feature head `6586b383` sets that value and omits the
obsolete `services.vpsadmin-webui.stateDirectory` option. Keep the module's
fixed state/session paths, account and secret handling. Base/container/shared
modules already supply the established container policy, DNS/SSH and
monitoring/logging; do not copy extra boot/network settings or the blog host's
monitoring exceptions. Use the existing registered site and WebUI checkouts
with clean exact heads. The new host derivation evaluates for `x86_64-linux`;
installed-machine verification below is an activation prerequisite, and
the channel lock pins the published WebUI commit `aff1e4b0`. The final
seven-machine build passed at site head `6586b383`. The rendered backend and
edge nginx configurations were checked. This build has not been activated.

## Preflight before any activation

1. Obtain the reviewed UI/configuration revisions, successful build results,
   full release limitations and the final version of this runbook. Confirm the
   published WebUI feature ref still contains `aff1e4b0` and that the site's
   `vpsadmin-webui` channel lock selects its full SHA. Verify that the frontend,
   BFF and module resolve to that one revision. For a later WebUI revision, use
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
3. **Before first activation or any BFF start**, inspect the reserved
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
   replace this prerequisite. Let the module create new private state after
   the check; preserve any confirmed existing BFF sessions and signing secret.
4. Confirm connectivity from `proxy.prg` to 172.16.9.170 and from the UI VPS to
   API/auth/DNS. The backend HTTP listener is private; do not expose the BFF port.
5. Install the environment file and OAuth registration. Check that no placeholder
   remains and that the configured secret path matches the deployed service.
6. Save the existing system generation IDs for each affected host and retain
   their closures. The first UI deployment has no earlier UI release to restore;
   its rollback is disabling the new service/vhost while keeping legacy access.
7. Preview changes with scoped `confctl deploy MACHINE dry-activate`. This is an
   operator action on real machines, even though it does not activate the result.
   Inspect service restarts/reloads and stop if unrelated changes appear.

## Deployment order

Run confctl commands from the reviewed `vpsfree-cz-configuration` feature worktree
inside `nix develop`. Source integration into master is a separate decision.

1. **UI VPS:** activate `cz.vpsfree/vpsadmin/int.vpsadmin-webui1` using
   `confctl deploy cz.vpsfree/vpsadmin/int.vpsadmin-webui1 switch`. Verify nginx
   and BFF locally, anonymous session behavior and restricted backend access.
   Exercise the approved proxy-header contract from the edge before opening
   the hostname.
2. **DNS:** deploy the public primary `cz.vpsfree/containers/ns1`. Deploy the
   internal zone consumers `cz.vpsfree/containers/prg/int.ns1`,
   `cz.vpsfree/containers/brq/int.ns1`, `cz.vpsfree/containers/prg/int.mon1` and
   `cz.vpsfree/containers/prg/int.mon2`, one at a time. Verify public zone transfer
   to ns0/ns2/ns3/ns4 and both DNS views. Updating monitor hosts may install the
   new availability checks before the edge is ready; handle that short interval
   within the deployment's normal monitoring procedure.
3. **Edge:** deploy `cz.vpsfree/containers/prg/proxy`. DNS must already direct
   `newadmin.vpsfree.cz` to the edge for ACME HTTP validation. Verify certificate
   issuance and the HTTPS redirect, then static and auth routes. The final nginx
   configuration must allow challenge handling and the site's ACME retry flow.
4. **Acceptance:** verify the public URL and complete the checks below. Confirm
   monitoring is green after all components are live.

Apply `confctl deploy <exact-machine> switch` to each named host; avoid wildcard deploys.
The secondaries need propagation checks, not necessarily fresh configurations for
this zone-only change. Re-evaluate the list if the final implementation changes
other hosts. This session has not deployed any system or run a live login.

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
- English/Czech language selection, validation, navigation, console and documented
  read-only flows work. Verify important real-API scenarios using an explicitly
  owned test account/environment, not arbitrary member resources.
- Restart the BFF in the agreed maintenance window and verify session persistence.
  Confirm service failure, endpoint and TLS alerts are observable.
- `vpsadmin.vpsfree.cz`, API/auth, existing maintenance routes and the old
  `clankerdev` deployment retain their intended behavior.

Record timestamps, source/configuration revisions, generations, checks and known
limits in a deployment receipt. Do not include cookies, tokens or user data.

## Recovery

For a bad UI release, restore the previously recorded UI/BFF and system
configuration generation through the site's normal confctl generation workflow.
Use the exact recorded generation rather than an assumed previous number. Keep
the environment file, stable signing secret and compatible session directory
with its dedicated owner. Fixing the state path does not change the cookie,
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

For a failed first activation, disable/revert the new vhost/service and continue
using the legacy UI. If reverting DNS contents, publish a new higher zone serial
rather than deploying an older serial that secondaries may ignore. Verify both
DNS views, TLS and monitoring after recovery. Retain the VPS/repository; this
runbook does not call for deleting infrastructure or session records.
