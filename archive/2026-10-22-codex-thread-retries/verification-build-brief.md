# Verification and build handoff

Prepared 2026-10-22; **no test, evaluation, build, copy, claim or activation was
run while preparing this brief**. Commands below are an execution packet for
lead and fresh verification utilities after affected final review passes.
This supplements [native-verification.md](native-verification.md) and
[design.md](design.md), preserving their original evidence.

## Identity and release gate

| Component | Candidate identity | Status |
| --- | --- | --- |
| A codex-web | `c1f415ad5602c23e6443cced73cb59267a796f05` | Affected review accepted; native run 4 passed |
| B dev-workspace | `d819ad044ef7fcc7bb4a111dc7676fe251383249` | Affected review accepted; native run 4 passed |
| C workspace | `ebf6ab35c7754f9ac2e5474959259fdcef24a7c8` | Published clean final nested B/A selection; mechanical review reuse accepted |
| C configuration | `81d0e68c52762d3804e00e4c4ef99a421bafc05f` | Published clean final channel-managed B/A selection; mechanical review reuse accepted |
| Site extension | `767dfd587e346168e1443e65ccdb67ce748f3fe3` | Preserve unchanged |
| Native Codex | `0.163.0`, exact binary/hash in native brief | No native changes |

This table supersedes the historical candidate sets below. Evidence:
[native run 4](native-verification/run-4-d819ad04/result.md) passed every required
case with no skip/missing/failure; [C mechanical reuse receipt](c-d819-mechanical-review-reuse.json)
binds final W/C trees and original plus affected review. Full A/B checks are
owned by the running watcher under `verification-build/ab-d819ad04`; this brief
does not claim their result or repeat that work. Final W/C checks and exact
system/profile artifacts remain pending. Preserve reviewed ranges, complete
graphs and exact derivation receipts; source-tree similarity alone proves no
check reuse. A later head change requires refreshed scope/identity evidence.

The exact pinned confctl generation-name, metadata, configuration-commit and
health receipt sequence is in
[confctl-generation-receipts.md](confctl-generation-receipts.md). It supplements
the build/copy/activation flags below. Confctl commands must actually run with
CWD `$C`: `nix develop "$C"` selects an environment but does not change CWD.

The source-only [postactivation checklist](postactivation-acceptance.md) supplies
scoped service/router/conversation reads, authenticated browser acceptance and
the limits of model-free naming/retry checks. It is a prepared checklist, not a
deployment or acceptance receipt.

All commands use Bash, the declared Nix environment, and a unique owned artifact
directory. Set these literal paths in each assigned shell:

```sh
GROUP=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries
A="$GROUP/codex-web"
B="$GROUP/dev-workspace"
W="$GROUP/workspace"
C="$GROUP/vpsfree-cz-configuration"
RUN=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/verification-build/RUN_ID
MACHINE=cz.vpsfree/machines/aitherdev
```

Lead supplies actual final SHAs and a new RUN_ID. The assigned watcher may create
RUN privately (`umask 077; mkdir -p "$RUN"`). Capture complete stdout/stderr and
the exact exit status for each command, without a pipeline masking failure.
No command updates a flake lock. Source checkout must remain the reviewed one.

## Full packaged check coverage

Sources: each repository's `AGENTS.md` and `flake.nix`; B
`nix/ruby-checks.nix`, `nix/workspace-portal.nix`, `.github/workflows/check.yml`
and `docs/workspace-portal.md:1492`; W's four declared checks. The configuration
guide requires the scoped machine build in addition to flake checks.

First, at each final A/B/W/C root, `nix flake check --no-build
--no-write-lock-file --print-build-logs` validates outputs. This is a future
watcher command, not a claim that evaluation cannot realize dependencies.
Do not run it during this planning assignment. Then use the split batches below
instead of rerunning an additional full building `nix flake check` campaign.
Together these cover all declared x86_64-linux checks at the inspected sources.

