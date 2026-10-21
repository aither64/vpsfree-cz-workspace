# Explicitly enable HTTP/2 for plaintext nginx fixtures

The pinned NixOS nginx module emits `http2 on;` only for a vhost with SSL and
`http2=true`. A plaintext fixture that sets only the option remains HTTP/1:
hyper-h2 sends a connection preface and sees HTTP/1.1 400/connection closed.

For an intentional local h2c fixture, set vhost extraConfig to `http2 on;`.
This is test-only; public TLS/ALPN still requires separate live acceptance.
Pinned nginx1.30.6 syntax and bounded SETTINGS/unauthenticated401 checks confirmed
the correction. Keep GOAWAY/stream reset diagnostics to distinguish transport
setup from authorization failures. Do not weaken auth/rotation assertions.

Evidence: work/2026-10-21-aitherdev-observability-access/verification-02.log and
verification-fixture-fix.diff; final retry results stay in that session.
