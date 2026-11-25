# Nov24 administrator incidents: combined final review

All intended source changes are committed; allocated quick checks pass. Root
verified eight clean final worktrees and React's final diff bindings. This is the
final committed-deliverable review, before the remaining browser acceptance work.
Feature publication is complete; no default merge, npm release or deployment is
approved. React PR333: https://github.com/vpsfreecz/vpsadmin-webui/pull/333.

## Assignment and scope

Session: 2026-10-30-oomd-abuse-policy. Tracking: ../plan.md, ../state.md,
../design.md TOP A/B/C/D. Worktrees:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/NAME.

Reviewer0 is the retained eligible independent reviewer, Sol/xhigh/read_only,
thread01a18d34-69d3-74d2-ae70-df2584ed8a12, roster44, full_access execution.
No authorship or unrelated review assignment is known. Preserve saved settings.
Overall risk HIGH: admin authorization/privacy, public API and generated-client
contracts, mixed-version capabilities. Apply GENERAL, ARCHITECTURE/REPETITION,
SCOPE/PROPORTIONALITY and RISK/COMPATIBILITY. Read mandatory-change-review/SKILL.md
and all four references; review directly without nested reviewers or source edits.

Start with user scope versus the implementation and diff size. User approved
administrator Incidents navigation with Overview (menu default), Reports and
History in PHP and React, then the same information in the daily report. Overview
shows all current matched VPS/policy pairs, including below-threshold and stopped
VPSes. Preserve bare Reports URLs, member/support/per-VPS behavior and existing
semantic documentation controls. Counts, reports remaining, restrictions, saved
evaluations, current action/mail outcomes and confirmed physical stops are distinct.

Non-goals: policy evaluation/reconciliation changes, writes/manual stop/retry,
new schema/migration/event log, new transport/SDK fallback, global pagination
rewrite, per-VPS fan-out, SMTP/live actions, production KB/media changes or rollout.
Do not expand supported behavior through optional hardening. Concrete defects in
the supported contract still require findings and owner fixes.

## Exact ranges, complete series and evidence

Each section lists the complete new range and its owning packet. Inspect final
Git diffs as well as the series; packets carry full binary diffs/check commands.
Targets name eventual delivery obligations, not integration authorization.
The auxiliary artifact branch also has a whole-default range d8cb..b619, consisting
of the two TS source purposes below plus its artifact commit. Do not double-count
that shared prefix. All previous bases were integrated before this extension.

### vpsadmin

Target `master`; base `4062a8da3314aa7b48170b0d6f441446bad9b207`; head `74c0af3aef3ec9124ca89ce7669ccd9b99633495`;
tree `c2e2de2d3e3a63cc14f122f0f43641cb0898e569`.
Evidence: backend/review-packet.md; php-implementation/implementation.md.

```text
73cd5d37b54c8d807752edae722c61876eedbaed webui: add admin incident overview and history
74c0af3aef3ec9124ca89ce7669ccd9b99633495 api: add admin incident policy overview and history
25 files changed, 4166 insertions(+), 618 deletions(-)
```

### vpsadmin-go-client

Target `master`; base `5934903568862a95b688479f0b13e11e4a36692f`; head `8708f170bd99522ac147fceadee9e7db6305c772`;
tree `82bcef44a48c31e7692cc4af8434ba75b39cf755`.
Evidence: ../nov24-client-sync/packet.txt.

```text
8708f170bd99522ac147fceadee9e7db6305c772 Add generated admin incident policy reads
10 files changed, 3686 insertions(+), 16 deletions(-)
```

### vpsadmin-rust-client

Target `main`; base `15db0ffd95ccd34247de9f839c906d860afb1b69`; head `2b49891cd22e08a945bff2cf4cff25b2b9903bf2`;
tree `b1430ae9a72645ad3c332674bcdca1c4b99a7de4`.
Evidence: ../nov24-client-sync/packet.txt.

```text
2b49891cd22e08a945bff2cf4cff25b2b9903bf2 Add generated admin incident policy reads
12 files changed, 2809 insertions(+), 23 deletions(-)
```

### vpsadmin-typescript-client

Target `main`; base `d8cb484748db8687554822772a98a1f873414d65`; head `aed11d01c0d1436293f45a1a4e83d88421375bc1`;
tree `2b1fa2c5093d3c6cdbe36b71e499f2bb6f67831f`.
Evidence: ../nov24-client-sync/packet.txt.

```text
18fb40f152335d57cbb49555767f0fb2cee77f42 Add generated admin incident policy reads
aed11d01c0d1436293f45a1a4e83d88421375bc1 Prepare TypeScript 0.6.0 candidate
15 files changed, 2044 insertions(+), 177 deletions(-)
```

