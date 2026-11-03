---
lifecycle: active
---

# Published advisory corrections

Current phase: **ready, awaiting merge approval**.
All intended changes are committed/published, quick-checked and independently
reviewed. Strict finalKB and the changed admin browser cases passed. The modern
PR is ready. All five repositories have fresh clean published-head/ancestor-default
proof and final native source/input/cleanup receipts are verified. No further tests
or source changes are selected. Current API CI is queued and KB Managed is in
progress; those runs are disclosed, not assumed green or added as a broad wait.

The user's “well then continue, prepare for merging” authorizes preparation.
No default-branch integration, production deployment or session lifecycle action
is authorized. Keep lifecycle active, the session open and the DEV preview running.

## Phase checklist

- [x] Advisory corrections/lifecycle, server-only visibility, both UIs and all six draft-sync guards.
- [x] Proven VPS redirect repair and owning pagination-observation test correction.
- [x] Normal quick/hooks, published consolidated API/KB/config histories and exact pins.
- [x] Independent final review, complete histories/consolidation and NO MIGRATIONS.
- [x] Hosted API full/core evidence plus scoped successful native reuse accepted by reviewer.
- [x] Strict finalKBf977 passed509.55s without overrides/allow-missing.
- [x] FinalAPI942c admin-core all3serial browsercases passed, no failures/skips.
- [x] Modern/client/config fresh source/default/ancestry snapshot; PR122 ready.
- [x] Final API/KB source/input/cleanup/freshness and one currentCI receipt reconciled; pending runs disclosed.
- [ ] Explicit integration direction for the named repositories/targets; nothing merged/deployed.

## Published sources and complete histories

| Repository / target | Feature head | Reviewed base |
| --- | --- | --- |
| vpsadmin / master | 942c6eaed41331f823d8e0f670ed239e2b308440 | 5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5 |
| vpsfree-kb-contracts / master | f97785c2c265172a4c78893e0673034fde56e4dd | ce2c8cd9358c3636e5d39343e595df813a0b197f |
| vpsfree-cz-configuration / master | c4107822060e9e34b24a83950d618c9f28a7722b | 0d71dd289feeb1ea2686f9c7cf0f93728baf9bd2 |
| vpsadmin-webui / main | 1c8478bceb3943645ec06ccde895ee4b0985873f | 63d484fc070dbee633d32624de545e834d483701 |
| security-advisories / 2026-07-13-security-advisory-automation | 0b771120bb2a878c012512b685208124c2b4263b | 7b6c71807e3c5a41f585fd1d9563e151ada71244 |

Worktrees: `worktrees/2026-11-01-published-advisory-corrections/<project>`.
Modern branch is `dev/published-advisory-corrections`; others use the session slug.

API's complete series is A8225229aa0e3306f8b1723c5583969a33c64571c,
B22e9c568daf45dfaafd0fc64f4205f1230650271 and C942c6ea.
Tree55fb83ca693d7c6be4665c55ee03d7383f44e8e5;29paths,+2258/-156.
A/B are identical to prior review; runtimeC/PHP regression remain byte-equal.
2823..942c adds only one existing helper call in the admin spec, after success/
URL assertions. Old2823 and earlier reviewed/deployed sources are retained evidence
refs, not claims of literal ancestry. Upstream HaveAPI0.32.2 baseline is preserved.

KB has exactly d3af1d16cf477b3f0706a900483251586183732b finalpin plus separate
unchanged readinesshelperf977. Tree3024c287051009f3ac207e16fabe55c54fb591f8;
6paths,+22/-10. Config has one generated flake.lock-only commitc410 over fresh0d71;
tree1efa0031c1b2339f2deb8e70861307f08bf95ac6,+3/-3. Both select API942c and
`sha256-uOxIGmW4aIERUDA1tPZdMudKVNZ3lZRarf8BsQ4T+X4=`. Only selected API lock
fields/four source references change in KB; only Services rev/hash/time in config.
Other nodes/edges/follows, OS6bdf458fd9105379860234ff33d352e55844f08f and
content/capture/assets provenance remain. No repeated obsolete pin stream, fixup,
transitional implementation or **MIGRATIONS** in any complete/per-commit range.

## Independent review and scope

