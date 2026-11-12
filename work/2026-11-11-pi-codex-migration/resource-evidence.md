# Resource comparison evidence (Package D)

Owner: implementer0. Read-only host snapshot on 2026-11-11, approximately
22:14–22:18 UTC. Initial package budget: eight active minutes. This note adds
aggregate scale and measured current memory to the source comparison; it does
not benchmark Pi or propose changing the portal UX.

Session identity and both environment identity values were reverified against
`2026-11-11-pi-codex-migration` and `/home/aither/workspace/ai/vpsfree.cz`.
The current same-session roster was checked. No other session records,
transcripts, roster contents, worktrees, prompts, credentials or environment
dumps were read. No lifecycle action, daemon/worker launch, model call, build,
benchmark or application change was performed.

## Scale: stored is different from loaded or active

| Aggregate observation | Count | Meaning / limit |
| --- | ---: | --- |
| Raw `work/` directories | 87 | Includes four names that are not dated session slugs |
| Dated current tracking directories | 83 | Names matching `YYYY-MM-DD-*`; not proof that every session is executing or has active lifecycle state |
| Dated `archive/` directories | 343 | All 343 directories match the date-slug shape; contents were not inspected |
| Dated current + archive directories | 426 | Tracking scale, not native thread count |
| Public `dev-session list` rows | 432 | Its documented/source implementation unions tracking, worktrees, sensitive sessions, tmux and recovery names; not a second authoritative count of dated sessions |
| Public list: managed tmux / none | 60 / 372 | Terminal/runtime management state; not loaded-thread or active-turn state |
| Dedicated workspace Codex home: stored native threads | 4,190 | Single `threads` table metadata aggregate |
| Same table: unarchived / archived | 2,213 / 1,977 | Native archive flag; **unarchived does not mean loaded or running** |
| Native threads with current workspace session-cwd prefix | 3,667 | `cwd LIKE '/home/aither/workspace/ai/vpsfree.cz/work/%'` |
| Prefix subset: unarchived / archived | 1,690 / 1,977 | Other 523 home records do not match that prefix; no identities/content examined |
| Prefix subset: distinct stored working directories | 205 | Does not prove these directories still exist or map one-to-one to current sessions |
| Native projects / spawn-edge records | 786 / 2,762 | Counts of stored native metadata, not live processes or retained portal members |
| Regular JSON filenames in this workspace's team-state namespace | 134 | File-count metadata only; not a validated count of current teams or members |
| Loaded threads / active native turns / retained portal members | Unknown | No inexpensive installed global count-only command established within this package |

The native `agent_role` metadata is empty for all 4,190 rows, so it cannot supply
the retained-member count. Portal members are independent native threads; do not
multiply the current eight-person team by all historical sessions. No peer
rosters were opened to fill that gap.

## Measured memory

Linux `/proc/*/smaps_rollup` snapshot at **22:14:56 UTC**. Units below are GiB
(2^30 bytes); raw KiB are retained for precision. PSS apportions shared mappings
and is more useful for summed process cost than summing RSS. This is one live
snapshot under ongoing work, not idle baseline, peak attribution or a forecast.

| Current workspace service component | Processes | RSS KiB | PSS KiB | Approx PSS GiB |
| --- | ---: | ---: | ---: | ---: |
| Shared native Codex daemon | 1 | 6,888,488 | 6,818,830 | 6.50 |
| `team-mcp` helpers in native service | 91 | 1,691,860 | 821,559 | 0.78 |
| Native code-mode host | 1 | 58,384 | 57,066 | 0.054 |
| Portal Go server | 1 | 124,596 | 112,783 | 0.108 |
| Portal-owned naming Codex child | 1 | 309,408 | 228,132 | 0.218 |

The native-service components above total about **7.34 GiB PSS**. The helpers
average approximately 8.82 MiB PSS each; they also account for 2,130 OS threads
in this snapshot, versus 120 in the main native daemon. OS threads are neither
LLM conversation threads nor active model calls. Helper role was confirmed by
reading only the known executable's first argv subcommand (`team-mcp`), never
remaining arguments. Helper count is not an authoritative loaded-thread count:
connection/process lifetime and native thread lifetime are distinct contracts.

Another 13 `codex` processes outside the native/portal service cgroups total
8,063,792 KiB PSS (about 7.69 GiB). Their workload ownership was not established;
they are **excluded** from the shared-daemon total and no peer work was examined.
Other portal helpers, Ruby commands and host workloads are likewise outside the
attribution above.

Native service cgroup at approximately 22:15–22:17 UTC:

| Cgroup observation | Bytes | Interpretation |
| --- | ---: | --- |
| `memory.current` | 36,719,140,864 | About 34.20 GiB; includes charged cache and kernel memory |
| `memory.stat anon` | 7,899,512,832 | About 7.36 GiB anonymous memory across service descendants |
| `memory.stat file` | 25,820,872,704 | About 24.05 GiB filesystem cache |
| `memory.stat kernel` | 3,034,570,752 | About 2.83 GiB kernel-accounted memory |
| `memory.peak` | 88,422,375,424 | Historical service-cgroup peak; time/workload not established |

