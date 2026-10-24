# Proposal: preserve ancestry during automated flake updates

Status: investigation and implementation proposal, 2026-10-24. No application
implementation, fetch, worktree creation, commit, workflow dispatch or deployment
was performed. Architect: `architect0`. The lead owns plan/state and approval.

## Recommendation and scope

Add an explicit `--forward-only` mode to confctl's existing root, channel and
machine input-update commands. Generate a candidate lock separately, validate
the entire reachable lock graph, and install it only when every replacement of
an existing revision preserves that revision's ancestry in the same source.
Enable this mode in all seven identified publishing GitHub workflows. Keep
repository-specific commit messages and existing tests around the shared update
operation.

The guarantee is **ancestry preservation**: an old commit must equal or be an
ancestor of its replacement. It prevents moving back to an older channel tip or
onto a branch that does not contain a manually pinned commit. It does not prove
that a later upstream commit has not reverted the fix, or that the updated
software is compatible. Existing tests remain necessary.

Use all-or-nothing validation per update invocation. Do not splice selected
nodes from rejected candidates into the old lock. Partial updating and automatic
patch-equivalence exceptions are outside the initial implementation.

## Evidence scope and freshness

The inventory covers the coordination repository and all 32 existing
`repos/*.git` canonical clones, using the locally stored default-ref pointer
where available. No remote was fetched or queried for current branch heads.
These are exact inspected snapshots, **not fresh remote-default evidence**.
Local feature branches, other worktrees, externally configured bots, and
non-default branch workflow variants were not audited. The two reference-only
fallbacks without an origin default pointer are marked below. Locally named
aliases are retained in the inventory rather than assumed to be independent
upstream projects.

Method: `git ls-tree` enumerated `.github` workflow/action files; `git grep`
located flake-lock/update references. The seven updater workflow files and
their invoked flake-update scripts were read in full. Root `flake.nix` input
declarations and `flake.lock` root graphs were inspected for those seven
projects. Confctl's README, AGENTS, input guide and relevant implementation/specs
were read. Repository AGENTS/README were read where present for the seven
consumers; neither exists at the inspected vpsadminos.org configuration root,
and the IRC bot has no root AGENTS. Unrelated CI implementation was not audited.

### Seven publishing update workflows

All seven currently commit and push directly; none of these uses an update PR.
None of the inspected paths checks old-commit containment before accepting the
new lock. `refs/remotes/origin/HEAD` resolves to `master` for these repositories
except vpsAdminOS, where it resolves to `staging`.

