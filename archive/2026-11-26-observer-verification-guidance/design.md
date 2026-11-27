# Observer verification guidance

Status: sufficient brief settled; ready for lead acceptance and allocation to
implementer0. No design blockers. Architect0 owns this document; lead owns
tracking, allocation and acceptance. Initial tracking commit: `51557ce2f`.

## Scope and edit boundary

Improve the observer's advice when costly verification cycles, growing
verification infrastructure or serial discovery of related defects delay the
user's goal. This is an instruction change, with no new runtime behavior,
verification framework, telemetry, approval gate or live team reconfiguration.

One implementation package, owned by implementer0 in the lead-provided workspace
feature worktree:

- `config/agent-teams.nix`: revise only `observer.instructions`.
- `docs/agent-teams.md`: align the existing verification paragraph under
  **Independent progress observation** and, where needed, clarify the existing
  retained-instructions paragraph's catalog/refresh distinction.

Peers: architect0 for routine technical clarification; lead for scope,
ownership, acceptance and any consequential deviation. No parallel writer is
needed. Initial tracking is committed; implementation depends only on lead
acceptance and the assigned feature worktree/commit window. No generic-runtime,
flake, test-harness or other-role edits are required.

## Intended advice and preserved invariants

The prompt already covers cumulative test/fix cost, focused checks, completed
failed-job evidence, known-fix batching and necessary long checks. Strengthen
those passages rather than layering on a second workflow:

1. Challenge repeated costly runs revealing problems one at a time and
   verification infrastructure growth disproportionate to the delivery risk.
   Judge accumulated cost and new information, using available evidence without
   inventing timings or summing overlapping work.
2. Ask the lead to reassess the implementation/design and verification strategy:
   distinguish a product/design flaw from a test-environment problem, simplify
   the approach where warranted, and identify what uncertainty the next check
   actually resolves. A sequence of small fixes alone need not resolve the
   concern.
3. Recommend bounded diagnosis of the shared cause and related affected paths,
   then batch related fixes before another expensive run. This goes beyond
   combining only already-known fixes, without demanding an exhaustive audit or
   preventing a genuinely independent fix from proceeding.
4. Prefer the smallest faithful existing check against the real failing
   interface/dependency. State its expected cost, evidence and limits; reuse
   unchanged passing evidence within its proven scope. Avoid turning incidental
   environment trouble into a verification-infrastructure project.

Keep required independent review and full final acceptance checks. Faster
diagnostics must preserve assertions and report untested behavior honestly.
Necessary long checks with a concrete acceptance purpose remain legitimate.
Keep the observer read-only/advisory: no editing, running checks/builds,
assigning work, canceling development checks or waiving requirements. Preserve
phase-aware assessment, safe dependency release, stable concern keys,
evidence-based resolution, delegated-ownership advice and cross-session read
boundaries. Recommendations use the existing concern/lead-response workflow.

## Compatibility, deployment and recovery

No schema, persisted format, API, CLI, protocol, generated client, Nix option,
role/model/effort/access setting or scheduling behavior changes. All seven
observer-bearing presets inherit the same role. The evaluated current prompt
is 4,021 UTF-8 bytes; the existing catalog check caps role instructions at
4,096 bytes. Condense existing wording while preserving its meaning; do not
raise the cap or alter checks to accommodate this change.

The pinned generic runtime is
`2a1d58df7c3bb845da4d286ef38989bae01da4a0`. Its
`portal/internal/progressobserver/instructions.go` refreshes exact historical
trimmed-text hashes through `RefreshedStockInstructions`; it does not import
the latest site-catalog prompt into retained observers. The current site's
trimmed prompt hash is
`9a013a6f45f526c3250c4445c1fed4675240082d3320cc28bc6d1df8530382e4`,
which is outside that recognition list. `refreshProgressInstructions` in
`portal/internal/web/progress_observer.go` applies recognized refreshes only
through the existing idle-thread/pending-submission safeguards. Leave all of
that code and its historical fixtures unchanged.

