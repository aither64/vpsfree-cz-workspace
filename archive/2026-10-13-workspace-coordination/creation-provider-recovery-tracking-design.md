The exception is safe and proportional **if it remains an exact, process-local replacement of repeat skeleton seeding**. Keep the reviewed provider correction and let the selected CLI perform every subsequent recovery, goal-reconciliation and completion step.

The requested recovery plan is [creation-provider-recovery-plan.md](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination/creation-provider-recovery-plan.md).

I confirmed the cause and the accepted history:

- [`Runner#start`](/nix/store/klrzzbd8zayqq6p3lc8cpgxniy8gdjsq-dev-workspace-0.2.0/libexec/workspace-portal/.dev-session-wrapped:1010) calls `seed_goal` again while this journal remains `creating`. [`seed_tracking_file`](/nix/store/klrzzbd8zayqq6p3lc8cpgxniy8gdjsq-dev-workspace-0.2.0/libexec/workspace-portal/.dev-session-wrapped:4965) accepts only an empty or exactly seeded skeleton. The substantive tracking therefore fails before recovery reaches goal reconciliation.
- The [original rollout](/home/aither/.codex/sessions/2026/10/13/rollout-2026-10-13T23-12-33-01a1371c-24b8-7ac0-ab2d-5ed7a6bb2d4b.jsonl:10) records the exact root and cwd, one native `UserMessage` matching the accepted goal, successful changes to both tracking files, and completion of turn `01a1371c-3c8e-79b3-a70d-f02fd88cff5d` at `2026-10-13T21:15:52.592Z`. This establishes acceptance independently of the failed receipt’s error message.
- The plan’s Goal section still equals the receipt goal. State still has anchored `lifecycle: active`.
- All files in [the expanded frozen evidence](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination/creation-provider-recovery-tracking-frozen.json), and tracking directory device/inode, currently match. The roster file checked there is the saved snapshot; execution must still recheck the live roster.

The narrow implementation should work as follows.

1. **Retain the existing launcher and selected-generation admission.** Keep the selected Host, shared transition lock, profile/token validation, registry-derived invocation, exact attempt-1 receipt, original request sidecar, frozen direct-team preset and reviewed provider-method substitution. Recheck frozen inputs after acquiring generation admission. Preserve the ordinary creation/slug lock order and lifecycle refusals.

2. **Prove acceptance through the existing selected helper before entering `CLI#run`.** Run `thread require-materialized`, then `thread ensure-initial` for the exact original root, cwd, socket and normalized goal, **without `--start-unmaterialized`**. Do this within the supervised recovery, outside the CLI’s slug lock.

   The selected binary embeds codex-web `5f15b9293f9b`. Its `EnsureInitialMessage(..., false)` cannot call `turn/start`: unmaterialized history refuses; materialized history must contain exactly one textual user request in the earliest turn, equal to the normalized goal. Missing, different, multiple or nontext requests refuse.

   This check calls `thread/resume`, so it is not a purely observational `--inspect` operation. Keep it out of that mode. Its success must never substitute for the CLI’s later reconciliation or authorize readiness independently.

3. **Replace only `Runner#seed_goal` in this Ruby process with a guarded no-op.** At its existing call site—after ordinary receipt, journal, manifest and tracking validation, under the creation and slug locks—require the following exact scope:

   | Binding | Required value |
   |---|---|
   | Workspace | `/home/aither/workspace/ai/vpsfree.cz` |
   | Slug | `2026-10-12-streamline-vpsadminos-config-imports` |
   | Root | `01a1371c-24b8-7ac0-ab2d-5ed7a6bb2d4b` |
   | Goal SHA-256 | `78db20d4c67a3475d3113a74ea279addf263d17775c471c03edff91ffe2d6121` |
   | Plan SHA-256 | `701db2b8abf5d365e326869df167906bb184660838692a5d0394af289d8e1beb` |
   | State SHA-256 | `58964e64f0c9170cb92acce8ae04ca678c6e09c6dea87b7248e8250c6cd5e3d5` |

   Check the actual internal `goal_file` using ordinary `read_goal`, rather than trusting the outer temporary filename. Require unchanged receipt/request/journal/manifest bindings, tracking directory identity, original root, `initial_goal_attempted: true`, `initial_goal_sent: false`, and the successful same-invocation acceptance proof.

   Read plan/state as bounded, stable regular files without following symlinks; compare their bytes with the frozen hashes immediately at this boundary. On any mismatch, raise. Do not refresh expected hashes, fall back to reseeding, or accept arbitrary edited tracking. The no-op writes nothing.

4. **Continue ordinary `Runner#start` unchanged.** Its retained-roster recovery must preserve the original root and member identities. Keep the attempted marker intact, so the later `send_portal_goal` again invokes `ensure-initial` without fresh-submission permission. The CLI alone reconciles the terminal, publishes authority, completes the manifest/journal and writes completion evidence.

   Afterwards, use the existing authenticated creation-status GET to reconcile the original failed receipt through `proveCreation`. Keep its receipt ID and attempt unchanged.

This avoids changing the meaning of `preserve_tracking`, adding a recovery marker, or weakening the installed skeleton contract. The process-local exception introduces no persisted format, migration, protocol, pin or package change. Its code disappears when the launcher exits; ordinary completion records remain readable by existing components.

The material risk is concurrent activity: creation locks do not prevent the root or a human from editing Markdown directly. Maintain the supervisor’s exclusion of concurrent retries and tracking edits, and compare both hashes again after execution. Any drift or refusal stops recovery; preserve the resulting evidence and diagnose it without restoring old snapshots or forcing readiness. Normal CLI writes may already have occurred before a later refusal.

Minimal verification for the revised launcher is sufficient:

- Syntax and source-boundary inspection: only the reviewed provider correction plus the narrowly guarded `seed_goal` override.
- A small isolated check showing exact inputs preserve both files byte-for-byte, while changed hashes, identities, attempt state or missing acceptance proof refuse.
- Inspect the constructed invocation for the complete original receipt/preset/generation arguments and absence of `--start-unmaterialized`.
- After recovery, verify unchanged plan/state and root/member identities, ordinary completion evidence, and reconciliation of the same receipt. Existing provider/package/VM results need no broad rerun for this operational exception.

The previous launcher review does not cover this added exception; the parent should obtain a bounded review of the concrete delta before executing it. The existing authorization covers the exact recovery, so no further permission is needed.

- [x] Design and source/history inspection complete.
- [x] No edits, recovery mutations, native RPCs, builds, tests or nested agents performed.
- [ ] Parent: implement and verify the scoped launcher delta, then perform the authorized recovery.
- [ ] Recovery success and subsequent deployment remain unverified.

[Coordination session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-13-workspace-coordination/)