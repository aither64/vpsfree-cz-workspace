# Final review packet: numbered clipboard filenames

Outcome: repeated images named image.png become image-1.png, image-2.png from the first occurrence. All pasted files are numbered per original filename and session across sends/removal/reload. Both New session and conversation use the shared provider. Text paste, selected/dropped names and existing upload identity/checksum/size checks remain intact.

Initiative: 2026-10-09-portal-codex-usability, created by this conversation with no Codex/root team. Parent owns design/code. Required workspace AGENTS routes: projects, sessions, git, lifecycle, documentation, verification, deployment, knowledge-base, commits, and docs/agent-teams.md. Read affected local AGENTS. Plan/state/design/rollout and complete inventory live beside this packet. All current source changes are committed; quick checks pass. No default-branch integration is authorized.

## Review assignment

Use /home/aither/.codex/skills/mandatory-change-review/SKILL.md, read all four lane references and review general, architecture/repetition, scope/proportionality, risk/compatibility directly without nested agents. Retained independent reviewer native identity 01a120fd-34cd-7272-8ae1-1222ee2f1773, gpt-6-astra/xhigh verified from session_meta and last turn_context. No authorship or roster changes. Threadless session has no eligible roster, so initial catalog fallback is retained. Catalog digest437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd. Overall high due additive browser persistence and deployment/mixed bundles. Remain read-only: no tests, edits, deployment, real session creation, reset use or other side effects.

## Heads / complete series

- codex-web: base 3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c; head 7dab76305dc0084735095d6dbdaef607585d9bca; worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/codex-web
- dev-workspace: base c51ba3c0ca0d41d237ef71c56accd564beb70a33; head 66262519d497073d9bb0dccc2252cdec4528f389; worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/dev-workspace
- workspace: base 21624498189f12fec0424d547c6e21c78145e84b; head 07b393609417e921d5b1c2cfec7b3d89abc473ab; worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/workspace
- vpsfree-cz-configuration: base ae670dc0d4a5d43adf9560da1a6a0a35925cd2e5; head 1f3569902a4a6b02633019cd172eade5afe90005; worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/vpsfree-cz-configuration

Read final-inventory.md and numbered-paste-<project>.diff alongside this packet. Inspect full base-to-head history and final diffs yourself; explicitly conclude whole-branch history and migration lineage. Eighteen commits total. No migrations in any component. Four new commits: shared behavior with tests/docs/cache import, runtime adoption with dependency pins/cache chain and real-browser fixture, workspace nested pin, confctl-generated matching host pin. Browser fixture and dependency/cache/doc edits form one coherent consumer adoption; new provider without matched cache/fixture is incomplete. Prior deployed revisions remain; unconsumed fixes will be folded into their owning commits. Workspace rebase is patch-equivalent; no feature has entered default branches.

## Contract / consumers / boundaries

Provider conversation/assets/uploads.js owns allocation and cloned File. Pasted draft entries optionally retain sourceName. Existing draft array stays unchanged; separate <storageKey>.clipboard-numbers holds [originalName, highWater] pairs. Names reserved synchronously, seeded from full authorized catalogue and drafts, including sent files. Generated stems fit255 UTF-8 bytes at Unicode boundaries; extension/type/lastModified/bytes preserved. Picker reselection clones matching sourceName under the same assigned name; transferUpload public validation contract is unchanged.

Consumers: provider mountConversation and standalone cmd/codex-web-example, portal conversation and New session mountUploads calls. Runtime Go module, flake source and vendorHash align at7dab76305dc0; workspace and configuration align at66262519, preserving extension0ff827df. Provider upload import v6, portal conversation import v14, app?v29; stylesheet unchangedv6. No new server API or database/catalog/ledger/manifest/journal/cluster format. Older drafts remain readable; older bundles ignore new metadata and can resume by selecting a file under its assigned name. A forward package fix preserves browser metadata; existing forward-only lifecycle policy governs deployment recovery.

This is filename convenience, not UUID identity/security. No server counter/rename endpoint, atomic multi-tab naming guarantee, cross-device history beyond available catalogue, or renaming existing/selected/dropped files. Existing exact-origin, scopes, quota, UUID creation receipts, chunk prefix checks and frozen creation recovery remain. File-storage byte validation is in scope. Trusted local operator boundary from runtime AGENTS applies.

## Documentation / verification

Provider docs/reference.md explains naming, counters and old-bundle recovery; portal README Prompt attachments describes user behavior. Design.md owns current brief; rollout.md owns executed/proposed rollout details. No public KB change. Parent applied the user-facing writing skill directly.

Quick: provider Node suite64 passes; latest focused upload suite39 passes including picker names. Provider/portal syntax and whitespace pass. Focused runtime Go internal/web Test(AutomaticArchival|Browser|Uploads) passes0.105s. Confctl precommitNixfmt and commit-msg hooks pass (generated width warning allowed). Composed deployment checker passes current runtime.

Dependency metadata build initially refused misaligned flake/Go pins before hash computation; parent aligned both. Fresh utility rerun produced expected fake-hash mismatch, new vendorHash sha256-Sh4RbvbmQMxOUryukIEnEsE/eT5RkpVanAc0Qmrmb+Q= adopted. Logs /tmp/portal-numbered-paste-vendor*.log retain evidence. These are metadata-generation runs; long final integration not started.

After review: provider packaged checks, affected real browser fixture, runtime evaluation/generic-source, composed workspace checks/package, aitherdev build and exact-head CI, through fresh Luna/low utility. Parent then dry activation and guarded host/profile switching with fresh observation-only utilities; read-only served-asset and account smoke. All three actual resets must remain intact.
