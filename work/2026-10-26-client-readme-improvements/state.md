---
lifecycle: active
---

# 2026-10-26-client-readme-improvements

## Status

Implementation authorized by user “proceed”. Preparing worktree and parallel documentation packages. HaveAPI master integration is not authorized.

## Phase checklist

- [x] Verify thread-bound session identity and retained roster.
- [x] Scope advisory HaveAPI README investigation.
- [x] Receive architect findings and [design](design.md).
- [x] Inspect acceptance evidence.
- [x] Prepare recommendations for user response.
- [ ] README implementation, quick checks and final independent review (future work, outside current advisory pass).

## Ownership and next actions

- `architect0` (retained design member, ready, workspace_write): source-backed client interface/README investigation and design.md.
- Lead: assess findings, prepare concise concrete recommendations and maintain records.
- Implementers and reviewer remain unassigned because this pass changes no project deliverables.

## Repositories

`haveapi` canonical objects are inspected read-only. No feature branches, owned worktrees or repository registrations created.

## Evidence

- `dev-session current` matched exact trusted slug and both environment identity markers.
- `dev-session team list 2026-10-26-client-readme-improvements --as-is` verified retained roster/settings/access.
- Architect assignment queued successfully through `dev-session team assign --message-stdin`.
- Shared workspace has extensive unrelated changes; preserve them and touch only this session’s records.

## Checks, blockers and risks

No tests/builds/deployments run. No blocker currently. Architect preliminary evidence uses cached origin/master `39e98020070fabcceca32f8fabcf0440f0d8763e` (2026-10-25); bare HEAD is older and lacks Rust. Both callback and async JS interfaces also support TypeScript through library declarations; there is no API-generated TypeScript client. The async resource/action API exists and can replace the raw-request introduction. Lead acceptance inspection confirmed all four current READMEs and async source (`async/client.ts` discovery/default handling and `{value,response}` receipts; `async/resource_model.ts` resource/action lookup). Python README leads with `.call()` and then extensive wire encoding rules; Rust puts development commands before generation and has no complete consuming application example. Both generated-client links resolve publicly according to architect. Candidate examples are source-checked, not executed.

## Cleanup

Session remains open. No lifecycle or cleanup action authorized.

## Accepted proposal

- JS/TS: two client interfaces (`CallbackClient`, `AsyncClient`), both usable from JS and TS; `Client` is the callback alias. Provide four clear examples, base URL/default discovery, resource/action calls, real result shapes and idiomatic errors. Explain dynamic endpoint typing accurately; move raw HTTP and routing/build internals behind reference links.
- Python: paired sync/async context-managed quickstarts with shorthand resource calls; practical authentication, results, errors, pagination and operations; relocate detailed encoding/ownership contracts to linked reference docs. Replace stale release-status wording with normal package installation after public registry check; user states Python is already published.
- Rust: generator/install/generate/consume flow, complete async and optional blocking usage, separate maintainer setup. Preserve explicit schema-version requirement.
- Go/Rust: add verified generated-client project links. No runtime changes proposed.

## User correction

The user states the Python client should already be published and the release-status text must be fixed. `implementer0` verified public https://pypi.org/pypi/haveapi-client/json: current version `0.30.2`, Python `>=3.11`, non-yanked wheel and source archive uploaded 2026-10-25. README recommendations must remove the stale disclaimer and directly show `uv add haveapi-client` / `python3 -m pip install haveapi-client`. No publishing action required.

## Handoff

Detailed source-backed proposal and four JS/TS examples: [design.md](design.md). Python publication correction above supersedes the design’s pending-registry-check caveat. No project implementation, quick test execution, independent final deliverable review or deployment performed. No feature branches created; no cleanup required. Session stays active and open for follow-up.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-client-readme-improvements/

## Implementation phase checklist

- [x] User accepted proposal; source-backed design exists.
- [ ] Initial substantive tracking commit and prepared HaveAPI worktree/hooks.
- [ ] JS/TS, Python, Rust/Go documentation packages implemented.
- [ ] Lead prose/acceptance pass and quick checks.
- [ ] All intended changes committed; complete history inventoried.
- [ ] Independent final review and finding reconciliation.
- [ ] Feature branch published; CI disposition recorded.
- [ ] Integration (requires separate user approval).
