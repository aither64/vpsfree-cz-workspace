# Nov18 reusable policies and presentation: final committed-source review

Status: released for final independent source review under assignment
`a7858cdc-e94f-4043-aabc-2eaa0b221433`. All intended substantive project changes are committed,
quick checks have passed, and root verified the eight clean final heads. Reviewer0
retains Sol/xhigh/read_only. Historical reviews remain evidence for their original
inputs; they do not replace this review. This gate precedes longer integration
checks and does not establish merge or deployment readiness. KB's final mechanical
pins/pinned verification and canonical media remain explicit later dependencies.

Session: `2026-10-30-oomd-abuse-policy` in
`/home/aither/workspace/ai/vpsfree.cz`. Project worktrees are beneath
`worktrees/2026-10-30-oomd-abuse-policy/`; this directory holds session evidence.
The [current plan](plan.md), [design](design.md) and [phase checklist](state.md)
record scope and remaining dependencies.
The user's request and later corrections define scope. Internal designs and
owning packets describe implementation decisions and cannot expand that scope.
The [fresh source inventory](nov18-final-source-inventory.json) lists every full
base-to-head commit series and diffstat at release. Owning packets link complete
binary diffs, previous ranges, preservation refs and original failure evidence.

## Requested outcome

The user rejected backend enrollment limited to node oomd reports: policies
must work with ordinary incident creation and configuration-owned selectors.
Several policies can match one report, with saved membership, independent
counts/limits and one ordinary source email. Matching runs at creation, not on
reads, later configuration changes or retries. The existing authorization,
owner epochs, action eligibility and one physical-stop safeguards remain.

Emails and both UIs must identify period, incident count, limit and action for
each shown policy. Saved report facts remain distinct from current settings.
Report details show authorized matched policies and safe policy/history links,
including retained historical keys. Separate Incident reports and Incident
policies navigation preserves the original reports destination. Czech wording
must be natural and avoid accidental repetition in adjacent sentences.

The older HTML styling stays in separate commits. Its requested 26 Mailpit
previews are delivered in [the existing preview index](nov18-older-mail-previews/index.md).
Those synthetic previews establish visual samples, not product delivery.

No new policy editor, action framework, per-row API fetching, historical
reclassification, dependency/runtime version change or new screenshot scenario
is requested. Default integration, registry release, refreshed demo/reset,
production KB and session lifecycle remain outside this source review.

## Review selection and conclusions

Overall risk is high: persisted membership/actions and schema lineage, tenant
history, node RPC authority, stop execution, public API/SDK contracts and paired
backend/configuration/CLI deployment. Use retained independent reviewer0 with
its saved Sol/xhigh/read_only settings after checking the live same-session
roster. Read mandatory-change-review and all four lane references: general,
architecture/repetition, scope/proportionality and risk/compatibility. The
reviewer performs the assessment directly without nested reviewers.

Inspect the full base-to-head series and final diffs, repository instructions,
actual consumers and relevant quick evidence. Return concrete findings and
explicit conclusions on whole-branch history, repeated update streams,
migration lineage, documentation placement/preservation and compatibility.
State no migrations for each applicable repository. Source acceptance below
does not prescribe the review conclusion. Long integration checks follow
resolution of findings; direct narrow fixes use focused verification.

## Frozen source ranges

