# Final cross-project branch review

Review the complete committed branches and their final diffs for initiative
2026-10-02-codex-package-portal-settings, workspace
/home/aither/workspace/ai/vpsfree.cz. Read plan.md, current state.md, design.md,
provider-review.md and provider-review-result.md. This is the final whole-branch
source review before manual long verification and deployment, not permission
to merge or a claim that execution gates have passed.

All application changes and pins are committed; source worktrees are clean.
Tracking/packets are maintained under the normal uncommitted tracking cadence.
Exact worktrees: worktrees/2026-10-02-codex-package-portal-settings/<project>.

## Complete series and migration provenance

| Repository | Base | Final head |
| --- | --- | --- |
| dev-workspace | 869b8d4728394127ba949dc76724dce56eae136b | 40838aa28c8433e42a4a3fbed4586a3df0146de9 |
| vpsfree-dev-workspace | 074926d33f7306288f7cfad87c6a85e8a430e750 | c56f981a950ab763b71dc91c59e8b5256d478851 |
| vpsfree-cz-configuration | 2758415cc11d719f22b341cee4e8e77c773c141f | 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d |
| workspace | 98389138caef0576dfa7a101d1dbcdbae943b0af | c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee |

Generic entire series:

- 22377c4417448c9f9fda2e8173d4762ce2c7b6b6: UI presentation and supporting
  existing browser regression, including the provider-review remediation.
- 4d527ae5b0d26b8eede7f6c256e5bd1686bdda6f: dependency-only Codex 0.160.0
  and its required llm-agents transitive locks.
- 40838aa28c8433e42a4a3fbed4586a3df0146de9: shared assembly/export/consumer,
  focused provider check and authoritative docs specifying that behavior.

Extension entire series:

- c56f981a950ab763b71dc91c59e8b5256d478851: generic exact source URL/lock,
  no extension behavior or site/provider changes.

Configuration entire feature series after current-default merge base:

- 80a5a5c23af774a8a540fde7aaef37341993fc0f: aitherdev helper consumer and
  site operation docs; input prerequisites remain separate.
- 81ac31c29d5de0ece5d2d0b67bac7fdd415eefd4: generated confctl llm-agents
  exact pin, with changelog disabled for this noisy input.
- 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d: generated confctl generic exact
  feature pin and required transitive locks, useful changelog retained.

Initial configuration base was 029c616e. Remote default advanced through four
published scheduled-input commits: b3cabc2b (stable/production/staging nixpkgs),
d2c99b8b (unstable nixpkgs), 6025f12a (vpsAdminOS staging), 2758415c (llm-agents).
Only flake.lock changed in that default advance. The consumer patch was rebased
onto it; range-diff proved 6f3efd09 -> 80a5a5c2 identical. Its old unpublished
435a4e60 input commit was removed and regenerated from the new base as 81ac31c2.
This retains upstream default updates, not feature-owned unrelated refreshes.
The current system deployment will therefore use this newer default baseline.

Workspace entire feature series:

- c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee: extension exact source URL/lock,
  full consuming user-profile package unchanged apart from selected runtime.

Workspace shared master is 98389138; dedicated branch checked against it before
this pin commit. The earlier initial tracking commit on shared master is not
feature integration and introduces no reusable workspace behavior.

No obsolete approaches, fixup commits, unused compatibility paths or transitional
migrations remain. The generic source was cleaned before publication: earlier
cf84da7/0f67f70/c1bb968 were unpublished, unreleased and undeployed. Their UI
remediation was folded into 22377c4; dependency and assembly patches are
range-diff equivalent to 4d527ae/40838aa. Only 40838aa was published as provider.
No old feature revision has been consumed externally or deployed.

Migration inventory: no migrations, no persisted workspace format changes.
All 73 upstream SQL paths and blob hashes are identical between Codex
rust-v0.159.2 tree ff6aec96948b70d94983af2641a6b67c94faeff5 and rust-v0.160.0
tree a956835d020762cb2b570053af06f643a11c0ecc. Both nonempty tree inventories
were verified. This does not establish general serialization/old-reader
compatibility; the disposable runtime probe remains mandatory.

## Outcome, boundaries and consumers

User requested normal Codex startup, 0.160.0 in dev-workspace/aitherdev, and no
unsaved-settings text stretching the desktop controls. They selected normal
daemon operation, one row at 1280/1440, mobile wrapping and feedback underneath.

Preserve native bytes, arguments/exit status, helpers/completions, Nix closures,
drafts/Apply/Cancel/stale-poll/error semantics and existing state/ownership/
generation/lifecycle/cluster contracts. The x86_64-linux-only helper assembles
cached outputs; it does not rebuild Rust. Representative consumers are generic
mkPackage, extension's delegation, full workspace's selected extension, and
aitherdev system codex/codex-ds using the same helper. Discover actual imports
and lock paths instead of relying only on this list.

