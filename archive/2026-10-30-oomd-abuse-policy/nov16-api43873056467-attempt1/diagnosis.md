# Exact final-head API failure — reviewed fixture correction validated and published

## Source impact and current boundary

Published failure input remains immutable 15ed330232aeeaff70738f546b317870abf54011/tree30b11fa9010cc72508a4ef3ad39fccd820eb62fc.
Reviewed candidate is cb8c214dba62731c93dafb102072444bcc77cc4e/treed9234850e0ccbefc20e3b205af359e10ae2c3d03, clean, with a two-file test-only
correction: api/spec/support/app_helper.rb and the new existing-pattern route
spec api/spec/api/routes/transactional_fixture_connection_spec.rb (128 additions).
No production API, authorization, HaveAPI cleanup, migrations, schema, dependency,
flake/package, workflow or exported contract bytes changed. Owner3 received exact canonical publication proof after root's conditional
source-stability release; downstream ownership and admission remain with root. No product defect is inferred.

The shared helper changes test connection ownership. Reviewer0 (retained Sol/xhigh)
completed affected general/architecture/scope review7b55b20d with no findings;
root accepted source clearance. Its explicit whole-series conclusion retains
cb8 as an independent fifth test-support purpose for the inherited fixture defect.
No fold/rewrite is required. The sole admitted original-context validation then
passed as recorded below. Root accepted the bounded upstream assessment and
exactcb8 was published by ordinary fast-forward with canonical SSH readback.
No CI dispatch, physical run, export, client generation, pin update, deployment,
cleanup or lifecycle action occurred in this package.
Main plan/state remains root-owned.

## Retained original CI and isolated replay

Run43873056467/attempt1/workflow234996228 failed on exact15ed. Core platform-operations
job133318936635, step9 Run RSpec, executed243examples/2failures/0pending under
seed36653. SecurityAdvisory cases [1:3:1]/source453 and [1:3:2]/source487 failed:
published Show expected200 became404; anonymous/retracted CVE parent filter
returned validationfalse instead of successful empty rows. The sources/specs
were byte-unchanged since537b, which alone establishes no cause/disposition.
All25other matrix jobs passed. Aggregate133332872164 had full13/core13 manifests,
424mapped/424eligible in each, with sole error core matrix failure. No coverage
partition defect was reported. Same-topic full243/0 used seed44838; mode and
order differ. Original failed outcome and raw logs/ZIPs/results stay unchanged.
Native-evidence.json binds retained provider bytes/digests and exact lock.

CI: Ruby3.4.12/Bundler2.6.9/RSpecCore3.13.7/Expectations3.13.6/Support3.13.8,
AR+AS8.1.4.1/HaveAPI0.32.2, MariaDB11.8.6 REPEATABLE-READ with
innodb_snapshot_isolation0. Recovered CI core lock SHA256 is
1b68dc1814fd0ccec7396e0e0f6930cbebbc24df00a48f295397d049c44ee631.
The private API bundle uses that frozen lock; the ordinary local API lock was
not overwritten. Local Ruby3.4.9/MariaDB11.4 remain explicit differences.
Ordinary .#vpsadmin setup separately bootstraps root Bundler4.1.0/root gems;
commands are not described as globally no-reinstall. The private leaf uses
Bundler2.6.9 and the installed100-gem CI API bundle.

Operationa7ad9f52/native69291 ran original453/487 once in isolation: PASS0,
2examples/0failures/0pending/0outsideerrors,464.10334296s (individual177.933733673s
and270.71806405s). JSON86032ea0 and environmentd0fa1178 remain unchanged. This is
focused non-reproduction, not cause proof. All six original input hashes remain.
Private trace calls original GET/scope once without additional SQL and records
only bounded role/path/status/fixture-state/error-field diagnostics.

## Ordered39 reproduces the first symptom

