# Final general exact-pin consistency review

Reviewed the final high-risk exact-pin checkpoint with the mandatory general
lane at gpt-5.6-sol xhigh:

- vpsAdmin `791ab3aa89e2f613979da6090b89785c78245db5` through pushed
  `337c9257f5e11f36afe81eba4951e267b83e2fc7`;
- vpsfree-cz-configuration
  `249bed1ee28e69a907edd09ea97a1144dbcdefeb` through committed
  `09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347`;
- vpsfree-kb-contracts `919577d0c770e47b623c591f8bf0cce4e8d30666`
  through committed `61aaf95d3dc0968728131a2cf4d4740dae6e9250`;
- the final exact assertions and unchanged operating procedure in `rollout.md`.

## Findings

No Blocking, Important, or Advisory findings in the assigned final consistency
scope.

The revision chain is internally consistent. Configuration changes only the
`vpsadminServices` lock from the recorded base to exact vpsAdmin head
`337c9257f5e11f36afe81eba4951e267b83e2fc7`; no staging, production, or
vpsAdminOS input changes. Its revision, timestamp, and NAR hash exactly match
the vpsAdmin lock in the KB contract. All 11 evaluated
`cz.vpsfree/vpsadmin/*` consumers select `vpsadminServices` at that revision,
and their final build completed successfully as generation
`2026-09-14--13-07-10`.

The KB commit records the same full vpsAdmin revision in `captures.json`,
`contract/navigation.yml`, `contract/pages.yml`, `flake.nix`, and the locked
and original fields in `flake.lock`. Its lock diff changes only vpsAdmin
metadata; the existing vpsAdminOS, nixpkgs, and other transitive locks remain
unchanged. The final canonical `bin/check` passed with no page, prose, or
capture change. Neither downstream pin tree retains any superseded feature
revision.

The commit series remains consolidated and reviewable. vpsAdmin contains the
recorder/provider commit `7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5`
followed by the repair/integration/documentation commit at the final head.
Configuration and KB each contain one final pin commit directly on their
recorded fetched bases; the generated configuration message is preserved.
All three base-to-head diffs pass `git diff --check`.

The only delta from reviewed vpsAdmin `feaa152436cf66e980c4e53f86a541bb10daae16`
to the final head is `tests/suite/supervisor/runtime-ingestion.nix`. It replaces
the timing-sensitive read of mutable current evidence with a complete
standalone synthetic report; product code, the repair command, migration, and
public behavior are unchanged. The exact literal passed the database preflight,
and the final supervisor/runtime-ingestion run passed all 11 examples, including
restart and public Rake preview/apply/idempotence behavior.

The rollout preflight asserts final configuration head
`09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347` and exact vpsAdmin pin
`337c9257f5e11f36afe81eba4951e267b83e2fc7`. The previously reviewed two-writer
mask checks, API1/migration/API2 ordering, separate quiescent repair preview and
approval, exact preview comparison, and rollback limits remain unchanged. It
also records the successful final 11-consumer build. No rollout or repair
command has been executed.

At inspection time the vpsAdmin worktree matched its pushed feature ref. The
configuration and KB worktrees had no tracked or staged changes and remained
one rewritten final pin commit ahead of, and one superseded pin commit behind,
their remote feature refs. Configuration retained only the disclosed untracked
`.bin/` and `.bundle/` caches.

## Outstanding gates

- Push configuration `09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347` and KB
  `61aaf95d3dc0968728131a2cf4d4740dae6e9250` with their recorded old-head
  leases, then verify the exact remote feature heads. Configuration has no
  branch workflow; its final 11-consumer build gate has passed.
- Monitor final vpsAdmin CI run `34836306209` and API Specs run `34836306199`
  to successful completion. Final-head RuboCop `34836306248` and i18n
  `34836306232` have passed.
- After the KB push, require its Check and Managed page runtime workflows to
  pass at exact head `61aaf95d3dc0968728131a2cf4d4740dae6e9250`.
- Capture final comparisons and finish the session's validation/tracking
  handoff after those remote checks. These are delivery gates, not review
  findings.
- Production rollout and node 400 repair remain outside this delivery. They
  require their documented later approvals and must use the exact reviewed
  artifacts.