| Repository, local origin ref and exact commit | Workflow and helper | Current update and publication behavior |
| --- | --- | --- |
| `haveapi`, `origin/master`, `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `.github/workflows/update-nixpkgs.yml`; `utils/update-nixpkgs.sh` | Weekly/manual; `nix flake update nixpkgs`, `nix flake check`, commits a short-revision subject, pushes `HEAD:${github.ref_name}`. Requires clean lock, compares abbreviated revisions; no ancestry check or rollback of rejected updates. |
| `terraform-provider-vpsadmin`, `origin/master`, `2a2c1055302f86f8e250f1d7e4c331d62012efe8` | `.github/workflows/update-vpsadmin-flake.yml`; `tools/update-vpsadmin-flake-input.sh` | Weekly/manual; defaults to `nix flake update vpsadmin`, verifies clean tracked state and lock-only changes, commits, pushes `HEAD:${GITHUB_REF_NAME}`. A nested dependency downgrade can accompany the root update. |
| `vpsadminos`, `origin/staging`, `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` | `.github/workflows/flake-update.yml`; `.github/workflows/scripts/flake-update-commit-message.rb` formats the message | Daily/manual; copies old lock to `/tmp`, runs unrestricted `nix flake update`, commits `flake.lock`, ordinary `git push`. Root inputs include nixpkgs stable/unstable, impermanence, netlinkrb and ruby-lxc. Backup is used for the commit message, not ancestry enforcement. |
| `vpsf-status`, `origin/master`, `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` | `.github/workflows/update-dependencies.yml` | Daily/manual; checks out the default branch, runs `nix flake update nixpkgs`, commits; then updates Go dependencies/vendor hash, tests and builds, and pushes the default branch. Reads `.nodes.nixpkgs.locked.rev` directly. |
| `vpsfree-irc-bot`, `origin/master`, `94ac4eb5a7caf0456fff7df86a44cae198463276` | `.github/workflows/nixpkgs-update.yml`; `tools/update_nixpkgs_flake.sh` | Weekly/manual; `nix flake update nixpkgs`, clean-tree and lock-only checks, then commits and pushes `HEAD:master`. Metadata reads also assume `.nodes.nixpkgs`; same-revision lock changes error. |
| `vpsfree-cz-configuration`, `origin/master`, `50d263d4127c05163d660fae1c4b9b887584032d` | `.github/workflows/daily-update.yml` | Daily/manual; confctl channel updates for stable/production/staging nixpkgs, unstable nixpkgs, staging/os-staging vpsAdminOS, and llm-agents when the Codex version string differs. Then Ruby dependencies; pushes `master`. The version-string inequality is not ancestry evidence. |
| `vpsadminos-org-configuration`, `origin/master`, `6b04b48e9c076e5525ccb7c38ce174232414f0b5` | `.github/workflows/daily-update.yml` | Daily; `confctl inputs channel update --commit --no-changelog nixos-stable` and `... --commit os-staging`, followed by ordinary push to `master`. |

### Important adjacent paths

- `vpsadmin` at `origin/master` `7963f5dbc2c30a669fcaf3b3a772265d3c803588`:
  `.github/workflows/daily-update.yml` accepts a manual `vpsadminos_input`
  override and runs `nix flake lock --allow-dirty-locks --override-input ...`
  for its dependency build environment. Its explicit staging paths include
  gems/composer outputs, **not `flake.lock`**. This is not an eighth publishing
  flake updater. Preserve the deliberate override; reassess if the workflow
  starts committing its lock later.
- vpsAdminOS and IRC bot `daily-update.yml` workflows update packaged gems,
  not committed flake inputs.
- The coordination workspace has no `.github` at local `origin/master`
  `9f6968ebae4f1fbb26ff548ddcbd6cf8332a5b8b` or local `HEAD`
  `b8d27d53ecd9b77e58c8274f887fd361db5b6e7e` inspected at the start.
- `vpsf-status` and `vpsfree-irc-bot` declare root `nixpkgs` as
  `follows = "vpsadminos/nixpkgs"`, with `vpsadminos` itself following
  `vpsadmin/vpsadminos`. Their scripts still update `nixpkgs` and read a hard-coded
  node key. Actual Nix behavior for that alias-targeted update was not executed.
  Resolve and test the terminal input path during rollout; do not silently
  change the policy to updating all of vpsadmin. The provider shares this graph
  but deliberately updates the real root `vpsadmin`.

### Remaining canonical snapshots: no publishing flake updater identified

Ref names below abbreviate `refs/remotes/origin/`, except marked local fallbacks.
This is static inventory coverage, not confirmation of enabled Actions schedules
or all possible external automation.

| Canonical clone | Ref | Exact inspected commit |
| --- | --- | --- |
| clankerdev | local `refs/heads/main` fallback | `fd290b5ec1b22900e704e8cb990c5ba050af2394` |
| codex-web | master | `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5` |
| confctl | master | `cc40679d267165aecfa569128438bb55fe910268` |
| dev-workspace | master | `bf6d4b0c49600c15e17fe71248807ef43424e932` |
| dokuwiki-plugin-vpsadmindoc | master | `f198173ed15dfa1fe124311fe45ae3c54914e7d3` |
| haveapi-client-php | master | `7fa4e35a9d9cb462320a4b2f2786bf84b8e024f2` |
| linux | local `HEAD` → `refs/heads/vpsadminos-6.12.95-backports` fallback | `fc37ccc43227ab8eef70b50660a081f2615d0ead` |
| ruby-lxc | vpsfree | `df19e1f287da338324db4dee6a2bac8340fc1154` |
| security-advisories | 2026-07-13-security-advisory-automation | `e6ceb642878dd97546174217676d9861afc38d4e` |
| ssh-exporter | master | `c1b481a68e00d90802aeb36730c68a19f3c17711` |
| syslog-exporter | master | `7c5a8e74e44a704cceb99cd05716af6800d78efd` |
| vpsadmin-go-client | master | `1d9240f3d27b5831baf3694baab5fe06294875d8` |
| vpsadmin-kb-captures | master | `ce2c8cd9358c3636e5d39343e595df813a0b197f` |
| vpsadmin-rust-client | main | `945af6a97717a7a6373507bbc9592d5cd53727c2` |
| vpsadmin-webui | main | `4140f90d2ebcd579e0db2a4cef0dfbfc1fc54cd5` |
| vpsfree-client | master | `56357098b914e19d3a0f2ed34896e5dbbd802e21` |
| vpsfree-dev-workspace | master | `767dfd587e346168e1443e65ccdb67ce748f3fe3` |
| vpsfree-kb-contracts | master | `ce2c8cd9358c3636e5d39343e595df813a0b197f` |
| vpsfree-mail-templates | master | `2cfd218d9152888feea4109f064459078ea9f76e` |
| vpsfree-maintenance-tasks | master | `2fdc9f2889ac419136cd0cde0e0955c015ae7107` |
| vpsfree-notification-templates | master | `2cfd218d9152888feea4109f064459078ea9f76e` |
| vpsfree-sms-gateway | 2026-06-15-vpsadmin-events | `af7b3fafb780c849ae03e31712128ecb0749ec0b` |
| web | master | `307635a96bc3532af51ff5d08206d920704eee00` |
| zfs | vpsadminos-release-next | `481845fca6ae3f61ca2262c1a5693a58ae364650` |

## Why confctl fits, and what cannot be reused unchanged

Code references in this section refer to confctl commit
`cc40679d267165aecfa569128438bb55fe910268`.

- `lib/confctl/inputs/updater.rb`: one update implementation feeds the root,
  channel and machine commands. It currently runs Nix against the real lock
  before comparing revisions or committing. It has no transactional guard.
- `lib/confctl/cli/inputs/root.rb` and `lib/confctl/conf_dir.rb`: root updates
  require a `flake.nix`, not confctl cluster outputs. The existing
  `spec/confctl/inputs_spec.rb` fixture uses `outputs = { self, ... }: {};`.
  Ordinary project flakes can therefore use the root command without adopting
  confctl's deployment configuration model. Channels still need their existing
  `.#confctl.channels` evaluation.
