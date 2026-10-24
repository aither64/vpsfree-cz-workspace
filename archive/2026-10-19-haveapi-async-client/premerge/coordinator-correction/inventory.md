# Coordinator repository Ruby selection candidate

Preparation only. Independent committed-deliverable review is next; the selected
runtime has not been changed and no merge preparation was retried.

- Repository: `dev-workspace`, feature `2026-10-19-haveapi-async-client`.
- Base: `09a407953026514ae84be81dab9442fd74b6a362`.
- Head: `dce4784fe0069b061dd76cdf689e2099b4b0e66d`.
- Tree: `5dc33558cc877c26573b9489aab13eb2e4c1ac89`.
- Clean index and working tree; one commit, three paths, 22 additions/7 deletions.
- Author and committer: Jakub Skokan <jakub.skokan@havefun.cz>.

Complete series: one cohesive `coordination: validate hooks with the repository
shell Ruby` commit. No superseded approach, follow-up fix, unused compatibility
path, migration, dependency/channel/input update, lockfile or generated-artifact
stream. No migration was merged, released, deployed or externally consumed in
this package because it introduces none. No pins or runtime selection changed.

The only production change substitutes shell-PATH `ruby` for `RbConfig.ruby` in
`prepare_merge_hooks`. The existing initialized-shell fixture records its Ruby
shim selection and delegates to a real Ruby interpreter to execute the actual
validation program. The missing-dependency fixture supplies runnable Ruby and
asserts the absent gem diagnostic. Environment restoration remains covered on
success and failure. Documentation explains why the repository Ruby is selected.

Quick checks under the repository's `nix develop --command`:

- Old production code plus strengthened selection fixture: expected failure at
  the interpreter-selection assertion (1 test, exit 1); `baseline.log`.
- `ruby -c libexec/workspace-coordination-execution.rb` and
  `ruby -c test/workspace_coordination_test.rb`: PASS.
- Existing four tests for prepared hook transport/restoration, initialized-shell
  interpreter/environment capture, missing Overcommit dependency, and fresh-source
  real checkout hooks: PASS, 4 tests/30 assertions, exit 0; `quick.log`.
- `git diff --check` before and after commit: PASS.
- Normal Nix `git commit -F` with command-scoped user identity: exit 0. No declared
  hook framework, configured hook path, or active non-sample Git hook was found;
  no bypass. Dirty-tree and deprecated Nix attribute warnings are retained in log.

Source/test bytes were unchanged after quick checks; the later change was the
lead-approved documentation code font/wrapping pass. `receipt.json` records the
full identities, evidence hashes, clean state and warnings. `final.diff` and
`series.txt` cover the complete branch. No push, long suite, package build,
activation, private helper, retained-gem repair or HaveAPI/WebUI edit occurred.

After review, the lead owns authorization of packaged coordinator checks and the
independent real-ABI proof. Shared runtime rollout remains a separate decision.
