# Independent final review

Review completed against the committed heads below. One Blocking and nine
Important findings remain. Do not start long integration checks or deployment
until the Blocking finding is fixed and the Important findings are fixed or
explicitly reconciled under the mandatory-review procedure.

## Findings

1. **Blocking — ordinary registration changes the registry and then necessarily
   fails activation.** Runtime `libexec/workspace-coordination-host.rb:166` and
   `libexec/workspace-host:954`, in `ecad26d56ba061fa67e8b19eb0ee12d693f13187`.
   `Host#register` writes the registration at `workspace-host:510` and calls
   `activate_installed` at line 515. Candidate `_activate` now unconditionally
   requires a claimed `profile_activate` attempt whenever `profileMachine` is
   configured (or any ledger exists). Ordinary `register`/`register --replace`
   has no such attempt, so the newly composed site package rejects it after the
   registry write, before installing/configuring its services. Preserve the
   distinction between selecting a profile and reconciling registrations within
   the already selected package, while retaining the appropriate machine and
   transition admission. Validate/refuse before modifying the registry when an
   operation cannot proceed. Add a real Host-path regression using a nonempty
   coordination catalog; current Host fixtures do not cover it.

2. **Important — suspension has no supported resume transition.** Runtime
   `libexec/workspace-host:1015`, `libexec/workspace-coordination.rb:502,901`,
   same runtime commit. `suspend` persists `suspended: true`; no production code
   ever sets it back to false. Re-enabling the services, activating the same
   package, or restarting the coordinator leaves all claims and notifications
   disabled. A coordinated profile switch also cannot resolve this because it
   waits for a claim from the suspended scheduler. Failed suspension after the
   ledger write has the same problem. Provide an explicit, generation-checked
   resumption/recovery path, with compensation for a partially failed suspend,
   and test preservation of the queued jobs and held reservations across it.

3. **Important — post-activation completion lost generation serialization for
   consumers without coordination.** Runtime `libexec/workspace-host:605,728`,
   same commit. The optional/default empty-catalog path releases the transition
   lock before `complete_candidate_activation`, which then unconditionally
   deletes the global pending-Codex record and restores terminals using its
   saved package. After A selects B and releases the lock, a newly started
   stable invocation may select C while A is waiting for sockets. When B and C
   have the same native registration semantics, A's verification passes and A
   can delete C's pending recovery record or restore clients from B. No resource
   claim protects this default path. Keep expensive observation outside the
   lock, but reacquire/revalidate the exact selected generation and operation
   identity before committing completion or restoring clients; retain the old
   serialization where the new claim mechanism is unavailable. Test two
   interleaved ordinary switches and same-native/different-package generations.

4. **Important — final lifecycle journal deletion precedes coordination
   finalization.** Runtime `libexec/dev-session:2152,6930`, same commit.
   Revival unlinks/fsyncs its journal before clearing the coordination fence;
   archive likewise deletes its journal and cleanup sidecar before marking the
   fence completed. A crash or ledger-write failure in that interval leaves an
   incomplete fence after the only resumable lifecycle journal is gone. In the
   revival case the tracking is already active, ordinary coordination refuses
   the fence, and repeating revival cannot reconstruct the operation from its
   now-absent archive source. Make coordination finalization an idempotent part
   of the durable lifecycle completion, before discarding the recovery journal,
   and bind it to the exact lifecycle/owner incarnation. Exercise interruption
   at this boundary for archive, revive and deletion.

5. **Important — one unavailable owner can starve every other owner's
   notifications.** Runtime `libexec/workspace-coordination.rb:503` and
   `libexec/workspace-coordination-host.rb:274`, same commit. The delivery loop
   takes the first two globally due outbox entries before filtering to the
   current workspace and owner. The scheduler also verifies an owner before
   calling delivery. If A has two pending events and its native thread is
   missing/unavailable, A never reaches delivery and those events keep
   `retryAt: 0`. Every healthy B call selects the same two entries and skips
   them, so B's native wakeups never run. Filter to the eligible current owner
   before applying the bound, or use a fair independent outbox dispatcher.
   Test a failed owner ahead of a healthy owner in another workspace.

6. **Important — network reconciliation runs synchronously in the sole
   scheduler and can stop unrelated work.** Runtime
   `libexec/workspace-coordination-host.rb:278` and
   `libexec/workspace-coordination-execution.rb:79`, same commit. Once an
   attempt's worker exits, the scheduler directly performs `git ls-remote`,
   fetch, adapter SSH inspection, or forward profile activation inside
   `reconcile_job`. `Command.run` has no read timeout; the adapter's ordinary
   `MachineControl` SSH path also supplies none. An unreachable or stalled
   endpoint for one uncertain job can therefore block all other workspace
   claims and deliveries indefinitely. Keep reconciliation bounded and outside
   the scheduler loop (or bound its read-only probes); preserve the original
   claim and never treat a timeout as no-effect proof. Verify that a stalled
   reconciliation does not prevent an unrelated ready job or notification.