All four lock graphs resolve llm-agents
6334544a4bfd921086a252caccc6c1c6eb1d18c7. Configuration has direct and generic
nested nodes, both exact633. Workspace/extension generic pins are exact408;
full workspace extension pin is exactc56. Generic primary nixpkgs/codex-web and
site/team/provider configuration are unchanged by the feature. Do not install
the workspace application through system configuration.

Non-goals: forced --no-daemon, moving PR source overrides, Rust/daemon-lifecycle
patch (#10132), new API/schema/migrations, unrelated clients, global nowrap,
new screenshot infrastructure, paid model turns, custom freeze/kill barriers,
global-state rollback promise or credential/config copying into evidence.
User authorized feature pushes and deployment, not default-branch integration,
session archival/deletion/stopping or destructive state restore.

The local workspace operator is trusted to administer this host. Remote inputs
remain untrusted; assess ordinary wrong-path/concurrency/state/secret risks,
not filesystem defenses against an already compromised operator.

## Review reconciliation, documentation and quick evidence

Your provider review found one Important intermediate-width UI overlap. Lead
accepted and assigned a narrow remediation: internal composer wrapping and
select sizing; containment/pairwise-overlap coverage now at 981/1024/1100/1200/
1280/1440/390 with realistic labels. Lead inspected final diffs/range-diff and
Node syntax/whitespace passed. Review step 9 permits direct verification of this
in-boundary fix; no separate provider rerun was requested. Include it in this
whole final branch review, without treating geometry execution as passed.

Docs: generic README and docs/dev-sessions.md link docs/codex-package.md, the
lasting layout/GC/version/recovery contract. Configuration's existing
docs/operations/codex-deepseek-aitherdev.md owns site use and links the generic
contract. Main-context writing-skill pass completed. Exact rollout/revisions/
execution and the deliberately limited online baseline belong in session
records; no deployment has yet occurred. Review placement and discoverability.

Quick checks passed: Nix parse of generic helper/check/flake and aitherdev
module; generic/extension/workspace nix flake check --no-build --show-trace;
Node syntax for app.js and final browser regression; focused Go template/
sidebar/live-authority tests; whitespace checks; required configuration hooks
on all its commits; consuming-workspace deployment-contract checker proves
matching runtime and portal identity. Generated confctl text-width warnings
were non-failing and generated messages were preserved as required.

Long verification is not complete. Existing push-triggered provider/extension
CI is observed by fresh Luna/low monitor_provider_ci, exact runs 36999356818 and
36999495059. Manual long application/build/browser/daemon/protocol/state checks
and aitherdev build wait for this review. No CI reruns or default-branch writes.

## Deployment and recovery gates

After review, execute provider/package checks, real browser regression and
generated experimental-schema validator. Session compat_probe.go exercises
synthetic old->new->old thread/settings/queue/fork state without model turns;
daemon_probe.py uses private CODEX_HOME for normal CLI/resume/fork, native
daemon copy/version/restart/stop. These are prepared, not passed. Inspect their
scope if relevant; they never connect to production sockets or use real auth.

Build only aitherdev, stop/investigate unexpected local kernel compilation.
Verify each assembled output's closure and real running daemon version rather
than equating command versions. Retain old system generations/workspace roots;
no production GC or root pruning is authorized.

Architect's follow-up design clarifies SQLite online baseline: all existing
top-level stores, per-database consistent only, no global snapshot. Resolve
SQLite home, then run sqlite_baseline.py privately outside Git/portal before
any candidate access to real state. Baseline completion/integrity is a cutover
gate, not authority to restore old queues/DBs over writers. No 11GiB rollout
copy is required for this forward-only assembly cutover, and no host-loss or
zero-data-loss guarantee is claimed. If a new destructive conversion or
compatibility failure emerges, defer cutover and scope supported recovery.

Dry-activate and activate system feature from configuration worktree, then
stable workspace-host switch --source the full workspace feature worktree.
Supported preflight/quiesce/deferred-retry/journals govern busy sessions; do not
bypass or kill sessions. Workspace rollback refuses older profiles: retry the
same supported operation or correct forward. System recovery retains prior
generation, but never rewinds Codex data automatically. Live versions/services,
root retention and UI are separate post-deployment gates.

Risk high due shared runtime/daemon contracts, host deployment and state/rollback.
Use retained reviewer0 gpt-6.1-sol/xhigh/read_only, no model/effort override.
Read mandatory-change-review plus all four lane references and applicable
workspace/repository guidance. Review all lanes and complete series yourself,
no nested agents. Report findings with severity/path/commit and explicit
whole-branch obsolete-history and no-migrations conclusions. Do not edit, run
long tests, push, deploy, merge or mutate tracking.
