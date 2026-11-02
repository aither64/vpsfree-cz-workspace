---
lifecycle: active
---

# Temporary service cleanup proposal

Proposal recorded in [design.md](design.md), authored by `architect0` and
accepted by the lead against the user brief. The session
stays open for the user's continuation. No implementation or live cleanup is
authorized.

## Phase checklist

- [x] Identity and Full-team roster verified.
- [x] Architect assigned investigation/design with explicit proposal boundaries.
- [x] Selected package behavior and ownership gap documented.
- [x] Minimal proposal and disposable verification plan recorded in design.md.
- [x] Lead acceptance inspection completed; recommendation prepared for presentation.
- Implementation, quick runtime checks, independent final change review,
  integration tests and deployment: outside this request; none performed.

## Owners, dependencies and acceptance

`architect0` owns read-only technical investigation and design.md; lead owns
tracking and user presentation. Retained implementers/reviewer have no proposal
execution assignments. Acceptance: the design explains the current gap, exact
ownership/launch API, cleanup before file deletion, interruption/recovery,
legacy-resource limits, alternatives, smallest project boundaries and focused
future disposable checks. Lead inspected the complete design and confirmed coverage of these acceptance
criteria. This is proposal acceptance, not implementation or integration approval.

## Evidence and commands

- `dev-session current` and both DEV_SESSION environment markers match
  `2026-11-02-session-temporary-service-cleanup` and
  `/home/aither/workspace/ai/vpsfree.cz`.
- `dev-session team list … --as-is`: Full team (`delegated`), all retained members
  ready; architect0 Astra/xhigh, workspace_write. Settings preserved.
- Read workspace routing procedures and documentation/handoff skills.
- `dev-session team assign … --to architect0 --message-stdin`: delivered.
- Architect verified this session's exact creation metadata: schema 3, ready,
  provider `codex-lb`; provider/team settings unchanged.
- No registered repositories or project worktrees; shared checkout is master.
  Unrelated shared changes and index contents are preserved.
- Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/

## Architect milestone

Selected package reverified via workspace-host status:
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
Source inspection confirms quiesce/retire handles native Codex/team/tmux, not
independent user services. `archive_with_access` invokes
`WorkspaceTrackingSummaries.prune(..., apply: true)` before
`prepare_archive_journal!`; cleanup only in final retirement or the ordinary
quiesced phase would be too late. The proposed durable inventory/fence and
verified stop must precede the first prune. No live lifecycle checks were run.

## Proposed boundaries settled by architect

- Local systemd USER transient services only; register ownership durably before
  launch, one identity per preview/candidate, native cgroup descendant cleanup.
- Pre-feature sessions without inventory coverage must declare a complete
  inventory or audited-empty result before archive/delete. Unit names, pathnames,
  ports and PIDs cannot authorize adoption or shutdown.
- Escaped or remote processes need separate ownership reconciliation; universal
  discovery is not claimed.
- Existing lifecycle operation policies and sealed file/Git proofs are retained.
  A durable cleanup intent precedes the first prune; retry uses the same original
  archive/delete operation.

## Results, risks and next action

The recommendation and fixture verification brief are in [design.md](design.md).
Lead acceptance checked the design against the full user brief and confirmed the
reported pre-prune source ordering at installed wrapper lines 2134–2135.
The design identifies the exact inspected package, derivation and source graph
entry; source-only findings are distinguished from live behavior verification.

Recommended ownership: reusable dev-workspace only; generic agent launch guidance
and at most a workspace pointer, with no extension runtime or production config
change indicated. Native user-service/cgroup launch is the supported boundary;
legacy unknown coverage blocks destructive cleanup. This is the main migration
tradeoff for the user's decision. API spelling, timeout defaults and package
compatibility details still require disposable verification during any later
implementation. No implementation readiness is claimed.

No runtime tests, build, CI, deployment or usability verification were performed.
Local checks cover record whitespace, active front matter and relative links.
These are planning/investigation records, so automatic independent final change
review is inapplicable; any later committed implementation requires its normal
quick-check, mandatory-review and integration-test sequence.

Next action belongs to the user: decide whether to request implementation or
revise the proposed supported boundary/migration gate. Stop after presenting;
leave this session open and active for the user's continuation.

## Cleanup and authorization

No live service inspected/stopped/removed, no lifecycle operation, no package
switch, deployment, merge, cross-session grant or other-session access. Only
this session's proposal/tracking files may be written. Lifecycle stays active;
completion or handoff does not authorize session closure.