### vpsadmin-typescript-client-development-artifacts

Target `main`; base `aed11d01c0d1436293f45a1a4e83d88421375bc1`; head `b619eb8324bfe80c7b225f698fb83efe97639c83`;
tree `47cc9b5f663048638c6d7f267d157e77c37e217e`.
Evidence: ../nov24-client-sync/artifact-publication/packet.txt.

```text
b619eb8324bfe80c7b225f698fb83efe97639c83 Retain the admin incident SDK candidate for HTTPS consumers
2 files changed, 31 insertions(+)
```

### vpsadmin-webui

Target `main`; base `4499f90fe11df0e4df6f23e5fa54829e2254ec1b`; head `c27d70dbd4e96540de4d58027bfa6fce09a4df15`;
tree `0e96635640b98aee93e2ef208909ad081ce9ca95`.
Evidence: ../nov24-react-admin-incidents-preparation/final-review-packet.md.

```text
5c2910668e71bbbdc2687c1a156691c46567e28c deps: select generated administrator incident SDK candidate
c27d70dbd4e96540de4d58027bfa6fce09a4df15 feat: add administrator incident overview and history
44 files changed, 3131 insertions(+), 68 deletions(-)
```

### vpsfree-notification-templates

Target `master`; base `64665b3944da4ebf5045ef00f403e410ce88e3ad`; head `7af51cd6164fd5aad7633f39f6cf4e7ef64c18a7`;
tree `e1872cbc645947495160b0b6a13a56cb5b2689d4`.
Evidence: ../nov24-daily-report-html/final-packet.md.

```text
7af51cd6164fd5aad7633f39f6cf4e7ef64c18a7 daily_report: add incident policy overview and outcomes
5 files changed, 526 insertions(+)
```

### vpsfree-kb-contracts

Target `master`; base `c064b4fe87d66486c5eb8f43cb278a464d8574ab`; head `75a721e14e07ae86975089fbdbb58a686d490550`;
tree `e196f5fa12226ab9ba9b2377508b9e651a21b638`.
Evidence: ../nov24-kb-alignment/packet.md.

```text
75a721e14e07ae86975089fbdbb58a686d490550 contract: align sources with admin incident views
5 files changed, 9 insertions(+), 9 deletions(-)
```

## History, migrations and update streams

Require explicit independent conclusions on whole-branch history, obsolete
iterations, repeated updates, migration lineage and documentation placement.
No migrations are added by any new range. vpsAdmin retains consumed migration
20261030180000_add_incident_escalation.rb, SHA256
2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e.
It was already merged into4062 and consumed by the prior completed initiative
stage; do not rewrite it or conflate earlier rollout proof with these new heads.
Obsolete20261115120000 is absent. New ranges change no schema/engine/node files.
Original merged history and preservation refs remain literal.

Proposed dispositions for independent assessment: PHP and API are separate
purposes in vpsAdmin; tests/docs/locale changes support their behavior. Each client
has one final generated-source stream; TS has a separately reviewable0.6 identity/
changelog purpose. Go's actual Python3.13.18 receipt correction was amended into
its sole purpose, with old60b7 retained and generated/schema bytes unchanged.
React separates dependency/lock/hash/provenance/docs from the UI/readers/tests.
KB contains one final five-home pin/context update. Site has one bounded daily
presentation purpose. Artifact adds only the exact tgz and machine receipt,
preserving old0.4 artifacts. No interim fixes or repeated unmerged pin stream is
proposed for retention. Ordinary publication is not a reason to retain obsolete
history; identify any concrete contrary evidence.

## Contracts and consumer graph

Backend74c0 owns two new admin-only Index resources and the daily producer:
incident_policy_exposure at /incident_policy_exposures and
incident_policy_evaluation at /incident_policy_evaluations. Existing schema nodes
are structurally unchanged. Exposure uses live vps/user/node Resource references;
History raw original IDs support deleted identities. Partial references are already
batched; no per-row Show. Offset/limit25(max100), total_count/next_offset/as_of/read_at
are endpoint-local. History orders by evaluation time plus ID; direction only.

Whole-second UTC as_of fixes arithmetic/recording cutoff, not a historical image
of mutable configuration, ownership or outcomes. Projection SQL selects relevant
count/page/order facts consistently; daily uses single-statement collections in
its existing write transaction, without isolation or connection changes. Check
actual SQL, authorization and query shape. No rematching during reads.

