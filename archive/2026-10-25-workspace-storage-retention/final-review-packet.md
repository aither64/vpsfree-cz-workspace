# Committed final review packet

Initiative: 2026-10-25-workspace-storage-retention
Plan/state/design and review-context.md are in this directory. Read them with
all four lane references under ~/.codex/skills/mandatory-change-review.

All intended changes are committed; all three worktrees are clean. Workspace
feature was rebased onto current shared master without modifying shared state.
Runtime and configuration upstream master remain their recorded baselines.

Final unit batch passed: archive 42 runs/1,727 assertions; GC 39/207;
collection concurrency 2/12; capabilities 3/9. Final workspace maintenance 2/10
and composition checker passed for runtime 98466eaf. Earlier focused verification
is in review-context.md. This is before local long integration testing. CI starts
automatically on publication; exact-head run 40180103947 is running independently.

Reviewer fallback: no valid lead native thread/team exists for this deliberately
threadless session. Installed catalog digest
840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa selects default
team delegated, review-purpose reviewer gpt-6.1-sol/xhigh. Fresh standalone
reviewer, read-only, no nested agents. Cover all four lanes directly. Explicitly
conclude on whole-branch history, consolidation streams and migration lineage.

No DB migrations. Existing private inventory 1/2 -> optional completed inventory 3
conversion has not been applied, merged or released. No branch iteration has been
deployed or externally consumed as a supported state boundary. Both input streams
are consolidated to one final pin selecting the same runtime. Follow-up fixes are
folded into their owning runtime commits. No intermediate pins remain.

## dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-workspace-storage-retention/dev-workspace

Base: 10bb047513c82d1310e8fcaa797e8772f948dd8a
Head: 98466eaf48ab68f09a2261cd472f88b26bcebff0

Complete series:

```text
adc2f21ff3837c52889425c049acb527fb12200c
archive: retain committed heads without checkout backups

Keep explicit archive recovery in compact schema-3 records and recreate
clean committed checkouts on revival. Discard uncommitted files and retain
Markdown tracking summaries, while preserving predecessor recovery readers
and partial-capture behavior. Require policy 3 for compact archive records.

73683cf2fd95a57907029303ca1250c002ee91e4
workspace: omit tracking from additional source checkouts

Initialize workspace feature, retained-source and integration scratch
checkouts with per-worktree sparse configuration. Exclude work and archive
tracking before materialization so historical evidence is not copied into
every source snapshot. Keep the shared checkout and other projects whole.

98466eaf48ab68f09a2261cd472f88b26bcebff0
coordination: expire unused payloads after one day

Shorten unused preparation and orphan retention to 24 hours and provide
explicit legacy expiration plus optional allocated-size reports. Continue
collecting completed integration scratch while busy drivers keep shared
sources and their required dependencies. Preserve live work and recovery.

```

Final diff: dev-workspace-final.diff

## workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-workspace-storage-retention/workspace

Base: 00fe575aff47eff8174c77281846f628aafd326e
Head: 0b5fe0dea7c2fee9bd9e37dea949c16c8a005fec

Complete series:

```text
94a49be34930090ae5f5f5660ae504518843ba7f
archive: remove disposable historical verification artifacts

Retain Markdown explanations and portal manifests while removing raw logs,
bundled repositories, downloaded artifacts and generated build output from
the current archive tree. These records accounted for about 4.1 GiB and
were copied repeatedly into worktrees and package source snapshots.

Keep committed history and repository branches unchanged. Historical raw
artifacts remain in prior commits; no history rewrite or artifact migration
is introduced. Shared tracking files change only after approved integration.

38e4c20ae73e705491e672c71f9e7344800bfcb3
workspace: keep compact tracking and provide storage maintenance

Keep Markdown explanations and portal manifests in tracking, and exclude
tracking directories from exported package sources. Document committed-only
archives and the 24-hour coordinator retention policy.

Provide explicit preview/apply maintenance for completed archived records
and private recovery payloads. Preserve active tracking, unfinished
operations, committed heads and the selected package transition boundary.

0b5fe0dea7c2fee9bd9e37dea949c16c8a005fec
deps: select compact archive and one-day retention runtime

Select the reviewed storage policy runtime through the existing nested
input while retaining the independent vpsFree extension and sibling pins.
The matching host contract is selected in the configuration repository.

```

Final diff: workspace-final.diff

## vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-workspace-storage-retention/vpsfree-cz-configuration

Base: d12a77374b18e15fe7600f95307114e2e1882828
Head: 0eebce77abbc3bafdb688e80b243b8cf64c74160

Complete series:

```text
f5d5555785b8d179657c4766b44bdba916727576
docs: describe workspace archive and coordinator retention

Explain the user-profile runtime's 24-hour preparation retention and
explicit completed-archive compaction procedure for aitherdev. Keep the
host GC policy and application ownership distinct so operators use each
tool's preserved recovery and locking contracts.

0eebce77abbc3bafdb688e80b243b8cf64c74160
inputs: set devWorkspace to 98466eaf

devWorkspace: 10bb0475 -> 98466eaf
git log for 10bb047513c82d1310e8fcaa797e8772f948dd8a..98466eaf48ab68f09a2261cd472f88b26bcebff0
> 98466ea coordination: expire unused payloads after one day
> 73683cf workspace: omit tracking from additional source checkouts
> adc2f21 archive: retain committed heads without checkout backups

```

Final diff: vpsfree-cz-configuration-final.diff