7. **Important — the prepared confctl activation still invokes Nix evaluation
   under the machine claim.** Extension
   `lib/workspace_confctl_adapter.rb:142`, in
   `9201bf5ed7a4e0313cebf589510a96025b97a953`. At configuration's actual pinned
   confctl `7bee58a52372b95c2198ce3f2a719807a3c2c66b`, `ConfCtl::Nix.new` calls
   `NixLegacy#initialize`, whose default `max_jobs` loads
   `Settings.instance.max_jobs`; `Settings#read_settings` creates a stateless
   Nix client and calls `confctl_settings`, which evaluates
   `.#confctl.settings`. Each activation is a new process, so preparation's
   singleton cache does not survive. This contradicts the no-evaluation
   activation contract and can introduce slow/failing Nix work after claiming
   the machine. Use the pinned public stateless/explicit-options API for the
   already prepared activation operations. Test against the real pinned
   constructor behavior: the current fixture's `Nix` class omits initialization
   and cannot detect this.

8. **Important — admission limits also prohibit the recovery/completion writes
   for which space was reserved.** Runtime
   `libexec/workspace-coordination.rb:258` and
   `libexec/workspace-coordination-execution.rb:609`, runtime commit above.
   `Store#request` applies the same 14 MiB admission threshold and 16,384-receipt
   ceiling to `cancel` and `finish` as to new jobs. For example, the last
   permitted submission/approval can fill the receipt ceiling; thereafter the
   owner cannot cancel an unstarted job or finish and release a settled machine
   even with the 2 MiB recovery reserve free. With history pruning deliberately
   absent this becomes a permanent recovery blocker. Separate new-work capacity
   checks from bounded completion/cancellation receipts and account for their
   reserved space at admission. Test cancellation and finish at both limits.

9. **Important — a queued machine artifact never revalidates its configuration
   branch baseline before activation.** Runtime
   `libexec/workspace-coordination-execution.rb:357,364` and
   `libexec/workspace-coordination.rb:695`, runtime commit above. Preparation
   records `configurationBaseline`, but no subsequent code reads it. Machine
   snapshot validation only compares the caller's fields to the sealed artifact;
   the worker checks the released-deployment frontier, not the current configured
   remote target. If B prepares from master R, then a merge-only A advances that
   configuration target to R+A while the live system stays unchanged, B passes
   its live baseline/frontier checks and deploys the old branch lacking A. The
   accepted design requires the configuration source to include the current
   remote baseline. Reobserve the exact configured target and prove coverage
   before mutation, returning `needs_refresh` when it advanced incompatibly.
   Include a preparation → independent integration → activation regression.

10. **Important — deploy-first installation does not deliver the coordination
    procedure to cooperating agents.** Runtime `nix/workspace-portal.nix:338`
    and existing `portal/internal/workspacecodex/lead_policy.go:32`, together
    with workspace `docs/agent-instructions/deployment.md:7` in
    `291a089274e886c725469ae7678d6cb82d14b4e0`. The new procedure routing lives
    only on the unmerged workspace feature branch. Shared master remains the
    ordinary agent working directory, runtime packaging installs the catalog
    and schema but neither coordination guide, and the linked GitHub master
    guides do not exist before integration. Thus a new/resumed session after the
    expressly authorized deploy-first rollout still receives the old direct
    Git/confctl instructions. Direct confctl is outside runtime enforcement, so
    otherwise cooperating agents can unknowingly bypass a retained machine
    reservation. Install the authoritative guide with the selected package and
    provide a discoverable command/path plus a bounded technical binding cue
    for managed sessions. Preserve the saved role instructions, model and effort;
    do not merge workspace master merely to make the guidance available. Test
    discovery from the deployed package with an unchanged shared checkout.
    This gap and the registration path were also identified independently in
    the lead's subsequent `review-addendum.md`, which was inspected before
    closing this review.

## Advisory observations

- A crash between the claimed ledger transaction and writing the attempt request
  leaves a proved pre-dispatch operation permanently reserved by the supported
  commands: `reconcile_job` refuses missing `request.json` at execution line 71,
  while cancel/refresh refuse claimed/reconciling states. The design permits a
  persistent blocker for uncertain outcomes, so this is not scored as another
  gate here, but this particular window precedes any worker launch. A bounded
  never-started dispatch recovery would improve operability without replaying a
  mutation. Keep that distinction visible in recovery documentation/tests.
- The design allows early release when no deployment occurred and associated
  jobs are proved unstarted/canceled. The current `finish` always requires full
  feature integration, while cancel never releases a held reservation. After a
  first `needs_refresh` with no effects, an operator who cancels deployment must
  use lifecycle/exceptional recovery instead. Either implement the bounded early
  release or explicitly reconcile this omission with the accepted design.
