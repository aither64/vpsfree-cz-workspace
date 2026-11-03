# Published advisory corrections

## Admin-list pagination: test-only acceptance correction

The exact API `2823e0e75c67dbb94d90722b06e6fcaebf8c9a34` recovery passed
services-up34, user-core4 and lifecycle3. Admin-core passed its creation case,
failed its list-action case and skipped the final serial case. Actual native
failure is `tests/playwright/webui/specs/vps-admin-core.spec.cjs:151` in
`runFilteredListAction`: after Restart32, the notification and canonical
`page=adminvps&action=list` assertions passed, but row32 was not on the default
25-row list. The snapshot contains “Restart of 32 planned” and “VPS list [Admin
mode] / Limit: 25”. C intentionally uses the canonical list fallback when
strict-origin removes the previous `from_id`, `user` and `limit` query.

Implementer0 may change **only this existing spec owner**: call
`openAdminVpsListAround(page, vpsId)` after the existing notification/dialog and
`waitForQueryParams` assertions, before the row-visibility assertion. The helper
already submits the existing filters with `fromId: vpsId - 1`, `limit: 1` and
the fixture user. This restores the row-observation setup without weakening the
return-navigation acceptance: never navigate before verifying the action result
and returned URL. Preserve every action, login/auth, dialog, notification,
row/link/filter, transaction-settling and final status assertion and timeout.
No runtime helper, header, policy, fixture semantics or auth change is needed.

Amend C with the test-owner correction, preserving A/B and C's runtime patch;
retain old2823's exact review/execution ref and receipts. Run pinned Node syntax
and normal hooks/quick checks, then consolidate one final KB pin stream while
preserving its readiness-helper patch. Implementer1 refreshes the single config
pin only after stable final API handoff. All intended final ranges/pins are
committed and quick-passed before retained reviewer0's affected review, including
complete history/no-migrations and the test-versus-product acceptance distinction.

After review, run **only `webui#vps-admin-core`**, all three existing serial cases,
using the actual nonempty selector and existing runner, short owned socket-state
path and fresh watcher. Keep the original failed evidence; do not repeat passed
services-up/user-core/lifecycle, API or advisory browser campaigns by default.
Reuse them only with actual runtime/dependency/plugin/runner/guest-input proof
and a selected-script comparison showing their source/definition/filter unchanged.
The whole bundled Playwright suite/source revision can change because this one
spec changed; distinguish that provenance change from the unchanged selected
successful scripts and application inputs rather than claiming identical overall
derivations. Escalate any additional material input change before extending checks.

**Strict KB validation must repeat on the final source pin:** the mandatory
canonical workflow validates the final committed vpsAdmin revision, so the old
strict5df pass (467.87s) is retained but not called a final-pin execution. Run
normal strict `nix develop -c bin/check` after affected review, without overrides
or allow-missing. This adds no page/capture/media work; runtime/UI bytes and the
KB helper/content remain unchanged. Do not rerun successful managed KVM merely
for this test-only source-pin change when its actual consumed-input comparison
supports reuse. No source implementation by architect, product scope expansion,
CI retry, preview mutation, deployment, merge or lifecycle operation is included.

## HaveAPI 0.32.2 target refresh: compatibility and bounded checks

Read-only inspection supports compatible preparation on fresh vpsAdmin master
`5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`. Implementer0 may now reconcile the
separately committed C (`c037c5a8ee19302881b3873c464e54448e157584`) and A/B onto
that target with normal hooks and patch-equivalence/history proof, then prepare
one final KB pin and the stable API handoff for implementer1's config refresh.
No HaveAPI edits, consumer migration, deployment or merge is authorized.

Canonical release comparison is HaveAPI `v0.32.1`
(`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`) to `v0.32.2`
(`1ef9b204ba45bb261d3334be5c555cc1856b713b`). Server changes concern localized
HTML documentation, example generation, article packaging and content-versioned
assets. `server.rb` adds documentation helpers/routes; ordinary action dispatch
and root OPTIONS handling are unchanged. Action/resource/parameter/input/output,
authorization and count implementations are unchanged. The upstream locale spec
explicitly covers ordinary actions and OPTIONS retaining the API locale despite
documentation cookies/query parameters, and locale restoration after rendering.
These are inspected source assertions, not a newly executed upstream suite.

No advisory state/visibility/count/cursor/resource-input or success-envelope
contract change is identified. Existing parent scopes, six draft-sync guards and
their capability metadata remain authoritative. Ruby client executable source
differs only in `version.rb`. TypeScript generator adds live descriptions, typed
receipts, local `ClientInputError` and metadata-namespace handling; its release
notes preserve existing generated clients with their matching runtime. The
unchanged modern/client consumers need no regeneration or code change. Actual
consumer inspection, rather than compatibility promises for old generated clients,
establishes the modern boundary: configuration-selected modern `70bd11d` uses a
handwritten fetch transport and its production frontend/BFF build consumes
`pkgs`, source/provenance and checked-in npm locks through `buildNpmPackage`,
documentation audit and Vite; it takes no Services API/generator or
`haveapi-client` npm input. Feature modern1c has the same production build
boundary and uses locked `haveapi-client@0.32.0` through AsyncClient adapters,
not a regenerated SDK. The followed API flake input supplies terminology,
module-evaluation and VM-check contexts, not frontend/BFF production arguments.
Thus this Services API refresh adds no relevant TypeScript-generator or production
frontend/BFF input and warrants no extra modern build/code/regeneration campaign.
Metadata/live-wire compatibility remains covered by Ruby/API source findings
and final native feature evidence. Exporter
tooling now requires exact HaveAPI 0.32.2 rather than 0.32.1; its bootstrap,
sanitization and schema algorithms are unchanged. This pin change alone does not
require generating or migrating a client/schema artifact.

The target changes 13 dependency/tooling/docs paths with no C or application
overlap and no migrations. All five HaveAPI gems are 0.32.2; implementer0's
`rubygems-0322-pin-proof.json` verifies published gem SHA256 values against the
actual `packages/api/gemset.nix` hashes. Source tags, published gem hashes,
dynamic ignored locks and packaged Nix inputs remain distinct evidence. Capture
the actual loaded versions/effective full/core locks, selected source/NAR hashes,
derivations and complete pin graph after refresh; do not infer them from a version
declaration or reuse an old 0.32.1 lock silently. The upstream PHP Composer and
this session's modern/client locks are unchanged.

Available exact-master API runs `41534770638` and `41537522135` passed all 26
topics plus aggregate; RuboCop/i18n passed. Their integration runs were still in
progress at the bounded snapshot. These passes establish baseline evidence,
not this feature's interaction with 0.32.2 or a packaged-doc result.

**Verification order.** Preserve C's passed PHP syntax/unit/style and normal
hooks for their actual inputs; after reconciliation verify unchanged C patch
and actual PHP dependencies. Run normal final hooks and the existing exporter
database-free `safety_spec.rb`/`snapshot_spec.rb` checks under its documented
environment, plus final-source affected API metadata/read/mutation evidence with
actual 0.32.2 inputs. Prefer the ordinary final-head hosted API job artifacts for
full/core coverage over a duplicate local full-suite campaign. Before review,
use focused existing advisory examples only where necessary to verify changed
load/metadata integration; do not repeat the prior lock-order diagnoses or all
API/native suites by default. All intended changes must be committed and quick
checks pass before retained affected review, including the dependency/source
reuse boundary and complete A/B/C plus KB histories.

After review, **`./test-runner.sh test services-up` is required** by vpsAdmin
`docs/agent-instructions/testing.md` for this HaveAPI package update. It tests
packaged shared JSON-schema/protocol/client documentation and generated examples,
addressing the actual changed release surface. Its previous native script passed
34 checks in 154.8s; allow roughly 5–15 minutes with guest setup, with uncached
package realization recorded separately. Add this target to the existing three
failed WebUI scripts (15–25 minutes), enumerate the actual nonempty selection,
and use the normal fresh watcher/stop-on-failure procedure. No arbitrary
135-script/4.5-hour replay. Final KB still gets the mandatory strict contract
check at its final pin, with reported real drift disposition and no media campaign.

Retain previous 117 native successes, advisory18, API and strict/KVM evidence at
their actual old inputs. They are not literal final-input executions: packaged
HaveAPI changes invalidate blanket derivation equality. Reuse unaffected behavior
only with the reviewed release/source/input comparison, and verify changed docs,
startup and feature integration as above. If existing exact-input CI supplies a
required check, use its actual manifest/environment/outcome instead of rerunning
it locally. A new concrete failure returns to its owner; no auth policy,
Referrer-Policy, server-only privacy, storage or preview-data change is included.
Legacy host-mounted PHP effects remain as recorded in C's receipt; API preview
stays on `a38c`, modern1c remains unchanged, and no cluster driver is invoked.

