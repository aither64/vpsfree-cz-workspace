# Architecture and repetition review

Reviewed commit `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8` against
`e5ed479f9d4058556dcf225b4c16afd5b9f0051a` in
`vpsfree-kb-contracts`.

## Findings

No Blocking, Important, or Advisory findings.

The image-selection responsibility remains at the existing provider boundary.
`tests/suite/kb/guix.nix:126-135` asks `osctl` for the `latest` Guix image and
then reads the imported container's concrete `version`; it does not duplicate
the repository's tag-resolution rules. At pinned vpsAdminOS revision
`6bdf458fd9105379860234ff33d352e55844f08f`,
`osctl-repo/lib/osctl/repo/remote/index.rb:21-33` owns exact-version/tag
resolution, `osctld/lib/osctld/container/importer.rb:26-33,103-117` imports the
selected archive's container configuration, and
`osctld/lib/osctld/container.rb:741-763` exposes its concrete version through
`ct show`. This supports the new assertion that the stored value is neither
empty nor `latest`.

The suite itself is the right owner for run-scoped image identity.
`tests/suite/kb/guix.nix:113-135,217-226` captures one concrete version in the
suite setup, shell-escapes it when creating the deployment target, and verifies
the target matches. The pinned runner executes suite setup before examples
(`test-runner/lib/test-runner/test_evaluator.rb:644-672`), and both closures
share the Ruby local, so selecting the target is ordered after resolution.
This local state avoids a new framework interface or cross-project contract.

The two fixture commands retain small, readable test-specific setup. Their
shared vendor, variant, distribution, and timeout text does not encode a new
behavioral rule that warrants extraction; the differing version source and
the explicit identity assertion are the behavior under test. No adjacent Guix
suite or consumer repeats the new resolve-once rule.

The README change at `README.md:195-202` describes the same suite-owned
behavior and introduces no second source of executable policy.

## Residual validation gaps

Quick evaluation and generated-Ruby syntax checks do not exercise the live
image repository, imported archive metadata, or the captured value across the
full hook/example lifecycle. The planned focused
`kb/guix#reconfigure` VM run should confirm that `latest` resolves to a
concrete version, the second fixture can be created by that exact version, and
both identity assertions pass. Feature and merged-master CI remain the broader
regression checks.