Counters were read at nearby times while the workload continued, so they need
not sum exactly. Do not describe 34.20 GiB as the daemon's heap. A later
`systemctl --user show` cross-check reported the same native MainPID and roughly
36.76 GB `MemoryCurrent`; the portal service reported roughly 1.31 GB. The
portal service also contains the naming child and cache, so its cgroup total
is not the Go server's PSS.

Host context from `/proc/meminfo` near 22:14 UTC: 98,854,756 KiB total,
62,583,620 KiB available, no swap. These values do not establish pressure,
leakage, a cause for earlier peaks or spare capacity for a proposed deployment.
No CPU/latency/throughput comparison was run.

## Disk archive is a separate budget

Metadata-only traversal of the dedicated Codex home (no file bodies), near
22:17 UTC:

| Native data | Files | Logical bytes |
| --- | ---: | ---: |
| `sessions/` rollout files | 2,213 | 9,812,692,927 |
| `archived_sessions/` rollout files | 1,977 | 8,716,348,423 |
| `thread_history_1.sqlite` | 1 | 6,295,584,768 |
| `state_5.sqlite` | 1 | 21,053,440 |
| `queue_1.sqlite` / `goals_1.sqlite` | 1 each | 106,496 / 28,672 |
| `log/` files | 6 | 111,776,011 |

The two rollout directories alone are about **17.26 GiB** logical storage;
the native thread-history database adds about **5.86 GiB**. These are different
representations/indices and may duplicate logical information; no contents were
read or deduplication asserted. Sidecars, other native files, portal receipts,
repository/worktree data and backups are outside this subtotal. Archived history
need not consume a live Pi process, but remains a disk-retention and migration
obligation. Nothing in these measurements authorizes deleting or unloading it.

## Resource implications for Pi while preserving the portal

Source comparison uses D `6587c4c1cedabee95bcc52f4667e7d33e3a82859`,
C `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` and implementer1's
[Pi capability evidence](pi-capabilities-evidence.md), pinned to
Pi `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`. These source conclusions are
separate from the host measurements above.

- **Current shared Codex:** one daemon serves many independent native
  conversations. Per-connection MCP helpers and loaded histories still cost
  memory; shared daemon does not mean zero marginal cost. Stored-thread counts
  cannot explain memory without loaded count, history size and actual work.
- **Pi SDK in a multiplexed worker:** `createAgentSession` embeds sessions in
  a Node/Bun host, allowing an architecture with shared process/module overhead
  rather than a new process for each retained member. Actual multiplexing,
  concurrency limits, extension/provider isolation and lifecycle remain host
  design obligations. Loaded histories, tools/MCP clients, token buffers and
  in-flight work remain per-session costs; a shared process also shares failure
  and garbage-collection pressure.
- **Pi RPC per loaded member:** long-lived `pi --mode rpc` is a process bridge,
  so one instance per retained member duplicates the Node/V8/module baseline,
  plus per-process tool/extension connections. Shared file mappings mean summed
  RSS exaggerates some duplication; neither a baseline nor a per-member PSS was
  measured. A process per all 4,190 stored threads is not justified by the
  portal's existing retention semantics.
- **Bounded loading/idle eviction:** keep portal/member identity and durable
  history independent of a loaded worker. A replacement could load on demand
  and evict safely idle runtimes without archiving the session, but only after
  preserving accepted/uncertain delivery, pending tools, queues/goals, utility
  ownership and terminal subscriptions. Pi source support for persistence is
  not proof that this bridge contract already works. Long histories should be
  paged for display rather than loaded into every browser/worker unnecessarily.
- **Coexistence:** legacy Codex state, receipts and any retained native runtime
  cannot be assumed removable at cutover. During staged migration, Pi workers
  would add to this baseline until legacy execution and recovery obligations
  are resolved. No Pi memory-saving percentage, capacity or performance promise
  is supported by this investigation.

## Measurement provenance and gaps

Measured daemon executable path:
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
The installed `dev-session` resolves below
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0/`.
The filenames identify observed artifacts; no native version probe, binary hash
or exact installed-source equivalence was established by this resource package.

Methods: `os.scandir` plus date-slug-name filtering; installed `dev-session list`
reduced immediately to aggregate columns; `/proc` comm/cgroup/status and
`smaps_rollup`; cgroup v2 `memory.current`, `memory.peak`, `memory.stat`;
`systemctl --user show` restricted to resource properties; metadata-only
`os.stat` traversal. SQLite used Python `sqlite3` with `file:...?mode=ro`,
`PRAGMA query_only=ON`, two-second busy timeout, table/column schema and
`COUNT`/boolean-sum/distinct-count queries only. No titles, IDs, cwd values or
message columns were selected. All database counts are live point observations,
not an atomic snapshot with the filesystem/process measurements.

C `codex/client.go:3837` provides metadata-only `thread/loaded/list`, but the
installed CLI's thread commands expose no equivalent global count-only command;
available Python websocket modules were absent. No custom client, helper build,
history enumeration or daemon was launched. Loaded/active counts remain unknown.
Retained team/member counts require an authorized aggregate implementation rather
than reading peer rosters. Pi idle/busy memory, MCP connection scaling, long-history
cost, CPU, resume latency and concurrency capacity remain unmeasured.

This is investigation evidence, not a substantive application deliverable or
independent-review packet. Lead owns plan/state linkage and architect0 owns the
resource design addendum.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
