# Workspace portal deployment

The portal is available at:

```text
https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/
```

The user has completed the one-time aitherdev bootstrap and deployed both
internal DNS servers. The restricted local deployment key is active, so the
agent can deploy later aitherdev iterations locally. The first portal
activation stopped before credential and certificate creation because a
wrapped helper could not find Bash. The activation-corrected aitherdev
generation was followed by the browser form origin fix. The current exact
configuration pin is deployed and healthy. No DNS redeployment is required.

## Branches

- Workspace branch: `2026-09-03-dev-session-portal`
- Configuration branch: `2026-09-03-dev-session-portal`

Check out the exact configuration feature-branch head reported in the handoff.
Its lock selects the corresponding exact workspace revision. Revisions are not
embedded here because this tracking file belongs to the workspace repository
whose feature head they would recursively change. The configuration uses the
ordinary `llm-agents` input, so pulling and deploying normal configuration
updates Codex as before. The aitherdev build fails if the selected Codex App
Server protocol is incompatible with the portal.

## Current deployment

The corrected aitherdev generation was built and deployed from the
configuration feature branch with the normal confctl workflow:

```sh
nix develop -c confctl build -y cz.vpsfree/machines/aitherdev
nix develop -c confctl deploy -y cz.vpsfree/machines/aitherdev switch
```

The bootstrap generation already activated the local root deployment key and
portal services. The internal DNS name already resolves to aitherdev.

The completed validation confirmed that the system profile and
`/run/current-system` select the corrected generation; nginx, the portal,
Codex App Server, tmux backend, renewal timer, and firewall are healthy; the
restricted deployment key still authenticates locally; DNS resolves to
`172.16.106.40`; certificate reconciliation is idempotent; and HTTPS enforces
Basic Auth. Repeating activation remains safe because password and PKI setup
validate and reuse complete state, while missing state is created atomically.

The browser-origin correction was built and switched only on aitherdev:

```sh
nix develop -c confctl build -y cz.vpsfree/machines/aitherdev
nix develop -c confctl deploy -y cz.vpsfree/machines/aitherdev switch
```

Post-switch validation confirmed that HTTPS responses use
`Referrer-Policy: same-origin`; missing, literal `null`, and foreign Origin
values still return 403; and the exact portal Origin reaches ordinary form
validation. Both internal DNS deployments were left unchanged.

Activation reads the prepared password from
`/home/aither/.local/state/vpsfree-workspace-portal/password`, derives nginx's
Basic Auth file, creates or reconciles the root-owned CA and leaf, installs the
server pair, and publishes the public CA at:

```text
/var/lib/vpsfree-workspace-portal-public/ca.pem
```

Copy only that public certificate to VPN clients and trust it as a TLS root.
Never copy files from `/var/lib/vpsfree-workspace-pki` or
`/var/lib/vpsfree-workspace-portal-tls`.

The authenticated portal controls a Codex process running as `aither`, which
can use the local deployment key. After bootstrap, portal access is therefore
effectively root command access to aitherdev. Keep both VPN and Basic Auth in
place and do not reuse the portal password.

## Client handoff

After installing the public CA on a VPN client, open the portal with username
`aither` and the password at the path above. Retry creating a test session in
the browser, send a turn, then attach from a terminal with
`workspace-dev-session attach <slug> --as-is` and confirm that both clients
show the same thread.

## Rollback

Use the ordinary previous NixOS/confctl generation for each affected machine.
Portal credentials and CA state can remain on aitherdev for a later redeploy;
they do not affect the previous generation. If DNS was already deployed, roll
back both DNS containers or expect the hostname to resolve while the portal is
offline until the DNS TTL expires.

Rolling aitherdev back to a generation before the deployment key was added also
removes that root authorization. That rollback is user-owned unless another
root credential is available. An agent-driven `confctl` rollback using only
this key can activate the old generation, lose access, and then report failure
when it reconnects to update the system profile. In that case the rollback may
already be active despite the command failure. The user must bootstrap the next
aitherdev deployment again.

## Permanent decommission

1. Roll back or remove the portal configuration on aitherdev and both DNS
   containers.
2. Remove the workspace CA from every client trust store.
3. After confirming that no client trusts it, destroy the root-owned CA, leaf,
   and nginx portal TLS state on aitherdev.
4. Remove the portal password and any copied public CA files that are no longer
   needed.
5. Remove the dedicated `confData.sshKeys.aither.aitherdev` authorization if
   agent-driven aitherdev deployment is no longer wanted.

The existing local private key is not owned by the portal and is not deleted as
part of portal rollback or decommissioning.

The CA is intentionally not DNS-name-constrained. Client trust removal is
therefore required for permanent decommission; merely stopping the portal is
not sufficient.

## CA compromise

Immediately remove the workspace CA from every client trust store and take the
portal offline. Destroy the compromised CA and all leaves it signed. Generate a
new CA and leaf through the packaged PKI initialization workflow, redeploy
aitherdev, distribute only the new public CA, and reinstall trust on each
client. Do not reuse the old CA key or retain it for rollback.
