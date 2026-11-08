---
lifecycle: active
---

# Codex 0.167.0 update

**Current phase: final review / awaiting product decision. Deployment blocked.**
The latest stable release0.167.0 intentionally rejects retained/requested thread
providers differing from the App Server's current default. This breaks supported
per-session providers. Exact creation CI and selected native source establish
R2; no public config/CLI opt-out exists. User choice requested: narrow downstream
native compatibility patch/rebuild (recommended) or retain0.165/defer. No native
patch, routing redesign, global config write or thread-history rewrite authorized.
Installed system/workspace remains0.165.0. No activation, machine/repo claim,
merge or lifecycle action performed. Session stays open.

## Phases

- [x] Verify session identity, retained roster and access
- [x] Freeze release/source and accept architect design
- [x] Implement, quick-check, commit and publish four source packages
- [ ] Receive/reconcile independent final review report
- [ ] Resolve R2 provider compatibility with user direction
- [ ] Required native/state/VM/package verification and exact output builds
- [ ] System then profile deployment and usability verification
- [ ] Explicit default-integration approval and approved remote integration
- [ ] Prove integrated deployed lineage and release machine

## Package table

| Package / deliverable | Owner | Dependencies / acceptance | Status / transition | Evidence / next result |
| --- | --- | --- | --- | --- |
| D: release/design incl R2 and switch constraints | architect0 | Official release/exact source; compatible providers/recovery | Design accepted22:40UTC; R2 found23:37 | [Design](design.md); user product decision |
| W: codex-web compatibility + necessary SQLite startup fix | implementer0 | Exact schemas/config/catalog, focused/full quicks and final CI | Source accepted23:06UTC; native gate parked | [W evidence](codex-web-evidence.md); review findings/native gates |
| R: packaged Codex/naming/Nix+Go+vendor | implementer1 | Exact W/input/vendor, naming/fixture quicks; provider compatibility | Corrected source accepted23:19UTC; R2 blocked | [R evidence](runtime-evidence.md); product decision |
| C: aitherdev two channel streams | implementer2 | Final R/schema+profile/graph/hooks | Source accepted23:22UTC; no system build | [C evidence](configuration-evidence.md); gated build/copy |
| S: workspace nested runtime composition | implementer3 | Final R and C, preserved extension/siblings, one joint check | Source accepted23:23UTC; no composed build | [S evidence](workspace-evidence.md); gated composition build |
| Final independent review | reviewer0 | All final committed ranges + four lanes | Assigned23:24UTC; progress only received | [Packet](review-packet.md); final report via lead transport |

Prep packages W/R/C/S were accepted before execution; one executing package per
implementer throughout. Exclusive repository source/index/commit windows retained.
Short session registration exclusion sequenced C→R→S after harmless busy refusals.
Architecture support did not edit applications. No member settings changed.

## Exact final published source

