# Workspace portal deployment

The portal will be available at:

```text
https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/
```

The implementation session prepares the Basic Auth password but does not
deploy aitherdev or either internal DNS server.

## Revisions

- Workspace branch: `2026-09-03-dev-session-portal`
- Workspace source: `4a300149052342665233c901fee92e2ec09e4fc9`
- Configuration branch: `2026-09-03-dev-session-portal`
- Configuration source: `5fba4dd7733a2a50600cd28c452e8c9ba2ac157a`

The configuration lock selects the workspace revision above. It continues to
use the ordinary `llm-agents` input, so a normal configuration pull and deploy
updates Codex as before. The aitherdev build fails if that Codex App Server
protocol is incompatible with the portal.

## Deploy

From a current checkout of the configuration branch, use the same normal
confctl workflow used for other aitherdev and internal-DNS changes:

1. Build and deploy `cz.vpsfree/machines/aitherdev`.
2. Confirm nginx, `workspace-portal`, `workspace-codex-app-server`, and
   `workspace-portal-tmux` are running.
3. Build and deploy `cz.vpsfree/containers/prg/int.ns1` and
   `cz.vpsfree/containers/brq/int.ns1`.

Activation reads the already prepared password from
`/home/aither/.local/state/vpsfree-workspace-portal/password`, derives nginx's
Basic Auth file, creates or validates the root-owned CA, installs the server
certificate, and publishes the public CA at:

```text
/var/lib/vpsfree-workspace-portal-public/ca.pem
```

Copy only that public certificate to VPN clients and trust it as a TLS root.
Never copy files from `/var/lib/vpsfree-workspace-pki` or
`/var/lib/vpsfree-workspace-portal-tls`.

After DNS is deployed, verify that the name resolves to `172.16.106.40`, HTTPS
fails without credentials, and the portal opens with username `aither` and the
password stored at the path above.

## Rollback

Use the ordinary previous NixOS/confctl generation for each affected machine.
Portal credentials and CA state may remain on aitherdev for a later redeploy;
they do not affect the previous generation.
