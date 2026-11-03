# HaveAPI 0.32.2 backport and release design

## Scope and verified baseline

Backport the complete applicable master-only source/documentation series into
the supported `haveapi-0.32` line and publish the coordinated 0.32.2 release.
The lead accepted this scope, including the TypeScript compatibility changes
below. No downstream deployment or master integration is included.

Session identity and `architect0` saved `workspace_write` access were verified.
Initial workspace tracking commit: `2e5bc7f`. Canonical repository:
`repos/haveapi.git`, remote `git@github.com:vpsfreecz/haveapi.git`.
Fresh SSH `ls-remote` on 2026-11-02 confirms:

- Source `master`: `f29c1e4675bc1f79641faa619b8c68ecec923c71`, VERSION `0.32.0`.
- Target `haveapi-0.32`: `9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`, VERSION `0.32.1`.
- Annotated `v0.32.1` peels to that target; `v0.32.0` peels to
  `0e7166a0f8f15827bfac051666a53bf449e999ec`.
- `haveapi-0.32` is the newest release branch; no `v0.32.2` tag exists.

Use remote-tracking refs, not the stale local `master`/`haveapi-0.32` branches.
Refresh before implementation/integration and escalate additional source changes
instead of silently adding them to this accepted scope.

## Exact source mapping

Cherry-pick these commits with `-x` in order. Preserve their source identities;
record resulting backport hashes in the lead's state/review receipt. These are
existing upstream commits, not new intermediate development history to squash.

| Order | Master commit | Change and dependency |
| --- | --- | --- |
| 1 | `661f571b91606ee33c3e6f4bdc7539fd518c48a4` | English/Czech documentation locale, controls, catalog and tests; foundation for the documentation series. |
| 2 | `0454207e0b31516dd71144d3e367da9b50f87a38` | `doc/en` and `doc/cs` article layout, Czech articles, copying and nested gem packaging; keep together with locale lookup from 1. Includes Python CI/doc-reference path adjustments. |
| 3 | `69454b95a957b29d6108165aad27f4723958af76` | Performance receipt normalization for the exact documentation packaging change in 2; retains dependency/runtime/input guards and budgets. |
| 4 | `c85b1d1817795edca13f77437feb9048ebc96d59` | Localized generated comments/client guidance in server and Go/Rust/TypeScript adapters, using immutable locale contexts from 1. |
| 5 | `51047a211d71f817ab25f2def1692517f00c15c6` | Native GET example selectors, preserving enhanced JavaScript controls and documentation locale. |
| 6 | `ab4ffe1837c976f6062895a354fa656f46445cd0` | Hide singleton detail choices; follow-up to 5. |
| 7 | `15a148629e2d1cb821d9fc43e035fdfb5e6fbd12` | Load the Ruby client before generated rescue handlers. |
| 8 | `ef4c0cdcb349815538bb93cedab9d3964c565998` | Switch user before Sign out; retains native POST/CSRF behavior. |
| 9 | `50ae16c64be519772ab4191acbd797695c50334d` | Shorter English example-language label; canonical catalog and generated locale changes travel together. |
| 10 | `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7` | Content-versioned documentation CSS/JS URLs for upgrades and rollbacks. |
| 11 | `83689f883f9d82e0d18761f143c9e92d28940b31` | TypeScript live descriptions, typed metadata receipts, local input errors, namespace override and runtime/smoke alignment to 0.32.0. |
| 12 | `f29c1e4675bc1f79641faa619b8c68ecec923c71` | Clarifies generated-client wording from 11. |

Do not repeat these already-present changes:

- Master `209a7ac0` ↔ target `9d404273`: performance CI default-ancestry handling.
- Master `ff0c2f07` ↔ target `0116bbe1`: switch-user revoke parameters.
- Master `391b0190` ↔ target `9efeadf9`: release fixture version independence.
- Master `cc06cb8c2a6305f13d3b80ebc0a461507055b14c` is the 0.32.1 changelog
  already included by target release commit `c54404c0`. The current CHANGELOG
  blob is identical on source and target:
  `8d8337a5fb5b0cc13d0df1cdc293123430e1755e`.

The three source/backport pairs are marked equivalent by `git log --left-right
--cherry-mark origin/haveapi-0.32...origin/master`. Exclude master version
metadata; retain patch-line metadata and then update it to 0.32.2.

## Implementation boundary and interfaces

One complete execution package belongs to `implementer0`, assigned by the lead.
Its feature worktree is `worktrees/2026-11-02-backport-and-publish-release/haveapi`,
based on the exact target above. Serialize its Git operations and source edits;
the commits overlap catalogs, server views, documentation and release tooling.
There is no useful independent second source package.

