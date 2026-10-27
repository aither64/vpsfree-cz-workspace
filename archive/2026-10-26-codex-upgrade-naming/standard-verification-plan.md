# Standard final-input verification

Recovery/manual-input follow-up is approved for implementation and autonomous
deployment. The prior352a results below are retained at their actual scope.
New source needs focused browser/server regressions and committed affected review
before long checks. Prefer normal exact-head automatic fast/creation/archive and
the existing session-recovery-boot check when final changes affect it. Reuse the
host-module output only with identical successful derivation/inputs; do not repeat
both VMs by habit. Native/client255/vendor evidence remains unchanged unless final
inputs prove otherwise. Normal final consumer/package builds and same-native live
verification remain. One utility operation at a time; no new check framework.

Before package/VM verification, run the existing focused mounted-page browser
regression after committed affected review. Owner3 prepared ordinary Nix
Playwright1.59.1 prerequisites (both paths already valid) and Go selection
`^TestQuestionBrowser$/^page_lifecycle_browser_test[.]cjs$`, Chromium and Firefox.
The existing fixture uses a disposable TLS server and absent provider catalog.
Estimate2–5minutes; reassess at5 without treating quiet time as failure. Preserve
original output/exit and stop at the first failure, no blind retry. Lead has a
native fresh Luna/low utility slot; selected5slsx policy digest3ff7a212 and matching
native utility full_access/never were verified. No check launched in preparation.


Current disposition,2026-10-27: final runtime352aa4c6 is accepted and published.
Client255 review/publication/automatic CI and actual final vendor computation pass.
The corrected existing two-attribute host batch passed exit0/995s on exact352aa4c6;
both outputs are valid and original command plus fresh watcher settled. See
[actual host receipts](host-vm-352a/outputs.json) and [current state](state.md).
Previous35d6 host failure was traced to three stale test fixtures, fixed narrowly
and directly inspected; its original failure evidence remains retained.

Exact runtime push run40493270858 completedSUCCESS: fast, creation and archive
pass; its host job is skipped and covered by the two successful local VM outputs.
Final configuration4a725/workspacea834 are matched and published. System build
passed0/134s, profile build0/642s with normal packaged checkPhase, and copy-only
passed0/23s. Final output identities were inspected without native/vendor replay.
Dry activation passed0/18s; ordinary system switch passed0/38s with both health
checks and exact system/profile irpd verified. Selected application5slsx and
ordinary native5rm5/0.164 are observed running after the external cutover. That
proves target identity, not original stage-command exit receipts or corrected UX.
Current operation ownership and the new same-native rollout are in state.md and
rollout.md. The sections below preserve original planning context.

Planning only. No local check/build, CI dispatch or monitoring utility was
launched. Runtime was not yet published at inspection; local HEAD was
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686` plus implementer0's work. Final runtime
results must bind its committed published head after final review/source freeze.

The existing [runtime workflow](../../worktrees/2026-10-26-codex-upgrade-naming/dev-workspace/.github/workflows/check.yml)
and [README Development section](../../worktrees/2026-10-26-codex-upgrade-naming/dev-workspace/README.md)
already define the required checks. No source additions are needed for CI:

| Job | Trigger and normal command |
| --- | --- |
| `fast` | Every push/PR/manual dispatch: `nix flake check --no-build --print-build-logs`, then `nix build --no-link --print-build-logs` for all exported checks except `host-module-idempotency`, `session-recovery-boot`, `session-archive-lifecycle`, `session-creation`. Includes packaged source/Go/Node/Ruby checks and the package. |
| `creation` | Every push/PR/manual dispatch: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation`. KVM VM uses the installed portal, browser, initializer and native App Server with synthetic Responses. Existing source covers naming/retries plus creation/fork/plan/provider/recovery paths. |
| `archive` | Every push/PR/manual dispatch: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle`. KVM VM covers packaged browser/native archive, recovery and revival using disposable sessions. Repository README requires it before deployment. |
| `host` | Default pushes or manual dispatch only: `nix build --no-link --print-build-logs .#checks.x86_64-linux.host-module-idempotency .#checks.x86_64-linux.session-recovery-boot`. Branch pushes normally skip it. |

The branch push automatically supplies the first three jobs. Prefer preserving
one successful final-head run to repeating these locally. No bespoke managed
naming VM, retirement campaign or real inference check is proposed. Synthetic
VM results cannot establish deployed configuration or real-provider behavior.

After runtime publication, select its exact SHA/run without launching anything:

```sh
gh run list --repo aither64/dev-workspace --workflow check.yml \
  --branch 2026-10-26-codex-upgrade-naming --limit 10 \
  --json databaseId,headSha,status,conclusion,url,startedAt,updatedAt
gh run view RUN_ID --repo aither64/dev-workspace \
  --json headSha,status,conclusion,url,jobs
```

After final review, lead can assign one fresh Luna/low utility to observe the
selected existing run with `gh run watch RUN_ID --repo aither64/dev-workspace
--exit-status`. It must not relaunch jobs. If required standard jobs were not
triggered, ordinary `gh workflow run check.yml --repo aither64/dev-workspace
--ref 2026-10-26-codex-upgrade-naming` supplies all four jobs, including host;
confirm necessity before duplicating an existing final-input run. Local VM
commands above are alternatives for an actually missing result, not extra gates.

Recent successful [base run40378571631](https://github.com/aither64/dev-workspace/actions/runs/40378571631)
at `7e6d7c9c` took fast10m31s, archive13m03s and creation18m40s in parallel;
host was skipped, total18m42s. This estimates the normal batch, not this final
head's result. README's dependency-update target is under20 minutes. Reassess
an overrun; silence/time alone does not justify cancellation or imply failure.

Stop when the required jobs pass at the exact final runtime head with no
superseding input change, and configuration/profile owners supply their final
build proofs. On failure, retain job logs and actual conclusion, notify the
owning implementer and diagnose before any rerun; no automatic retry. One global
utility slot remains lead-controlled (currently implementer0's quick batch).
Implementer1 owns configuration/system builds; implementer2 owns workspace/profile
builds. Both were directly notified that this package launches no duplicate
builders. A later post-review host dispatch, if selected by lead, is a standard
workflow operation and needs no new harness.

Client025's new branch already has successful packaged
[Check40385717557](https://github.com/aither64/codex-web/actions/runs/40385717557)
at exact `02533a152223416f159bac2578e88bcbe653f247`, elapsed83s. No repeated
client run is needed absent changed input or an actual unresolved failure.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/