The source update will reach newly selected observers after a separately
authorized package deployment. Retained observers, including this session's,
will not automatically acquire it; historical stock refreshes still use the
runtime's specific migration targets. Custom instructions remain retained.
This limitation is deliberate within the requested source-only boundary.
No deployment, live prompt replacement or integration is part of this package.
Reverting the two source edits restores the prior catalog/docs for future
deployment. Package recovery follows the runtime's forward-only procedure and
does not rewrite already retained member prompts.

## Acceptance, checks and evidence

Accept when the prompt and guide explicitly cover design/strategy reassessment,
verification-infrastructure growth, faster faithful diagnosis and shared-cause
batching, while preserving the invariants above. Source changes remain within
the two files, with only observer instruction values changing in the catalog.

Use the smallest quick checks; no builds or long suites are needed for this
prose-only boundary:

- Evaluate `config/agent-teams.nix` with `nix eval --json --file` and compare
  base/head catalog values: only observer instructions may differ; all seven
  observer-bearing presets remain identical, with nonempty text at most 4,096
  UTF-8 bytes. Evaluation establishes syntax without building a package.
- Run `git diff --check` and the existing focused
  `test/agent_instructions_test.rb` using the repository's declared Nix
  environment (or its documented interpreter provision). No new string-matching
  tests or launcher are needed. Preserve required commit hooks.
- Inspect the final prose against the acceptance list, including the retained
  prompt limitation. If an existing check fails, diagnose it within this
  package before proposing any broader run or scope change.

Implementer supplies exact base/head, changed-file inventory, commands/results,
prompt byte count and catalog comparison, known gaps, and whole-branch history
provenance (no migrations or runtime deployment). Lead invokes the mandatory
independent final review after all intended changes are committed and quick
checks pass. This planning brief itself needs no automatic review. Escalate any
new concrete risk that genuinely requires a build instead of adding one by
default. Stop investigation at this established boundary.

## Authorized deployment addendum

The user subsequently requested deployment and specified deployment through
`vpsfree-cz-configuration`. Workspace source is already reviewed and integrated
at `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`. This addendum supersedes the
earlier source-only scope only for deployment. No new source edit is proposed.

**Release:** sufficient operations brief settled for implementer0's preparation,
build/check evidence and diagnosis; lead accepts results and owns activation,
machine claims and release. Activation remains blocked on the matching-source
prerequisite below. Architect0 does not duplicate that investigation.

### Configuration authority and prerequisite

Follow the configuration repository's AGENTS.md and established operations:
`docs/operations/workspace-coordination-aitherdev.md` (read at local master
`86e19685313270d88e4db30038c056ce4b807abd`) and the application-only rule in
`docs/operations/codex-providers-aitherdev.md` at the registered source. The
former is absent from current `origin/master`; record that distinction rather
than treating the two revisions as interchangeable. The selected package's
`workspace-host coordination guide` governs claims, recovery and prompt release
after verified deployment plus integrated lineage; its rule supersedes the
older runbook's instruction to retain ownership for human review.

The configuration channel `dev-workspace`, role/input `devWorkspace`, selects
the host module/runtime contract. The separate composed workspace source selects
the application. Configuration mediation does not require rebuilding the system
when its effective module and deployed host contract already match.

Concrete unresolved prerequisite, owned by implementer0: the new configuration
checkout at `1e43e2e18c85cf1fc63f31327d1f8e5eb953eab8` locks `devWorkspace` to
`e3102d0b7bc0e8904388d8019847df24f233d3b1`, while the reviewed workspace locks
`vpsfree-dev-workspace/dev-workspace` to
`2a1d58df7c3bb845da4d286ef38989bae01da4a0`. Establish the exact live host/current
configuration identity, effective machine inputs and matching committed source.
Do not assume that a root lock, revision label or older local branch proves the
deployed module. Do not silently bump pins or build a system to resolve this.
Return any required configuration change/system activation to lead as a concrete
scope dependency. A necessary pin uses the existing confctl channel, with normal
review and separate configuration integration authority.

