# Managed lead implementation and rollout takeover

Retained root 01a153f2-476c-7710-a39f-75ad837fbe94 is this initiative's lead.
This transfers ownership from the external conversation, superseding your earlier
idle-only initial request. External lead will observe only after your acceptance.
Do not add a team. Read plan.md, design.md, state.md and applicable routed guidance.
Workspace /home/aither/workspace/ai/vpsfree.cz; verified initiative
2026-10-19-session-creation-end-to-end; live roster null. Lead owns code.

User: session creation still fails with “creation journal has missing or unknown
fields”; prior claims of complete fixes were wrong. User explicitly requires
coverage of the creation process as a whole, not one parameter. User accepted
the proposed plan and said “Implement the plan.” Standing direction authorizes
aitherdev deployment, then affected default master merges and release only after
this fix is deployed and actually verified. No native Codex patch or rebuild.
The external lead has not deployed this candidate or claimed full acceptance.

Completed:

- New ordinary initiative created via dev-session start, actual native root above;
  initial plan/state/design committed/pushed before project edits and requested
  deletion. Original setup commit 7b25bc4a. No inherited external binding existed.
- Own registered worktree worktrees/2026-10-19-session-creation-end-to-end/dev-workspace,
  same named branch, base f27925c43460066424dd8d6c4ab8ad93a267d60b.
  Published head 8d1d43a (one functional fix with its regression), clean.
- The shared Go reader agentteams.DecodeCreationJournal omitted optional provider.
  Ruby writer already supports it for schemas 1/2/3 and both states. Go now uses
  codexproviders.ValidID and returns optional Provider without changing formats.
- Added creation_journal_contract_test.go. It runs the real Ruby journal producer
  (prepare_creation_journal and ready_creation_journal/write) and actual Go reader
  for 3 schemas × 2 states × 4 provider selections, plus bad type/syntax, unknown,
  missing and duplicate field rejection. Passed in 8.931s through declared Nix
  shell with TMPDIR=/tmp. gofmt and git diff --check passed. There is no declared
  hook framework in generic runtime or root. Full workflow test NOT implemented.
- No mandatory final review yet: intended substantive deliverable is incomplete.
  Do not treat the producer contract as the user's requested end-to-end coverage.

User-requested removal is DONE, do not retry the request:

- Request 61cdf917-6900-4fa3-89a0-bf8b059db8c3, receipt
  b9ccc2bf15ef4fd0c6fa4a6f1d71daf861834a76de5c0d28bcf9a3055a8ac592,
  destination 2026-10-19-haveapi-async-client-plan, root
  01a153e8-7364-7321-b0ae-0f636dd6824b. Source was untouched.
- Ordinary dev-session delete --force accepted via normal y confirmation.
  It first stopped at thread_retiring: exact archive proof found the idle root,
  but RetireThread directory discovery did not see its alternate-provider root.
  No lifecycle record was edited and no guard bypassed. Global TUI archival also
  refused because the workspace App Server owned its writer.
- Exact-root native thread/archive through the workspace socket verified ID/cwd
  and idle first. Evidence stuck-root-retired.json and bounded operator script
  retire-stuck-root.py. Then the SAME normal delete resumed and all phases passed,
  tracking deletion commit 926a566f. Private recovery retained. Pending journal gone.
- Read-only status now reports conflict (“recorded session creation identity
  changed”), and destination is absent. Never POST retry on the user's request;
  stale-post prevention must be tested on disposable fixtures instead.
- A first Nix shell unnecessarily snapshotted large root getFlake; canceled before
  script execution and corrected to small runtime flake. No running command remains.

Remaining accepted implementation (complete it, do not narrow coverage):

1. Implement mandatory packaged browser/native creation acceptance in generic
   runtime. Existing nix/tests/session-archive-lifecycle.nix and its browser
   driver show real host module/user service/authenticated Chromium setup.
   Existing codex-web/codex/recovery_integration_test.go (read-only source at
   worktrees/2026-10-18-provider-switch-redesign/codex-web) demonstrates stock
   native binary against deterministic loopback Responses SSE provider. There is
   no reason to patch/rebuild Codex or require real credentials in CI.
