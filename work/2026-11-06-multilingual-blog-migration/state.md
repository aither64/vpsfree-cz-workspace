---
lifecycle: active
---

# 2026-11-06-multilingual-blog-migration

## Status

- Phase: planning delivered; Hugo recommendation and implementation design are
  complete. Implementation, container extraction and production changes remain
  future work, outside the current planning request.
- Identity verified by `dev-session current` and matching environment:
  `2026-11-06-multilingual-blog-migration`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- User settled shared CS/EN discussions, Git/Markdown authoring, AI drafts with
  human review and historical comments in their original language.
- Later clarification: agent-first/human-friendly authoring instructions/skills,
  easy previews, dedicated content Git repository and same-VPS deployment.
- User permits bot updates and then confirmed `/feed/` should be preserved for
  other subscribers. Stable feed identity and no archive re-announcements are
  acceptance concerns; optional English feed stays separate.
- User confirmed retaining existing Discourse account and signup rules; no
  expansion of registration or anonymous posting is required.

## Phase checklist

- [x] Verify session, retained team/access and scope.
- [x] Clarify publishing, discussion and translation preferences.
- [x] Complete bounded investigation and migration design.
- [x] Deliver generator recommendation and implementation plan.
- [ ] Implementation and quick checks (future work).
- [ ] Independent final review and integration tests (future work).
- [ ] Approved integration/deployment and usability verification (future work).

## Packages

| Package / deliverable | Owner | Dependencies / acceptance | Status / evidence |
| --- | --- | --- | --- |
| D: generator, preservation, bilingual/Discourse architecture; `design.md` | architect0, retained Astra/xhigh, workspace_write | Bounded primary docs/public samples; actionable packages, acceptance, cutover/recovery, explicit unknowns | Assigned ~20:37 UTC; research complete ~20:43 UTC; reported/accepted ~20:50 UTC; seven successful primary references + homepage/article/CSS sample; [design](design.md) |
| C: canonical configuration discovery; `configuration-findings.md` | implementer0, retained Sol/xhigh, workspace_write | Read-only canonical config, max ~6 files; exact refs/paths and runtime uncertainties; no mutations | Assigned ~20:37 UTC; reported/accepted ~20:40 UTC; capacity free; [evidence](configuration-findings.md) |

Other retained implementers and reviewer are unassigned: this is a plan, and
additional execution packages would add unnecessary work. Assignment times are
approximate; exact starts are not known. No overlapping edit or Git windows.

## Next actions

- Begin package A (source inventory) once implementation is requested and blog
  container access is available. Agree repository destination, `/en/` convention,
  forum category and translation-review ownership before dependent steps.
- Use the design's future package A–E boundaries; none is currently executing.
  Existing account policy, feed continuity and all other asked preferences are
  settled. Runtime/data inventory remain the material evidence gaps.

## Documentation

- [Plan](plan.md), [design](design.md) and
  [configuration findings](configuration-findings.md) are complete planning records.
- Stable session URL:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/

## Repositories

- No feature branches or worktrees created; configuration is read-only.
- Shared workspace remains on `master`; unrelated dirty files/index are preserved.
- Configuration findings inspect retained `origin/master`
  `85b38f1cd07d6b3a0fde3eefd32258f747e757e5`, not a fresh remote/runtime head.

## Commands run

- `dev-session current`, environment identity check, retained same-session
  `team list --as-is`, and bounded assignments to architect0/implementer0.
- Read applicable workspace guidance and documentation/handoff skills.
- Opened official Discourse embedding and Hugo multilingual docs to confirm
  native support; actual installed forum settings still need runtime validation.

## Results

- Discourse official docs support explicit `topicId` embedding and replying on
  the forum. Both translations can use the same ID without automatic topics.
- Hugo supports translation pairing and per-language explicit URLs.
- Existing configuration supports same-backend static deployment without an
  expected public proxy change; WordPress-specific health checks need replacement.
  IRC bot consumes `/feed/`. See configuration findings for exact paths/limits.
- Workspace `git fetch origin` completed; local master is ahead of origin/master
  with no remote-only commits. No project fetch or push performed.
- Initial architect assignment hit transient concurrent session mutation;
  exact retry with the same message ID succeeded. No bypass or roster changes.
- Mandatory-change-review procedure checked: routine planning, investigation,
  design reconciliation and evidence do not trigger automatic review. No code,
  configuration, final authoring skill or operating procedure was implemented
  in this request; no independent final implementation review is claimed.
- Lead accepted architect0's five future packages, dependency boundaries,
  preservation/translation acceptance and same-container rollback approach.
  Source inventory and deployed-version checks remain explicit gates.
- Planning records passed formatting, local-link and active-state checks. No
  application build, content-completeness check, runtime test or deployment was
  run. Workspace declares no commit-hook framework; ordinary hooks are preserved.

## Open questions

- Container access, authoritative content/media inventory and installed runtime
  versions/settings are unavailable yet.
- Proposed `/en/` placement, blog repository destination, Discourse category and
  person responsible for translation review remain to confirm as needed.

## Cleanup

- No services, machine reservations, merge claims or remote changes.
- Session remains open; no lifecycle cleanup is requested or authorized.
