# Git mirror rework: bounded verification brief

Accepted design: [current Git contract](design.md#current-revision-git-evidence-through-shared-mirrors).
This is a prepared verification plan, not an execution receipt. Implementer1
owns confctl and its checks; implementer0 owns all seven consumers and their
prepared extraction drivers. The lead owns final review, publication, manifests
and fresh serialized Luna watcher launches. Architect performs no runtime here.

## Baseline and affected boundary

Start from provider R `5436d3d7c36d3d5174eab3c44e3578830749d3db` and the exact
eight heads in [final-source-inventory-2.json](verification/final-source-inventory-2.json).
Keep [R acceptance](verification/final-acceptance.json),
[R full workflow summary](verification/final-workflow-summary.json),
[R exported check](verification/provider-R-exported-check/retained.json),
[R local Git race](verification/git-race-r-success/retained.json) and
[Terraform eight-example result](verification/terraform-workflows-success/retained.json)
intact. These receipts prove their recorded source, package and inputs only.

The new delta is the evidence backend, shared mirror coordination/integrity,
their tests/docs, and seven consumers' cache steps, API-only token text/env and
final CI tool pins. Retain graph/source policy, transaction/extraction rules,
manual updates, full-SHA JSON metadata, packaged Ruby startup behavior, hook
environment, application code and consumer dependency locks unless a separate
material finding is accepted. The package source changes even when its Git/Nix/
Ruby dependency inputs do not: record both boundaries rather than assuming an
old passing package is equivalent.

| Repository | Exact workflow path | Retained updater selection/helper |
| --- | --- | --- |
| haveapi | `.github/workflows/update-nixpkgs.yml` | Root `nixpkgs`; `utils/update-nixpkgs.sh`. |
| terraform-provider-vpsadmin | `.github/workflows/update-vpsadmin-flake.yml` | Root `vpsadmin`; `tools/update-vpsadmin-flake-input.sh`. |
| vpsadminos | `.github/workflows/flake-update.yml` | `--all`; `.github/workflows/scripts/flake-update-commit-message.rb`. |
| vpsf-status | `.github/workflows/update-dependencies.yml` | Semantic `nixpkgs`, terminal `vpsadmin/vpsadminos/nixpkgs`; full-SHA subject metadata. |
| vpsfree-irc-bot | `.github/workflows/nixpkgs-update.yml` | Same terminal selector; `tools/update_nixpkgs_flake.sh` and full-SHA subject metadata. |
| vpsfree-cz-configuration | `.github/workflows/daily-update.yml` | Existing channel selector sequence and conditional llm-agents version check. |
| vpsadminos-org-configuration | `.github/workflows/daily-update.yml` | Existing stable `nixpkgs` and os-staging sequence. |

HaveAPI remains the tested head `74f1cef68946fe4d6a6bc0a25c626df18c7232cf` on
base `7ac977a26080d45d44b6608aafad2cadd2ec7f81`; do not refresh to default
`1103a3a14b1dc6dec17fc4859df80220a54f111d` during this rework. The table is
coverage of these retained sources, not a renewed audit of every remote default,
external bot or non-default workflow.

## Author checks before final review

Use repository-declared quick checks. Tests must exercise the actual Git
executable against disposable local bare repositories, alongside provider wiring
and existing transaction/graph checks. Keep fixture configuration fabricated
and isolated; never inspect real credentials/configuration to build a fixture.

- DAG outcomes: equality/no work, forward, backward, divergent and unrelated
  roots; a cherry-pick does not qualify, while a descendant revert still does.
  Validate result-to-CLI mapping and all-or-nothing retention on error/rejection.
- Exact objects/history: missing tip fetched by immutable SHA; unavailable tip,
  raw tag/tree/blob, missing deep parent, wrong origin, shallow/graft/alternate/
  common-store/partial-promisor states all error. Replacement refs cannot alter
  proof. Negative traversal must fail on missing commit parents; irrelevant
  missing tree/blob data must not force a general fsck requirement.
- Cache lifecycle: old exact-URL layout reused, cold clone installed atomically,
  failed clone leaves no authoritative hit and subsequent attempt can succeed,
  warm objects need no fetch, missing detached objects can refetch. Case-sensitive
  cache keys retain current behavior even when source identity normalizes case.
- Coordination: concurrent cold users, guard versus changelog setup/read, and
  exception release use the same sibling lock. Both real changelog callers are
  covered; manual soft changelog failure remains distinct from strict evidence
  failure. Any reentrant implementation detail needs focused deadlock coverage.
- Process boundary: inherited repository/object/replacement redirection cannot
  redirect proof; ordinary fabricated URL rewrite/auth configuration survives.
  Git errors are sanitized, no REST/API fallback or token lookup remains, and
  Ruby/BUNDLE parent/child behavior is unchanged.
- Consumers: all seven use one final immutable CI pin, five acquire cache pairs,
  all seven save under `!cancelled()`, and a cache hit/miss/save does not bypass
  guard failure or permit publication. Retain selector/subject/final-lock tests
  and update documentation without adding resolver/provider copies.

Record exact commands, counts and outcomes. Do not hard-code the old count of
197 as the new expectation: Git fixtures replace API examples and add coverage.
Required real-Git or package cases must not silently become pending examples.

## Ordered affected checks after final committed review

Freeze the final confctl revision and seven consumer heads; capture reviewed
base-to-head ranges and final diffs, retaining historical R source refs/receipts.
Consolidate the superseded provider implementation and pin streams according to
the lead's history/review procedure. Publish the final provider before consumers
that reference it. This is feature publication, not default-branch integration.
No new runtime starts before the lead accepts the final committed review packet.

1. **Exact package and exported specs.** Run the final flake's exported RSpec
   check, whose `src=self` and `CONFCTL_BIN` bind source and actual package.
   Capture derivation/output paths, immutable source, complete input graph and
   packaged Git/Nix/Ruby versions. Include real local Git cases and the existing
   two real caller-preload/hook cases. This replaces a duplicate source-suite
   invocation; the prior 197-example R result is historical only.
2. **Actual caller boundaries.** Use the same final package inside IRC and both
   configuration environments with actual caller hooks. Preserve caller Ruby/
   BUNDLE state; do not sanitize it to make the check pass. Retain the narrow
   test-harness `BUNDLER_SETUP` distinction and Nix-store shebang portability
   already established. Record old configuration output compatibility and
   unchanged deployment-tool pins.
3. **Seven selected updater paths.** Adapt existing extraction drivers minimally,
   recording exact workflow/helper blobs, commands, selectors and omissions.
   Exercise guarded candidate update, repository-specific commit creation and
   final committed-HEAD lock validation for every row above. For status/IRC
   preserve parent inputs and subject SHA lengths; for configuration channels
   retain the existing ordering and conditional llm-agents/version check. If a
   conditional arm is not taken, say so and cite its fixture coverage. Use only
   disposable clones and nonpublishing/local remotes.
4. **Shared cache and race.** Use one owned cache across the serialized selected
   paths: record one genuinely cold nixpkgs mirror clone followed by real warm
   reuse, with the exact URL/digest path, source objects and outcome. Record
   additional cold source mirrors honestly. Exercise target movement with the
   new provider and an actual local Git remote: ordinary non-force push rejects
   the stale update, and retry begins from a fresh target snapshot. Never fix a
   stale candidate by force-pushing or assuming a PR mechanism.

Steps 2–4 may share one driver where that avoids duplicate environment startup;
they are acceptance assertions, not a requirement for four separate processes.
Keep the root watcher's work serialized, and keep a mirror's lock scope local to
its Git operations. Do not hold it while running another repository's hooks.

These seven runs are **selected guarded updater/commit/final-lock checks**, not
complete workflow reruns. Omit standalone Go/Ruby dependency refresh and
application check/build stages, plus the Terraform eight-example VM. HaveAPI's
unchanged `utils/update-nixpkgs.sh` line 42 retains `nix flake check` after an
actual revision change and before commit; equality exits before it. The lead
accepted this existing conditional gate as part of the exact selected updater
path in [the scope correction](verification/git-cache-haveapi-inline-check-scope.json).
Its actual branch remains pending receipt inspection; do not claim the check
ran or was omitted yet. Preserve the frozen helper, drivers and manifests with
no fixture transformation, extra standalone check or batch restart. The kernel
policy remains unchanged. Preserve omitted stages' R receipts as component/source-bound
evidence and record retained input graphs. A new relevant source/input change or
failure can require additional checks through the lead; the Git backend
replacement alone does not justify unrelated rebuilds.

## Authentication, retention and receipts

The prepared scoped sources are public GitHub inputs and retained local/SSH
source clones; no private-input requirement has been identified. Remove the old
API-only `GITHUB_TOKEN` precondition and token-loader invocation from successor
drivers. Do not run `gh auth token`, dump environment/configuration, or have a
watcher load credentials. Preserve existing Git/Nix/publication authentication
where independently needed; the guard itself neither consults nor requires API
tokens. If an actual private-input requirement appears, stop that affected check
and report it to the lead rather than inventing authentication or fallback.
Nix's own GitHub fetch mechanism may still use HTTP APIs; “no API calls” here
means no compare/API backend or hidden fallback in confctl's ancestry evidence.

Retain each new built package/check output through an owned Nix-managed out-link
or GC root before dependent verification; record the exact target and verify
it still exists before reuse. A historical unrooted output disappeared for an
unproven reason, so a remembered store path is insufficient. Cache retention is
separate: preserve the session-owned mutable mirror directory across the scoped
checks, record its location, and do not replace another run's cache. No cleanup
or session lifecycle action is authorized by this brief.

Use successor manifest/driver/receipt filenames, leaving prior attempts intact.
Every receipt records final source/input/package identity, selected stages,
omitted stages, exact initial/final lock and HEAD identities, exit status,
cache cold/warm evidence and log location without secrets. Reuse existing
drivers and receipt formats; no general equivalence/test framework is needed.
Cold full-mirror cost, final hashes/counts and actual new runtime success remain
unverified until these checks run. The lead owns their acceptance and state.
