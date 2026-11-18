---
lifecycle: archived
---

# NixOS stable channel update

## Status

All requested work complete: original nginx one-time pins, confctl source fix,
and both confctl adoption updates merged into remote master defaults. A final
`bf19f6aacae7f57c8bd06746ff10481b242baf2f`, B final
`fadb89a3f828bc98ea75aa5fcd8de953390c15e2`, confctl
`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`, exact remote proofs recorded.
Both configurations now load corrected forward-only behavior on next tool/workflow
invocation. Existing nginx4077fb98 pin and nixos-26.05 tracking preserved. No
system deployment or session lifecycle action performed; session remains open.

## Phases

- [x] Design and fix inclusion
- [x] Channel updates committed and quick checks
- [x] Independent review/history assessment
- [x] Feature publication and approved integration
- [x] Deployment target handoff

## Confctl follow-up phases

- [x] D5 formal design accepted
- [x] C implementation/docs committed and quick checks
- [x] Independent final review
- [x] Broader local checks and feature publication
- [x] CI completion
- [x] Concrete result prepared
- [x] Confctl integration approved and merged

## Confctl adoption phases

- [x] D6 brief accepted
- [x] A2/B2 generated commits and quick checks
- [x] Independent complete-history assessment
- [x] Adoption heads published and merged

## Packages

| Package / deliverable | Owner | Dependency / checks | Status | Transition / evidence |
| --- | --- | --- | --- | --- |
| D: bounded upstream/channel analysis and design.md | architect0 | PR inclusion, mapping, compatibility, deployment scope | accepted | brief accepted 2026-11-18 16:38 UTC |
| D3: forward-only follow-up | architect0 | pinned updater/workflow evidence, no mutations | accepted | completed 2026-11-18 17:59 UTC; forward-only.md |
| D4: forward-only no-update solution proposal | architect0 | reuse D3, bounded updater/graph design; no implementation | accepted | recommendation in forward-only.md |
| D5: formal confctl design | architect0 | current confctl baseline/interfaces/compatibility/check brief | accepted | sufficient brief accepted/released 2026-11-18 18:23 UTC |
| C: complete confctl implementation/tests/docs | implementer0 | accepted D5; hooks/quick/full checks/commits/evidence | accepted source/local checks; CI pending with lead | package-c.md; d8ab7d4 |
| D6: bounded adoption brief | architect0 | root/channel mapping and lock-only checks | accepted | design.md current D6 |
| A2: vpsfree confctl pin adoption | implementer0 | D6 + quick semantic checks | accepted and merged | prior C accepted, capacity confirmed |
| B2: org confctl pin adoption | implementer1 | D6 + quick semantic checks | accepted and merged | prior B accepted, capacity confirmed |
| A: vpsfree-cz-configuration channel update | implementer0 | sufficient D brief, hooks, input/evaluation checks | accepted | assigned/capacity confirmed 2026-11-18 16:31–16:33 UTC |
| B: vpsadminos-org-configuration channel update | implementer1 | sufficient D brief, hooks, input/evaluation checks | accepted | assigned/capacity confirmed 2026-11-18 16:31–16:33 UTC |

Retained members verified with workspace-write for design/implementation; model
and effort preserved. Other implementers remain unassigned because two repository
packages cover the scope. Lead owns shared tracking and integration.

## Evidence and next

Initial guidance read: project map, sessions, Git, documentation, verification,
deployment, commits, lifecycle and team roles. Documentation and handoff skills
apply. Source deliverables and package reports accepted; merged proof and final
checks recorded below. Current follow-up: read-only forward-only semantics.
No machine claims or deployments. Preserve all unrelated shared workspace edits.

## Design acceptance

[design.md](design.md) settles independent A/B boundaries, source recovery and
no-deployment scope. PR merge `1e6cf0d7cf5f5354d1bfd7105813dddb527851d4` is in
release-26.05; actual locked revision will be checked by each owner. Expected
nginx versions are stable 1.30.7 and mainline 1.31.9. Both worktree bases are
fresh origin/master: A `e3910c79e85edc94ee3e715bf93887413bfed827`, B
`91b5f45d8956c1cd8102e74cf720da306107b308`. Shared tracking remains lead-owned.

## Scope correction

