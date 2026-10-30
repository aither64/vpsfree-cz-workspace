# Final independent review

No findings. No Blocking, Important or Advisory issue was identified. This
completes the source-review gate; broader checks, deployed usability and
integration approval remain separate. Report returned by read-only reviewer0
and persisted by lead without changing its conclusions.

## Identity and reviewed ranges

Reviewer0: native thread `01a188ac-be29-7da2-813c-e3cb96f773d9`, purpose review,
access read_only, retained `gpt-6.1-sol/xhigh`, no settings override or fallback.
Verified dev-session current, both environment bindings and live same-session
roster against this session/workspace. No nested reviewers, source edits, test
launches, merge, deployment or lifecycle operation.

Read packet, plan/design/state, implementation evidence, mandatory-change-review
skill and all four lane references, routed workspace guidance, both repository
AGENTS/READMEs and relevant activity/attention documentation. Overall high risk
concerns optional persisted metadata and cross-project snapshot contract; actual
fix is bounded and compatible.

Complete ranges independently inspected:

- codex-web: `f6f4a187509b3bebfc81585c535be856eaab0d04..9d337b70987fdf1dd42a5d8efff31f755a122550`.
- dev-workspace: `cc0d452a0653a112c8a013492c1734d9554bb909..5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`.

Each base is the locally available origin/master merge base. Exact final heads
and clean worktrees rechecked. Later workspace/config deployment pins are outside
this report.

## Lane conclusions

**General:** Attention previously read interactive Prompts from an ObserverOnly
client that deliberately never admits them. Fix consumes native identity from
its activity snapshot and retains original attention digest. Real passive Unix
WebSocket fixture covers omitted isBlocking, projected ReadActivity and empty
Prompts. Portal regression covers observation/reduction and GET attention;
browser coverage checks title/focus/subsequent input and resolution preserving R.
Existing observer tests independently guard against answering native requests.
Owning/consumer documentation is accurate and discoverable.

**Architecture/repetition:** Reuses bounded recorder and shared requestPolicyFor;
no second registry, policy catalog or response-authority API. Representative
consumers inspected: conversation ActivityProvider/authorized activity endpoint,
portal activity/attention, communication activity reads and exact Nix/Go pins.
Consumers can ignore optional projection. Key locations: codex/activity_recording.go:299,
codex/activity_snapshot.go:120, portal/internal/web/attention.go:211.

**Scope/proportionality:** Restores Plan-question title marker. Diffstats (6 files
+252/-33; 10 files +109/-35) largely reflect focused coverage, Go alignment and
paired pins. Production browser/title and acknowledgement code unchanged. Native
identity distinguishes consecutive questions; waitReason/timing cannot preserve
deduplication. Smallest compatible solution found. Provider/consumer commits
arrived at 17:33/17:39 UTC after approximately 17:19 start, with design/check
milestones. No evidenced scope/stall issue or optional hardening request.

**Risk/compatibility:** Projection requires durable connected waiting state,
current in-progress turn, complete identity and supported blocking policy.
Resolution, terminal cleanup, connection generation, unknown state/scope and
write-failure boundaries suppress obsolete identities. Portal stale/age/thread
gates remain. Optional itemId/method preserve schema 1: predecessor JSON readers
ignore them, new readers accept absence, old writers may drop them without losing
timing, reconnect does not restore connected authority from disk. Privacy/timing
coverage and byte/count bounds remain. No private question/command/answer data,
response token or remote mutation surface added.

Nix input/lock and Go version select upstream
`9d337b70987fdf1dd42a5d8efff31f755a122550` /
`v0.0.0-20261029173332-9d337b70987f`. New portal source needs paired provider;
old source ignores additive metadata. No coordinated fleet update or database
repair. Existing forward-recovery rules govern activation.

## Whole-branch history, dependency stream and migrations

Each complete range has one logical commit: `9d337b7 activity: expose passive
blocking request identities` and `5f4f1c1c portal: use passive request identities
for attention`. Tests/docs and consumer pins reasonably belong with their
behavior; commit bodies explain cause/compatibility.

No obsolete unmerged approaches, fixups, superseded compatibility paths or
transitional iterations. Independently grouped dependency stream: codex-web
source/library in flake.nix, flake.lock, portal/go.mod, portal/go.sum and
vendorHash. One final selection in one consumer commit; no repeated intermediate
updates need consolidation or unrelated dependency streams changed.

**No migrations.** Neither range adds database migrations, seeds, schema-version
changes or conversion paths. No merged/released/deployed/externally consumed
migration version to preserve. Optional schema-1 metadata is not a transitional
migration. Publication supplies dependency availability, not deployment/integration.

## Verification and residual gaps

Inspected committed tests and quick logs: provider Test(Activity|Observer) passed
(package 3.192 s), portal Test(Attention|Notifications) passed (0.588 s); evidence
reports browser 75/75. Exact-range diff checks independently passed. Reviewer did
not rerun checks.

Vendor result/log confirms
`/nix/store/8m2rrmwr5bcnkw1daii6wb08d3af381b-dev-workspace-0.2.0-go-modules`
from `/nix/store/mxvfp26s261x63fbzcx05w8fmzvc2n76-dev-workspace-0.2.0-go-modules.drv`.
Recursive graph has target and 1,972 derivations; evidence records final-head
evaluation returning same drv. Dependency verification, not whole-package success.

Flake suites and exact-head CI acceptance remain with lead. Coverage composes
synthetic native transport and separate portal/browser checks; no deployed real
background-tab Plan-question/focus/answer scenario yet. Verify after paired
activation. Explicit verification/deployment limits, not identified source defects.

Review completed 2026-10-29 approximately 17:45 UTC.
