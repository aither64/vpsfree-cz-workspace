# Final review packet

Review the completed private Codex state boundary and native 0.165 upgrade, plus
the one-installation migration source preserved in rollout.md. Read the workspace
AGENTS.md, required Git/lifecycle/verification/deployment/documentation procedures,
each repository's AGENTS.md and the mandatory-change-review skill and all four
lane references. Review directly without delegation; do not edit application or
operational source or execute the migration. A report under this initiative is
allowed. Review committed source; raw Python files mirror the committed fenced
blocks and are convenient for inspection.

User scope: restore all portal sessions/status/timing/messaging while stock CLI
keeps an independent home. Portal tmux supplies terminal access; stock need not
open portal conversations. Upgrade portal to exactly 0.165. Deployment through
vpsfree-cz-configuration is authorized. One installation means the migration is a
one-time operation, not a permanent framework. Retry only `yes go ahead` to the
confctl session with original ID 2a2656f4-3d35-4bee-9a71-14e20bc35669 after acceptance.
No master merges, reboot, forced interruption, lifecycle cleanup or backup removal.

Acceptance: consistent private home across native, providers, naming, CLI/tmux,
recovery and teams; explicit SQLite/log overrides; retained-state startup refusal;
old contracts retained; exact native/package tests; all portal history conserved;
stock history preserved; detached idle-only migration with durable resume; both
reported sessions usable and original send accepted exactly once.

Trust: the local operator administers this development host. Assess ordinary
configuration mistakes, concurrent operations, interruption, data integrity and
remote-client boundaries. Do not invent hostile-local-filesystem defenses.

High risk: persistent native databases, authentication separation, protocols,
deployment order and forward-only recovery. Lanes: general; architecture and
repetition; scope and proportionality; risk and compatibility. No retained team
exists (team list cannot resolve a lead for this threadless initiative). Installed
catalog 495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7 selects
`delegated/reviewer`, model gpt-6.1-sol, effort xhigh. Reviewer must remain independent.

Dependency/consumer direction: codex-web provides generic protocol and ephemeral
utilities to dev-workspace via Nix source and Go pseudo-version. dev-workspace owns
home selection, native packaging, host module and portal; configuration consumes
its host contract, workspace composes its user-profile application through the
unchanged extension. Inspect actual selected inputs/imports, not only this list.

Commit split: protocol compatibility/provenance is one codex-web commit. Runtime
is one functional native-service selection change containing home propagation,
exact native/name prerequisites and matching source/Go pins. These deploy together
to avoid a mixed native/name runtime during the home cutover. Configuration has a
generated channel pin commit and a separate provider credential path commit.
Workspace has one composition pin commit. One-time operational source is in a
coordination rollout checkpoint. No repeated pin streams or abandoned branch
iterations are intended; independently assess whether this split is adequate.

Migration lineage: no new project-owned SQL migration. Native upstream 0.165 adds
migration 62 (attached_thread_parent_id); stock already applied it to shared state.
The reviewed one-time partition requires exact current native schemas and copies
rows into equivalent schemas, rewriting only structured rollout paths. It has
never been run, deployed, merged, released or externally consumed. There is no
legacy version of this operational script to retain. The existing source home is
preserved by atomic exchange. After package selection recover forward, even if
home publication has not happened. Whole-branch history/migration and repeated-pin
conclusions must be explicit.

Quick evidence: codex-web entire Go units, version-probe tagged unit, exact0.165
schema/request corpus and 55 config restrictions passed. Runtime entire Go units,
focused naming/local schema, corrected host batch (23 tests/742 assertions) and
native-client batch (2 tests/12 assertions) passed. Fresh vendor derivation proved
sha256-XEvzpQbsCzcHzhTdqghrjhGmiqna25MPU2b/wGJekqA=. Composition check passes.
Seven migration fixtures pass (schema/history/source conservation, orphan stock
records, refusals, exchange crash recovery retaining new writes, and open source
file exclusion). Native integration and final builds intentionally await review.
Current free space is 90.4 GiB; final admission requires source bytes +8GiB scratch
+20GiB reserve. Independent portal ChatGPT login is already complete, mode0600;
stock auth untouched. No live service has changed or message been resent.

