# Duplicate VPS deletion: minimal error guard

Status: authorized implementation brief, 2026-10-05. Design owner:
`architect0`; the lead owns coordination and the exact user-facing copy.
This document specifies the work; implementation and verification results
belong in the session state.

## Scope and superseded proposal

Replace the unexpected server error on an already soft-deleted VPS with a
localized, ordinary API error. Prepare an exact reviewed feature pin in the
`vpsadmin` channel of `vpsfree-cz-configuration`. Do not merge or deploy.

The earlier helper, resource-lock acquisition/transfer, pending-chain matching,
idempotent/no-op success, and concurrency redesign are **superseded** by the
user's narrower request. Do not implement those proposals or their additional
test infrastructure. There are no lifetime/model/helper/locking changes and no
nil-safe `state_id` change in this design.

## Source-backed diagnosis and limits

Initial source analysis used canonical `repos/vpsadmin.git` at
`9fc0648accd414246d6422e67106ae7217486020`, with relevant architecture context
from `doc/object_lifetimes.mdwn` and `doc/transactions.mdwn`. Source links below
identify that investigation baseline, not the eventual implementation head.

VPS DELETE loads the caller-restricted `Vps.including_deleted` scope, which
includes soft-deleted records. It derives the effective target from the user's
role and normalized `lazy` value, then calls `set_object_state` with
`expiration: true`
([resources/vps.rb:538](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/lib/vpsadmin/api/resources/vps.rb#L538),
[model/vps.rb:139](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/models/vps.rb#L139)).

For `soft_delete -> soft_delete`, the lifetime calculation
`enter = target_index > current_index` is false. It therefore looks up a
`leave/soft_delete` default, and missing expiration raises the reported
exception before wrapper lock acquisition
([lifetimes.rb:465](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/lib/vpsadmin/api/lifetimes.rb#L465),
[lifetimes.rb:509](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/lib/vpsadmin/api/lifetimes.rb#L509)).
Adding that default would conceal an invalid transition and is not the fix.

The lead's sanitized evidence identifies three failing DELETE requests, with
`direction=leave,state=soft_delete`, from WebUI, Go HTTP client, and
`vpsfreectl`. May reports identify deployed revision
`8cd6889929f90199d4edd166d8ffcf8eb1e9868f`; October identifies
`f9beb46e5206864bca9d37672e1419cf03661467`. May code checked the owner's
state only. October and the investigation baseline additionally check the VPS
state, so a normal owner's serialized repeat generally encounters the generic
access error first. Admins bypass that state check
([lifetimes.rb:623](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/lib/vpsadmin/api/lifetimes.rb#L623)).
The new guard covers both paths. Actual actor roles and preceding chain outcomes
are unknown; raw request values do not establish normalized input or role.
Raw emails remain outside version control.

While a deletion runs, its final state normally awaits an edit-after
confirmation; a repeat can therefore still see active/suspended and encounter
the existing resource lock
([wrapper.rb:35](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/models/transaction_chains/lifetimes/wrapper.rb#L35)).
`ResourceLocked` already returns HTTP 423
([api.rb:260](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/lib/vpsadmin/api.rb#L260)).
This guard preserves that path. Stale concurrent reads and chain outcomes are
outside the fix; the investigation did not reproduce them at runtime. The
message describes stored state and must not claim node work succeeded.

## Exact implementation contract

In `VpsAdmin::API::Resources::VPS::Delete#exec`, retain this order:

1. Caller-restricted VPS lookup.
2. Existing maintenance check.
3. Existing effective target selection.
4. `object_state_check!(vps.user)`.
5. The new guard below.
6. Existing generic VPS state check, including the suspended-to-soft-delete
   exception.
7. Existing `set_object_state`, chain handling, and success response.

Insert only this behavior between steps 4 and 6:

```ruby
if state == :soft_delete && vps.object_state == 'soft_delete'
  error!(VpsAdmin::API::I18n.message('errors.vps_already_marked_for_deletion'))
end
```

Add `vpsadmin.errors.vps_already_marked_for_deletion` to the English and Czech
API locales, using the lead-approved wording exactly:

| Locale | Message |
| --- | --- |
| English | This VPS is already marked for deletion. |
| Czech | VPS už je označeno ke smazání. |

The lead applied the user-facing-writing workflow and owns this copy.
`I18n.message` supplies the existing `vpsadmin` scope
([i18n.rb:30](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/lib/vpsadmin/api/i18n.rb#L30)).
Preserve the repository's locale-generation conventions.

Return the ordinary `error!` response: HTTP 200 with JSON `status: false`
and the localized message. This is consistent with existing resource-error
specs
([vps_write_spec.rb:504](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/spec/api/resources/vps_write_spec.rb#L504)).
It is not successful deletion or an accepted pending operation. Leave
`Delete#state_id` unchanged: ordinary error paths already exit before a chain
is set.

Implementation files are limited to:

- `api/lib/vpsadmin/api/resources/vps.rb`.
- `api/lib/vpsadmin/api/locales/en.yml` and `cs.yml`.
- Focused regression coverage in the existing
  `api/spec/api/resources/vps_write_spec.rb` and existing locale-test locations
  as appropriate.
- The separate configuration input pin described below.

A short nearby explanation of guard ordering is sufficient if useful.
This session brief preserves the diagnosis; no general lifecycle documentation
rewrite or WebUI controls/layout change is needed.

## Invariants and acceptance criteria

- Foreign, missing, and hard-deleted records retain restricted lookup behavior.
  Authentication, ownership, maintenance, and owner-state checks keep their
  existing precedence and admin exceptions.
- An eligible owner or admin requesting soft deletion of an already
  soft-deleted VPS gets the exact localized ordinary error, not a server error.
  `set_object_state` is not called.
- The guarded request leaves expiration/reminder dates, state logs, chain count,
  resource allocations, and node work unchanged.
- Admin `lazy: false` on a soft-deleted VPS still reaches
  `set_object_state(:hard_delete, ...)`.
- Active/suspended deletion behavior, in-flight HTTP 423 conflicts, and genuine
  missing enter-state expiration defaults remain unchanged.
- No new helpers, state transitions, chain reuse, locks, retries, successful
  no-op response, state-ID handling, migrations, or concurrency guarantee are
  introduced.

The WebUI may continue showing its existing deletion-failed presentation while
rendering the meaningful API message. This scope changes the error explanation,
not the operation outcome or client flow.

## Compatibility, downstream pin, and recovery

The fix changes no routes, inputs, response schema, generated clients, CLI or
Terraform contract, persisted state, on-disk format, database schema/seeds,
transaction types, node messages, Nix options, or vpsAdminOS behavior. It
introduces no migration and requires no coordinated node upgrade.

Prepare the configuration change only after the exact source feature head is
reviewed, passes the required checks, and is published. Use the session's
configuration feature worktree and its Nix environment:

```sh
confctl inputs channel set --commit vpsadmin vpsadmin FIX_SHA
```

Replace `FIX_SHA` with that exact reviewed published feature commit. The
`vpsadmin` channel's `vpsadmin` role maps to `vpsadminServices`
([flake.nix:100](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/b6e650ad902482b4c4e66b5a89a4275bed92419e/flake.nix#L100)).
Keep production/staging pins and unrelated inputs unchanged. Preserve the
generated commit/changelog, inspect the entire lock diff, and verify the selected
revision and existing follows. Do not manually edit `flake.lock`, merge either
repository, deploy, or run a production dry activation under this assignment.

Inventory the complete old-pin-to-feature delta. At the read-only configuration
baseline `b6e650ad902482b4c4e66b5a89a4275bed92419e`,
`vpsadminServices` pins `c38839d5be62e9d40d055b23a84844e2037ba4db`, which
is newer than the initial investigation baseline. Its delta to October's
deployed `f9beb46e5206864bca9d37672e1419cf03661467` includes
`20260909170000_add_ip_release_campaigns.rb`. Thus the fix itself is
migration-free, but a cumulative channel bump cannot be described as such
without checking its full history. Before any future activation, establish the
actual deployed revision and migration provenance; API `autoSetup` is false
([common/api.nix:39](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/b6e650ad902482b4c4e66b5a89a4275bed92419e/cluster/cz.vpsfree/vpsadmin/common/api.nix#L39)).
Do not pin an old-baseline feature that drops intervening changes.

If deployment is separately authorized later, mixed API workers are compatible;
older workers can still emit the old error until all API workers update.
Existing nodes and chains require no changes. Reverting the application/config
revision restores the old error behavior without state conversion for this fix.
Any cumulative pin's rollback must account for its other changes and migrations.
Never release failed/fatal locks, rewrite logs, or alter deletion deadlines as
part of this fix or its rollback.

## Verification brief

The design is based on source analysis and sanitized reports; no runtime
reproduction or new test results are claimed here.

Quick checks after implementation, using the repository's API Nix environment:

1. Exercise already-soft-deleted VPS requests for both ordinary owner and admin,
   with English and Czech message resolution. Assert HTTP 200,
   `status: false`, exact text, and no call to `set_object_state`.
   Compare expiration/reminder dates, state-log count, and chain count before
   and after the request.
2. Verify admin hard-delete escalation from soft-delete still calls
   `set_object_state(:hard_delete, ...)`.
3. Retain/rerun relevant authentication, foreign-VPS, maintenance, owner-state,
   active-delete, and suspended-delete checks. Check that an active/suspended
   request raising `ResourceLocked` still returns HTTP 423.
4. Run changed-file Ruby lint and the existing API locale
   validation/normalization checks. Keep exact approved copy and inspect
   generated diffs for unrelated changes.

The existing Delete specs stub `set_object_state`
([vps_write_spec.rb:732](https://github.com/vpsfreecz/vpsadmin/blob/9fc0648accd414246d6422e67106ae7217486020/api/spec/api/resources/vps_write_spec.rb#L732)).
A negative-call expectation is meaningful for this guard: it proves the
exception-producing path is not entered. There is no need for the superseded
real-chain concurrency suite, transactional-fixture changes, or a new VM lane.

After the intended source changes are committed and quick checks pass, run
mandatory independent final review with the complete branch diff/history and
an explicit no-new-migration conclusion. Existing CI coverage and any
repository-required longer checks follow that gate. Delegate checks/builds of
uncertain or long duration to the required fresh watcher; no new concurrency
or integration lane is requested solely for this guard.

For the downstream pin, verify `vpsadminServices` resolves to the reviewed
feature SHA and only intended lock entries changed. If scoped configuration
builds are selected under the normal verification procedure, target the API
consumers `cz.vpsfree/vpsadmin/int.api1` and `int.api2`; builds are not
deployment or merge approval. Record outcomes and cumulative migration
provenance in lead-owned session tracking.