Operationbde1bd1f/native30386 terminated1. The same40 selected native IDs are the
38passing same-file predecessors plus the2original failures, retaining seed36653
and native relative order. Actual39IDs exactly match the expected prefix:
first38pass, [1:3:1]/453 fails at465 on published advisory42 Show200->404.
[1:3:2]/487 did NOT execute because fail-fast stopped. Duration760.368293829s,
failing example17.616991403s. Native JSON7dfcec93/orderproofca8bf088/log2969cb0b
and all eight frozen inputs remain unchanged. Cross-file81predecessors were
unnecessary to reproduce this first symptom locally. No automatic retry occurred.

Trace: anonymous Index included published42; draft41 Show404 and draft Indexempty
were correct; subsequent published42 Show404 contradicted uncommitted fixture
memory states41draft/42published/43retracted. This does not establish which exact
predecessor returned which connection. The retained concurrent-parent deletion
case [1:10:3]/1688 uses another thread/pool.with_connection; it is a source-backed
candidate for a spare connection, not a proven chronological culprit.

## Proved mechanism and deterministic HTTP controls

HaveAPI0.32.2 server.rb:547 calls the real connection handler's
clear_active_connections! after each request. AR8.1.4.1 connection_handler.rb:162
calls pool.release_connection and disables query caching. release_connection
returns the lease to the pool without rolling back the outer RSpec fixture
transaction. The normal spec_helper around hook runs examples inside an AR
transaction; :no_transaction deliberately bypasses that fixture wrapper.
An available second connection can therefore read without the fixture's
uncommitted rows. Production cleanup is valid; the test fixture owns the lease.

The private real-DB3-control check (native3053) passed3/0/0 in16.097930146s,
JSON90e753395cf8248048897e3728c1d330a8f4d91e3485eccd7f72556894211a55.
Same-connection uncommitted reads succeed; a deterministic real second-connection
handoff makes the actual published visible_to.find raise RecordNotFound and the
actual CVE parent parameter.clean raise HaveAPI::ValidationError; committed rows
remain valid with hidden-parent empty visibility. This proves sufficiency for
both observed failure mechanisms, not exact historical connection chronology.

The first HTTP baseline had3examples/1failure (hidden-parent), with published
and committed controls passing. Its vpath helper performed an additional OPTIONS
request between the intended handoff and GET. Preserve http-baseline.log/.json/
.exit and http-baseline-spec.rb: RSpec1 is distinct from owned outer shell66374
ending127 later in /etc/bash_logout. The completed corrected baseline99189 used
one computed path per transactional example:3examples/2failures/0pending,
40.979690345s, nativeRSpec/shell1. Both actual HTTP symptoms reproduced: published
Show404 and parent filter resource-not-found validation. Committed cleanup passed.
http-original.log/.json/.exit and http-original-spec.rb preserve those bytes.

The fix wraps only the pool's release_connection during the example. It returns
false only for the captured example fixture connection, on its owning thread,
while that transaction remains open. All other calls delegate to the original
method with unchanged arguments. No connection pinning, cross-thread sharing,
SQL, getter replay, authorization change or global request-cleanup suppression is
introduced. The real handler still performs query-cache cleanup and other-pool
cleanup. :no_transaction skips this retention entirely. The inline helper comment
is the durable explanation of the fixture ownership invariant.

Final fixture-regressions.json:4examples/0failures/0pending/0outsideerrors,
31.932756848s, owned native25095 and exitfile0. Controls cover published Show
visibility across a second available connection; hidden-parent successful empty
response/count; committed :no_transaction requests releasing connections and a
real explicit second-connection handoff; and another thread's independent open
transaction being released while the fixture thread retains its own lease.
The two failing transactional regression bodies match the corrected original
baseline; describing ApiAppHelper and strengthening the separate committed
handoff/worker control do not replace those original assertions.

An intermediate corrected4-case run85333 passed both HTTP regressions and
committed cleanup but failed a new control that incorrectly expected in_use?
to be literalfalse (AR returns owner/nil). Preserve http-corrected.json/log/exit;
final control checks owner.nil? directly. Initial scoped lint also rejected a
string describe; final describe uses ApiAppHelper. No product change or weakened
HTTP assertion accommodated either preparation error.
Final Ruby syntax, two-file RuboCop and normal trusted pre-commit/commit-msg hooks
pass. Commit-msg emitted two >72-character body warnings, both within required
80-character limit. Exact new spec belongs to foundation once in each plugin
matrix via existing routes glob; workflow/topic bytes are unchanged.

