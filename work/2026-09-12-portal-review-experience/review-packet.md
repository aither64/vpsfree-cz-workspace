# Portal review experience: committed implementation review

Review initiative `2026-09-12-portal-review-experience` at
`/home/aither/workspace/ai/vpsfree.cz`. Read `plan.md`, `state.md`, this packet,
repository AGENTS.md and your mandatory-change-review lane reference. Perform
review directly; no nested agents. Save your findings as `review-LANE.md` beside
this packet. Do not modify project code. Cite concrete commit/file/line evidence.

## Requested behavior and accepted boundaries

The user requested all seven portal improvements and then approved the plan and
implementation: more usable question height with visible actions; immediate final
session navigation while initialization reports progress; local commit and branch
review with GitHub links, expandable commit messages and split/unified diffs;
typed webSearch/subagent events; root-turn message/tool counts; working versus
waiting durations; Messages as the initial filter. Subagents were authorized.

Repository review must include unpushed commits, two desktop cards per row, one on
narrow screens, 50-commit pages, files left and continuous stacked diffs right,
file navigation scrolling to its section, remembered split default. User accepted
CodeMirror's numbering: both sides in split, current-file numbering with deleted
blocks unnumbered in unified. Native Git supplies bounded blobs; CodeMirror owns
text difference computation. Preserve binary/mode/rename/submodule/symlink/newline
metadata. Current comparisons use locally available origin/default merge base.
Save viewed immutable pairs; integrated exact heads use the latest saved pair;
original recorded base fallback has an explicit possible-upstream-changes label.
No implicit fetches, GitHub-only review, Git mutation, editable merge UI or arbitrary
browser-provided refs/paths. Existing GitHub Actions/status remain independent.

New, fork and implement-plan-new should return the final URL quickly and show
honest progress, errors and explicit retry before a manifest is available.
Exact plan/source/settings must survive initialization/retry. Existing CLI
journals and runtime generation/identity locks remain authoritative. No duplicate
fork/thread/initial goal after a provable completed attempt.

Work means observed root-thread work excluding blocking questions, approvals and
permission requests. Overlaps count once; asynchronous nonblocking questions do
not pause. Closed waits and between-turn gaps form waiting totals; current open
wait is separate and trailing idle does not inflate totals. No subagent wall-time
sum. Forks exclude inherited turns; ambiguous lineage is unknown. Unobserved old,
offline or restart gaps must remain unclassified. Browser-independent passive
observation must never answer/reject requests or change request ownership/policy.
Counts are distinct assistant messages/plans and actual root tool invocations,
not streaming deltas, outputs, lifecycle markers or child tools.

## Ownership and consumers

`codex-web` owns Codex protocol normalization, optional typed `entry.activity`
plus preserved summary/details fallback, safe shared `createTranscriptActivity`,
ObserverOnly client, application-owned ActivityRecorder, full root turn metadata,
fork/revert scope and optional Read-authorized ActivityProvider. Existing Client
interface remains source-compatible. Its standalone conversation renderer is a
consumer alongside dev-workspace (Go import and pinned shared browser assets).

`dev-workspace` owns workspace/session authorization and runtime identity, receipt
worker and CLI completion evidence, browser navigation/progress, native Git reader,
private workspace comparison records, repository UI/bundle, and service monitor
that subscribes only matching ready owned session threads. It passes optional
Target.Activity to codex-web. It owns recorder/client shutdown. New APIs are
session-scoped opaque-token operations; browser refs and file paths are not trusted.

`vpsfree-dev-workspace` wraps dev-workspace.lib.mkPackage with organization tools;
`workspace` consumes that wrapper with existing siteConfig and deploys a user
profile. Their changes are pins only. No system configuration, node or guest
change is intended. Inspect actual imports/pins/wrappers and any additional
consumers you discover rather than treating this list as a closed catalog.

## Risk and compatibility

Overall HIGH: new private persisted receipts/comparison/activity state, async
lifecycle recovery, read API and experimental Codex protocol consumption, multi-repo
package/rollback contracts. All four lanes apply (general, architecture, scope,
risk), each fresh gpt-5.6-sol at xhigh. Remote clients remain untrusted; local
workspace operator is trusted to administer this host (repository AGENTS scope).
Do not invent a compromised-local-operator filesystem attack boundary. Ordinary
wrong-workspace/path/identity/concurrency, remote input, secrets and rollback still
matter.

