# Independent FINAL review

## Findings

1. **Important — R1: rejected foreground operations can wait indefinitely before reporting the error.**
   Reviewed commit `45086fb34ebc2bf7ad6a965b27c286c580ce44cb`,
   `osctl/lib/osctl/cli/container.rb:1266` and `:1270`; supporting existing
   `open_console_tty` at `:1283` and `:1295`, `osctl/lib/osctl/client.rb:138`,
   and `osctl/lib/osctl/console.rb:24`.

   `open_console_tty` forks a child holding the console socket, then executes
   the operation in the parent. On rejection, `sock.close` closes only the
   parent's descriptor. The child retains its descriptor and waits in the
   console's `IO.select`; the parent waits for that child before restoring the
   terminal and reaching the new error raise. This is concrete for a stopped,
   tainted container: the daemon allows tty0 clients while stopped and retains
   them without a backend (`commands/container/console.rb`,
   `console/tty.rb`). A rejected Start performs no teardown that would close
   that connection. The user must manually detach before receiving the error.

   The descriptor behavior predates this change, but the newly claimed
   foreground error delivery remains incomplete. The new CLI regression stubs
   `open_console`, so its `:restored` marker assumes away the fork/socket
   boundary. Explicitly terminate the inherited console connection or child on
   a failed response, retain child wait and terminal restoration, then raise
   the original message. Add a bounded real socket/fork regression with input
   kept open, proving completion without manual detach. General and risk lanes.

   Sent to lead before this report; lead accepted Important and assigned the
   narrow fix to implementer0. Implementer0 reports planning shared-endpoint
   shutdown before close and a real socket/fork regression. This report does
   **not** inspect or approve that later revision.

2. **Advisory — R2: add performed validation to the owning commit message.**
   Commit `45086fb34ebc2bf7ad6a965b27c286c580ce44cb` explains motivation,
   behavior and invariants, but omits validation. The repository's mandatory
   `docs/os/patch-series-policy.md`, “Commit descriptions and provenance,”
   requires meaningful retained commits to explain validation performed.
   Include the focused spec/render/hook results when amending the logical
   owner for R1. No extra validation run is requested. General/history lane.

No Blocking findings and no other Important or Advisory findings.

## Reviewed identity, scope and method

