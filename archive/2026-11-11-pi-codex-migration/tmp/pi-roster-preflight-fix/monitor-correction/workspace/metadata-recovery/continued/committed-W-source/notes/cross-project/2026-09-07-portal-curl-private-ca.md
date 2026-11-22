# Check the workspace portal with its public CA

Initiative: `work/2026-09-05-cgroup-v1-shared-device-fix`.

Ambient `curl -I` and an explicit system certificate bundle both failed with
`unable to get local issuer certificate` for the workspace portal. Its private
CA is documented in `docs/workspace-portal.md` and exported publicly at
`/var/lib/vpsfree-workspace-portal-public/ca.pem` on aitherdev.

Use `curl --cacert /var/lib/vpsfree-workspace-portal-public/ca.pem -I <portal-url>`.
This verified TLS and returned the expected HTTP 401 authentication challenge.
No password or private key is needed to check that the protected listener is up.