The implementer owns all twelve backports, conflict diagnosis, repository docs,
version preparation, hooks, quick checks, commits and review fixes. Supply a
technical CHANGELOG draft to the lead and pause only the final metadata commit
for the lead's writing pass; source cherry-pick commits proceed. The lead owns
plan/state, user-facing release-note editing, acceptance, review assignment,
publication and approved integration. The architect owns this brief. Escalate
semantic conflicts or scope changes before adapting upstream behavior.

Read HaveAPI AGENTS and its development, release, localization and documentation
procedures, including the new paths introduced by the backports. For renderer
changes read `doc/en/client-examples.md` as routed by AGENTS; for performance
changes read `doc/en/performance.md`. Do not hand-edit generated locale files.
No new infrastructure, publication helper or downstream project change is needed.

Preserve these interfaces/invariants:

- Documentation locale is request-scoped, distinct from API request locales;
  public `/doc/...` routes and fragment IDs survive the source directory move.
  Both languages and nested generated documentation must be in the server gem.
- Generated example executable source and wire samples retain their meaning;
  standalone adapters/older contexts retain English fallback.
- Authentication conditions, CSRF, authorization and API envelopes are retained.
- TypeScript `describe` uses the existing executor and protocol-2 OPTIONS routes;
  static generated presence does not establish authorization. Receipts preserve
  the full envelope and HTTP status, plus extensible metadata.
- Namespace overrides affect declared metadata positions only; Custom/nested
  payloads and original envelopes are preserved. Executor failures pass through.
- Performance comparison normalization is limited to the reviewed packaging
  statements; no reference, threshold, dependency or runtime guard changes.

## Compatibility, deployment and recovery

There are no database migrations, seeds, persistent on-disk schema changes,
Terraform/provider changes, node protocols or Nix configuration changes.
Existing API clients and previously generated clients keep working without
regeneration. Server/client machines need no coordinated update. Package users
upgrade through their usual package managers; this initiative deploys no fleet.

Explicitly mention the TypeScript generation boundary in 0.32.2 release notes:

- The supported JavaScript runtime becomes **exactly `haveapi-client@0.32.0`**,
  replacing the generator's previous exact 0.30.2 support. This independent
  tested runtime version must not be mechanically bumped to 0.32.2.
- New generated roots reserve `describe`; new helper/type export names are also
  reserved. Schemas colliding with those names are rejected during generation.
- An explicit action help route must contain its matching `?method=...` selector
  and matching placeholders. Only absent help uses the deterministic fallback.
- Generated local validation raises `ClientInputError`, still a `TypeError`
  subclass, with a pre-dispatch marker. Transport failures are not reclassified.

These constraints are intentional upstream behavior accepted by the lead for
this backport. Users needing regeneration must use the documented runtime and
valid snapshots; existing generated source is not rewritten by a package update.
The generator's own README already carries the detailed contract.

For rollback, select previous package versions and keep previous generated
clients/runtime pairs. No data rollback is required. Asset digests request CSS/JS
matching the selected server code. Do not overwrite published packages or tags;
defective published content requires a subsequent patch release.

## Version and release contract

Run release/version commands in the top-level Nix shell. Prepare ignored local
locks with `make release-deps` before `make version VERSION=0.32.2`.
Keep external dependency resolutions stable through versioning. Do not commit
library locks, generated server documentation or newly built package archives.

The version commit is separate from source commits. `make version` updates:

- Root `VERSION` and the server, Ruby-client, Go-, Rust- and TypeScript-generator
  `lib/haveapi/**/version.rb` constants.
- JS `package.json`, `src/haveapi/client.ts` and the existing tracked
  `dist/haveapi-client.js` version string; ignored npm lock identities also update.
- PHP `composer.json`/`src/Client.php` and Python `pyproject.toml`/ignored uv lock.
- Server/Go/Rust/TypeScript gemspec `haveapi-client` constraints and the
  activerecord-auth example Gemfile. Prepared Rust/TypeScript local locks update.
- Add the `# 2026-11-02 - version 0.32.2` CHANGELOG section (use actual release
  date if publication shifts), describing changed components and the TypeScript
  compatibility boundary. Unchanged components need no invented notes.

All maintained packages release together: RubyGems `haveapi-client`, `haveapi`,
`haveapi-go-client`, `haveapi-rust-client`, `haveapi-typescript-client`; npm
`haveapi-client` plus the browser bundle; PyPI `haveapi-client` wheel and sdist;
Composer `haveapi/client` via `vpsfreecz/haveapi-client-php`. Elixir is excluded;
the embedded Rust runtime is not a separate crates.io publication.

