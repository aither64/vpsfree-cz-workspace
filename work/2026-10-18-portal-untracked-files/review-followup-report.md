# Follow-up final independent review

No findings. The blocking global-exclusion finding in `review-report.md` is
resolved for the supported configuration boundary. The original report is
preserved as evidence for the superseded heads.

Reviewer: the same standalone `/root/final_review`, assigned
`gpt-6-astra` / `xhigh`. Reviewed all four mandatory lanes directly, without
delegation or application edits. Applicable repository/workspace instructions
were unchanged across the baseline refresh.

## Correction and verification

`portal/internal/repository/source.go:152` now asks Git for only the effective
`core.excludesFile` path using the normal system, global and repository config
files. It passes that single setting to the isolated untracked-file query.
The setting is passed as a process argument, without shell interpretation.
Git retains ownership of path expansion, configuration precedence and exclude
matching. A missing setting retains Git's standard default exclude location;
unexpected configuration errors, timeouts and output-limit failures reject the
request.

The configuration-reading path has one production caller and uses the existing
bounded execution helper. `portal/internal/repository/review.go:153` preserves
the fixed Git options, concurrency limit, deadline, output limits, cancellation
and stripping of inherited `GIT_*` variables. Other repository/object operations
continue to disable system/global configuration. Process-level `GIT_*` overrides
remain intentionally outside the supported configuration boundary, as specified
in the follow-up packet; the correction supports the operator's normal config
files.

The added HTTP regression checks that ordinary Git excludes the synthetic file
and that the project, shared-workspace and unpublished tracking readers all
return 404. It also checks that index membership and explicit artifact
publication still grant access. I independently ran this committed regression
through the repository's Nix shell, with `-mod=readonly` and the absent provider
catalog fixture:

```text
go -C portal test -mod=readonly ./internal/web \
  -run '^TestSourceFilesRespectConfiguredGlobalExcludes$' -count=1
ok github.com/aither64/dev-workspace/portal/internal/web 0.411s
```

The lead reports the final broader Source/WorkspaceSource suite passing in
3.744 seconds. All three final diffs passed independent `git diff --check`.
No longer checks or deployment were launched by this reviewer.

The correction remains proportionate to the requested file-eligibility policy.
It does not introduce a new public API, persisted format or general policy
framework. The portal guide now explicitly includes the configured global
ignore file. The original review's conclusions about confinement, repository
identity, artifact publication, preview limits and archived final-commit reads
remain valid. The range-diff shows only this correction, its regression and its
documentation added to the previously reviewed implementation.

## Exact final branches and consumer pins

Reviewed each complete base-to-head series and final diff:

| Repository | Base | Head | Commits |
| --- | --- | --- | --- |
| dev-workspace | `9e66eb84c204cd83fcd2a891a0d052c1e32a77de` | `c1c620f91a04a70d599d208953b412a466981999` | 1 |
| workspace | `a243ff2bfbabdb8bf23cc010adf2b692e77ba644` | `2b60e845de29aef76f3b31690f00e74bc0b2f614` | 1 |
| vpsfree-cz-configuration | `a4847bd6bbf2a62c107cff30b47452a60548a33e` | `cf1271132140ca69776c6b24efce7891a531c736` | 1 |

All worktrees were clean at these exact heads, and every listed base is an
ancestor of its head. The supported upstream baseline changes are outside these
feature ranges. The relevant source reader, Git helper, session manifest and
source HTTP implementation were unchanged between the old and new runtime
bases.

The workspace retains its nested runtime selection beneath the same site
extension. Its only changed lock node is `dev-workspace`; configuration's only
changed lock node is `devWorkspace`. Both select
`c1c620f91a04a70d599d208953b412a466981999` with matching NAR hash
`sha256-AG9C/vCmBRdkr5PB5WhctfjFofq5i4DKTB51UPX8L3U=`. All other lock nodes
remain equal to their current baselines. The original consumer/topology
conclusions therefore still apply.

## History, repeated streams and migrations

The runtime correction is folded into its single owning behavior commit with
tests and documentation. Each consumer has one final selection commit; the
configuration commit retains its generated confctl history. No obsolete
approach, redundant follow-up or superseded feature-pin commit remains in any
reviewed branch.

Repeated update streams have been consolidated. The final branch histories
contain no repeated runtime-selection stream requiring further consolidation.
Matching pins in the two separate consumers remain necessary for their distinct
package and host configuration inputs.

**No migrations.** The feature introduces no schema, persisted-format or
lifecycle-journal changes. There is no migration lineage to repair or retain.
The packet confirms that none of the feature revisions was merged, released or
deployed. Old software retains readable state and narrower file eligibility;
the correction does not change deployment ordering, require fleet coordination
or alter the existing forward-only package recovery contract.

## Disposition and remaining checks

The final independent review gate is satisfied for the exact heads above.
The lead may proceed to the planned packaged/build/CI checks, composed deployment
validation and coordinated live acceptance. Those results are not established
by this review. The original Rust design link and disposable untracked/ignored
file checks still need validation on the deployed runtime. Deployment reservation
ownership and separate default-branch integration approval remain in force.
