# Remove software pins from confctl

## Goal

Implement the accepted repository-wide plan for making confctl support only
flake-based cluster configurations. Remove software-pin management, evaluation,
build and status paths; delete the software-pin example and rename
`example-flake/` to `example/`.

The initial request authorized investigation and planning. The user's subsequent
"proceed" authorizes implementation of this plan, local verification, independent
review and publication of the feature branch. Deployment, release and default
branch integration remain later, separately directed phases. The architect's
[design and verification brief](design.md) governs implementation.

## Affected repositories

- `confctl`, inspected in this initiative's dedicated worktree. No downstream
  configuration changes are included in the present scope.
- The coordination workspace holds the plan, design, state and portal manifest.

## Approach

Full-team mode: retained `architect0` (Astra/xhigh, workspace-write) owns the
repository walkthrough and technical design; the lead owns reconciliation and
tracking. Retained `implementer0` owns the authorized application changes.
Reviewer0 receives independent final review after commits and quick checks.

Inventory Ruby CLI/library paths, Nix evaluation and exports, persisted build
generations, shared deployment helpers, examples, documentation generation,
packaging, test fixtures and CI. Separate software-pin functionality from common
deployment and flake-input functionality before choosing deletion boundaries.

The walkthrough is complete at confctl `1b56616` (v3.0.0). The accepted ordered
implementation sequence is:

1. Consolidate flake evaluation/building and inherited deployment helpers into
   `ConfCtl::Nix`. Remove backend dispatch, pin/migration CLI namespaces,
   legacy initialization, pin auto-updates and obsolete cache handling. Require
   `flake.nix` for configuration operations, preserving init/help/stateless tools.
2. Simplify generations, status, changelog and diff to flake inputs. Preserve
   the existing flake JSON and roots; reject unsupported records explicitly.
3. Delete Nix pin modules, evaluators, options and old system builders. Retain
   shared metadata/network helpers. Replace legacy option extraction with a
   shared flake-native documentation evaluator for Rake and `confctl ls -L`.
4. Delete the old `example/`, move the complete flake example into `example/`,
   update every consumer, simplify deployment fixtures to flake mode, remove
   pin success tests, and prune `nix-prefetch-git` from packages, shells and CI.
5. Update README, manuals/templates, input/carrier guides, version-scoped
   migration guidance, changelog and repository instructions. Correct touched
   snippets and regenerate documentation.
6. Complete focused checks and commit the implementation; inventory the whole
   branch and run independent final review before monitored integration tests.

The [design brief](design.md) supplies exact files/functions, acceptance criteria
and commands. Coupled changes may share commits to avoid broken intermediate
states. The initial planning checkpoint preceded application implementation.

## Decisions

- Legacy cluster configurations and the software-pin CLI are intentionally
  unsupported after the change. Operators must migrate using an earlier confctl
  before upgrading; do not add a replacement legacy implementation.
- Flake input channels, role overrides, non-flake source inputs (`flake = false`),
  deployment, carriers, health checks and rollback remain supported.
- Retain `impureEval`, flake-derived `legacyNixPath`/`legacyNixPathMap`, developer
  shells and package helpers: they do not implement software-pin clusters.
- Remove the migration implementation, while retaining upgrade guidance that
  explicitly uses v3.0.0 before selecting the new tool.
- The lead accepts the design's unsupported-generation policy: diagnostics with
  paths/reasons; no fallback when current names a rejected record; explicit or
  ambiguous numeric selections fail before deployment; unresolved current
  blocks implicit local retention; normal new flake builds can still proceed.

## Compatibility and deployment

- Saved flake generations should retain their existing JSON format and GC-root
  names so an older flake-capable confctl can read newly created records.
- Old software-pin records, directories and GC roots remain untouched and
  unsupported. Keep a runnable v3 tool for their management and rollback;
  JSON backups alone do not protect closures. Generic remote profile operations
  remain supported independently of old local pin metadata.
- Update the configuration's confctl input with the operator tool to gain the
  new cluster `moduleOptions` output. Existing primary flake outputs stay stable.
- Pin-related CLI/options/exports and internal Ruby APIs disappear. Netboot's
  optional `swpins_info` JSON field disappears; external consumers are unknown
  and must be inventoried before a later site rollout.
- Removing software-pin support does not itself require simultaneous updates of
  running machines. Do not infer that production configurations have migrated.
- No database, service API, generated client or Terraform schema is involved.
  Changes to Nix module options, user hooks and Ruby extension APIs are part of
  the implementation inventory and must be called out in upgrade guidance.
- Publish only the feature branch by default. Integration into confctl `master`
  requires explicit user direction. No release or deployment is included here.

## Documentation

Readers are confctl maintainers and operators upgrading existing configurations.
Implementation will update README, CLI and Nix option manuals, example README,
repository instructions and affected skills. Keep supported upgrade guidance
in confctl's own docs, distinguishing commands available only in an earlier
version. Session-specific rollout and verification evidence stay here.

## Testing plan

The architect's brief specifies focused regression checks and actual Nix,
RSpec, lint, documentation and integration commands from the repository.
Implementation must preserve shared activation/copy/rollback behavior and test
legacy rejection and existing flake-generation round trips. Final independent
review follows committed implementation and quick checks, before long integration
verification. Fresh Luna/low utility watchers own uncertain-duration tests/builds.

Planned commands include RSpec/RuboCop and both documentation Rake tasks in
`nix develop`, package/RSpec Nix checks, and retained integration selectors
`deploy/flakes`, `auto_rollback`, `carrier/deploy` and `carrier/netboot`.
Require meaningful generated options, legacy-command/config rejection,
generation/GC-root round trips and rejection behavior, shared deployment/rollback
coverage, input channel/override semantics and no residual supported pin paths.
All checks are prospective; no builds or application tests ran during planning.
