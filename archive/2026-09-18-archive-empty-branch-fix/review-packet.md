# Mandatory change review packet

## Requested outcome

Fix `dev-session archive` so a registered feature branch may remain unpushed
when its local head exactly equals the portal manifest's `initial_base_sha`.
The command must still fetch the configured remote default branch and prove
that this head is an ancestor. Branches with feature commits must retain the
existing exact local/remote feature-head requirement. The same rule must apply
to archive retries and recovery verification.

Acceptance requires the unchanged `2026-09-14-kernel-history-fix` session to
archive after the fixed runtime is deployed and health-checked on aitherdev.

## Initiative and revisions

- Initiative: `2026-09-18-archive-empty-branch-fix`
- Plan/state: `work/2026-09-18-archive-empty-branch-fix/`
- Runtime worktree: `worktrees/2026-09-18-archive-empty-branch-fix/dev-workspace`
- Runtime base: `8c6f7025fc3c86b02b602dbd1f478c3a6de460f3`
- Runtime head: `fe67863`
- Configuration worktree carries the deployment pin at `6ac2068`; the
  consuming workspace carries the package pin at `e4bfa8d`.

## Change set and boundaries

The runtime commit owns the archive proof, regression tests, and lifecycle
documentation. The shared proof helper checks remote-ref existence with `git ls-remote`,
distinguishes Git's no-match status from transport/authentication failures,
fetches the default branch in every accepted case, and preserves exact-head,
worktree, ancestry, journal, manifest, retry, and retained-ref behavior.

There is no manifest, journal, API, database, protocol, or NixOS schema change.
No feature branch is deleted or pushed by this change. Configuration pinning and
aitherdev deployment are later operational steps, not part of the runtime
commit. The requested final archive is performed only after deployment health
checks.

## Quick verification

- `git diff --check`: passed.
- `nix develop --command ruby -c libexec/dev-session`: passed.
- Focused new tests: passed, one test each for unchanged/unpushed acceptance
  and changed/unpushed rejection.
- Archive-focused suite: 19 tests, 401 assertions, 0 failures.
- The first packaged flake check at `a82af45` found one compatibility
  regression in `test_automatic_archive_keeps_registered_branches_after_worktree_removal`.
  The final head narrows the no-push exception to registered worktrees, and the
  failing test plus the archive suite pass locally.
- The initial `bundle exec` attempt was invalid because this repository has no
  Gemfile; the corrected direct Ruby invocation through the Nix environment
  passed.

## Risk and compatibility

Risk classification: high. The code controls destructive lifecycle operations,
retry recovery, deployment ordering, and mixed old/new runtime behavior.

The exact-base condition is backward compatible: old runtimes reject absent
feature refs safely, while the new runtime accepts only a valid recorded base
with no feature commits. Remote refs that exist must still match; unexpected
Git failures remain fatal. Rollback is available through the previous
`workspace-host` profile and aitherdev configuration generation.

## Review lanes

Run General, Architecture and repetition, Scope and proportionality, and Risk
and compatibility. Review the committed runtime diff against the base, local
repository guidance, lifecycle documentation, tests, and the deployment and
rollback assumptions above. Report Blocking, Important, and Advisory findings
with file/line evidence; do not edit files, retry checks, deploy, or launch
nested reviewers.

## Review remediation

The Luna Architecture reviewer identified duplicated proof logic and a missing
retry regression test. The implementation was amended to centralize the
conditional fetch and exact-head proof in `archive_branch_proof`, recheck an
initially absent feature ref after fetching the default branch, and cover an
interrupted archive retry for an unchanged unpushed branch. The final
compatibility fix narrows the no-push exception to registered worktrees so the
existing missing-worktree guard remains intact. The final General and Risk
reruns against `fe67863` reported no Blocking or Important findings.