**A, cwd `$A`:** both checks; default is also packages.default, so do not build
that alias again as another check.

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.default .#checks.x86_64-linux.generic-source
```

Default includes Go, protocol coverage and all declared conversation/browser
contracts, including retry UI. Native tests skipped in this packaged suite do
not establish native verification; the explicit native batch below is mandatory.

**B Ruby batch, cwd `$B`:** exported shards may run independently from A and
native fixtures. Aggregate `ruby-verification` depends on all 13 shards and
validates complete unique coverage; build it rather than rerunning the unsharded
Ruby suite. Individual shard outputs retain `timings.json`.

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.ruby-verification
```

Exported shard selectors: `ruby-dev_session-0` through `-3`,
`ruby-workspace_coordination-0` and `-1`, and `ruby-auto_archive-0`,
`ruby-workspace_host-0`, `ruby-coordination_claims-0`,
`ruby-coordination_admission-0`, `ruby-coordination_gc-0`,
`ruby-integration-0`, `ruby-integration_certification-0`. Prefix each with
`.#checks.x86_64-linux.` when assigning individual shard builds. Nix can realize
the aggregate dependency graph concurrently; no duplicate suite invocation is
needed. Packaged Ruby deliberately sets `DEV_SESSION_SKIP_REAL_TMUX_TESTS=1`;
that fixture policy is distinct from forbidden skips in selected native cases.

**B package and non-VM batch, cwd `$B`:** package depends on the same Ruby
aggregate, so the prior exact derivation is reused. It runs portal Go/browser
checks and the A pin/protocol coverage contract; it is also B's default package.

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.package \
  .#checks.x86_64-linux.codex-package \
  .#checks.x86_64-linux.ruby-source-filter \
  .#checks.x86_64-linux.host-module \
  .#checks.x86_64-linux.host-auth-benchmark \
  .#checks.x86_64-linux.host-package-contract \
  .#checks.x86_64-linux.extension-catalog \
  .#checks.x86_64-linux.agent-team-catalog \
  .#checks.x86_64-linux.user-namespace \
  .#checks.x86_64-linux.generic-source
```

**B VM batches, cwd `$B`:** separate from native App Server fixtures. Use
authorized KVM-capable local/CI workers; do not silently replace these with
unaccelerated runs or omit them because feature CI does not auto-run host jobs.
The first two can share one related watcher batch; archive and creation are
independent CI lanes. Do not change host device permissions in this handoff.

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.host-module-idempotency \
  .#checks.x86_64-linux.session-recovery-boot
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.session-archive-lifecycle
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.session-creation
```

**W composed checks, cwd `$W`:** these are distinct from generic B checks and
include site policy/catalog and cluster-provider composition.

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.deployment-contract \
  .#checks.x86_64-linux.agent-instructions \
  .#checks.x86_64-linux.agent-team-policy \
  .#checks.x86_64-linux.cluster-provider-composition
```

**C full declared checks, cwd `$C`:** no system activation.

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.nix-store-cleanup \
  .#checks.x86_64-linux.alert-recipients \
  .#checks.x86_64-linux.infra-monitoring-rules \
  .#checks.x86_64-linux.infra-monitoring-config \
  .#checks.x86_64-linux.vpsf-status-prometheus-rules \
  .#checks.x86_64-linux.vps-autostart-prometheus-rules \
  .#checks.x86_64-linux.process-count-prometheus-rules \
  .#checks.x86_64-linux.newadmin-prometheus-rules
```

Before launch compare final declared check names with this inventory. A new or
missing name is a coverage decision for lead, not a silent skip. Independent
batches may run concurrently within the retained watcher/resource policy; the
composed package's shared derivations should be realized once by Nix.

## Native and resolver evidence

Use the exact commands, binary, environment, synthetic failure payload and case
manifest in [native-verification.md](native-verification.md), substituting final
B identity. Keep A's six named subcases and both existing recovery/reconnect
tests. Every selected top-level/subcase must actually PASS in `go test -json`;
zero regex matches, missing-binary SKIP and package-only pass are insufficient.

