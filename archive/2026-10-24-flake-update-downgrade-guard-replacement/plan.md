# 2026-10-24-flake-update-downgrade-guard-replacement

## Goal

i'd like you to update all automated updated of flake inputs using github workflows to make sure that the update cannot actually cause a downgrade. for example, I sometimes set nixpkgs input to a revision that is not yet propagated into a channel, in order to deploy a fix. the automated workflows mustn't replace this revision with an older revision that doesn't yet contain the fix. not sure how to implement this, but I guess we should somehow check that the new revision is not behind the current revision. maybe this would be useful to have in confctl itself. suggest a solution.

## Affected repositories

Investigation scope: all canonical workspace projects with automated GitHub
flake-input updates, the coordination workspace, and confctl as a possible
shared implementation owner. Architect will inventory exact affected projects.

Identified implementation scope: confctl, haveapi,
terraform-provider-vpsadmin, vpsadminos, vpsf-status, vpsfree-irc-bot,
vpsfree-cz-configuration and vpsadminos-org-configuration. Exact inspected refs,
workflow paths and scope limitations are in [design.md](design.md).

## Approach

Replace GitHub compare evidence with ancestry checks in cached Git repositories.
Reuse confctl's `~/.cache/confctl/git-mirrors/` where possible; handle a cache
miss by fetching enough history to prove the result. Preserve full semantic
lock-graph validation, transactional lock installation, fail-closed errors,
committed-lock publication checks and manual update behavior.

Architect0 completed the design and verification brief. Implementer1 owns confctl;
implementer0 owns cache adoption and exact new tool pins in the seven workflows.
Independent final review follows committed quick-checked changes. Root serializes
long checks through fresh utilities and keeps their evidence bound to exact
new source and package identities. Prior R verification remains historical.
No unrelated Terraform VM rerun is implied by a provider-only backend change;
the architect must bound checks around changed cache/Git/package behavior.

## Decisions

- User requested cached Git replacement: "yup, rework it" after discussing the
  existing confctl mirror cache. Remove GitHub compare API evidence; use Git
  ancestry without a silent API fallback. Cache misses and failures must preserve
  fail-closed guard behavior. Keep `inputs ls --json`, which exposes full resolved
  revisions for status/IRC scripts; the user asked for its purpose, not removal.
- Existing source/review/verification records and Nix roots are preserved. At that checkpoint no
  integration, deployment, cleanup or lifecycle action was authorized. Later
  explicit merge approval and equivalent fresh-base integration are recorded below.

- Rollout refinement accepted by lead: all seven workflows use the same external
  exact-pinned guarded confctl CI tool. Leave both configurations' deployment
  tool pins unchanged, avoiding unrelated legacy/swpins removal and generation
  compatibility changes. New root/channel CLI consumes their existing flake and
  channel outputs. This supersedes the proposed configuration-pin bootstrap.

- User authorized implementation: "great, implement it". This covers the guard,
  all seven consumer workflows and required confctl pin bootstrap, feature
  publication, checks and mandatory review. It does not authorize default-branch
  integration or machine deployment.

- Treat the user's final request, "suggest a solution", as a request for a
  concrete design and rollout recommendation first.
- Distinguish a known non-forward candidate from an inability to prove ancestry.
- Assess the full changed lock graph and stale automation branches, rather than
  checking only the intended top-level input.

## Compatibility and deployment

Design must preserve intentional manual pins, fail safely on divergent/unknown
history, and explain intentional branch switches and rollbacks. Investigate
tool-version bootstrap and ordering before recommending workflow adoption.

## Documentation

Readers: repository maintainers and operators managing manual advance pins.
Proposal and repository evidence belong in this session's `design.md`. Lasting
CLI behavior and repeatable operations would belong in confctl documentation
with implementation, and workflow usage belongs with each consumer.

## Testing plan

Quick checks: existing graph/transaction/CLI tests plus real local Git DAG,
cache reuse/missing commits/type/history/error/locking/changelog regressions;
workflow cache scheduling and retained alias/commit/publication mocks; owning
lint, man generation and ordinary hooks. Commit complete intended changes and
consolidate obsolete unmerged provider/pin streams before independent final
review of the complete eight ranges and affected behavior.

After that review, root runs the new exact packaged exported check and records
source/input/derivation identities. Exercise the actual package in IRC and both
old configuration shells with real hooks. Run all seven scoped guarded
update/commit/final-HEAD-lock paths with real cold/warm shared-cache receipts and
a real local target-movement race. Record explicitly any skipped unchanged
non-updater dependency-refresh/build stages. Retain historical R complete
workflows and Terraform’s eight-example results as evidence for those old exact components;
no automatic unrelated VM rerun. Final publication is provider-first and each
consumer keeps one final exact CI pin. This verification plan preceded the
explicit default-integration approval recorded below.

## Verified outcome

The exact Git-cache provider 822c0e35 and all seven consumer adoptions are
committed, independently reviewed and published. Packaged check with 203 examples, all seven scoped
updater/caller/final-lock paths, real cold/warm cache and local push-race checks
passed. Every observed exact-head CI run succeeded.
[Current acceptance](verification/git-cache-acceptance.json) records exact source
identities, the same-source org fixture correction, all verification limits and
integration proof. The user later explicitly approved all eight default merges;
they are now integrated with fresh remote proof and released claims. See
[merge summary](verification/integration/summary.json).

## Integration execution

User direction: "ok, merge it to the default branches". All eight default
merges are now verified. vpsAdminOS targets staging; the other seven target
master. HaveAPI and vpsFree configuration received independently reviewed
patch-equivalent fresh-base successors, preserving upstream changes. Every
merge claim is released. No deployment, cleanup or lifecycle action occurred.
The accepted final post-integration observation proves actual ancestry and exact
default equality for all eight heads. All eight observed default-branch CI runs
passed; vpsAdminOS and both configurations had no matching runs. See
[final evidence](post-integration-final-observation.md). No CI wait, rerun, dispatch,
deployment, cleanup or lifecycle action occurred. No merge work remains.
