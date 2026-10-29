# Review remediation packet

Follow up the same coherent change and original final-review.md. Read the
mandatory-change-review skill and affected lane references. Review general,
risk/compatibility, and the new one-time recovery/source-observation design's
architecture and proportionality. Reuse prior conclusions for unchanged code.
Do not edit source or run live migration/deployment; report in
review-remediation-result.md. The original packet still owns scope, acceptance,
trust boundary and dependency direction. No changes to user authorization.

Committed operational source: shared workspace 5e267d26a, rollout.md under this
initiative. Raw scripts match its six fenced source blocks. Review new hook
recovery, inotify observation, durable fingerprint resume, and fixtures. Fifteen
fixtures pass in 8.4 seconds. SQLite read-only WAL access materializes empty
sidecars before observation; derived SHM reader indexes are excluded from
stability evidence. WAL/data/transcript changes still refuse publication.
The selected-service recovery uses systemctl start (does not interrupt a running
service) after verifying pending package/native identity, then ordinary switch.
No publication intent permits recopy; original inode identity and fingerprint
must survive interrupted publication. Changed original data requires manual
reconciliation. No source conversion has executed; no supported legacy script.

Narrow fixes: runtime creation/archive VM fixtures now configure/inspect the
private home. Configuration operations prose describes independent portal login.
Codex-web adds a separate focused asynchronous browser-test scheduling fix,
validated by 46 focused tests and successful final CI 40852873773. Fresh runtime
vendor hash is sha256-2aYEuOcFTjdecQu/GEP2i2sLlYi5eMnDxpKb2nyU7Mw=; exact
composition checker passes. Longer native/package gates remain after review.

History: runtime home/native/pin stream remains one commit. Configuration's old
and final runtime channel updates are consolidated into one generated pin commit
plus the functional credential path/doc commit. Workspace remains one composition
pin commit and is patch-equivalent after its final rebase onto shared master.
No new project-owned SQL migrations; retain the previous native schema-62 and
one-time partition provenance conclusion. Please explicitly assess the final
series, repeated-update consolidation and migration lineage for these heads.

## codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/codex-web`
Base: `58300182763a01de7248ddf7c6cb9a4f0c6216cb`
Head: `f6f4a187509b3bebfc81585c535be856eaab0d04`

```text
ba8dfdd27daa7ab3f4350f7a2627984b6b7f84cf codex: support prompted naming and state upgrades with 0.165
f6f4a187509b3bebfc81585c535be856eaab0d04 test: wait for asynchronous upload recovery
codex/ephemeral.go                                 |  2 +-
 codex/ephemeral_integration_test.go                | 23 ++++++++++++++----
 codex/native_upgrade_integration_test.go           | 21 +++++++++++-----
 .../prompted-ephemeral-models-0.165.provenance     | 10 ++++++++
 docs/reference.md                                  | 19 +++++++++++----
 skills/update-codex-web/SKILL.md                   |  6 ++++-
 .../update-codex-web/scripts/refresh-catalogs.py   | 28 ++++++++++++++++------
 test/uploads_browser_contract_test.cjs             |  7 ++++--
 8 files changed, 90 insertions(+), 26 deletions(-)
```

## dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/dev-workspace`
Base: `d0e4318cb1872feb69f3109f032870c310f14bdf`
Head: `7d1163585a51da684be0f5cdd500a64822165839`

```text
7d1163585a51da684be0f5cdd500a64822165839 codex: isolate workspace state and select native 0.165
docs/codex-package.md                              | 10 +--
 docs/session-preparations.md                       |  8 +--
 docs/workspace-portal.md                           | 22 ++++++
 flake.lock                                         | 16 ++---
 flake.nix                                          |  4 +-
 libexec/dev-session                                |  6 ++
 libexec/workspace-codex-providers.rb               |  8 ++-
 libexec/workspace-coordination-host.rb             |  2 +-
 libexec/workspace-host                             | 78 ++++++++++++++++------
 nix/tests/session-archive-lifecycle.nix            | 22 +++---
 nix/tests/session-creation.nix                     | 12 ++--
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
 22 files changed, 231 insertions(+), 101 deletions(-)
```

## vpsfree-cz-configuration

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/vpsfree-cz-configuration`
Base: `7a254c88b0b54a32300a319b3e4ed32936d9b004`
Head: `c92408739d53d0e5198710723d89d8189f0f4d99`

```text
d432863dc9ad9f7a68dd099c5069f14fe5c88e74 inputs: set devWorkspace to 7d116358
c92408739d53d0e5198710723d89d8189f0f4d99 aitherdev: use the portal's private provider credential
cluster/cz.vpsfree/machines/aitherdev/config.nix |  2 +-
 docs/operations/codex-providers-aitherdev.md     |  6 +++---
 flake.lock                                       | 22 +++++++++++-----------
 3 files changed, 15 insertions(+), 15 deletions(-)
```

## workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/workspace`
Base: `5e267d26a3c99e94a616f0c2a0f29e2ef34eeab8`
Head: `277833e8f9d8a45a502afca02b5df527da9440f0`

```text
277833e8f9d8a45a502afca02b5df527da9440f0 workspace: select private Codex state and native 0.165
flake.lock | 24 ++++++++++++------------
 flake.nix  |  2 +-
 2 files changed, 13 insertions(+), 13 deletions(-)
```