Corrected B now has `turn_retry_native_integration_test.go` plus a native
receipt barrier proxy. Retain its actual lost-reply/client/controller restart
evidence. The ordinary retained admission regression is separately
`TestTurnRetryResolverRecoversExactNativeLedgerBeforeOrdinaryGate` in
`portal/internal/web/turn_retry_resolver_test.go`; do not claim direct
Controller.Step proves that web resolver gate. Its explicit evidence command,
cwd `$B/portal`, is:

```sh
nix develop "$B" -c go test -mod=readonly ./internal/web \
  -run '^TestTurnRetryResolverRecoversExactNativeLedgerBeforeOrdinaryGate$' \
  -count=1 -json
```

Reuse a final-head quick-check receipt for that selector if already complete;
do not repeat it without a changed source/failure. Owner must add the final I3
production-wrapper root/member MCP selector(s) to the case manifest before
final review/run. No helper-only test substitutes for actual settings -> active
QueueWithPolicy composition. Native fixtures use private state and loopback
synthetic providers, never registered workspace state, real keys or policy prompts.

## Identity receipts and reuse

For every batch retain final clean Git head/tree, source path/NAR identity,
complete semantic flake graph and locked revisions/narHashes/follows, Nix
version/system, check selector -> drvPath -> output paths, exact command/env,
exit/logs and native version/hash where relevant. Future receipt commands include:

```sh
nix flake metadata --json --no-write-lock-file "$B"
nix eval --json --no-write-lock-file "$B#checks.x86_64-linux" \
  --apply 'checks: builtins.mapAttrs (_: drv: { inherit (drv) drvPath outPath; }) checks'
nix derivation show --recursive DERIVATION_PATH
nix path-info --json --recursive OUTPUT_STORE_PATH
```

Repeat metadata/selector mapping for A/W/C as applicable. Keep exact input
derivations for Ruby source filtering; a portal-only change may reuse a shard
only when its drvPath/input receipt is identical and the prior successful
result exists. Tree equality, matching test names or a prior green branch is
insufficient. `ruby-verification` must prove all shard manifests exactly once.
Do not rerun known identical successful derivations for a moving revision label;
do not reuse changed derivations. Confctl embeds the configuration commit, so
final committed C source must be rebuilt even if its Git tree matches earlier
preparation. Preserve prior evidence, not just the latest success log.

## Artifact preparation: no activation

Use final C/W pins. Configuration channel `dev-workspace` role `devWorkspace`
and W's `vpsfree-dev-workspace/dev-workspace` nested input must both resolve to
final B; B must resolve final A. Extension and unrelated inputs remain unchanged.
From `$W`, in its Nix environment:

```sh
nix develop "$W" -c bin/check-dev-workspace-deployment \
  --workspace-root "$W" --configuration-root "$C"
nix build --no-write-lock-file --print-build-logs --json \
  --out-link "$RUN/workspace-package" "$W#packages.x86_64-linux.default"
```

This is the **composed user-profile application**. W aliases
`packages.x86_64-linux.vpsfree-dev-workspace` to the same derivation. Capture its
exact store path as PROFILE_PACKAGE and retain the output link/closure until
rollout/recovery obligations settle. The site checks may already have built this
exact derivation; requesting its output receipt does not require duplicate tests.

From `$C`, prepare the exact standalone NixOS machine and copy its named build
generation without activation:

```sh
nix develop "$C" -c confctl build "$MACHINE"
# Set SYSTEM_GENERATION to the exact name emitted by that completed build.
nix develop "$C" -c confctl deploy --generation "$SYSTEM_GENERATION" \
  --copy-only --no-reboot "$MACHINE" switch
```

