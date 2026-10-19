# Recovery of the blocked provider-enabled creation

Operational design, 2026-10-14; delegated Astra/xhigh, read-only investigation.
The user explicitly authorized recovery of this exact creation, then deployment
and the previously approved integration. The parent owns the launcher and all
mutations. This design leaves the reviewed deployment artifacts unchanged.

## Conclusion and observed scope

Resume the ordinary creation command once, using the **selected installed**
Host/CLI and its exact frozen receipt. Apply only the already-reviewed
`native_provider_arguments` correction in that Ruby process. Let the ordinary
creation owner publish readiness and completion evidence, then let the portal
reconcile its failed receipt through `currentCreation`.

There is no simpler working public retry on the selected generation: it repeats
the same broken terminal call. Package activation is correctly refused while
creation is unfinished. `resume`, `--no-codex`, clearing journals, selecting a
candidate executor or starting a replacement conversation are not substitutes.

Read-only inspection established:

| Binding | Retained value |
| --- | --- |
| Workspace | `/home/aither/workspace/ai/vpsfree.cz`, registered `vpsfree-cz` |
| Slug | `2026-10-12-streamline-vpsadminos-config-imports` |
| Selected package | `/nix/store/klrzzbd8zayqq6p3lc8cpgxniy8gdjsq-dev-workspace-0.2.0` |
| Portal receipt | `a9ea3ef892d5344be881fca8afc1eddfd09f4436dde6f79eeec407a43851e1c7`, schema 3, attempt 1, failed, validated |
| Root thread | `01a1371c-24b8-7ac0-ab2d-5ed7a6bb2d4b` |
| Initial goal digest | `78db20d4c67a3475d3113a74ea279addf263d17775c471c03edff91ffe2d6121` |
| Retained policy | `delegated`, lead `gpt-6.1-sol` / `high`; full direct-team snapshot retained |
| Creation | Journal creating; manifest creating, initial goal attempted true, sent false |
| Roster | Same root, revision 17, architect0/implementer0/reviewer0 all ready |

The receipt error is specifically terminal reconciliation:
`undefined method 'capture' for nil`. This is after the ordinary initial-goal
ensure step in `Runner#start`. The attempted marker must remain intact; do not
interpret `initial_goal_sent: false` as permission to send another request.
The retained roster also prevents ordinary recovery from replacing a missing root.

The selected raw Ruby helper is
`PACKAGE/libexec/workspace-portal/.dev-session-wrapped`, not the shell wrapper.
Its SHA-256 is
`180c80420c6f444a2d939b44f930fbc0df8c1921cbdda6726564345b235119f1`.
Comparing its complete body with the reviewed a10af6c4 source, excluding only the
shebang, showed exactly this change:

```diff
-      output = @runner.capture(
+      output, = @command_runner.capture(
```

The surrounding provider invocation, output-size and argument validation are
unchanged. Preserve them.

## Narrow launcher

Use a reviewed/checksummed operational launcher owned by this initiative. It is
not installed, registered or made available as a general recovery mechanism.
Do not modify any Nix-store file or application worktree. Keep goal/preset
temporary files private, and never print their contents or provider arguments.

1. Snapshot the exact receipt, `.complete.json.request` binding, creation
   journal, manifest, tracking directory device/inode and team roster identity
   into private recovery evidence. Preserve originals. Recheck the expected
   receipt ID/attempt/state, schema, slug, goal digest, direct-team equality and
   root identity immediately before execution. Stop if they no longer match.
   Require no concurrent portal retry or other recovery of this slug.
2. Run with the selected package's Ruby and required wrapper tool environment.
   Load `PACKAGE/libexec/.workspace-host-wrapped` as a library, using a launcher
   name without `workspace-host` so its main guard does not dispatch a CLI.
   Resolve the real registry entry through that Host; do not fabricate runtime
   socket, authority, state, provider or profile paths.
3. Enter the installed Host's
   `with_current_generation_lock(mode: File::LOCK_SH)`. Require the frozen
   package and profile token, including rejection after a switch/rollback while
   waiting. Keep that shared lock through the ordinary CLI invocation.
4. Obtain environment, private command and full arguments from the installed
   `dev_session_invocation(entry, argv, transition_lock: true)`. This retains
   `--require-runtime`, selected package/token, transition lock, authority,
   tmux/App Server sockets, Codex version/command, portal command and extension
   providers. Use the returned environment for the CLI and its subprocesses.
   Do not suppress provider admission or inherit another session's identity.
5. Load the selected raw helper in the same process with only the exact reviewed
   line correction. One bounded implementation is to verify its whole-file
   checksum and the expected method fragment, replace that fragment once in
   memory, then evaluate those bytes with the **installed raw filename** as the
   source filename. This preserves `require_relative` and package-relative
   behavior. Verify the corrected body equals the frozen reviewed source body.
   Do not load the entire candidate helper or override recovery methods.
