# Final committed deliverable review

Initiative: 2026-10-15-portal-performance-fix. Workspace root
/home/aither/workspace/ai/vpsfree.cz. Read plan.md, design.md and state.md here.

Outcome: remove repeated whole-workspace YAML parsing per watched reconnect;
page arbitrary-length conversations with existing native Codex APIs, isolate
bulk replies from live watches/sends/approvals, incremental exact counts, explicit
partial/stale snapshots and per-thread backoff. Keep 64 MiB individual-message
safeguard and fail explicitly if one item cannot fit. No Codex fork or version
change; no tags, release publication, session archival/deletion or reboot.

Acceptance: authorization/lifecycle/recovery checks remain fail closed; current
record and socket epoch changes invalidate cached permission; long aggregate
history has no fixed byte/turn ceiling; individual-item failure cannot disconnect
live transports; partial/backfill/count and stale semantics remain honest.
Post-review live targets are in design.md; no live acceptance claimed yet.

Risk HIGH: recovery admission, shared protocol/public API, deploy topology.
Assign all lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. No retained roster (verified live); installed catalog default
lead_reviewed reviewer gpt-6-astra/xhigh, fresh standalone fallback. Read every
lane reference from mandatory-change-review skill; perform review directly,
read-only, no nested agents. Local operator is trusted (runtime AGENTS); remote
clients remain untrusted. Do not require defenses against compromised operator.

## Complete branch inventory

### codex-web

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-15-portal-performance-fix/codex-web
Base: c9aa6dc2f8cd6e80eeb711a3f9c569e08b7b2016
Head: f684f843123aab9fc30e769ddb77b4a5a1ae1326
Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-15-portal-performance-fix/codex-web-final.diff

Complete series:
```
f684f843123aab9fc30e769ddb77b4a5a1ae1326 codex: page long history outside the live observation transport
```

### dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-15-portal-performance-fix/dev-workspace
Base: 4e7ff517e1cac52c3cc8bb08f2a6a5ca21d3715b
Head: 862c9dcf8be8f22fe717df250bf9128e662456e5
Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-15-portal-performance-fix/dev-workspace-final.diff

Complete series:
```
7b64dc922005769227c2d18c83170f187ee5acd5 portal: reuse validated session records during recovery
862c9dcf8be8f22fe717df250bf9128e662456e5 portal: isolate paged history and back off activity failures
```

### workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-15-portal-performance-fix/workspace
Base: 60fd9da5a6f72d926c97db0f3921f3520eb5ccc9
Head: 01d1fe0bcad054054d077bfd138a24784de3d9b1
Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-15-portal-performance-fix/workspace-final.diff

Complete series:
```
01d1fe0bcad054054d077bfd138a24784de3d9b1 workspace: select paged history and cached portal records
```

### vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-15-portal-performance-fix/vpsfree-cz-configuration
Base: 206f3025c0142865ed516283eaf5c2f298a6e6cf
Head: f789cd8be941e9e6d0c944c2f24a31c1580f51e5
Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-15-portal-performance-fix/vpsfree-cz-configuration-final.diff

Complete series:
```
f789cd8be941e9e6d0c944c2f24a31c1580f51e5 inputs: set devWorkspace to 862c9dcf
```

## History, streams and compatibility

No migrations, persisted format changes, or schema changes in any repository.
No migration version was merged/released/deployed/externally consumed. Unmerged
followups were amended into their owning logical commits. Current feature heads
are published, none deployed or merged. Superseded codex refs a7d6557/68b108c were
replaced by f684f84 before final review; original source ref evidence retained.
Codex rebased cleanly over c9aa6dc (range-diff identical before protocol corpus
fix). Runtime rebased over naming changes; pin conflicts resolved to include
current master, preserve its model catalog and adopt final codex revision.

Repeated pin streams consolidated to one final update each: codex-web into
runtime (flake + Go module + vendor hash, in 862c9dc), runtime into workspace
(direct nested override + generated lock, 01d1fe0), runtime dev-workspace channel
devWorkspace in configuration (generated confctl commit f789cd8). There are no
retained intermediate pin commits in the reviewed ranges. Explicitly assess
complete history, obsolete approaches, consolidation and no-migration conclusion.

Commit split: runtime catalog/recovery behavior is its own commit with tests.
Isolated history adoption, matching API pin and stale/backoff handling share the
second commit because the consumer requires the provider's new types and error
semantics; docs describe both resulting portal behaviors. Provider paging,
incremental activity and fork proof are one coordinated long-history feature.
Workspace/config are mechanical pin commits, included in whole-branch review.
Assess split independently and flag any genuinely separable bundled behavior.

Provider owner codex-web exposes optional ClientOptions.HistoryReader,
HistoryPool, existing ReadThread/ReadThreadPage/ReadActivity; consumers found in
runtime portal/internal/workspacecodex wrapper, cmd/workspace-portal interactive
constructor and web/activity observer. Inspect both injection sites. Other
clients retain old transport behavior when no reader supplied. Two shared passive
connections, one RPC per connection, no watch/resume/mutation methods. Runtime
owns session catalog/private recovery index. Site extension is unchanged.

Caches are process-local; old/new versions read the same persistent records.
JSON Stale/Refreshing additions are optional. Existing checkpoints unchanged.
Deploy matching aitherdev system contract before composed application profile.
Keep Codex 0.160.0/native sessions/tmux; forward-only profile recovery via original
coordinator attempts. All four master merges/deploy/finish already authorized
by user's actual instructions recorded in plan. Another session currently holds
aitherdev; no bypass or foreign mutation is authorized.

## Documentation and quick evidence

Provider README History reads documents injection ownership, pooling, paging,
partial/stale and single-item safeguards. Runtime docs/workspace-portal.md
documents catalog, backfill and freshness. Existing configuration operations
workspace-coordination-aitherdev.md checked, remains accurate. Individual rollout
evidence stays in this session. No KB publication needed. Lead applied writing
skills directly to visible text/docs.

Quick checks passed on final sources: codex protocol corpus coverage plus
go test -short -mod=readonly ./codex ./conversation -run
'TestBound|TestHistoryAggregate|TestActivity|TestReadThreadPage|TestReadActivity'.
Runtime focused Go session/web/workspacecodex/cmd tests (catalog, activity,
attention, recovery and shipped browser contract) passed with actual pinned
module. TMPDIR=/tmp avoids Unix socket path overflow; local host catalog override
DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-performance-absent-catalog keeps tests
independent of operator /etc catalog. No production settings changed.
Go formatting, diff whitespace checks pass. Channel generated commit passed
Overcommit Nixfmt and message hooks. Final semantic deployment lock checker passes.
Vendor hash generated by isolated goModules probe. Initial probe accidentally
included default package and failed expected fake hash; no operation remains.
Long suites, >64 MiB actual websocket/aggregate tests and live acceptance remain
for after final review. Prior automatic CI failure was protocol corpus call
inventory drift; corrected corpus now includes historyRequest wrapper calls.

Please save findings/conclusions in review.md here (review report only, no source
edits), ordered Blocking/Important/Advisory with code evidence. State residual
gaps and explicit branch-history, pin consolidation and migration conclusions.
