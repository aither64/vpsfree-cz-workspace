# Review: dev-workspace host-auth cost

## Requested outcome

Review the committed generic host-auth amendment for correctness, security,
scope, architecture, compatibility and verification adequacy. The change must
keep the generic bcrypt default at 12, expose only a bounded integer option,
regenerate the derived htpasswd atomically when the declared cost changes, and
support an aitherdev-only cost 5 deployment without changing the password, TLS,
Basic Auth boundary or user-profile runtime.

Acceptance requires exact two-digit cost validation and generation, idempotence
at a stable cost, failure preservation of the previous complete auth file,
mixed-system-generation rollback behavior, deterministic non-timing regression
checks, and a credible long VM/live verification plan. Report findings as
Blocking, Important or Advisory. State residual risks and test gaps when there
are no findings.

## Initiative and scope

- Initiative: `2026-09-29-portal-performance`
- Plan: `work/2026-09-29-portal-performance/plan.md`
- State: `work/2026-09-29-portal-performance/state.md`
- Design amendment: `work/2026-09-29-portal-performance/design.md`, section
  `Host-auth amendment: failed live latency gate`
- Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-29-portal-performance/

This incremental review covers only the committed generic module unit in
dev-workspace. The site configuration input pin and aitherdev option are a
separate later commit/review in `vpsfree-cz-configuration` after this module
head is approved and pushed.

## Repository and commits

- Repository/worktree:
  `worktrees/2026-09-29-portal-performance/dev-workspace`
- Base: `b9465ab61dfc4e9820e312b062cb7b96ed3f09b0`
- Head: `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40`
- Commit under review:
  `ec05cb9 host: make portal bcrypt cost configurable`
- Diff: `git diff b9465ab61dfc4e9820e312b062cb7b96ed3f09b0..ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40`

The single commit intentionally bundles the option, reconciliation behavior,
provider-level evaluation/VM coverage, deterministic synthetic harness and
owning operator documentation. They define and verify one security-sensitive
module contract and should revert together. The configuration consumer pin and
site setting remain separate because they have independent deployment,
rollback and integration ownership.

## Files and public contract

- `nix/host-module.nix`: adds
  `services.dev-workspaces.auth.bcryptCost`, integer bounds 4 through 17,
  default 12; derives a two-digit cost and a concrete anchored validator; uses
  the same cost for `htpasswd -niBC`.
- `nix/tests/host-module.nix`: checks default/custom/boundary/invalid values and
  exact concrete generated scripts at 04, 05, 12 and 17.
- `nix/tests/host-module-idempotency.nix`: extends the existing NixOS VM test
  for 12 -> 5 -> 12 -> 5 transitions, stable reruns, auth success/denial,
  malformed/current-cost inputs, publication failure and concurrent readers.
- `test/host_auth_benchmark.py`: uses fresh synthetic 256-bit secrets, validates
  encoded cost and correct/wrong-password behavior, and reports timing without
  using timing as a portable pass/fail contract.
- `flake.nix`: exposes the deterministic benchmark as a flake check.
- `docs/workspace-portal.md`: documents the option, random-secret-only low-cost
  exception, regeneration, mixed-generation rollback and recovery.

The owning component is dev-workspace's `nixosModules.host`. The actual site
consumer is `vpsfree-cz-configuration`, whose aitherdev machine imports this
module through the `devWorkspace` input. That consumer remains pinned to the
old module during this review. After approval, its feature branch will use
`confctl inputs channel set --commit dev-workspace devWorkspace <reviewed-head>`
and set `services.dev-workspaces.auth.bcryptCost = 5`. Unconfigured consumers
retain default 12. Nginx consumes the same bcrypt file format at either cost.

## Risk and compatibility

- Overall risk: **High**. This changes authentication work factor, privileged
  host reconciliation, deployment ordering, rollback and mixed-generation
  behavior.
- Selected lanes: General, Architecture and repetition, Scope and
  proportionality, Risk and compatibility.
- Reviewer: retained `reviewer0`, saved `gpt-6-sol` with `xhigh` effort,
  read-only. No model or effort override.