Worktree prefix: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/`.
Feature branches all `2026-11-08-codex-version-update`, target `master`.

| Repo / worktree | Final source base | Published head / series |
| --- | --- | --- |
| codex-web | dd90fb4308ba85617ee2a4267cc835aa9a4f11ce | f78eae3415d20b98503f11e9fe251e3111bfe4da; compatibility7e3143b then independent startup fixf78eae3 |
| dev-workspace | 32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6 | 71654e18c5558c6b8b5cb3f33bfedced7fab727d; one consolidated runtime update |
| vpsfree-cz-configuration | 1072f89f932ad570fb6d14007387d230549ccd14 | ec1ccce401f81d604cd059d159ca6033df07f2a0; llm56c8557a then runtimeec1ccce4 |
| workspace | 8aae9bd4af090260a92ec0296472fadce13c6cd7 | 3f813d5862c1a29d8dd34bd78863b5dfba38767a; one source pin commit |

All final worktrees clean; exact SSH refs independently verified. Workspace
registered initial527362b66; inherited coordination ancestor8aae9bd4 inventoried
by metadata only, no peer records read. Remote workspace base0c112efeb separately
recorded in S evidence. No integration approval. No new migrations/schema formats;
independent whole-branch/history/consolidation/no-migrations conclusion pending.

Frozen Codex0.167.0/tag086ccc833bc9cf01024ad2dd6af7dbd421b6bf9a,
llm-agentsd960982d3b05c294f3cf98cab3e23798548a0ced. Exact native SHA256
13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10.
Canonical Luna/full catalogs unchanged; strict0.163 and prompted0.164/0.165
retained. Native source/binary identities, full inputs, hashes and provisional
outputs in linked evidence. Superseded c92d539/637103e4/64fbbad input commits were
consolidated before review; never deployed. Narrow R successor fixed stale
postFixup0.165 assertion, deriving exact selected codex.version. No vendor rerun
for unchanged module inputs; byte-equivalence evidence retained.

## Verification and material findings

- W exact native schema/consumed requests and55 fixed config restrictions pass;
  catalog reproducibility/preservation, full Go/tagged deterministic and109
  browser contracts pass. Final W CI42533307656 success.
- W initial CI42532327561 exposed SQLite cold bootstrap race, reproduced current
  2/20 and base3/30. Existing predecessor lock moved before lazy first query/WAL.
  Deterministic test fails old source (28672-byte initialized DB while lock held),
  passes fix. Original cold conditional test unchanged; one count100 lane,
  focused storage/fence/cancellation and full quicks pass. Same schema/WAL/FULL/
  timeout/receipts/recovery; no new lock/retry layer. W1 disk log omission honestly
  recorded, native tool output retained without rerun.
- R naming mismatch guards, tagged compile, local protocol, Ruby3tests119assertions,
  pin/module/Node/diff pass. Fresh absent-before-build vendor proof passes digest
  sha256-jUWhtHeiuyvh4Rzf/0KePGFrG72pNimtH6GBKJhRVkk= (55s final batch).
- C active hooks, final graph/eval/diff and whole managed DeepSeek exact Draft7
  profile/catalog validation pass. Private native load passes; malformed catalog
  rejects. No credentials/model call or profile change. S single joint checker
  and complete runtime/llm locked-object equality pass.35nodes/all edges+follows,
  extension and six sibling closures preserved.
- Exact R CI42534510998 attempt1 terminal FAILURE: fast/archive success, creation
  failure, host skipped. Creation job128895731073 log
  `ci-runtime-42534510998-creation.log`: thread/resume RPC-32600 alternate vs
  current primary. No rerun. Supported provider incompatibility R2 blocks release.
- Small private no-inference probe was incomplete: untouched thread lacks rollout,
  so resume fails before provider guard. Native PID/thread/process group fully
  joined; no HTTP inference/history rewrite. Wrapper cat exit0 is not probe pass.
  No further diagnostic expansion; CI and intentional native guard suffice.
- Candidate native/prepared sources were collected unrooted during review. Exact
  cache retrieval/original prepared-copy reconstruction reproduced same paths/
  hashes; explicit session `gc-roots/` and W disjoint old-native/tool roots now
  retain prerequisites. Historical check results remain scoped; outputs collected
  since proof are not claimed currently readable. Preserve all roots.

Known environment corrections: short TMPDIR avoids Unix socket108-byte limit;
existing notes cover it. C reuses W's realized Python validator; aborted offline
source-bootstrap tooling command fully exited. No product change for either.

## Review, monitoring and next action

Mandatory reviewer0 retained gpt-6.1-sol/xhigh/read_only,
thread01a1bd45-41c9-71e0-ab51-f96af1e8fada; general/architecture/scope/risk lanes.
Read-only report is returned via lead transport and saved by lead; no reviewer
writing required. Four source histories inspected; no final report received yet.
Review does not accept pending native/CI gates. Packet includes exact disposable
naming harness SHA4384c86e11826b288cc3928d8a6a56af3ac2bc43f55ddc8954395e4cf7ba72b4.

Long watchers use installed9yib package catalogf2d5a890... gpt-6-luna/low/full_access,
operation lifetime. Managed CI observer797275ea failed tool interface without
invoking commands, native terminated completed; visible minimal parent gh
fallback observed terminal CI. Resolution212b2387-14f9-4053-a3a1-2f09ada672ad
settled external-effect uncertainty without changing failed result.

Next: receive final review and user R2 decision. Native/VM/system/composition
builds remain unlaunched. [Rollout](rollout.md) preserves original system/profile,
full target/alias and exact prepared commands. Selected switch has no idle-only
flag: final native change needs EXTERNAL shell in coordinated natural-idle window,
including lead/team/watchers; do not launch inline or interrupt other sessions.
Prepare concrete exact outputs first. Default integration needs separate explicit
user approval; deployment alone cannot release its lineage obligations.

Initial tracking committed527362b66. Subsequent records maintained under normal
checkpoint cadence. Session remains open; no cleanup/lifecycle action authorized.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-codex-version-update/
