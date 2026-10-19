# Final package and resource proof

The exact-head guarded batch completed all declared package checks and built
`/nix/store/cfrf8mjcww7lks1ylqzgfay5920ab029-dev-workspace-0.2.0`, derivation
`/nix/store/gi1i29akjbha530a7an99hiyqx1d6zs9-dev-workspace-0.2.0.drv`.
Provider327, runtime45d4f13, extension67c9a60 and workspace8876efbf were clean.
Its sequential set-e driver reached BUILT_FINAL_FIXTURE_CANDIDATE only after
provider full flake checks, runtime normal checks (excluding the unchanged
host-module-idempotency VM), extension/workspace full checks and package build.
The existing host/module VM evidence remains qualified to unchanged source.

The overall batch then exited1 after1254s in the separate managed test-binary
derivation, before CI observation. That failure does not change the preceding
package result. The original exit file remains1. Parent recorded the verified
package phase separately in package-checks.status; no batch status was rewritten.

The fixture compiled and installed, then failed a silent inherited postFixup
assertion requiring $out/bin/dev-session, which its single-binary install does
not create. The native Nix log ended after ordinary stripping; stripping was
not established as the failure. Parent read the complete source postFixup and
the failed derivation's actual env.postFixup to identify its first unavailable
helper check. The private fixture expression now owns its postFixup and checks
its own executable. Production package postFixup remains intact and passed.
Fresh utility final_fixture_ci_verification owns only corrected fixture build
and exact final CI; it does not repeat passed package suites.

Git identity diagnostics in the original log had no corresponding failed test
result. The watcher independently reported passed fixture/contract summaries;
no test setup change or retry was made on the basis of those diagnostics.

Parent's exact resource check passed for this candidate: all18 installed public
provider resources match provider327; native ELF/version/SHA, full original
read-only model catalog, config schema and saved team catalog are identical to
their pinned identities. Runtime contract/service template and team resources
match the source. binary-identity.json now records this actual candidate and
all final heads, while preserving the prior identity separately.

Private original evidence: final-package-verification.log/.exit/.elapsed,
post-fixture-package.json/-path under /tmp/automatic-session-slugs-. The fixture
failure derivation is pid17sn90ywlcwmhh00pi1przh6xq4jd-managed-session-naming-fixture.drv.
CI, immutable fixture manifest, actual managed VM, deployment and live MODEL/
custom/replay are separate gates; package success does not imply deployment.

Corrected fresh fixture/CI batch passed exit0/32s. Fixture binary is
/nix/store/dyhxydd57pb8qxy9hbyjndc2z4f2jhg1-managed-session-naming-fixture/bin/managed-naming-fixture.
All three exact CI runs completed success with matching provider327/runtime45/
extension67:37182636158,37184684052,37184744414. Raw JSONs and full corrected
log/status/elapsed remain private. No operation remains from that batch.

The later actual managed-service VM passed exit0/152s against the immutable final
manifest and package; see [managed-child-provenance.json](managed-child-provenance.json).
The initial profile switch then refused before selection because another
initiative's turn was active. After the user's "try again", the normal retry
passed0/69s and selected this exact candidate as generation82. Live verification
passed0/about15.8s, including actual MODEL/custom/replay409; both retained canaries
completed idle. See [deployment-observation.md](deployment-observation.md) and
[live-verification.json](live-verification.json). Final source/package/CI/VM and
deployment/live gates are complete; default integration remains unauthorized.
