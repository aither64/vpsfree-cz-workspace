# Review bootstrap password and action input contracts

Initiative: work/2026-09-09-ip-release-mechanism.

A reset-cluster bootstrap returned HTTP401 because it assigned `User#password`
directly. That attribute stores the encrypted value; use `user.set_password`
followed by `save!`. The corrected bootstrap restored the private review
credentials and API authentication succeeded. Never record plaintext credentials
in tracking or logs.

The signing-key unlock action then returned `invalid input layout`: its hash
input uses the default resource wrapper. Submit `api_server: { passphrase: ... }`
to `ApiServer.UnlockTransactionSigningKey`. The corrected call unlocked signing
and VPS creation succeeded. Use API discovery or the existing client when
constructing other action payloads.

User has no `ip_addresses` association. Review inventory checks should query
`IpAddress.where(user: user, charged_environment: environment)` explicitly.
