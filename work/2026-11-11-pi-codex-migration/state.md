---
lifecycle: active
---

# Pi replacement assessment

## Current status

Implementation authorized by the user's "proceed" in this conversation on
2026-11-12. Start the accepted initial Pi-addition plan; future conversion,
backend migration, Codex removal and default switching remain deferred.
This does not authorize repository-default integration, deployment/profile
activation, or any session lifecycle action. Shared canonical Pi credentials
remain selected; no live login/model request has run.

Initial application worktrees created and registered by the lead:
`worktrees/2026-11-11-pi-codex-migration/dev-workspace` at
`6587c4c1cedabee95bcc52f4667e7d33e3a82859`, and `codex-web` at
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`, both on this session's branch.
Fresh fetched defaults match investigated bases. Existing installed package,
Codex sessions, default selection and shared workspace master are unchanged
apart from owned tracking records. No feature code has been edited yet.

The complete main plan is [implementation-plan.md](implementation-plan.md).
Retained member settings/access are unchanged. Initial implementation dispatch
will hand P0 to implementer1, C-contract design to architect2 with architect0
acceptance, and P1 diagnosis/preparation to implementer0 before app edits release.

## Phases

- [x] Initial scope, same-session roster and access verified.
- [x] Current runtime and Pi capabilities accepted.
- [x] Resource inventory and first architecture recommendation delivered.
- [x] Follow-up isolation/coexistence/extensions/questions/fallback evidence accepted.
- [x] Revised design reconciled and prepared for delivery.
- [x] Authentication follow-up evidence/design accepted.
- [x] Detailed initial Pi integration plan accepted and prepared for delivery.
- [x] User authorized initial implementation; worktrees registered.
- [ ] P0 API/admission/launch probes and concrete neutral contract.
- [ ] Backend seam and opt-in Pi pilot.
- [ ] Provider/team/question/Plan workflow implementation.
- [ ] Intended commits/quick checks, final independent review, long checks/CI.
- [ ] Feature branches ready; separate integration/deployment approvals absent.

## Current recommendation and user constraints

- Preserve current portal UX and its domain ownership. Add Pi beside fully
  writable Codex first; do not emulate the full Codex protocol.
- User explicitly chose "One session cgroup/namespace, with team worker
  processes inside". Use a supervisor per development session, separate loaded
  lead/member worker processes and tool/service descendants. No shared agent
  host across development sessions. This supersedes initial shared-SDK ideas.
- Existing Codex sessions remain editable with their original runtime/history/
  queues/goals/teams/recovery. Legacy shared Codex is a disclosed limitation of
  the proposed transition, not a user-approved exception or performed action.
- A derived Pi conversation is not full-fidelity execution migration. Keep
  source attribution, exact backend identities and one execution authority;
  no automatic history conversion or worktree/resource transfer is promised.
- Use Pi SDK workers or stock RPC with small reviewed first-party extensions;
  choose after supported durable admission/recovery proof. No external extension
  was selected, installed or certified trustworthy. Pin/review actual source,
  artifact and dependencies and verify concrete maintenance before enabling.
- Preserve optional ask-and-continue questions with durable question/reply IDs,
  current browser choice/free-text UI, later authenticated delivery, reconnect,
  holds, corrections and stale-answer behavior. Native Pi dialogs block and
  are process-local; they are not this feature.
- Add inherited session provider defaults plus per-member override and explicit
  finite provider/account/model fallback. Pi virtual models natively route
  physical providers per request/retry, but retry initiation is conditional.
  Structured provider failures, text refusals and unknown outcomes differ.
  Snajpa codex-lb -> subscription Daybreak is requested user configuration,
  not a verified entitlement or automatic cybersec classifier.
- Exact namespace/tool permissions, supported durable prompt admission and
  provider/account/error behavior remain prototype gates. Nix daemon builders
  and separately launched services do not automatically inherit accounting.

## Package table and known transitions (UTC; A–I Nov11, J–P Nov12)

| Package / evidence | Owner | Acceptance | Status / known transition |
| --- | --- | --- | --- |
| EXEC-P0: compatibility/admission/launch probes | implementer1 | Accepted main/M brief; D worktree; finite fake fixtures, supported API path, evidence/checks/commits; no live state | Preparing dispatchNov12 09:08 |
| DESIGN-C: concrete neutral C contract | architect2, architect0 accepts | Existing C public API and main/N/O; own implementation-contracts.md, no source edits | Preparing dispatchNov12 09:08 |
| ARCH-EXEC: release briefs/dependency decisions | architect0 | P0 evidence and DESIGN-C; update design.md sufficient release boundaries, no app edits | Preparing dispatchNov12 09:08 |
| PREP-P1: C seam diagnosis/preparation | implementer0 | Own C worktree; read AGENTS/source/hooks, await concrete design release before app edits | Preparing dispatchNov12 09:08 |
| P: [implementation-plan.md](implementation-plan.md) and design pointer | architect0 | M/N/O accepted; main plan read, review wording corrected, local checks pass | AssignedNov12 08:11; draft08:31; complete/accepted08:36 |
| M: [pi-runtime-plan.md](pi-runtime-plan.md) | architect1 | Runtime package/dependency/permission/unknown-state brief read and accepted | AssignedNov12 08:11; ready/accepted08:19 |
| N: [backend-evolution-boundaries.md](backend-evolution-boundaries.md) | architect2 | Minimal present seams/outcomes/legacy fencing read and accepted; no migration machinery | AssignedNov12 08:11; ready/accepted08:17 |
| O: [backend-integration-map.md](backend-integration-map.md) | implementer0 | Source/public-API/dependency ownership and exact existing check map read and accepted | AssignedNov12 08:11; ready/accepted08:17 |
| J: [authentication-evidence.md](authentication-evidence.md) | implementer5 | Cross-process file locking/cache/OAuth limits read and source spot-checked | AssignedNov12 07:56; ready08:02; accepted08:05 |
| L: [authentication-gateway-evidence.md](authentication-gateway-evidence.md) | architect2 | Gateway vs shared store and Daybreak transport/program limits read | AssignedNov12 07:56; ready/accepted08:05 |
| K: auth reconciliation in `design.md` | architect0 | J/L accepted; shared canonical native Pi store selected by user | AssignedNov12 07:56; ready/accepted08:05 |
| A: initial [design.md](design.md) | architect0 | B/C, architecture, history/recovery and resource limits | Ready22:15:31; accepted22:16; D reconciliation22:20 |
| B: [current-runtime-evidence.md](current-runtime-evidence.md) | implementer0 | Exact source heads, portal/backend seam, provider and receipt contracts | Assigned22:00; ready22:09:33; accepted22:10 |
| C: [pi-capabilities-evidence.md](pi-capabilities-evidence.md) | implementer1 | Immutable official sources; native vs custom capability/auth limits | Assigned22:00; ready22:10; accepted22:11 |
| D: [resource-evidence.md](resource-evidence.md) | implementer0 | Aggregate counts and attributed snapshot, no invented Pi savings | Assigned22:14; ready22:19; accepted22:20 |
| E: revised [design.md](design.md) | architect0 | F/G/H/I and all latest user constraints, no hidden migration/privilege assumption | Assigned22:41; ready/accepted22:53 |
| F: [process-isolation-evidence.md](process-isolation-evidence.md) | architect1 | Supervisor/worker topology, service/Nix accounting, tmp/permission limits | Assigned22:41; ready/accepted22:53 after wording correction |
| G: [coexistence-evidence.md](coexistence-evidence.md) | architect2 | Writable legacy, supported import limits, backend authority/migration lineage | Assigned22:41; ready/accepted22:49 |
| H: [extension-and-question-evidence.md](extension-and-question-evidence.md) | implementer4 | Native dialogs vs host async questions, exact-source trust/update policy | Assigned22:41; ready/accepted22:47 |
| I: [provider-fallback-evidence.md](provider-fallback-evidence.md) | implementer5 | Native virtual routing, retry gate, account auth and member-local effects | Assigned22:43; ready22:48; accepted22:49 |

Times are approximate dispatch/acceptance observations unless a source report
supplies precision; overlapping work is not summed. Each executing member owned
one package. B was accepted and capacity available before D. New members confirmed
first-assignment capacity. Other peers were not assigned duplicate work. Source
research was bounded to6–8 active minutes for follow-ups; synthesis/writing and
procedure reading are not claimed as pure research time.

## Source identity and evidence limits

Accepted source snapshots (not proved installed equivalence):

- dev-workspace `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- codex-web `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`.
- Pi main `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`; observed release v1.5.2
  `b4afdddf44e059c67ccf5097e5317d913521b470` does not certify all main behavior.
