---
lifecycle: active
---

# Published advisory corrections

Current phase: server-only visibility fix complete in the running DEV preview.
Only published advisories are readable by anonymous/member/support; drafts and
retracted records/relations are admin-only. Direct retract remains silent and
retains admin history. Both UI runtimes are unchanged; rejected modern f7 guard
candidate was withdrawn and exact1c847 restored. No frontend filtering shipped.

Final APIa38c9f871f89312f16d18e158efbbbb340ec53e4 and
KB4fd4f2b8ca737b6b6baaf97998fb9484be4c1e91 are committed/quick/hook-pass/pushed.
[Independent affected review](visibility-final-review.md): no findings, fourlanes,
Highrisk, complete histories/NO MIGRATIONS. Full API84/core74, strictKB4fd4 and
native legacy18 passed. Exact failed CI case seed19905 also passed1example/
60successful-envelope requests; original hosted countnil cause remains UNKNOWN.

Data-preserving services update exited0 in319.3s. Running APIa38c/sourcebytes
verified, services /nix/store/mygq0r3nbd1hyb3ddy1r0sbvmsb7n7l2...; appliedpending
null, node/config/OS unchanged, modern1c unchanged. Actual trustedTLS API66 role
reads PASS; modern24destinations normalOAuth/freshcontexts PASS; PHP21pages normal
rolelogin PASS. Anonymous/member lists only2published and denied direct1draft/
3retracted; admin management retains1/2/3. No advisory writes. Fixtures1draftrev1/
2publishedrev2/3retractedrev2 remain. No active test/browser/utility; cluster stays
RUNNING for user. [Delivery](visibility-verification.md), [preview](preview-verification.md),
[modern browser evidence](modern-preview.md). No reset/stop/production/defaultmerge.

Open hosted checks: API41465157664 failed corecountmetadataassertion whose first
response was not retained; full local+isolatedpass do not relabel CIgreen orprove
flake. KBManaged41465898434 failed unchangedobsoleteHTMLreadinessbaseline; strict
localpassed, no unrelatedKBcodefix. APIintegration41465157701 inprogress at final
snapshot; lint/PHP/i18n/KBCheck passed. No CI wait/rerun/retryloop. Production/
integration readiness remains separate; DEVrequest complete on reviewedsource.
Temporary1lineassertionpatch savedprivately/notshipped; no needlessamend/repin.

Development preview is RUNNING/READY for both WebUIs, left running for the user's
manual trial. Explicit user START request fulfilled; no production deployment,
merge, session stop/reset/archive or cluster cleanup occurred.

- Legacy PHP: https://webui.aitherdev.int.vpsfree.cz/?page=security_advisory
- Modern React: https://newadmin.aitherdev.int.vpsfree.cz/admin/security-advisories
- Login: session portal → Cluster → service credential fields (no passwords here).
- Internal/VPN DNS/routes and public [development CA](preview-ca.crt) trust required.
- Shared synthetic examples:1draft/rev1,2published/rev2,3retracted/rev2.

Normal trusted-TLS OAuth/login/control checks passed in both UIs. Modern
published/retracted editor, lifecycle confirmations and separate announcement
composer opened/canceled; legacy all3details, guarded editors and bounded node
form verified. No advisory browser writes; one guarded same-name API correction
on published2 advanced revision silently. Publications/retraction retained0→0
Mailpit evidence; final3messages are new-sign-in notices, no advisory mail.

Exact API49f5/React1c847 worktrees remain clean. Runtime source/store/closure,
paired modern2541sourcefiles+7BFFmodule equality, actual path-input unknown build
metadata limitation, source OS823, operation ownership and browser evidence:
[preview-verification.md](preview-verification.md), [modern-preview.md](modern-preview.md),
[preview-plan.md](preview-plan.md). Two guests services+node1 single/bridge,
pid1475262; all start/browser observers finished. No active utility/check; cluster
runner/guests intentionally remain running. Do not stop/reset/release them absent
explicit direction. Technical preview plan/verification are session evidence,
not new product changes requiring another final code review.

Implementation/review/local acceptance remain complete, exact feature heads
below unmerged. Remaining hosted CI and any integration/deployment are separate.

## Final branches and histories

