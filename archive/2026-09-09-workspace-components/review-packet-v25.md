# Mandatory change review packet: pre-mutation and trust isolation

## Outcome and exact ranges

Complete the reusable workspace extraction while preserving the existing
aitherdev password, CA, TLS identity, authentication meaning, sessions, URLs
and service identities. Host reconciliation must reject unsafe physical state
before it mutates credentials or CA state, validate retained TLS material only
against the configured local CA, and remain idempotent across locales.

- `codex-web`: review
  `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`.
  It is unchanged since the clean v11 review.
- `dev-workspace`: review
  `f39f8e62097b5e9da9de8a5eb678131b1e478e35..e4c75076573ed2e986298626a80309a93e07d93a`.
  The owning host implementation and VM are in `a7f1e20`; public wording is in
  `3a2ccc1`.
- `vpsfree-cz-workspace`: review
  `26606cfa0134ce3680cf592f9ab3c345683fbdc2..42729432a8723648112cdd176497569d86bc23c2`.
  The branch is a descendant of current shared `master@26606cf`.
- `vpsfree-cz-configuration`: review
  `7481618dacab04bfd5b09bc730c373c2d2bf14d7..afc5a3f30aee330ddcceafbd8fe9a4b7236a4d3f`.

All worktrees are clean and equal their pushed feature refs. The exact chain is

`vpsfree-cz-workspace@4272943 -> dev-workspace@e4c7507 -> codex-web@e8655b7`

Configuration `afc5a3f3` pins `dev-workspace@e4c7507` with NAR
`sha256-iN4P2rZQzoCukmLMTvwigLo74iEZacWyJb9TkLWsCG0=` and therefore the same
nested `codex-web@e8655b7`.

## V24 findings and remediation

V24 Scope was clean. Architecture and Risk independently found a Blocking
self-ancestor bind escape: the physical topology validator skipped record
pairs belonging to the same managed-directory index. Risk also found an
Important CA alias issue because existing CA files were chmodded and chowned
before canonical and cryptographic validation. General found a Blocking
pre-mutation ordering issue because the selected TLS pair was inventoried only
after directory, auth and CA mutation, plus an Important trust-isolation issue
because `openssl verify -CAfile` could still consult an ambient CA directory.

The remediation:

- rejects a repeated device/inode identity within a single managed path before
  cross-inventory relationship comparisons;
- losslessly parses a valid `current` target and adds its selected pair to the
  managed inventory immediately after acquiring the protected lock, before
  credential, auth or CA mutation;
- retains the later exact target reread and selected-pair inode comparison;
- rejects existing CA key or certificate files that are mount points, have a
  link count other than one, or lack exact root ownership and modes `0600` and
  `0644`; unsafe existing files are never normalized in place;
- verifies generated and retained CAs and retained leaves with explicit
  `-no-CApath -no-CAstore`, so only the supplied CA file is trusted; and
- documents the existing-CA and local-trust boundaries in the public README.

The VM now proves:

- a parent bind-mounted onto its child with an absent final path is rejected
  without creating the escaped output or changing password, auth or CA bytes;
- malformed hard-linked and file-bind-mounted CA certificates are rejected
  without changing the aliased source metadata/content or unrelated state;
- an unsafe selected pair combined with malformed auth bytes and metadata is
  rejected before the auth file or other state changes; and
- an otherwise conforming foreign-signed leaf offered through a hashed ambient
  `SSL_CERT_DIR` is rejected and rotated exactly once to the configured CA.

## Verification

For the exact committed `dev-workspace` tree
`972a228fea82ff77ed4861ebb8aeabb6d17377a2`:

- Nixfmt and `git diff --check` pass;
- `nix flake check --no-build` evaluates every output;
- `nix build .#checks.x86_64-linux.host-module --print-build-logs` passes the
  generated-script ShellCheck and pure path fixtures; and
- `nix build .#checks.x86_64-linux.host-module-idempotency
  --print-build-logs` passed the complete NixOS VM in 1,099.01 seconds.

The first VM attempt reached the new foreign-trust fixture after every earlier
new case passed, then failed because `openssl rehash` was given a directory
containing the private key. Moving the fixture key outside the hashed trust
directory corrected the test setup; the complete rerun passed. Both runs used
the cached NixOS kernel and initrd, with no local kernel compilation.

Workspace and configuration no-build flake checks pass. The configuration pin
was generated only through `confctl inputs channel set --commit`; its Nixfmt,
commit and rebase hooks passed inside the Nix shell, and `.bin`/`.bundle` were
removed. All four ranges pass `git diff --check` and contain no fixup commits
or repeated input-update commits.

Exact-head dev-workspace Actions run `34491981369` is in progress. Cancellation
of superseded run `34483741579` returned HTTP 403 because the configured token
lacks Actions write permission; the stale run is not accepted as evidence for
the current head.

## Compatibility and deployment

Risk is high because the work changes authentication-derived state, TLS
persistence, public Nix options, host activation, deployment and rollback.
Persisted formats, paths, owners, credential meaning, SANs, service identities,
URLs and runtime/session records remain unchanged. Existing correctly owned,
single-link CA files and valid local-CA leaf pairs remain readable by old and
new generations. Unsafe alias state now fails closed instead of being
normalized. Rollback can consume state written by the new generation, though
the older reconciler may resume harmless derived bcrypt or leaf churn.

The retained original aitherdev TLS pair has already been checked read-only for
exact SANs, local-CA signature, key match, canonical PEM and required metadata.
After clean review, deploy the configuration feature directly to aitherdev,
atomically restore that pair as `current`, and run two non-C-locale
reconciliations to prove the original leaf/key and password/CA hashes remain
exact. Then switch the user profile through the stable installed
`workspace-host` command and restore the exact eight clients.

Default-branch integration, releases, archive, delete and session stop remain
out of scope. The user authorized aitherdev deployment only.

## Review request

Rerun the General, Architecture/repetition and Risk/compatibility lanes affected
by v24, plus Scope/proportionality because public wording and downstream heads
changed. Focus on self-ancestor detection, selected-pair pre-mutation ordering,
CA hard-link/file-mount preservation, isolated OpenSSL trust, VM assertions,
commit ownership, exact pins, mixed-generation behavior and proportionality.
Report Blocking, Important and Advisory findings with direct evidence and a
specific remediation; explicitly report a clean lane.
