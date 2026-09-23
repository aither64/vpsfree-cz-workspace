# Real persistent Codex teams

## Goal

Replace the virtual managed-team implementation with independent persistent
Codex threads that can be controlled consistently from the portal and the
terminal. The initiative keeps the existing session tmux layout: one attached
lead conversation per development session. Specialist threads remain headless
until assigned work and retain their own history for the lifetime of the
session.

## Design

- `lead` is the permanent root thread and the only member resumed in the
  session's tmux `dev` pane. `dev-session attach <slug>` continues to attach
  that tmux session unchanged.
- Each other member has a real App Server thread and a stable compact address:
  `architect0`, `architect1`, `implementer0`, and `reviewer0`. The supported
  roles are architect, implementer, and reviewer; addresses are never
  renumbered or reused.
- The portal and `dev-session team` use one package-owned team runtime and the
  same durable roster. There is no separate agent simulator, message broker,
  database, or background scheduler.
- `dev-session team assign --to architect0` submits a correlated App Server
  turn to that member. Members report to `lead` through one package-owned,
  member-bound stdio MCP tool that calls the same assignment path on the host.
  The tool never accepts a session slug, sender, or recipient from the member;
  its launch binding and the private roster establish those values. There is
  no separate broker, queue, or background scheduler; a busy target uses App
  Server's ordinary turn/steer behavior. The read-only architect/reviewer
  shells remain read-only and never receive the shared portal socket.
- A new member receives a real configured thread but no model turn until its
  first assignment. The creating App Server connection writes one internal
  developer item to materialize the otherwise absent headless rollout, then
  verifies its exact marker before declaring the member ready. An uncertain
  injection is never blindly repeated. Member model and reasoning-effort
  settings apply to the next turn; a single assignment may override them.
  Long builds and tests use a fresh Luna/low watcher utility and never appear
  in the roster.
- Member creation registers a real App Server project with a durable
  idempotency key scoped to the workspace, session, root thread, and member
  address. The returned project UUID is stored before `thread/start`; an
  uncertain start is reconciled within that project. Ambiguity fails closed
  instead of allocating a second thread. Assignments carry stable retry IDs.
  A fork keeps the source roster snapshot and refuses retry after the source
  changes.
- Team presets are editable starting points: `Solo — lead`, `Lead-designed
  team — lead · implementer0 · reviewer0`, and `Full team — lead · architect0 ·
  implementer0 · reviewer0`. UI labels use human-readable text without
  underscores. The site policy uses GPT-6 Sol for every retained team role,
  preserving role-specific high/xhigh efforts, and GPT-6 Luna/low for the
  operation-scoped verification watcher. GPT-6 Astra is not selected
  automatically.

## Final portal cleanup and integration (2026-09-23)

- Remove the Team tab's redundant Assign work form and its browser-only retry
  code. Retain the team assignment API, CLI command, and member reporting path;
  users can message a ready member directly from the Codex tab. Align the
  Codex-tab Member label and selector, including at narrow widths. Keep the
  index-page host label supplied by workspace configuration.
- Audit the dirty shared workspace checkout by owner and provenance. The
  archive worker is not presumed to own old records or generated captures.
  Preserve unrelated session files; only their owners may curate or commit
  them. Keep confirmed generated artifacts in place but allow exact-path,
  local-only excludes to make status usable; record these paths. Do not bulk
  stage, delete, or archive unresolved evidence. A dirty shared checkout must
  not cause data loss during integration.
- After code and documentation commits pass quick checks, run one consolidated
  Sol/xhigh review, then use fresh Luna/low utilities for long packaged checks
  and the aitherdev switch. Check the live Team and Codex tabs before merging.
  The user has approved integration into the affected default branches after
  these final fixes. Rebase and capture the exact final feature heads, then
  fast-forward codex-web, generic dev-workspace, the vpsFree extension, and
  this workspace in dependency order. Retain feature refs and do not integrate
  an unrelated configuration branch.

This cleanup changes no roster, ledger, session, database, CLI, or API format.
Old and new browser assets use the same server contract; existing sessions and
member threads remain readable. The forward-only aitherdev package deployment
still requires the active generation to satisfy cluster transition checks.

## Portal feedback follow-up (2026-09-23)

The next deployment is one review unit, not a new team transport. Finish these
steps before another consolidated Sol/xhigh review:

1. Replace preset option rosters with total member counts and role counts;
   keep exact model and effort controls visible elsewhere. Show a copyable,
   live `dev-session start` command on the new-session form. An interactive
   CLI invocation asks for the initial request; portal uploads are not part
   of the command.
2. Keep Add member available after every Team tab refresh, populate newly
   inserted model and effort selectors from the live catalog, and collapse
   removed members below the active roster. Bound the member-message pane's
   scroll area and show timestamps.
3. Add a ready-member selector to the Codex tab. Selecting a member opens its
   complete independent conversation, with direct chat and uploads scoped to
   its thread. Browser writes share the team operation lock with add, remove,
   and configure; direct sends and queued turns rebind the saved per-member
   policy and model settings. Reject removed, unknown, or cross-session
   addresses. Keep `lead` as the tmux-attached root conversation.
4. Update the codex-web, generic, extension, and workspace package pins;
   perform quick checks, one consolidated review, then Luna-watched packaged
   checks and aitherdev deployment. Verify the controls in the deployed portal
   without modifying the unrelated test session.

