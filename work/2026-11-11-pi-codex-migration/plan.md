# 2026-11-11-pi-codex-migration

## Goal

I'd like you to evaluate if we could replace codex in the dev-workspace portal and cli with pi https://github.com/earendil-works/pi and how difficult it would be.

updating codex can be difficult and now we have to be patching it, see session 2026-11-08-codex-version-update.

I understand that the pi harness is more bare... I sometimes use the planning mode (and the portal supports it). I'm looking for a replacement that could increase the speed of development of the dev-workspace portal. I'd be willing to forgo the ability to work with sessions both from web and CLI... as long as the web works, I don't use CLI. otoh perhaps pi would support it as well. What I definitely need is the ability to use different providers for sessions as we do here. I also like the automated teams, not sure how that would translate -- perhaps we'd need to create our own communication channel?

Investigate and give me your opinion / suggest a solution.

## Affected repositories

Read-only assessment of `dev-workspace`, `codex-web`, their packaged Codex
patches, and official `earendil-works/pi` sources. No application changes,
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

## Testing plan

Source/document inspection with immutable revision and file pointers. Reconcile
contradictions and distinguish documented API support from runtime validation.
No integration tests or benchmarks; propose bounded proof-of-concept acceptance
checks for a future decision.
