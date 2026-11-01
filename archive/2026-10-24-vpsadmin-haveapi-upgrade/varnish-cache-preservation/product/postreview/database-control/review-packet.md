# Inherited API test database and worker cleanup: final review packet

Clean local head `fbd0b9379839dd0e747a00b5bd63e4be98880889`, tree
`700dd72dea72992cf876496b283532ef6468878b`, is committed and quick-green.
**Source writer released; stop before full foundation topics, publication or site repin.**
Lead owns retained reviewer0 assignment/acceptance. Request affected all four
lanes at HIGH risk, retaining reviewer0's Sol/xhigh settings. The whole branch
contains security changes; the new correction itself changes test infrastructure.

Session `2026-10-24-vpsadmin-haveapi-upgrade`; repository worktree:
`worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-oauth-client-logs`.
Authoritative bounded brief: `design.md:6963` and the control-setting clarification
at `design.md:7102`. Lead authorized the conditional repair after valid mechanism
discrimination; native/source evidence is below. Plan/state remain lead-owned.

## Complete history and scope

Base `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a` to this head has six commits:

| Commit | Purpose |
| --- | --- |
| `11b26c0a5f6fa51fc6eb63b8f28dd5e8ccbaf721` | Released HaveAPI packages |
| `ccb08e3cebb06f46b4dddea3a86baec31f1ff5b3` | OAuth documentation/client consumer |
| `967da811892062ffc82d4cd98a43ed6a7e7a5a28` | Derived documentation selectors |
| `9cff7f2a14f8316468623d57a81482598beef98e` | PHP callback diagnostics |
| `7219ab22a49f666077056fc2f093424547294aeb` | Persistent-log defaults and preserved Varnish routing/cache proof |
| `fbd0b9379839dd0e747a00b5bd63e4be98880889` | Inherited test database semantics and failure cleanup |

The first five commits remain **literally unchanged**, including authorship,
messages and tree history. Their complete review was accepted in
[the prior review receipt](../../review.md). This correction is a separate
inherited-infrastructure defect, rather than a revision of those product changes.
It is one coherent commit because the explicit database contract and cleanup
of committed concurrency fixtures address the original foundation failure chain.

[Full history with authorship](complete-history.txt),
[exact correction commit/authorship](correction-commit.txt),
[7219-to-final correction](correction.diff),
[complete base-to-final diff](complete-final.diff),
[hash/source/history binding](final-proof.json).

The correction has three paths, +36/-3:

- `tools/test_db.rb`: temporary server explicitly selects REPEATABLE-READ and
  `innodb_snapshot_isolation=OFF`; startup emits actual version/isolation facts.
- `api/spec/models/mail_templates_spec.rb`: accounts for every worker before
  committed-fixture cleanup and retains the original/first failure.
- `docs/agent-instructions/testing.md`: documents the test contract and the
  separate product READ-COMMITTED contract, with an owning-source link.

One released HaveAPI update stream remains; no repeated pins, obsolete bypass
add/remove pair, new dependencies or CI workflow edits are introduced.
**NO MIGRATIONS:** the complete base-to-final diff has no migration/schema changes.
Earlier historical live/recovery lineage remains in the accepted prior packet;
this packet makes no literal-ancestry claim for older rewritten deployments.

## Controlled evidence and its limits

Original run41245794195/attempt1/head7219 failed full/core foundation RSpec;
the original logs/results/manifests, setup evidence and artifact hashes remain
in the parent postreview directory. Actual CI jobs used MariaDB11.8.6,
Ruby3.4.12, AR8.1.4/mysql2 0.5.7/HaveAPI0.32.0. The historical effective snapshot
variable was not recorded and is **not asserted** from its version.

The valid local mechanism control uses the unchanged representative
`cluster_resource_adjustment_concurrency_spec.rb:68`, core seed25558, one actual
MariaDB11.4.12 server/client, Ruby3.4.9, the same effective bundle and source7219.
Only the owned disposable server's globals change before fresh RSpec children;
both workers' effective settings are asserted before classifying the result.

- Unmodified default RR/OFF passes.
- OFF: worker sessions16/17 both RR/OFF. Competing commit22; old ordinary read20;
  original current-value adjustment26 passes.
- ON: worker sessions22/23 both RR/ON. Commit22 and old ordinary20 remain;
  the original adjustment aborts with native errno1020/SQLSTATE HY000.

Native71070 completed0; its three child statuses are0/0/1, the last an intentional
negative control. Owned server2284370/start8874792 is absent; children were waited.
[Actual control identities/results](global-control/control-result.json),
[OFF events](global-control/off-events.jsonl),
[ON first SQL error](global-control/on-events.jsonl),
[effects](global-control/effects.json).
This establishes the **11.4 mechanism**, not an exact historical11.8 reproduction.
The socket-readiness failure, Array-row instrumentation failure and invalid
constructor-only ON contrast are retained and explicitly excluded from causal
proof in `readiness-1*`, `instrumentation-1/` and `corrected-control/`.

## Quick verification of the final patch

The actual tested dirty7219 patch equals the committed correction byte-for-byte
(SHA256 `b540bd0edb02b4389c791ff5c4584054b841245f9d6050bdaf2d163e7f3f22b9`).
No source changed after those checks. [Binding](final-proof.json).

- Declared API shell: syntax of both changed Ruby files passed; component
  `bundle exec rubocop` inspected both with no offenses.
- Native quick91212 completed0. The new runner's real server argv contains both
  explicit settings; its startup records actual version/RR/OFF.
- Normal cluster adjustment plus concurrent mail reconciliation:2/2 PASS.
- One controlled post-commit worker exception: the original
  `ControlledWorkerFailure` survives, both workers are absent, and committed
  marker/template/translation counts are0. The following existing source-marker
  lock example passes. The injected child exits1 intentionally; this is not
  reported as an all-green native RSpec run.
- Normal root shell commit60970 completed0. All five pre-commit hooks and
  commit-message hooks passed. TextWidth issued advisory warnings for two body
  lines over72 columns; all message lines satisfy the workspace80-column rule.
- `git diff --check`, local documentation link and clean index/source checks pass.
  Writing/Humanizer guidance was applied directly to the technical paragraph.

[Quick commands/results and native server identity](quick/quick-result.json),
[normal worker settings/values](quick/normal-events.jsonl),
[worker-error cleanup evidence](quick/cleanup-state.json),
[native JSON with failed-control then passing marker](quick/worker-error-result.json),
[fixture effects](quick/effects.json), [normal hooks](commit.log).
Scratch observers inject only public synthetic failure data; no product retry,
transaction change, broad runner framework or dependency installation is added.

## Remaining review and verification boundary

Review the first-failure/cleanup semantics and diagnostic contract as well as
the complete six-commit history, update-stream consolidation and NO MIGRATIONS
conclusion. `tools/test_db.rb` owns the temporary DB contract consumed by its
manual CLI and spec setup; product database configuration remains READ-COMMITTED.
No auth, model locking, Varnish, nginx/PHP, schema or site source changed here.

After accepted review, the lead must release the full/core foundation topics and
final source/publication/input binding. They have not run for this correction.
The published feature remains7219 as last verified; no publication or site repin
occurred. No global CI success is claimed. Existing observer87797 continues only
published7219 integration run41245794185; its original failure evidence is retained.
All live33d6/private/updater3922 paths, recovery refs and prior roots remain intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