The opaque browser conversation ID is session slug plus `~` and the member
address; it is not persisted and never substitutes for the roster identity.
The roster schema, App Server thread format, CLI interface, creation receipt,
and session lifecycle format do not change. Existing ready members become
selectable after deployment; removed members remain visible only as history.
The codex-web submission ledger retains its schema but adds an optional
snapshot of nonempty model/effort options. This ensures an uncertain member
send retries with the original policy even if the saved member setting has
changed. Old attempts without options continue in their previous wire form;
an old nonempty attempt lacking a snapshot fails closed. The single aitherdev
host is quiesced during the forward-only package switch, so no cross-version
ledger writer is supported; rollback is not required.
Rolling back this browser feature would remove direct member chat but leave
their threads and messages intact. This development host remains a forward-only
deployment; no coordinated machine or database update is required.

## Earlier deployment phases (historical)

The initial direct-thread runtime is committed, but the deployed system is not
accepted: creation deliberately rejects team selection, the Add member action
has not been demonstrated end to end, the UI hides actual default settings, and
the active generic package omits both development-cluster providers. Complete
these phases before declaring the initiative finished:

1. Restore the extension-bearing package chain. Pin the feature generic
   runtime in vpsfree-dev-workspace and that extension in the workspace feature
   worktree; verify both provider catalog entries, existing cluster-state
   transition requirements, and installed skills before switching the aitherdev
   user profile. Restore the workspace's vpsadmin/vpsadminos provider declaration
   without touching unrelated sessions or further resetting cluster state.
2. Make real team selection part of new-session creation in portal and CLI. Use
   the installed site team catalog for exact lead/member model and effort
   values; project designer to the compact `architectN` address. Snapshot the
   selected policy in a new creation receipt schema, create all specialist
   threads before the lead's initial request, and resume interrupted member
   creation without allocating another address. Existing sessions remain
   accessible and can add a roster later.
3. Finish the Team tab and settings UX: show human-readable preset names, role
   and exact model/effort summaries, concrete choices in all creation controls,
   prominent add/configure/remove actions, pending-member retry, and inline
   failures. Verify actual browser submission against the deployed portal.
4. After quick verification and all code commits, switch the composed profile
   to restore the installed review and writing skills. Run one consolidated
   GPT-6 Sol/xhigh mandatory review; address findings, then run long checks
   with fresh GPT-6 Luna/low watcher utilities and exercise team, tmux,
   lifecycle, and cluster behavior end to end.
5. Live acceptance found that member shells cannot access the host transition
   lock or shared portal socket, so their instructed CLI report path is not
   functional. Add a scoped host-side MCP report tool for every retained
   member, reapplying its exact per-member config before every assignment
   turn, including after fork or reconnect. A new member is bound only after
   its thread ID exists; no unbound tool is installed during start/fork.
   Verify that a read-only member can report after reconnect, that two
   sessions cannot cross-address or
   borrow one another's tool binding, and that the lead sees the report in
   CLI and portal transcripts. Review the final committed correction before
   another packaged build and aitherdev switch.

## Compatibility and deployment

This is a forward-only aitherdev cutover. Existing virtual-team records have
no retained member value: keep their root conversation and expose an empty
editable roster after upgrade. Existing direct rosters and creation receipts
remain readable; new direct-team creation uses a distinct receipt schema, not
the retired virtual binding. Preserve filesystem, tracking, worktrees, tmux,
root thread, and lifecycle journals. The site catalog is package-pinned for
new creations; each accepted request retains its exact selection for retry.
The workspace application is deployed from its user profile, never system pins.
No configuration-master integration or rollback support is requested. Package
switches must still obey existing cluster generation and ownership checks;
unsupported state fails closed instead of being reset for convenience.
The member roster keeps schema 1 but changes `projectId` from a synthetic
string to App Server's project UUID. The old direct-team package rejects a
roster after the new package starts a member; rolling back that package would
require operator repair of the roster and is intentionally unsupported on this
single development host. Deploy the new codex-web client, generic runtime,
extension, and workspace pin together through the user-profile switch before
retrying any pending member start. No database migration, generated NixOS
option, external API, Terraform contract, or vpsAdminOS node update is involved.
The added `bootstrapAttempted` and `retireIntent` roster fields are scoped to
incomplete member creation or verified empty-thread recovery. A package built
before this change may not safely resume those intermediate states, consistent
with the forward-only cutover; the active package must reconcile or fail closed
without changing the lead thread, tmux identity, or cluster ownership.
The report tool is a new package-owned per-thread configuration, not a roster
schema or persisted message format change. Existing ready member threads gain
it on their next assignment/resume under the new package; idle sessions need
no migration. A package rollback would remove the tool but leave member and
lead thread history intact. This forward-only aitherdev deployment accepts
that loss of the new report capability on rollback; it does not widen member
filesystem or network access to recover it.

## Verification and review

- Test portal/CLI parity, root tmux attachment, roster-local assignment,
  addresses, model/effort defaults, removal, and incomplete-create recovery.
- Test full-team fork, archive/revive/delete, and auto-archive through the
  existing lifecycle suite.
- Exercise the public workspace alias in a browser: lead conversation access,
  `architect1` creation, delegation, activity, and result delivery, including
  a report from a read-only member after reconnect.
- Validate the pinned Codex binary's MCP configuration on the pre-send resume
  for both newly started and forked members, including after reconnect. The
  feasibility probe showed a successful read-only member tool call, then
  showed the tool disappearing after a
  resume without `config.mcp_servers`; every relevant resume must rebind it.
- Check a member-bound tool cannot send from a removed/replaced member or
  reach a different session, and preserve stable message IDs across retries.
- Use fresh GPT-6 Luna/low watchers for every long or uncertain build, test, or
  deployment operation. Run one consolidated GPT-6 Sol/xhigh review after all
  implementation phases, then integration and deployment checks.