| Repository / target | Final head | Reviewed base |
| --- | --- | --- |
| vpsadmin / master | a38c9f871f89312f16d18e158efbbbb340ec53e4 | 097226b22edf8b59f80b5dfaa55265e9d0cac633 |
| security-advisories / 2026-07-13-security-advisory-automation | 0b771120bb2a878c012512b685208124c2b4263b | 7b6c71807e3c5a41f585fd1d9563e151ada71244 |
| vpsfree-kb-contracts / master | 4fd4f2b8ca737b6b6baaf97998fb9484be4c1e91 | ce2c8cd9358c3636e5d39343e595df813a0b197f |
| vpsadmin-webui / main | 1c8478bceb3943645ec06ccde895ee4b0985873f | 63d484fc070dbee633d32624de545e834d483701 |

API has A163677bd45b5ac0a179a0bfa144bcbd9ada9e231 then Ba38c9f87.
Previous49f5/5276 acceptance below remains baseline evidence, not new runtime proof.
Others each have one consolidated commit; KB is five coherent source pins +8/-8.
No obsolete fixup, repeated pin stream or MIGRATIONS. Old reviewed/tested ranges
remain evidence refs; no default history rewritten. Modern branch is
`dev/published-advisory-corrections`, [draft PR122](https://github.com/vpsfreecz/vpsadmin-webui/pull/122).
Other branches use this slug; all worktrees are in its verified group.

## Phase checklist

- [x] User authorized same-session devcluster start; supported topology/source/auth plan recorded.
- [x] Development cluster ready on exact reviewed API/modern source.
- [x] Both WebUIs verified with shared development data; user access/instructions delivered.

- [x] Verified session/provider/full retained roster; initial substantive tracking committed.
- [x] Architect design, expanded user scope, API/client/both UIs/exact KB pin implemented.
- [x] Quick checks and mandatory hooks; main-authored cs/en copy and implemented visuals.
- [x] Independent High-risk four-lane final review, full histories and no-migrations conclusions.
- [x] Three Important modern findings and Advisory copy resolved/directly reconciled.
- [x] Independent HaveAPI0.32.1 baseline compatibility refresh, no findings.
- [x] Independent affected readiness and form-layout reviews, no findings.
- [x] Full/core advisory API, complete client, modern full tests/build/browsers/packages.
- [x] Final strict KB and all18 real legacy browser cases; native guest/process cleanup proven.
- [x] Current CI/failure/retry snapshot, exact source/input proofs and final handoff.
- [ ] Remaining hosted integration/Managed CI conclusions, not awaited.
- [ ] Explicit integration approval and approved default integration; no deployment authorized.

## Acceptance

| Check | Result and actual source |
| --- | --- |
| Full-plugin advisory API/model/concurrency/outage | 88 examples, 0 failures/pending on c8ef; reviewed identical effective inputs retained for final API |
| Core advisory API/model/concurrency | 79 examples, 0 failures/pending, same source/input proof |
| Complete client | 298 examples, 0 failures/pending on final0b771120 |
| Modern | Final1c847:1976 tests/314files, production build,10desktop/2mobile cases,all5Nix outputs passed |
| Strict KB | Final5276 selecting API49f5, exit0,453.13s |
| Real legacy browser | Exact final49f5,18 Playwright passed, exit0,1387.69s; native expected_success |

Final strict/legacy batch1844.06s. Services and node1 native QEMU exit0/destroy;
node2 never started/destroyed. No exact owned run-path process remains. Final
native13files and definition/runner/all guest closures retained in
/tmp/2026-11-01-published-advisory-corrections-acceptance/layout-final/.
Definition /nix/store/qby9fzk9y3021xb00nzkah8yc7v2062h-os-test-vpsadmin-webui.json;
runner /nix/store/88cifs3zcrd25xqx63h3k5ackdcjdpiw-test-runner.drv.
Complete source/input/derivation/environment/status paths and counts are in
[verification-final.md](verification-final.md), [API acceptance](api-acceptance.md)
and [modern verification](modern-verification.md).

API runtime tests were actually executed at c8ef. Final A/API/runtime/spec/DB
inputs, locked graph, actual shell derivation and effective full/core bundles
are equal except independently tested inventory entries and separately reviewed
readiness helper. Reuse is supported by those exact effective input proofs,
not tree equality alone or falsely claiming the new SHA was rerun. Final legacy
and strict KB were executed on the actual final heads. No unchanged long suite
was repeated. MariaDB11.4.12/REPEATABLE-READ/snapshot_isolation0 captured.

## Reviews, failures and documentation

Retained reviewer0 Sol/xhigh on codex-lb, independent/read_only, covered general,
architecture, proportionality, risk/compatibility. Original full four-repo review:
[final-review.md](final-review.md). Findings/fixes and exact successors:
[review-reconciliation.md](review-reconciliation.md). Independent affected reviews:
[refresh-review.md](refresh-review.md), [readiness-final-review.md](readiness-final-review.md),
[layout-final-review.md](layout-final-review.md). All complete series have explicit
consolidation and NO MIGRATIONS conclusions. Earlier paused review supplies no clearance.

First savepoint, real-metadata shape, uppercase fixture and endpoint inventory
failures remain recorded. Real legacy failures exposed obsolete HTML readiness,
wrong notification container (7/1/10) and overflowing membership table (11/1/6).
They were diagnosed/fixed with normal hooks, reviewed as applicable and verified
by final18/18. No forced clicks, weaker guards, timeout increases or framework.

Unchanged KB process fixtures had two observed startup/snapshot failures;
original failing tuple/TIDs were not retained, so precise timing causes remain
supported explanations. Exact owned orphan reconciliation and first failures
are retained. Final strict check passed without fixture/runtime/guard changes.
Guest traces/screenshots from earlier real failures were not retained; native
logs/counts and synthetic actual-renderer layout evidence are distinguished.
See [legacy-layout.md](legacy-layout.md), [API acceptance](api-acceptance.md) and
[history](history.md) for the complete chronology and limitations.

Owning API behavior/compatibility documentation is discoverable through
[vpsadmin docs](../../worktrees/2026-11-01-published-advisory-corrections/vpsadmin/docs/security-advisories.md);
client docs and modern REQ/workflow/API/action/evidence records are in their
committed owners. [Handoff](handoff.md) describes exact interfaces/rollout/recovery.
No advisory KB binding exists; only the exact-source pin/check was needed.

## Hosted CI snapshot and remaining work

Client final RSpec41336065180/RuboCop41336065173 SUCCESS. Modern final required
CI41339759463/browser41339759427 SUCCESS. API topic matrix41351014848 at0111
passed all26full/core jobs plus aggregate (27/27); later B-only changes did not
select API specs, and identical API inputs are proven. Final49f5 PHP41358612246
and i18n41358612247 SUCCESS, integration41358612359 in progress/no failure in
snapshot. Final5276 Check41358727268 SUCCESS.

Final5276 Managed41358727216 attempt1 failed before VMs in unchanged ack-loss
fixture test-machine.rb1025, seed8022. Complete failed log retained; zero uploaded
artifacts and missing original tuple limit diagnosis. After inspecting the first
failure and exact final local strict PASS, one retry of only failedjob125004296897
was approved: HTTP201, same head, attempt2/newjob125007871097 queued in final
snapshot. Attempt1 remains failed; no Managed VM/retry success claimed. No further
retry or CI waiting. Complete own-branch inventories36API/16KB show zero
superseded active runs; previous cancellations terminal, current runs untouched.

Next operator action: inspect remaining exact-head CI conclusions and diagnose
any failure before approving integration into the named targets. Implementation,
review and local acceptance are complete; CI is not merge/deploy permission.
Implementer0 retains API/KB Git and follow-ups, implementer1 client/modern/legacy
UI follow-ups; no active utility or local operation. No repository/machine claim.

## Rollout and boundaries

Corrections to draft/published/retracted original text, CVEs/node membership/time
and explicit retract/delete remain silent, guarded by revision/state and admin
scope. Announcements retain their separate explicit mail/state/time controls.
Pause sync, upgrade all active clients, finish compatible API/UI rollout before
writes; no mixed API pools. No schema/daemon/OS coordination. Software rollback
does not reverse content/retraction; deletion recovery needs backup. Production
excluded drafts and existing update posts were untouched. Nothing deployed.

Initial tracking c4eb9add7; final consolidated handoff checkpoint follows normal
cadence, stages only owned Markdown/manifest/notes and preserves unrelated shared
changes. Raw evidence remains untracked. Runtime exact-pair grant allowed a
useful completion message to source session2026-10-30-linux-cve-review; no peer
files/roster/worktrees/credentials accessed. No lifecycle cleanup authorized.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
