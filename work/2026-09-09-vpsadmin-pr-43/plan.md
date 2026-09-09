# Prepare vpsAdmin PR #43 for approval

## Goal and affected repositories

Prepare and push `2026-09-09-vpsadmin-pr-43` in vpsadmin with the reviewed
payment-history feature, an API JSON compatibility fix, and bilingual cursor
documentation. Stop for the user's explicit review before merging. The existing
PR source branch and master must remain unchanged during preparation.

## Implementation and commit split

1. Rebase the original PR commit, preserving authorship, onto current
   origin/master (inspected at 41af23e207478af2469e1d6423312930e720ba87).
2. Add a separate API JSON dependency fix: declare json < 3 in api/Gemfile and
   regenerate its packaged Gemfile, lockfile and gemset with
   `rake vpsadmin:gems:api`. These generated files describe the same dependency
   constraint and belong with it; do not update other packages.
3. Add a separate cursor-documentation commit: patch only UserPayment::Index
   from_id metadata, preserve labels/type/validation, and localize the new
   description in Czech and English using the workspace writing skill. Explain
   last-row continuation, unchanged filters and unavailable-cursor empty pages.
4. Extend existing payment specs for bilingual OPTIONS, unaffected inherited
   metadata on another action, and unavailable/filtered cursors.

## Compatibility and deployment

The added date inputs are optional. Preserve the PR's created_at DESC/id DESC
pagination and tenant restrictions. The existing WebUI uses the last returned
payment ID and remains compatible. The inherited numeric-threshold description
must be replaced for this action only.

ActiveSupport 8.1.3.1 passes JSON.parse options positionally, while JSON 3.0.2
accepts keyword options. Constrain only the API bundle to compatible JSON 2.x;
there is no Rails upgrade, runtime monkey patch, or persisted JSON conversion.
No new data/schema changes are added. The original secondary-index migration
is reversible and works with old/new API code. No daemon protocol, on-disk,
Nix option, client pin, or WebUI behavior changes are included.

No production deployment or migration execution is authorized. Future rollout
uses the usual index-migration window and completes API rollout before the
dependent WebUI Next feature. Old code can read data produced by this change.

## Verification and review

Use repository Nix shells and mandatory Overcommit hooks. Verify JSON decoding
and API startup with development and packaged dependencies, focused payment
and retained boundary specs, isolated migration up/down, i18n health, Ruby
syntax and lint. Run the mandatory general, architecture, scope and risk review
lanes on the final committed series with gpt-5.6-sol/xhigh fresh contexts.

Push only the development branch. Require successful RuboCop, i18n health,
API Specs including topic coverage, API Migration Specs and any other triggered
non-integration workflow on the final head. Dispatch a required workflow if
path filtering omits it. Investigate failures and fix them. Cancel only runs
superseded by a later push on this development branch.

Do not wait for CI / Run selected ci-tagged tests. Leave current integration
runs running and report their status in the review handoff.

## Approval and eventual integration

After validation, provide the development branch, exact commits, comparison
link, checks and findings. Keep tracking/worktree active and wait for explicit
merge approval. Only after approval, update the PR source branch with an exact
lease where needed, recheck upstream, and integrate using a fresh target
worktree, git merge --ff-only and an SSH push to master. Any needed rebase or
further change after approval returns the updated head for review. Never use
GitHub merge operations or force-push master. Retain branches after integration.
