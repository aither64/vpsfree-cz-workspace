# PR 43 implementation review packet

Requested outcome: prepare the reviewed payment-history feature and its cursor
documentation improvement on a development branch. The user also approved an
API JSON dependency fix after fresh bundles and current master proved unable
to boot with JSON 3. Stop before merge for the user's review. Do not update
master or the original PR source branch. Do not post GitHub messages.

## Location and boundaries

- Workspace: /home/aither/workspace/ai/vpsfree.cz
- Initiative: work/2026-09-09-vpsadmin-pr-43
- Plan/state: plan.md and state.md in the initiative directory.
- Repository worktree: worktrees/2026-09-09-vpsadmin-pr-43/vpsadmin
- Branch: 2026-09-09-vpsadmin-pr-43
- Base: 41af23e207478af2469e1d6423312930e720ba87
- Head: 19971f039771500d5d0304610f91fe6f4af5fed3

Review the complete committed series and repository AGENTS.md. Earlier
review-*.md files concern the original PR and are historical, not this review.
The intended split is the original feature commit (preserving authorship),
a separate JSON compatibility commit including its generated package metadata,
and a separate action-specific cursor description with locales and request
specs. The generated dependency files describe the same API dependency and
must remain consistent with its source Gemfile.

## Acceptance and non-goals

Preserve optional inclusive date bounds, created_at DESC/id DESC pagination,
and authorization. Explain from_id as continuation after the previous page's
last payment, using the same filters; an unavailable or filtered-out payment
returns an empty page. Change only this action's description, preserving
labels, parameter types and validation. Verify Czech and English metadata and
an unaffected endpoint, plus unavailable cursor cases.

Constrain json below 3 only in the API bundle. ActiveSupport 8.1.3.1 invokes
JSON.parse with positional options; JSON 3.0.2 accepts keyword options and
raises before API startup. Regeneration selects JSON 2.21.2 without other
version changes. No Rails upgrade, monkey patch, persisted-data conversion,
shared HaveAPI change, WebUI change, new schema guard, or other package update.

## Ownership, compatibility and deployment

Owner: plugins/payments/api/resources/user_payment.rb. HaveAPI 0.29.8 provides
the ActiveRecord pagination block and parameter metadata DSL. The application
overrides its description using a plain literal; inherited LocalizedMessage
descriptions on other actions remain owned by HaveAPI. The generator compacts
the new application translation to vpsadmin.attributes.from_id; bilingual
OPTIONS specs verify another action is unaffected.

Existing WebUI consumers are payment log/user_payment_history in
webui/forms/users.forms.php, using last-row from_id with user/accounted_by
filters. WebUI pins haveapi/client 0.29.6. No companion WebUI Next revision was
supplied. Canonical bare repos under repos/ are available for read-only context.

The original secondary-index migration is reversible, retains stored data,
and works with old/new API code. Use the usual index-migration window for any
future deployment; API must precede dependent WebUI Next use. No deployment is
authorized. No daemon protocol, client pin, on-disk format, or Nix option
changes. Production-scale index timing and dependent frontend end-to-end tests
are residual limits. The user excludes long VM integration CI from the gate.

## Verification and review procedure

Commits: ed8121659 (original feature), a22f37263 (JSON), 19971f039 (cursor).
The worktree is clean and upstream was re-fetched without advancing the base.

Quick verification passed using repository Nix shells:

- API-shell RuboCop: three touched files, zero offenses; diff whitespace clean.
- Payment request suite: 25 examples, zero failures (seed 54261).
- Retained review-probes.rb: seven examples, zero failures (seed 6292).
- Migration spec in separate process with --options /dev/null: one example,
  zero failures, up and down verified.
- API locale regeneration and i18n:health passed.
- Nix vpsadmin-api package built from corrected metadata. Its wrapped Ruby
  passed positional-options JSON decoding and serialized-JSON roundtrip.
- Package ruby-env/bin/rspec ran worktree smoke/api_boot_spec.rb with packaged
  dependencies: five examples, zero failures (seed 51726).
- Both follow-up commits passed all mandatory Overcommit pre-commit hooks.
  Commit-message width warnings concern lines over 72; all lines are within
  the repository's required 80-character limit.

Do not start
Nix/Bundler/database jobs or change project files. Review directly and do not
spawn nested agents. Read the mandatory-change-review skill and assigned lane
reference at skills/mandatory-change-review/ in the workspace.

Classification: High (API cursor contract, tenant isolation, schema migration
and runtime dependency compatibility). Required lanes: general, architecture,
scope, risk. Model gpt-5.6-sol, reasoning xhigh, fresh contexts for every lane.
Write findings with Blocking/Important/Advisory severity, references and
concrete scenarios to implementation-review-<lane>.md in this initiative.
If none, state that clearly and record remaining test gaps. Send a concise
result to the coordinator.
