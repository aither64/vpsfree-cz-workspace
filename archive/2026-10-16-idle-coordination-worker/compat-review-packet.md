# Final compatibility and composition review

Independent final committed-deliverable review under /home/aither/.codex/skills/mandatory-change-review/SKILL.md. Read all four lane references and perform the review yourself, read-only, without nested agents or long checks. Read root AGENTS.md, routed git/lifecycle/verification/deployment/documentation procedures, each affected worktree AGENTS.md, and plan.md/design.md in this directory. Use current packet and exact ranges below; older review-packet.md is historical.

## Outcome and boundary

User requested idle sessions instead of token-consuming reservation polling, then instructed implementation and aitherdev deployment through vpsfree-cz-configuration. User later authorized: "then wait for reservation and proceed. when it is deployed and verified, you can merge it". This covers three repositories/master only after live acceptance. Preserve FIFO, approvals, claims, review reservations, exact reviewed state, synchronous/manual behavior, and uncertain-effect recovery. Reuse native notification transport; no Codex upgrade, codex-web edit, foreign journal mutation or session adoption.

Acceptance: background submission durably returns before preparation; independent systemd continuation runs while agent is idle; intermediate reservation/progress events stay in status; final/actionable notice is deduplicated and preserves native settings. Pause/lifecycle/package handover fence future admissions; exact original steps/jobs survive crash/restart. Operational completion keeps session active for review.

## New correction and baseline

Original independent all-lane review at earlier heads is review-report.md; narrow remediations are review-remediation.md. Now runtime rebases onto upstream archive-local-first 59833652; sole merge conflict was the archive fixture dependency list, resolved retaining BOTH workspace-tracking-sync.rb and workspace-integration-background.rb. Review complete final branch plus interactions, especially tracking/archive and package recovery.

Predecessor profile refuses metadata integration.journalSchema=2 while ANY schema-1 manual journal is pending, and its Go metadata decoder rejects new top-level fields. An older completed session still has a pending manual journal; changing foreign state is outside scope. Our unmerged correction keeps package.json.integration EXACTLY {journalSchema:1, certificationSchema:1} and installs share/dev-workspace/integration-contract.json: {schema:1,journalSchemas:[1,2],certificationSchema:1}. New Store uses this optional sidecar; missing means legacy schema-1 reader only. Contract keys/version/certification/read set are checked. Active AND completed schema-2 journals prohibit legacy-only downgrade. Pending manual journals stay unchanged for their owner; no automatic retry/migration. Strict Go legacy metadata validation restored, no broadened old ABI. No ledger/snapshot/attempt/adapter/native format changes.

Probe with ACTUAL predecessor Store and disposable pending manual journal passed; source SHA/evidence in compatibility-predecessor-probe.json and .rb. Product-focused tests: 3 runs / 33 assertions passed for pending manual upgrade, active/completed schema-2 downgrade and invalid/forward reader sets. Go TestLoadInstalled passed. Ruby syntax/diff check and pinned nixfmt check passed. Final consumer composition contract also run. No long verification started for this correction yet; review precedes it. Old package/CI evidence does not certify this revision.

## Ownership, risk and selection

High risk: persisted state, package-transition compatibility, host deployment, native notification/crash recovery. All four lanes: general; architecture/repetition; scope/proportionality; risk/compatibility. No retained roster (live team list has roster null). Prior standalone reviewer absent from live agent list, identity/settings cannot be verified; fresh standalone fallback is installed default_development_team lead_reviewed, review-purpose reviewer gpt-6-astra/xhigh/read_only. Catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd. Matching behavior TOML: /home/aither/.local/state/dev-workspaces/profile/share/dev-workspace/agent-teams/lead_reviewed/reviewer-xhigh.toml. Confirm your actual settings and read-only behavior.

Local development operator trusted: review ordinary concurrency, ownership, integrity, recovery and untrusted remote clients; do not require hostile local operator filesystem hardening.

## Complete history, migration and update streams

No database migrations. Journal schema 2 is newly introduced by this single unmerged feature, never deployed/released/externally consumed. Schema-1 manual journal support retained. Sidecar is new contract schema 1 and changes no existing persisted representation. Metadata-2 abandoned iteration removed entirely. No intermediate feature candidate/pin deployed or released.

Runtime has ONE feature commit combining continuation, pause, notification routing, capability advertisement and directly supporting docs/UI/tests; these are coupled behavior. Workspace has ONE policy commit plus ONE final nested runtime input update. Configuration has ONE generated final confctl update. Prior pins consolidated, no intermediate retained update commits. Inspect complete series independently and explicitly conclude history, stream consolidation, and migration lineage.

Provider is generic dev-workspace. Consumers: workspace nested vpsfree-dev-workspace/dev-workspace runtime override, extension fixed 767dfd587e346168e1443e65ccdb67ce748f3fe3, configuration devWorkspace selected through dev-workspace/devWorkspace channel and NixOS host module; application remains workspace user profile. Both consumers select final runtime. No new mkPackage arguments or changes to extension/native APIs. Discover other representative consumers from actual pins/imports as needed.

Owning docs: runtime docs/integration.md (upgrade and background contracts), docs/coordination.md and docs/coordination-operations.md. Workspace docs/coordination.md plus routed git/verification waiting guidance. Configuration docs/operations/workspace-coordination-aitherdev.md checked, unchanged. README integration link checked. Technical English edited by context-owning lead under workspace writing guidance. Individual rollout and historical evidence stay here in rollout.md and immutable evidence artifacts.

System then profile selection under SAME original reservation. Queue currently held by startup-fix session; our original system job remains requested/waiting. Startup on own owner is ready. Prepare new exact snapshots, approvals and refresh original queued job after final review/builds; never activate stale old snapshots. Forward recovery only once selected. No reboot, forced release, archive/delete or foreign mutation.

## Requested report

Findings ordered Blocking/Important/Advisory, file/line and exact commit with concrete scenario. Conclude full branch histories, pin-stream consolidation, journal lineage and upgrade/rollback safety; state no database migrations. Include residual verification gaps. Do not edit product or tracking, rubber-stamp, launch checks lasting >1min, deploy or message other sessions. Return report to lead.

## Exact ranges

### dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/dev-workspace
Base: 598336522fbb490e7606670d5fdb504e66c607ec
Head: 79da0bb5eafd5b8e7cd4e32a02dc5a16da6116f6
Complete series: compat-review-dev-workspace-series.txt
Final diff: compat-review-dev-workspace.diff

### workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/workspace
Base: 78c1257dbe88ddec30799cf3d4f3bda629b5970b
Head: 524ba50b692a00b5119f4a35f194de67026737b0
Complete series: compat-review-workspace-series.txt
Final diff: compat-review-workspace.diff

### vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/vpsfree-cz-configuration
Base: 500a197a3a4da1702ac6dc1c41f7286ffd4d7f68
Head: 35eeeddcfbcdf192c3cb2d0576ba364d38f9c6f4
Complete series: compat-review-vpsfree-cz-configuration-series.txt
Final diff: compat-review-vpsfree-cz-configuration.diff

