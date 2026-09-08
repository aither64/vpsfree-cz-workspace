# Python strict verification and the retained development CA

Python 3.13 urllib rejected the retained vpsAdmin development cluster CA with
`CA cert does not include key usage extension`. The certificate remains
accepted by the ordinary curl/browser verification policy; Python now enables
stricter X.509 checks by default.

For a one-off check against this explicitly loaded development CA, use
`ssl.create_default_context(cafile=...)`, then clear only
`ssl.VERIFY_X509_STRICT` from that context's `verify_flags`. This retains CA
chain, hostname, and expiration verification. Do not disable certificate
verification globally or recreate a running cluster's CA for a smoke check.

Read-only authenticated Mailpit API discovery succeeds with this context.
Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