Docs: plan.md/design.md/state.md and rollout.md explain this individual operation.
Runtime docs/workspace-portal.md and docs/codex-package.md own supported storage,
launch and recovery behavior; codex-web docs/reference.md and update skills own
protocol/catalog contracts. Configuration's existing Codex operations guide was
checked; its token path is declarative. Shell snapshots preserve original bytes;
old-home paths observed there occur only in PATH, not storage environment variables.

## Complete branch inventory

### codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/codex-web`
Base: `58300182763a01de7248ddf7c6cb9a4f0c6216cb`
Head: `ba8dfdd27daa7ab3f4350f7a2627984b6b7f84cf`

```text
ba8dfdd27daa7ab3f4350f7a2627984b6b7f84cf codex: support prompted naming and state upgrades with 0.165
 codex/ephemeral.go                                 |  2 +-
 codex/ephemeral_integration_test.go                | 23 ++++++++++++++----
 codex/native_upgrade_integration_test.go           | 21 +++++++++++-----
 .../prompted-ephemeral-models-0.165.provenance     | 10 ++++++++
 docs/reference.md                                  | 19 +++++++++++----
 skills/update-codex-web/SKILL.md                   |  6 ++++-
 .../update-codex-web/scripts/refresh-catalogs.py   | 28 ++++++++++++++++------
 7 files changed, 85 insertions(+), 24 deletions(-)
```

### dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/dev-workspace`
Base: `d0e4318cb1872feb69f3109f032870c310f14bdf`
Head: `8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5`

```text
8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5 codex: isolate workspace state and select native 0.165
 docs/codex-package.md                              | 10 +--
 docs/session-preparations.md                       |  8 +--
 docs/workspace-portal.md                           | 22 ++++++
 flake.lock                                         | 16 ++---
 flake.nix                                          |  4 +-
 libexec/dev-session                                |  6 ++
 libexec/workspace-codex-providers.rb               |  8 ++-
 libexec/workspace-coordination-host.rb             |  2 +-
 libexec/workspace-host                             | 78 ++++++++++++++++------
 nix/tests/session-creation.nix                     |  2 +-
 nix/workspace-portal.nix                           |  4 +-
 portal/cmd/workspace-portal/naming_runtime.go      | 10 +--
 .../naming_runtime_integration_test.go             | 14 ++--
 portal/cmd/workspace-portal/naming_runtime_test.go | 25 ++++---
 portal/go.mod                                      |  2 +-
 portal/go.sum                                      |  4 +-
 test/dev_session/codex_runtime_test.rb             |  9 ++-
 .../workspace_host/agent_team_registration_test.rb |  9 ++-
 test/workspace_host/archive_recovery_test.rb       |  2 +-
 test/workspace_host/commands_and_locks_test.rb     | 51 +++++++++++---
 test/workspace_host/live_switch_test.rb            | 14 ++++
 21 files changed, 214 insertions(+), 86 deletions(-)
```

### vpsfree-cz-configuration

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/vpsfree-cz-configuration`
Base: `7a254c88b0b54a32300a319b3e4ed32936d9b004`
Head: `dcb5982fd4325d57cda79693fa4da27c7a955413`

```text
f455dcc8f3e3aba685d1f569cc2903696b409b69 inputs: set devWorkspace to 8c597b6f
dcb5982fd4325d57cda79693fa4da27c7a955413 aitherdev: use the portal's private provider credential
 cluster/cz.vpsfree/machines/aitherdev/config.nix |  2 +-
 flake.lock                                       | 22 +++++++++++-----------
 2 files changed, 12 insertions(+), 12 deletions(-)
```

### workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/workspace`
Base: `c2bfb715fd7b0d0c2ba6a75d24625a2910944d2f`
Head: `5deaee4fcf6692f617e346aa84ab3f95f52c3bfd`

```text
5deaee4fcf6692f617e346aa84ab3f95f52c3bfd workspace: select private Codex state and native 0.165
 flake.lock | 24 ++++++++++++------------
 flake.nix  |  2 +-
 2 files changed, 13 insertions(+), 13 deletions(-)
```

Read each complete final diff with git diff BASE HEAD. Read the committed
rollout.md source and verify its source checksums. The active tracking checkpoint
head will be supplied with the assignment. Put findings (Blocking/Important/Advisory),
residual gaps and explicit whole-branch history/migration conclusions in
final-review.md. Include scope/proportionality assessment before optional hardening.
