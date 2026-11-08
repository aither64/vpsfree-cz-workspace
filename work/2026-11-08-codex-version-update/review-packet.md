# Combined final review — Codex 0.167.0

All intended project changes committed and quick checks passed; four feature
worktrees clean and exact SSH heads independently verified by lead. No final
native/integration/build/activation/merge has run. Review is independent final
review, not early/advisory-only review. Sources below are final; older heads in
owner receipts are historical preparation, not review targets.

## Outcome, scope and reviewer

User requested latest Codex on aitherdev and in dev-workspace/codex-web, using
vpsfree-cz-configuration for aitherdev. Frozen latest stable0.167.0, tag commit
086ccc833bc9cf01024ad2dd6af7dbd421b6bf9a, llm-agents
d960982d3b05c294f3cf98cab3e23798548a0ced. Native SHA256
13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10.

Acceptance: preserve strict0.163 and prompted0.164/0.165 support, add exact0.167
prompted/native compatibility, align Nix/Go/vendor/host+profile inputs, preserve
fixed defenses/state/recovery, pass exact schemas/config/catalog and native
release gates. Necessary observed SQLite cold-start correction included because
CI/current/base reproductions exposed supported startup contention.

Non-goals: new upstream capabilities/approval UX, protocol/client redesign,
provider/packaging rewrite, unrelated inputs, new coordination/lifecycle policy,
confctl metadata fixes. Deployment authorized; no default integration approval.

Risk high: protocol/native/state compatibility and host/profile rollout/recovery.
Assign reviewer0, retained gpt-6.1-sol/xhigh, read_only, exact native thread
01a1bd45-41c9-71e0-ab51-f96af1e8fada, independent of authorship and ready.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review SKILL and all four references; perform review directly.
Trusted local development-host operator; remote HTTP/browser users untrusted.

## Final ranges and complete source series

All worktrees below under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/.

| Repository / worktree | Source base | Final head | Complete source series / diff |
| --- | --- | --- | --- |
| aither64/codex-web / codex-web | dd90fb4308ba85617ee2a4267cc835aa9a4f11ce | f78eae3415d20b98503f11e9fe251e3111bfe4da | 7e3143bd508153d8c1860b2a916029ee9b8c455b compatibility; f78eae3415d20b98503f11e9fe251e3111bfe4da SQLite startup;11 files +227/-70 |
| aither64/dev-workspace / dev-workspace | 32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6 | 71654e18c5558c6b8b5cb3f33bfedced7fab727d | one runtime/naming update;14 files +57/-56 |
| vpsfreecz/vpsfree-cz-configuration / vpsfree-cz-configuration | 1072f89f932ad570fb6d14007387d230549ccd14 | ec1ccce401f81d604cd059d159ca6033df07f2a0 | 56c8557ac1b7041ff5cf086c5f219104196448a4 llm channel; ec1ccce401f81d604cd059d159ca6033df07f2a0 runtime channel; only flake.lock +26/-26 |
| aither64/vpsfree-cz-workspace / workspace | 8aae9bd4af090260a92ec0296472fadce13c6cd7 | 3f813d5862c1a29d8dd34bd78863b5dfba38767a | one nested runtime pin;flake.nix/flake.lock +19/-19 |

Inspect complete series and final diffs at these ranges, not only latest commit.
Workspace remote default0c112efeb3e88b62ca0d48feb532bab93303735c also precedes
initial own tracking527362b66eb903819ccb13ebb1e62495887195ca and inherited shared
coordination8aae9bd4. Inventory this ancestry by metadata only; peer tracking
content is outside authorized scope and must not be read. Actual source diff
8aae9bd4..3f813d586 contains all workspace functional changes. Own plan/state
and receipts under work/2026-11-08-codex-version-update are authorized context.

## Consolidation and migration provenance

W's two commits have independent purposes: compatibility update and observed
startup correctness. No obsolete iteration/fixup or pin stream remains. R has
one final update selecting only Wf78eae3. Initial uncommitted W7e3143 pin/vendor
preparation never entered R history. R's first published c92d539 was amended
before review/deployment for stale postFixup .165 assertion; final expectation
derives exact text from selected codex.version, naming remains explicit. C's
runtime stream637103e4 was regenerated from original runtime source into final
ec1ccce4; llm stream56c8557a unchanged. S64fbbad was amended into3f813d586.
Old ranges/source receipts/range-diffs retained in owner evidence. No intermediate
revision deployed/released; no supported boundary requires superseded pins.