- Host configuration read-only context `e91c8d21055b7110182fd4c531389947f180e359`.

The earlier Codex-update session was not opened; source/default evidence does
not establish its reported provider-patch provenance. No peer transcripts,
rosters, credential files or worktrees were read. Aggregate resource inspection
used count/stat/metadata-only methods, documented in D.

D snapshot22:14–22:18:83 dated current tracking directories+343 archived;
4190 stored native threads (2213 unarchived,1977 archived),3667 matching this
workspace's session paths. Loaded/active/member counts unknown. Attributed native
service PSS about7.34GiB; cgroup34.20GiB includes24.05GiB file cache. Rollouts
17.26GiB plus history SQLite5.86GiB logical disk. No numerical Pi savings claim.

## Checks, scope and tracking

Lead read all accepted artifacts and spot-checked the exact portal client seam,
provider contract, Pi setModel/RPC admission, p2 warning, native virtual routing
and existing systemd service spawn. Owned Markdown existence, UTF-8, reference
and whitespace checks passed. No runtime provider, namespace, async-question,
fallback, migration or recovery acceptance ran. All changed files are session
planning/design/findings/evidence; no substantive application deliverable or
maintained product instruction was created, so automatic independent final
change review is not triggered.

Initial tracking commit `5c159a29f`; later updates/findings remain in the session
directory under the short-session checkpoint cadence. No feature registrations,
merge approval or resource claims exist for this assessment. Preserve unrelated
workspace changes; nothing was cleaned or stopped.

