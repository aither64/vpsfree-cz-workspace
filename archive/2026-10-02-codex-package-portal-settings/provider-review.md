# Provider publication review packet

Scope: complete committed generic dev-workspace branch before publication for
dependent pins. This is not the final cross-project readiness gate: exact
configuration, extension and consuming-workspace heads will follow in a final
packet to the same reviewer. No application builds or browser integration have
been launched. Publishing the generic feature may trigger its existing CI.

Initiative: 2026-10-02-codex-package-portal-settings; shared workspace
/home/aither/workspace/ai/vpsfree.cz. Read plan.md, state.md and design.md here.
Worktrees are under worktrees/2026-10-02-codex-package-portal-settings/.

Provider dev-workspace base 869b8d4728394127ba949dc76724dce56eae136b;
head c1bb968d4027544e5c333e7781c9a037a7d3645a. Entire series:

- cf84da79735a280a060653e28d3ad803e5eb3587: settings presentation and existing
  browser regression. No settings API/storage changes.
- 0f67f70ed5b91f99d9350eb85eb0e404e8513414: isolated Codex 0.160.0 input pin;
  required llm-agents transitive bun2nix/nixpkgs locks only. Primary generic
  nixpkgs and codex-web pins are unchanged.
- c1bb968d4027544e5c333e7781c9a037a7d3645a: shared assembly, focused provider
  check and owning documentation, bundled because they specify/test its contract.

Inspect the complete base-to-head diff and series, not only the last commit.
No obsolete branch approaches or fixups remain. An unpublished coordination
commit accidentally included staged new files and was immediately amended to
the dependency-only commit above; file content was preserved. It never reached
a remote, release or deployment. No new migrations or persisted formats are
introduced in any component. Upstream SQL migration paths and hashes in main,
queue and thread-history are unchanged from 0.159.2 to 0.160.0; disposable
old/new/old reader verification is still pending after review.

Requested outcome: normal plain Codex daemon startup (not forced no-daemon),
0.160.0 in system/workspace, no dirty-settings text, one desktop row at
1280/1440 and existing mobile wrapping. Preserve drafts, Apply/Cancel, saving,
errors, stale polling, argument forwarding, helpers/completions and ELF bytes.

Non-goals/rejected alternatives: no Rust rebuild or upstream daemon-lifecycle
patch (#10132), no source override from a moving PR, no paid model turn, no
state/schema migration, no unrelated toolchain/client refresh, no global nowrap
or new screenshot framework. Deployment is authorized, integration into any
default branch and session archive/delete/stop are not.

Owner/public interface: generic dev-workspace owns lib.mkCodexPackage
{ pkgs; codex; }, wrapping selected upstream native output. Current consumers
are lib.mkPackage (generic -> extension -> full workspace) and aitherdev's
configuration consumer (draft at its companion worktree config.nix). The latter
uses it for both system codex and codex-ds; the system does not install the
workspace application. Other pinned consumers remain unchanged until feature
publication. Discover consumers from actual imports and pins as well.

Compatibility: runtime-root symlinks are materialized; native binaries keep
store references, retained workspace Codex roots/system generations retain
closures needed by daemon copies. Native daemon selection is independently
verified and not claimed permanently pinned. Existing workspace ownership,
generation, lifecycle, runtime-authority and cluster formats remain unchanged.
The local operator is trusted to administer the development host; remote clients
remain untrusted. Review ordinary mistakes/concurrency/data safety, not defenses
against an already compromised local operator. No fleet-coordinated update.
System generation retained; workspace recovery stays forward-only via supported
switch/retry. No root pruning or production GC is planned.

Docs changed: generic README, docs/dev-sessions.md and docs/codex-package.md.
The last owns lasting layout, closure, retention and recovery semantics; exact
rollout revisions/results stay in initiative records. Main-context writing pass
completed. Companion site operations draft links to this authoritative contract.

Quick evidence: git diff --check; nix-instantiate --parse for flake/helper/check;
nix flake check --no-build --show-trace (all evaluation checks passed);
node --check app.js and team_settings_browser_test.cjs; three focused Go
template/sidebar/live-authority tests passed in declared Go/stdenv.cc shell.
Actual assembly/browser/schema/daemon/state tests remain pending and must not be
represented as passed.

Risk: high, due shared package/daemon contract, deployment and rollback/state
reading. Required lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Selected eligible retained reviewer0 is independent,
read_only, gpt-6.1-sol/xhigh; use saved settings with no overrides. Read the
mandatory-change-review skill and every lane reference completely, inspect
repository AGENTS.md/context, review yourself with no nested agents. Report
Blocking/Important/Advisory findings with paths/commits and distinct lane
conclusions, whole-series obsolete-history conclusion and explicit no-migrations
conclusion. Do not edit, run long tests, push, merge, deploy or write tracking.
