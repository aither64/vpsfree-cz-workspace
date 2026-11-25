# Shared redesign: lead closure and corrected source gate

2026-10-31. Read together with the independent [original report](shared-review.md),
which remains scoped to its exact reviewed ranges and retains Important R1.
This is the lead's direct narrow-fix verification and history/publication record,
not a new independent review or runtime certificate.

## Finding closure

Reviewer0 completed all four lanes at HIGH risk: no Blocking finding, only R1,
no other Advisory/Important. Whole-series consolidation, no repeated update
streams and single unreleased migration lineage were explicitly assessed.

R1 requested summary-aware public last-stop/epoch output while evaluator and
reconciliation read persisted values. Lead inspected the exact four-path repair
and actual-route tests, negative2/2 on reviewed source then positive9/0, scoped
lint/whitespace and normal hooks. The fix adds no schema, API field, qualifier,
mail, transaction or product contract. [Remediation](shared-timestamp-remediation.md)
binds commands/results and retained commit3cde6709. This closes R1 under
mandatory-change-review step9. A confirmation-only unaffected review rerun is
not needed; the original review is not relabelled as reviewing the fixed source.

## Corrected complete backend history

Base/default: ac10a62f1cb0fc890378ae83cdf18dd0e29f049a.
Final head: f60d41a453b1703e42de4341285bdc6ba339aff0.

- 89a303e6396882ea7981a8077dba05a4ce9861ac: shared backend/API/schema/support.
- f3e58cd3e5bf19e588ca40ef44b3b1da696137c7: legacy consumer.
- f60d41a453b1703e42de4341285bdc6ba339aff0: isolated test DB compatibility/docs.

Lead independently read HEAD/tree/commit list, confirmed only the four R1 paths
differ from original reviewede9 and `git diff3cde..final` exits0. Final tree
f6656bd2c1d49f308c6cc1697ad3fb1c44d2be5c exactly equals tested/hook-checked
3cde6709. Owner range-diffs and stable legacy/testenv patch IDs agree. No fixup,
superseded OOM implementation, alias, transitional migration or repeated input
update is introduced by consolidation. Migration, core schema and lock graph
are unchanged by R1. Original e9 and pre/post-consolidation refs remain evidence.
Normal Nix rebase and hooks passed; fresh SSH default/mergebase remained the base.

SSH feature publication exited0 with explicit last-remote4d72 lease; fresh
ls-remote proves featuref60d and unchanged defaultac10. Capture comparison saved.
See shared-r1-final-history.json, shared-{reviewed-final,r1-consolidation}-range-diff.txt,
publication receipts and [delivery](shared-backend-delivery.md).

## Other applications and direct browser fix

Templates bf32762126f21fb7fc825fac25b5b45d075a2681 remain exactly independently
reviewed, published over SSH, clean; exact-head Check41185476621 passed.

React reviewed55a813b4 had no independent finding. Subsequent real fixture-browser
checks found two URL writer races. Initial batch10pass/1fail/1notrun, then
canonical-limit-only follow-up1pass/1fail are retained. Lead inspected the final
four-path narrow correction: pass existing pagination.limit to the new incident
filter, write canonical limit with page/from_id reset, and opt into existing
router flushSync convention. No shared pagination/router/API/toolchain redesign.
Focused21, subsequent filter2/types, actual affected desktop/mobile2/2 and
previously unrun mobile old-API1/1 passed without retries. The unit option guard
is not claimed to reproduce timing; actual failed browser traces are the
negative evidence. Lead accepts this correction of reviewed filter preservation
under the existing narrow-fix boundary; no unrelated review rerun.

Corrected app4343a02cb13ba42ae50a3276715f1c8e5b7765ea/tree
4bee7d1455f35cd422fc385fafda18486f6ee3ea equals tested staged runtime.
Routine evidence child9e7dd95d67a3b33b88674a3d436775e0bb820504 adds work-log,
four accepted actual synthetic PNGs and two screenshot-only scroll lines.
Those lines passed affected E2E types and one desktop case. Lead viewed all four
images and requested/accepted the desktop replacement with heading/history
visible. Eight unchanged detail component paths bind retained55 mobile detail;
new list images come from fixed runtime, desktop detail from4343 plus capture
lines. No screenshots claim real backend authorization/stop/mail proof.

Final React tree47812c2ba7826c71cf6a014de1dd92592bb7dbea, two coherent
commits; original/fix/preconsolidation evidence retained. SSH/main/lease verified,
final9e7 published and PR115 updated. Runtime/toolchain equal4343; no migrations,
pins, obsolete fixups or old current-media claims. [Final owner receipt](react-shared-final.md)
contains exact ranges/source hashes/allocated tooling and cleanup. Automatic exact
head CI41186801790 and Playwright41186801724 remain pending.

## Limits and next gates

Corrected application source gate is cleared for the planned bounded verification
and feature publication workflow. No merge, deployment, policy activation,
production KB write, lifecycle action or readiness-for-use claim follows.

Exactf60 hosted foundation modes passed with MariaDB11.8.6/OFF/RR receipts:
full1469examples/0failures/3pending; core1469/0/52pending. Both VPS topics also
passed; remaining topic aggregate and actual required physical/browser scenarios
are pending. Smaller API migration/PHP/lint/libnodectld/i18n workflows passed.
Hosted integration is actively running, so no duplicate local guest/image run
is admitted. A supported no-build ResourcePool/cache plan is retained for a
conditional fallback only, requiring fresh measurements before allocation.

KB's five-pin refresh is a separate mechanical source/history/capture package.
Its unchanged runner retained-metadata test failed after successful shutdown;
targeted diagnostic passed. [Architect disposition](kb-source-check-disposition.md)
and lead accept a PIN-ONLY baseline exception, not a full check pass or runtime
identity change. OriginalFAILED + targetedPASS + exact unexecuted suffix results
must remain separate. Independent pin/history assessment and final strict hosted
Check remain required; no runtime/capture admission yet.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