## VPS return navigation: approved bounded integration fix

The lead approved this correction from actual final-head integration evidence.
In run `41497643925` on API `ebe0ab`, the three failed native scripts
`webui#vps-admin-core`, `webui#vps-lifecycle` and `webui#vps-user-core` successfully
planned Restart/Shutdown, then landed on Overview. The configured `strict-origin`
Referrer-Policy strips the path; `webui/lib/vps.lib.php`'s existing
`vps_run_redirect_path` accepts that same-host origin-only referrer as `/` instead
of its explicit VPS fallback. Implementer0 reproduced both list/detail failures
in the declared PHP environment and confirmed full filtered referrers work.
This is a proven wrong destination, not a deadline or asserted baseline failure.

Implementer0 owns the existing helper and its existing PHP unit test (about two
paths). Ignore only an origin-only target with missing/empty query, with or
without the trailing slash, and use the existing explicit list/detail fallback.
Use canonical list fallback `?page=adminvps&action=list` if the existing fallback
needs correction; preserve detail `info`/`id`. Root `/` with a nonempty query is
valid WebUI routing and remains accepted, as do full same-host filtered/paginated
targets. Preserve existing local-redirect validation, foreign/absent/reflexive
referrer handling, authentication, CSRF, Referrer-Policy, JavaScript, assertions
and timeouts. No URI framework, unrelated hardening, copy/catalog/style change,
navigation semantic IDs or default screenshot campaign.

Extend the owning unit tests for origin-only slash/no-slash with list and detail
fallbacks; absent, reflexive and foreign referrers; meaningful root query; and
full filtered/paginated same-host return paths. Run declared PHP syntax, targeted
PHPUnit and normal hooks. Commit the correction as separate logical **C** after
original API A and advisory legacy B: this VPS navigation fix has an independent
purpose and must not be folded into B. All intended changes are committed and
quick-checked before retained affected review. No speculative backend/auth fix.

After review, run only the three failed native scripts through their actual
existing **nonempty** selector; verify the selected names before launch. Expected
duration is 15–25 minutes versus the original 16.1-minute WebUI run. Use the
normal fresh Luna/low watcher and stop on actual failure. Preserve the 117 other
successful native tests and exact-`ebe0ab` advisory 18-test success, API, strict
KB and KVM evidence for their actual sources and inputs. No 135-script/4.5-hour
workflow repeat by default. Prove relevant source, dependency, runner and guest
derivation identity before reuse; a package revision-label change is not itself
changed backend behavior, and a source-only comparison is not full input proof.

At stable final API head, implementer0 consolidates the single final KB pin
stream and evaluates the mandatory actual contract/drift; implementer1 then
consolidates the configuration pin from the exact handoff. This restores intended
VPS return navigation rather than introducing new UI concepts. No production KB,
staging or capture campaign without an actual reported need. Retain the separate
KB readiness-helper commit and previous check provenance.

Before editing, implementer0 records whether the development PHP service reads
the host worktree live. If so, authorized source edits can immediately affect
PHP behavior without a separate activation; report the actual source effect
instead of calling that runtime unchanged. No additional driver, cluster update,
fixture write, browser campaign, reset/stop, deployment or merge is authorized.
API preview `a38c`, modern1c and stored data remain; backend/client/modern product
behavior and server-only advisory privacy are unchanged. Implementation proceeds
under this accepted brief without another product question or per-command release.

## Final-head foundation failure: bounded diagnostic disposition

This follow-up keeps frozen API `ebe0ab51509222fba69a53431ea512cea51e2b6a`,
KB `c46bc3f753439b962ae4e11c59a71e15c0a56b87` and config `2dde376` unchanged.
The lead accepted one diagnostic and automatic continuation to the missing KB
checks as specified below; implementer0 owns execution. No auth runtime change,
broad test campaign, deployment or preview operation is selected. The one hosted
rerun accepted after the completed diagnosis is recorded below.

**Completed diagnosis and selected hosted verification.** The one 39-case run
passed in exact original order (92.28s total, 25.48s setup, 50.29s native), using
Bundler 2.6.9 and current full lock `8e06732a…`. Its sanitized observations show
zero open transactions after all nine advisory cases, idle worker connections,
and no lock waits. Local Ruby 3.4.9/MariaDB 11.4.12 still differ from hosted
3.4.12/11.8.6. No actionable cleanup defect was found; strict/KVM checks resume.
The lead selected **one ordinary targeted rerun of the failed hosted
full-foundation job and dependent aggregate at exact `ebe0ab`**, with supported
Actions debug logging, to cover that remaining hosted environment distinction.
Implementer0 owns the normal parent mutation and monitoring coordination;
reviewer0 assesses the evidence/residual disposition concurrently. Retain
attempt 1 separately; do not rerun the 25 successful topic jobs or a second local
diagnostic. A pass verifies the current check, not the unknown original cause.
If it fails again, retain debug/native artifacts and return the result to the
lead; no retry loop, source/auth change or timeout adjustment is authorized.

**Observed failure.** Final API run `41497643976`, full-foundation job
`125456660302`, attempt 1, seed 57138: 1461 examples, one failure, three pending,
zero outside errors. Password-recovery case `[1:31]` failed after 50.65s at
`api/lib/vpsadmin/api/authentication/password_recovery.rb:265`, `user.lock!`,
with `ActiveRecord::LockWaitTimeout`. The spec's POST is at line 970. Its actual
blocking transaction/query identity was not retained. No resource-hook exception
record is expected from this custom-route path; absence is not evidence of no
DB failure. Core-mode success and unchanged route/spec bytes do not waive it.

Native JSON proves nine advisory-concurrency examples at positions 808–816,
18 intervening OOM/dataset examples, then eleven password cases at 835–845 before
failure 846. The contiguous segment totals 62.55s native including the timeout.
The advisory spec uses `:no_transaction`, worker `with_connection`, session/context
ensure cleanup, and joined/value-checked threads with `finish_threads` safeguards;
no cleanup exception is recorded. The failed case creates a **new** lifecycle
user under the ordinary per-example rollback transaction, not `SpecSeed.user`.
This narrows the question to actual connection/transaction ownership; it does
not identify a leaked worker or justify changing authentication locking.

Hosted full environment: Ruby 3.4.12, Bundler 2.6.9, RSpec 3.13.6, effective lock
`8e06732a351ca376e1acee926fb8a6c0d5b703a3d73f0b2d0578d32b80d2bdc5`, MariaDB
11.8.6, REPEATABLE-READ and `innodb_snapshot_isolation=0`. Existing local MariaDB
is 11.4.12. Capture the actual diagnostic full-plugin environment and effective
lock; do not infer them from packaged locks or call differing inputs identical.
Implementer0 found no workflow runs at exact master `1d4869b`. Compare the retained
successful `a38c` full-foundation artifact/environment/order if available, as
already requested, without a new baseline execution or broader history search.
That comparison narrows differences; it does not erase the current failed run.

**One selected run.** Using normal RSpec and an isolated test DB, execute only
native JSON `examples[808..846]` from the retained failed result, full-plugin
mode, seed 57138, with native JSON output and stop-on-first-failure. The paths are
the existing advisory concurrency, OOM-report, dataset full-download and password
recovery specs. Derive the exact 39 IDs from the saved artifact; verify the actual
ordered IDs before interpreting results. Keep the 18 intervening cases: they
cost about 2.5s native and remove an unnecessary ordering assumption. This is
not a 1461-example foundation replay. Budget about 3–8 minutes including ordinary
setup, record setup separately, and reassess unexpected duration rather than
extending application timeouts. A fresh Luna/low watcher owns the one run.

Use a temporary private diagnostic loaded through the existing runner to observe
thread/connection ownership and outstanding DB transactions after advisory
cleanup, before the password segment and at the failed request. During a lock
wait, a bounded native DB observer may record requesting/blocking transaction
and connection IDs, transaction state/age, lock table/index/mode and relevant
thread liveness/open-transaction counts. Restrict observations to this isolated
test database. Exclude SQL text/values, lock row data, tokens, credentials and
request/advisory bodies; do not dump process lists or InnoDB status verbatim.
Stop/join the observer when the run ends. Preserve ordinary test transactions,
timeouts and assertions; do not add an application/framework diagnostic layer.