Daily optional flat Hash has as_of/period_start/end and three collections, each
with total_count/rows/omitted_count/url, capped25. Missing payload omits new content;
present empty remains truthful. Rolling half-open24h activity and older outstanding
work differ. Native timestamps and prepared links reach ERB; no queries there.
Recipients/scheduler/template matrix stay unchanged. SMTP sent means mail-server
acceptance, not inbox delivery; confirmed physical stop/shared identity is separate.

Backend final clean export is API7/protocol2/en/fullfixture/all6plugins,
529actions/156resources/9031params. Raw schema SHA256
7e2a529787c06944f1ad0cdf3369edd8b4650d79826f3bbda9101af2dfb67628;
provenance429fd99e3dee126e2306fad1fb4c5bc6f8442a7fcb7abdab8f8fae34b121418e;
lock2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0.
One producer/export; exporter/profile/tooling unchanged. Go preserves the sole
OAuth endpoint projection. HaveAPI generator1ef9/0.32.2 and runtime pins unchanged.
Rust Option, TS nullable/partial unknown refs and Go scalar-null limits are explicit.

PHP uses actual HaveAPI client/XTemplate. React consumes real generated SDK calls
through its existing adapter with role/action/required-field/meta guards. Old APIs
show unavailable new tabs while Reports remains available. No raw transport fallback.
React manifest/lock/provenance/frontend hash select the immutable artifact:
https://raw.githubusercontent.com/vpsfreecz/vpsadmin-typescript-client/b619eb8324bfe80c7b225f698fb83efe97639c83/development-artifacts/vpsadmin-typescript-client-0.6.0.tgz
Packed sourceaed11 is distinct from supportcommitb619.348079B/SHA256
9cba02754bec157616c66207312f44312e9af36fe5deb05e8e68585615e17ca9;
integritysha512-XEZ9FeH18wsg4RzAamouPP/o7RhL1BA6C8OscVRZKfnMVVZjrTZmrtIfKql9c/achRz6g9VOzhNPH8vunHy7Hw==.
Archive packed once, checked, public readback byte-equal. React ordinary install
matches1390 archive files and locked versions; only SDK/root selection changed.
Frontend hashsha256-+BJv7MpMaZdj0J468IdrOqPAU5RQZqAowxhqgC2jaRU=.

Before React merge, select a published compatible registry SDK in final manifest,
lock/provenance/hash, with temporary development selection removed. Publication,
backend capability readiness and deployment are separate decisions. None is
implied by this review. Rollback restores matching source/inputs; no new persisted
format exists. Existing BFF/session data and backend history remain compatible.

KB pins exact74c0 in five homes. Only Backups' adjacent radius1 fingerprint changed
because the admin menu call precedes it; source labels/routes/role stay unchanged.
Existing member incident controls, actual page paths and six capture selectors
were assessed; no changed member geometry/content/media. Inspect the evidence,
not an assumption that admin changes can never affect member captures.

## Quick evidence and honest remaining gates

- Backend: final core18examples/0 in158.136s; full meaningful cases passed across
  corrected finite segments. Actual final7af51 HTML/sharedfixture9322962 plus built-in
  text six variants and endpoint coverage2examples/0 in51.059s. No SMTP. Final11Ruby
  RuboCop, locale health, normal hooks, selector16runs/55assertions and exact-once
 429spec full/core inventory pass. Export0/44.778s. checks.json retains failures.
- PHP:35tests/345assertions, syntax/formatter/catalog health pass. Ten actual EN/CS
  XTemplate renders, eight offline desktop/mobile DOM/no-JS captures. Root visual
  acceptance at final local layout; isolated normal commit prevented foreign API
  stashing. Guarded ordinary FF preserved all18 foreign file hashes/modes.
- Site: actual TemplateBuilder9/0, ordinary77-template/393-file check, eight static
 390/1280 render cases. Original daily bytes reconstruct exactly after two insertions.
  Historical site packet's pending producer seam is superseded by backend pass above.
- Clients: ordinary all3 generation pass. Focused batch0/~88.5s: Go projection/tests,
  Rust fmt/syntax/provenance/refusal/determinism, TS regeneration/build/typecheck/
  strictconsumer/unit/source selection. Full stdout log was not captured; native
  result and checks-result.json are actual evidence, no rerun to repair logging.
  Final candidate provenance/new-Index executor and exact packed-consumer checks pass.
- Rust compilation gap: extra offline cargo test stopped143 after dependency rebuild
  began; no compiler remained. Compilation/package/MSRV/docs/real-server are UNRUN,
  not waived. Finite CI read saw exact2b498 run45396167185 in_progress. Determine the
  remaining necessary verification, without launching tests or granting readiness.