User clarified one-time update, no tracking branch change. Both implementers
steered immediately; original URL/ref must be preserved, obsolete branch-switch
commits consolidated, final diff expected generated lock only. Architect amending
brief. Merge approval persists for corrected intended scope in both master targets.

Corrected heads observed (pending owner check reports): A
`828c390c7e1857f11522933977afd852634b85f8`, B
`72c18d811086dac8e16ec8c7ee6bf8e32ce62123`. Each final diff contains only
three generated locked-field replacements in flake.lock; flake.nix unchanged.

## Quick check acceptance / review

Both owners report final committed quick checks PASS, clean worktrees, exact
normal tracking preserved and only selected locked fields changed. Git mutation
windows released to lead; inventories remain read-only with owners. Mechanical
content exemption applies; reviewer0 Sol/xhigh assigned general whole-branch
history/migration assessment using [review-packet.md](review-packet.md). No
substantive review lanes needed for generated-only update.

## Integration preparation

Clean detached target worktrees `<repository>-merge` prepared from each recorded
base with repository Nix shells, satisfied gems and active installed/signed hooks.
Feature heads published and freshly proved equal by ls-remote. Comparison captures
saved for both exact ranges. `gh run list` for each feature branch returned no runs;
no scheduled update workflows dispatched. No repository claim acquired yet; review
assessment remains pending.

## Deployment inventory progress

B system evaluation PASS: all 11 managed machines resolve changed input; four
nginx targets `org.vpsadminos/{int.images,int.iso,int.www,proxy}`, all service
ExecStart paths nginx 1.30.7; images/ISO fancyindex overrides. All 11 assertions
empty; four toplevel derivation paths evaluated without realization. Narrow
source-identity receipt extraction pending; A inventory remains running.

## Review accepted

[review.md](review.md): reviewer0 retained Sol/xhigh, general/history assessment
of both exact final ranges, no findings, no obsolete/repeated streams, no
migrations, normal tracking preserved, docs placement accepted. Mechanical
content exempt from standalone substantive review. Lead rechecked complete
single-commit series and final lock-only diffs against reviewed ranges.

## Integration evidence

Both approved updates fast-forward integrated with active hooks from fresh clean
detached target checkouts. Fresh remote master equality:

- vpsfree-cz-configuration master = `828c390c7e1857f11522933977afd852634b85f8`.
  Base `e3910c79e85edc94ee3e715bf93887413bfed827`; claim
  `85992d1b-9092-437c-84c7-a08cc88fcf0a` held 16:49:16, released and resulting
  released state verified 16:50:20 UTC.
- vpsadminos-org-configuration master = `72c18d811086dac8e16ec8c7ee6bf8e32ce62123`.
  Base `91b5f45d8956c1cd8102e74cf720da306107b308`; claim
  `c8d028f0-1ab7-4a8d-a241-9d26325a0323` held 16:50:40, released and resulting
  released state verified 16:51:35 UTC.

Ordinary Git pushes over SSH succeeded and exact ls-remote equality proved
before releasing. No stale baseline, rebase, uncertain push or hook failure
within either critical section. No claims held during review/check waits.
`workspace-host coordination` only supports status/guide in selected package;
a refused acquire had no mutation; documented `dev-session coordination` used.
Feature refs retained. No machine deployment/claims or session lifecycle action.

## Deployment command syntax

User added request for commands using `--one-by-one`; execution remains outside
scope. Architect D2 verified pinned confctl docs/source: quoted File.fnmatch?
brace alternatives, full machine selectors, `confctl deploy --one-by-one PATTERN
switch`. Normal deploy builds first, then serializes copy/activation/checks;
brace order is not deployment-order guarantee. B command:
`nix develop -c confctl deploy --one-by-one 'org.vpsadminos/{int.images,int.iso,int.www,proxy}' switch`.
A exact command pending completed target inventory.

## Final acceptance

A/B packages accepted after checking owner evidence and actual full diffs.
A: 51 changed-input consumers, 17 enabled nginx, all fixed stable1.30.7 source;
34 disabled; 52 managed vpsAdminOS entries use unchanged inputs and seven org
references are unmanaged. B: 11 changed-input consumers, four enabled fixed nginx,
seven disabled; fancyindex variants preserve fixed source. No independently
sourced enabled nginx in either selected subset.