**Outcome and automatic next action.** If failure or test interference reproduces,
retain the actual lock relationship and fix its proven owning test/cleanup code
before acceptance; any proposed auth runtime change returns to the lead with
evidence and a new bounded brief. Stop dependent expensive checks if that finding
requires an API successor. If no actionable source defect appears, end this
diagnostic after the one run, retain the original lock-holder/cause as UNKNOWN,
and automatically resume strict final-pin `nix develop -c bin/check` followed by
the previously selected managed KVM target on frozen `c46bc3f`. Those missing
checks have independent value and no concrete source fix currently makes their
discard inevitable. No per-command lead release or repeated plan is needed.

A diagnostic pass does not relabel the failed hosted full-foundation job green,
prove a flake, or cover an untested DB-version distinction. Report its exact
inputs and known residual for lead/reviewer readiness disposition alongside
actual final hosted results; do not announce unconditional readiness while a
required result remains failed or unresolved. Further reproduction needs a new
concrete finding, not the irrecoverability of the original lock identity.
Existing server-only privacy, all six client draft guards, modern1c, retained
data and no-migrations contract remain unchanged.

## Authorized merge preparation: current delivery delta

The user said “well then continue, prepare for merging”. This authorizes feature
preparation and verification, not integration or deployment. This section owns
the remaining readiness work; [visibility-design.md](visibility-design.md) owns
the server-only privacy contract and [visibility-verification.md](visibility-verification.md)
retains the actual failures, successes, inputs and running-preview evidence.
No new product decision is needed. Preserve the existing preview/data, unchanged
modern `1c8478bceb3943645ec06ccde895ee4b0985873f`, all six client draft guards,
correction/revision/locking/mail semantics and administrator access. No migrations,
UI campaign, new framework, production action or cluster operation is included.

**Ownership and target reconciliation.** Implementer0 owns all API/legacy/KB
edits, Git, diagnostics and required checks. Implementer1 holds config `25288bf`
until exact final API handoff, then makes one consolidated channel-pin refresh
with bounded graph/evaluation/remote proof. The lead owns scope acceptance and
independent review; architect edits this design only.

Implementer0 reports the authorized clean rebase complete, local/unpushed:
`37ea14b646e388db3bc1594b8153ae3311609b54` on master
`1d4869b6e81dd60916ecb96688ca14a192000b1f`. The old `097226b..a38c9f8` feature
patch is byte-equal to `1d4869b..37ea14b`; reconstruction matches the new tree,
range-diff maps both commits 1:1, normal hooks ran, and old refs/evidence remain.
The only old-head/new-head differences are the 16 generated dependency files
from the two upstream commits. Retain this proof and verify any further target
movement before final readiness. The preview still runs reviewed `a38c9f8`.

**Bounded API diagnostic and assertion correction.** Original hosted run
`41465157664`, job `125343963839`, attempt 1, seed `19905` failed child case
`spec/api/resources/security_advisory_spec.rb[1:3:2]` at line 511: requested
count 0 was nil. HTTP 200 and `rows || []` did not prove a successful envelope.
The original response/role/child was not retained and cannot be recovered.
The prior isolated 60-request pass is not cause proof or evidence of a flake.

Implementer0 reconstructed the hosted effective lock from its log, exactly
SHA256 `9a28f956043b65a7ca8ed7b96bcedad17a9d589154028934ec07b07bc4ed0bd1`.
Against successful local core lock `9ff97d9b998c7169302cf28f08c0bb3ef814dac660eec526ca7caec2d2200e05`,
the sole gem-version difference was `amq-protocol` 2.10.0 hosted versus 2.9.0
local; checksum/Bundler metadata also differed. The rebased baseline supplies
2.10.0, while its `domain_name` 0.7.20261031 differs from the original hosted
0.7.20261007. Hosted Ruby 3.4.12/Bundler 2.6.9 versus previous local
3.4.9/4.0.23 remains an explicit distinction; capture actual new identities,
effective lock, plugin mode, DB isolation and result order before interpreting
new results. Do not claim a fully identical hosted environment.

Add the conventional successful-envelope assertion before reading collection
rows/counts in the owning spec. On failure retain sanitized role, request path,
advisory state, HTTP status, success/error classification and requested/returned
metadata; no credentials or report bodies. Preserve all exact row/count/privacy
expectations. Inspect the actual request/count owners against the retained
artifacts; neither unsupported metadata nor a flaky test is an established cause.

Run one focused core diagnostic using normal RSpec, the isolated test DB and
seed 19905: the original twelve predecessor examples
`[1:10:2], [1:10:1], [1:10:3], [1:10:5], [1:10:4], [1:2:2], [1:2:4],
[1:2:3], [1:2:1], [1:9:1], [1:9:2], [1:9:3]`, then `[1:3:2]`, all in the
same resource file. Use the existing retained response diagnostic and native
JSON evidence; verify actual executed IDs/order rather than assuming filtering
preserves it. Expected duration is 6–8 minutes, not a quick gate. A fresh
Luna/low watcher launches it with stop-on-first-failure; it is diagnosis needed
to establish the final change and may precede final review. No whole-file/topic,
full/core or native campaign follows automatically.

If a current failure reproduces, fix its actual owner and run the affected
focused regression before acceptance. Otherwise stop this diagnostic after the
one evidence-based run: the missing old response is a named historical residual,
not an unbounded investigation requirement. Source inspection, stronger failure
evidence and exact-final hosted affected checks must support the readiness
conclusion. Independent review assesses that disposition; a green repetition
does not retrospectively fix or relabel the original failure. Any further run
needs a concrete remaining distinction and a narrower-alternative assessment.

**KB observation correction.** Managed run `41465898434`, job `125346565326`
failed five KVM readiness waits despite healthy HaveAPI 0.32.1 HTML; its literal
`API description` check is obsolete. In KB's existing
`tests/runner/extensions/vpsadmin_services.rb:92–107`, use the same behavior-based
readiness predicate already reviewed in the API-owned helper: unauthenticated
root OPTIONS `?describe=versions`, successful JSON envelope, Hash response,
versions Array, and a nonempty String default contained in that array.
Keep the existing host/caller/deadline/curl error behavior; malformed/error JSON
remains unready. Do not replace one HTML title with another, increase timeouts,
change production services or introduce a readiness framework. Reuse the narrow
valid/malformed/timeout/error checks described in [readiness-review.md](readiness-review.md)
and its [accepted review](readiness-final-review.md), adapted to this owner.
Commit this substantive helper correction distinctly from the one consolidated
final API pin stream; preserve unrelated KB inputs/content/captures.

**Ordered gates and reuse limits.** First finish the bounded diagnosis, owning
assertion/helper changes and focused regressions; run touched syntax/lint, helper
contract checks and normal hooks. Commit all intended final API/KB changes and
prepare exact ranges, range-diff, complete histories, no-migrations conclusion,
source/input identities and failure/residual disposition. The lead then assigns
affected independent review. Diagnostic runs above are not a substitute for
that final committed-deliverable gate.

After review, use exact-final hosted affected API results and native result/
environment artifacts to cover the failing core platform-operations path and
any changed owner. Check the formerly pending integration run's actual outcome
once; it is old-source evidence unless a matching final-input receipt establishes
reuse. A completed failed job requires its logs before any retry. Do not repeat
local full84/core74 by default. Those passes remain valid for their recorded
source/Ruby/bundle/DB inputs, but changed effective dependencies forbid claiming
automatic final-input equivalence. Use focused current-input coverage for the
actual changed risk and hosted evidence; if broader execution is necessary,
record which risk narrower checks cannot resolve before launching it.

Run mandatory strict `nix develop -c bin/check` on the final KB pin, then the
failed managed KVM target through its existing runner/selection to exercise the
changed readiness helper in a real guest. Preserve successful unrelated managed
results with their actual source/runner/guest-input receipts; compare those
inputs before reuse. No blanket managed/native rerun or new screenshot campaign.
Original native18 and live API66/modern24/legacy21 remain proofs of running
`a38c9f8` and unchanged modern1c, not execution of the rebased package. Modern
and client evidence can remain reused when their exact inputs are unchanged.

Hand the stable final pushed API revision to implementer1 for the consolidated
config refresh. Final readiness records exact pushed heads, target ancestry,
required check outcomes, review and any bounded historical residual. Do not
merge, claim integration readiness from pending checks, activate configuration,
update the preview or stop/reset its data under this preparation assignment.

## Approved visibility correction