- Bound session: `2026-11-13-osctld-start-recovery-errors`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`. `dev-session current` and both
  `DEV_SESSION_*` values match. Live roster confirms reviewer0, purpose review,
  ready, read_only, retained `gpt-6.1-sol` / `xhigh`, thread
  `01a1d707-8aee-7940-bdb3-d35f482eb249`. No fallback or settings override.
- High-risk final review: general, architecture/repetition,
  scope/proportionality, risk/compatibility. Read the mandatory review skill and
  all four references, applicable workspace procedures, documentation/handoff
  skills, repository AGENTS/README and permanent patch-series policy.
- Exact vpsadminos range:
  `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62..45086fb34ebc2bf7ad6a965b27c286c580ce44cb`.
  Inspected the complete commit, final diff, changed tests/manual, admission,
  locks/netif readers, recovery checks, console client/server, forwarding and
  wire error handling. Merge base equals the specified base; rev-list count is
  one; exact-range `git diff --check` passes.
- Read the full packet, plan/state, incident, design, contracts/checks, July
  comparison and race evidence. Spot-checked their consequential claims against
  exact committed current/July sources. Inspected representative vpsAdmin
  consumer code at `2d0946c4e699aa61092228d8a7cb275477ee46d0`.
- No nested agents, builds, tests, source edits, ref changes, deployment or
  integration. Only this assigned review report is written. Quick-check script
  and final log were inspected: 236 osctld and 40 osctl examples passed with the
  reported seeds; man rendering is included in the fail-fast script. Hooks and
  metadata refresh are packet evidence, not independently rerun review checks.

## Four-lane conclusions

**Scope and proportionality.** The recorded user scope is actionable admission
errors, concrete read-only July comparison and a safe race-fix proposal. The
eight-file `+293/-31` branch delivers diagnostics and their ordinary/foreground
CLI path, manual and focused regressions. It introduces no lifecycle framework,
new recovery policy or proposal implementation. The recorded milestones cover
investigation/design acceptance around 22:38–22:46 UTC and committed diagnostics
around 22:53 UTC after the 22:29 session start; they establish delivery rather
than an unexplained expansion. No disproportionate mechanism needs removal.
The future terminal-record proposal has explicit unresolved release contracts
and no implementation authorization; those are future work, not missing code
in this branch.

**Architecture and correctness.** One protected blocker decision owns the five
gates and retains their short-circuit order. `can_start?` remains Boolean and
cheap on success. Start checks the reason before force/no-op and its first side
effect. Recovery descriptions read existing netif data without external probes,
registry acquisition, persistence or cleanup. Capability checks follow the
existing netif-manager polymorphic contract. The small shared foreground helper
has the right ownership, subject to R1. No harmful new behavioral duplication or
unnecessary extension point was found.

**Risk and compatibility.** The failed socket envelope remains
`status:false/message:String`; normal restart and custom boot preserve failed
subcommand messages. Representative nodectld code uses process exit/output,
without parsing the old literal. Arbitrary external scripts remain an
unverified free-form-wording consumer. No persisted format, hook protocol,
configuration pin, public option, API generator or migration changes occur.
Node-by-node userspace updates and rollback retain the same state. No coordinated
fleet update follows from this change. Existing absent/reused-link, both-selector,
IFB, shared-owner and stopped/no-init checks remain intact. Error advice makes
cleanup conditional and points to the manual before acknowledging absence.
Boot's earlier effects, guest reboot, raw JSON console and asynchronous
queue/autostart limits remain explicitly outside the changed contract.

**Whole-branch history.** The complete range contains only
`45086fb34ebc2bf7ad6a965b27c286c580ce44cb`, one coherent diagnostic-delivery
change including its tests and manual. No obsolete unmerged approaches,
fixup/WIP residue or transitional compatibility paths remain. The reported
earlier message-only amend is not retained in the reviewed series. No repeated
dependency/channel/input/pin/generated-artifact update streams exist, so no
consolidation or retained intermediate-boundary justification is needed.
**No migrations**: none appear in the complete series/final diff; no transitional
migration lineage or merged/released/deployed/externally consumed migration is
introduced by this range. R1 should be folded into its logical owner before the
lead performs final readiness checks.

## Documentation placement and preservation

The existing `osctl/man/man8/osctl.8.md` start/recover sections are an appropriate
operator reference/how-to home, discoverable through README's man links and
existing `man osctl` usage. They remain useful without this private session.
Source comments retain the shared decision/order and read-only rationale with
the owning implementation. No new documentation index or subsystem is needed.

The manual accurately distinguishes recorded identity from live-link proof,
aggregate taint from historical cause, read-only inspection from `recover state`,
full from partial cleanup, and ordinary recovery from privileged absent-link
acknowledgement. Existing stopped/no-init, name-and-index/IFB absence, live/reused
link refusals and unrelated-error retention are preserved. No content move,
anchor removal, supported upgrade retirement or rollback-path removal occurs.
The queue acknowledgement limitation matches source. The foreground delivery
claim in the packet/design remains subject to R1; it is not a proven runtime
result.

July/current incident evidence and future proposal are correctly placed in
session records, separate from maintained product guidance and from an executed
rollout. They identify exact revisions, distinguish recorded CI from rerun
checks, and leave the exact incident response and initiator unproved. The
proposal distinguishes accepted intent from unknown stopped state, preserves
host-link safety, and explicitly leaves writer authority, launch binding,
legacy coverage, crash persistence and rollback fencing unresolved. Reusable
Ruby environment lessons have the recorded workspace-notes destination. No
documentation placement/preservation finding beyond the R1 fidelity limitation.

## Disposition and remaining evidence

Current reviewed head is **not ready to pass the final gate until R1 is fixed or
an explicit decision is recorded**. Lead has chosen the fix. A narrow endpoint
termination change and regression can be directly inspected/verified by the
lead under the mandatory review skill's narrow-remediation rule; a new design or
contract expansion would require affected-lane review. R2 can accompany that
amend.

No real fork/terminal or packaged VM verification was performed by this review.
Full suites/VM/CI and final revised-head evidence remain lead-owned after finding
reconciliation. Source analysis does not reproduce the production callback race
or prove July runtime behavior. This review grants no publication, integration,
deployment or lifecycle authorization.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctld-start-recovery-errors/)