Deterministic mechanism coverage is distinct from original-case validation:
original487 remains unexecuted in ordered39. Both original full-role cases
subsequently passed on this successor in the sole original40-context run below.
The complete auth/visibility assertions in the original spec remain byte-identical.
Original failed CI is still FAILED.

## History, compatibility, documentation and next boundary

Narrow review delta:15ed..cb8c214, two files/128 additions, in fixture-lease.diff.
Full537b..candidate diff and complete series are retained alongside it. Existing
four logical purposes remain untouched. Reviewer0 and root accepted the retained
fifth independent test-support purpose: it corrects an inherited test fixture
defect across API consumers. This supersedes the earlier proposed API-purpose
fold, preserved in originalfbd76b52/diagnosis.md. No history rewrite is needed;
all consumed/reviewed/tested input identities remain exact.

```text
3af143d96ee4ca0244afc5a86573c30b36768871 api: evaluate incident escalation through site policy
129679b42ea1156918536f675b2507bada42d2c8 api: localize ordinary oomd incident reports
098ce5c642a4a1bd215ba2e87530bd576b804433 webui: show incident history and unknown runtime limits
15ed330232aeeaff70738f546b317870abf54011 docs: explain isolated MariaDB locking settings
cb8c214dba62731c93dafb102072444bcc77cc4e api: preserve transactional fixture connection leases
```

Refs/review preservation: nov16-api43873056467-before->15ed and
nov16-api43873056467-fixture-lease->cb8c214dba62731c93dafb102072444bcc77cc4e, beneath
refs/review/2026-10-30-oomd-abuse-policy/. All older historical/diagnostic refs
are retained. Migration20261030180000 remains byte-identical
f1e6bc75aeffb14d2d14676a908fc4332d7f42f79ee29fe54f48def8e2756c7a;
additive20261115120000 remains
b9d894772f61c65dd40952db0eacc04783cbc940144377f1a783d34b2a4a441c.
Unknown historical production consumption still justifies preserving original
migration lineage. No new migration/release/deployment consumption is asserted.
All non-test bytes equal15ed, including schema, product/API sources, flake/package
and dependency locks. No SDK/generated contract change follows from this delta;
no export/client work was initiated. This is source-byte scope, not a new Nix
runtime derivation proof. Existing exact15ed SMTP04902f8a/ff1a51f2 remains its
accepted full physical pass. Earlier SMTP failures, quota non-reproduction with
unknown historical cause, and receipts5882/4070/98ac/21814 remain unchanged.

Documentation routing: fixture ownership->test developers->inline app_helper
comment (durable rationale); individual CI/replay/fix evidence->lead/reviewer->
this diagnosis and fixture-lease-receipt.json. Product reference docs were checked
for scope; no product behavior changed, so no new product prose is useful.

## Accepted original40-context validation

Sole operationb723de0e-8696-4771-a58d-4de156e3a6b2/native5115 terminated0,
with reporting/artifact cells complete per root's terminal handoff. The unchanged
lease-context-command.sh executed once against exactcb8/treed923. All10frozen
input hashes remain equal. Bundle-check, RSpec, order-check and wrapper exitfiles
are0. Native JSON96ad7941a582c37febd113e3df624c40f5c3f62234728df61a64faabb91909b3
records40examples/0failures/0pending/0outsideerrors, seed36653,
duration1276.042092849s. Actual40IDs equal the expected ordered-native-ids.json
exactly, including all38retained predecessors and both original targets.
Orderproofe1c42d07ec44c1cc2d6bd1a90928b564a9c6d350dbb6a0358aa72dde405a4a7b
and native loga5a92cf365a3e082cf59d1c1c87e215c9b9fc8f8a1dd0f370e0edf5e0a8b7443
are retained unchanged in this directory.