Retain confctl generation metadata/digest, configuration commit, inputsInfo,
system toplevel, auto-rollback closure, evaluated machine mapping, immutable
confctl environment and copy result. Never use a moving/latest generation at
activation. Corrected source authority (read at configuration
`01634abe06fc618fd3d55fea1df455dbe574cbf0`):
`docs/operations/codex-providers-aitherdev.md`, section **Deploying a change**
(lines 21–65), owns the concrete machine alias, channel/runtime selection,
matching nested workspace input, build/copy, dry activation/no-reboot switch,
system-link verification and subsequent user-profile selection. The former
reference `docs/operations/workspace-coordination-aitherdev.md` does not exist
at this revision and must not be used as authority. Read configuration
`AGENTS.md` and `skills/update-aitherdev-codex/SKILL.md`; the latter routes to
`docs/operations/codex-deepseek-aitherdev.md` and the generic coordination and
recovery guides. For this unchanged-native, unchanged-provider feature, those
guides do not authorize extra provider requests or provider switching.

The configuration's locked confctl is
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`
(`sha256-gh1tmTv8aAO1OA3HX2NEYnRALMK2i666Lxey8hxD0QM=`).
Its `lib/confctl/cli/app.rb:340–395` declares generation/copy-only/reboot
switches; `lib/confctl/cli/cluster.rb:579–594` returns after copying and before
activation for copy-only (the one-by-one path similarly skips at 653).
These exact pinned source reads replace the earlier stale line references.
Confirm the
final C-pinned tool's `deploy --help` before execution; if its flags differ,
stop and reconcile the command, never substitute an activating command.

The workspace/user profile is local to aitherdev, so a locally built application
closure is already there and needs no profile installation for preparation.
If lead deliberately builds on a separate machine, copy only the prepared
application closure before claiming aitherdev:

```sh
nix copy --to ssh-ng://aither@aitherdev.int.vpsfree.cz "$PROFILE_PACKAGE"
```

No `nix-env --set`, `workspace-host switch`, confctl activation or remote service
restart belongs to this preparation phase. The application stays out of system
pins. Do not invoke legacy coordination prepare/approve/submit or private
activation helpers as a workaround.

## Lead activation sequence and recovery constraints

Planning only; lead owns activation authorization and effect reconciliation.
Read the freshly selected `workspace-host coordination guide` before use. During
this preparation it selected `/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0`
with catalog digest `sha256:a476a823824d95cb6ea7e995c786c11d6e8f4fb421f48fbc84e86d7292139b10`.

After review, checks, builds and copies, acquire a **machine-only** claim for
`vpsfree:aitherdev` (aliases `aitherdev.int.vpsfree.cz`, `$MACHINE`), empty
repositories array, fresh request UUID. Confirm exact claim status `held`.
Capture predecessor `/run/current-system`, `/nix/var/nix/profiles/system`, user
profile store path/token, active Codex binary, selected package/input graph and
live root/team identities before the first activation. Under the same claim:

```sh
# cwd: $C; exact prepared generation, no reboot, configured auto-rollback retained
nix develop "$C" -c confctl deploy --generation "$SYSTEM_GENERATION" \
  --no-reboot "$MACHINE" dry-activate
nix develop "$C" -c confctl deploy --generation "$SYSTEM_GENERATION" \
  --no-reboot "$MACHINE" switch

