# Forward B fast-job cancellation failure

Run40128088687, head556a6e51b141fa419d620ad0d4ccd629fd2be6f5,
completed fast job120973723284. The job ID is taken from main's saved
`forward-review-20261024/ci-snapshot.json`, not inferred from a current branch.
The failure is package Go verification, before the later Node check commands.

## Exact evidence and boundary

Complete original raw job log: `package-b-forward-fast-ci-original.raw.log`,
277217bytes,1979lines, SHA-256
`6fc137693cd9a9d03824afe887d7c825e1e24822b9f5b5b447cc959c1c69144d`.
Direct completed-job logs API succeeded while the run was active. Initial CLI
output protection refused terminal escape bytes; the successful request used
`--allow-escape-sequences` only to write the raw file, never to display it.
Initial stderr/empty output and the successful fetch stderr are retained.
Artifacts API returned `total_count:0` in
`package-b-forward-fast-ci-artifacts.json`; no native/RPC trace was available.

Workflow: unchanged `.github/workflows/check.yml`, fast step
**Build package and focused checks**. It evaluates the check attributes, excludes
host-idempotency/recovery-boot/creation/archive VMs, then builds the remaining
check set. Failed derivation:
`/nix/store/l0j90v5381w0rm9s3k2iyfnjixh734c3-dev-workspace-0.2.0.drv`;
output `/nix/store/z3v2c21x2hwd3qjlq77midf4qbkj9ngq-dev-workspace-0.2.0`.
Its `nix/workspace-portal.nix` checkPhase runs `go test ./...` after the pin and
protocol checks. Exact failing case:

`TestRetireThreadLoadedDiscoveryRefusesUnsafeEvidence/cancel`

Log1878, `client_test.go:1314`:
`cancellation changed find session conversation: Codex App Server disconnected: failed to get reader: use of closed network connection`.
The workspacecodex package failed in44.765s. Web package, including naming,
passed in98.323s. Repeated failure lines later in the log are Nix's copied tail,
not three independently observed failures. No timeout or model error is reported
at the failing boundary. Sanitized bounded excerpt and source/check identities:
`package-b-forward-fast-ci-excerpt.txt` and `package-b-forward-fast-ci-boundary.json`.

## Baseline comparison and causal limits

At failed556, both `portal/internal/workspacecodex/client.go` and
`client_test.go` are byte-identical to deployed baselineb3a6eb2. Their exact Git
blobs are8642a734e0e5dadc9ae8a2c959f617ff3a8755e4 and
5ed876f27415623d71cedf65cf08fe9e69742a4d. Baseline058ee2 introduced the retained
conversation retirement fixture. A's shared `codex/client.go` is also identical
between deployed11ec57d and refreshed6e469 (blob21e140c8536dc826e3dd97ddb932fcf45fa18f00).
The naming patch changes neither path. A new pin is not an indicated correction.

The fixture cancels the caller immediately when the server receives
`thread/loaded/list`, before replying. Pinned websocket1.8.14's
`conn.go:171–177` installs an AfterFunc that closes a connection when a write
context expires. A's `requestOn` selects a pending response or ctx.Done at1148;
its response-error branch returns the original disconnect error at1150 without
including cancellation. Thus a cancel during the send-completion window can
produce both ready events; selecting the disconnect loses errors.Is(Canceled).
B loaded-retirement discovery returns that observation error before its later
ctx check. This source-backed race matches the observed category mismatch.
The precise remote scheduling/write completion was not traced or reproduced;
that timing explanation remains an inference. No environment failure was found
in the available evidence at this boundary.

Retirement refuses before its archive call and attempt clearing. The defect is
error-cause preservation on a failed read-only observation, not demonstrated
unsafe archival or acceptance. Main and architect accepted that narrow scope.

## Released correction

Main's bounded direct brief releases only failed LoadedThreadIDs and
ReadThreadMetadata observations in loadedRetirementCandidate. If ctx.Err is
nonnil, join that cause with the original error, preserving errors.Is and
errors.As. Active-context errors retain their original identity. Successful
observations, metadata/uniqueness proofs, generic RPC arbitration, archive
mutation/receipt handling, attempt clearing, state contracts, provider and naming
behavior remain unchanged. A6e469 and all dependency files stay fixed.

The private reader seam exposes only the two read operations and supports
ordered deterministic failures. Tests cover list/metadata × transport/generic
error × active/canceled context, preserving cause and transport identity.
Real-protocol retirement tests additionally cover both cancellation stages,
retained exact attempts and zero archive calls. The original unsafe-evidence
assertions are byte-identical. A fixture-only metadata cancellation mode reaches
the second root read, after the loaded-list response.

Documentation decision: existing `docs/dev-sessions.md` already owns fail-closed
retirement and retained attempts. A local code comment records the error contract
rationale; this internal record owns CI/provenance and no product prose changes
are needed. Main's already approved naming docs are unchanged.

Before edits, exact556 source/pins, complete forward review and failure evidence
were copied to `package-b-forward-fast-ci-before-fix-556/` with36-file SHA manifest.
All original forward/source/review receipts remain untouched.

Quick regression and final verification results are recorded separately under
`package-b-forward-fast-ci-*`. The regression-red overlay removes only the two
normalization blocks while retaining the private test seam; it models the old
error behavior and is not claimed to be an unmodified old tree execution.
Main retains affected independent review and all long/native/runtime checks.
No CI rerun/trigger/wait, live operation, package selection, repository claim,
merge, deployment or session lifecycle action is part of this correction.
