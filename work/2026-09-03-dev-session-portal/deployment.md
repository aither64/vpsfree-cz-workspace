# Workspace portal deployment

This runbook deploys the portal at
`https://workspace.aitherdev.int.vpsfree.cz/`. Run the commands yourself; the
implementation session does not deploy aitherdev or the internal DNS servers.

## Revisions

- Workspace portal source branch: `2026-09-03-dev-session-portal`
- Workspace portal source: `6371e9c` (replace with the final head recorded in
  `state.md` after review)
- Configuration feature branch: `2026-09-03-dev-session-portal`
- Configuration implementation commit: `15b473be`

Use the final configuration commit recorded in `state.md` if review or test
fixes add commits after this runbook was written.

## 1. Prepare TLS files on aitherdev

Fetch the workspace feature branch, then create the CA and leaf certificate as
`aither` from its dedicated worktree:

```sh
cd /home/aither/workspace/ai/vpsfree.cz
git fetch origin 2026-09-03-dev-session-portal
cd worktrees/2026-09-03-dev-session-portal/workspace
git pull --ff-only
bin/workspace-pki init
bin/workspace-pki verify
bin/workspace-pki inspect
```

Store the CA passphrase in your password manager. The encrypted CA key remains
at `/home/aither/.local/state/vpsfree-workspace-pki/ca-key.pem`.

Install only the nginx leaf certificate and key into the root-owned directory:

```sh
sudo bin/workspace-pki install-server \
  --state-dir /home/aither/.local/state/vpsfree-workspace-pki \
  /var/lib/vpsfree-workspace-portal-tls
```

The aitherdev configuration expects these files before nginx evaluates its new
configuration. Do not deploy aitherdev before this step.

Export the public CA for client installation:

```sh
bin/workspace-pki export-ca /tmp/vpsfree-workspace-ca.pem
```

Install that public certificate as a trusted TLS root on each macOS, iOS, or
other VPN client. Do not copy any file whose name contains `key`.

## 2. Build and deploy aitherdev

From the configuration checkout containing the final reviewed commit:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
nix develop
confctl build -y cz.vpsfree/machines/aitherdev
confctl deploy -y cz.vpsfree/machines/aitherdev
```

The portal service remains inactive until its password file exists. Create it
interactively, then start the service:

```sh
workspace-portal auth set-password
sudo systemctl restart workspace-portal
systemctl status workspace-portal --no-pager
curl --fail http://127.0.0.1:2460/healthz
```

## 3. Deploy both internal DNS servers

Deploy DNS only after the HTTPS service is healthy on aitherdev:

```sh
confctl build -y cz.vpsfree/containers/prg/int.ns1
confctl build -y cz.vpsfree/containers/brq/int.ns1
confctl deploy -y cz.vpsfree/containers/prg/int.ns1
confctl deploy -y cz.vpsfree/containers/brq/int.ns1
```

Confirm that both servers return the aitherdev alias:

```sh
dig @172.16.9.90 workspace.aitherdev.int.vpsfree.cz CNAME +short
dig @172.19.9.90 workspace.aitherdev.int.vpsfree.cz CNAME +short
```

Both commands should return `aitherdev.int.vpsfree.cz.`.

## 4. Smoke test from a VPN client

With the public CA installed and trusted:

```sh
curl --fail --cacert /path/to/vpsfree-workspace-ca.pem \
  https://workspace.aitherdev.int.vpsfree.cz/healthz
```

Open the portal in a browser, sign in, and check this initiative page. Create a
disposable session with a harmless initial request, attach from a terminal, and
confirm that a message sent from either client appears in the other. Test one
supported question or approval prompt, then archive or abandon the disposable
initiative through the normal workspace workflow.

## Renewal

Renewal leaves the CA unchanged:

```sh
cd /home/aither/workspace/ai/vpsfree.cz
bin/workspace-pki renew
bin/workspace-pki verify
sudo bin/workspace-pki install-server \
  --state-dir /home/aither/.local/state/vpsfree-workspace-pki \
  /var/lib/vpsfree-workspace-portal-tls
sudo systemctl reload nginx
```

## Rollback

If the portal service fails, inspect it without changing DNS:

```sh
journalctl -u workspace-portal -u nginx --since today
```

Roll back aitherdev through the normal NixOS generation workflow. Revert the
internal DNS commit and deploy both internal DNS servers if the name must be
removed. The workspace tracking files and Codex thread histories do not depend
on the NixOS generation and remain available from the terminal.