## Authentication follow-up (2026-11-12 07:56UTC)

User cannot log in for every worker; one rotating refresh token must have a
coordinated authority. User suggests personal codex-lb with one login and states
Daybreak requires hardware-key login. Check native Pi shared-store refresh first,
then compare broker/gateway without assuming either is required. Exact hardware-
key/Daybreak flow and shared legacy Codex credentials remain unverified. No login,
credential reads, service or model request authorized/performed by this inquiry.

## Detailed-plan scope (2026-11-12 08:11UTC)

User chose shared credentials and requests a detailed plan to add Pi. Later
clarification: migration and Codex removal are future work; code should be cleanly
separated now, without implementing migration. Future preference is full
representable converted conversation unless disproportionate, with original
history retained and omissions disclosed; no converter work is authorized now.

One backend per development session initially. Existing Codex remains fully
workable. New Pi is opt-in. Early pilot can establish conversation/history/stop,
accounting and shared auth while visibly holding uncertain sends and disabling
unproved automatic dispatch. Namespace/tool access gates actual pilot launch;
full durable acceptance/recovery gates team/automatic delivery, not independent
seam/UI preparation. Specific Daybreak availability does not block ordinary
verified Pi providers. No automatic new-session default switch or Codex removal.

Dispatch08:09 was refused before acceptance by a transient dev-session lock;
read-only lock/roster inspection and stable-ID retry08:11 succeeded for all four
packages. No application edits were taken over and no session state repaired.

## Detailed-plan input acceptance (2026-11-12 08:19UTC)

M/N/O are complete and accepted. Main-plan owner has sufficient inputs and is
finishing synthesis; no additional investigation/subsystems requested. Source
file/test map preserves public codex-web clients and the one-way dependency.
Generic projections/history reads are separated from native execution and
recovery. Future migration/removal is recorded only as code-boundary criteria.
No implementation assignments or checks have been launched.

## Detailed plan accepted (2026-11-12 08:36UTC)

The main plan is the single proposed package/owner/dependency table. Supporting
M/N/O tables supply evidence, not additional assignments. Preserves existing
writable Codex and unchanged default; new Pi sessions are opt-in, one backend
per development session. Early manual pilot, automation and launch gates are
separate. Stable receipt IDs survive worker restarts; runtime generation is
only execution proof. Auth is shared, history/settings private. No converter,
import pipeline, cutover, archive conversion, retirement automation, broker,
repository rename or generic agent server is included.

Lead read the full main plan and all supporting briefs. Accepted a narrow final-
review wording correction: completed intermediate packages alone do not trigger
review; final review follows all intended committed deliverable changes and
quick checks, before long integration. No review is invoked for current planning.
Main/brief/design UTF-8, final newline, whitespace and relative links pass.
No runtime tests/builds/CI were run. Exact commands are future checks in the plan.

## Implementation authorization and first handoff

User's exact instruction: "proceed", following the accepted detailed plan in
this conversation. Authority covers initial implementation, appropriate checks,
feature commits/publication and review preparation. No repository/target merge
or deployment approval is present. No machine/repository merge claims acquired.

This checkpoint records a genuine phase/ownership handoff from planning into
implementation before any project-code commit or external mutation. It is the
first consolidated tracking checkpoint on Nov12; preserve unrelated workspace
index/worktree contents and stage only this session's Markdown/manifest.

## Next

Dispatch complete P0 and bounded C-contract/preparation packages. Run known quick
checks inline; use fresh monitor utilities for long/uncertain builds/checks per
the monitor skill. Final mandatory review begins after all intended substantive
changes are committed and quick checks pass, before long integration tests.
Release independent packages on sufficient relevant briefs, not unrelated gates.
Session remains open; no archive, stop, cleanup or lifecycle action is authorized.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
