# Review packet: instruction routing

## Request and accepted boundary

User selected moving detailed procedures behind mandatory action-specific routes,
with every existing requirement preserved. Inventory every repository; retain
cohesive small files where splitting adds overhead. No policy cleanup, runtime
instruction injector, scheduler, model-default change, deployment or CI wait.

## Revisions and owners

- haveapi: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-agent-instruction-routing/haveapi
  Base 67cf01afecaa4e0dc4eee96f81f8b1218546b5c7; head a2fc755452db60dac919205829fda6db362e3fce.
- vpsadmin: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-agent-instruction-routing/vpsadmin
  Base 15ae9175c382a3661079c3b7f9446749b230ac74; head 7b309b6c4b54898b0859b353b0c2e80b43b3b23e.
- vpsadminos: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-agent-instruction-routing/vpsadminos
  Base 0855b958e7d6623298cca67e1c47ad06f0a98552; head aa8bffbb44d83354d8afc5fda928706cb9739a5b.
- workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-agent-instruction-routing/workspace
  Base c62285fccaaaaea29085bb479722be5d7cc8886d; head ebb838cacd04726cb5c2c8891e16f0db5d6942e6.

## Implementation and documentation

Each repository owns its AGENTS.md and doc(s)/agent-instructions procedures.
The workspace owns its coordination, verification, deployment, KB and lifecycle
rules; no vpsFree-specific behavior is added to the generic runtime. Local files
retain standalone usefulness. Twelve other canonical repositories stay unchanged
after inspection; renamed clone aliases were deduplicated.

All original nonblank paragraphs are preserved verbatim and mapped in coverage.md
and coverage.json; verify-instructions.py independently reads the original Git
revisions and validates text preservation, routes and size. Review semantic scope
and trigger completeness separately. Critical boundaries intentionally also appear
in the short core; this duplication keeps them visible before procedure loading.

Each repository has one coherent commit containing its shortened entrypoint and
the required files it routes to, plus documentation links. The workspace commit
also adds its size/reference regression check and flake check wiring. These must
ship together so a checked-out revision has complete instructions. No pins change.

## Verification and risk

Quick coverage/route/whitespace checks pass; workspace Ruby check passed 2 tests,
32 assertions, no failures/errors/skips. Nix formatting passes. Project commits
run declared Overcommit hooks via their Nix shells. vpsAdmin first failed because
the new worktree lacked API gems; diagnosed and initialized its API shell (Luna/low
watcher, exit 0) before retrying. No hook bypass.

Overall risk high because instruction routing covers authorization, destructive
operations, deployment and recovery obligations. All reviews use fresh Astra/xhigh:
general, architecture, risk and scope. No application API/schema/state/protocol
or rolling-upgrade change. Old revisions remain self-contained. Rollback reverts
entrypoint/procedures together. No host deployment is needed.

Next validation after review: Nix-packaged instruction check and read-only fresh
Astra/xhigh cases (verification-plan.md) inspecting actual file-read events.
Missing-file behavior and new-phase routing are included. Automation remains
instruction-driven; no claim of perfect compliance or measured weekly savings.

## Reviewer instructions

Perform your assigned lane directly; do not spawn agents or edit files. Read
the mandatory-change-review skill and your lane reference. Focus on concrete
omissions, weakened/strengthened rules, misleading scope, unreachable procedures,
and proportionality. Inspect committed diffs and the original wording. Report
findings with severity/path/revision and residual test gaps.

User subsequently authorized merging both this initiative and Luna monitoring
into all default branches, including configuration. Still do not wait for CI
or archive/delete the sessions. Review content is unchanged by this authorization.