- React: full app typecheck0/57.97s,111tests/11files0. Later narrow callback/sidebar
  fixes have affected strict/controller/sidebar/lint/format proofs. Ordinary final
  installation and actual wire5 tests pass. Final docs/i18n/inventory and e2e strict
  core pass. Counts overlap: do not sum them. Initial failure receipts remain literal.
  No browser execution yet. Synthetic seven-case interaction/desktop/mobile work
  follows this review. No frontend/system/VM build or deployed API claim.
- KB: source contract47controls/38paths/35concepts/3selectors, annotations98/9,
  managed sources and Nix/JSON/YAML/diff checks pass. No aggregate/build/VM/wiki work.

Finite CI evidence only: site45389094906 success; TS45396187381 success;
backend five runs pending/running at its snapshot; KB two queued; Rust above;
React45399754619 in_progress at publication. No broad CI wait/rerun/dispatch.
Go has no workflow. Known six bundled WASI prefetch warnings remain qualified;
source prefetch is not a frontend package build. Prior green runs at other heads
must not be transferred. All owner native/check effects are joined; reviewer does
not need to observe processes or run product tests to perform this review.

## Documentation routing and fidelity

| Topic | Reader / class | Authoritative home and evidence |
| --- | --- | --- |
| API, current/saved semantics, daily compatibility and recovery | developers/operators; reference | vpsadmin/docs/incident-escalation.md linked by docs/README; actual projection/API/daily specs and export |
| API export/client synchronization | contributors; how-to/contract | vpsadmin/docs/api-schema-export.md; exact clean export and client receipts |
| PHP visible text | administrators; UI/help | new admin form + EN/CS gettext; actual client/XTemplate checks and captures |
| React behavior and routes | developers/maintainers; reference | docs/design/API_CONTRACTS.md, WORKFLOWS.md, REQ-051, DOMAIN_COVERAGE/inventory; linked handbook and tests |
| React SDK/dependency/rollback | developers; reference/how-to | HAVEAPI_CLIENT.md, PACKAGING.md and provenance JSON; ordinary install/lock/archive proof, historical0.5 link pinned4499 |
| React execution history | maintainers; individual record | docs/work-log/2026-11-24-admin-incident-policies.md and WORK_LOG link; scoped results/remaining browser+registry gates |
| Daily HTML behavior/testing | template maintainers; reference/how-to | tests/README.md and minimal root README link; actual builder cases/shared fixture |
| Generated reads/nullability/provenance | client users/contributors; reference | Go README, Rust/TS docs/development, TS0.6 CHANGELOG; generated output and quick checks |
| KB source/control/media impact | KB maintainers; contract | existing canonical workflow, annotations/navigation/page contracts; exact final source assessment. No new KB prose/media warranted |
| Dated command/publication receipts | session operators; individual execution | owning packets below, not product deployment claims |

Root applied the writing skill directly to final EN/CS/prose. Check discoverability,
placement, factual preservation, links and retained compatibility caveats rather
than just audit exit codes. Do not require a new document bundle for this review.

## Owning evidence and requested result

Owner1: backend/{receipt.json,review-packet.md,checks.json,history.txt,full-base-head.patch,schema-export/}.
Owner4: php-implementation/{implementation.md,receipt.json,final.diff,history.txt,render-results.json,dom-results.json}.
Owner0: ../nov24-client-sync/{packet.txt,result.json,final-history.json,candidate-receipt.json};
artifact-publication/{packet.txt,result.json,artifact-only.diff,artifact-series.txt,public-readback.json}.
Owner2: ../nov24-react-admin-incidents-preparation/{final-review-packet.md,final-review-bindings.json,full-series.txt,final.diff,terminal-source-receipt.json}.
Owner3: ../nov24-daily-report-html/{final-packet.md,receipt.json,base-to-head.diff};
../nov24-kb-alignment/{packet.md,receipt.json,base-to-head.diff,retained-full-series.txt}.

Report findings ordered Blocking/Important/Advisory with lane, exact file/line and
concrete failure case. If none, state that and explicit residual gaps. Conclude on
all complete histories, repeated streams, migration lineage (no new migrations),
documentation placement/preservation and actual consumer compatibility. Include
scope/proportionality judgment, especially added projection and UI machinery.
Save the review to ../nov24-admin-incidents/final-review.md and report completion.
Do not edit source, run long checks, merge, publish, deploy or use nested agents.
Root routes fixes to existing technical owners. Narrow remediations get focused
checks; a new design/public-contract boundary needs affected-lane rereview.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
