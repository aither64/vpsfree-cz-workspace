# Extension pin independent review

No Blocking, Important, or Advisory findings in this extension publication supplement. Complete report sent to the native lead.

Extension head `c0dad081732dcb10d5df0f276ba358e46bcf3b87` is ready to publish. This conclusion covers pin adoption only; consuming-package checks, workspace/configuration alignment, deployment and default-branch integration remain separate gates.

Reviewer: retained independent reviewer0, thread `01a0fd0c-62f4-7300-8912-2e82ffbab9cd`, `gpt-6.1-sol/xhigh/read_only`, verified against the live roster. Session identity matches the trusted binding; both identity environment variables are absent. I reused the mandatory skill, general/risk references and applicable workspace procedures already in context, read extension AGENTS.md and README, and directly inspected the full history, commit body, final diff and consumer composition. Unaffected architecture/scope assessments were not rerun. No edits, nested agents, tests/builds, publication, CI monitoring or lifecycle action were performed.

General: [flake.nix:6](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/vpsfree-dev-workspace/flake.nix:6) selects exact reviewed runtime `7e4e62b9f7c785e9fc36b8fd3c75c0f864140c75`. Independent parsing of old/new committed locks confirms that only `dev-workspace` and `codex-web` nodes changed, with no other top-level lock changes. The SDK node selects reviewed `4c170393a96ed0a6ac2e43488d073f6fcab36132` and matches the runtime’s SDK pin/hash. Provider, catalog, nixpkgs and llm-agents nodes remain unchanged. The subject/body accurately describe this mechanical adoption; `git diff --check` passes and the worktree is clean at the exact head.

Compatibility: the actual runtime adoption is `40838aa28c8433e42a4a3fbed4586a3df0146de9` → `7e4e62b9`. I inspected the intervening upstream `4bec201` commit: it adds documentation/comments only. Host module, host-path definitions, package API and persistent runtime contract are unchanged across the consumed revision and reviewed feature. Extension `mkPackage` still passes the same siteConfig, teamConfig, providers, namespace/router options and catalog composition to the generic runtime. `nix/host-paths.json` still matches the unchanged generic defaults; no namespace or host-path migration is introduced.

Consumer composition remains extension → workspace user-profile package, with concrete site/team configuration owned by the workspace. Configuration independently consumes generic host support. No application system pin, new helper override or deployment behavior was added. Existing state stays readable by the new runtime, and the feature changes no persistent format; operational recovery still uses a newer generation reverting code, as recorded in rollout.md.

Whole-extension history: exact merge base is `c56f981a950ab763b71dc91c59e8b5256d478851`. The complete series contains one commit, `c0dad081732dcb10d5df0f276ba358e46bcf3b87`, “inputs: select faster portal session creation runtime”. Final diff is flake.nix/flake.lock, 9 insertions and 9 deletions. No obsolete history, superseded iteration, follow-up fix, unused compatibility path or transitional migration remains. There are no migrations; no feature migration/schema version was merged, released, deployed or externally consumed.

Verification limits: this read-only supplement confirms source/lock consistency and relies on the completed SDK/runtime reviews for adopted behavior. No consuming build/test or deployment result is claimed. Runtime exact-head CI remains owned by its separate watcher; downstream alignment and regular consuming checks remain required before final cross-project readiness. No new feature documentation is needed for this mechanical pin change.

The lead should preserve this report and reviewed exact head in state.md. Next: publish this extension feature revision, align workspace/configuration pins and continue the planned verification/readiness supplement. Default-branch merge approval is absent; the session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/)
