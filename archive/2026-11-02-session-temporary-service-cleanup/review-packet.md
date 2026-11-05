# Affected native Job review: committedee3f1fdd (current)

SAME retained reviewer0 Sol/xhigh/read_only, affected GENERAL and RISK/compatibility
follow-up before new long native/package verification/publication. All intended
source changes committed and quick checks pass. Reuse unaffected earlier content,
architecture/scope/UI conclusions and original reports; no new framework/design.

Runtime exact range c2182254d29c4175c3e9fe4267e5a92dd1da6b79 →
ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f,
treee52d2aa3da60fcf2e5d563b7606c98e7ef844180. Complete LOCAL-only clean3series:
UI19dd03b79a2997098934afafbe70c63b978c1ca7,
coref7add7cea8a836810d32688ef2d1cf4cc011af19, dependentee3f1fdd.
UI/dependent range-diffs equal published7302; core changes ONLY2files71+/3-
(production5lines + native-format/default and strict regression fixtures69lines).
Whole source49files4216+/127-. Fixupbb87e2e9 folded; exact fixup/final trees equal;
old7302/fixup/final refs retained under refs/session/<slug>/native-job-*.
Source `/nix/store/8ygzal9j12xj6x600ws7yrhgn1ijngx2-source`, NAR
sha256-5mDdLgLQl/XPjIs9Ey5l2UDxWwVKR/VWpNCQwEvqsiw=.
Runtime lock/full9node graph unchangedfa808c04...; no new flags/dependencies/schema/
public API/identity/cgroup/journal/receipt or admission boundary.

## Actual native failure and source clarification

CI41526190428 at7302 settled: fast/package and nativecreation PASSED; archive
passed repaired oldrevive path, then first registered service main starts and
durable registry/resource IDs are observed, but CLI fails 'service manager job
state unavailable'. This is after the expected recovered permission interruption,
not that interruption's failure. No registered cleanup success claim. Actual
logs: tracking/runtime-ci-7302f4dc/{final-run.json,failed-archive-job.log,SHA256SUMS},
native systemd260.2 at3644/3857, first service command5586/error5590. Raw native
Job output was NOT captured; do not invent an observed Job value.

Architect independently froze official260.2 commitf1d0952a and inspected pinned
nixpkgs patches + actual command. design.md 'Native Job formatting clarification'
and tracking/runtime-ci-7302f4dc/systemd-source/ show: no-job D-Bus tuple(0,'/')
is printed as PRESENT-EMPTY Job=; positive IDs decimal; explicit --property already
sets SHOW_EMPTY, missing requested property emits no line. Relevant blocks equal
260.5 source. No --all or liveprobe needed. Missing is not zero.

Product correction normalizes ONLY values.key?('Job') && values['Job']=='' to
internal'0', retaining explicit0 compatibility. Positive canonical decimal remains
pending; unsupported optional whitespace-tail acceptance removed. Missing/null/
bare no-equals/malformed/whitespace/noncanonical values remain unknown, no coercion,
strip or fallback. Loaded InvocationID equality and unloaded/uncertain start
native-job+expected-cgroup absence proof untouched. Job zero alone is not process/
start settlement. Native fixture now emits raw Job= by default, covering running,
stop and retry through existing full service tests. Tests reject missing/bare/
null-text/text/space/leadingzero/tail values, retain registry/phase and dispatch
no stop; positive jobs block loaded and not-found retirement; exact retry settles.

Evidence: ci-remediation.md latest section and
tracking/runtime-ci-7302f4dc/job-parser-{red,focused}.log,
job-parser-consolidated-receipt.json, job-parser-range-diff.txt,
job-parser-final-delta.patch, recorded standalone/aggregate/final smoke commands.
Fixture-only native-format change red reproduces exact first-launch error1/4.
Focused7/118, standaloneallservice32/466(21.91s), aggregateallservice+2badroot34/478
(22.38s), final consolidatedsmoke7/118(1.49s), Ruby syntax/whitespace pass. Lead
directly inspected production/test diff against actual design clarification.
No new user-facing strings; nearby comment and source design provide rationale.

Review exact native interpretation/presence distinction and strict process proof,
test causality/limits, complete owning history/fixup disposition and no-migration
lineage. Report concrete findings, not a rubber stamp; no tests/builds/liveprobes/
source/Git edits or nested reviewer. Save review-native-job.md; oldreports unchanged.

## Current artifacts/pins and later mechanical boundary