- `lib/confctl/flake_lock.rb`: assumes node ID `root`, and an array-valued
  follows reference is handled as `node_id[0]`. This is not a complete resolver
  for nested follows paths. `lib/confctl/flake_lock_diff.rb` considers only
  requested root revisions and treats equal revisions as unchanged regardless
  of source metadata or descendants. Neither is a sufficient safety validator.
- `lib/confctl/inputs/nix_output_guard.rb` rejects GitHub metadata-cache fallback
  warnings. Preserve this check: valid containment alone does not prove a fresh
  upstream query. The current updater does not restore the file when it raises.
- `lib/confctl/inputs/setter.rb` already uses `--output-lock-file` and a rename,
  but its multi-input loop installs each result separately. Reuse the technique,
  not an assumption that the setter is an all-input transaction.
- `lib/confctl/inputs/commit_message.rb` uses `GitRepoMirror` for optional
  changelogs. `--downgrade` only reverses changelog direction; it neither permits
  nor blocks revision changes. Do not silently reinterpret this existing flag
  as an override of the new guard.
- `lib/confctl/git_repo_mirror.rb` clones full mirrors and later fetches them.
  It provides no ancestry predicate, interprocess cache lock or typed missing
  history result. Changelog errors are intentionally softened into text;
  **guard errors must never follow that best-effort behavior**.

The configuration workflows execute older pinned tools:
`vpsfree-cz-configuration` locks confctl to
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`;
`vpsadminos-org-configuration` locks it to
`af164b442100b92b8d93c0d67b315eff982e0180`.
Their `inputs/updater.rb` files were also inspected and have the same in-place,
unguarded update structure. A confctl merge alone changes neither workflow.

## Proposed interface and transaction

All examples below are **proposed**, not commands currently available. Option
placement follows the existing CLI (options before positional arguments):

```sh
# Ordinary project; leave its existing commit/test wrapper in charge.
confctl inputs update --forward-only nixpkgs
confctl inputs update --forward-only vpsadmin
confctl inputs update --forward-only --all