### Preparation and ordinary activation

Use these session-owned source paths; the configuration revision may change only
after the prerequisite is resolved and accepted:

```sh
observer_workspace_source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/workspace
observer_config_source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/vpsfree-cz-configuration
```

In the configuration's declared environment, run the existing cross-repository
contract check and prepare the application, before machine ownership:

```sh
nix develop "$observer_config_source" --command ruby \
  "$observer_workspace_source/bin/check-dev-workspace-deployment" \
  --workspace-root "$observer_workspace_source" \
  --configuration-root "$observer_config_source"
nix develop "$observer_config_source" --command nix build \
  --no-link --print-out-paths --no-update-lock-file \
  "$observer_workspace_source#default"
```

Build only after the source/host comparison establishes this application-only
route. Use the monitor skill for the build/uncertain checks: implementer0 owns
diagnosis and acceptance evidence; a fresh installed-policy verification utility
only executes/observes its bounded batch. Keep the parent active for native
delegation, account for all command effects, and preserve the visible fallback.
No full check suite, new fixture, kernel/system build or repeated baseline-failing
instruction suite is required by this prompt-only package. Reuse reviewed checks.

Retain exact workspace/configuration heads, complete locked input graphs with
revisions/content hashes, relevant effective machine inputs, candidate store path
and installed descriptors/catalog. Compare native executable, launch arguments,
capacity and live-switch policy with the selected package/launch evidence.
Current selected package is
`/nix/store/3y9ns5h3raj9zszrwcr5pgvf9gng8q4b-dev-workspace-0.2.0`.
Preserve its recovery roots and capture current profile/system identities.

Lead acquires a fresh schema-2 claim through **dev-session coordination**, with
no repository claim, selecting registered repository
`vpsfree-cz-configuration`, selector `cz.vpsfree/machines/aitherdev`, adapter
`confctl`. Installed profile identity is
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`;
legacy `machine:vpsfree:aitherdev` is its bridge, not a substitute new request.
After authoritative `held` status, run `verify-machine` once for this committed
batch. Then the lead performs the configuration-mediated application selection:

```sh
nix develop "$observer_config_source" --command env \
  DEV_SESSION_SLUG=2026-11-26-observer-verification-guidance \
  DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  DEV_WORKSPACE_CLAIM_ID="$observer_claim_id" \
  workspace-host switch --source "$observer_workspace_source"
```

Use the ordinary selected host command, with the same prepared source; no private
helper, maintenance enablement, forced restart or lifecycle action. Compatibility
refusal or an unexpected native-changing transition returns to diagnosis under
the original operation. If host change proves necessary, the config runbook's
confctl dry activation/no-reboot switch and both system-path checks precede this
application switch; that is a lead-accepted additional package, not assumed here.

### Minimal post-activation acceptance and recovery

Check `workspace-host status` and the actual selected profile target against the
prepared candidate. Compare its installed `agent-teams.json` observer text with
the reviewed catalog (4,087 bytes, seven identical observer roles); preserve all
other settings. Verify active router, portal and coordinator units, successful
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/healthz`, and the existing
session page/roster/conversation access. Check naming availability using existing
status evidence and unchanged native/runtime identity; do not create a trial
session. Compare Codex/tmux process and socket/launch identities with preparation
to establish continuity. Retained observer prompts remain unchanged by design.

Record command results, exact application/profile and both system store paths,
source/input graph, repository/target aliases and candidate/final heads in the
existing session evidence. Zero switch exit or profile selection alone is not
full acceptance. Read bounded relevant service diagnostics when a check fails;
do not add a verification framework or rerun costly checks without new evidence.

If interrupted or uncertain, keep the exact machine claim, source, candidate,
pending target and original journals. Reconcile command effects, then retry the
same ordinary switch only under its forward-recovery contract. No rollback to an
older workspace package, state deletion, forced service restart or replacement
operation to hide uncertainty. No new fixture or live team reconfiguration.