All commands/watchers quiescent. A targeted inventory passed in82s; selected
normal proxy system derivation passed in6s. Original broad A pass was stopped
and supplies no fleet assertion evidence; its two web-package IFD builds were
not full systems/kernels. B assertions and four system derivations pass. Exact
source/package/system paths and logs are in package records. No fleet build,
activation or runtime/deployed-generation verification.

User-requested --one-by-one commands verified against exact evaluated inventory
using Ruby FNM_EXTGLOB: A compact nested brace pattern selects exactly17, B exactly4.
See handoff. No new validation CI runs on final feature or master heads; existing
scheduled Daily update results do not validate these changes. No more checks
or source changes required. Remaining operator action: deploy selected systems.
Clean disposable merge checkouts and feature worktrees/refs retained; no session
cleanup or lifecycle mutation performed. Tracking updates follow initial-commit
cadence and remain uncommitted working records until authorized tracking milestone.

## Forward-only follow-up

User asks whether daily --forward-only prevents a downgrade after the one-time
ahead-of-channel pin. Bounded read-only D3 assigned to architect0 after prior D/D2
acceptance; own session identity/environment and roster reverified. Scope is exact
workflow flags and pinned updater comparison/skip/error semantics, with optional
single upstream ancestry comparison. No source changes or update execution.
Conclusion/evidence pending; no automatic review triggered by investigation alone.

D3 accepted: [forward-only.md](forward-only.md). Exact pinned implementation
uses Git ancestry, not timestamp. Behind/diverged candidate exits3, real lock
unchanged, daily workflow fails before push. A grouped first update is atomic,
so unrelated production/staging updates also wait in that invocation. Same pin
becomes no-op0; descendant resumes automatically. Live compare17:57:17 UTC showed
nixos-26.05 behind by106, so current candidate would reject and preserve pin.
No source changes or workflow run; no review gate triggered by findings alone.

## No-update proposal request

User requests a solution where expected behind-channel status means successful
no-update. D4 bounded design assigned; no implementation or integration requested.
Assess independent updates and graph safety, explicit error compatibility and
focused tests; avoid masking errors through workflow exit-code suppression.

D4 proposal accepted: expected behind/equal should be successful no-update in
confctl update; descendants advance, divergence/invalid/evidence errors fail.
Per-selected-input Nix attempts under single final atomic install/commit preserve
independent updates and whole shared/nested graph integrity. Existing strict
check-update retains rejection semantics. Detailed scope/tests and compatibility
recorded in forward-only.md. Proposal only; user deliberating expected behavior,
no app implementation or additional merge performed/assumed.

Formal design and C prep released; one repository owner avoids overlapping source
/index changes. No other implementers assigned because scope is narrow. Lead owns
acceptance/tracking/review and approval-bound integration.

C preparation evidence: registered confctl branch `2026-11-18-nixos-channel-update`
at fresh default/base `ff5e017780a35fb97b549db2a51b570193867c3b`, same as
configuration-pinned version. Nix environment/hook prep owned by implementer0;
no application edits before D5. [package-c.md](package-c.md) owns execution evidence.

D5 brief accepted in design.md; relevant interfaces, invariants, compatibility and
recovery settled. C released to implementer0 after clean env/hooks/capacity proof.
One finite deterministic per-target Nix pass; typed behind-only skip, no manual
graph splice; final strict check/snapshot/install once. Lead precommit prose pass
and mandatory all-lane final review remain; full suite follows review.

## C verification/review preparation

CI inspected at unchanged baseline: push triggers RSpec Ruby3.3/3.4/4.0,
RuboCop, and self-hosted ci-tagged tests for lib changes. No workflow edits
needed. Review risk classified high due to public CLI exit behavior and atomic
lock/index/commit recovery semantics; use general, architecture/repetition,
scope/proportionality and risk/compatibility lanes. Reviewer0 retained Sol/xhigh
is independent of C; explicitly assign only after complete commits/quick checks.
No automatic review of the design/proposal alone. Applicable references read.

C milestone: core transaction/CLI/tests/docs implemented, precommit prose pass
performed directly by lead with writing skill. Corrected documentation to state
mixed forward+behind whole-attempt skip and preserve post-install hook-failure
recovery exception. Exact final wording sent to owner; rest accepted. First focused
run128 examples/8 fixture failures (not passing evidence), fixed at narrow fixture
boundary, affected checks running; no broad repeat/full suite before review.

