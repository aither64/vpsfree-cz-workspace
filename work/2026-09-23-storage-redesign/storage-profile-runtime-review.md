# Runtime maintenance policy review packet

## Requested review

Independent complete-branch review of the bounded generic runtime prerequisite,
before feature publication and its provider dependency update. This does not
declare the whole storage profile ready or authorize integration/deployment.
Overall risk is HIGH: persistent cluster state, package transitions, mixed
generations and recovery. All four mandatory lanes apply.

Selected reviewer: retained `reviewer0`, review purpose, read-only,
GPT-6.1 Sol/xhigh. Use saved settings with no override and no nested reviewer.
Read the mandatory-change-review skill and all four lane references, workspace
routes and repository AGENTS. The local workspace operator is trusted;
ordinary misconfiguration, concurrency and interruption remain in scope.

## Exact source and complete inventory

- Session: `2026-09-23-storage-redesign` in `/home/aither/workspace/ai/vpsfree.cz`.
- Repository: generic `dev-workspace`.
- Worktree: `worktrees/2026-09-23-storage-redesign/dev-workspace-maintenance-policy`.
- Branch: `2026-09-23-storage-redesign-maintenance-policy`.
- Base: `4bec20165387d567b761e43b11fdeabb096618d7`, fetched default `master`.
- Head: `8b2439938cbcbe527f2c703d88ed3c9f72f44b7e`.

The complete series is one commit:

1. `8b2439938cbcbe527f2c703d88ed3c9f72f44b7e`
   `runtime: require maintenance-aware cluster transition policy`.

The final diff has exactly three paths: canonical
`portal/internal/session/runtime-contract.json`,
`test/workspace_host/profile_transition_test.rb`, and
`docs/workspace-portal.md`. No superseded implementation or intermediate
dependency pin exists in this branch. **No migrations**; schema stays at 1.
There is no host algorithm, prompt, team, protocol, OSVM or cluster operation
change. Tests and explanation accompany the one policy boundary.

## Intent and consumers

The stopped populated cluster needs a provider maintenance hold to prevent the
old seed rewriting namespace/resource assignments during restart. The current
policy-2 provider ignores an additive maintenance record when accepting package
adoption. The existing host already requires an equal state schema/tracking
limit and a target transition policy at least its own, then calls candidate
provider adoption. This commit advances only the canonical policy to 3.

Canonical ownership/export is the JSON file, `flake.nix`'s `lib.runtimeContract`
and `nix/workspace-portal.nix`'s installed host contract. The vpsFree provider
consumes and copies the same exported file through its flake and
`nix/organization-tools.nix`; it must not hand-edit a copied JSON. The companion
provider worktree is `vpsfree-dev-workspace-storage-profile`, base
`c56f981a950ab763b71dc91c59e8b5256d478851`. Its maintenance-aware implementation
and generated runtime input update remain pending. Inspect those consumers
and the accepted [design](design.md), especially its canonical-policy section.

Acceptance is ordinary forward schema-1 adoption, explicit policy-2 refusal
before adoption/quiescing/profile mutation while cluster state exists,
candidate adoption and activation recheck, malformed/schema/tracking refusal,
and unchanged no-state behavior. Hold-bearing tests use opaque fixture bytes;
the generic host does not acquire a provider-private state parser.

## Accepted compatibility cost and deployment limits

Policy 3 ships only with the complete reviewed maintenance-aware provider
composition. It does not give old helpers new behavior by itself. Normal
switch to an old policy is refused while **any** registered cluster state
exists, including after a hold finishes and for other providers. This is an
intentional conservative cost, not only a pending-hold restriction.

Ordinary rollback is already disabled. Supported recovery selects an equal
or newer reviewed maintenance-aware candidate. Old `--from-candidate` or
private store helpers are excluded from the supported recovery procedure;
old binaries do not universally enforce the new policy. No additional host
algorithm or generalized recovery mechanism is requested.

Source publication enables the generated provider input update. Actual package
activation, maintenance VM regression, cluster restart and payload acceptance
remain later gates. Default-branch integration is not authorized. There is no
production, strict, physical-quiet, repair or APPLY authority.

## Quick evidence and documentation

Fresh Luna/low watcher ran, in the generic Nix environment:

```sh
nix develop -c ruby -r ./test/workspace_host/suspension_test.rb \
  test/workspace_host/profile_transition_test.rb
```

Result: exit 0, 40 runs, 244 assertions, zero failures/errors/skips. The required
fixture loader also runs sibling suspension tests. Private log:
`/tmp/storage-profile-prereq-check.SCWrBf71/generic.log`.
The held three-file hashes remained unchanged before/after. Ruby syntax,
metadata delta assertion and staged/range whitespace checks passed.

No hook framework is declared, `core.hooksPath` is unset, and the canonical
hooks directory contains no executable non-sample hook. Normal
`nix develop -c git commit -F /tmp/storage-profile-runtime-policy-commit.txt`
completed without a bypass. The worktree is clean at the exact head.

Owning explanation is in `docs/workspace-portal.md`, linked by the README.
Session [plan](plan.md), [state](state.md) and [design](design.md) keep execution
facts separate. Please explicitly conclude on the complete history and
no-migrations lineage, and record concrete findings and residual gates.

## Review outcome

Reviewer0, saved GPT-6.1 Sol/xhigh/read-only, reviewed the complete assigned
`4bec2016..8b243993` branch in all four HIGH-risk lanes. No Blocking or Important
findings. One general/risk Advisory concerns the existing transition refusal at
`libexec/workspace-host:2318`: its suggestion to reset retained clusters conflicts
with the preservation procedure. The lead assigned a direct wording correction
and focused assertion before publication; the transition algorithm remains
unchanged. This narrow remediation needs direct verification under review step 9,
not a repeat of unaffected lanes.

The reviewer explicitly concluded one coherent commit, no obsolete or
transitional history, no migrations and no state-schema conversion. Publication
can unblock the generated provider pin. Activation still requires the complete
maintenance-aware provider composition, equal packaged contracts, unknown-state
refusal and the retained-root regression; policy 3 alone supplies none of those
behaviors. No merge, reset or deployment clearance follows from this review.

## Direct remediation and publication

The final amended head is `2b67af62b40149e7554bab0c31b139cd52c963c1`. Compared
with reviewed `8b243993`, only `libexec/workspace-host`'s refusal string and two
assertions in the existing refusal test changed. The message now directs the
operator to preserve retained state and select a reviewed compatible package.
The lead inspected that exact delta; the focused Nix test passed 1 run/26
assertions, with no failures/errors/skips. No algorithm changed or new guard
was introduced. This is direct step-9 verification of the requested Advisory,
without a repeat review.

The branch remains one coherent commit and now has four affected paths. No
migrations or state-schema conversion. Normal Nix amend passed, the worktree
is clean, and fetched default remains `4bec2016`. SSH feature publication and
remote head verification confirm final `2b67af62`; default integration remains
unauthorized. The provider may now generate its runtime input update, but actual
package activation still needs the paired implementation and remaining gates.