# Existing configuration workflow, preserving its commit/changelog policy.
confctl inputs channel update --forward-only --commit --no-changelog \
  '{nixos-stable,production,staging}' nixpkgs
confctl inputs channel update --forward-only --commit \
  '{staging,os-staging}' vpsadminos
```

Expose the same policy in machine update for consistency, although no inventoried
workflow uses it. Preserve unflagged manual update and explicit `inputs set`
behavior. Intentional rollback, branch migration or cherry-picked successor
selection remains an explicit operator decision. `--downgrade` alone never
disables `--forward-only`.

Implementation sequence:

1. Require an existing valid lock in guarded mode, a supported lock schema and
   a clean tracked lock; when committing, reject unrelated staged changes.
   Acquire an update-process lock for cooperating confctl invocations. Snapshot
   exact lock bytes, relevant flake declarations and target Git HEAD. Assume
   a workflow-owned checkout with one writer; do not claim arbitrary external
   writers obey the process lock.
2. Resolve requested aliases to the terminal update paths; deduplicate shared
   targets. Preserve the semantic requested selection in diagnostics. Do not
   silently expand an alias update into refreshing its parent input.
3. Run Nix from the original flake directory, with the old snapshot as reference
   lock and a temporary output lock on the same filesystem. This preserves
   relative-path semantics. Use `--reference-lock-file`/`--output-lock-file`
   where supported, and verify the supported Nix version matrix before rollout.
   Do not fall back to updating the real lock in place. These flags are documented
   in the [Nix update reference](https://nix.dev/manual/nix/2.35/command-ref/new-cli/nix3-flake-update).
4. Check Nix's exit status and existing cached-metadata warning guard, parse the
   candidate, and validate the full semantic graph as below. Generate the result
   summary from the full diff, not just changed top-level SHA fields.
5. If validation passes and the original inputs/HEAD/lock are unchanged,
   atomically rename the candidate to `flake.lock`. Validate before optional
   changelog generation and Git commit. On policy rejection or evidence error,
   discard only the owned candidate; the original lock, index and HEAD remain
   unchanged. No broad reset or restore of someone else's files.
6. A commit-hook failure after installation leaves an already-validated lock
   uncommitted and returns failure; do not attempt to undo hook side effects.
   Workflows must stop before pushing. After hooks/tests, validate the final
   lock content against the saved workflow baseline again before publication,
   or prove it exactly matches the approved candidate. A read-only proposed
   `confctl inputs check-update --old-lock FILE --new-lock FILE` entry point can
   expose the same validator for this final check; it does not update or commit.

Use typed results in the library: `unchanged`, `updated`, `rejected`, `error`.
Only unchanged/updated return success initially. Known non-containing revision
changes should produce a clear policy-rejection exit (proposed code 3); missing
evidence, unsupported changes or tool failures return an error (proposed code 1).
This deliberately stops existing workflows before their final push. A future
explicit wrapper may map a known rejection to a visible, whole-update skip;
it must not map errors to successful skips. Do not add implicit per-input skips.

Multiple confctl invocations in a configuration workflow remain separate
transactions. Earlier locally committed updates can exist when a later one
rejects, but the job must stop before the common push. Initial scope promises
atomic lock acceptance per invocation, not rollback of the whole job's earlier
gem or input commits.

## Graph and ancestry invariants

The validator works from `data['root']`, resolves node links and complete
root-relative follows paths, detects dangling edges/cycles and compares stable
logical dependency paths rather than generated node IDs such as `nixpkgs_2`.
Represent aliases for diagnostics and deduplicate identical source/old/new
ancestry queries. A node-ID-only renaming must not alter the result.

For every previously reachable dependency path:

- An unchanged resolved source and revision is allowed. An equal revision with
  changed content/extraction attributes (for example `narHash`, `dir`, submodules
  or fetch mode) is not silently treated as unchanged. Require explicit support
  for a proven harmless metadata difference or reject it.
- For a changed Git revision, require the same normalized source identity and
  prove `old == new` or `old` is an ancestor of `new`. Identity includes fetcher
  kind, host, repository and relevant extraction attributes; keep credentials
  out of diagnostics and cache keys. Treat host/repository/type/dir changes as
  migrations requiring manual review, even if a similarly named ref exists.
  Do not infer identity from a branch name, timestamp or version string.
- Check all changed descendants, including changes introduced by a root
  vpsadmin/vpsAdminOS update and dependencies reached through follows. A forward
  root revision with a regressed nested nixpkgs revision rejects the candidate.
- Removed old logical paths or ambiguous graph restructurings reject in the
  strict initial policy. New paths have no predecessor to compare: allow only
  structurally valid, explicitly supported immutable Git sources, report them,
  and check all surviving old paths. This conservative policy may require a
  manual reviewed update when upstream reorganizes dependencies.
- Unchanged unsupported sources may remain. A changed path/tarball/indirect
  source, missing revision, unsupported host/fetcher or unknown schema is an
  evidence error; never a bypass. Raw `flake = false` GitHub sources with a
  locked revision are ordinary supported Git sources.

Default branch movement, channel timestamps and `lastModified` are not proof.
An older channel tip fails; so does a divergent stable branch containing a
cherry-picked equivalent patch. Cherry picks have different ancestry. Retain
the manual pin until the branch actually contains it, or make an intentional
manual transition after verifying the change. A later revert commit can pass
ancestry; this is an explicit limit of the guarantee.

## GitHub compare API versus local Git

Recommend the GitHub compare API as the economical initial provider for
`github.com` lock sources: all seven workflows' inspected root sources resolve
to GitHub, including raw sources. Compare **full immutable old/new SHAs**, not
moving branch names. Accept a well-formed `ahead` result only with zero
behind-count and the old SHA as merge base/base; equality can be decided locally.
Reject `behind` and `diverged`; reject missing or inconsistent evidence.
Use summary metadata, not membership in the returned commit list, which may be
paginated/truncated. The endpoint and response fields are documented by
[GitHub](https://docs.github.com/en/rest/commits/commits#compare-two-commits).

Use bounded HTTP timeouts/retries and explicit token environment support in
confctl. Workflows must supply the token to that client; Nix's access-tokens
configuration is not automatically a confctl HTTP credential. Do not log token
values, put them in URLs, or forward credentials to arbitrary redirect hosts.
401/403/404, rate limiting, timeout, server failure or malformed JSON is unknown
evidence and must preserve the lock and fail. Missing commits are not evidence
that the update is safe. Exact-SHA comparison caching is optional, keyed by
source and both SHAs, not branches; no stale-success shortcut for a new pair.

Local Git's `git merge-base --is-ancestor OLD NEW` offers the same graph
predicate without depending on API availability. It requires both commit
objects and adequate history; exit 0 is proof, exit 1 with complete history is
non-containment, other failures are errors. Shallow history cannot justify a
negative conclusion without completing the necessary history. Suppress replace
refs and reject unsupported graft/shallow states when trusting a cache.

Reusing confctl's mirrors for a Git provider is possible, particularly for
non-GitHub Git URLs, but a cold full nixpkgs mirror is much more expensive than
one comparison request. Add cache locking, exact object availability checks and
typed status handling before using those mirrors as authority. Keep a provider
interface so Git can be added without changing policy. Do not silently switch
to a costly clone on an API failure in the initial implementation; explicitly
unsupported changed Git sources fail until the Git provider is implemented.

## Publication race and rollout

Each direct-push job should start from a fresh target-branch snapshot and retain
that exact baseline lock/commit. Check the final candidate against that baseline
and use an ordinary non-force push. If another target commit lands, including a
manual pin, the update branch is no longer a fast-forward and push rejects it.
Retry the update from a fresh target snapshot and regenerate the candidate;
do not pull/rebase/merge stale lock changes and push without revalidation.
Concurrency groups can reduce duplicate jobs but do not replace this rule.
No new PR machinery is required. If PR automation is introduced later, its
merged result must be revalidated against the then-current base, including base
movement; a check tied only to the original PR base is insufficient.

Ordered rollout, subject to separate implementation/integration authorization:

1. Implement and review the shared confctl policy and transaction. Publish an
   exact approved revision/package with a documented supported Nix range.
   Do not invent a release version or automatically publish a gem.
2. Bootstrap both configuration repositories to that confctl revision before
   enabling the new option. Use the approved new tool to validate the pin update
   itself; an old pinned tool cannot supply its own missing guard. Check wider
   confctl compatibility because these pins precede current master; this
   investigation inspected the updater, not the entire old-to-new tool release.
3. For the five ordinary projects, run a reproducibly pinned confctl package
   as a CI tool, e.g. via `nix shell github:vpsfreecz/confctl/<approved-sha>#confctl
   -c ...` (illustrative placeholder). It need not become a project runtime
   dependency or a flake input. In particular, adding confctl as a normal
   vpsAdminOS input would introduce the reverse dependency of confctl's existing
   vpsAdminOS input; avoid that bootstrap cycle.
4. Update every identified invocation in the seven workflows/helpers, retaining
   commit style and validation. Verify terminal update selection for the status
   service/IRC bot follows graph. Include llm-agents: a Codex version difference
   must not bypass ancestry validation, and the existing post-update version
   assertion must still handle an unsuccessful update by stopping publication.
5. Establish fresh inventory and enable coverage per repository only after
   candidate behavior is verified. Record which exact workflow/tool revisions
   are active; until all seven are rolled out, coverage is partial. Future
   automated flake writers must use the same guard.

## Implementation packages and ownership boundaries

These are proposed work packages, not assignments or permission to implement.
The lead selects retained implementers and serializes shared-file/Git changes.

| Package | Files and interface boundary | Dependencies and acceptance |
| --- | --- | --- |
| A: graph policy and evidence provider | New `lib/confctl/inputs/forward_guard.rb`, graph resolver/provider files, focused new specs. Own the pure `validate(old_lock, candidate_lock)` result contract. Avoid editing updater/CLI in this package. | Independent initial work. Detect aliases/transitives, source migration and all ancestry/error outcomes; tests do not need network. |
| B: transaction, CLI and contract docs | `lib/confctl/inputs/updater.rb`; `lib/confctl/cli/app.rb`; `lib/confctl/cli/inputs/{root,channels,machines}.rb`; new read-only check command; transaction/CLI specs; `docs/flake-inputs.md`, README and `man/man8/confctl.8.md`. | Depends on A's agreed result contract. Can prepare transaction fixtures in parallel. No real lock mutation/commit before acceptance; preserves existing manual/set behavior and cached-metadata checks. Coordinate any edits to existing FlakeLock/FlakeLockDiff with A. |
| C: ordinary workflow adoption | The five ordinary-project workflow/helper paths listed above; minimal CI tool pin/setup and repository-specific fixture checks/docs. | Depends on approved/published A+B tool. No copied ancestry algorithms. Test selected inputs, existing commit formats, hooks and non-force publication. Resolve follows selection explicitly. |
| D: configuration adoption/bootstrap | Both configuration `flake.lock` pins, `.github/workflows/daily-update.yml`, existing reusable docs if needed. | Depends on A+B and compatibility assessment of confctl pin advancement. Every channel invocation guarded, including llm-agents. No machine deployment implied. |

The authoritative lasting contract belongs in confctl's input guide/manual,
linked by consumer workflow documentation. Exact rollout evidence remains in
this session. There is no need for a new shared project or seven algorithm
copies. A reusable action could later package tool installation, but is not
required for the first guard.

## Compatibility, failure and recovery

No database, persisted runtime-state, API, daemon protocol or Nix module-option
migration is needed for this feature. Accepted output is an ordinary Nix lock;
older Nix/confctl may read it subject to the existing lock schema/version range.
The new CLI option is additive; older confctl must reject it rather than run
an unguarded fallback. Keep manual setter and intentional rollback semantics.

No coordinated vpsAdminOS node upgrade is required. This changes CI tool
selection and input acceptance, not running hosts. Actual confctl pin upgrades
may have additional historical compatibility constraints that must be assessed
before implementing those configuration changes.

On rejection, keep the manual revision, record the old/candidate full SHAs,
logical paths and rejection reason, and retry after the intended branch catches
up. On unknown evidence, repair credentials/network/provider support and retry;
do not bypass the check. Intentional migration requires a reviewed manual pin
change. If a new guard is faulty, keep automated updating disabled/blocked or
roll back to another guarded version; reverting to an unguarded workflow
reintroduces the original risk. No rollback of live machines is involved.

## Acceptance criteria and verification brief

Quick checks after implementation (in confctl's declared Nix development shell):

- Focused RSpec cases for the graph resolver, policy/provider adapters,
  transaction and CLI; RuboCop on changed Ruby; documentation/man generation
  consistency; Nix formatting only for changed Nix files.
- Synthetic DAG fixtures: equality; normal forward; current pin newer than
  channel; merge containing the pin; divergent/rebased history; equivalent
  cherry pick; later revert that correctly passes ancestry; misleading dates.
- Graph fixtures: non-`root` root ID, arbitrary node renumbering, nested/chained
  follows, shared nodes, raw Git source, same root SHA with changed descendants,
  upstream root forward with nested rollback, source/fetch-attribute changes,
  removed/new paths, unsupported changed inputs, malformed/cyclic graph.
- Mock API fixtures: ahead/behind/diverged, incomplete or contradictory summary,
  large/paginated comparisons, 401/403/404/rate limit/timeout/5xx, no leaked token.
  Verify errors never become equality or successful skip.
- Transaction fixtures: Nix exits nonzero, emits cached-fallback warning or
  writes malformed output; rejection of one input among several; interruption
  before rename; changed original lock/flake/HEAD during preparation; no-change;
  hook failure. Assert original lock bytes/index/HEAD are preserved for every
  pre-install failure, and no commit call occurs before acceptance.

Longer checks after committed deliverables, quick checks and mandatory review:

- Existing full confctl RSpec suite and package/CLI checks. Use disposable local
  flakes, with mocked provider responses or a controlled Git provider, to prove
  Nix's reference/output-lock behavior and multi-input transaction semantics on
  supported Nix versions. No node VM is needed merely to test graph acceptance.
- Execute guarded candidates for all seven workflow patterns in disposable
  checkouts without pushing; verify commit formatting, hook behavior, full lock
  graph and final baseline comparison. Preserve each repository's required
  tests; consumer owners read local routed procedures before selecting them.
- Simulate target-branch movement in disposable Git repositories. The stale
  ordinary push must reject; a new run from the manual pin must retain it unless
  the next candidate contains it. Exercise the exact resolved nested nixpkgs
  selection for status/IRC and llm-agents rejection handling.
- Bounded GitHub API smoke comparisons using public known SHAs; compare results
  to complete local fixture Git histories where appropriate. These live checks
  supplement, rather than replace, deterministic failure tests.
- Long/uncertain checks use the dev-session-monitor utility under workspace
  policy. No checks or live mutation described here were executed this turn.

Acceptance for rollout completion: all seven active workflow paths invoke the
approved guard, rejected/error candidates never reach publication, transitive
and follows protection is demonstrated, bootstrap pins select the approved
tool, and concurrent target movement triggers retry from a fresh baseline.
Repository integration still needs separate explicit approval.

## Open verification items

- Fresh remote refs, enabled workflows/schedules, non-default workflow variants
  and external dependency bots remain unverified by design.
- Exact oldest supported Nix version for reference/output-lock flags and nested
  follows update selectors must be established in implementation tests.
- Full old-pinned-confctl to new-tool compatibility must be assessed before the
  configuration pin bootstrap; no blanket compatibility claim is made here.
- GitHub provider schema and token handling need implementation fixtures. A Git
  fallback is an optional follow-on, not an unverified escape on API failure.
- Strict removal/restructuring rejection may stop ordinary upstream graph
  migrations. This is deliberate initial behavior; any relaxation needs an
  explicit design revision through the lead.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>
