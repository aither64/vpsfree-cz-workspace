# Mandatory change review: general lane

Reviewed organization commits
`0a9c974994746e2a6d9d74e83cde8abbf0e65f0a..54b1d7a3f3cbfc4261abbe2fc3632d0908599696`
against the initiative plan, state, review packet, repository guidance, the
generic runtime at `bcbaf825d71285cbbd05b56e78bc386f2df480bd`, the consuming
workspace flake, and the pinned vpsAdmin/vpsAdminOS dependency interfaces.

## Blocking

None.

## Important

None.

## Advisory

### A1. vpsAdminOS documentation names a nonexistent refresh failure

- Location: commit `35a7090c8c9e0c77f6ba3ac742409200500a4c4f`,
  `dev-clusters/vpsadminos/README.md:120-124`.
- Evidence: the documented sentence says an update stops at the first failed
  copy, activation, or refresh. The vpsAdminOS implementation at
  `dev-clusters/vpsadminos/bin/devcluster:581-617` builds the configuration,
  copies each closure, and activates it; it has no refresh phase or refresh
  command. Refresh is specific to the vpsAdmin provider.
- Failure scenario: after a vpsAdminOS update fails, an operator can infer that
  a post-activation refresh may have run or failed and investigate state that
  this provider never creates. Change the sentence to mention only copy and
  activation failures for vpsAdminOS.

## Commit and coverage assessment

The four commits have distinct purposes: packaged assets, vpsAdminOS dependency
compatibility, command failure propagation with regression tests, and packaged
Nix smoke coverage. Support tests and documentation remain with the behavior
they explain. The amended final test commit introduces its final implementation
directly; the rejected `builtins.fromJSON config.text` iteration is absent from
the reviewed history. Commit subjects and bodies explain the final behavior and
rationale, and the worktree was clean at review.

The installed-source checks cover the original missing defaults and out-of-flake
runner source failures. The runner build covers the current vpsAdminOS overlay
arguments and source-gem configuration. Command tests exercise both stable
provider implementations through the real lifecycle/credential lock functions,
including failed builds with and without a retained result, credential failures,
copy and activation failures, vpsAdmin refresh failure, environment retention,
and lock release.

## Residual gaps

- The corrected packaged smoke app was still rerunning when this review was
  recorded. Its completed result must be recorded before deployment.
- The review did not run VM tests. Real bridge-network start, readiness, update,
  stop, restart, and retained-data behavior for both providers remains the
  planned integration acceptance after review and cache verification.
- The command regression tests stub Nix, SSH, OpenSSL, and Git. They establish
  shell control flow and retained-link behavior but do not prove real closure
  copy, activation, certificate-tool, or runner-process behavior.
- The consuming workspace revision pin and candidate profile deployment are
  intentionally outside this reviewed organization commit range and remain to
  be verified through the generic runtime's package-generation and transition
  contract.