All pins/artifacts remain held7302 scope: published workspaced250081c over
tracking-onlybase2e5bc7f (2commits/singlepin; instructionb4c8dc82 patch-equivalent
c474); config4a9be5ba (one pin fromc040). Finalmatchingchecker passed. Lead already
ran installedreadonlyverifiers + fullNAR/managed9node graphs and independent
tracking-only exact merge-tree reconstruction; schema1scope receipt
mechanical-review-proof/certified-refresh.json preserves originalreview bindings.
No deployed range, copy, claim, activation or integration. Appbwq5/system4cbl are
verified7302 artifacts, NOT futureee3 certification. Driver never built/run.

Later PURE generated refreshes to accepted publishedee3 may use the same existing
certified-review exception, actual installed verifier and independently bound full
NAR/subgraphs/ranges/retained accepted reports/migrations/consolidation. No new
source boundary or hypothetical pin is accepted by that statement. Any tracking
baseline refresh needs exact reconstruction; unproved scope requires affected
review. Source publication triggers fullCI, so this affected content review
precedes it; no skip-CI/ref hack or duplicate Ruby campaign. Fresh exact input
checks/native proof still required; previous passes do not certify changed source.
No DB migrations, no new local schema or supported predecessor-state boundary;
ordinary recovery/receipt/Store formats preserved. Default integration approval
remains absent and session lifecycle untouched.

---

# Affected UI lifecycle review: accepted7302f4dc snapshot

Request SAME independent reviewer0 Sol/xhigh/read_only for affected **general and
risk/compatibility** follow-up before new long native verification/publication.
All intended source changes committed, quick checks pass. Preserve prior reports
and reuse unaffected architecture/scope/content lanes; this is a bounded product
UI correction beyond the earlier harness-only fix, so direct lead inspection does
not replace independent affected-lane review. No source edits/tests/builds/probes.

Exact runtime range c2182254d29c4175c3e9fe4267e5a92dd1da6b79 →
7302f4dc961ded7c768733e25ec39e3c603e093b; tree934f92ba1bc27675161f315ae0a8835ff1d7d8f3.
Complete clean LOCAL-only three commits:
19dd03b79a2997098934afafbe70c63b978c1ca7 (UI),
565e28973a106369bc18ee7f3487c359cf9adc16 (core),7302f4dc (dependent).
Core/dependent patches equal prior published3d76; only accepted UI correction
folded into owner. Entire final diff49files4148+/127-; changed since3d76 only
3files81+/6-. Published3d76 and fixupbe0f0b69 refs preserved outside final ancestry.
No DB migration, new schema/API/ownership or consumer boundary; runtime9node graph
and lock byte-unchanged. Source9fsjqqji / NAR
sha256-bILeNLuxVReQbq2RvL2wvgOr5NMmlLTd+8p1mG43gz0=.

Actual CI41518664500: creation native passed; archive reached existing recovery
case then browser freshrevive failed before POST/CLI dispatch. Expected permission
interruption/retry had completed with same61fa... receipt and archived target
(native assertions passed). Captured same-page navigation/no open dialog/no POST.
Raw operation/details callback JSON absent; lifecycle source necessarily preserves
journalExpected=true in completed retained-journal retry. The next registered-
service native subtest was NOT reached; no cleanup-success claim. Static full
failure trace and observed-vs-inferred bounds are in
runtime-ci-3d76f527/archive-lifecycle-diagnosis.md and archive-browser-failure.json.

Deterministic regression executes actual shipped openLifecycleConfirmation,
showLifecycle, details refresh and reconciliation handlers. Before fix fresh
revive + completed historical archive with journalExpected reproduces ['reload'];
active archive completion control already passes. Product fix adds one state
guard: completed historical display does not assign NEW pendingLifecycle intent.
Existing in-flight pending flag still reloads on genuine completion. History,
Options, target proof, failed/incomplete recovery and backend semantics untouched.
Two regressions now pass, including later explicit revive submit. Existing native
browser helper adds bounded16 whitelisted lifecycle snapshots/8navigation paths
and safe final dataset fields within its existing1500ms diagnostic budget, to
resolve the missing callbacks if native verification still fails. No new harness.