Before release, lead freshly proves the complete deployed source/input lineage
is integrated into each approved remote default, including any configuration
change that was actually needed. Inspect authoritative status of the exact owned
claim and settle all command effects. Once deployment and lineage are verified,
release promptly and verify `released`; no separate UI acceptance is needed.
Missing lineage or failed/uncertain deployment keeps ownership held. A later
deployment requires fresh ownership. Release leaves this session open.

## Current-generation refresh — 2026-11-27

This section supersedes the November 26 candidate/baseline selection; the
configuration-mediated activation, ownership and recovery boundaries still
apply. The accepted old candidate must not be selected against a changed live
generation. Existing review of the observer text remains useful within its
scope; it does not establish a new package's transition compatibility.

### Public source decision and package boundary

Fresh SSH inspection found workspace `origin/master` at
`79478c47f0e7ac392c4e9c7ca04c6c153393ed19`. It contains the exact reviewed observer
instructions/docs from `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`, but the root
runtime selection remains `2a1d58df7c3bb845da4d286ef38989bae01da4a0`. Therefore
that published root is not an already aligned source for the selected host
runtime `f3bd843f9858b87cef66d0949706f8af16ba9b13`.

The smallest candidate alignment, if the transition prerequisite below is
satisfied, changes only root `flake.nix` and generated `flake.lock`: select that
exact host runtime through the existing nested URL and run
`nix flake update vpsfree-dev-workspace/dev-workspace`. Preserve extension
`bf12ac71a8a00b1581eed5352f99c1b2daaeff5b`, other independent inputs/follows edges,
the reviewed prompt/docs and newer shared content. Expected transitive runtime
inputs must be recorded, not treated as unrelated lock churn. Preserve the
integrated `maintenance/2026-11-24-pi-discard/` sources unchanged; repinning its
old site input would alter a separate recovery artifact.

Implementer0 owns the conditional source/preparation/check package in the own
workspace worktree, after lead acceptance. Advance from the preserved integrated
history to the fresh approved baseline; never rewrite the already merged prompt
commit. No configuration change, system build, generic-runtime edit, bridge
implementation, new test infrastructure or live member reconfiguration is
included. Architect0 owns this brief; lead owns release of its dependency,
scope decisions, review invocation, integration/activation and claims.

### Transition prerequisite and stopping condition

The current installed `workspace-updates.md` adds the public epoch-2 discard
bridge contract. Keep the exact bridge selected until the original operation's
cleanup is positively confirmed. The original owner/administrator must supply
authoritative completion-audit, matching terminal-mapping, confirmed marker
cleanup and exact startup-grant retirement evidence. Marker/grant absence,
successful admission or an active service alone cannot establish that proof.
This brief records no private operation identity, content or completion claim.

Stock `f3bd843f` supplies the relevant ordinary reader contract:
`portal/internal/web/preparation_store.go` accepts schema-3, snapshot-free
`terminal/cancelled` mappings and reads them at startup/transition;
`portal/internal/web/preparation.go` returns terminal status/conflict before
retry launch and skips terminal records during reconciliation. This public code
evidence does not certify cleanup of a particular live operation or all other
package-transition prerequisites.

Source alignment/build release remains conditional on positive original-owner
evidence and a supported successor transition. If that evidence cannot be
established from existing receipts, stop at the external dependency. Do not
reconstruct recovery, invoke private helpers, retry creation, discard, archive,
delete, restart services, retire a grant or modify peer records. Those actions
are outside this observer task. Do not remove temporary recovery behavior merely
because the root and host runtime revision strings can be made equal.

### Acceptance and smallest verification

Once the prerequisite is accepted, implementer0 first resolves immutable
configuration source `109d789f0a4ee875f8bd27a0b72ea76c38ee234a` and its complete
effective input graph using the already established current-host evidence.
Use its declared tools environment from the own writable configuration checkout,
with the recorded `path:` source form and runtime-only `GEM_HOME`/`GEM_PATH`
removal where required. Do not infer the installed application root commit or
effective graph from an embedded skill-source reference.