2. Use actual shipped portal, form serializer, ordinary HTTP routes, async naming,
   Ruby initializer/journal, stock native App Server, root/member creation,
   initial message, proof, canonical redirect and normal conversation follow-up.
   Only simulate the EXTERNAL model service. Never replace creation or status
   endpoints, write fabricated ready receipts, stub the initializer or hold naming
   forever as the earlier optional browser admission test does.
3. Test representative auto/custom names; inherited/default-explicit/alternate
   providers; solo/multi-member teams and captured model/effort/instructions;
   sensitivity/notifications/attachment delivery; forks and approved-plan new
   sessions with destination provider selection and preserved source. Assert
   completion and usability, correct provider, durable consistent receipts/journals,
   one initial user turn and no duplicate destination/root/member identity.
4. Test reload, interruption, portal restart and idempotent retry before native
   creation and after initial-send acceptance. Use test-only external barriers,
   no product test hooks. Fail promptly on terminal errors. Include failed error
   rendering/selection/Copy error and deletion/stale-retry on fixture requests.
   The full test must demonstrably fail with the old broken reader. A newly
   added Go test that cannot compile on old source is not that failure proof.
5. Add flake check and mandatory CI on EVERY push/PR (dedicated KVM job patterned
   on archive check; exclude VM from fast job). Check latest official versions
   for imported actions when editing workflows. Keep this scoped; no speculative
   generic test framework. Update README/test guide and preparation compatibility
   documentation, apply user-facing writing skill yourself before commit.
6. Finish quick checks, clean intended commit series, and independent final review
   covering all four lanes, full history/no migrations and no repeated pin streams.
   Select reviewer from installed catalog default development team since roster
   null; actual settings govern. Fresh Luna/low utility for uncertain tests,
   package builds and CI. Preserve failed-run evidence and diagnose before reruns.
   Source Go checks need -mod=readonly, TMPDIR=/tmp and absent host provider
   catalog DEV_WORKSPACES_CODEX_PROVIDERS to avoid ambient host configuration.
7. After full packaged acceptance passes, publish final runtime and create own
   workspace/configuration feature worktrees. Read their AGENTS. Preserve nested
   runtime override and extension/codex-web/native identities; update matching
   configuration channel with confctl inputs channel set --commit. One final pin
   stream per consumer. Composition checker and exact artifact preparations.
8. Prepare/approve/reserve/activate system then application through normal
   coordinator jobs. No direct confctl activation or ledger editing. Finish any
   lifecycle journals first, preserve other rollouts and exact upstream frontiers.
   DO NOT use an automatic deploy_first run that merges before LIVE acceptance.
9. Live browser acceptance must actually create usable dedicated sessions and
   complete follow-up for default/alternate provider, team, fork and plan paths.
   Existing user's request stays removed. Clean only owned test sessions under
   accepted plan authorization. Read-only health/assets/constructed envelopes are
   insufficient. Preserve actual test request IDs, final slugs/thread IDs and
   statuses so claims are inspectable without secrets.
10. Only then perform conditional master integrations through the normal driver,
    accept exact final CI/remote proofs, release own reservation through finish,
    maintain state/portal and concise result. Leave initiative open and retain refs.

No active external process, deployment, reservation or integration run is owned
by this initiative. The initial branch push may have started existing automatic
CI; it is not final acceptance. Whole intended suite/review remains to be done.

Please first write takeover-acknowledged.md confirming ownership and next action,
then implement and continue autonomously through the accepted finish line. You
may read the managed portal conversation for this task; the external lead will
send the exact accepted-plan clarification in the takeover message. Do not ask
again for permissions already recorded here; stop only for an actual missing
approval or recovery constraint that cannot be resolved within the scope.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-session-creation-end-to-end/