The existing `.github/workflows/release.yml` is authoritative. `make publish`
only prints instructions and fails. Branch pushes/workflow dispatch build only;
an annotated `v0.32.2` push triggers the protected publishing path. The lead
confirmed `HAVEAPI_RELEASE_ENABLED=true`, required reviewer `aither64`, and
`prevent_self_review=false`; no GitHub Release 0.32.2 exists. Registry OIDC and
PHP deploy-key validity remain subject to workflow preflight.

## Checks and acceptance

Before final independent review: finish all intended changes, install/verify
Overcommit in the owned worktree, use declared hooks for all commits, run
`git diff --check`, `bundle exec rake i18n:health`, source metadata
`ruby utils/release/cli.rb check-clean`, prepared-input `make release-check`, and
focused static/syntax/format checks for changed files. Hook installation/signing
uses the declared root bundle; hooks must not be bypassed. Retain upstream
cherry-pick attribution and follow temporary-file commit-message rules for any
new or adjusted commit.

The final review packet must inventory target-base → candidate-head history,
source/backport equivalence, complete diff, and an explicit **no migrations**
conclusion. Retain all upstream commits, including follow-up fixes: their history
is already integrated into source master and the repository release procedure
specifically requires `cherry-pick -x` provenance. Consolidate any newly introduced
repair noise before final review. No independent review of this planning record
alone is required.

After review, use the mandatory fresh verification watcher for long/uncertain
checks. Run the repository's existing full release build/test workflow on the
exact candidate head; it performs `make release-deps`, i18n health,
`make release-test`, `make release`, `make test`, npm packaged-consumer smoke,
Python packaged-consumer smoke and retained-artifact verification. `make release`
already covers Rust and TypeScript extracted-gem smoke tests. Do not duplicate
successful exact-head checks without a changed input or unresolved failure.

For focused failure diagnosis use existing `make test-documentation`,
`make test-typescript`, `make test-go-cli`, `make test-rust-unit`,
`make test-performance` and catalog/release specs; do not invent another harness.
Inspect applicable automatically triggered component/performance CI and failures.
Performance checks must preserve exact sources and dependency receipts; follow
the existing performance procedure rather than adding a fresh benchmark campaign.
The expected stopping condition is green required candidate checks with complete
artifacts, not repeated timing attempts to force a favorable measurement.

Acceptance is the exact twelve-commit mapping plus a focused 0.32.2 metadata
commit, clean tracked source, synchronized versions, passing hooks/quick checks,
independent whole-branch/content review, required full checks and public release
verification. No package claim rests on a bare build success alone.

## Lead release execution and receipts

1. Preserve original user authorization in state: integration only into
   HaveAPI `haveapi-0.32`, and publication of 0.32.2. No duplicate authorization
   question is needed; no master merge is authorized. Existing source fixes are
   already on master; any later master release-note synchronization is separate.
2. After checks/review, publish the development branch and capture the final
   comparison. Before integration read workspace coordination and the selected
   package's `workspace-host coordination guide`; acquire a short repository
   merge claim only for fresh target check, fast-forward merge/hooks, SSH push
   and remote verification. Release it before CI or record updates. A moved
   baseline or intervention requires releasing ownership before repair.
3. Ensure approved remote `haveapi-0.32` contains the exact candidate, then push
   its annotated `v0.32.2` tag. Never move tags or start a second tagged release
   while this one is incomplete. Tagged `check-clean v0.32.2` requires the remote
   tag and refreshes master; master must remain a valid patch-zero line.
4. Monitor the tag workflow through its candidate summary and retained
   `release-<run-id>` artifact. Approve the protected `release` environment using
   the already authorized publication scope once the exact candidate is verified.
5. The publishing job verifies saved bytes, creates a draft GitHub Release,
   preflights all registries/PHP, uploads missing original Python files, confirms
   their hashes, publishes the Ruby client before dependent gems, then npm/PHP,
   and publishes the GitHub Release only after all destinations pass.
6. Record final branch/tag hashes, workflow URL/run ID, artifact ID/manifest and
   original hashes, per-registry verification and PHP mirror source/tag. Verify
   Packagist separately because its indexing is asynchronous. Preserve exact
   source/input identities and the original artifacts for recovery.

Partial publication is not atomic. Inspect successful uploads against original
artifact identities/hashes before rerunning failed jobs. Missing public metadata
does not prove an upload failed. Preserve the original tag, artifact and draft
Release; do not rebuild accepted versions, retag, delete packages or use
`skip-existing`. Matching existing artifacts may be skipped by the existing
helpers; conflicts stop. Once diagnosis supports retry, use the original run's
failed-job recovery. Its retained-artifact contract governs older attempts.

The lead owns lifecycle accounting for the release target; do not weaken exact
final-head completion rules or integrate master merely to satisfy accounting.
No machine reservation, session closure or cleanup is part of this design.
