# Chromium smoke tests with the portal's private CA

A Playwright Chromium launch using `--ignore-certificate-errors-spki-list` with
the local root CA's public-key hash still failed with
`net::ERR_CERT_AUTHORITY_INVALID`. The server supplies its leaf certificate, not
the root CA, so that root SPKI was not matched by Chromium.

For a temporary browser smoke test, first establish a normal verified TLS
connection using `/var/lib/dev-workspaces/public/ca.pem` and the exact portal
hostname. Hash the verified live leaf certificate's exported DER SPKI with
SHA-256 and pass its Base64 digest to Chromium's SPKI allowlist. This trusts only
the verified leaf key; do not enable a blanket certificate-error bypass when
sending portal credentials. Read credentials privately at runtime and omit them
from results, URLs and command output.

The initiative's `live-browser-smoke.cjs` implements this with Node's `tls` and
`crypto` modules. The separate Python HTTPS check uses ordinary CA and hostname
verification and already passed. Browser verification result is recorded in
`archive/2026-09-14-portal-planning-question-controls/live-browser-results.json`.