| Repository | Recorded review base | Final head | Final tree / owning evidence |
| --- | --- | --- | --- |
| vpsadmin | `537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02` | `de4df3d63f4d4afb0c27e8b9be2785c15d24811c` | `5c0a69fdb65828faaaf7c770d0d099390ccd1c49`; [core/history packet](nov18-reusable-policies/packet.md) |
| vpsfree-cz-configuration | `15e3b9af90276e41d19e6a33477add58e5f9a8c9` | `2a06abc21b23e9e500bfdb6d657854c545511d21` | `0b8586bc2bafeb976763b6a32596858a65699b6a`; same owning packet |
| vpsfree-notification-templates | `2cfd218d9152888feea4109f064459078ea9f76e` | `1ba7169bf64c61cff8802af33279260c0f81bfc8` | `1ef951adf31f8f0be18972c567c9995426d868c9`; [template history](nov18-template-history/packet.md) |
| vpsadmin-typescript-client | `2da950a98fa13468b36d03b13fb5e81cca206e0e` | `2d251bb0e10f5379a19df3a07eb7a0b0f19e3c88` | `a7e5c7b6153c8353568f56a1a634ff6be0d26af3`; packed source `44c651b2a57e8de553dd51236c2dccbc09946fac`; [artifact proof](nov18-reusable-sdk-sync/ts-artifact-verification.json) |
| vpsfree-kb-contracts | `ce2c8cd9358c3636e5d39343e595df813a0b197f` | `9e0f6c062a982ab034289c0da9d8de322944e27c` | `af76acc022e825b19f28ef7b3904bbcc51655fc7`; [KB source packet](nov18-kb-source/packet.md), de4 local override/final public pin pending |
| vpsadmin-go-client | `af9a819ca35f6de5556092679b4df7cb72e7aa89` | `5934903568862a95b688479f0b13e11e4a36692f` | `4b335f644bc2a414c6c5c98b41d148e4088f34ba`; [SDK history](nov18-reusable-sdk-sync/final-history.json), [accepted SDK package](nov18-reusable-sdk-sync/packet.md) |
| vpsadmin-rust-client | `823a4f8450fce4947310fc81bcdebdca91d9ffae` | `15db0ffd95ccd34247de9f839c906d860afb1b69` | `359eeee99e9d88167567b716db7d38fa2928d0eb`; [SDK history](nov18-reusable-sdk-sync/final-history.json), [accepted SDK package](nov18-reusable-sdk-sync/packet.md) |
| vpsadmin-webui | `88ac13b89d6421c914cd57e18153de1fee6fc7b7` | `6b14ae5e1702ee8c137605d3512c123c9a24b582` | `727af56aede9132a1e9a77c5726330f31ed61044`; [React final packet](react-report-links-nov18/final-review-packet.md) |

Root independently verified all three client heads, trees, clean tracked source,
complete series and thirteen preserved refs, plus25 client inputs,54 bound check
artifacts and all17 packet bindings. SDK acceptance is recorded in
[root proof](nov18-reusable-sdk-sync/root-acceptance-proof.json). Root also verified
React's94 artifacts,33 committed blobs,31 checked inputs, three-purpose history,
full/Nov18/fold binary diffs and seven-path prose fidelity in
[React acceptance](react-report-links-nov18/root-final-acceptance.json).
Historical3cb7/b1fb/4be identities remain distinct from their successors.
The unchanged HaveAPI generator and separately registered historical API
advisory diagnostic retain their established scope and recovery evidence; this
packet allocates no work to them.

## History and migration evidence

Backend has four purposes: fixture63bd0c8a, API/incident-mail665e46e0,
PHP/browserd56baa8c and separate password-HTMLde4df3d6. The complete98-path
final diff and3226 tracked files equal accepted568. Configuration folds its
source stream into one two-path purpose; all445 files equal accepted0ca.
Root verified their complete base binary diffs and clean registered sources,
all71 history-receipt artifacts and100/12 recorded refs. Full series,
range-diffs, normal-hook logs and preserved old refs are in the owning packet.

The original feature migration remains20261030180000 immediately after
20261006120000, SHA256
`2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e`.
The obsolete20261115120000 is absent throughout the reconstructed series.
User-confirmed no external consumers permitted the earlier consolidation and
one disposable demo reset, which is already consumed. Preserve the literal
historical deployed source/schema evidence and supported recovery limits in
[the prior owning packet](nov17-generic-policies/g1/packet.md). A same-tree
successor is not literally the deployed commit or proof of a new deployment.
The separate H binary patch remains SHA256
`d8c013f06470f706233c926ae57974759d5c0573125607c00930fcac7da97e52`.
The user's no-external-consumer decision excludes upgrading disposable old
feature schemas. The one reset was consumed on2026-11-18 at06:41:58Z; the accepted
demo later ran backend011/Reactb1fb with the recorded original migration and
loaded configuration/template inputs. See the reset boundary and accepted runtime
record linked in state.md. That history neither deploys de4/6b14 nor authorizes a
second reset. No feature-migration default merge or production release is claimed;
review its literal deployment/consumer lineage and exact predecessor separately.


Template history has three purposes:32 incident paths atbce597e7, writing
guidance at502932ba and24 older HTML paths at1ba7169b. All400 entries and the
full base diff equal accepted898. Its old refs and separate H purpose remain.
KB retains the three already-merged d3af/f977/cb782 commits and independent
runtime91d exactly. Only unmerged4be plus the new source edits became9e0f6c06;
all262 entries and full base/unmerged source diffs equal checkedb915d65c.
Root verified56 receipt artifacts, all262 working blobs and four preservation
refs. The historical merged pin boundary stays separate; the pending final pin
must be consolidated into this unmerged purpose before publication/readiness.
React consolidates six working commits into three purposes on88ac: SDK input,
provenance and cache429d84cb; application/tests/contractsff61f4b1; dated evidence
and historical captures6b14ae5e. The complete79-path diff is+3810/-62; the Nov18
b1fb delta has33 paths,+967/-158. Both full patches and the final tree equal the
retained raw six-commit head a9bf9f7f. All33 owned blobs and31 check inputs match;
prior b1fb/raw-six refs remain. Eight feature screenshots and115 total PNGs retain
their historical bytes and source labels; they are not successor visual proof.
React has no migrations. Its repeated SDK input updates are one final stream.

