# Final review packet

Review the completed deliverable directly in all four lanes: general, architecture and repetition, scope and proportionality, risk and compatibility. Read the mandatory-change-review skill and all four references. Do not edit sources, deploy, launch long tests or delegate.

## Request and acceptance

Add a new default development preset with exactly a gpt-6.1-sol/xhigh lead and gpt-6-astra/xhigh reviewer. Lead owns investigation, design and edits. Display concrete default model/effort in New session. The user selected resetting both controls whenever the starting team changes and deployment on aitherdev. No merge, archive, delete or unrelated member reconfiguration is authorized.

Initiative: 2026-10-07-lead-review-defaults. Read plan.md, design.md and state.md in this directory.

## Branch inventory

### dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-lead-review-defaults/dev-workspace
Base: 9e8e6e87a5a4844d4639ddf4008de483d1897f4c
Head: a2bbf2f1c588de7eec0d7d52580a89a9d4bef984
Final diff: dev-workspace-final.diff

Complete feature commit series:

- 514af7190792fa5272b7a92beaf881712349b360 teams: support development teams implemented by the lead
- a2bbf2f1c588de7eec0d7d52580a89a9d4bef984 portal: select concrete lead defaults for new sessions

### workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-lead-review-defaults/workspace
Base: 079394ded6c49ea1ff2b6131eb11908b8be0240a
Head: 43e83a2a5d795a2f6a1a2255a50b6de4adc8572c
Final diff: workspace-final.diff

Complete feature commit series:

- 8540d5a04da946fffad87a875fe2ddde33737945 inputs: select lead-owned team runtime
- 43e83a2a5d795a2f6a1a2255a50b6de4adc8572c teams: default to a Sol lead and Astra reviewer

### vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-lead-review-defaults/vpsfree-cz-configuration
Base: 5447020fccf99705e65a907cfe6e80684a5a1577
Head: cfa61475e57e12d3cc980844dfe00384cca14271
Final diff: vpsfree-cz-configuration-final.diff

Complete feature commit series:

- cfa61475e57e12d3cc980844dfe00384cca14271 inputs: set devWorkspace to a2bbf2f1

Workspace registration began at 70035dfe565058054e30efe2562c655c80dd183c. Its later base 079394ded6c49ea1ff2b6131eb11908b8be0240a is the initial tracking-only commit on shared master, not a feature change. Shared master tracking is published separately.

## History, migrations and commit split

No migrations in any branch. No schema, database, API field or journal version was introduced. No obsolete approaches or branch-only compatibility shims remain. The initial combined generic commit was split into catalog and portal commits with an identical final tree, then the existing selector-source assertion was corrected and folded into the portal commit. Generated input updates were consolidated to one per consumer. None of these feature revisions has been merged, released or deployed. Superseded hashes were referenced only by unpublished or superseded feature pins and CI; no production state was created. Verify this conclusion independently.

Catalog validation, projection, tests and its documentation form one behavior commit. Portal controls, browser regression, matching HTML tests, documentation and app.js cache version form another. Each consumer has a separate generated input pin. The site preset, its instructions, ownership documentation and policy assertions form one behavior commit.

## Ownership and consumers

Generic dev-workspace owns schema-4 catalog validation/packaging, Go catalog load, teamruntime projection and the browser form. Actual consumers include the vpsFree extension pinned at 0ff827df13e82dfab4b536ff29979280f264e8f5 through the workspace flake; the composed workspace passes config/agent-teams.nix to mkPackage. Configuration dev-workspace/devWorkspace selects the same generic runtime for its host module and Codex assembly. The application remains a workspace user-profile package. Extension and sibling pins/follows paths are preserved. No extension source or codex-web source edits. Inspect imports and pins rather than relying only on this list.

## Compatibility and boundaries