[Admin pagination final review](admin-pagination-final-review.md): no Blocking,
Important or Advisory findings. Reviewer0 retained read_only/gpt-6.1-sol/xhigh,
codex-lb/native01a19801-1fc5-70e3-ba37-8c0952a89392; actual identity/settings
verified, no override/fallback/authorship/nested agent. All four lanes applied at
HIGH overall feature risk, narrowly reusing unchanged prior conclusions.
It independently verified final942c/f977/c410 ranges/trees/clean status/complete
histories/no migrations, assertion order and actual selected-input reuse.
[Prior navigation/HaveAPI review](navigation-haveapi-final-review.md) retains the
source/provider/consumer compatibility conclusions at its exact prior heads.

The original advisory writes remain silent, admin-authorized and revision/state
guarded; stored projection updates are atomic. All six sync mutation types retain
expected_state:draft. Announcements use the separate update resource. Server-only
published read authority is retained; the withdrawn modern filtering approach
is absent. C repairs origin-only return navigation without changing auth/CSRF/
Referrer-Policy/JavaScript/timeouts. The final test helper revisit occurs only
after actual action success and canonical page/action checks, so it cannot hide
wrong-Overview routing. It restores filtered row observation, not product behavior.

No new product prose/media/capture campaign is needed for that test-context/pin
delta. Behavior and compatibility docs remain in
[vpsadmin docs](../../worktrees/2026-11-01-published-advisory-corrections/vpsadmin/docs/security-advisories.md)
and committed client/modern owners. [Design](design.md) and [handoff](handoff.md)
link prepared rollout/recovery separately from executed evidence.

## Checks and actual acceptance

Normal API commit hooks70.16s and pinned Node syntax/version passed. First
prepush used ambientOvercommit0.71 versus declaredNix0.74; ordinary push inside
declaredNix passed without signing/bypass/recommit. KB quick45.95s,
lockgeneration4.14s/wholebatch58.41s passed with unchangedhelper/zero drift.
Config hooks/64-node graph/17mappings/API1+PHPWebUI1 evaluation passed. Recorded
source IFD realization is not a system build or deployment.

Final operation `final942c-20261103T021953Z` used one fresh catalog495e
Luna/low/native dw_af6/fullaccess-never watcher, actual banner checked before
release and per-invocation --disable multi_agent, exact-once/nootherCLI/nesting.
Short state `/tmp/aa942c-gbpak7je`; preflight socket64bytes, maximum observed
retained path68bytes, both below108byte limit. Strictf977 ordinary
`nix develop -c bin/check` passed509.55s, actual nonempty admin-only enumeration
158.25s and kernel preflight53.38s passed/no kernel compile. Only admin-core ran:
actual services-shell log **3passed (21.6m)**, no failures/skips, native
expected_success. Script1624.99s, wrapper1299.84s, nativegroup1866.28s,
command2021.36s, wholebatch2747.17s. Utilityterminal0 and no owned local check
remains active. Actual final guest graph6656;2958consumed runtime blobs equal942c
with0differing, separately bundled adminspec matches942c/SHA3c0c4fe9.... Services
and node1 logs stop/qemu_exit/destroy; node2 never starts and is destroyed. Native
recorded PID is gone; two retained virtiofs pidfiles point to nonexistent PIDs.
No blanket claim that all pidfiles were removed. Complete system/derivation paths,
selected dependencies/config/bundle/source and full graph are retained in
`final-acceptance/redirect/final942c-20261103T021953Z/{actual-native-proof.json,actual-input-graph.json,actual-systems.json}`
under the visibility artifact root. Main independently inspected native, source,
systems and final CI receipts.

Reviewer-approved scoped reuse retains actual2823 services-up34/34 (369.87s),
user-core4passed and lifecycle3passed. Their selected scripts/definitions,
14shared browser helpers, runtime/dependency/plugin/runner/filter inputs are
unchanged2823..942c. The changed admin spec is excluded from the2958-blob runtime
source. Actual guest graphs differ from preflight graphs; no whole Playwright
bundle/guest derivation equality is claimed. These are actual2823 executions
reused by proof, not claimed942c executions. Earlier KVM remains scoped to
c46/OS6bdf/unchangedhelper/script/runner boundary, not new-pin execution.

API41544311588 on exact2823 passed all26topics+aggregate. Actual full/core platform
239/0 each explicitly pass selected[1:1:3],[1:3:1],[1:5:6]; foundations1461/0 with
28advisory passes each, fullplugins337/0 including10advisory/outage. Ruby3.4.12/
Bundler2.6.9/all5HaveAPI0.32.2/Maria11.8.6 and actual locks/native artifacts are
retained. Unchanged Ruby/API inputs support reviewed942c reuse.

