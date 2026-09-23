# Final direct-team integration review

## Outcome and bounds

Review the complete committed direct-thread team feature and final portal
cleanup before integration. The user wants persistent independent Codex member
threads, compact stable addresses, portal and CLI controls, direct member chat,
and fresh Luna/low utilities for long verification. The last UI request removes
the redundant Team-tab Assign work form and aligns the Codex-tab Member control.
The index-page `aitherdev` label is configured through `hostLabel`; no code
change is required. The user approved default-branch integration after final
fixes and a consolidated review.

This is the sole forward-only aitherdev development host. It is trusted at the
local operator boundary; remote portal clients remain untrusted. Do not ask for
rollback support for old virtual teams or for a new message bus. Keep the
assignment API/CLI and member reporting path. Do not mutate unrelated sessions,
clusters, KB staging, or configuration master. The dirty shared workspace
checkout belongs mostly to other sessions; its audit is tracked separately.

## Revisions and ownership

| Project | Base | Reviewed head |
| --- | --- | --- |
| codex-web | `0a75d720171c52719679c7dd2e356d50f4b81f16` | `d542e767310d9d7b32460691a54829371b88e3b2` |
| generic dev-workspace | `b52a2363be8bb9985e4b9f254fb43e8cade4551d` | `2f3c8b80a52ee932b21236df07e7fca164402439` |
| vpsFree extension | `298a8a42282f193c82a24e87a95300548a4d5903` | `1cea22427b809f5774631abc8f40400337e7b688` |
| workspace feature | local `master` `3132359b310287db2455e1ba74043dce9fff5c36` | `361925dd52ddbf791550dd921c6b836d74ba2304` |

The workspace remote master is currently `4bdc90b6601383ecee13fef4931227f09da89fda`;
the shared local master contains 28 additional coordination commits. The
workspace feature was rebased onto that local master. The generic runtime owns
team lifecycle, portal and CLI; codex-web owns capability-checked App Server
transport; the vpsFree extension and workspace compose and pin those providers.
The consumer chain is codex-web → generic runtime → extension → workspace.
The extension and workspace retain successive pin commits because each head
was an independently deployed or verified checkpoint on this development host;
review whether this provenance justifies their separate commits.

The complete series and prior review findings are recorded in `state.md`,
`review-transport-packet.md`, `review-portal-feedback-packet.md`, and their
results. Current feature documentation: generic
`docs/workspace-portal.md`, `docs/dev-sessions.md`, and README; workspace
`work/2026-09-21-agent-teams-workflow/plan.md`. Site-specific rollout evidence
stays in `state.md` and linked logs. The final portal cleanup alters no public
API, CLI, roster or ledger schema, session on-disk format, generated NixOS
option, or vpsAdmin contract. The earlier direct-thread cutover's deliberate
incompatibility and operator action are in the plan and generic portal guide.

## Checks and review scope

Quick checks after the final UI commit: focused generic web Go tests passed
with Go and GCC in the Nix shell; Node syntax passed; extension and workspace
`nix flake check --no-build` passed; all changed diffs passed `git diff --check`.
Earlier final-head codex-web checks and live member-report checks are in
`state.md`. Long packaged checks and the new aitherdev switch have not run on
these final heads and must follow this review.

Risk: High for the complete feature because it manages persistent member
threads, authorization, retries, and package transitions. Review at Sol/xhigh
in General, Architecture, Scope, and Risk lanes. Inspect the full commit
series, not only the final UI diff. Pay particular attention to same-session
address resolution, headless thread recovery, uncertain delivery, source
generation checks, and whether browser removal leaves the API/CLI intact.
