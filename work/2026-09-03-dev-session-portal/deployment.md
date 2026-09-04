# Workspace portal deployment

The portal will be available at:

```text
https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/
```

The implementation prepares all local files on aitherdev. This session does
not deploy aitherdev or either internal DNS server.

## Revisions

- Workspace branch: `2026-09-03-dev-session-portal`
- Workspace source: `0ae37664d211adc4ccf608544ccccbaa0e1d7d5e`
- Configuration branch: `2026-09-03-dev-session-portal`
- Configuration source: `5d4e9eafa67c27ef1ef4913794250806431f1153`

The configuration lock selects the exact workspace revision above. It uses the
ordinary `llm-agents` input, so pulling and deploying normal configuration
updates Codex as before. The aitherdev build fails if the selected Codex App
Server protocol is incompatible with the portal.

## Deploy

From a checkout of the configuration feature branch, use the normal confctl
workflow:

1. Deploy `cz.vpsfree/machines/aitherdev`.
2. Confirm `nginx`, `workspace-portal`, `workspace-codex-app-server`, and
   `workspace-portal-tmux` are running.
3. Deploy `cz.vpsfree/containers/prg/int.ns1` and
   `cz.vpsfree/containers/brq/int.ns1`.

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

After DNS is deployed, verify that the name resolves to `172.16.106.40`, HTTPS
fails without credentials, and the portal opens with username `aither` and the
password at the path above. Create a test session in the browser, send a turn,
then attach from a terminal with `workspace-dev-session attach <slug> --as-is`
and confirm that both clients show the same thread.

## Rollback

Use the ordinary previous NixOS/confctl generation for each affected machine.
Portal credentials and CA state can remain on aitherdev for a later redeploy;
they do not affect the previous generation. If DNS was already deployed, roll
back both DNS containers or expect the hostname to resolve while the portal is
offline until the DNS TTL expires.

## Permanent decommission

1. Roll back or remove the portal configuration on aitherdev and both DNS
   containers.
2. Remove the workspace CA from every client trust store.
3. After confirming that no client trusts it, destroy the root-owned CA, leaf,
   and nginx portal TLS state on aitherdev.
4. Remove the portal password and any copied public CA files that are no longer
   needed.

The CA is intentionally not DNS-name-constrained. Client trust removal is
therefore required for permanent decommission; merely stopping the portal is
not sufficient.

## CA compromise

Immediately remove the workspace CA from every client trust store and take the
portal offline. Destroy the compromised CA and all leaves it signed. Generate a
new CA and leaf through the packaged PKI initialization workflow, redeploy
aitherdev, distribute only the new public CA, and reinstall trust on each
client. Do not reuse the old CA key or retain it for rollback.