C complete committed range ff5e017780a35fb97b549db2a51b570193867c3b..
d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49. One logical14-file452+/79- commit,
clean tree, no migrations, obsolete approaches or repeated streams. Final quick
128RSpec25.91s, changed Ruby11files lint, active hooks/man generation/diff--check
pass. Evidence [package-c.md](package-c.md), full packet
[confctl-review-packet.md](confctl-review-packet.md) checked and assigned to
retained reviewer0 Sol/xhigh all four lanes. Full suite/publication await review.

C final all-lane review accepted: [confctl-review.md](confctl-review.md), reviewer0
retained Sol/xhigh, exact ff5e017..d8ab7d4, no findings. Explicit history/no-migration/
documentation conclusions pass. Full RSpec/full RuboCop and then fresh-baseline
feature publication released to C owner; no default integration approval.

C full checks pass at unchanged reviewed d8ab7d4:245RSpec/0failures/2existing
packaged-CLI pending (CONFCTL_BIN unset in source shell),65.44s; full RuboCop
110files/no offenses, batch72s. Fresh fetch origin/master still ff5e017,
0behind/1ahead, no rebase. Feature published; exact remote equality inspected.
CI attempt1 exact d8ab7d4:Tests44372697108(workflow242179286),
RSpec44372697114(workflow240426206),RuboCop44372697153(workflow240426208).
RuboCop CI success; other two in progress. Runtime monitor start id
2ca59ed6-804a-4cd7-bbf2-6d68b49c3372 rejected caller ownership with no registration;
no acknowledged executionOwner/runtime/native operation. Own identity/roster
verified. Use documented minimal-output parent GitHub reads fallback, no duplicate
native observer, retries or CI mutation. No claims acquired.

CI RSpec run44372697114 attempt1 success on Ruby3.3/3.4/4.0; RuboCop
44372697153 success. Integration44372697108 remains in Run tests on self-hosted
runner, no terminal outcome yet. Only exact reviewed d8ab7d4 observed, no reruns.

C source/package accepted after owner complete report; root owns CI observation,
implementer0 retains failures/fix responsibility. Previous successful Tests run
43477531381 on baseline ff5e017 took17m36s; current observed run remains within
normal integration duration. One run only, no repeat/cancellation.

## C final CI acceptance

Authoritative GH Tests44372697108 attempt1 completed SUCCESS19:09:36UTC at exact
reviewed/published d8ab7d4; no failed steps. All CI green: RSpec matrix3.3/3.4/4.0,
RuboCop, self-hosted integration. Bounded runner read-only evidence confirms4of4
integration tests successful,1532.96s; carrier/deploy scenario spent223.35/191.01/
162.79s building/deploying generations in late examples. Runner moved to unrelated
job afterward; no confctl test processes. This diagnoses elapsed overrun without
rerun/restart. No code changes after review. Final diagnostic read joining before
handoff, no unknown mutating effects. C accepted; no further fixes/checks needed.
Ready for explicit confctl/master integration approval. No repository/machine
claims acquired for this source work. Existing configuration refs remain retained.

Final C diagnostic fully joined/quiescent, read runner source ref equals exact
reviewed head, no remaining tool sessions/watchers/remote commands. Latest bounded
GH read confirms all three exact-head runs completed success. No cleanup/lifecycle
action performed. Awaiting user confctl integration direction.

## Confctl integration approval

User replied “merge” to the explicit confctl/master merge request. Approval
covers confctl/master; no config pin update, release or deployment added.
Preparing reviewed d8ab7d4 integration at fresh default outside repository claim.

## Confctl integration complete

User “merge” approved confctl/master in response to concrete ready result. Lead
freshly checked unchanged single-commit full series/diff, no obsolete streams or
migrations against final review. Fresh fetch before preparation and inside claim
kept default ff5e017; feature head remained d8ab7d4, clean target/worktree, no rebase.
Prepared detached confctl-merge checkout with documented Nix shell/gems and active
installed/signed hooks outside claim. Bootstrap took longer for local gem setup,
completed0 with existing nonfatal RubyGems platform warnings; no hook bypass.

