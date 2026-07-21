# 2026-07-20-security-advisory-review

## Goal

Register `security-advisories` in the workspace project map and prepare an
isolated feature worktree for reviewing security advisories against current,
typed vpsAdmin Node evidence once the user supplies an authentication token.
Investigate the production token-creation failure, fix it, then complete an
evidence-backed review of every advisory against every active Node.

## Affected repositories

- Top-level coordination repository: project-map documentation only, committed
  directly on `master`.
- `security-advisories`: isolated review branch and worktree, initially with no
  source changes; inspect the exact requested token scopes and client payload.
- `vpsadmin`: inspect the deployed token table schema and API integration.
- `haveapi`: inspect token option/scope serialization and validation used by
  vpsAdmin.
- `vpsfree-cz-configuration`: after the vpsAdmin fix is committed, reviewed,
  and pushed, pin the `vpsadmin` channel's `vpsadmin` role to that exact feature
  revision using `confctl`.
- Production vpsAdmin API data remains an external read-only review input; no
  production data changes are currently planned.

## Approach

1. Add `security-advisories` to the top-level `AGENTS.md` project map.
2. Fetch its canonical SSH bare clone and create
   `2026-07-20-security-advisory-review` from the current upstream default
   branch in the matching initiative worktree directory.
3. Keep the authentication token ephemeral: do not write it to initiative
   notes, repository files, command-line URLs, commits, or captured output.
4. After the token is supplied, verify its identity and permissions, inspect
   the repository's API and evidence documentation, then perform the requested
   read-only advisory review against typed vpsAdmin data.
5. Do not synchronize drafts, modify vpsAdmin data, or publish advisories
   without a separate explicit user request and the repository workflow's
   required review gates.
6. Trace the reported `tokens.opts` overflow from the advisory client's scope
   list through HaveAPI serialization to vpsAdmin's schema. Reproduce the size
   boundary locally if possible and report the root cause and safe remediation;
   do not implement a fix unless requested.
7. Implement the requested vpsAdmin fix as one focused commit containing the
   reversible schema migration, core schema update, migration coverage, and
   end-to-end long-scope MFA token regression coverage.
8. Run quick focused verification, commit the complete vpsAdmin change, and
   push the feature revision so the configuration flake can resolve it.
9. Set the `vpsadmin` channel's `vpsadmin` role to that exact revision with
   `confctl inputs channel set --commit` and verify the generated configuration
   commit.
10. Run the mandatory standalone change review over both committed repository
    changes before broader tests. Address significant findings, then run the
    broader verification and push the final configuration branch.
11. After authentication is available, collect one canonical typed evidence
    snapshot and assign every advisory to its own fresh standalone reviewer.
12. Classify storage Nodes by their backup/NFS workload. They do not host VPSes
    and an older kernel does not make them affected by a VPS-only trigger;
    storage is applicable only when the vulnerable operation is reachable from
    its real storage workload.
13. Independently cross-check each reviewer result, resolve all active Nodes,
    validate every dossier, and run the complete test and lint suites. Do not
    sync or publish vpsAdmin drafts without a separate explicit request.
14. Commit and push the reviewed dossier and workflow-instruction changes only
    after the mandatory standalone change review has no unresolved significant
    findings.
15. Replace the ignored per-CVE evaluation cache with a tracked
    `advisories/<CVE>/evaluation.json` review record. Keep raw production
    evidence ignored, and compare fresh in-memory evaluation results with the
    committed record before sync or readiness can proceed.
16. Normalize English and Czech public text into the same factual structure;
    remove generic user non-action statements, editorial first-person language,
    and internal storage-role explanations from public fields.
17. Recollect one coherent production snapshot after the dossier text is final,
    regenerate every tracked evaluation, run mandatory standalone review, and
    push only after the complete local and GitHub checks pass.
18. Restore the useful kernel-warning monitoring note with one factual English
    and Czech sentence on the four memory-lifetime advisories, while keeping the
    non-UAF overwrite advisory unchanged.
19. Treat periodic sample revisions and their raw evidence digest as audit
    provenance rather than conclusion drift. Before a draft write, continue to
    require the exact Node set and all per-Node result fields to match the
    committed review.
20. After standalone review, complete verification, push, and green GitHub
    checks, synchronize all five reports to vpsAdmin as drafts. Verify every
    remote draft against the committed dossier and evaluation; do not publish.

## Compatibility and deployment

