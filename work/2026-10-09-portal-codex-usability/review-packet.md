# Review packet

Requested outcome: quiet automatic refresh, compact confirmed model/reasoning with an Edit dialog, credits and safe confirmed banked resets, and binary clipboard attachments with unchanged native text paste.

User decisions: 30 continuous visible seconds before transient refresh warnings; 750 ms initial loading, 250 ms manual history loading; retain polling rates, tune shared code policy; dismissal discards settings drafts; count-only reset redemption is allowed with confirmation. Tests must never consume actual resets (user has three).

Design and current evidence: [design.md](design.md), [plan.md](plan.md), [state.md](state.md). All intended project changes are committed and quick checks pass. No prior independent review. No default-branch integration authorized.

Overall risk: high because reset use is an irreversible account operation, protocol and browser persisted retry state change, and four-repository deployment ordering matters. Review lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. Parent read all four lane references.

Reviewer: installed catalog default_development_team lead_reviewed, lexicographically first review-purpose role reviewer, GPT-6 Astra/xhigh/read_only. Fresh standalone fallback: threadless initiative has no valid retained lead or roster. Catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.

## Whole-branch inventory

No migrations. No database, ledger, uploads, manifest, journal, cluster or runtime-authority format changes. The browser uses an existing verified durable-attempt store for a new origin-scoped reset record. No superseded approaches or follow-up fixes remain in committed feature history. The workspace was rebased onto shared master tracking commit 747e9a87; its originally registered base is 4ac9ef3e. Tracking is exempt from feature review.

### codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/codex-web`. Base `3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c`; head `fc73d85ca50916f3979b28d96cbf77bf85eae925`.

```
dd13156b051c1ae32bc9bc409b622b5eb5d58e18 codex: expose account credits and idempotent limit resets
8263ccd44587a50148242d4e94d2e582d6bda759 conversation: attach binary clipboard files from the composer
fc73d85ca50916f3979b28d96cbf77bf85eae925 conversation: keep refresh quiet and edit settings in a dialog
```

Final diff: [codex-web-final.diff](codex-web-final.diff).

### dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/dev-workspace`. Base `c51ba3c0ca0d41d237ef71c56accd564beb70a33`; head `901af601e841b12bfa3a2c45953a7fc745a2ab4e`.

```
65c93f8b97836427beb9114b0d4064201b5e3219 portal: keep refresh values visible and compact model controls
e8e2e2ed813dd1c1c08fe7328de119ea943b1f4e portal: show credits and confirm banked reset use
901af601e841b12bfa3a2c45953a7fc745a2ab4e inputs: select the updated Codex web integration
```

Final diff: [dev-workspace-final.diff](dev-workspace-final.diff).

### workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/workspace`. Base `747e9a875c23a7a760fcb3ce18d7d7a51f3015e5`; head `c91d1f1613a8f476e3fd7501fdd84c1bce0c4513`.

```
c91d1f1613a8f476e3fd7501fdd84c1bce0c4513 inputs: select the portal usability runtime
```

Final diff: [workspace-final.diff](workspace-final.diff).

### vpsfree-cz-configuration

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-codex-usability/vpsfree-cz-configuration`. Base `ae670dc0d4a5d43adf9560da1a6a0a35925cd2e5`; head `049bad1c4da298b6d39f85b9d508c691fda3678d`.

```
049bad1c4da298b6d39f85b9d508c691fda3678d inputs: set devWorkspace to 901af601
```

Final diff: [vpsfree-cz-configuration-final.diff](vpsfree-cz-configuration-final.diff).

## Commit scope and consumer map

codex-web separates explicit account protocol support, binary clipboard uploads, and the chat refresh/settings presentation. The latter shares current-thread confirmation, stale-read fencing and quiet notice lifecycle, so those UI changes stay together. dev-workspace separates chat presentation, account reset UI/backend with recovery fixtures, and mechanical dependency pins. Shared dialog styles accompany chat presentation; the account browser fixture also covers its clipboard interaction. Workspace and configuration each contain one mechanical pin change.

Provider: codex-web owns account types/reset RPC, uploads, refresh policy, notice helper and conversation sync. Consumers: generic mountConversation/reference app and dev-workspace portal (Go import, browser asset import and Nix source/module pins). Workspace composes its unchanged extension source with the generic runtime; configuration selects the same runtime for the host module. Preserve optional capabilities and existing conversation.Client; account mutations have a separate exact-origin route.

Scope limits: trusted local workspace operator per dev-workspace AGENTS.md; remote clients remain untrusted. Do not add defenses against an already compromised local administrator. No runtime settings UI for refresh policy. No Codex version/model migration, session/team/lifecycle redesign, KB writes, default-branch merge or reset consumption during testing. Account identity is required for redemption to avoid retrying against a different account.

## Verification and documentation

58 codex-web Node contract tests passed, including delayed failures, visibility and page restoration, native text paste, binary/mixed uploads, late catalog population and stale model reads. Three pure mocked reset-action tests also passed. Focused Go account/client tests passed. Portal focused limits/reset/cache/template tests and TestShippedBrowserClientMatchesSessionAPI passed against the published Go dependency (GOWORK=off). Selected Codex 0.160.0 generated experimental schema corpus validation passed. All branch whitespace checks passed; config Overcommit Nixfmt and commit hooks passed. Deployment composition check passed at runtime 901af601. Vendor hash generated from Go vendor output; packaged build still pending.

Long packaged suites and real Playwright fixtures have not been launched. They must follow review resolution. Automatic push CI may run independently for published provider/dependency branches.

Project docs: codex-web/docs/reference.md explains optional account data, explicit idempotent reset RPC, shared refresh and clipboard contract. dev-workspace/README.md explains sidebar reset confirmation, account binding and saved attempts; docs/workspace-portal.md explains dialog drafts and shared refresh. Existing docs/workspace-portal.md user-profile transition sections and site deployment guidance remain authoritative. Individual deployment record will be rollout.md in this session, not project feature docs. User-facing writing skill applied by parent after facts settled.

Deployment: publish codex-web, pin/publish runtime, compose workspace and confctl channel; validate host/profile match. Build/dry-activate/deploy aitherdev host then switch workspace user profile through workspace-host. Preserve live Codex under existing compatible transition, no schema migration or coordinated machine update. Recovery uses a newer fixed package under forward-only policy. Do not perform rollback to an earlier committed runtime merely for testing.

Please inspect all committed base-to-head series and final diffs, instructions, docs, tests and actual consumer pins. Report Blocking/Important/Advisory findings with lines and lanes. Explicitly conclude whether obsolete branch history remains and whether migration lineage is sound, including "no migrations". Do not edit code, redeem live credits, deploy, run long checks, or spawn nested reviewers.

Historical packet: final diff artifacts have been refreshed to the exact final heads in [final-inventory.md](final-inventory.md); original reviewed commits remain identified above.
