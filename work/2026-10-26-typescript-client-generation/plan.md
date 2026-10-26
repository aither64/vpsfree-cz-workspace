# 2026-10-26-typescript-client-generation

## Goal

I wonder about haveapi typescript client. As it is, apparently the user of this client must use findResource and findAction, unlike the javascript client, where the client auto-generates properties for resources and actions. Would it be better if we'd support generating typescript client against concrete API versions, like the client generators for go and rust do it? We'd then have vpsadmin-typescript-client. Would it be more developer-friendly and safe? Intend use of this client is in vpsadmin-webui. Please investigate and make suggestions.

## Affected repositories

- `haveapi`: TypeScript/JavaScript runtimes, Go/Rust generators and schema contracts.
- `vpsadmin-webui`: intended consumer and current API integration.
- `vpsadmin`, `vpsadmin-go-client`, `vpsadmin-rust-client`: API metadata, versioning and generated-client release examples.
- `vpsadmin-typescript-client`: user reports creating `vpsfreecz/vpsadmin-typescript-client`; generated package design remains proposed, with no clone or implementation started.

## Approach

Implementation authorized by the user after investigation. Implement the HaveAPI TypeScript generator, explicit reproducible schema input/export and the generated package in `vpsfreecz/vpsadmin-typescript-client`. Use this session's dedicated worktrees and published feature branches. Defer WebUI source edits until the user's integration of the HaveAPI 0.30.2 adoption; no integration, package releases, production API calls or deployment authorized here.

| Owner | Expected result / acceptance | Dependencies / checks |
| --- | --- | --- |
| architect0 | Refresh `design.md` to concrete implementation contract, boundaries and verification brief | Existing accepted comparison; refresh selected component instructions and baselines |
| implementer0–3 | Complete execution packages assigned after design acceptance: generator, schema export/fixture, package/tooling/docs | Saved workspace-write access verified; independent file boundaries; serialize Git in each repo |
| reviewer0 | Mandatory independent final whole-deliverable/history/migration review | Complete committed deliverables and passing quick checks, before long tests |
| Lead | Prepare tracking/worktrees, assign work, assess results, coordinate review/checks and dependency handoff | Defer WebUI edits; no integration approval supplied |

## Decisions

- User now authorizes implementation. Default-branch integration and package releases remain separately approval-bound.
- Investigation findings and plans remain evidence; substantive source/docs/config deliverables require mandatory final review after commit and quick checks.
- User preference: prioritize one API version deployed alongside WebUI. Arbitrary independently upgraded servers are not the primary target.
- Recommended direction: concrete generated async client methods/types with injectable transport; publish version-pinned `vpsadmin-typescript-client` generated offline from an explicit reproducible API snapshot. Preserve generic HaveAPI for dynamic consumers and WebUI's current transport/domain policy.
- Stage adoption with one collection read and one write, then expand after validating compile-time contracts, optional/null semantics, metadata, cancellation, capabilities and uncertain-write behavior.
- Retain WebUI's HaveAPI 0.30.2 adoption owned by `2026-10-24-vpsadmin-haveapi-upgrade`. That replaces custom wire transport with the real npm AsyncClient; our generated facade will layer over the upgraded adapter. Earlier source evidence described cached main before adoption. Do not restore its old transport or modify the upgrade session's owned work.
- Future generator/schema work can proceed independently; WebUI integration should use the accepted upgraded baseline, preferably after it reaches main. Exact baseline and published runtime compatibility must be rechecked at implementation start.

## Compatibility and deployment

Assess API-version selection, schema provenance, permission-filtered metadata, mixed client/server versions, nullable/optional fields, action availability, browser authentication and transport, packaging, and rollback. No deployment is planned.

## Documentation

Readers: the user and future implementers. Preserve the comparison and proposed design in this session's `design.md`; keep status and source revisions in `state.md` and supporting findings. No established project behavior changes, so no repository documentation edits are needed.

## Testing plan

Run meaningful generator, type-negative and executor contract checks; prove deterministic generation with explicit input/version/provenance and fail-closed unsupported schema/collision handling. Verify exporter fixtures against controlled loaded schemas and preserve omission/null/metadata/auth boundaries. Require normal hooks and local component checks before final review. Run bounded longer integration/build checks only after independent final review, using a fresh policy watcher. WebUI browser validation waits for the upgraded baseline; no production mutation.