SDKs consolidate the reusable-policy generation stream into one final generated
commit per client, followed by wire tests and reference documentation. TS also
retains a separate archive delivery commit because React consumes that immutable
HTTPS artifact. Go and Rust each have two purposes; TS has three. Their earlier
selected input revisions remain in preservation refs, with full old/new series,
binary diffs and range-diffs in the SDK package. No SDK migration exists. React's input stream is consolidated as described above.

Configuration's unrelated-ref aggregate changed during composition; its
initial snapshot retained only a hash. Available reflogs cannot reconstruct
full attribution. Own source/feature/preservation refs and normal hooks are
independently proven. This explicit metadata limit is separate from source
correctness. No unrelated refs were undone or attributed to an actor.

## Verification and compatibility boundaries

- Core: affected40 examples, concurrency/older-transaction/parser4, RPC7,
  offline actual nodectl control, locale health and scoped lint passed.
  Preserve each exact batch scope; overlapping totals are not unique coverage.
  The nodectl control used the working declared libnodectld bundle because the
  standard nodectl Gemfile references a missing helper; it is not a packaged
  CLI runtime pass. See the owning packet for original failures and corrections.
- Mail:35 builtin planned IDs covered by22 retained plus13 disjoint passes;
  site24 passed. All830 inputs stayed equal, with827 Git blobs and3 retained
  dependency inputs distinguished.42 builder renders and8 static visuals are
  accepted for layout. [Mail packet](nov18-incident-mail-tables/packet.md).
- PHP:17 tests/122 assertions, gettext,8 actual synthetic renders and browser
  syntax passed. [PHP packet](nov18-php-policy-presentation/packet.md).
  Live API/browser execution remains pending for this source.
- TS required generation/build/type/consumer/test/package checks and retained
  archive consumer passed, including18 tests. Initial incorrect test nullability
  assertions remain recorded; only corrected/unrun checks were continued.
  Root-final SDK reference paragraphs are in the committed TS source and returned
  Go/Rust writing windows. The actual archive SHA983061ec/345048bytes binds final
  raw7cb28e/provenancea9e536. Owner2 independently verified HTTPS, installed it through npm and verified all1382 archive files.
- Go passed10 native tests and4 projection checks. Rust focused7, provenance7,
  refusal10, formatting and regeneration passed. The default all-targets matrix
  passed9 tests with1 real-server case ignored; blocking passed9 with2 ignored.
  The first wrapper stopped after default tests because its PATH omitted Git;
  the corrected continuation19349 ran only unexecuted steps. Documentation and
  package exits are0. Owner3 found its nominal1.95 Cargo invocation selected
  rustc1.98 through PATH; that output is not MSRV evidence. The corrected minimum
  matrix ran as19071 after19349 joined0. Root inspected Cargo's retained
  effective-compiler-at-start receipt: release1.95.0/commit59807616e, with exact
  minimum-only script SHAa09e9b4b. Both minimum profiles now pass9 tests each,
  with1/2 live fixtures ignored. Root read both effective1.95 compiler receipts
  SHA db00ce4c and async/blocking/final exit markers0. Native19071/19349 are joined0 and the final
  SDK effects receipt has no active or uncertain handles. Root accepted the
  completed SDK package; normal matrix passes were not repeated.
- React application typechecking against the actual new SDK passed. The original
  nine-file test run passed86 and failed two link assertions. A minimal JSDOM
  control reproduced a selector lookup failure for a present link. The stronger
  complete five-destination assertion passed all9 tests in the affected file.
  A later narrow type attempt stopped because its temporary tsconfig omitted
  existing ambient declarations; the complete application type pass remains
  valid. Corrected narrow typing and E2E typing passed. Lint then rejected four
  arbitrary percentage-width classes; owner2 substituted existing w-1/4 tokens
  and focused lint passed. The nine remaining commands now all pass: formatting,
  i18n/structure/component/UI-string/mutation audits, production asset build and
  npm dependency prefetch. Root verified all nine command/log hashes and prefetch
  `sha256-R22CY+X8p6ZSXIq9shb+Plz4JNOCFiaMa5H3pqTUtWE=`. Native45924 is reported
  joined. Final inventory passed with268 routes/75 modules, docs audit passed
  with289 docs/76 requirements, and final formatting/hash metadata checks passed.
  The eight unchanged test files plus corrected9/9 cover88 focused tests without
  claiming a full unit rerun. Three-purpose source/history is committed and
  accepted. All handles are terminal. Six prose paths remain root-exact; the
  seventh has only the authorized factual verification update. Product strings
  are unchanged. Browser and exact clean-head Nix-package verification remain
  pending, including the six optional WASI-cache warnings. Historical captures
  and package/CI/demo results do not prove this successor.