High risk: cross-project catalog semantics and deployment/mixed-version ordering. General, architecture, scope and risk lanes all apply. Schema 4 and roster/receipt formats remain unchanged. Older validators reject the newly supported lead-owned composition, so its catalog must be shipped with its matching runtime; old catalog presets remain supported. Saved rosters, fork selections and submitted retry bodies retain their exact choices. Normalize only unsent legacy drafts whose model and effort are both empty. Catalog acknowledgement remains required on changed catalogs. No client protocol, generated clients, Terraform, database or fleet change.

The local host operator is trusted under generic AGENTS.md; remote browser clients are untrusted. Keep existing backend input validation and request locking. No new security framework or lifecycle transition behavior is intended. Existing forward-only profile switch, journal, cluster and global session quiescence checks remain authoritative; do not bypass refusals. Host configuration deploy first, then composed workspace user profile. Correct newer package is the supported recovery path.

Non-goals: removing existing presets; changing retained teams; removing empty defaults from all other portal/CLI/API flows; changing the selected Codex version; introducing a new mode or catalog schema; automatically substituting another model/effort when discovery omits a catalog default; merging or closing sessions.

## Documentation

Changed generic docs/dev-sessions.md and docs/workspace-portal.md (team ownership, catalog invariant, creation defaults and retry/version contract). Changed site docs/agent-teams.md and AGENTS.md (default lineup, models, ownership). Existing generic workspace-portal transition/host sections and configuration docs/operations/codex-deepseek-aitherdev.md checked. Temporary rollout details belong to this initiative rollout.md; no new release numbers or permanent rollout checklist added.

## Quick checks

- Focused Go agentteams validation, teamruntime projection/member creation/retry and web HTML/client/archival tests passed. Commands and raw evidence: quick-checks.log (initial output truncated) and lead-access-check.log, explicit-selector-check.log (final focused selector check).
- node --check on app.js and creation_settings_browser_test.cjs passed.
- Actual Chromium TestNewSessionSettingsBrowser passed (creation-browser.log/result JSON): pending and failed model discovery, team reset, manual choices/reload, legacy draft, catalog acknowledgement and locked submitted retry body.
- Generic nix flake check --no-build --show-trace passed (nix-evaluation.log). Positive Nix fixture formerly deep-forced a whole derivation graph; evaluate helper now forces drvPath to reach validation without stack overflow.
- Site agent_instructions_test.rb: 8 runs, 144 assertions, no failures. Root AGENTS byte limit passes (16354 bytes).
- Composed workspace nix flake check --no-build --show-trace passed (workspace-evaluation.log).
- Deployment input contract checker passed at final generic head. Configuration hooks Nixfmt and commit-msg passed; generated width warnings retained per instructions.
- git diff --check passed; all three feature worktrees clean.

Automatic initial CI failed only its stale source-text selector assertion; failed logs retained as ci-original-failure.log, focused corrected test passed. Current head has a fresh automatic run, not yet accepted. Superseded run cancellation was attempted and denied HTTP403. Long local package tests/builds have not been launched pending this review.

## Reviewer selection

No retained roster: this initiative was created --no-codex; same-session team list refuses without a valid lead thread. Installed catalog package /nix/store/y0j44svpcdpqzvjj43n5kg06iqfnxvzv-dev-workspace-0.2.0 has default development team delegated; lexicographically first review-purpose role reviewer uses gpt-6.1-sol/xhigh, read_only, fresh_context. Matching native TOML share/dev-workspace/agent-teams/delegated/reviewer-xhigh.toml, name dw_f1f5803be5453d8dd8e3707a3dcb1b1265e4f095e05ab472. Standalone fresh reviewer uses these exact settings; this fallback does not reconfigure a team. Confirm identity/settings in the report; distinguish settings verified from any unavailable runtime metadata.

Return findings ordered Blocking/Important/Advisory with file/line, commit and lane. Explicitly assess the entire branch history, obsolete-history disposition and migration lineage (state no migrations). State residual risks and gaps if there are no findings.