Quick checks: inspect the two-file semantic pin diff; pure-evaluate the candidate;
run the existing configuration/workspace matching checker; prove catalog equality
to the reviewed seven-role 4,087-byte observer result; and check whitespace and
required hooks. Compare immutable current/candidate native executable, launch
policy/arguments/capacity, Pi/runtime and package-transition contracts. Account
for every changed runtime component, including any permitted retirement of the
temporary bridge. Unknown effective provenance or a substantive incompatible
delta returns to lead before a build, not to a new recovery project.

Commit the final narrow candidate and give lead the exact base/head, full diff,
input identities, compatibility evidence and no-migrations conclusion for the
mandatory-review decision. A new runtime selection is not covered merely by the
earlier prompt review. Publish the feature branch; any new default integration
needs explicit workspace/master approval for this changed patch. Keep the
already integrated prompt history intact.

After applicable review, perform one monitored application build using the
immutable candidate and matching configuration environment. Prove that the
ordinary switch's real-directory source evaluates to that exact derivation.
Reuse unchanged passing evidence; no system build or unrelated suite is needed.
Lead must obtain fresh machine ownership and recheck generation freshness before
activation. Repeat the existing post-activation catalog, health and continuity
checks against the new candidate, with fresh complete lineage and release proof.
If another generation changes while waiting, release an unused claim and return
to preparation rather than deploying a stale artifact.

## Current installed delivery — later 2026-11-27 checkpoint

This checkpoint supersedes the proposed `f3bd843f` alignment and its build/switch
dependency. Implementer0's fresh inspection establishes that selected package
`/nix/store/6j7rpx2j176blr46602kzzpb8ycm1mwp-dev-workspace-0.2.0` already contains
the exact reviewed observer text in all seven presets: 4,087 UTF-8 bytes each,
SHA256 `6057ebc7639a99651ae5ca4b70d85f8761537cdf3bfa43beedfc020ee793d011`, with
reviewed catalog digest
`4ae58b06cf34c345d952f2ce0288a78d739c5ee06584292062220a217e7f7922`.
The smallest route is acceptance of existing delivery, with no source edit,
build, redeployment or new machine claim.

Published workspace root `0d24fd5596e65ae1e918e9441142d1e11bf418ec` retains the
reviewed prompt/docs byte-for-byte and now selects runtime
`bbe27c6ffb5f367e7be9a4ce45bffdf34185854f`. Implementer0 establishes the same
effective host runtime under clean configuration
`a3af000f116bca48dd59b9fd3f0ca46fd433a640`. No alignment or system change is
needed. Preserve maintenance sources and all unrelated inputs.

The selected ordinary package's public update guide no longer contains the
temporary bridge's exact-package hold section. This observation and the actual
installed feature remove the need for this initiative to prepare a transition
away from that bridge. They are not retrospective proof of another operation's
cleanup. Do not reopen that separate operation or demand new recovery work to
re-deploy an already installed prompt. Any future transition retains the selected
package's ordinary admission and original-owner recovery contracts.

Remaining owner/package: implementer0 completes bounded current-generation
health/continuity and source/input evidence; lead accepts delivery and updates the
existing rollout/state. Preserve the distinction between installed artifact and
Git provenance: package metadata does not publish the exact root application
commit, and an embedded skill-source reference cannot establish it. Where needed,
use a cheap exact-source derivation comparison to the installed deriver
`/nix/store/ifpsi7200wia0v0dcr091kgamq4w62wd-dev-workspace-0.2.0.drv`, without a
build, to establish a reproducible integrated source. Report any unmatched
provenance honestly rather than inventing the deployment's original Git head.
No new review of unchanged observer prose or further source package is released.

Current guide clarification: an ordinary switch that changes native invocation
can use managed maintenance even without `--enable-maintenance`; omitting that
flag does not guarantee an idle-only transition. There is no switch to run for
this installed-delivery acceptance. Session lifecycle and peer mutations remain
outside this task.