The user explicitly agreed that **only published advisories are readable by
non-admins; draft and retracted advisories are admin-only**. Direct hidden reads
return 404 and related collections must not expose their content or membership.
Retraction remains silent and preserves administrator history; deletion remains
separate. The user subsequently directed that visibility belongs entirely to
the server and the UIs display its authorized responses. The API is the sole
authority: central `visible_to` scope plus the concrete reverse-outage query
intersection. No additional UI filtering, render/cache defenses or public-route
restrictions on administrators are part of this correction.
[The visibility brief](visibility-design.md) is authoritative. The previous
15-path React visibility candidate is superseded; implementer1 completed its
restoration to `1c8478bceb3943645ec06ccde895ee4b0985873f`, pushed and clean per
the lead-confirmed peer receipt. Retain its ref/equivalence evidence.
Implementer0 solely owns API/legacy/KB. Focused quick checks precede affected
committed-source review; the full multi-file API suites follow review.
API/KB checks and affected review remain required before
the authorized same-session preview update. Both UIs receive read-only acceptance
against the server policy, preserving existing administrator access and behavior.
Retracted exposure is confirmed; anonymous draft exposure was not reproduced.
No product question remains open, and no production/default merge is authorized.

## Expanded scope: authoritative delta brief

This section supersedes conflicting restrictions in the original brief below.
The user explicitly requested published CVE-link/node-membership corrections,
editable publication time, retract/delete, and matching `vpsadmin-webui` changes
where appropriate. The lead accepted the lifecycle and compatibility decisions
below. Existing committed heads inspected: vpsAdmin
`d80ac520c66a9d4a318df517a06f13ac717f2399`, client
`9140e4bf4d286865b016f2549d0b883ccbb624e1`, KB contract
`0a12d7d97703ce5e6405130bf9325f28ddcf4bee`. No production action is authorized.

### Settled API behavior

Use the existing parent/CVE/node resource and model owners. Original edits,
CVE create/update/delete and node create/update/delete work for draft, published
and retracted advisories. Add `retracted` to expected-state choices. Each action
requires the existing parent `expected_content_revision`, accepts optional
`expected_state`, locks/reloads the parent before checking both, rereads scoped
children under that lock, and increments the revision once on successful mutation.
No CVE can move between advisory parents. Keep existing normalized CVE format,
uniqueness and node scope validation. Published/retracted node create/update
require resolved states and mitigation timestamps as previously designed.
Removal may leave missing node rows or zero CVEs: do not run whole-advisory
publication validation on corrections or introduce a new minimum constraint.

Original PUT accepts and intentionally changes/clears `published_at` in every
editable state, following its nullable model type. Preserve exact seconds on UI
round trips and preserve null rather than pre-filling the current time. Clearing
it leaves the public value blank/dash; current list ordering falls back to
`created_at` via existing COALESCE logic. No automatic publish/state reset occurs.
Other identity/authorship fields, state and existing update history remain
unchanged by corrections. Only explicit lifecycle actions change state/delete.

Every published/retracted node create/update/delete rebuilds affected VPS/user
projections under the parent lock in the same transaction, including localized
notes, row deletion, derived membership/counts and the revision. Draft behavior
remains unchanged. Failure rolls all of it back. Parent/CVE edits do not rebuild.
The existing locked manual rebuild remains. No schema or new correction endpoint.

Add ordinary admin-only lifecycle actions to `SecurityAdvisory` resource:

| Action | Interface and result |
| --- | --- |
| Retract | `POST /security_advisories/:id/retract`, scope `security_advisory#retract`, ordinary advisory wrapper/output |
| Delete | `DELETE /security_advisories/:id`, scope `security_advisory#delete`, ordinary advisory wrapper/input and `ok!` result |

Both require expected revision and accept expected state under the parent lock.
Retraction permits published only; it sets `state=retracted`, stamps
`retracted_at` once and increments content revision once. It preserves publication
time/authorship, every report/update row and projections, with no mail/update
post. A stale retry conflicts; a fresh already-retracted request is an invalid
transition. Corrections to the retracted report remain allowed. There is no
implicit restoration or automatic reannouncement.

Deletion permits any existing state, uses transactional `destroy!` and existing
dependent associations, and returns 404 if repeated after success. It permanently
removes the advisory, original/update translations, update posts, CVE links, node
rows/notes, affected projections and outage links. It does not delete referenced
users, nodes, VPSes, environments, locations, outages, transaction concerns or
mail/log history. No soft-delete framework, tombstone or new cascade migration.
Recovery of deleted content needs an existing backup; software rollback cannot
restore it. This is an implementation capability, not permission to delete live
data. Existing scoped tokens gain no new retract/delete scope automatically.

Publication now checks `draft` under its existing lock before doing anything;
published/retracted requests fail without resetting a cleared publication time.
Successful draft publish retains its existing unchanged-content-revision contract
and publication recovery behavior. The separate advisory-update resource retains
its existing explicit state/publication-time fields and optional mail choice;
do not silently remove its supported announcement behavior.

### Deletion races and ownership

There are no advisory SQL FKs in the inspected schema. The model already owns
all core dependent deletions; `plugins/outage_reports/api/models/outage_security_advisory.rb`
adds `SecurityAdvisory.has_many :outage_security_advisories, dependent: :delete_all`.
Use these existing associations, including both plugin modes, instead of manual
hard-coded child-table cleanup.

Parent locking must also cover `SecurityAdvisory#create_update!`,
`SecurityAdvisoryUpdate#update_translations!` and the separate update Delete
action, and outage-link Create in
`plugins/outage_reports/api/resources/outage_security_advisory.rb`.
Reload the parent under lock, and reload the update child under the parent lock
before writing its translations. These narrow supporting changes prevent an
already-loaded object from creating children after parent/child deletion.
Preserve announcement mail defaults, choices and rollback behavior. Missing
parents/children fail conventionally. Serialize correction/delete/update creation
without a generic lifecycle framework or modifying unrelated resources.

### Ready implementation packages

**A delta, implementer0:** existing model/resource/spec/docs/locale ownership,
plus `api/lib/vpsadmin/api/resources/security_advisory_cve.rb`,
`api/models/security_advisory_update.rb`, its resource's Delete path and the
outage-link Create owner above. Extend existing advisory model/API/concurrency
specs and `api/spec/api/plugins/outage_reports/security_advisory_spec.rb`.
Own broadened corrections, lifecycle actions, parent-lock serialization and
updated behavior/compatibility docs. Inspect existing route/default Delete
conventions; do not add an HTTP variant. A can start now.

**B delta, implementer1:** same two legacy PHP advisory files, existing browser
scenario/helper and only necessary fixtures/locale outputs. Restore publication
time/CVE editing in published/retracted forms; allow an explicit empty CVE set
when editing while retaining existing draft-creation requirements. Pass rendered
state/revision to every parent/CVE/node mutation. Add explicit node add/remove
controls using existing CRUD; omission from a partial POST must not implicitly
delete rows, and a removed row must not be silently re-created on the next save.
Node removal must work even when the node is no longer eligible for a new row.
Keep per-request atomicity and stop sequential saving on the first conflict.
Use POST+CSRF confirmation forms for lifecycle actions, with expected state and
revision; delete confirmation describes loss of advisory/updates/node assessments.
Retract appears for published only; delete for all states; success redirects to
detail or list as appropriate. No mail toggle on these silent actions. B can
start against A's settled interface; browser acceptance depends on A.

**C delta, implementer1:** same reconciler/spec/README/permissions files. Before
the first applying-sync write, require expected-state capability on all SIX
mutation types the sync actually uses: parent Update, CVE Create/Delete and node
Create/Update/Delete. Every such request sends `expected_state: draft` alongside
its revision; API CVE Update also accepts the guard although sync does not use it.
Keep the existing root OPTIONS validation, refuse missing/malformed capability
on any action with zero writes, and preserve read-only/dry-run operation. Never
downgrade after a refusal. Existing draft/digest/source/evaluation protections
and checkpoints remain. No client retract/delete/correction command or new token
scope is needed. C can start against A's agreed metadata. Implementer1 sequences
B/C; implementer0 serializes all Git/index operations in the vpsAdmin worktree.

**E ready for lead assignment:** the separate React `vpsadmin-webui` package is
specified below. It depends on A's settled API, has independent repository/file
ownership, and does not block A/B/C. No app redesign or client migration.

### Delta acceptance, compatibility and delivery