- There is no new VM/native/two-workspace end-to-end test in the reviewed series.
  The existing package and Host suites remain useful, but the recorded 18
  coordinator tests execute workers directly with fixture admission and several
  deployment tests manually write successful ledger state. They do not establish
  systemd worker survival, real confctl no-evaluation behavior, native transport
  crash recovery, or coordinated self-deployment. These remain acceptance work.

## Exact reviewed history

| Repository | Base | Head | Complete feature series |
| --- | --- | --- | --- |
| dev-workspace | `7c07b540a5e45cac4b39351f713cf3528e4df614` | `212dbb6adc36df9a0984ab5a7df51b3d0adff1a9` | `ecad26d56ba061fa67e8b19eb0ee12d693f13187`, `212dbb6adc36df9a0984ab5a7df51b3d0adff1a9` |
| vpsfree-dev-workspace | `7157c8098dcf60127aa4df823fab82b4185ad22a` | `9201bf5ed7a4e0313cebf589510a96025b97a953` | `2e195d450c7eb7f6dd7d0aa1342e0afdb402a806`, `9201bf5ed7a4e0313cebf589510a96025b97a953` |
| workspace | `06a0a8a529c686556b33165f7a536bf7bff50050` | `291a089274e886c725469ae7678d6cb82d14b4e0` | `aa9ba7e187e6d485b7c164f0083917da5185e414`, `291a089274e886c725469ae7678d6cb82d14b4e0` |
| vpsfree-cz-configuration | `bfb1d89c95308024a9269974c207bf7cefe1fb1c` | `5c4da1de524f5fa2c303ca10f33693e6e024dc5c` | `dfd85c5e28b222262067c9edb06103e14c521a27`, `5c4da1de524f5fa2c303ca10f33693e6e024dc5c` |

Inspected the entire eight-commit base-to-head series, messages, final diffs,
tests and owning documentation. The histories introduce the final approach
directly; no obsolete fixup/design iteration or transitional compatibility
commit remains. The integrated runtime state-machine commit is coherent under
the packet's stated indivisibility rationale; the read-only UI, extension pin,
adapter, site policy/composition and configuration documentation/pin are
separately reviewable. No additional history-split finding.

Independently checked update streams: extension has one runtime update (with its
required codex-web transitive selection), workspace has one extension plus
nested-runtime composition update, and configuration has one generated
`devWorkspace` update. All select runtime `212dbb6a`; codex-web resolves to
`5f15b9293f9b1eef7469a34d7b2044c743160283`. No redundant intermediate pins remain;
generated configuration history is preserved. Superseded published refs are
outside these reviewed series and are reported by the packet as unused.

The workspace feature is not yet rebased onto shared master
`90005ea3a7a170b23699c38933b111b046ce43f8` (the initial tracking-plan commit).
Its merge base remains `06a0a8a5`. Complete the required patch-equivalent rebase,
comparison capture and final-head checks before claiming readiness; this report
only certifies inspection of the listed heads.

**No database migrations.** New private schema-1 coordination records are
introduced directly. There is no intermediate migration lineage, nor an edit to
the existing manifest, lifecycle, cluster or Codex submission schemas. According
to the packet, this new protocol has not been merged, released, deployed or
externally consumed. Retained old-package behavior is intentionally rejected
after coordination state exists; forward recovery and exact adapter/worker
contracts remain the supported boundary.

## Lane and validation conclusions

All four assigned lanes were assessed directly, without nested agents:
general correctness/history/coverage; architecture/repetition and actual
consumers; scope/proportionality; risk/compatibility/recovery. Runtime owns the
ledger and fixed mutation kinds, extension owns the confctl adapter, workspace
owns site identity/input mappings, and configuration pins the corresponding
host contract. Those boundaries are appropriate. The shared bounded command
runner avoids competing runtime/adapter implementations. No additional
speculative framework or inappropriate security-hardening finding was identified
under the trusted-local-operator boundary; remote portal routes remain read-only
under existing authentication and render values with safe DOM text operations.

Project feature/operations/site documentation is linked and mostly placed with
its owner. The individual rollout record correctly says prepared, not executed.
The findings above identify claims that still exceed the implementation.
No default-branch integration or reboot is authorized by the reviewed plan.

Read and checked the saved successful quick evidence: 18 coordinator tests/92
assertions, 140 Host tests/1069 assertions, four adapter tests/20 assertions,
syntax checks and the native-helper fixture test. The addendum additionally
records eight workspace-instruction tests/144 assertions and four composition
tests/19 assertions passing. Per assignment, no long tests,
deployment, source edits, roster changes or live mutations were performed. Real
systemd/profile/SSH/native-Codex integration and live continuity remain unproved;
the safe pre-RPC notification ambiguity and conservative remote unknown-outcome
behavior are accepted documented limits, not findings demanding a new transport
or distributed execution service.
