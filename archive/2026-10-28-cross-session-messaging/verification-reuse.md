# Exact verification evidence

Runtime e9153e614e44766d0f0efd6721b34b7bf2f4c14a, CI run 40678431473.
final-check-derivations.json evaluates the final locked source. Both below
identities appear in the retained successful CI log and their jobs passed:

- session-archive-lifecycle: `/nix/store/2p8m9jdkrw445whfamc1ixp2c532ciyq-vm-test-run-dev-workspace-session-archive-lifecycle.drv`, CI job archive passed.
- session-creation: `/nix/store/h6x8274lgk2krd0fyw5gx9bzpm1p65ia-vm-test-run-dev-workspace-session-creation.drv`, CI job creation passed.

Reuse these successful exact derivation/input identities under the verification
procedure. No source changed after CI. The full local aggregate is not recorded
as passing: two archive runs expired at browser initialization, before an archive
request; no JavaScript error was captured. Serializing local VMs did not resolve
it. CPU pressure observed afterwards did not establish ongoing contention, so
that explanation remains unproven. Browser initialization code is unchanged by
this feature. The dedicated communication acceptance test passes in Chromium and
Firefox on this host. Retain the local timeout as a verification-environment
limitation, without claiming its precise cause or a local archive pass.

All fast/package checks passed in CI and the local Go variants passed. Local
host-module-idempotency passed. The local session-recovery-boot VM subsequently passed (344.15s), and both
deployment builds passed. System activation and both system links are verified.
Application activation currently waits for active work to finish; see rollout.md. No further
archive/creation rerun is needed unless new evidence changes this conclusion.