Use the previously specified Nix quick checks, adding touched CVE/update/plugin
Ruby files. Required focused API/model/concurrency checks now prove all new
mutations in published/retracted states, intentional null timestamp/zero CVEs,
authorization, missing/stale revision, wrong state, invalid node rollback and
projection refresh on membership add/remove. Verify new action metadata/scopes,
DELETE JSON body parsing, repeated retract/delete behavior, blocked republish,
preserved explicit update announcement state/time/mail behavior and draft
publication readback. Browser coverage includes CVE empty/nonempty correction,
node add/remove, timestamp edit/clear and confirmed retract/delete.

Deletion tests assert the complete owned cascade and preservation of referenced
objects/logs in full and core modes, rollback on a dependent failure, and races
against correction, update creation/translation and outage-link creation. Reuse
bounded concurrency barriers; no sleep-only assertions. C tests publication
racing each newly enabled CVE/node membership write and refusal of missing
capability for each of the six actions before any mutation, with unchanged
baseline on failed writes and retained publication recovery coverage.

No migration or state conversion is planned. Updated sync requires the expanded
API metadata; the earlier two-action-only API is insufficient and must fail
closed. Earlier client `9140e4b` remains unsafe for membership writes against the
expanded API, so update all sync consumers before resuming writes and avoid mixed
API pools. Nullable time and empty CVE/node sets already fit persisted types;
older publication validation may reject them if deliberately returned to draft.
Correction does not return an advisory to draft. Retraction uses the existing
state enum; deletion is irreversible without backup. No deployment is authorized.

After all expanded deliverables and quick checks, consolidate superseded
unmerged restrictions/tests/docs and repeated KB pin commits into coherent final
history. Preserve earlier heads as evidence, never rewrite remote defaults.
Refresh D to the final pushed vpsAdmin head, then run new mandatory whole-branch
review before longer verification. The paused earlier review does not certify
this expanded result. No open correctness decision blocks A/B/C.

## Package E: React advisory management

### Base, ownership and scope

Fresh canonical SSH fetch and remote HEAD inspection selected `main` at
`f2765d3fd778927f4cda3563f66615bfcf72b7cf`. The lead registered
`worktrees/2026-11-01-published-advisory-corrections/vpsadmin-webui` on
`dev/published-advisory-corrections` from that exact revision. E belongs to one
retained implementer assigned by the lead after its A/B/C workload boundary;
no concurrent Git work in this repository. Architect inspection made no app edits.

Open canonical PR file inventories checked on 2026-11-01 contain no advisory
implementation overlap. PR74 changes shared HaveAPI transport; other open PRs
overlap common requirements/workflow/work-log docs. Preserve their changes,
recheck before publishing, and keep E in the existing advisory adapters. Do not
import another feature branch or access another session's checkout. The repo
requires a focused PR against canonical `main`, naming REQ-055 and preserving
REQ-054's public/admin access boundary. PR approval is not merge/deploy approval.

The application owns handwritten TypeScript adapters using `haveapi-client`
0.32.0, not a generated advisory SDK. No client generation, dependency upgrade,
BFF, router, infrastructure or database change is needed. The current adapters
omit content guards, CVE reconciliation uses parallel writes, and the header
couples edit eligibility with publication. These are concrete compatibility
changes within the existing management flow.

### Interfaces and behavior

- Add typed `content_revision` and advisory mutation preconditions. Parent PUT,
  CVE CRUD, node CRUD, retract and delete send the captured revision and state;
  namespace DELETE bodies conventionally (`security_advisory`,
  `security_advisory_cve`, `node_status`). Publish sends its required captured
  revision and existing publication/mail payload; it remains draft-only and
  does not increment the revision. Do not add unsupported state input to publish.
- Before an affected workflow's first write, fetch authenticated root OPTIONS
  through existing `haveApiCall({ method: 'OPTIONS', path: '/' })` against the
  configured versioned API base, following C's resource/action graph. Validate
  the complete selected workflow's actions, including CVE mutations following
  draft creation. Use real lifecycle endpoint OPTIONS when the parent exists;
  do not invent child IDs such as `/0` for action discovery. Keep the helper
  advisory-specific and leave shared transport unchanged.
  In the unwrapped root description, parent actions are under
  `resources.security_advisory.actions`, CVE actions under
  `resources.security_advisory_cve.actions`, and node actions under
  `resources.security_advisory.resources.node_status.actions`. Guarded actions
  require `input.parameters.expected_content_revision.type == 'Integer'` and
  `expected_state.type == 'String'`, with `expected_state.validators.include.values`
  an array of strings containing the captured state. Parent Create has no
  revision precondition; Publish has revision but no expected-state parameter.
  Missing/malformed/denied capabilities or invalid revision disable affected
  writes with an upgrade/unavailable explanation. Never retry without guards.
  Root metadata with an authenticated user is authorization-filtered, but pinned
  HaveAPI 0.32.0 only runs endpoint `prepare` for endpoint OPTIONS. Root metadata
  therefore proves contract capability, not authority over a specific record.
  Preserve admin route guards and every mutation's server authorization/locking.
  Fetch once per attempted workflow, or scope any local cache to API/auth identity;
  do not reuse anonymous bootstrap/discovery metadata or fall back to it after an
  auth failure. Public reading, admin inspection and the separate announcement
  flow remain available. A mixed API pool is unsupported.
- Capture state/revision with the data shown when opening an edit, confirmation
  or bulk operation. Obtain a coherent parent/children snapshot (read parent,
  children, then verify unchanged parent revision/state before enabling the form)
  where the operation reconciles children. Do not fetch a fresh revision at save
  and apply old form values to it. Background invalidation must not reset input,
  close a failed editor, or silently rebase a stale edit onto newer content.
- Serialize parent/CVE saving and bulk node writes. Start at the captured
  revision; advance exactly once after each acknowledged successful correction,
  using returned revision where supplied or the API's established +1 contract
  for child responses. Never adopt an arbitrary newer read-back revision.
  Stop on conflict, refusal or uncertain outcome. Preserve additions-before-CVE-
  deletions, unchanged row IDs, and the existing explicit partial-success UI.
  A parent+children save is not one transaction. Show completed work and retain
  unsaved values; stale/uncertain bulk work needs explicit reload/review before
  continuation, not blind retry. Draft create must pass the returned draft
  revision/state into CVE reconciliation and must not create a duplicate parent
  after a child failure.
- Enable original name/localized text/CVEs/publication-time editing in all three
  states. Empty CVEs are valid on edit; draft creation retains its existing
  required-CVE rule. Separate `canEdit` from `canPublish` and `canPostUpdate`:
  publish only draft; existing update posting stays published-only with its
  explicit mail/state/time behavior. Original corrections have no mail choice.
- Preserve seconds and null in publication/mitigation timestamps. Use an opt-in
  precision helper or advisory-local conversion and `step=1`; do not change all
  unrelated datetime controls. A no-change round trip must retain the exact
  persisted value; explicit blank sends null, with no current-time fallback for
  correction. Publication readiness checks apply to publishing, not correction.
- Extend existing node row edit/add/remove and bulk controls; published/retracted
  create/update offers resolved states with required mitigation timestamps.
  Existing rows for nodes outside the active inventory remain visible/removable;
  use included node identity or an ID fallback. Removal is explicit and does not
  silently re-create rows on later ordinary saves. Missing rows stay missing
  unless an explicit add/bulk operation includes them. Node notes use actual
  localized `LANG_note` fields (current generic `note` input is not an API field),
  preserving other languages when editing one. Reuse loaded languages and the
  existing localized form patterns.
- Add direct retract and advisory delete adapters and confirmation dialogs.
  Retract is published-only, silent, and preserves the report and history;
  deletion is available in every state and clearly describes permanent loss of
  the advisory, updates and assessments. Use captured guards, prevent duplicate
  submission, retain errors, and navigate to the list only after acknowledged
  delete success. Do not report an uncertain response as successful deletion or
  retry automatically. Read-back 404 may reconcile an uncertain delete explicitly.
- After corrections/partial success, invalidate advisory, CVE/node, list and
  affected-user/VPS queries; include existing public advisory cache keys when
  returning to public/member views. Retract refreshes state without clearing
  projections; delete evicts the removed detail and refreshes lists/relations.
  Preserve direct admin route gates, public read access, outage linking, manual
  rebuild, and separate update edit/delete/announcement behavior.

### File boundaries and required documentation

