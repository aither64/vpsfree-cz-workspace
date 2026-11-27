---
lifecycle: archived
---

# 2026-11-24-monitor-session-ownership

## Status

- **Administrative archive recovery, 2026-11-27:** the user explicitly directed
  repair and archival, including bypassing the blocking checks. A fresh installed
  `dev-session archive-check` now passes **6/6**, with zero blockers and local
  monitors quiescent. Normal explicit archival is the next action.
  See [recovery evidence](archive-recovery.md). This supersedes the earlier
  readiness-only restriction; no rollout or configuration integration resumed.
- **Rolled back and released, 2026-11-27 11:00 UTC.** At the user's direction,
  the aitherdev running and boot-selected system were restored to the exact
  pre-rollout system (`109d789f`), without reboot. Health and session-service
  checks passed. The coordinator confirms the original claim is `released`.
  The separate, already-integrated workspace bridge remains selected and
  unarmed; the original request is unchanged. Do not resume the rollout or
  acquire a new claim without direction. The final MCP helper was not activated,
  and no pending configuration pin was merged.
- **Archive readiness, 2026-11-27 15:46 UTC:** `dev-session archive-check`
  passes 5/6 checks; the only reported blocker is `conversation` (`Pi runtime
  scope mismatch`). The [archive-readiness diagnosis](design.md#archive-readiness-only--one-naturally-empty-pi-member-current)
  traced it to a single unfinished team member with a live runtime mapping
  but no persisted history. The selected runtime has no eligible member-only
  detach/removal or persistence-only recovery. Follow-up at 16:06 UTC on the
  newly selected profile reproduced 5/6 and proved an existing first-input
  reservation. The sender-side input was accepted, but no matching recipient
  receipt established acceptance or non-delivery. The installed conflict
  recovery does not cover that same-ID state. Do not resend or substitute a
  readiness prompt. Native unload retains the supervisor's member mapping,
  so it cannot by itself make a local record move safe. No member, records,
  worktrees, or services were changed and the session was not archived.
  Recovery requires settling the original delivery and the member's live
  ownership without replay. The prior aitherdev claim remains released.

| Package / deliverable | Owner | Acceptance | Status / next evidence |
| --- | --- | --- | --- |
| Trace Codex ownership and Pi monitor/result paths; [design](design.md) | architect0 | Separate reproduced mechanisms from historical unknowns; disposable regression brief | Assigned 16:35 UTC; accepted design 16:44 UTC |
| C: Codex diagnostics, source validation, real adapter regression | implementer0 | Accepted design; exact authority, no dispatch on invalid/denied cases, stable identity and delivery checks | Assigned 16:44 UTC; quick-check handoff 17:01; remediated 17:10; native evidence accepted 17:21 UTC |
| D: Paired aitherdev rollout brief and helper cutover gate | architect0 | Scope, matching pins, guarded system/profile order and release proof | Brief accepted at 21:48 UTC; checking supported cutover options |
| R: Runtime branch refresh onto current `master` | implementer0 | Patch-equivalent rebase, focused checks, publish only feature ref | Accepted and published by 21:49 UTC; exact-head CI passed by 21:59 UTC |
| P-config: configuration channel pin | implementer1 | Hook-safe registration, exact published runtime, confctl-generated lock, paired check | Published and quick-check evidence accepted by 21:58 UTC |
| P-workspace: user-profile runtime pin | implementer0 | Independent registered worktree, exact nested runtime input, paired check | Published by 21:53 UTC; quick checks and paired check passed |
| A1: refreshed managed application and native verification | implementer0 | Exact published workspace/runtime, three disposable cases; no profile or system changes | Assigned 22:01 UTC; accepted 22:06 UTC |
| D2: managed helper refresh design | architect0 | Use installed compatibility contract and ordinary source-owned cutover; preserve effects | Accepted 2026-11-25 08:04 UTC |
| D2: runtime compatibility epoch and focused tests | implementer0 | Older helper replacement via ordinary 2→3 switch, current 3→3 live path retained | Final review at `689572ab`; docs-only finding fixed and accepted at published `871c6447` by 08:21 UTC |
| P2: final user-profile pin | implementer0 | Replace provisional pin with published `871c6447`; one generated pin commit | Published `9fc8f8ae`; paired checks against provisional D/F passed; accepted 08:26 UTC |
| A3: final application build and monitor behavior | implementer0 | Verify target sealed package and three native cases on epoch 3 | Released 08:26 UTC; D4 process cutover remains separate |
| A2: provisional exact configured system artifact | implementer1 | Exact aitherdev build only; no activation, machine claim or live writes | Build passed; artifact includes drift from live baseline and is not approved for activation |
| D3: avoid unrelated live system drift | architect0 / implementer1 | Two generated pin projections on exact live and current master bases; prove equivalent deployed feature lineage | Brief accepted 08:17 UTC; live base control reproduces installed system; final pin generation released 08:22 UTC |
| D4: quiet process cutover verification design | architect0 | Minimum faithful disposable switch through stock worker | Brief written; refresh exact source/target outputs after rebase |
| R3: rebase the two runtime commits | implementer0 | Full range-diff, patch IDs and focused checks | Accepted and published 2026-11-26 10:54 UTC at `2a1d58df`; exact-head CI running |
| P3: regenerate the paired workspace and config pins | implementer0 / implementer1 | One exact runtime SHA; keep live-baseline deployment and master integration config projections distinct | Workspace published `94d89fc5`, config D `3637ae47` and F `ef407ce3`; paired checks passed; rollout review assigned 11:03 UTC |
| A4: exact rebased application verification | implementer0 | Build immutable composed package and run three disposable native cases | Accepted 11:04 UTC; all three passed |
| D4: refreshed quiet cutover fixture | implementer0 | Disposable stock first switch, preserved root, actual replaced helper | Accepted 2026-11-26 12:07 UTC. Exact 2→3 guest switch, zero participants/children, actual helper/schema and retained history checks passed. |
| A5/A6: exact live-baseline system build and registered generation | implementer1 | D realized, rooted, and registered with normal hooks; verify no unrelated system drift | Accepted 11:39 UTC; generation `2026-11-26--12-37-01` on exact D. No transfer or activation. |
| Rollout baseline refresh | architect0 / implementer1 | Confirm final paired pin and disposable cutover adaptations against advanced masters and selected source | Assigned 2026-11-26 10:49 UTC; later F4 review accepted |
| D5a: selected-source bridge transaction | implementer0 | Exact owner/no-start, durable exclusion and recovery; original-page confirmation; quick checks and review | H `25519802` reviewed: no Blocking, two Important. B asset cache key and terminal-vs-cleanup confirmation remediation assigned; one combined amend pending |
| D5b: unchanged readers and bridge composition proof | implementer1 | Exact O/T readers, then smallest disposable stock O→B→T sequence | [Composition plan](verification/d5-compose-plan.md), exact-O fixture layout and guest HTTPS+serving-asset control runner prepared. Static only; no VM yet |
| D5c: bridge integration/release lineage | architect0 / implementer1 | Exact dated buildable B artifact and complete deployed-input ancestry while keeping D and T unchanged | K `e0858cb8` reviewed; browser baseline refreshed locally to K′ `589347ee`. No selection, push or default integration; blocked by D5d |
| D5d: noninteractive owner delivery | architect0 / implementer0 | Independently authenticate local operator in stock site; exact claim acts as scope, not caller identity | Rejected at 19:26 UTC: stock project commands can share operator UID and namespaces. Draft frozen, not wired or committed |
| D5e: one-shot privileged startup repair | architect0 / implementer0 / implementer1 | Root publishes exactly one original-request grant, serving bridge alone writes; no listener or restart of native daemon | Final H `9044ec0d` and K `5ba7a171` passed quick/provenance checks and standalone final review. Exact disposable build/guest pending. Root SSH read-only returned UID 0 + active D |
| F5: integration-only config refresh | implementer1 / independent reviewer | Fresh default, exact generated pin, typed mapping and D lineage; preserve registered D | `ed66ec29` on `2f470c0f`, [exact range](verification/f5-review-range.diff); independently accepted D→F5 deployed feature equivalence. Integrate only after verified T; never activate F5 |

## Next actions

- Re-entry 2026-11-26: user directed continuation and another rebase. Fresh SSH
  master tips are runtime `e3102d0b`, workspace `56aadac58`, config `0b648b23`.
  The selected epoch-2 profile is now `3y9ns5…`; the running helper remains
  `gh680…` and the system generation is unchanged. The previous candidates and
  cutover inputs are historical evidence, not deployable substitutes. Rebase the
  reviewed runtime series, then regenerate both pins from the exact new revision.
  Runtime rebase completed at `2a1d58df7c3bb845da4d286ef38989bae01da4a0`.
  Both range-diff entries and stable patch IDs match; scoped Ruby/Go and tagged
  fixture/compile checks passed. [Exact-head CI](https://github.com/aither64/dev-workspace/actions/runs/45805531497)
  passed. Workspace pin `94d89fc5` and config D `3637ae47` and F `ef407ce3`
  agree on that SHA and content hash. The final A4 application artifact
  `/nix/store/0qmdcq0mg6rdzjsfx5jrinrbdj066nfc-dev-workspace-0.2.0` passed
  the three exact-native `passed`, `busy`, and `lost-reply` cases. The final
  reviewer cleared all four ranges and confirmed D→F deployed feature lineage
  equivalence for the ordinary schema-2 claim (not whole-system/patch-ID or
  legacy-certificate equivalence). No source findings, obsolete history,
  repeated streams or migrations. D is evaluated but not realized; its diff
  from the live recursive derivation graph is limited to metadata, aggregate
  etc, activation wrapper and toplevel. A5 was released for the exact D build.
  D4 has exact inputs. Under the user's approval for the three `master`
  targets, the runtime and workspace pin were fast-forwarded and SSH-verified
  at `2a1d58df` and `94d89fc5` on November 26. The original short repository
  claims `dcacfe81-7958-4556-a823-2e5525f079f5` and
  `ec1f3d45-bd14-49b4-a619-42d9d1948dff` both returned `released`.
  Configuration F integration remains sequenced after verified activation on D.
  D is now built, rooted and registered (see below). Both exact candidates
  survived verification after one restoration each; keep the session-owned
  Nix output links `verification/a5-system` and `verification/d4-a4-target`
  through the rollout. The final isolated stock switch passed: exact selected
  epoch-2 source → epoch-3 target, unchanged native ELF/settings, original guest
  operation `6246feb5-a56a-4b69-b378-670d3c3d9d39` completed with zero participants
  or children. Verified the new daemon and actual target MCP child, unchanged
  root/roster/history, `local|ci` discovery, and invalid-start predispatch refusal
  with no operation, command or wake. Final evidence: `verification/d4-guest.y0mKGTin.log`,
  build `/nix/store/q4jijr8jvji2d6dgg69yf9nmsrijh8yl-vm-test-run-monitor-helper-d4-quiet`.
- Live readiness at about 12:10 UTC: portal health passed on its local socket;
  the actual Codex daemon still runs the unchanged 0.165.0 ELF and retains
  the old helper. Read-only paginated native inventory for that stable process
  returned 109 idle and **6 active** threads. Not a quiet window. Do not take
  the machine claim or activate either half yet; the stock worker could pause
  or interrupt active work. At the next quiet window, recheck admission and
  unresolved effects, the exact rooted targets and registry, then deploy D,
  switch profile, verify live results, integrate F and release. No host mutation
  or machine claim.

- Independent high-risk review by retained `reviewer0` (saved Sol/xhigh) on
  `df3a66d4`, general/architecture/scope/risk. [Packet](review-packet.md).
  Confirmed no obsolete history, repeated input streams or migrations.
- The lead inspected direct fixes for all findings on `0c714b16`: decode the
  native acknowledgement correctly; fail closed on a known duplicate root in a
  partial inventory; remove redundant foreign-ID preflight and assert service
  refusal; qualify recovery and uncertainty in the portal docs. Scoped Go tests,
  tagged fixture-unit tests, tagged compile and `git diff --check` passed.
- [Hosted Check run 45447644242](https://github.com/aither64/dev-workspace/actions/runs/45447644242),
  attempt 1, completed successfully on `0c714b16`. Latest runtime `origin/master`
  seen at `d15735fa`; refresh and validate the feature before integration.
- Independent review of the three published heads completed by retained
  `reviewer0` (Sol/xhigh, general/architecture/scope/risk); see
  [rollout packet](review-packet.md). No blocking or important source findings.
  Reviewed complete exact ranges; patch-equivalent runtime refresh, matching
  supported pins, no obsolete history, repeated streams, or migrations.
  The serving-helper cutover remains a blocking deployment gate, not a source
  finding. Refreshed dependency graph requires new exact-package native evidence.
- The user explicitly confirmed deployment, activation, merge, and release
  after the three `master` targets were named (`dev-workspace`, `workspace`,
  `vpsfree-cz-configuration`) and directed us to solve the MCP helper refresh.
  Treat this as approval for the reviewed lineage and managed cutover required
  for this fix, not for unrelated interruption or any command/session replay.
- The installed update/reconcile paths preserve the old helper for a package
  path-only change. D2 uses the existing cutover by declaring the compiled
  helper compatibility boundary, not a new operator command. It preserves
  native roots and source-owned recovery. The exact prior host predicate
  recognizes 2→3 and the focused checks passed. Independent review cleared the
  source after a documentation clarification: a capable predecessor can use
  maintenance even without `--enable-maintenance`, so a verified quiet window
  is required. The published epoch-3 head is `871c64476a0e10c37ec1c62099dde2a5ef5fcf2c`;
  [CI](https://github.com/aither64/dev-workspace/actions/runs/45575485816) and
  final pin prep are underway. Process-level acceptance remains. No restart,
  claim or activation. P2 workspace is published at `9fc8f8aeb819dacd17438278e3fd7549c7a6c75b`;
  paired validation passed against D `1bd660c3d86a752727f1631ac894073e85b78358`
  and F `2ac40b30cf2e5449e4473a7bc864b48a533632eb`, pending final D3 acceptance.
- Deployment re-entry 15:26–15:34 UTC: user directed deployment, then configuration
  merge only after live verification. Both current system links, the selected
  profile and the rooted target hashes were unchanged. Read-only inventories
  found 3–5 active Codex threads, with 4 at 15:35 UTC. Portal health passed. No quiet
  window was established; no production dry activation, service restart,
  roster edit, watchdog adoption, configuration merge or machine reservation.
- The user subsequently confirmed that managed interruption is expected and
  asked about resuming interrupted threads. Use the installed source-owned
  pause/resume workflow rather than requiring zero active Codex turns. Verify
  accepted continuation for each captured lead/member not explicitly stopped;
  recover any uncertain delivery by the original maintenance UUID. This does
  not authorize starting substitutes for commands, monitors or child agents,
  or bypassing unknown effects and other maintenance admission fences. The
  exact quiet fixture proved helper replacement but did not exercise live
  participant continuation.

## Live deployment, 2026-11-26

- User authorized managed interruption/resume and asked to continue until done.
  Source admission and original-work ownership checks remain in force.
- Held schema-2 aitherdev claim `59fef080-c78c-4fd2-92e1-d8c1286cb4b7`; typed
  mapping verified at D `3637ae47`. Exact generation dry activation passed,
  then confctl switched without reboot; both live system links resolve to the
  reviewed D toplevel and both system health checks passed. Evidence:
  `verification/live-system-{dry,switch}.log`.
- The one ordinary epoch-2 source switch was invoked as user unit
  `monitor-fix-aitherdev-switch-20261126.service` (invocation
  `2844130c7fcf44faadbaa48d952fb527`). It exited 1 before maintenance admission:
  `preserved Pi creation requires unchanged native registration and maintenance`.
  The system is on D; profile switch refused. Hold the original machine claim
  while diagnosing the creation fence; do not clear any foreign records, stop
  a native process, or merge F4 before live verification. Read-only inspection
  with the selected package confirmed one intentionally preserved, failed Pi
  creation: the immutable request, receipt, and creating binding match, and
  native Create did not begin. The user authorized discarding only that original
  request, superseding Retry creation. The selected build exposes neither a
  discard operation for this schema-4 failed Pi receipt nor a matching normal
  deletion/recovery context: no session tracking, native root or removal journal
  exists. Do not retry, fabricate records, or remove files. No new maintenance
  operation or resume sends were issued. Portal remains healthy.

- D5 design complete: [design.md](design.md#d5--discard-one-never-materialized-pi-request-without-retrying-it)
  describes a request-owner discard in a compatible epoch-2 bridge, with durable
  replay and compatibility checks. D5a owner transaction feasibility assigned to
  `implementer0` and D5b independent disposable reader compatibility assigned to
  `implementer1` around 16:44 UTC. D5b accepted: exact current and target
  readers admit the existing compact cancelled mapping; original/stale retry
  fixtures return refusal without a worker, receipt or tracking change. D5a
  owns clean `worktrees/2026-11-24-monitor-session-ownership/dev-workspace-discard-bridge`
  (branch `2026-11-24-monitor-session-ownership-discard-bridge`, base `e3102d0b`).
  D5a design settled: one pending marker checked by the portal, CLI and host;
  authenticated recovery must remain available after a crash. Implementation
  released at 17:01 UTC. First checkpoint: marker reader and CLI/host guards
  drafted, including the raw-lock Pi tracking path. Focused Ruby reservation
  (20 tests) and host (1 test) checks and the Go session marker tests passed.
  A disposable stock handoff now reproduces separate preparation/creation
  attempts and the matching failed receipt, journal and binding before runtime
  start. The empty attachment selection left the catalog unchanged in that
  fixture and focused `TestPiDiscard` checks passed. The architect settled
  upload admission in the existing file window: prove stock-writer provenance
  and empty immutable selection, and refuse if either receipt goal could match
  a retained legacy upload. The pure bridge predicate passed stock legacy-wire
  fixtures for both fields, with catalog bytes unchanged. The draft discard now
  runs behind the original owner action in disposable state; focused checks
  exercised wrong Origin/attempts, successful terminal replay and startup
  recovery after intent, selector retirement, mapping and completion. No live
  eligibility proof. The prior B-only browser path required a human click.
  The user explicitly delegated the original discard and declined a separate
  confirmation. Do not ask for one again. The architect is designing a narrow
  authenticated operator path; do not select the browser-only bridge.
  Focused restart/uncertain-sync/race and browser-contract checks passed. H
  is clean at `255198028181dfeacb19004b82ef58838a776c1f`; full binary patch and
  pure-tree proof are in the [review packet](review-packet.md#d5-temporary-pi-request-discard-bridge).
  Exact composition K `e0858cb839ef0f74f36ed810273f82ff070be979` passed
  source/tree/immutable-subdir evaluation. `reviewer0` (GPT-6.2 Sol/xhigh,
  General/Architecture/Scope/Risk) reviewed H/K and found no Blocking, no
  obsolete history/repeated pin streams and no migrations; docs are correctly
  placed. The two Important findings are O's cached browser asset key and
  confusion after final marker unlink succeeds but its directory sync fails.
  Both assigned to `implementer0` at 18:40–18:42 UTC. B must distinguish a
  durable cancellation from unconfirmed cleanup; a real B exact-original
  cleanup confirmation, not permissive stock admission, gates T. Packaged
  guest verification was prepared for the browser baseline. The cache and cleanup
  fixes are folded into clean H′ `26c46a909f9384ed2a88fa005b7c754a430e1444`;
  they and the dated composition are a baseline for the operator path, not a
  deployment candidate. D5d [site blocker](design.md#d5--discard-one-never-materialized-pi-request-without-retrying-it):
  stock project commands can use the same UID and namespaces as the trusted
  operator. A held claim proves ownership of the reservation, not the caller
  making the connection. No existing independent noninteractive ingress was
  found; no approval or click is being requested. Three draft paths remain
  unstaged at H′: `libexec/workspace-host`,
  `portal/internal/web/pi_creation_discard.go`, and new
  `portal/cmd/workspace-portal/pi_discard_operator.go`. The listener was not
  wired or started. No bridge selected, request cancelled, second profile
  attempt or new claim. The original aitherdev claim remains held. Bounded
  one-off host repair recheck: stock suspension refuses this unfinished
  creation before recording a hold. A compatible profile switch neither joins
  the old portal before activation nor passes a single-request action and
  transition-lock FD to its activation subprocess; it is not a crash-durable
  offline repair boundary. No live mutation and no additional confirmation
  requested. Do not pursue a generic endpoint for this one request.
- D5e replaces that blocked design with independent root scheduling and a
  selected-portal startup-only writer. Final H/K fix the unrelated-portal
  startup and retained HTTP authority findings; browser files match O and an
  old valid-shaped POST fails without effects. [Independent final review](verification/d5e-standalone-review.vYbRc9/result.md)
  ran as standalone installed `gpt-6.1-sol`/xhigh, General/Architecture/Scope/Risk
  (retained `reviewer0` could not execute identity checks). Exact final H/K:
  no Blocking/Important, no obsolete/repeated history or migrations; correct
  documentation placement. Accepted deferred stale internal POST comment to
  preserve exact reviewed build inputs. Same reviewer accepts the F5 feature
  lineage. Exact B/publisher artifacts realized; retained-source and closure
  proofs passed after correcting two fixture expectations. The first VM lacked
  stock Pi substrate. The corrected stock-Pi VM passed O seed and O→B join
  but failed at its first privileged test grant publication, before discard.
  See `verification/d5e-stock-pi-guest.k9iENV.log`; bounded diagnosis assigned
  at 08:22 UTC on Nov 27. The refusal was the expected unprivileged negative;
  the runner had not captured publisher stderr. The corrected exact guest
  passed in 542.49s, including cleanup/replay and actual T helper proof
  (`verification/d5e-stderr-guest.NKglcq.log`). Workspace master advanced to
  `00edc4c9` with identical dated subtree; short merge claim released.
- Live O→B completed at 08:50 UTC, exact B serving and O portal joined, no
  Codex restart. The first exact root grant was published, but B's portal
  startup refused before intent. All five original selectors remained
  byte-identical; no marker, audit, mapping, runtime start or request retry.
  The refusal grant was retired exactly and unarmed B portal restored.
  The original Pi claim owner is valid and held; the private bridge check
  wrongly requires a Codex thread. The [bounded correction](design.md#d5e-follow-up--authorize-the-original-retained-pi-claim-owner-bounded-correction)
  was implemented as H+ `3965b0f3` and packaged as additive K+ `79478c47`.
  Focused checks and independent [delta review](verification/d5e-plus-review.XYEO25/result.md)
  passed; no repeat VM run at user's direction. K+ is verified remote workspace
  `master`, short repository claim released, exact B+ realized, selected
  unarmed and verified serving; prior portal joined and native unchanged.
- Live B+ managed startup with one new exact package/token-bound grant
  (`56ddf61f12a04b24bcd3eae506ee1ba2`) also refused before intent at 10:03 UTC.
  All five original selectors are still byte-identical; no marker, audit,
  terminal mapping, or retry. Exact B+ grant retired; unarmed B+ portal restored
  (`55f99f5750f241ea9cdfc7489b6d10d1`) and socket available. Native unchanged.
  No grant remains. The generic hold does not identify the failed predicate.
  Read-only triage dispatch returned refused/unknown; no further retries or
  package changes. D and the original machine claim remain. F6 `eb6e1d41`
  is integration-only after verified T and supersedes F5 on current master.

## Rollback and release, 2026-11-27

- Restored the exact retained NixOS toplevel from `system-337-link`:
  `/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`,
  configuration `109d789f0a4ee875f8bd27a0b72ea76c38ee234a`. Dry activation
  passed. The first attempt lacked a transient-service PATH and had no switch
  effects. The next selected the exact toplevel but stopped late when its
  root login disappeared from logind. A supported same-toplevel switch in a
  persistent root SSH login completed the pending system activation with exit
  zero. The prior failed unit receipt is retained; no command remains running.
- Verified the running and boot-selected system links, exact configuration
  metadata, no reboot, drained activation queues, system state `running`,
  firewall active, portal health, unchanged portal and native invocations, and
  unchanged original request. No grant remains. The live workspace profile
  stays at the integrated B+ package; no unsupported profile downgrade or
  public history edit was performed. Fresh remote proof includes the
  equivalent baseline pin and exact B/B+ ancestry, not whole-system equality
  with current config `master`.
- Authoritative release: `59fef080-c78c-4fd2-92e1-d8c1286cb4b7` is `released`.
  Evidence: [activation log](verification/rollback-aitherdev-20261127/complete.log),
  [lineage](verification/rollback-aitherdev-20261127/lineage.txt), and
  [release status](verification/rollback-aitherdev-20261127/released-status.json).

## Historical activation inputs (before rollback)

- Runtime master `2a1d58df`; workspace master `844ac4db` retains integrated pin
  `94d89fc5` and passed the paired check. Exact reviewed D
  `3637ae47905dff5762e43dfd0c6e3b9a7f9a8444` is the clean registered config
  feature. F4 `676816f9734e23d2f710ec80e34621e00c38d070` on configuration
  master `1e43e2e18c85cf1fc63f31327d1f8e5eb953eab8` supersedes F `ef407ce3`.
  Independent delta review confirmed identical pin patch and D→F4 feature
  equivalence, with no remaining source findings, repeated pins or migrations.
  F4 is integration-only; do not activate it.
- Confctl generation `2026-11-26--12-37-01` resolves to
  `/nix/store/z16l3iq5sa5l1f8mb4wqiyd9b7n8i3iv-nixos-system-aitherdev-26.05.20261121.94c3211`
  (NAR `sha256-oXKNgGQYrcnZj3GCA9BYvsgJyG8uSLF/e/sAovO2i/M=`). Actual L/D
  system and user unit trees, `sw`, kernel and initrd match. No dry activation.
- Exact epoch-3 target `/nix/store/0qmdcq0mg6rdzjsfx5jrinrbdj066nfc-dev-workspace-0.2.0`;
  exact epoch-2 switch executor `/nix/store/3y9ns5h3raj9zszrwcr5pgvf9gng8q4b-dev-workspace-0.2.0`.
  Live helper `gh680…` is process provenance, not a switch executor. Older
  `py81…`, pin heads and artifacts below are historical only.

## Repositories

- `dev-workspace`: registered branch `2026-11-24-monitor-session-ownership`,
  now published at `46a547dce36e5f341b737e378fb721f8ac770f8e` on
  `d15735fa9695aaed3cb45c073e01b8ef4e6904c8`. Range-diff and stable patch ID
  match prior `e61d3b7e..0c714b16`; focused checks pass. Baseline codex-web
  changed, so the original exact-build native test evidence remains scoped to
  `0c714b16`. [Rebased Check run 45494845460](https://github.com/aither64/dev-workspace/actions/runs/45494845460)
  passed at the exact head.
- `workspace`: published pin `83c20c7c700bc5f6db910cb79ffe0dbc62d9d31d` on
  `c6534049f84fea7a017e9ad8828a96236ba8c748`. Only the nested runtime URL and
  lock fields changed; extension and follows remain unchanged. Exact metadata,
  parse and diff checks passed.
- `vpsfree-cz-configuration`: registered feature worktree under
  `worktrees/2026-11-24-monitor-session-ownership/`, published pin
  `d4e80199ceca98ea63375dffc6f6a056beb13dbc` on `1c81a4d7`. Declared hooks
  and exact metadata checks passed; only aitherdev's runtime input changed in
  the evaluated machine map. The paired deployment-contract check passed,
  with both runtime SHA and NAR hash agreeing. This does not prove an
  installed system, selected application, or serving helper.
  Initial tracking commit `aaf86bc2e`.

## Phase checklist

- [x] Verify investigation binding and assign architect.
- [x] Reproduce a Codex rejection path at the adapter boundary; historical caller unknown.
- [x] Confirm Pi lead capability gap and document active-parent fallback.
- [x] Commit narrow fix and boundary regression; focused Go checks passed per owner.
- [x] Independent review; inspect and quick-check narrow remediation.
- [x] Exact managed candidate build and three disposable native cases.
- [x] Feature branch published; verified remote head.
- [x] Hosted CI succeeded for the original candidate.
- [x] Rebase and publish runtime fix and both pins; paired contract and hosted CI passed.
- [x] Independent three-repo rollout review; source cleared, live cutover blocked.
- [x] Exact refreshed application artifact and three disposable native checks.
- [x] Explicit integration and deployment scope confirmed by user.
- [x] Loaded and verified exact provisional aitherdev system artifact.
- [ ] Prepare final system artifact for the selected compatible rollout lineage.
- [ ] Supported helper refresh, activation, integration proof and release.

## Results

- The provisional config `d4e80199` build passed from its clean captured source
  (`confctl` local generation `2026-11-25--09-04-48`, output
  `/nix/store/2mbi1fj7k5a1rdnqvzqxyfx3ck1h4sv5-nixos-system-aitherdev-26.05.20261122.0dc498b`).
  This is not the final system artifact. Live configuration `109d789f` uses an
  older NixOS baseline and system Codex CLI 0.170 versus candidate 0.171. The
  kernel and initrd match; DBus restart triggers differ. This system CLI is
  independent of the selected workspace native 0.165. No copy, dry activation,
  deployment or claim was performed. D3 proved exact live source reproduces
  the installed system, and actual build-plan source paths show llm-agents
  differs across the baselines despite equal higher-level input metadata.
  Use the exact live baseline for the proposed deployment projection and
  fresh config master (`5b68d121` at first check) for integration, not A2.
- Current Pi shell lacks both `DEV_SESSION_*` variables and has no `dev-session`
  on its default PATH. With the reported package's CLI added to PATH,
  `dev-session current` matches the trusted binding for this investigation.
- Normal-cache dry-run cleared the initial offline preflight. Managed build of
  composition `aaf86bc2e60bc490c70e366b80f9892b8839fe8e` with exact runtime
  override `0c714b165ac01ad6f27db299f4a23757297d12f8` produced
  `/nix/store/kl10c9z429njx857i3mrbp15vn86nzmi-dev-workspace-0.2.0` without
  selecting it. Its pinned `codex-cli 0.165.0` and fake provider were used for
  `CGO_ENABLED=0 go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^TestNativeMonitorOperation$/(^passed$|^busy$|^lost-reply$)' -count=1 -failfast -v`
  from `portal/` with repository-pinned Go/Git/Ruby/Node. All three passed
  (19.343s total): one command per case; correct launch/origin and immutable
  terminal receipt; exact idle lead wake and busy steer; stable-ID retry
  retained the original launch, changed payload refused, and lost-reply
  reconciliation produced one matching history input. Other tagged modes,
  actual native compaction, and live package reconciliation were not tested.
- Refreshed managed application built from immutable workspace `83c20c7c` and
  nested runtime `46a547dc`: source `/nix/store/19yrhr2ribnv9zv11jglxsm2d6c76kgp-source`,
  output `/nix/store/ygh36g1npqhv1aj4s3vx6yk1zk8k8bvr-dev-workspace-0.2.0`.
  No lock writes or package selection. The same targeted `passed`, `busy`, and
  `lost-reply` test command passed against that output (19.440s), including
  exact-root receipt/history, single execution, unchanged-ID retry, and
  reconciliation without a duplicate wake. The candidate uses the same pinned
  native Codex 0.165.0 ELF. This is disposable acceptance, not live cutover.
- The investigation roster is Pi-backed and native team assignment works.
  The Pi lead has no `monitor_operation start` tool: the conversation callback
  filter rejects the method, and the Pi utility tools are status/report only.
  Native team delivery does not establish monitor registration or lead wake.

## Open questions

- Historical MCP caller metadata unavailable; no direct evidence of changed
  native caller or compaction. Tested absence of shell variables in the
  disposable lead request does not cause denial.
- Pi does not support durable lead registration or wake through this surface;
  investigate only, no Pi feature expansion in package C.