Evidence and exact checks: revive-ui-remediation.md,
revive-ui-final-receipt.json, revive-ui-{baseline,regression,package-js}.log,
revive-ui-package-js-result.json, revive-ui-go-{assets,lifecycle-assets}.log,
revive-ui-{range-diff,fixup-range-diff}.txt and final complete diff/metadata.
Baseline2tests1failure; fixed2controls pass; package129Node+10syntax pass16.691s;
BrowserAsset/OperationsNavigation0.103s + exact lifecycle assets0.094s pass.
Lead directly inspected committed3file diff. Native helper changes filtered Ruby
input identity, so previous generic/site check results DO NOT certify newsource;
upcoming actual package checks cover it, no separate duplicate Ruby campaign.

Review actual complete owning history and affected app/test paths, especially
completed history vs real active/failed intent and strict recovery preservation.
Report concrete findings; do not rubberstamp causal claim or waive native proof.
Save review-revive-ui.md; original reports stay unchanged. No nested reviewer.

Current workspace2c5f/config46 pins and built app09qh/system26g4 artifacts remain
HELD at3d76. No future selection, activation, copy, deployment or default integration
has occurred. They are not final7302 inputs. Source publication triggers long CI,
so affected substantive review precedes it. After acceptance, mechanical pins
will be consolidated once again and verified with the installed read-only
workspace-integration-recipe action=verify under the mandatory-review skill's
certified refresh exception, binding retained accepted reports/exact ranges and
new reviewed source, full actual NAR/subgraphs and schema1 evidence. The selected
package integration.json declares existing workspace-pins recipe; its immutable
command parses committed locks, identity and unrelated fields/follows/Nix files.
No new certification framework, legacy job or approval bypass. This proposes
review reuse only for later pure generated pins; no uncreated pin is called
reviewed, and unproved transformations still require affected review. Integration
approval remains missing. Flag an applicability concern if the exception does not
cover the eventual verified pure refresh; do not inspect hypothetical new commits.

---

# Final history and matching-input follow-up packet (accepted3d76 snapshot)

Current committed deliverables and quick checks are complete. Retain reviewer0
Sol/xhigh/read_only and the original independent all-four-lane review in
review-final.md. This follow-up requests independent **general/history and
risk/compatibility provenance** conclusions on the complete final series,
consolidated pin streams and full locked graphs. Reuse unaffected content lanes;
do not repeat a full review merely to confirm the requested narrow fixes.
Report any concrete new serious issue encountered. No tests/builds/live probes.

## Current exact ranges and complete series

Worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/`.
Canonical SSH repositories and target master remain those in the original packet.

- Runtime: c2182254d29c4175c3e9fe4267e5a92dd1da6b79 →
  3d76f527a6b88e9d32c202f729a1a0d673b341f2,
  tree b9f7154cabbd95624dc447d87b855f2b01b33247.
  Complete three commits: UI16e4b98212292446cec28724ac9a62ccfcbdfb56;
  core d9ec31a05074b5f0774fc9cd9114fc74e3691c29;
  dependent3d76f527. Final diff48files4068+/122-.
  Published feature exact3d76, fresh remote masterc218; clean source/index.
- Workspace: ef09cf555332afebafb276e3ae54cc1f5ea6012c →
  2c5f6cdb59995700bc33026c7c1e27e71b4d893a,
  tree1c0c706d7dbacff04e6521bddbbfdbbecda99587.
  Complete two commits: unchanged reviewed instruction
  c474bcc55b04459dd936d2e4d8bea358b2b84184, then ONE final runtime pin2c5f6cdb.
  Final diff4files25+/6-; pin alone2files5+/5-. Unpublished, clean;
  shared masteref09 and origin/master6383e884 remain unchanged. Initial portal
  base6383e884 retained; earlier feature rebase patch-equivalent, no shared writes.
- Configuration: c040c14cdbacc07998700b524996a89306188d7f →
  46e281115294e5d45286b60c8ff862ac287d862b,
  treec6230cc4950d12b357b8d53edb2b193e5b45a514.
  ONE generated confctl pin commit, flake.lock3+/3-, unpublished/clean.
  Base/origin-master unchanged. Generated changelog retained as produced by
  confctl from originalc218 to all three final runtime commits; normal Overcommit.

## Corrections, streams and lineage to assess independently

Original R1/R2/R3 were fixed as requested, committed/focused-tested and directly
inspected, then folded into their owning UI/core/dependent commits. R1 keeps both
existing capabilities required for any retained registration; R2 refuses first
conversation root creation before mutation; R3 updates existing nested nav test.
See review-r1-r2-remediation.md, implementation-b.md and runtime-consolidation.md.

Subsequent narrow CI fixes restore reviewed behavior without design/API/schema/
ownership expansion: d137 error ordering/typed lifecycle boundary/test clock is
folded into core; c850 changes only three browser harness lines to mount actual
shipped count helpers/prelude and document listener, folded into UI. Direct lead
committed inspection and focused acceptance recorded in ci-remediation.md and
browser-ci-remediation.md. Sources/services/public contracts unchanged by c850.

No DB migrations; new local service schema1 is introduced directly. No preceding
service schema was merged, released, deployed or externally consumed. Ordinary
journal/receipt/automatic Store formats preserved. No activation/deployment or
default integration occurred. Exact predecessor fixture remains byte-proven.

Inspect dispositions rather than accepting labels: runtime published312/e29,
their d137/c850 fixups and earlier source refs are preserved outside final series.
Workspace pins252(312),00381(e29) are outside final ancestry under retained refs;
final series has only2c5f6cdb selecting3d76. Config7b6d(312),abee(e29) similarly
retained outside final ancestry; final has only46e28111 selecting3d76. No release,
supported consumer or state boundary requires intermediate pin commits. Full
old/new ranges, equivalence/range-diffs and raw graphs remain linked in existing
receipts. Require explicit whole-branch history/migration and repeated-stream
conclusions, including whether obsolete history remains.

## Final graphs, quick checks and limits

Both pins select runtime3d76/NAR
sha256-nW2yN5CRj/4hlx1PvK0vCUn7Tkejc8ZiEKqfPO0ygU0=;
runtime lock unchangedfa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955.
Workspace35nodes preserve all34others, extensione4e7e95e/NAR and every edge/follows;
config64nodes differ only runtime locked rev/NAR/time. Full graphs and originals,
source metadata, semantic baseline comparisons, refs and matching-check receipts:

- runtime-browser-final-handoff.md + runtime-browser-final-receipt.json.
- configuration-pin.md + config-pin-3d76f527/ (baseline and final full graphs).
- workspace-pin-handoff.md + workspace-pin-3d76-receipt.json and linked full graphs.
- workspace-pin-3d76-deployment-contract-receipt.json: ONE final matching checker
  exit0; binds both exact committed heads, clean pre/post states, full runtime/NAR.

Final config lockd8e4594f17393579f1b45b5fd4d53e2e7b0197d891a5becdfbe00c36e8e8d9dd;
workspace lock55cdebcc65c10f7333baa6f52af5385a560d995ca9388fb3001a86ca110885c4.
Known quick final syntax/whitespace/clean/ref checks pass. Exact package15Node
commands pass127browser tests+10syntax; original390/5281 packaged shard proof
rebound through identical filtered source, all selected drv/output identities and
complete recursive derivations. No tree-only verification reuse claim.

Current CI41518664500 at3d76 remains observed by a fresh Luna/low utility. Fast
job reports a pinned Codex binary cache download failure; A is diagnosing saved
static log, no blind retry. Native creation/archive remain active. Earlier e29
all-three failure was same extracted-browser harness dependency, native never
started; all four Ruby shards530/7852 and host245/2804 passed in each job. Full
native/package/installed/browser/deployment evidence is not yet claimed complete.

User scope/approval remains original packet: registered temporary services only,
read-only Services, Resources/Team counts, implementation and aitherdev deployment.
No default integration approval or real-session lifecycle permission. Independent
history/graph acceptance grants neither. Save focused follow-up report alongside
review-final.md; leave application/source/Git untouched, no nested reviewers.

---

# Original final substantive change review packet (historical reviewed snapshot)

Mode: mandatory FINAL review of the completed, committed substantive runtime
feature and workspace instruction deliverable. This is not advisory early review.
All intended functional source/docs/instructions are committed and quick checks
passed. No long VM/browser/integration check or source publication has occurred.

## Publication and mechanical pin boundary

Runtime `.github/workflows/check.yml` launches long archive/creation VM tests on
EVERY push. Final substantive review therefore precedes feature publication.
Remaining deployment pin updates are genuinely mechanical: exact reviewed runtime
selection in workspace and confctl configuration. They cannot be generated against
a published revision until source publication. They are exempt standalone content
review. After source acceptance/publication and pin commits, the SAME reviewer
will receive final complete series/graphs for an explicit generated-stream and
whole-branch history/migration conclusion before readiness. Do not call pins,
long tests, deployment, integration or use verified yet. No CI skip/ref/cache hack.

## User scope and decisions

User requested automatic cleanup of session-owned temporary services before
archival removes supporting files; explicit and automatic archive policies,
identity/isolation, graceful/forced shutdown, descendants, stop uncertainty,
interruption/retry and old journal/revival/package behavior must remain coherent.
User then excluded ALL existing unregistered services: no discovery, adoption,
audit, coverage/migration gate or legacy unit inspection. Registered local user
services and ordinary native cgroup descendants are the supported contract.

Portal: ONE Resources sidebar entry with Clusters / Reservations / Services
subtabs, preserving links/history/controls. Separate nonzero counts; unavailable
or stale is not zero. Clusters are confirmed owned instances including stopped;
services are nonretired registered IDs; reservations are distinct canonical held
machines, not waiting/released/repository-only claims. Team (N) includes lead plus
all nonremoved retained members, excluding utilities/activity-only counting.
Services view is read-only; no start/restart/stop/logs/links/proxy/network expansion.

User authorized implementation and aitherdev deployment via configuration.
Default-branch integration and real-session archive/delete/stop are NOT authorized.
No live example services or other-session private files/units were inspected.
No production lifecycle experiment; real-systemd proof belongs to disposable VM.

## Repositories and exact review ranges

- dev-workspace: git@github.com:aither64/dev-workspace.git, target master.
  Worktree `worktrees/2026-11-02-session-temporary-service-cleanup/dev-workspace`.
  Base c2182254d29c4175c3e9fe4267e5a92dd1da6b79;
  head 85760a7a673f3ec072c7c16dc88006e89214d448;
  tree 26177eafea54f4427af09b87daad1540ac3e5feb. Fresh origin/master is that base.
- workspace: git@github.com:aither64/vpsfree-cz-workspace.git, target master.
  Worktree `worktrees/2026-11-02-session-temporary-service-cleanup/workspace`.
  Review base ef09cf555332afebafb276e3ae54cc1f5ea6012c (shared master);
  head c474bcc55b04459dd936d2e4d8bea358b2b84184;
  tree d1222f4d112d86bdbbd0925225d7f4744717eef4. Remote master6383e884 is its ancestor.
  Feature-only rebase from6383e884..1a22338c7 is range-diff '=' equivalent to this
  range; shared master remained untouched. Historical initial portal bases retained.
- vpsfree-cz-configuration: git@github.com:vpsfreecz/vpsfree-cz-configuration.git,
  target master; registered feature at c040c14cdbacc07998700b524996a89306188d7f,
  unchanged in this content review. Exact channel pin follows reviewed publication.

Both reviewed source worktrees and indexes are clean. No feature branch published,
no source/deployment claim held. Current session identity is verified exact slug
2026-11-02-session-temporary-service-cleanup, workspace /home/aither/workspace/ai/vpsfree.cz.

## Risk, reviewer and required lanes

HIGH: new persisted local ownership, destructive file-removal ordering, native
process/cgroup shutdown, lifecycle receipts/partial recovery and mixed-version
package selection/activation. Reviewer0 is independent retained review-purpose
member, gpt-6.1-sol/xhigh/read_only; no overrides or fallback. Review directly,
no nested reviewers/subagents, edits, builds or live commands.
Read mandatory-change-review SKILL and ALL lane references: general,
architecture/repetition, scope/proportionality, risk/compatibility.

Repository trust boundary: local operator is trusted to administer this host.
Do not request hostile-local-operator containment (bind mounts/hardlinks/physical
ancestor graphs); preserve ordinary I/O/configuration errors, concurrency,
wrong workspace/incarnation, remote input safety, secrets and recovery correctness.

## Owner/API and representative consumers

Reusable dev-workspace owns service state/CLI/cleanup; one Ruby validator/writer
in libexec/workspace-session-services.rb. Go calls only allowlisted public schema1
`service list --json`, never private registry. workspace-host calls the same pure
requirements validator. Registry/marker/prelude and exact public/Ruby seams are
in design.md execution section; runtime capability keys are sessionServicesStateSchema
and sessionServicesLifecyclePolicy, both1. Conventional native systemd transient
user units, fixed stop/cgroup properties and deterministic placement proof; no
resource-plugin framework, PID/port scanner or terminal lifetime dependency.

Consumers: CLI archive/delete/auto-worker, Go lifecycle/progress/receipt readers,
Go service status projection and sidebar, workspace-host transition/candidate
activation, generic packaging and source docs; site workspace extension input
e4e7e95ed39bf514b33f8f8ae61ba9868de060ae composes generic runtime, configuration
selects matching host module. Current runtime pin c2182254, confctl7bee58a52372b95c2198ce3f2a719807a3c2c66b.
Runtime flake.lock unchanged SHA256fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955.
Full graphs/final selected source/store receipts accompany later mechanical pins.

## Compatibility and migration inventory

No database migrations. New local schema1 registration marker/registry/prelude
are introduced directly; no predecessor service schema was merged/released/
deployed/externally consumed. Earlier extra semantic-key/epoch drafts were never
published and are absent from final source; no draft rescue path. The only
superseded temporary commit77e71bf8 was amended before publication; final series
contains08a0df82 only. Ordinary archive/delete journals, sealed files/Git proofs,
receipt format and automatic Store key/schema shape remain unchanged.

Launch activity composes into existing dimensions.activity; absent registration
retains native bytes; unknown state preserves prior digest and defers eligibility.
Predecessor Store+Policy fixture is an exact byte copy of c2182254 prefix before
Runner (hash7bf2baefcfb6b47b098c8f43c73d7f33b47ff3476277724fdb4c10b3e573ce05),
not runtime duplicate/compatibility engine. Test proves old parsing/new persisted
scans and fresh grace. Conditional host gate is absent for no registrations and
fully retired state without pending recovery; review supported predecessor
lifecycle/revival/deletion implications as well as scanner parsing. Live/uncertain/
corrupt known state fences incapable packages; pending cleanup blocks transitions.

Review exact one-way archive-prelude→ordinary receipt promotion, same operation
and accepted target, old ordinary evidence strictness, concurrent display/late
executor race, delete force-upgrade behavior and lost/interrupted cleanup.

## Commit split, history and provenance

Independent UI/navigation/count commit; core registered lifecycle/state/CLI commit;
dependent portal/capability/packaging integration commit; independent workspace
launch-instruction commit. Supporting tests/docs follow behavior. All three
runtime commits are delivered together; none deployed/published independently.
Assess split and coupling independently; lead inventory is not your conclusion.
No dependency/pin streams in these reviewed ranges yet. Future one final runtime
selection per workspace/config channel must be consolidated and included in your
explicit full-history conclusion. No obsolete source approaches should remain.

## Verification already performed

Final complete runtime HEAD85760a7a smoke exit0 in repository Nix environment:
- Ruby service21tests/243assertions; host4/59; full Go cluster1.238s/session3.844s.
- Focused Service/Resource/InitialLifecycleReceipt web0.446s; JS syntax and16/16
  resource/coordination browser-unit tests; complete-range whitespace, clean index/tree.
- B additionally focused all receipt/target/observation/lifecycle paths including
  missed/full overlap, mismatches, second ordinary hash, late persistence races;
  packaged Ruby helper sibling layout1/3; VM Nix and embedded Python syntax only.
- Workspace instructions exact wording/routing/links/anchors/whitespace; no prose-
  mirror tests. Ordinary hooks/framework settings inspected, none declared/active.
- Prior broad component run130tests/3108assertions passed460.076s on immutable
  digest5a6c091dd944cfe80720adb6c9e6a34bcae644bd38986845a404ba02c75c304a,
  BEFORE final inventory I/O and activity-digest corrections. Evidence only for
  unchanged portions; final21/243 directly covers those corrections.
- First snapshot environment attempt failed before tests; explicit path flake fixed
  it once. Both retained; no product pass inferred from failed attempt.

Detailed receipts: package-a-handoff.md, implementation-b.md,
runtime-final-preparation.md, runtime-final-smoke.log, a-ruby-components-02/.
No packaged real-systemd VM, full package/browser suite, CI or deployment yet.
After review reconciliation, exact-head package + host-package-contract + extended
session-archive-lifecycle checks and CI run with fresh pinned watcher; no duplicate
Ruby campaign because package depends on all exported shards. Site app and final
committed config build/copy follow; system then user-profile activation under
vpsfree:aitherdev claim. Rollout/recovery and release rules are in rollout.md.

## Documentation and scope evidence

Owning docs changed: docs/dev-sessions.md (launcher), docs/session-archive-recovery.md
(cleanup/retry/retained evidence), docs/workspace-portal.md (UI/counts/package contract).
Workspace AGENTS/lifecycle adds mandatory launcher pointer. Lead applied required
user-facing English writing pass after facts settled. Session design/plan/state
and rollout retain individual decisions, checks and prepared-vs-executed state;
no project release-receipt backfill or KB scope. No extension runtime/config host
logic changes beyond upcoming matching mechanical inputs.

## Required review result

Report Blocking/Important/Advisory findings with file/line and actual failure path.
Explicitly conclude complete commit series/consolidation and migration lineage,
including no database migrations/new local schema introduction and no repeated
pin streams at this stage. State residual native/VM verification gaps plainly.
Do not waive checks or grant deployment/default integration approval. Retain same
reviewer for narrow fixes; direct requested fixes get focused inspection/checks,
rerun only affected lanes for new design/public-contract changes.

## Complete source commit inventories

### dev-workspace

```text
fac02494b5b41d0d4a6f299f083e67f4ea3a799e portal: group session resources and show retained counts
08a0df822b4a01cef25207ba663df861b2b4006d sessions: retire registered temporary services before file cleanup
85760a7a673f3ec072c7c16dc88006e89214d448 portal: expose registered services and protect lifecycle handoff
```

```text
 docs/dev-sessions.md                               |  50 ++
 docs/session-archive-recovery.md                   |  64 ++
 docs/workspace-portal.md                           |  76 ++
 libexec/dev-session                                |  90 ++-
 libexec/workspace-archive-check.rb                 |   3 +-
 libexec/workspace-auto-archive.rb                  |  23 +-
 libexec/workspace-host                             |  31 +-
 libexec/workspace-session-services.rb              | 779 +++++++++++++++++++++
 nix/tests/session-archive-lifecycle.nix            | 120 ++++
 nix/workspace-portal.nix                           |   4 +-
 portal/internal/cluster/status.go                  |  56 +-
 portal/internal/cluster/status_test.go             |  44 ++
 portal/internal/session/lifecycle.go               |  54 +-
 portal/internal/session/runtime-contract.json      |   2 +
 portal/internal/session/service_cleanup.go         | 159 +++++
 portal/internal/session/service_cleanup_test.go    | 116 +++
 .../internal/web/cluster_controls_browser_test.cjs |  22 +-
 portal/internal/web/coordination_browser_test.cjs  |  44 +-
 portal/internal/web/lifecycle_target.go            |   3 +-
 portal/internal/web/observation_receipts.go        |   2 +-
 portal/internal/web/operation_state.go             |   2 +-
 portal/internal/web/resources.go                   |  67 ++
 portal/internal/web/resources_browser_test.cjs     |  24 +
 portal/internal/web/resources_test.go              | 113 +++
 portal/internal/web/server.go                      |  99 ++-
 portal/internal/web/server_test.go                 |   3 +-
 portal/internal/web/service_cleanup_handoff.go     |  45 ++
 .../internal/web/service_cleanup_handoff_test.go   | 298 ++++++++
 portal/internal/web/session_services.go            | 165 +++++
 portal/internal/web/session_services_test.go       | 209 ++++++
 portal/internal/web/static/app.js                  | 108 ++-
 portal/internal/web/static/coordination.js         |  18 +-
 portal/internal/web/static/style.css               |   6 +
 portal/internal/web/team_settings_browser_test.cjs |   2 +-
 .../internal/web/templates/automatic-archival.html |   2 +-
 portal/internal/web/templates/clusters.html        |   2 +-
 portal/internal/web/templates/index.html           |   4 +-
 portal/internal/web/templates/operations.html      |   2 +-
 portal/internal/web/templates/services.html        |  18 +
 portal/internal/web/templates/session.html         |  36 +-
 test/dev_session/session_services_test.rb          | 589 ++++++++++++++++
 test/dev_session_test.rb                           |   1 +
 .../auto-archive-before-session-services.rb        | 182 +++++
 test/workspace_host/archive_recovery_test.rb       |   4 +-
 test/workspace_host/session_services_test.rb       | 124 ++++
 test/workspace_host_test.rb                        |   1 +
 46 files changed, 3749 insertions(+), 117 deletions(-)
```

### workspace

```text
c474bcc55b04459dd936d2e4d8bea358b2b84184 workspace: require managed launches for temporary services
```

```text
 AGENTS.md                            |  7 ++++++-
 docs/agent-instructions/lifecycle.md | 14 ++++++++++++++
 2 files changed, 20 insertions(+), 1 deletion(-)
```