## Freshness, PR and CI

Implementer1's final03:14:07Z Nov3 snapshot confirms configc410, modern1c and
client0b local=remote, clean and unchanged ancestor defaults as listed above.
Modern CI41462732480/browser41462732324 and all rollups passed; client
RSpec41336065180/RuboCop41336065173 passed. Config CI listing is empty; no hosted
config green is claimed. Normal local preparation evidence applies.

[PR122](https://github.com/vpsfreecz/vpsadmin-webui/pull/122) is READY (isDraftfalse)
at03:14:45.924716Z, exact1c/main, MERGEABLE/CLEAN, no review requests. Title unchanged;
only the main-approved terminal sentence changed to “Prepared for merging; no
production data, merge or deployment changes.” Exact before/after and readiness
proof are in implementer1.md and implementer1-final-readiness.json.

Final API/KB fresh SSH proof confirms exact remote942c/f977 and unchanged
master5586/ce2c, both target ancestors, clean trees/series3+2/no migrations;
comparisons captured at final ranges. Together with impl1's snapshot, all five
published heads match the independent final reviews. No merge claim is held.

ONE final currentCI snapshot: API942c CI41563874916 queued; PHPUnit41563874914
and i18n41563874994 SUCCESS. KBf977 Check41564405469 SUCCESS; Managed41564405472
in_progress. Old2823 integration41544311870 is now completed/cancelled. No new
failure observed, current/foreign/completed runs untouched, no further wait or
retry. Local accepted checks and reviewed scoped reuse complete preparation;
queued/in-progress CI is not described as green. Any later actual failure returns
to its owner before integration. No blanket campaign was added.

## Preserved failures and limits

Original missing-count and hosted password-lock holder/causes remain UNKNOWN.
Later exact-case/order diagnostics and one hosted retry do not establish flakiness
or retrospectively fix the first failures. Receipts correctly describe60expected
responses:48successfulHTTP200 plus12expectedHTTP404denials,36successful counted
collections. EBE integration135scripts/118tests failed3WebUI scripts after117tests
passed; C's wrong-Overview cause is fixed and its own assertions remain strict.
The later admin pagination failure1pass/1fail/1skip remains retained beside the
new3pass proof. Failed setup with163byte socket exceeded108limit before process
spawn; shortening unique state fixed setup, without application changes.

Earlier local focused utility nested agents/another CLI and duplicated shared
outputs. Combined status/later wrapperexit/earlier overwritten DB identities have
limits; clean hosted API proof is primary. Known commands/PIDs were reconciled,
no two-clean-invocations claim or receipt-tidying rerun. Subsequent utilities use
the supported per-invocation delegation restriction. All original records remain
in [owner evidence](visibility-verification.md), [risk addendum](merge-preparation-risk-addendum.md),
[history](history.md) and prior source-scoped review/acceptance reports.

Reusable lessons: [socket paths](../../notes/vpsadmin/2026-11-03-native-runner-unix-socket-path-length.md),
[Nix hook environment](../../notes/vpsadmin/2026-11-03-overcommit-pre-push-nix-environment.md),
[kernel package names](../../notes/cross-project/2026-11-02-kernel-preflight-package-name-ambiguity.md).

## Preview and next operator action

DEV preview remains running on backendAPIa38c/modern1c with synthetic data intact.
Host-live-mounted PHP reads unchanged runtimeC from current942c worktree without
separate activation. Prior TLS/OAuth API66/modern24/PHP21 role checks belong to
their recorded runtime; Mailpit4sign-in notices/0advisory messages. Credentials
stay in portal Cluster fields. See [preview access](preview-verification.md).
No fixture writes, restart/backend update, stop/reset or session cleanup is
requested. Config still selects modern70bd; API channel does not select/deploy1c.

Future rollout must pause sync, upgrade every active six-guard consumer, complete
compatible API/UI rollout before writes and avoid mixed API pools. Software
rollback must preserve published-only privacy; it does not reverse corrections
or retraction and cannot restore deletions (backup required). No schema/daemon/OS
coordination is introduced. Production advisory edits/deletions remain separate.

Next operator action: explicitly direct integration for the repository/target
set in the table when desired. Before an approved merge, recheck exact current
target/head/history and apply ordinary changed-input/review rules if they moved.
Preparation is ready; no integration or production action has been performed.
No repository/machine integration/deployment claim is held; keep session open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
