# Devcluster Certificate Reissue

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`

Symptom:

- Adding `mailpit.aitherdev.int.vpsfree.cz` required a new server certificate
  SAN.
- The imported `vpsf-dev` leaf certificate did not contain that domain.

Cause:

- The devcluster originally reused the `vpsf-dev` CA and leaf certificate.
- The imported CA key is encrypted, so unattended tooling cannot reissue a leaf
  certificate from that CA without the passphrase.

Fix/workaround:

- Generate certificate SANs from the configured devcluster `domains` and
  `tmpDomains` instead of a hardcoded list.
- Reissue the leaf certificate when configured domains are missing from the
  current certificate.
- If the current CA key cannot sign unattended, fall back to a fresh
  workspace-local devcluster CA.
- Set `VPSADMIN_DEVCLUSTER_CA_PASSPHRASE` before `devcluster start` or
  `devcluster update` to reissue from an encrypted imported CA instead of
  generating a fresh CA.

Verification:

- The running certificate contains `mailpit.aitherdev.int.vpsfree.cz` in its
  SAN list.
- `curl -k --resolve mailpit.aitherdev.int.vpsfree.cz:443:172.16.106.53`
  returned HTTP 401 without credentials and HTTP 200 with the configured
  Mailpit basic-auth credentials.
