# Final change review packet

User requests root cause and fix for reboot recovery refusal, deployment to
aitherdev, integration once verified, then continuing three explicitly named
sessions. Scope and design: plan.md, design.md, state.md in this directory.

Risk: high because this exact retained-set proof also gates archive safety and
recovery of persistent sessions. General, architecture/repetition, scope and
risk/compatibility lanes all apply. Local operator is trusted (runtime AGENTS);
remote users, wrong identities and uncertain submissions remain constrained.

No retained roster exists in this threadless maintenance initiative. Installed
catalog default delegated review-purpose reviewer uses gpt-6.1-sol/xhigh;
standalone fallback is required. Review directly, no nested agents or source edits.

Complete implementation: library adds optional model-provider query filter;
runtime opts into all providers for exact retained discovery. Nil keeps existing
behavior. No schema changes, migrations, journal edits or native thread loading.
Existing ownership/project/submission checks remain. Library wire test and runtime
cold/paginated regression pass; regression demonstrably fails without the runtime
fix. Unknown extra identities remain refused. Nix vendor hash regenerated from
new Go dependency. Configuration hooks pass. Workspace/host composition checker
passes at f05f50eed6dbfa2794502653176f0bbbbf20f1fa.

There are no migrations (none merged/released/deployed/externally consumed), no
superseded approaches in history, no repeated pin streams. One codex-web pin in
runtime, one runtime pin per deployment consumer. Runtime dependency commit is
separate from behavior/tests/docs. Library API tests/docs stay with the API.
Documentation: codex-web docs/reference.md and dev-workspace docs/workspace-portal.md.
Source diagnosis uses live read-only observations: all retained subjects verify,
ordinary saved query returns no rows, explicit empty modelProviders returns all
8, loaded list empty. Initial project-filter hypothesis was disproved.

Consumer map: codex-web ListThreads -> dev-workspace workspacecodex discovery ->
teamruntime observation/archive readiness -> CLI resume and portal recovery.
Composed workspace nests runtime through unchanged vpsfree-dev-workspace extension;
configuration devWorkspace selects matching host module. No native Codex upgrade,
provider change or wider default-list behavior change. System before profile;
forward package recovery preserves state. Longer checks and deployment follow
review. Live sessions stay untouched until candidate is verified.

Assess full history/diff and explicitly conclude consolidation and no migrations.
Save report in this directory as review.md.

## codex-web

Path: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/codex-web
Base: 9d337b70987fdf1dd42a5d8efff31f755a122550
Head: d3a29bee90ef00a08816920408c596152339a637

d3a29be codex: expose provider filters for saved thread discovery

codex/client.go      | 7 +++++++
 codex/client_test.go | 2 ++
 docs/reference.md    | 5 +++++
 3 files changed, 14 insertions(+)

## dev-workspace

Path: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/dev-workspace
Base: 4155d0099d03028b43d5f08d225a88156cb4155a
Head: f05f50eed6dbfa2794502653176f0bbbbf20f1fa

f05f50ee recovery: discover retained threads across model providers
6c9a6337 deps: select provider-aware Codex thread discovery

docs/workspace-portal.md                           |  5 ++
 flake.lock                                         |  8 +--
 flake.nix                                          |  2 +-
 nix/workspace-portal.nix                           |  2 +-
 portal/go.mod                                      |  2 +-
 portal/go.sum                                      |  4 +-
 .../internal/workspacecodex/archive_ready_test.go  | 60 ++++++++++++++++++++++
 portal/internal/workspacecodex/discovery.go        |  3 ++
 portal/internal/workspacecodex/discovery_test.go   |  3 ++
 9 files changed, 80 insertions(+), 9 deletions(-)

## workspace

Path: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/workspace
Base: 3fa192f600293128871245efe55c6587ed82fb20
Head: 1deb88301418722ed1aebeaa2bebafd9b2e007d8

1deb88301 workspace: select provider-independent session recovery

flake.lock | 16 ++++++++--------
 flake.nix  |  2 +-
 2 files changed, 9 insertions(+), 9 deletions(-)

## vpsfree-cz-configuration

Path: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/vpsfree-cz-configuration
Base: fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627
Head: f9a6996153daec9e20a3feb58e05981b5907ef7b

f9a69961 inputs: set devWorkspace to f05f50ee

flake.lock | 14 +++++++-------
 1 file changed, 7 insertions(+), 7 deletions(-)

Exact quick-check commands and outcomes: quick-checks.md.