- There are no database, session, journal, runtime-authority, manifest, ledger,
  protocol or on-disk format migrations. The htpasswd remains derived state in
  the existing bcrypt format; **no migrations**.
- The additive Nix option is forward compatible for unconfigured consumers.
  An old module cannot evaluate a configuration that retains the new option;
  pin and setting must therefore deploy together.
- Rolling back to the old module after removing the new setting detects cost 5
  as invalid and atomically regenerates cost 12 from the unchanged password.
  This restores compatibility but can restore the measured latency problem.
- Failure must keep the previous complete htpasswd. Credentials, CA, TLS state,
  ownership/modes and nginx Basic Auth remain unchanged.

## Decisions and non-goals

- User approved live aitherdev deployment and later default-branch integration
  after all gates pass.
- Cost 5 is accepted only for this site's generated 64-hex, 256-bit random
  secret over TLS. It is not guidance for human-chosen or reused passwords.
- Rejected alternatives: changing the generic default, auth caching, cookies or
  bearer sessions, bypassing auth for assets/APIs/SSE, request batching as an
  auth workaround, manual htpasswd edits, password rotation and automatic
  hardware calibration.
- No Codex, codex-web, site extension, user-profile package or unrelated host
  configuration change belongs in this unit.
- Timing measurements are diagnostic. Encoded cost and verification behavior
  are deterministic gates; browser p95 remains the live acceptance gate.

## Quick verification

Passed on the host against the committed/staged final implementation before
commit, with no long VM execution:

- `nix flake check --no-build --show-trace`
- `nix build .#checks.x86_64-linux.host-module .#checks.x86_64-linux.host-auth-benchmark --no-link --print-build-logs`
- `nixfmt --check flake.nix nix/host-module.nix nix/tests/host-module.nix nix/tests/host-module-idempotency.nix`
- Python syntax/AST checks for `test/host_auth_benchmark.py` and the embedded VM
  `testScript`
- `git diff --check`

The focused build generated concrete validators and generators at costs 04, 05,
12 and 17 and rejected unevaluated placeholders. The synthetic Apache 2.4.68
check accepted the correct password and rejected the wrong password at both 5
and 12. Its latest cost-5 ten-verification batches were 124, 118, 105, 124 and
122 ms, all under the 0.5-second rollout diagnostic budget. Cost-12 batches were
roughly 3.3 to 3.6 seconds. These timings are evidence, not portable unit-test
thresholds.

The first pre-commit focused build exposed an unevaluated Nix interpolation;
the implementer replaced it with a concrete Nix-computed pattern. The next
build exposed the dropped intentional ShellCheck suppression; it was restored.
Both findings were fixed before commit, so there is no superseded committed
auth implementation in this incremental commit.

The first long-VM attempt stopped before boot because Ruff reported two F541
violations in the embedded Python test: two concatenated string fragments kept
an unnecessary `f` prefix. The exact two-prefix removal was checked with
Nix parsing, nixfmt, Ruff F541 selection and `git diff --check`, then folded
into the still-unmerged commit as `ec05cb9`. It changes no test behavior or
reviewed host-module contract, so the mandatory review did not need a rerun.

## Remaining checks after review

- Fresh Luna/low watcher runs the long
  `checks.x86_64-linux.host-module-idempotency` NixOS VM test.
- Push exact reviewed dev-workspace head and confirm CI.
- Pin the exact head and add the aitherdev-only option in
  `vpsfree-cz-configuration`; review that configuration diff separately.
- Fresh watcher runs aitherdev `confctl build`, dry activation, switch and
  deployment verification.
- Verify encoded cost/permissions without recording the hash or secret,
  authenticated success, unauthenticated/wrong-password denial and stable
  reconciliation.
- Repeat 30 no-scan and 30 overlapping dry-run-scan browser loads; both
  nearest-rank p95 usable values must be at most two seconds with no load
  failures.

## Reviewer instructions

Read `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all four
selected lane references. Inspect repository-local `AGENTS.md`, the commit,
diff, adjacent implementation/tests/docs, actual generated script semantics and
the stated configuration consumer. Perform the review directly and remain
read-only. Report concrete findings with file/line and commit references, or
state clearly that there are no findings and list residual risks/test gaps.