- KB source checks passed against the frozen de4 override:47 controls/38 paths,
  contract8 runs/50 assertions,98 annotation bindings/9 exceptions, annotation
  tests10/22 and pure selector9 cases. Exact retained Ruby3.4.9/minitest5.26.1
  was used;16 check inputs stayed unchanged. The five public pins retain5aa1. Following independent source review and backend
  feature publication, the coherent five-file pin and pinned source check are
  an explicit mechanical/verification dependency. The published old pin must
  not be described as compatible with new fixture/source changes.

The API owns membership/counts/privacy/actions; PHP, React, the three generated
SDKs, site declarations/templates and KB fixture are concrete consumers. The
new node RPC path validates node/VPS authority and stable token/fact retries.
Backend support precedes new nodectl; old direct SQL creation is unsupported
for this creation-time contract and must be held or retired at activation.
Paired backend/site config must load before new events; there is no hot reload.
Notice fields come from consistent saved linkage, retaining authorized old-owner
admin history. All error evaluations remain admin-only, even if matched=true.
Their saved membership can still count. Unknown legacy membership is not false.

Preserve current settings-first locking and current membership/action reads
inside mutation transactions, including callers with an older snapshot.
Rollback and retry must remain atomic. Explicit Stop/Suspend reports retain
membership/counts with policy decision none, leaving the explicit action to its
normal chain. Rollback requires a compatible backend/configuration/client set
and reconciliation of uncertain effects; no demo reset is implied.

## Documentation and remaining delivery

| Topic | Reader / class | Authoritative home | Evidence / limit |
| --- | --- | --- | --- |
| Policy creation, counts, actions, RPC and compatibility | Developers/operators; reference | vpsadmin docs/incident-escalation.md | Final core source/specs and normal hooks |
| API export and generated clients | Contributors; how-to | vpsadmin docs/api-schema-export.md | Final raw/provenance and accepted SDK packet |
| Site selectors and paired operation | Operators; reference | Configuration configs/vpsadmin/api/README.md | Exact declaration/parser proof; no activation |
| Mail layout and writing rules | Template maintainers; reference | Site AGENTS.md and actual template bodies | Final builder/layout evidence |
| Member report/policy navigation and history | Members; how-to | nov18-kb-source/incidents-{cs,en}-candidate.txt | Root final wording/paired annotations returned; source contracts passed against de4 override; final pin pending |
| React and SDK contract guidance | Consumers/contributors; reference | Existing owning handbook/SDK docs | Accepted SDK and React source/check packets; runtime/package gates remain |
| Individual checks, rollout and recovery evidence | Session owners; execution record | Linked session packets and state | Old identities and failures retained literally |

The new unmanaged article candidates have hashes CS
`e48c89df8f68f55d2cc939ca4d5a5a4cb2d4500f5b2eef593c3f78c9935337ce` and EN
`d3ac846e724f3865e0d2f30f656eb218d4edeaf43184b633c137f9261075ff3e`.
Original owner3 candidates remain byte-identical at their historical paths.
Both new candidates retain the original prefix and unrelated incident sections,
with exactly one reports and one policies navigation annotation. They are local
unmanaged page candidates, not production/staging writes or uncommitted project
source. Include their factual and manual UI-instruction/binding review.

KB still owes assessment of getting-started/vps-details, getting-started/vps-list
and restore-backups/playground-vps-list in Czech and English. Existing1150px
geometry stays literal. Synthetic views and source checks do not certify the
canonical media. Runtime/capacity, affected captures, strict inventory and
wiki staging/production remain separate parked work.

After review, only affected existing alerts/incident-escalation and
webui#incident-escalation integrations plus scoped React browser/package gates
are planned. Historical011 CI/demo does not prove these latest changes.
Registry publication remains an eventual React integration prerequisite. Owners
retain concrete review fixes: implementer1 core/configuration, implementer4 PHP,
implementer0 mail/templates/KB source, implementer3 SDKs and implementer2 React.
Architect0 remains the design clarification owner. Review findings return to
root for reconciliation and scoped owner assignment. No source writer is active.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
