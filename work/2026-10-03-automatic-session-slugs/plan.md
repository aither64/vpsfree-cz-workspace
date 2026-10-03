# Automatic portal session slugs

Implement the accepted plan: creating a session from the portal requires only
the initial prompt and team selection. An optional custom slug remains available
under expanded options. Preserve the dated slug format and 48-character short
name limit. Scope is New session; forks, approved-plan creation and CLI naming
retain their existing contracts.

## Components and ownership

- `codex-web`: public isolated ephemeral-turn client helper, protocol corpus,
  meaningful tests and API documentation.
- `dev-workspace`: asynchronous naming, durable preparation requests, receipt
  handoff, upload ownership, browser drafts/progress, tests and feature docs.
- `vpsfree-dev-workspace`: runtime input update after the generic runtime is
  committed and pushed.
- Workspace feature worktree: assembled package input update and deployment.
- `vpsfree-cz-configuration`: inspect the aitherdev host contract; modify only
  if evidence shows a host change is required. Application deployment remains
  in the user profile, not system configuration.

The retained designer owns `design.md`; the implementer owns application edits.
The coordinator owns tracking, integration of reports and deployment. Retained
reviewer performs independent whole-branch review. Fresh catalog Luna/low
utilities run and monitor long checks. No default-branch integration is
authorized by the user's instruction to implement.

## Accepted design

The browser stores a random `clientRequestId` in its draft before submitting.
`POST /sessions` freezes the accepted snapshot (raw prompt, attachment IDs and
scope, date, custom name, resolved team/model settings). Same ID and same input
replays the operation; changed input with the same ID conflicts. Acceptance
persists before naming and immediately returns `/creations/<request-id>/`.
Status is at `/api/session-creations/<request-id>` and retries at its `/retry`
endpoint with receipt/attempt checks. Legacy explicit-name submissions without
a request ID remain supported. Progress shows the accepted prompt, elapsed
time and phases, then redirects to the reserved canonical session URL.

Use a public `codex.Client.RunEphemeralTurn` with model, effort, instructions,
input, JSON output schema and trusted private working directory. Utility
threads do not enter persisted conversation resume paths. Subscribe to their
notifications, wait for turn completion and the final agent message, then
interrupt/unsubscribe on cancellation. Disable tools and workspace instruction
inheritance. Validate every RPC shape against the pinned Codex schema.

Naming uses `gpt-6-luna` with low effort, independently of development settings.
Send at most the first 8 KiB of raw textual prompt at a UTF-8 boundary, without
attachment paths or contents. Request JSON `{"name":"..."}` with 3–6 English
words and validate lowercase ASCII kebab syntax, at most 48 characters. Limit
the entire operation, including connect/model lookup/queue, to 10 seconds and
two simultaneous calls per workspace. Missing model, timeout or invalid result
falls back deterministically: first nonempty line, lowercase, fold diacritics,
up to six ASCII words and word-boundary truncation. No useful words yields
`session`; attachment-only requests skip the model. Generated collisions use
`-2`, `-3`, etc. within the limit; custom collisions remain errors.

Persist separate private version-1 preparation records, leaving existing
manifest, lifecycle journal and creation receipt formats unchanged. Freeze the
generated base before reservation and final slug plus predetermined receipt ID
before handoff. Existing receipt acceptance must accept that supplied ID and
prove matching ID and request, never adopt an unrelated matching receipt.
Recovery between file writes resumes the exact operation. Reserve active,
archived, worktree, receipt and journal names under existing serialization.
Never rename a reserved session.

Reserve accepted upload scopes to request IDs before a slug exists. Reject
competing ownership and mutations. Retain accepted submissions, reconcile
before collection, then transfer to ordinary creation ownership. Keep complete
snapshots while unfinished, compact immutable request ID to receipt/slug/input
digest mappings afterward. Bound unfinished operations to 512 and completed
mappings to 10,000; reject admission rather than forgetting replay identity.
Server shutdown pauses naming, and package generation is revalidated before
mutations.

## Compatibility and recovery

No SQL schema, seeds, service message or host module contract changes are
expected. New API endpoints and the ephemeral client helper are additive.
Legacy explicit-name portal requests and all CLI behavior remain supported.
New state is isolated from slug-keyed receipts and journals. Old packages
ignore and retain it. Accepted uploads use existing pending retention so older
collection preserves them. Rolling forward restores preparation recovery UI.
Rollback can load existing standard receipts/manifests and completed sessions;
unfinished pre-slug requests pause until the newer package is restored. Verify
these claims with tests, including crash gaps and collection.

Update exact feature pins in dependency order: codex-web → dev-workspace →
vpsfree-dev-workspace → assembled workspace flake. Preserve unrelated Codex
and other dependency inputs, checking the complete nested lock diff. Deploy
the assembled workspace package with `workspace-host switch --source` from
the dedicated workspace worktree on aitherdev. Retain the previous profile
generation for rollback. Host configuration needs no deployment unless the
contract inspection shows otherwise; record any expansion before editing.

## Verification and acceptance

Quick meaningful tests cover automatic/custom naming, fallback, Unicode and
long prompts, attachment-only input, duplicate IDs and input conflicts,
distinct requests with the same prompt, concurrent collisions, response loss,
restart/crash handoff, upload ownership and collection/rollback, nonblocking
acceptance, ephemeral cancellation/isolation, draft preservation, safe URLs and
legacy callers. Browser syntax and protocol corpus must pass.

Commit intended changes after quick checks. Inventory each complete branch and
all persisted format changes, recording migration provenance (no database
migrations expected). Mandatory review covers general, architecture, scope and
risk/compatibility lanes, with all Blocking/Important findings resolved or
explicitly reconciled before longer tests. Run packaged Nix checks and live
protocol/browser checks through fresh watchers, then deploy and exercise
automatic/custom/retry behavior. Logs include naming duration/outcome, not
prompt text.

Keep public helper semantics in codex-web reference docs and creation/recovery
contracts in dev-workspace portal/session docs. Exact revisions, commands,
review evidence, rollout and rollback generation belong in this initiative.
Apply the user-facing writing skill in the context-owning coordinator before
committing final visible copy. Finish with active branches ready for explicit
merge direction; retain the session and all feature refs.
