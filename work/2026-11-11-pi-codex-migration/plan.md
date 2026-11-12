# 2026-11-11-pi-codex-migration

## Implementation authorized (2026-11-12)

The user instructed "proceed" after accepting the detailed plan. Execute initial
Pi addition and evaluation alongside writable Codex. Migration/conversion,
Codex retirement and default switching stay deferred. Merge and deployment
remain separately approved actions; neither is authorized by this instruction.
Start P0 plus the neutral-seam prerequisites in registered feature worktrees.

## Current deliverable (2026-11-12)

Prepare a detailed implementation plan for adding Pi as an opt-in backend in the
existing portal alongside fully usable Codex. Shared canonical native Pi
credentials are selected. Preserve standalone development-session process trees,
provider/member settings and existing portal workflows through bounded phases.

Migration/conversion and Codex removal are future work. Design current code
boundaries to permit them; do not implement or plan a converter/cutover/retirement
subsystem as part of initial integration. The future preference is full history
where representable unless too complex, with original history and disclosures.
User clarified that Pi should first be integrated and evaluated in practice.

Delivered main plan: [implementation-plan.md](implementation-plan.md), supported
by [runtime packages](pi-runtime-plan.md), [separation boundaries](backend-evolution-boundaries.md)
and [source/check map](backend-integration-map.md). Accepted2026-11-12 08:36UTC.
This request does not start implementation, login, testing, deployment or integration.

## Goal

I'd like you to evaluate if we could replace codex in the dev-workspace portal and cli with pi https://github.com/earendil-works/pi and how difficult it would be.

updating codex can be difficult and now we have to be patching it, see session 2026-11-08-codex-version-update.

I understand that the pi harness is more bare... I sometimes use the planning mode (and the portal supports it). I'm looking for a replacement that could increase the speed of development of the dev-workspace portal. I'd be willing to forgo the ability to work with sessions both from web and CLI... as long as the web works, I don't use CLI. otoh perhaps pi would support it as well. What I definitely need is the ability to use different providers for sessions as we do here. I also like the automated teams, not sure how that would translate -- perhaps we'd need to create our own communication channel?

Investigate and give me your opinion / suggest a solution.

## Affected repositories

Read-only assessment of `dev-workspace`, `codex-web`, their packaged Codex
patches, official `earendil-works/pi` sources, and read-only aitherdev host
configuration for process/namespace feasibility. No application changes,
paid model calls, integration, deployment or session lifecycle actions.

## Approach

Compare the actual current integration with pi SDK/RPC capabilities. Determine
which portal and team responsibilities can remain, which need adapters, and
which require new behavior. Prioritize reliable web sessions and multiple
providers; assess planning and automated teams explicitly. Give a recommendation,
phased alternative and uncertain effort ranges rather than promise parity.

Bound first-pass packages to 12–15 active research minutes. Reassess gaps before
expanding. Architect owns synthesis/design; implementers own independent source
evidence. Lead owns acceptance, user communication and session records.

## User clarification (2026-11-11, ongoing conversation)

The user is happy with the portal's current workings. The motivation is the
provider-switching dependency on modified Codex. Evaluate preservation of current
portal behavior: explicitly identify unchanged UX, internal runtime adapters,
and unavoidable or optional visible changes. No portal redesign is requested.

## User addition: resources

Compare aggregate open/archived session and Codex thread counts with observed
current runtime process/memory use. Distinguish stored, loaded, active and
archived state. Preserve peer-session confidentiality: aggregate inventory only,
no other session transcripts/records/rosters/worktrees. Do not invent measured Pi
performance. Evaluate lazy loading/eviction and shared SDK host versus one RPC
process per loaded conversation. This is an additional investigation milestone.

## Follow-up constraints (22:39–22:43 UTC)

- User requires a standalone process tree per development session. Explicit
  answer: "One session cgroup/namespace, with team worker processes inside".
  This supersedes the earlier shared-across-development-sessions SDK proposal.
- Keep current portal capabilities; do not recreate the Codex protocol.
- Extensions may be reused only with credible maintenance, pinned source and
  code/dependency verification; package popularity is not sufficient evidence.
- Compare side-by-side backends versus direct replacement while preserving
  writable existing sessions. Existing Codex isolation is not retroactively solved.
- Preserve optional nonblocking questions: post choices/free text, keep working,
  receive a correctly bound durable answer later; native blocking dialog is not
  equivalent.
- User requests individual member provider overrides and fallbacks, e.g. from
  Snajpa codex-lb to subscription-only Daybreak on a relevant error. Exact account
  access is unverified. Distinguish inherited session defaults/member overrides,
  mapped provider/model fallbacks and safe error/delivery handling.

## Authentication follow-up (2026-11-12)

User asks how one OpenAI subscription login can serve standalone workers without
refresh-token conflicts, and whether a personal codex-lb gateway would be better.
Daybreak requires hardware-key login. Assess one canonical locked Pi store versus
a broker/inference proxy, cross-process rotation and legacy Codex coexistence.
Do not read credentials or attempt login/model calls; distinguish supported OAuth
mechanisms from unverified Daybreak/client/scopes requirements.

## Decisions

Investigation only. Existing Full-team settings retained; no reviewer assignment
for findings/planning alone. Other sessions' private records, transcripts and
worktrees are outside scope; derive Codex upgrade costs from current source and
public repository history instead.

## Compatibility and deployment

Assess transcript/state retention, provider/model/auth differences, tool policy,
team identity and message durability, plan-mode enforcement and restart recovery.
Any eventual implementation should preserve Codex sessions and use an opt-in pi
backend for new sessions before considering migration or removal. No deployment
is authorized by this assessment.

## Documentation

Readers: workspace owner and future migration implementers. Findings remain in
this session: `design.md`, `current-runtime-evidence.md`, and
`pi-capabilities-evidence.md`. No maintained product documentation is changed.

## Outcome

Recommend side-by-side backends: keep existing sessions fully writable on Codex
while new Pi sessions use the existing portal. A narrow backend capability
contract avoids Codex wire emulation. Each Pi development session gets one
supervisor/cgroup/mount namespace with separate loaded lead/member workers and
tool/service children; initial shared-across-sessions SDK ideas are superseded.
Legacy shared Codex is a disclosed transition limitation, not an approved action
or automatic native migration.

Reuse supported native Pi operations and reviewed first-party host extensions;
no external extension is selected. Preserve optional asynchronous questions and
add per-member provider override/finite fallback policy, using native virtual
routing where its retry semantics fit. Exact error classification, subscription
Daybreak access, durable admission and namespace/tool permissions require later
runtime acceptance. Retain original Codex evidence and recovery; a Pi context
continuation is not native execution import. See [design.md](design.md) and its
linked evidence for source-supported contracts and open decisions.

## Testing plan

Source/document inspection with immutable revision and file pointers. Reconcile
contradictions and distinguish documented API support from runtime validation.
No integration tests or benchmarks; propose bounded proof-of-concept acceptance
checks for a future decision.
