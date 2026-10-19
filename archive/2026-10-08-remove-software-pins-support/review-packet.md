# Final review packet: remove software pins from confctl

## Outcome and boundary

The user requested complete removal of software-pin support, flake-only cluster
configuration, deletion of the old example and `example-flake` renamed to
`example`. The initial plan was accepted by the subsequent "proceed". Review the
complete committed deliverable against [design.md](design.md), [plan.md](plan.md)
and [state.md](state.md). This is final review, not a planning review.

Only confctl application content changes. No downstream configuration pin,
live rollout, release or default-branch integration is authorized. Session
records are coordination evidence and not product behavior. Leave session open.

## Source and history

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-08-remove-software-pins-support/confctl`.

Branch: `2026-10-08-remove-software-pins-support`; target `origin/master`.
Base: `1b56616eff41e760327f3a0dbed8875e4aa9dbec` (Version 3.0.0).
Final remediated head: `3be154b5f86125146e444d5fb6aa60916e99b77d`. Independent review was completed at `18d8b4862a2523d629a534ea38d2ba92ef0209c8`;
narrow corrections and unchanged-unit range-diff are reconciled in review-report.md. Complete series, commit-split rationale, final diff and
migration/use provenance are in [branch-inventory.md](branch-inventory.md).
The source tree/index is clean, parent fetch confirms upstream at the base, and
all intended changes are committed. Review all five commits and the whole diff.

## Acceptance criteria

- One public `ConfCtl::Nix` preserves flake evaluation/building, stateless use,
  copying/activation/profiles/auto-rollback/shell/GC helpers. Delete software-pin
  namespaces, migration implementation, backend dispatch/cache, legacy builders
  and obsolete pin dependencies. Bound operations require `flake.nix`; init,
  help and stateless tools remain usable outside a cluster.
- Preserve flake input role/channel precedence and overrides, raw `flake=false`
  sources, path/follows inputs, GitRepoMirror, impure evaluation and flake-derived
  legacyNixPath. The NIX_PATH bridge is not a non-flake cluster backend.
- Local generations accept only explicit `mode: "flakes"`; preserve JSON/input
  links and GC-root naming so v3 can read new generations. Reject old/missing/
  unknown modes and invalid records with path/reason, leaving files/roots intact.
  Rejected/broken current must not silently fall back. Rejected explicit or
  ambiguous numeric selection must fail before any host deployment. Unresolved
  current blocks implicit local old/rotation. Normal new builds may replace
  current. Generic remote profile operations remain available.
- Delete legacy Nix modules/evaluators/options/exports/builders while preserving
  metadata/network helpers. New shared option evaluator serves root
  `moduleOptions` documentation and cluster `confctl.moduleOptions` for `ls -L`.
  Include confctl/cluster/carrier/program options and custom cluster options.
  No repository module declares services.*; remove the empty SERVICES category.
- Rename the full flake example, including hidden/locked/nested content and the
  optional source-developer shell. Keep root developer shell and existing
  mkConfigDevShell modes. Adapt remaining deployment/carrier fixtures and CI.
- Current docs describe only flakes; upgrade guidance explicitly uses retained
  v3 migration commands before updating tool/config input. Explain old state,
  GC-root retention, current/numeric safeguards and rollback prerequisites.

## Compatibility and provenance

No database or state conversion migrations are introduced. Existing merged v3
flake-generation JSON is retained; software-pin records are deliberately
unsupported and untouched. No earlier branch iteration has been published,
released, deployed or externally consumed. Verify this against the complete
commit inventory. Require explicit history and migration conclusions, including
"no migrations" when applicable.

Pin CLI/Nix exports/internal Ruby APIs are intentionally removed. Flake tool and
configuration confctl input must both support the new moduleOptions output.
Nodes can remain on old system profiles; absent input metadata remains unknown.
Netboot's optional swpins_info export is removed and inputs_info is exported when
available; boot/profile paths remain supported. External index readers and
production configuration migration status are unknown, deferred to a later
operational inventory before rollout. No all-node update is required by this
operator-tool change. Verify supported preservation and intentional breaks.

## Interfaces and discovered consumers

confctl owns the CLI, Ruby extension surface, mkConfctlOutputs/config-devshell
flake interfaces, Nix modules, generation JSON and optional netboot index
metadata. In-repository consumers include init templates, renamed example,
Rake/manual generation, Ruby specs, deploy/auto-rollback/carrier suites and
package/dev shells. README links external configuration repositories; they are
not edited here. Inspect representative retained in-repository consumers and
relevant public exports; report any current-scope broken consumer. Site adoption
is a separate step requiring v3 migration/custom-hook/index-reader inventory.

## Documentation and quick evidence

Lead personally applied vpsfree-user-facing-writing to settled English drafts.
Product documentation: README.md, docs/flake-inputs.md, docs/swpins-to-flakes.md
(version-scoped migration/recovery), docs/carrier.md, example/README.md,
man/man8/confctl.8.md, template/confctl-options.nix/main.erb and generated option
manual; CHANGELOG.md and AGENTS.md reflect the supported workflow. Inspect
technical fidelity, placement and discoverability, not just stylistic changes.

- Parent repository shell full RSpec: 58 examples, 0 failures, 23.24 seconds;
  `rspec-final.log`. Earlier failures were factory double/mock lifetime issues
  corrected before this pass.
- Parent real root option evaluation: 114 public options; all required confctl,
  cluster, carrier and program representatives present and no pin options.
  `initial2-options.json` plus final Rake-render logs provide evidence.
- Parent final `rake confctl-options` and `rake md2man:man` passed. Final markup
  rerun has no raw_html warnings and whitespace check is clean.
- Implementer: 87 Ruby/runner/netboot syntax checks and extracted deploy fixture
  syntax passed; 27-file changed Nix format check; RuboCop94 files/no offenses;
  focused 25 and 17 examples passed. Hooks run on the final commits.
- Source audits found removed backend/pin/prefetch/example-flake APIs absent;
  remaining pin mentions are migration/changelog/rejection/negative-test context.

Long checks deliberately follow review: package/check builds, disposable custom
`ls -L`/raw/follows/precedence/NIX_PATH smoke and the four CI integration suites.
These are pending, not verification claims. No production deployment occurred.

## Reviewer selection and lanes

Overall risk: high, due to incompatible CLI/Nix/Ruby contracts, persisted
local generation handling, retention/GC roots, deployment selection and rollback.
Selected retained reviewer0: review-purpose, ready, read-only, independent of
all authored changes, saved gpt-6.1-sol/xhigh. No fallback or setting override.
Read mandatory-change-review SKILL.md and all four references: general,
architecture/repetition, scope/proportionality, risk/compatibility. Perform review
directly with no nested reviewers/agents. Read applicable workspace/repository
instructions and verify this exact session identity from the tracking cwd.

Report findings by severity with file/line/commit evidence, distinct lane
reasoning, whole-series history disposition, migration-lineage conclusion and
remaining test/deployment limits. Remain read-only; return the report to the lead
for recording. No source/coordination edits, commits, pushes or lifecycle action.