The actual native JSON explicitly records original [1:3:1]/source453 PASSED in
160.768078436s and [1:3:2]/source487 PASSED in249.443453092s. This supplements the
monitor's conservative per-target sentence; the original monitor report is not
rewritten. Root accepts the reviewed correction and this original40-context
validation. It is a faithful local validation of both failures with prior-history
context, rather than a reclassification of the original failed CI attempt.
Environmentd0fa1178 remains identical to the earlier private CI bundle. The
recorded local Ruby3.4.9/MariaDB11.4 versus CI3.4.12/11.8.6 limitations remain.
No claim is made that the exact historical predecessor was isolated, that the
complete topic was rerun, or that the original15ed CI changed outcome.

Historical fbd76b52 receipt and all34bound artifacts were verified before this
live reconciliation. Original diagnosis and receipt bytes are retained at
originalfbd76b52/diagnosis.md and originalfbd76b52/fixture-lease-receipt.json;
all other bound artifacts remain at their original paths and unchanged. This
snapshot keeps the original receipt's historical document identity usable.
The new final receipt will bind this reconciled version without a circular hash.

## Original canonical publication refusal — retained evidence

The released exactcb8 fast-forward publication guard stopped before fetch/push:
canonical SSH git ls-remote --symref returned refs/heads/master and symbolicHEAD
25b0717975802293bd24ecc2056385575d5fe29d, while the expected default was
537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02. Remote feature
refs/heads/2026-10-30-oomd-abuse-policy remains expected15ed330232aeeaff70738f546b317870abf54011.
The successful transport response is preserved as publication-remote-before.stdout/
.stderr/.exit. Owned preflight session29564 terminated1 at the expected-default
assertion; no fetch, push, ref/source/history rewrite or hook invocation occurred.
Root and Owner3 received the exact mismatch. Local cb8/treed923 remains clean
and frozen. Root subsequently dispositioned this baseline dependency through the bounded
assessment below and authorized exactcb8 without rebase. This initial refusal
remains immutable evidence, not a source/test failure. No publication or new CI
inventory is attributed to the original refused preflight.

## Bounded upstream compatibility assessment

Root released only the exact canonical default/feature fetch and source analysis.
Native52993 completed0, fetching default25b0717975802293bd24ecc2056385575d5fe29d
and expected feature15ed without further remote drift. Preserved refs beneath
refs/review/2026-10-30-oomd-abuse-policy/nov16-upstream-assessment/ bind base537b,
published15ed and candidatecb8. Local worktree/index/head remains clean/frozen.
No push, rebase or default modification followed.

The complete537b..newdefault series is one commit25b07179, a bot-generated
packages update. Its six paths (lock+gemset for API/client/download-mounter) have
9additions/9deletions; all change connection_pool3.0.2 to3.0.3 plus gem source
hashes. No feature537b..cb8 path overlaps. Graph: merge-base537b, default-only1/
feature-only5; neither final head is ancestor of the other. upstream-series.txt,
upstream-diffstat.txt, upstream-name-status.txt, upstream-six-file.diff and
upstream-assessment.json preserve exact graph/path/input evidence.

Compared537b to25b Git objects are identical for API source/migrations/schema/
fixtures, tests, workflows, exporter, flake, Ruby series, NixOS modules, WebUI and
the three package constructors. The constructors' bundlerEnv gemdir consumes the
changed lock+gemset pairs, so a rebase would materially change those packaged
dependency inputs despite no handwritten-source overlap. It cannot inherit old
Nix runtime proof solely from conflict-free application. The separate gem
connection_pool is not AR's unchanged ConnectionAdapters::ConnectionPool class;
no upstream fix for the observed fixture lease mechanism is claimed.

The b723 original40 run uses frozen private CIlock1b68/connection_pool3.0.2.
The isolated exporter lock also remains3.0.2. API Specs CI resolves its API bundle
fromapi/Gemfile rather than packages/api/Gemfile.lock; both API Gemfile and
workflow are unchanged, but a future job's normal resolution can still change
its effective lock. Keep actual future environment evidence separate. Existing
15edSMTP proof is not certification of a rebased3.0.3 package graph.

