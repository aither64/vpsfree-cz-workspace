# Final API branch review packet

## Outcome and authorization

Handle a closed SSO token while preserving independently valid OAuth access.
Capture the optional SSO token once; extend it only when present and earlier than
access expiry. Keep closed SSO tokens absent, preserve existing renewal policy
for present tokens, and retain all access/session/account denials. User also
requested API Specs full/core job limits of 60 minutes after the previous
full-platform job reached 45 minutes. Coverage keeps its 10-minute limit.

User authorizes fast-forward integration of both API and configuration master
branches after API Specs succeeds at the updated exact API head. Integration CI
is explicitly unawaited. Deployment belongs to the user; session remains open.
Read [plan](plan.md), [state](state.md), [design](design.md) and
[timeout evidence](api-specs-timeout.md).

## Complete branch and migration inventory

Worktree `worktrees/2026-10-03-newadmin-exception/vpsadmin`, branch
`2026-10-03-newadmin-exception`:

- Base: `148ef0eaed0459c825f1ba94b8dad2b9f3311b2f`.
- Final published head: `f9beb46e5206864bca9d37672e1419cf03661467`.
- Complete series:
  - af8a97670293f4aa9a57e3196ac263c9c9530644 api: preserve OAuth access after SSO closure
  - f9beb46e5206864bca9d37672e1419cf03661467 ci: allow 60 minutes for API spec topics

[Actual final diff](api-final.diff): four paths, 200 additions/6 removals.
The auth fix, invariant comment and two persisted spec files are one coherent
behavioral correction. The separately reversible workflow policy is its own
commit. No obsolete approach, fixup residue, unused compatibility path or
transitional mechanism remains. At the review checkpoint, tracked tree/index were clean and untracked `work/`
contained only observer logs. Lead subsequently relocated that intact capture
to canonical tracking storage; entire Git status is now clean. Source/ref
content did not change.

No migrations, schema, seed or persisted-format changes. No new migration
version has merge/release/deployment/external-use provenance to reconcile.
Existing nullable SSO token schema supports the handled state.

The full old channel pin `a65a4dfeb92a59df4a80a737a20bcbf8558793ff` to final head
contains 18 commits/18 changed paths: 16 already-merged dependency updates, the
auth fix and the timeout policy. Preserve supported merged dependency history.
The previously reviewed inherited delta changes 14 generated dependency paths;
no API implementation or migrations differ before the feature base.

## Checks and documentation

- Original-source regressions: 3 examples/3 intended nil.valid_to failures,
  including persisted cleanup, refresh and access authentication.
- Guarded source: three focused suites, 72 examples/zero failures; RuboCop passed.
- All original source/spec blobs are identical at af8 and f9. Runtime checks
  remain valid for the unchanged code; no needless rerun was performed.
- Workflow aliases-enabled YAML parse and structural comparison against af8
  prove exactly the two timeout fields changed. Matrix, patterns, plugin settings,
  steps, permissions, concurrency, actions and coverage are unchanged.
- Official action repositories confirm current imported release lines:
  checkout/upload 7.0.1 through v7, download 8.0.1 through v8 and Ruby setup
  1.327.0 through rolling v1. No action upgrade is needed.
- Final diff check and all mandatory applicable precommit/commit-msg hooks pass.
  Lead executed the implementer's unchanged prepared commit because the member
  sandbox denied the API i18n hook's local socket. No edit takeover/hook bypass.

See [implementation report](implementation-result.md), [red](red-regression-result.json),
[green](green-regression-result.json) and [verification](verification.md).
The lasting tokenless-SSO invariant is explained beside the owning source;
this bounded fix needs no separate product guide. Rollout state and rollback
preparation belong in [rollout](rollout.md), not product documentation.

## Review and compatibility

Overall high risk from authentication and the deployment pin. Retained eligible
independent reviewer0 uses saved gpt-6.1-sol/xhigh/read_only without overrides
or nested reviewers. All four affected lanes apply to the final series. Inspect
actual history/diff and explicitly conclude whether obsolete history remains and
whether migration lineage is sound, including no migrations. Preserve the prior
unchanged auth implementation review; assess the workflow follow-up directly.

Public API/OAuth/token formats, database state, clients/daemons and Nix options
are unchanged. Existing channel consumers and exact pinned WebUI source have
been inspected. Incremental API worker replacement is compatible; old workers
may still raise until replaced. Rollback reads unchanged state and restores the
defect. Close/renew concurrency is unchanged. No SSO recreation, refresh redesign,
WebUI update, fleet coordination or schema accommodation is introduced.

Final independent checkpoint passed all four affected lanes with no findings;
see [review](review.md). Exact-head API Specs is still pending at run 37151153953.
Configuration receives its own final pin review and API1/API2 builds.
