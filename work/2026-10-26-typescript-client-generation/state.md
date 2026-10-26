---
lifecycle: active
---

# 2026-10-26-typescript-client-generation

## Status

- Phase: implementation preparation. User authorized implementation; architect refreshing concrete brief, lead preparing initial tracking commit and owned worktrees. No application edits yet.
- Follow-up alignment: keep the other session's WebUI HaveAPI 0.30.2 adoption and build generated types/operations above it. User reports new GitHub repository `vpsfreecz/vpsadmin-typescript-client`; not cloned or implemented here.

## Phase checklist

- [x] Verify exact session identity and retained roster/access.
- [x] Scope investigation and delegate substantive comparison to architect0.
- [x] Gather source evidence and assess WebUI/generator compatibility.
- [x] Accept findings and provide suggestions.
- [ ] Accept concrete implementation brief and assign independent packages.
- [ ] Implement generator, schema export/fixture and generated package with quick checks/hooks.
- [ ] Commit complete deliverables; independent final review/history/migration gate.
- [ ] Bounded postreview verification and publish feature branches; inspect CI.
- [ ] WebUI integration pilot after upgrade baseline integrates.
- Default-branch integration, registry releases and deployment require separate direction.

## Next actions

- Architect finalizes executable contracts; lead creates owned worktrees and assigns implementation. Start generator/schema/package work independently of unfinished upgrade.
- Use the upgraded WebUI adapter/runtime baseline, rather than the old custom transport inspected during initial investigation. Keep WebUI edits separate from the upgrade session's ongoing ownership; preferably wait for accepted upgrade to reach main.

## Documentation

- `plan.md`: scope, owners, acceptance and constraints.
- `design.md`: accepted architect-owned investigation/proposal, exact source revisions, implementation boundaries, caveats and verification brief.
- No project documentation changes are needed for an investigation-only request.

## Repositories

- Local canonical bare refs only: HaveAPI, WebUI, vpsAdmin and generated Go/Rust clients.
- No session worktrees or feature branches registered.
- Inspected cached upstream defaults (not fresh remote/deployment proof):
  - HaveAPI: `ec84ec874eb209ab59848873998456293ddf3c52`.
  - vpsadmin-webui: `5a2d2bdc3ad7a827038f877d75959916528db844`.
  - vpsadmin: `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`.
  - vpsadmin-go-client: `1d9240f3d27b5831baf3694baab5fe06294875d8`.
  - vpsadmin-rust-client: `ff876abe17e3301da62c1b6afbda055ec89db9d2`.

## Commands run

- `dev-session current`: exact bound slug, environment slug and workspace agree.
- `dev-session team list 2026-10-26-typescript-client-generation --as-is`: retained architect and implementers ready with workspace-write access.
- Assigned architect0 via native team assignment.

## Results

- Investigation in progress; no tests needed or run for read-only source comparison.
- User selected one API version deployed with WebUI as the recommendation's priority.
- Preliminary evidence accepted: HaveAPI's TypeScript-authored async runtime already attaches dynamic resource/action properties; generic declarations cannot know concrete endpoint names. Checked `clients/js/src/haveapi/async/{client,resource_model}.ts` and source-derived documentation schema precedent at `servers/ruby/lib/haveapi/documentation_clients.rb` against cached origin/master.
- Compared refs are explicit cached origin defaults, not differing bare local HEADs; no upstream freshness or deployed-state claim is made.
- implementer0 completed Go/Rust comparison: Rust's saved versioned snapshot, provenance, deterministic generation/ownership/check-mode and collision diagnostics are useful precedents; Go's live default-version capture and loose response types should not be copied.
- implementer1 completed WebUI/backend comparison: WebUI already uses a handwritten TS transport (`src/lib/api/haveapi.ts`) and domain wrappers, with metadata/envelopes, permission OPTIONS checks, cancellation and uncertain-write handling. Prefer generated methods with injectable transport, preserving these guarantees. Full schema export needs controlled plugins and DB-dependent schema inputs.
- Lead inspected `src/lib/api/haveapi.ts` and `src/lib/api/networks.ts` at the cached WebUI revision to accept migration boundary and preserved semantics, and HaveAPI `parameters/typed.rb` / `authorization.rb` to confirm output nullability/filtering limitations.
- No project docs edited: these are proposals and investigation evidence, not changed supported behavior. No independent final review triggered.
- Lead read and accepted final `design.md`. Recommendation is a version-pinned generated facade/package with injected executor, offline deterministic schema provenance and incremental WebUI adoption. Investigation is complete; implementation remains a future user-directed activity.
- Stable handoff: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/>.
- Follow-up read-only coordination evidence: upgrade session plan, current state and design Package C/C3 record npm `haveapi-client` 0.30.2 adoption with `AsyncClient` owning wire transport/serialization/decoding and WebUI retaining OAuth/session/domain policy. Recorded WebUI final head is `f10d3d48c4f21cc39187c3667ffffd9952404c11`; state reports reviewed/checked but not merged, with broader verification/publication still pending. This is recorded evidence, not fresh Git/remote verification. No other session's records, refs or worktrees changed.

## Open questions

- Follow-up implementation must prove reproducible complete schema export with intended plugin/data fixture inputs; source inspection establishes feasibility, not a verified exporter.
- Choose exact facade naming and runtime adapter contract; syntax shown in the recommendation is illustrative.
- Define JavaScript safe-integer handling, custom parameter representation and output narrowing before claiming sound response types.

## Cleanup

- None. Session remains open; no lifecycle action is authorized.