New records are separate private files; existing strict session manifests, start/
fork lifecycle journals and Codex submission state retain formats. Old packages
ignore new records. No migration, coordinated machine update, old-client removal
or Codex version change. Delivery: provider -> generic runtime -> organization
wrapper -> workspace user-profile switch. Rollback should read previous supported
state and leave new additive records harmless. Long live/package-upgrade/rollback
acceptance follows review; branches stay unmerged and session open.

## Dependencies and implementation choices

Selected Codex remains 0.154.0. Protocol corpus was generated with
`app-server generate-json-schema --experimental` because initialize enables
experimentalApi. Exact selected Rust/schema inspection established full vs summary
turn items and trusted physical fork-prefix semantics. Summary is insufficient for
intermediate current-turn counters, so recent20 full turns plus paginated older
metadata are used; older metadata cache invalidates on revert. Missing old counts
are identified by countsKnown rather than invented zeros.

CodeMirror merge6.12.2, view6.43.11, state6.7.4, esbuild0.28.2 and complete locked
graph. Maintenance checked 2026-09-12; CodeMirror's move to Forgejo explains GitHub
archive status. Native Git CLI chosen over go-git/libgit2. diff2html rejected for
intermittent maintenance; other rejected viewers and evidence are in plan.md.
No network-loaded browser assets or broad CSP relaxation: self-hosted Nix bundle,
complete licenses/integrity manifest and per-response CodeMirror style nonce.
Git/API concurrency/time/output/blob/file limits bound local review; display
computation uses CodeMirror limits and lazy viewport editor retention.

## Commit split

Provider typed event support is separate from passive timing/history. Runtime
provider pin is separate and precedes dependent code. Runtime has separate commits
for async creation, Messages default, question layout, local Git review, typed
rendering and timing monitor/UI. Tests/docs stay with the behavior they validate.
Creation's durable receipt, worker, CLI completion proof and UI are one behavior:
fast navigation is unsafe without retry/recovery proving the same destination.
Git reader, review API, remembered comparison state, viewer/bundle/licenses/Nix
packaging form one local-review feature; the reader is not a separately exposed
library. Provider timing protocol, history ownership and recorder are coupled:
recorded durations require exact own-turn scope and observed request boundaries.
Organization and consuming workspace delivery pins are separate.

## Quick verification before review

Provider Go ./..., Go race codex/conversation, Node browser contracts and syntax,
full exact0.154 experimental protocol corpus all pass. First provider feature CI
failed an immediate-post-resume disconnect race; logs were inspected. Fix preserves
successful subscription and watches while refusing stale connection coverage;
regression pair100 repetitions and observer/reconnect race suite10 repetitions
pass. Exact final provider feature Check CI passed; evidence is recorded in
codex-web-implementation.md.

Runtime all Go packages pass using actual pinned Go module with
`GOWORK=off GOFLAGS=-mod=mod go test ./...` from portal via pinned Nix Go/GCC.
Browser unit contract and creation/repository/shared JS syntax pass. Creation
focused Ruby25runs239assertions and focused Go race pass. Activity monitor tests
cover no-browser observation, ownership/retirement and wrong cwd; provider tests
cover overlaps/nonblocking/terminal/restart/ID reuse/storage failure/fork/revert/
missinglineage/41turn pagination and passive unsupported-request behavior.

Focused question CSS geometry fixture passes desktop/short/mobile/zoom-related
sizes including390x600 and780x422, actions visible outside body scroll. This is
not yet complete real-browser portal acceptance. Repository Chromium fixture
passes30stacked files with lazy loads, last-file scrolling, split/unified gutters,
readonly/no merge controls, two/one cards, retained disclosures/scroll/immutable
head warning, zero CSP errors. Nix asset output matched local locked build bytes.
See repository-review-verification.md and curated artifacts.

No long VM/live App Server integration began before this review. Ordinary feature
CI executes focused package checks; host VM only master/manualdispatch. Complete
packaged checks, real portal browser/App Server, upgrade/rollback and deployment
follow finding reconciliation. Assess gaps candidly; do not equate synthetic
fixtures or planned commands with completed integration evidence.

## Exact reviewed commit ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..bba2ae1d9796dc7267c0bfc5ee9f072f43d6e92e`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`
- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..774c2083333b9b71d4abb04d4aa7c79ea0aa897d`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`
- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..d0ebe39e4cc2e41cb791ad048c60eb1e940c023e`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`
- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..bfc80f25864528b5b954daf84c6e8a7d4a8348c7`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`

Provider Check CI and runtime feature fast CI both pass on these exact heads.
Extension and consuming package derivations evaluate successfully. No long tests run.