E owns `src/lib/api/securityAdvisories.ts`, `securityAdvisoryRelations.ts`, their
focused tests, and advisory-specific helpers if needed; existing shared transport
stays unchanged. UI owners under `src/pages/app/admin/security/` are
`AdminSecurityAdvisoryDetailPage.tsx`, `AdminSecurityAdvisoriesPage.tsx`,
`securityAdvisoryAdminApi.ts`, `securityAdvisoryAdminModel.ts`,
`SecurityAdvisoryEditorModal.tsx`, `SecurityAdvisoryNodesPanel.tsx`,
`SecurityAdvisoryNodeForm.tsx`, `SecurityAdvisoryDetailHeader.tsx` and
`SecurityAdvisoryDetailDialogs.tsx`, plus focused tests and both
`src/i18n/locales/{cs,en}/admin/security_advisories.ts` catalogs. A small advisory
mutation hook/helper extraction may keep the detail page within its existing
structural limit; remove its resolved ledger exception rather than refreshing a
hash to excuse growth. Adopt changed deferred E2E files into `tsconfig.e2e.json`
and `scripts/fixtures/e2e-type-coverage.json`; do not weaken the type gate.

Update REQ-055, affected workflow/API/action contracts and evidence entries,
generated `docs/design/IMPLEMENTATION_INVENTORY.md`, and one dated
`docs/work-log/` entry with a WORK_LOG pointer. Explain per-request atomicity,
partial/uncertain outcomes, supported API upgrade ordering and rollback limits.
The API's advisory documentation remains the authoritative mutation contract.
Read local AGENTS/procedures before edits. Locked terminology was resolved with
the repository's Nix expressions and both guides read at
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; record it with E. Do not bump that
runtime/module input merely to change UI forms. The context-owning lead applies
the user-facing writing skill to final cs/en copy before commit.

### Acceptance and commands

Use the pinned `nix develop` shell and root `npm ci`; install BFF dependencies
only if a required aggregate check actually needs them. Quick verification:
`npm run docs:inventory`, `npm run ci:quick`, and focused
`npm test -- src/lib/api/securityAdvisories.test.ts src/lib/api/securityAdvisoryRelations.test.ts src/pages/app/admin/security`.
If a new test lives under a different advisory-specific name, include that file.
Verify configured author/committer identity and declared hooks before committing.

Tests must exercise real HaveAPI serialization, especially namespaced DELETE
bodies and all guards; all editable states; empty CVEs; exact/null timestamps;
localized notes; sequential revisions; draft publish race; concurrent edit/retract
conflicts; no writes without capabilities; retained input and partial outcomes;
affected-count refresh; explicit retract/delete; and unchanged announcement mail
and state/time controls. No UI-only fixture claims backend atomicity or cascade.
Package A owns that real API evidence.

After committed-deliverable independent review, required longer checks are
`npm test`, `npm run build`, and focused browser runs using the repository wrapper:

```sh
npm run e2e -- e2e/specs/app/security_advisories_admin.spec.ts e2e/specs/app/security_advisory_update_mutations.spec.ts --project=chromium
npm run e2e -- e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts e2e/specs/admin/security_advisory_outages_mobile_actions.spec.ts --project=mobile-chrome
nix build .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents
```

Add new correction/lifecycle cases to the selected browser files; include desktop
and mobile cs/en confirmation/error interactions. The current mobile-WebKit
testMatch excludes these advisory files, so do not claim a zero-test WebKit run
as coverage. Capture implemented desktop/mobile UI using synthetic fixtures for
progress and final PR handoff. Use an own free local server port, no production
credentials or live scenario commands. Long/uncertain commands use the mandated
watcher workflow. Inspect normal feature/PR CI without expanding into a release
campaign; any required gate failure is investigated and recorded.

### Compatibility, KB and recovery

Deploy A's complete API before enabling E's writes, with C already upgraded before
resuming sync. New E remains readable against older APIs but affected writes fail
closed; old E does not satisfy the current revision protocol and is not a safe
admin-write rollback target. UI rollback leaves persisted corrections intact;
re-enable writes only with a compatible UI/API pair. No new persisted browser
format, schema, daemon/OS coordination or generated-client dependency is introduced.
Cleared timestamps, removed CVEs/nodes and retraction are intentional persisted
state; deletion needs backup restoration, not a software rollback.

Canonical KB inspection at `0a12d7d9` found no advisory semantic/page/capture
bindings and no `vpsadmin-webui` input in the contract inventory. E therefore has
no contract pin or KB page/capture to fabricate. Its repository screenshots are
UI review evidence, not KB publication. D still refreshes all five existing
vpsAdmin pins to final A/B source and runs the mandatory full strict `bin/check`;
do not substitute targeted checks or start unrelated content/capture work.

No open E product decision or cross-API change blocks assignment. No application
edits, builds, production writes, deployment or integration were performed by
the architect; implementation and verification remain with assigned owners.

## Original brief (superseded where the expanded delta differs)

Status: implementation brief. architect0 owns this design; the lead accepted
the decisions below in the same-session assignments on 2026-11-01. No application
edits, production requests, deployments or commits were performed by the architect.

## Scope and source evidence

Allow administrators to correct an original published advisory's name, localized
summary/description/response, and existing structured node rows (state, mitigation
times and localized notes) through the existing PUT actions. Corrections never
send mail, publish again, reset state, create another advisory or append an update.
The separate `security_advisory_updates` announcement interface remains unchanged.