Claim92a761f8-fc14-4ff5-939f-5ecabe702f6f briefly waiting then held19:18:34UTC,
authoritative state checked before mutation. Ordinary ff-only merge, hook result
inspection, non-force SSH push and exact ls-remote proof:
refs/heads/master=d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49.
No uncertain effects or hook failure. Authoritative own held state checked,
released19:19:34UTC, resulting released state verified before bookkeeping.
All earlier green final-head CI/test/review receipts apply to this unchanged head;
no source/input change warrants repeated full checks. No claims remain for C.

Feature ref/worktrees retained. No config adoption/version release/deployment or
session lifecycle/cleanup performed. Next optional authorized scope would be
updating confctl pin in both configurations; not part of this merge instruction.

Current integration scope recorded from user continuation of the explicitly named
two configuration targets. Lead will merge verified adoption under separate short
claims. No extra approval prompt needed for this same continued scope.

D6 accepted: confctl is unchannelled root input, generated root update owns it.
A2/B2 released, exactd8ab7d4 source only, all nginx4077fb98/ref/nested siblings
unchanged, one new commit/repo preserving merged history. Semantic/hook checks and
new pinned mapping smoke only; no source suite/fleet rebuild repeated.

A2/B2 complete generated commits: A2828c390..bf19f6aacae7f57c8bd06746ff10481b242baf2f,
B272c18d8..fadb89a3f828bc98ea75aa5fcd8de953390c15e2. Both new diffs3+/3-
flake.lock only, exact confctld8ab7d4/hash/timestamp, every sibling/nested/follows
and original attr identical; full nginx4077fb98/ref unchanged, flake/workflows
byte-identical. Required hooks/diff checks pass. Read-only updated-tool smoke
running; feature publication/Git window release pending owner. Cumulative
initiative histories include prior merged pins unchanged. Independent general
mechanical history assessment assigned reviewer0 retained Sol/xhigh; packet
[adoption-review-packet.md](adoption-review-packet.md), no substantive review repeat.

A2/B2 package acceptance: exact updated wrapper vcxb3mrqcr4yrglwf9fmv7q6gc2igviz
loads source zh2jpdp1hcllnb761v1n61z2yykdkamq, reports exactd8ab7d4. Read-only
input/channel smoke passes, machineNames A110/B11. Feature remote equality
bf19f6aa/fadb89a3 proved, source clean, commands quiescent, Git windows released
to lead. No source-suite/fleet checks repeated. Comparison captures saved.

A2/B2 review accepted, no findings; exact new+cumulative ranges, independent
semantic/wrapper/NAR/remote proof, no obsolete/repeated streams/migrations, docs
placement preserved. See adoption-review.md. Lead freshly checked same two tiny
diffs and full cumulative history against reviewed heads; ready for integration.

## Adoption integration complete

All checks/review finished outside claims. Clean fresh adoption target checkouts
with active hooks prepared before ownership. Reviewed new/cumulative series and
tiny final diffs rechecked, no drift/rebase/merged-history rewrite.

B2 claimc58d63cd-642c-4d89-a5ce-501d22a6996a held19:33:24, fresh base72c18d8,
ordinary ff-only merge/hooks/non-force SSH push; exact remote master
fadb89a3f828bc98ea75aa5fcd8de953390c15e2 proved. Own held state checked, released
19:34:11UTC and resulting released state verified before other work.

A2 claim2d6e19fd-5ee1-4277-8b65-2bec502e6c1f briefly waiting, held19:34:25 verified,
fresh base828c390, ff-only merge/hooks/non-force SSH push; exact remote master
bf19f6aacae7f57c8bd06746ff10481b242baf2f proved. Own held state checked, released
19:35:29UTC and resulting released state verified. No unfinished/uncertain command
or hook effects, no remaining repository/machine claims. Source/provider all-green
CI reused exactd8ab7d4, config adoption semantic/mapping/hook checks and independent
history gate passed. No workflows dispatched. Tool adoption needs no activation.

Original nginx deployment list/commands unchanged in handoff. Operator may deploy
those21systems separately; no fleet activation performed by this session. All
owned check/watcher sessions quiescent. Feature refs/checkouts retained and no
cleanup/lifecycle operation requested/performed. Tracking remains normal active
session records; no extra tracking-only commit required by short-session cadence.