The initial preparation changes only workspace documentation and creates Git
worktrees. The later review is intended to be read-only and therefore must not
change production state.

The advisory review changes local dossiers and assessment instructions only.
Evidence collection is read-only, ignored runtime state. Role-based exclusion
of storage Nodes is compatible with existing evaluations because every active
Node remains present in the output; only the real attack surface determines
whether its kernel history is applicable. No vpsAdmin draft synchronization or
publication is part of this stage.

The per-Node evaluation is now a committed review artifact rather than an
ignored short-lived cache. Its schema remains unchanged. A reviewed evaluation
does not expire solely because of age: `sync --apply` and `ready` collect fresh
evidence and require the current Node set and every per-Node conclusion field to
match before proceeding. Periodic sample revisions and the resulting evidence
digest remain audit provenance but do not by themselves change a conclusion.
This changes no vpsAdmin API, database, or protocol and remains safe for mixed
repository versions.

The authorized synchronization creates or updates vpsAdmin records only in the
`draft` state. It uses stable external IDs, remote content-revision checks, and
read-back verification. Draft creation is reversible through the ordinary
draft workflow and has no Node or VPS runtime effect. Publication is excluded
and remains a separate administrator action.

The investigated failure requires a vpsAdmin schema fix before the review token
can be issued through MFA: widen `auth_tokens.opts` from `VARCHAR(255)` to
`TEXT`, retain its existing JSON serialization, and add a long-scope MFA
regression test. This is backward-compatible with old API processes because
they read and write the same JSON value. Deploy the migration before retrying
token creation. Pinning the `vpsadmin` channel updates the vpsAdmin service
containers together, including the API and database migration service. A
rollback to `VARCHAR(255)` is unsafe while any continuation row contains more
than 255 characters. Authentication continuations expire logically after five
minutes, but their rows remain until `vpsadmin:auth:close_expired` removes them.
Before rollback, wait for expiry and successful cleanup or explicitly close the
temporary rows, then require `SELECT COUNT(*) FROM auth_tokens WHERE
OCTET_LENGTH(opts) > 255` to return zero. Assess the ordinary MariaDB DDL lock
before applying the column change. No HaveAPI, vpsAdminOS, node, protocol, or
client rollout is required.

## Testing plan

- Verify the top-level documentation diff contains the intended project-map
  entry while preserving unrelated shared-worktree edits.
- Verify the advisory worktree uses the initiative branch at the fetched
  upstream default-branch commit and starts clean.
- Record exact branch, worktree, base commit, commands, and results in
  `state.md`.
- Reproduce the exact 34-scope request against the current vpsAdmin test schema
  with MFA enabled and confirm the `auth_tokens.opts` overflow.
- Run the existing focused token-config spec to establish that current coverage
  remains green despite omitting a long-scope MFA case.
- Run the new migration spec in both directions, the focused token-config spec,
  migration-spec inventory check, `git diff --check`, and applicable Overcommit
  hooks before committing.
- After standalone review, run the broader relevant API spec groups and verify
  the configuration channel update through `confctl` evaluation/build checks
  appropriate to the affected vpsAdmin service machines.
- Verify authenticated collection returns every active Node without revealing
  the token, then evaluate all five dossiers from one fresh snapshot.
- Require one fresh standalone reviewer per advisory and independently inspect
  every resulting accepted build, historical attestation, per-Node state, and
  role-based exclusion.
- Run `bin/security-advisory validate` for all advisories, evaluate all five
  against a final fresh evidence snapshot, and run full RSpec, RuboCop, and
  Overcommit checks before committing.
- Verify `evaluate` writes beside the dossier, missing reviewed evaluations fail
  closed, old matching records remain usable, and fresh mismatches block both
  apply and readiness without rewriting the committed record.
- Verify all five tracked evaluations contain the exact 13 reviewed Node IDs,
  resolved completeness summaries, matching dossier/evidence digests, and the
  storage Node as `not_affected`.
- Verify every English and Czech response uses the shared status closing and no
  public field contains generic non-action, editorial first-person, or internal
  storage-role wording.
- Verify the four memory-lifetime advisories use the exact bilingual monitoring
  sentence and the non-UAF advisory does not.
- Verify fresh sample/evidence revisions are accepted only when the exact Node
  set and every per-Node conclusion field remain unchanged.
- Dry-run all five synchronizations, apply them only after the committed branch
  passes review and CI, then run `ready` for each draft. Confirm that every
  remote report remains a draft and matches local content and Node results.