Root ACCEPTED assessment76f27c97 and exactcb8 feature publication without
rebase, adopting observed25b as the remote default guard. This retains exact reviewed/tested source and does not modify/integrate
newdefault. No source/check/review refresh is needed for unchangedcb8 publication;
normal fresh SSH/push/readback/comparison and bounded workflow inventory remain.
The feature is not ready to fast-forward integrate25b: later explicit integration
preparation must rebase/refresh then reassess the packaged-input delta. If root
instead selects rebase now, preserve ranges, verify patch/migration equivalence
and reassess new runtime graph before reusing Nix proof; no new test/build is
launched by this assessment. Accepted exactcb8 publication and directOwner3
canonical proof are recorded below.

## Final exactcb8 publication continuation94f19d6b

Only the expected-default guard changed for the resumed operation; expected
feature15ed and candidatecb8 remained exact. New publication94-* outputs preserve
the original refusal and upstream files. Native81373 fresh canonicalSSH/fetch
confirmed default25b/feature15ed. Ordinary trusted Nix environment and installed
executable Overcommit pre-push entry point were used without bypass variables,
force flags, rebase or source change. Native29660 normal push exited0,
fast-forwarding feature15ed->cb8. Independent canonical SSH readback86431 exited0
at2026-11-16T16:48:20Z and confirmed:

- refs/heads/2026-10-30-oomd-abuse-policy = cb8c214dba62731c93dafb102072444bcc77cc4e;
- refs/heads/master and symbolicHEAD =25b0717975802293bd24ecc2056385575d5fe29d,
  unchanged by publication;
- local exactcb8/treed9234850e0ccbefc20e3b205af359e10ae2c3d03 remained clean.

publication94-canonical-proof.json SHA256
047dc55c80452b8ee8691aad2fa27ee495f45d2c0596d6a38ccd49dac16766a2 binds raw SSH/
push receipts. DirectOwner3 handoff19df8c35 supplied this proof promptly after
verified publication. Root's conditional source-hold requirement is satisfied;
Owner3 owns any downstream work under root admission. No backend pin/SDK/export
or new physical validation was inferred or launched.

The comparison capture completed0 with explicit historical reviewed
base537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02/headcb8. Its baseLabel is Captured
comparison, with currentdefault divergence explicitly retained here and in the
final receipt. This is not a claim thatcb8 descends from25b or is integration-ready.
Five accepted purposes remain exactly committed; no fold/rewrite or reference
deletion occurred. All older reviewed/consumed/diagnostic refs remain preserved.

A single bounded exact-head inventory returned4/4 actual attempt1 automatic runs:

| Workflow | Workflow ID | Run ID | Status at inventory |
| --- | --- | --- | --- |
| API Specs |234996228|43911462363|queued|
| CI |228803702|43911462168|queued|
| i18n health |307073542|43911462191|in_progress|
| RuboCop |229534945|43911462468|completed/success|

Required same-branch queued2/2 and in_progress2/2 scans were complete first-page
count matches. Sole superseded active candidate was prior15ed CI43873056258/
attempt1. A fresh targeted metadata read proved samebranch/oldhead/in_progress;
ordinary cancellation POST returnedHTTP202/CLI0, native80246 terminal0. This
records acceptance of the cancellation request, not terminal remoteCI or hosted
effects/cleanup proof. Existing rootobserver144fe883 retains authoritative oldrun
terminal ownership. No currenthead/otherbranch/completed run was cancelled.
No observer, dispatch, rerun or additional provider observation was started.
publication94-workflow-inventory.json and its raw metadata/cancel files preserve
complete identities/statuses and bounded scan evidence.

Final exactsource verification reuses the passing4focused cases, normalhooks,
independent affected review and b723actual40pass only for their proven identical
inputs. All original failedCI/a7/ordered39/SMTP/quota outcomes remain separate.
The old immutable fbd receipt and its original diagnosis are retained under
originalfbd76b52; the initial refusal's bound doc/receipt are retained under
original4aa59a40. The new publication receipt binds this final live diagnosis,
all raw publication/check evidence and source equality without a circular hash.

All owned local commands/handles are terminal. Source remains frozen; root owns
CI observation, main records and later integration/capacity decisions. No new
source/test/build/physical/export/pin/default integration/deployment/cleanup or
session lifecycle action is pending or inferred from this bounded completion.
Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