6. Call `DevSession::CLI.new(arguments, env: environment).run`. Its own shared
   transition lock and `validate_host_generation!` remain enabled, followed by
   the normal creation-then-slug locks. Propagate its exit status and retain
   bounded private stdout/stderr. No direct calls to readiness writers.

The shared Host lock is compatible with the raw CLI's shared lock. Do not
pre-acquire the creation or slug lock in the launcher: the ordinary command
owns their order and must release the slug lock around initial-goal
reconciliation. Do not hold an exclusive package-transition lock.

Construct the trailing ordinary command exactly as the portal does:

```text
start 2026-10-12-streamline-vpsadminos-config-imports
  --as-is --exclusive --no-attach --json
  --goal-file PRIVATE_GOAL
  --team-preset PRIVATE_FROZEN_PRESET
  --model gpt-6.1-sol --effort high
  --creation-receipt-id a9ea3ef892d5344be881fca8afc1eddfd09f4436dde6f79eeec407a43851e1c7
  --creation-evidence ORIGINAL_COMPLETE_EVIDENCE_PATH
```

Copy `receipt.goal` bytes to PRIVATE_GOAL and `receipt.directTeam` to the preset
file. Compare them with the original request/binding/journal using the runtime's
normal goal normalization and complete preset equality. Do not resolve today's
`--team delegated` catalog, change effort to current defaults, reconstruct member
instructions, select a new slug after midnight, or generate another receipt.
The request kind is `new`, so no source-session override belongs in this command.

The original completion path is beneath
`/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/creations/`
and named `SLUG.RECEIPT_ID.complete.json`; its existing `.request` sidecar is
authority, not a file for the launcher to rewrite.

## Completion, retries and deployment

Before launch, prove the recorded root is still materialized at its exact cwd
through the selected native reader; do not infer this solely from YAML.
The normal recovery must retain that root and all member thread IDs. Its
`thread ensure-initial` checks the existing first request against the original
goal. Because the attempted marker is already true, the retry must not acquire
fresh/unmaterialized submission permission. Missing or ambiguous history is a
refusal to investigate, not grounds to reset that marker.

The ordinary command reconciles the existing terminal with the corrected
provider arguments, publishes runtime authority, marks the manifest and journal
ready, removes only its normal transient start state, and writes schema-3
completion evidence. Reapplying the saved direct-team preset uses its normal
idempotent roster checks. No user/team settings are refreshed.

After CLI success, request the existing authenticated creation status endpoint
`GET /api/sessions/SLUG/creation`. This is an intended state reconciliation:
`currentCreation` calls `proveCreation`, checks matching tracking identity,
root, goal and complete direct-team roster, binds retained uploads and saves the
original receipt as ready. It does not invoke creation again. Confirm receipt
ID and attempt remain unchanged, error clears, and the evidence still binds the
original root and request. Do not POST `creation/retry` merely to clear the UI.

If the launcher stops or fails, retain all journals/evidence. Reread the actual
state before deciding whether another exact invocation is needed. If ordinary
completion evidence already exists, try portal reconciliation first. An exact
CLI retry uses the same receipt/goal/preset and existing journals; it cannot
change the accepted request. A new refusal has to be diagnosed.

After both ordinary creation and portal evidence are complete, repeat the
original deployment preparation from the frozen creation-fix source, under its
existing reservation and transition guards. Recovery may leave the root busy
with its original work; a subsequent idle/active-turn refusal remains valid.
Wait through the normal deployment policy rather than pausing or killing that
conversation to make activation pass. No merge occurs before the required fix
deployment succeeds.

## Validation and limits

The reviewed provider tests and recovery VM cover the correction and ordinary
creation contract. Before this live invocation, check launcher syntax, exact
single-replacement/body equivalence, selected profile/token/registry checks and
argument construction without calling `CLI#run`. A focused disposable harness
should verify no generation/receipt/goal/preset option is omitted; use the normal
review rule for any substantive launcher logic. A fresh utility watcher owns
long/uncertain monitoring; the parent owns launch and diagnosis.

This designer performed no native conversation RPC, recovery mutation,
application edit or live test. Materialized-root/first-message proof, live
generation token, current receipt/roster hashes and absence of concurrent retries
must be established by the parent before launch. The existing failure strongly
locates the error after initial-goal handling, but is not itself that proof.

No persistent schema, reader, profile, package or protocol changes are needed.
The one-process correction ends with the launcher. The original authorization
does not extend recovery to other slugs, permit new conversations, release the
coordination reservation, or bypass later deployment checks.