No new migrations/schema/state formats in any branch; no migration history
rewritten. W1 only moves existing sorted context-aware predecessor locks before
lazy SQLite bootstrap/WAL; same WAL/FULL/timeouts/max-one connection, exact import
identities/backups/fences/receipt errors/recovery. No new lock/retry layer.
Upstream78 SQL migrations unchanged; rollout/replay changes still require .165→
.167 disposable state tests. Old-reader observation does not establish downgrade
write safety. Recovery forward-only, preserve native roots/generations/journals.

Require explicit independent whole-branch history, each repeated-update stream
consolidation, and migration/no-migrations conclusions before readiness.

## Components and consumers

codex-web owns public App Server client/prompted utility contract. Runtime imports
it through actual Go/Nix pins and bundles canonical Luna catalog. Configuration
consumes runtime host module/mkCodexPackage and independent system llm-agents.
Workspace composes unchanged vpsFree extension with direct nested runtime override.
System substrate precedes dependent user-profile activation; application not
installed into system config. Current extension f8da821e3c76e26e73aa9d89a712eab0e0faa319
and all siblings/follows preserved. Config and workspace final runtime/llm locked
objects match. Actual daemon identity separate from CLI/assembly identity.

## Documentation and verification evidence

- [Design](design.md), [state](state.md), [rollout](rollout.md).
- [W evidence](codex-web-evidence.md): full diff/commands/identities; exact native
  protocol+consumed fields and55 fixed config restrictions pass; reproducible
  catalogs unchanged; full Go/tagged deterministic +109 browser pass. Original
  CI SQLITE_BUSY reproduced current2/20/base3/30. Deterministic held-lock test
  fails old source (28672-byte DB initialized), passes fix; bounded count100 cold
  conditional, storage/fence/cancellation and full quicks pass. Final W CI
 42533307656 success. W1 disk log omission honestly recorded; native tool evidence
  retained without redundant rerun. Docs reference.md, submission-storage.md,
  API comment and repository update skill changed with feature/test support.
- [R evidence](runtime-evidence.md): focused naming Go, tagged compile, local
  protocol, Ruby3tests119assertions, pin/module/Node/diff checks pass; fresh unique
  absent-before-build vendor proof passes with final digest
  sha256-jUWhtHeiuyvh4Rzf/0KePGFrG72pNimtH6GBKJhRVkk=. Narrow postFixup fix
  evaluated/script bash-n and exact dependency byte-equivalence proof; reused
  unchanged checks. Docs codex-package.md/session-preparations.md updated.
- [C evidence](configuration-evidence.md): active hooks/generated messages,
  graph/eval/diff pass; complete unchanged DeepSeek TOML exact Draft7 schema and
  private native catalog load pass, malformed catalog negative rejects. Provider
  call still post-activation. Pure channels need no new reusable docs.
- [S evidence](workspace-evidence.md):35nodes/all edges+follows/extension/six
  sibling closures preserved; exact joint deployment checker and full C/S locked
  runtime+llm equality pass; clean committed-source eval. Pure pin no new docs.

Required post-review gates: namespace ownership; .167 prompted low/high/native
question/cancellation/retry/teardown; conditional steer; .165→.167 resume/fork and
separate old reader; managed naming lifecycle/failure/forced-exit/ordinary daemon
continuity in disposable VM; packaged/composed checks; exact system/profile builds.
No fake/schema pass claims native isolation or real-provider adherence.

Disposable support harness runtime-naming-vm.nix SHA256
4384c86e11826b288cc3928d8a6a56af3ac2bc43f55ddc8954395e4cf7ba72b4;
review it with committed fixture guards and final head binding in R evidence.
It is session-only raw verification support, not a new installed subsystem.
Retains prepared-source closure, exact package/fixture/native/catalog manifest,
protected ancestors, UID1000/systemd/cgroups, guest-private state and denied-canary
firewall. Verify graph/kernel cache before its post-review build/execution.

Final R CI42534510998 attempt1 for71654e18 observed separately; old42533810335
cancelled after archived failed fixup logs. Current CI outcome not yet known.
An unavailable managed observer is a monitoring limitation, not passing evidence.