Fresh SSH fetch of canonical `repos/vpsadmin.git` selected `origin/master` at
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`. This contains the advisory feature.
The supplied reference `ff730be468e366ee346dc6d02dc0fe57c3f8677c` is its ancestor,
23 commits behind; canonical local `master` was stale and was not selected.

The necessary companion change belongs in `security-advisories`. Fresh SSH fetch
and `ls-remote --symref origin HEAD` identify its actual default as
`2026-07-13-security-advisory-automation` at
`7b6c71807e3c5a41f585fd1d9563e151ada71244`; there is no `origin/master`.
Use a new session-owned branch from that exact default. Comparison against public
feature `33f253a9dd8242ed23271399339db023068b86db` shows no changes to APIClient,
`update_advisory`, `reconcile_node_statuses`, revision checks or draft guards.
That feature adds status-history handling around `sync`, `ready`, `evaluate` and
`publish`; retain it when applying this narrow companion patch later. Do not import
its unrelated history into this initiative. Comparison used only canonical Git
objects, not another session's files or checkout.

Read guidance: workspace AGENTS and required projects/sessions/git/lifecycle/
documentation/verification/knowledge-base/commits procedures, documentation and
handoff skills, vpsAdmin AGENTS and development/localization/testing procedures,
docs index, advisory owners and specs; security-advisories AGENTS, README and
API permissions; canonical KB-contract AGENTS and WebUI workflow. vpsAdmin has
no existing advisory behavior page, so add one concise page and index entry.

## Interface contract

The existing parent `PUT /security_advisories/:id` and nested
`PUT /security_advisories/:id/node_statuses/:row_id` retain their scopes, payload
wrappers, response shape and required `expected_content_revision` integer.
Add optional `expected_state`, with `draft` and `published` choices, to these two
PUT actions only. Omission leaves deliberate ordinary corrections possible;
supplied state is a precondition, never a state assignment. Check it under the
same parent lock as the revision. State/revision conflicts return HTTP 409 without
any changes. Do not add an endpoint, schema migration, mail option or API version.

| Operation | Draft | Published | Retracted |
| --- | --- | --- | --- |
| Original name and localized text PUT | Existing behavior | Allowed, silent | Rejected |
| Existing node-row PUT | Existing behavior | Allowed, silent, atomic projection refresh | Rejected |
| CVE create/update/delete | Existing behavior | Still rejected | Still rejected |
| Node-row create/delete | Existing behavior | Still rejected | Still rejected |
| Separate advisory-update resource | Unchanged | Unchanged | Unchanged |

`published_at` remains editable for drafts. On a published original, omission
preserves it; an exactly equal normalized timestamp is accepted as a no-op;
a different value, including null when currently non-null, rejects the entire
request. Compare typed time values, not textual timezone representations.
Use conventional record/input validation errors for this field. Preserve
`id`, `external_id`, state, `created_by`, `published_by`, `created_at`,
`published_at`, `retracted_at`, CVE associations and every existing update row.
Only the intended content, `updated_at`, and one content-revision increment change.

Published node corrections must leave the edited row `not_affected` or
`mitigated`; the existing model still requires both mitigation times for
`mitigated`. Keep draft `unknown`/`vulnerable` support. Do not run global
`validate_publishable!` on corrections: a newly added unrelated active node must
not block correction of an older advisory. Preserve existing active-node scope
validation; permitting edits to retired nodes or changing publication validation
is outside this package. Omitted localized fields are preserved, and explicit
blank/null notes retain their current clear semantics.

## Atomicity, projections and concurrency

Keep the existing draft mutation helper's contract for its other callers. Add a
small content-edit path in the same model/resource owners, sharing revision logic
where useful; do not globally loosen `mutate_draft!` and thereby enable CVE/node
membership changes. All correction steps run in the parent row's `with_lock`
transaction:

1. Reload/lock the parent and check allowed state, optional expected state and
   expected revision before writing anything.
2. For parent PUT, validate publication-time immutability and apply original
   attributes/translations. For node PUT, reread the scoped child under the lock
   before applying attributes/notes and validating the resulting row.
3. After a published node PUT, run the existing affected-VPS/user rebuild before
   committing. Parent text edits and draft node edits do not start a rebuild.
4. Increment parent `content_revision` once only after every step succeeds.

Any row/translation/projection failure rolls back all preceding changes,
including deletions and the revision. Do not catch and suppress errors inside the
transaction. Reuse the existing rebuild meaning: current active/suspended VPSes
on mitigated nodes, with current owner/environment/location/node and corrected
mitigation times. `not_affected` removes those VPS rows; affected users and their
VPS counts are derived again; transitions back to mitigated add them. Node count
continues to count mitigated rows. This is a current snapshot, not reconstructed
historical VPS placement. Never implement a second projection algorithm.

The public manual `rebuild_affected!` path must take the same parent lock, since
an unlocked rebuild could otherwise overwrite a committed correction with old
rows. Prefer making the model entry point lock so publish/manual/correction calls
share the serialization. Avoid stale loaded associations; use fresh scoped reads
under that lock. Inspect locking reads where an existing outer transaction can
retain a repeatable-read snapshot, and verify actual concurrent behavior rather
than substituting a mocked lock. Production uses READ-COMMITTED; the test helper
uses REPEATABLE-READ with snapshot isolation off. Do not change database defaults.

Two edits using the same revision must have exactly one winner. A subsequent
fresh-revision correction must use current child/projection data. A manual
rebuild waiting on a correction must finish with its corrected projections.
Use bounded barriers/timeouts and independently committed fixtures for meaningful
concurrency coverage, following existing model concurrency specs.

## Draft-sync race and required client protection

`publish!` currently leaves `content_revision` unchanged, and the companion
client's publication readback/recovery requires that contract. Preserve it.
Once PUT accepts published rows, a request prepared while draft could otherwise
cross publication with the same revision and mutate the published original.
This is why the optional expected-state precondition is necessary.

The WebUI submits the state rendered with each edit form, alongside its rendered
revision. It must retain submitted state/revision when rerendering an error,
rather than silently rebasing a stale form onto fresh values. The draft-sync
client sends `expected_state: draft` on both parent and existing-node PUTs.
Existing draft-only node/CVE create/delete paths need no new parameter.

Before `sync --apply` performs its first write, verify advertised support for
`expected_state` on both PUT actions via ordinary OPTIONS metadata. Root schema
discovery can cover the new-advisory case without creating a row just to probe
capability. Keep the check local to applying sync; read-only commands and dry-run
planning should remain usable on older APIs. Missing/malformed capability or an
OPTIONS refusal stops applying sync before any create/update/delete; no fallback
to an unguarded PUT, server-version guessing or retry after removing the parameter.
Check all required capabilities before the first write, not after parent content
has already changed. Existing revision/digest/draft/committed-source/evaluation
checks and post-write checkpoints remain intact. A state conflict stops the run
and propagates; do not rewrite the committed baseline to conceal it.

Add client tests simulating publication between preflight and parent PUT, and
between preflight and node PUT. The simulated corrected API must reject the
draft precondition without changing published values, sending mail or updating
the client's recovery baseline. Also test missing capability on either action,
malformed metadata, no writes on refusal, guarded successful sync, and preserved
publication/recovery behavior with the same content revision.

## WebUI behavior

Keep the existing Edit advisory and Node statuses actions and their CSRF/admin
checks. On a published original, show publication time and CVEs as read-only
values; omit `published_at` and skip CVE parse/reconciliation on submission.
The current form sends the timestamp rounded to minutes, so leaving it in the
payload would either reject otherwise valid corrections or corrupt original time.
Use existing labels and rendering helpers; no new announcement workflow.

For published node forms, edit existing eligible rows only. Do not automatically
POST a new row because an active node was added after publication; filter the
display/save set consistently. Draft forms keep their existing create behavior.
Preserve full seconds when round-tripping existing node timestamps so saving a
note does not truncate mitigation times on every submitted row. Preserve blank
values and language-specific notes. The existing form makes sequential per-row
requests: each request is atomic and revision-checked, while an error in a later
row does not undo already successful rows. Keep and document that boundary; a
batch endpoint or new transaction protocol is not required.

Extend the existing advisory browser scenario for published text and node edits,
unchanged publication time/CVEs, no automatic update, read-only publication
fields, stale form state/revision refusal, and affected-user display after node
correction. Reuse current fixtures/helpers where possible; avoid touching shared
unrelated browser infrastructure. API specs establish the mail/history guarantee.

## Implementation packages and ownership

The lead assigns these complete packages after accepting this brief. Two
implementers can work on distinct files in the vpsAdmin worktree; implementer0
owns serialized Git/index/hook operations. Nobody stages another owner's unfinished
files. The companion repository has its own session-owned worktree and branch.

### A: vpsAdmin API, model, focused tests and behavior docs — implementer0

Files: `api/models/security_advisory.rb`,
`api/lib/vpsadmin/api/resources/security_advisory.rb`, existing
`api/spec/models/security_advisory_spec.rb` and
`api/spec/api/resources/security_advisory_spec.rb`; a focused model concurrency
spec if needed. Add `docs/security-advisories.md` and its `docs/README.md` link.
API locales generated/normalized for changed metadata/errors belong to this
package. Change node model only if needed for the narrow state validation.

Own locked corrections, expected-state contract, published timestamp protection,
atomic rebuild serialization, rollback and authorization coverage. Document
silent original edits versus explicit announcements, field/state restrictions,
revision/state preconditions, projection meaning and per-request atomicity.
No changes to migrations, `security_advisory_update.rb`, notification templates,
or CVE mutation behavior are planned. This package has no implementation dependency.

### B: WebUI and browser regressions — implementer1

Files: `webui/forms/security_advisory.forms.php`,
`webui/pages/page_security_advisory.php`,
`tests/playwright/webui/specs/security-advisories.spec.cjs`, its existing
`lib/pages/security-advisory.cjs` helper if needed, and only necessary advisory
fixture changes in `tests/suite/webui.nix`. WebUI locale artifacts belong here
only if source wording actually changes. No API/model/spec/docs overlap with A.

Own the UI behavior above. It may be implemented in parallel against the settled
PUT contract; executing browser acceptance depends on A. Route new required API
behavior through the lead instead of independently editing A's files.

### C: security-advisories guarded sync and compatibility docs — implementer1

Files: `lib/security_advisories/reconciler.rb`, `spec/reconciler_spec.rb`,
`README.md`, `docs/api-permissions.md`; modify APIClient only if its existing
OPTIONS helper proves insufficient (it currently supports OPTIONS). Keep scope
descriptions accurate; this change adds no token scope or correction command.

Implement after B, or independently before B at the lead's choice. Contract
depends on A's agreed parameter/metadata, not its unfinished code. Use focused
fake-API tests to prove guarded writes and pre-write fail-closed behavior. Preserve
feature-line status-history logic when later consuming this patch; it is not
needed in our default-based narrow deliverable.

### D: pin the final WebUI revision and run the KB contract — implementer1

Lead disposition: this is a required verification package under the canonical
WebUI procedure. The targeted checker is diagnostic only and does not replace
the pinned full check. Assign after B/C, when the final vpsAdmin feature commit
is committed and pushed. D has independent repository files but depends on that
exact immutable revision; a later vpsAdmin change requires updating the pin and
repeating affected verification.

Fresh SSH fetch and `ls-remote --symref origin HEAD` on 2026-11-01 confirmed
`git@github.com:vpsfreecz/vpsfree-kb-contracts.git`, default `master`, at
`ce2c8cd9358c3636e5d39343e595df813a0b197f`. The architect read its complete
`AGENTS.md` at this head, along with the canonical
`docs/webui-change-workflow.md`, relevant README setup and `flake.nix`.
The lead registers a new session-owned worktree/feature branch from this base;
the implementer reads those repository instructions in full before editing.
Also follow workspace Git, verification, commits and configuration-input
procedures. Refresh upstream before branch publication and report any moved base.
The architect creates no worktree and changes no pins.

Only these five files belong to D:

| File | Exact value to update |
| --- | --- |
| `flake.nix` | `inputs.vpsadmin.url` to `github:vpsfreecz/vpsadmin/<final-40-character-SHA>` |
| `flake.lock` | Regenerate the selected `vpsadmin` input with Nix |
| `captures.json` | Top-level `vpsadmin_commit` |
| `contract/navigation.yml` | Top-level `vpsadmin_revision` |
| `contract/pages.yml` | `revisions.vpsadmin` |

All four source pins currently contain
`939159f27b5d627930281d5fac0c0aa9ba53bfc7`. Change them to the same pushed final
vpsAdmin SHA; do not use a branch name. Preserve the explicit
`inputs.vpsadmin.inputs.vpsadminos.url` override and `revisions.vpsadminos` at
`6bdf458fd9105379860234ff33d352e55844f08f`, and preserve unrelated root input pins.
Inspect the generated lock diff: any transitive change must follow from the
selected vpsAdmin input; do not refresh all inputs or hand-edit lock metadata.
Do not change screenshot provenance to pretend existing images were recaptured.

From the new contract worktree, after updating the four source pin values:

```sh
nix flake update vpsadmin
git diff --check
git diff --stat
git diff -- flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml
```

Verify those files agree on the full SHA, inspect/install any declared hook
framework (none is declared in the inspected root/package.json), and commit the
focused pin update under the workspace commit procedure. Keep its complete
base-to-head diff/history in the initiative's final review packet; the lead
applies mandatory-review mechanical-content rules without inventing an extra
substantive review gate. Do not bypass hooks. The full check uses the pinned shell
and its default pinned `VPSADMIN_KB_VPSADMIN_SOURCE`, not an environment override
to a mutable checkout:

```sh
nix develop -c bin/check
```

Have a fresh verification watcher launch/monitor this uncertain-duration check
under `dev-session-monitor`; do not start a cluster, run captures or perform
production/staging operations. Use the strict command above, without
`--allow-missing`. Preserve exact contract and vpsAdmin heads, command, exit status
and log path. A successful targeted checker or permissive CI check is not a
substitute. Stop unexpected kernel builds under the verification procedure.

Acceptance: all five pin locations are coherent, the final diff is pin-only,
the full contract check succeeds, and the final source still has zero advisory
controls/page/capture bindings. No page text, PNG, fingerprint, semantic ID or
capture record is fabricated to make the result pass. Publish the feature branch
and inspect its CI; integration into `master` still requires explicit direction.

If the full check fails, preserve its first actionable failure. Distinguish an
environment error, final-feature drift and existing baseline drift using a
same-session clean snapshot of the recorded contract base and, when relevant,
the pre-correction vpsAdmin base. Reuse the standard checker; do not repair
unrelated fingerprints, missing media or stale capture provenance automatically.
Report the exact failing command/path, base/final comparison and smallest needed
follow-up to the lead. A baseline failure is a recorded verification limitation,
not a passed check. No baseline-drift investigation is needed before a failure
provides concrete evidence.

## Acceptance and verification

Quick checks per owned repository/component: `git diff --check`, Ruby/PHP/JS
syntax as relevant, component RuboCop/formatting and installed Overcommit hooks.
Use the repository's Nix shells, whose component shell hooks change directory.
Suggested commands from the vpsAdmin root:

```sh
nix develop .#api -c bundle exec rubocop models/security_advisory.rb lib/vpsadmin/api/resources/security_advisory.rb spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
nix develop .#webui -c php -l forms/security_advisory.forms.php
nix develop .#webui -c php -l pages/page_security_advisory.php
nix develop .#webui -c node --check ../tests/playwright/webui/specs/security-advisories.spec.cjs
```

Include a new concurrency file in lint/spec commands if created. Existing
foundation patterns cover model specs; platform-operations patterns cover the
existing resource spec. Do not add arbitrary CI topic changes. Honor generated
locale hooks. Lead applies required user-facing writing guidance before commits.

After intended changes are committed and quick checks pass, mandatory independent
review covers complete branch histories and migration provenance (no new
migrations). Longer/uncertain test runs use the mandatory fresh verification
watcher; do not launch them inline. Target these bounded checks, then stop when
they resolve the identified risks:

```sh
VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
./test-runner.sh test 'webui#security-advisories'
```

Companion repository: `nix develop -c bundle exec rubocop --parallel --force-exclusion`
and `nix develop -c bundle exec rspec spec/reconciler_spec.rb`, followed by its
ordinary complete suite when appropriate. Its Nix shell installs the locked
bundle. Keep successful exact-head evidence; investigate failures before retries.
Inspect branch CI after publication without merging. Stop unexpected local
kernel builds under the workspace verification procedure.

Required assertions across these checks:

- Authorized published parent/name/localized corrections and node/note/time
  corrections succeed; original publication identity, CVEs and update history
  survive; no mail chain, advisory creation or publish call occurs.
- Missing/stale revision, wrong expected state, unauthorized writes, changed
  publication time, unresolved published node state and invalid mitigated times
  reject with no partial text/note/projection/revision mutation.
- Node transitions add/remove/update VPS projections, user membership/counts and
  advisory affected filters/counts, preserving ordinary user visibility isolation.
- Inject a rebuild failure after some writes and prove rollback of rows, notes,
  projection inserts/deletes, parent revision and update timestamp.
- Concurrent same-revision writes have one winner; rebuild/correction ordering
  cannot restore stale projections; publish racing a guarded draft PUT is refused.
- Draft edits/publication, draft CVE/node membership management and explicit
  announcement mail behavior remain compatible; retracted corrections stay denied.

## KB impact, documentation and client scope

Canonical owner is `vpsfree-kb-contracts`, not the historical
`vpsadmin-kb-captures` spelling in vpsAdmin's localization procedure. At inspected
contract head `ce2c8cd9358c3636e5d39343e595df813a0b197f`, searches of navigation,
managed pages, captures, scenarios and tests find no advisory controls, page
bindings or screenshot concepts. The two advisory PHP files contain no semantic
documentation IDs. The intended visual changes concern administrator forms only;
no shared renderer or member navigation changes are planned.

Package D implements the mandatory final-revision pin and full
`nix develop -c bin/check` workflow in a dedicated contract branch. The existing
`tools/check-contract.rb --vpsadmin-source <exact-checkout>` may additionally
compare base/final source when diagnosing a reported failure, but cannot replace
D. Record exact source revisions and zero advisory bindings. Do not invent
advisory captures or fetch/stage/publish KB content when no page is affected.
If final scope touches a bound shared control, revisit the impact decision and
follow its reported page/capture requirements. No KB production write is authorized.

No generated Go/Rust/TypeScript SDK, Terraform or general CLI change is required:
existing update routes and resource fields remain, with an optional precondition.
The draft-sync companion change is required because it relied on the previous
server state restriction; do not treat that protection as optional documentation.

## Compatibility, deployment and recovery

There are no new persisted formats, schema migrations, seeds, daemon protocols,
Nix module options or vpsAdminOS changes. Old software can read corrected rows and
projections. API and WebUI rollout should complete together before claiming the
UI usable. Old WebUI against the new API can reject timestamp-bearing edits
safely; new guarded UI against old API may reject the unknown precondition.

Updated draft-sync requires the new API capability to apply writes and stops
before any write on older servers. Update every active draft-sync consumer before
resuming it against the upgraded API. A stale client against the new API can
still make an unguarded PUT; the optional parameter cannot enforce client intent
retroactively. Pause sync during API/client rollout and do not use a mixed API
pool as a stable capability guarantee. Read-only client operations remain usable.
Keep publication's unchanged-revision readback/recovery contract.

Software rollback needs no data conversion; already corrected content/projections
remain. Rolling API back restores the old inability to edit published originals;
the updated sync client refuses to apply until the required capability returns.
Restoring incorrect content would be a separately reviewed correction, never a
database reset, republish or automatic reverse update. No production corrections,
credential operations, deployment, default integration or session lifecycle
cleanup are authorized here. Future deployment requires its own approval and
coordination procedure. Session remains open.

No unresolved product/correctness decision blocks A, B or C. D waits for the final
pushed vpsAdmin revision. The lead owns later operational/integration approvals.