# Run on aitherdev after both system links prove the intended generation.
DEV_SESSION_SLUG=2026-10-22-codex-thread-retries \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID="$CLAIM_ID" \
workspace-host switch --source "$W"
```

The stable workspace-host command owns compatibility and transition journals;
its source build should reuse the prepared exact output. A changed predecessor
token/source/package/claim refuses and requires renewed preparation. System
activation precedes application selection. No reboot, default-branch merge,
session closure or machine release is implied by these commands.

Final runtime contract must publish `turnRetryStateSchema=1`, required final
provenance epochs/keyed charges and existing sessionRecoveryPolicy/native
submission schema 3. Preserve all lifecycle, generation and cold execution holds.
Final private schema rejects preliminary branch fixture state; none was deployed.
Do not migrate/reset records to silence a refusal. Once real retry state exists,
a package lacking its capability is unsafe; recover forward with the same or
reviewed compatible successor. Keep exact pending UUID/options and receipts,
enrollment watermarks, opt-out and quota. First deployment never revives an
existing failed task. System recovery preserves confctl auto-rollback and both
live/profile link evidence; uncertain remote effects retain ownership and the
original operation, not a replacement activation.

Trusted developer retention overrides the older guide's weaker release prose:
retain the physical machine until deployed feature lineage is integrated into
approved remote defaults, the user accepts the behavior on that machine, **and
the user explicitly directs release**. Idle time, review, reconnect, completion
or a green check supplies none of those conditions. No release command is part
of this packet. Integration needs separate approval.

## Post-deployment acceptance and watcher instructions

Lead checks exact selected system/profile/package/native identities and composed
graph, portal/router/coordinator health, naming backend readiness and existing
Codex/tmux/root/member continuity. Use supported status/health interfaces and
confctl's normal scoped health check (`nix develop "$C" -c confctl health-check
"$MACHINE"`). Do not expose credential values or read another session's private
history. Verify ordinary browser loading and authenticated controls on the
canonical portal and alias, without treating an unauthenticated redirect as
application health.

Live UI acceptance: lead/member retry capability visible and default-on;
persisted opt-out; countdown follows server time; cancel suppresses subsequent
work and reports unknown sends honestly; settings preserves the approved epoch
boundary; old failed tasks remain failed. Pending postdeployment retry intent
must survive an authorized portal restart with exact same receipt, while cold
and stopped threads remain held. Use an authorized disposable synthetic
acceptance context for retry errors; never force policy rejection with a real
model request or use registered live work as a fixture. Naming can be exercised
through the supported benign acceptance flow without accepting a created task
for automatic execution; record readiness/failure/manual-name fallback clearly.
Human UI/behavior acceptance is recorded separately from automated checks.

Fresh utilities follow `~/.codex/skills/dev-session-monitor/SKILL.md`: exact
retained watcher model/effort and installed execution policy; one owned operation
or related batch, exact cwd/head/commands/logs, no edits/diagnosis/retries/acceptance
or nested delegation. The lead launches mutation-bearing activation commands;
a utility may observe independently accessible logs/status. No watcher launched
by this brief. Stop/escalate unexpected local kernel builds unless an existing
documented kernel/cache exception applies. Stop an owned fixture on production
egress, foreign workspace/socket or credential access. Quiet output alone is
not a timeout; no unapproved host service/process termination. Report passed,
failed or incomplete, exact exits/selectors/revisions/derivations, elapsed time,
artifact paths and any still-running owned process. Preserve failed evidence;
lead decides diagnosis/rerun.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/>

## Historical first execution identities (superseded)

A d2d74f931cc50e39345c6c15931748062ee51951; B e0fb1238bd17cc3b29cc7d59ddaa9784c89ef939; W e6c2008a8f1215265fb8ceef3081a202570c30c6; C 49397f0d8ec0c2c33a4e8a0285843445068fe0ca. All committed/published/clean and quickchecked. Original independent review plus affected reports resolve all findings; last2 test-only fixture corrections directly inspected under step9. Final pin graphs independently reconstructed, one pin commit each, only runtime node changes from61de; A/extension/edges preserved. Final C receipt c-repin-e0fb1238.json and final-pin-inspection.json. Earlier candidate IDs/placeholders in preparation prose are historical and superseded by this exact execution set. Native/full package gates now released; no deployment approval inferred from verification itself.

## Historical native-run2 source set (superseded)

Use A b6d3a92ff85edbcd661b193c2319951eb4a71725, B3f2153a44e87bcd60c40ac5dcc660f214ccf04fa, W06ea83416387ebb16ecbb91acbf079cfdda1500b, C01634abe06fc618fd3d55fea1df455dbe574cbf0 for any next exact-source check. Previous e0fb/d2 source appendix is superseded after diagnosed native fixture corrections (A explicit empty environment, B actual-acceptance uncertainty/barrier diagnostics) and single consolidated final dependency pins. Public production review retained per narrow direct-inspection rule; full delta and graph receipts available. Runtime/library source changes require distinct derivation receipts, no previous success tree-only reuse. Full package and build commands still UNRUN, gated on native-run2 results.
