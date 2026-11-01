---
lifecycle: active
---

# 2026-11-01-api-doc-language-settings

## Status

- Phase: implementation preparation. User explicitly requested implementation;
  exact Settings labels are now English / Česky.
- Identity verified with `dev-session current`; environment and thread binding
  both match this session and workspace.
- Same-session retained roster inspected. Architect `architect0` owns investigation
  and design, with saved workspace-write access; lead owns scoping and acceptance.
- User added linked internal protocol documentation to the proposal scope;
  forwarded to architect for source/layout and navigation design.

## Phase checklist

- [x] Scope and same-session ownership verified.
- [x] Existing renderer/settings behavior established; proposal recorded.
- [x] Revised design accepted and user-facing recommendation prepared.
- [ ] Runtime/UI localization and regression coverage.
- [ ] English/Czech articles, source-layout migration and packaging.
- [ ] Final user-facing writing pass; intended changes committed; quick checks pass.
- [ ] Independent final review with whole-branch history/migration conclusions.
- [ ] Broader checks, feature publication and CI.
- Deployment and default-branch integration: not requested.

## Next actions

- Commit initial plan/state, create the HaveAPI feature worktree, and release the
  architect-confirmed execution packages to retained workspace-write implementers.

## Documentation

- [Plan](plan.md); accepted architect-owned proposal in [design.md](design.md).
- [Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-api-doc-language-settings/).

## Repositories

- HaveAPI canonical bare clone: `repos/haveapi.git`; read-only investigation.
- No feature branch/worktree is registered or required for this proposal.

## Commands run

- `dev-session current`
- `dev-session team list 2026-11-01-api-doc-language-settings --as-is`
- Design-only assignment to retained `architect0` via `dev-session team assign`.

## Results

- Architect verified that `refs/remotes/origin/master` is `391b0190241cf195a69b06f7297d3e4eebec5a83`.
  The bare local `master` (`7835acafdda19779815a0f1ba905d78e0085456d`)
  predates the current documentation UI, so the proposal uses the remote-tracking
  baseline without fetching or creating a worktree.
- Current documentation already has unified preferences, multi-page navigation,
  search and OAuth controls; existing framework and parameter localization can
  be reused.
- Recommendation: server-rendered documentation locale, Settings
  English/Čeština before Theme, cookie/query preference then weighted
  browser language then English; reload retains current page and fragment.
- User removed the visible Automatic option and authorized moving English article
  sources to `doc/en/` alongside `doc/cs/`. Browser detection remains the initial
  behavior without a saved choice. Architect's revision was inspected and accepted;
  source lookup, copying, packaging and repository links move together, while
  public URLs and fragment IDs stay stable.
- Existing example-language preference continues to mean programming language.
  API request/client settings remain independent; generated code stays unchanged.
- Linked internal docs gain Czech article sources with English fallback, stable
  anchors and shared locale navigation. Copying/gem packaging needs to include
  locale directories; machine-readable schema representation is unchanged.
- Lead inspected the design and confirmed current Settings placement,
  documentation-copy behavior and packaging glob against the inspected baseline.
  Architect verified 15 pinned source anchors. This is source inspection, not
  runtime/browser verification. No tests/builds were run or needed for planning.
- No application changes or completed product-documentation deliverable; this
  planning/investigation record does not trigger mandatory final change review.

## Open questions

- No blocking design questions. Application-authored descriptions require their
  owners to supply translations through existing hooks; plain text falls back
  to the supplied original. Full details and future checks are in the proposal.

## Cleanup

- No resources acquired or lifecycle changes requested. Leave the session open.
