# Final independent review — G/H

Reviewer0, saved gpt-6.1-sol/xhigh/read_only, bound native thread `01a1de4d-3ae1-75f2-9b24-43ff50a436c6`; no override, fallback, nested reviewer or implementation authorship. Report returned through report_to_lead and saved by lead to preserve reviewer's read-only role. High-risk general, architecture/repetition, scope/proportionality and risk/compatibility lanes completed after the skill, all references, workspace procedures and all three repository-local instructions were read.

## Findings and lead disposition

No Blocking or Important findings. Reviewed implementation may proceed to planned post-review verification; this review is not deployment or final readiness evidence.

Advisory A1 (general/documentation; pre-existing/outside changed diff): configuration `docs/operations/codex-providers-aitherdev.md:17` describes whole-workspace switching after active work finishes, and line62 describes a guarded daemon restart. Current generic provider guide/scoped engine support active scoped switching without daemon restart. Existing site pin/deploy/recovery instructions remain useful. Reviewer recommends an optional future wording correction, with supported behavior authoritative in the linked generic guide.

Lead decision: accept A1 as a pre-existing optional documentation follow-up; do not expand this bounded helper rollout or add a real provider switch. No finding requires code remediation or another review run.

## Complete reviewed ranges

| Repository | Full base | Full head |
| --- | --- | --- |
| dev-workspace | 458c7857b942fb592607c83af7b5287a6c93ea96 | e96284d1a0484a01888a6d7166fcbd5f68855659 |
| workspace | aa9333916fdc1062755a88e1b8298b845ec2ccc4 | da432f0a2928bf296c497ec66a282e4ee61af960 |
| vpsfree-cz-configuration | 11ef63c5e173019b5312d672570158a0b0fb6dad | 9f7679c90bb3c7dc2070a611685e631a25e06a51 |

Reviewer independently inspected complete commit messages, full series and final diffs: one functional runtime commit/four files/+216/-12, one workspace pin/+5/-5, one generated configuration pin/+3/-3. Each base equals the merge base against locally recorded origin/master. All exact final heads/indexes/worktrees remained clean; no remote refresh was performed, so integration still needs fresh remote/target checks.

## Scope, correctness and architecture conclusions

Reviewed user scope from accepted Archive behavior through provider fix/deploy/merge direction against plan/state, G/H design, actual diffstats and milestones. Two input corrections, a small testable factory and focused regressions are proportionate. Archive, RetryStore, idle policy, diagnostics framework and native upgrades are outside the diff.

Traced production codex-provider command → providerCodexClient → scoped inventory → monitor project/metadata/bootstrap/archive proofs, plus Ruby scoped helper → codex_environment(entry) → capture_env!. Independently checked pinned codex-web91a17d00 headless/source membership: empty SDK source list rejects valid utilities; vscode matches existing workspace policy. Client retains explicit no-implicit-resume, submission identities, instruction preservation and no resolver/watch/question-answer composition. Canonical homes derive from registered workspace and override incidental variables. No validation/safety gate/public API/schema/permission/recovery path is weakened.

Go regression uses production factory and actual scoped inventory with retained monitor. Positive case allows active metadata/unrelated loaded identity; independent negatives cover empty source, missing home, wrong source/origin/CWD/ephemeral/history/bootstrap. Fake RPC rejects unexpected calls/transcript requests. Ruby uses actual subprocess boundary with absent/conflicting parent/host values, verifies all homes/scope arguments and restores ENV. Existing scoped checks cover busy/idle, unrelated-session isolation and lost-close recovery. No new framework/speculative abstraction is needed. Actual working-turn acceptance remains post-review.

## Consumers, graphs and history

Traced owner dev-workspace through workspace composition/unchanged extension and configuration channel/role/input to aitherdev module/native packaging. User-profile application selection is required; configuration alone cannot deliver the Go/Ruby fix.

Independently parsed complete committed lock graphs: runtime graph unchanged; consumer node sets/root/version/all edges/follows/every other node identical. Only intended runtime locked/original identities change. Both lock e96284d1 with narHash `sha256-7J2yBTO+gdq+B1bl9HWyPHOjaXXQKbjDbkKNviR8AT8=`. Extension/codex-web/llm-agents/native unchanged. Reproduced workspace lock SHA256 `37622d11fe1b9f116794755bc2116ab8195fbe1962a19583c3ba6b3189aee38f` and configuration `5ebd2b162fe19f23727436e8ea87a7382e7f47ea2f75bdc3e64605319f630d91`.

Explicit whole-branch conclusion: no obsolete unmerged approaches, fixup/tidy history, abandoned compatibility paths or transitional migrations remain. Functional behavior/tests belong together; each consumer pin remains independently reviewable in its repository. Generated configuration history is appropriately retained. No repeated dependency/channel/input/generated-update stream exists within any full range; each consumer selects the same final runtime once, so no consolidation outstanding. No migrations/schema transformations/provenance requiring intermediate history. Feature publication is not deployment/integration evidence.

## Documentation placement and preservation

Factory comment adequately preserves raw-client rationale; another feature page would duplicate it. README reaches generic docs/codex-providers.md for transition/source/identity/recovery/package contracts. Workspace deployment procedure and mkdocs-linked configuration operations guide own matching pins, host/profile ordering and forward recovery. Session execution/review records correctly remain outside reusable product/config docs. No moves/removed anchors/lost prerequisites/retired upgrades/weakened recovery warnings in diff. Placement/preservation sound subject to accepted pre-existing A1; no cosmetic expansion/backfill required.

## Evidence and residual verification

Reviewer inspected reported quick Nix Go PASS1.648s; Ruby12runs/80assertions PASS1.373s; formatting, final parity PASS0.19s, graph/Nix parse/channel/selector and configuration hooks. Did not rerun tests/builds/start services. All additional actions were source/history/status/graph reads; no target/private incident data, lifecycle, deployment, merge or cleanup access.

Required post-review work: exact-native disposable idle/truly-working scoped preparation through actual Ruby boundary with retained utility; required package/session-creation/archive VM results; composed app and exact aitherdev generation builds; selected profile/native/portal/conversation continuity. Stop fixture at preparation; no live target retry/full switch implied. No persistent-format change; old software reads state but restores refusals. Preserve forward-only recovery, original journals, admission/failure contracts. Build/copy before machine ownership; activate system only if exact comparison requires it; lead owns fresh integration/lineage/machine-release proof.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-archive-confirmation-regression/
