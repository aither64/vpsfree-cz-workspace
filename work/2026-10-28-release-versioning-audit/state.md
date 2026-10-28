---
lifecycle: active
---

# HaveAPI release versioning investigation

## Current phase

Implementation authorized by user: "implement it". Accepted policy: master
0.31.0, release branch 0.31.N. Preparing initial tracking commit and assigning
one implementation package. Integration/publication remain unapproved.

## Phase checklist

- [x] Verify exact session identity and inspect retained Full-team roster.
- [x] Establish HaveAPI-only scope and assign architect investigation.
- [x] Establish fresh master/release ancestry and version-file evidence.
- [x] Explain release-process gap and assess proposed correction.
- [x] Preserve findings and deliver initial recommendation.
- [x] Reconcile architect brief with user-selected major/minor policy.
- [ ] Implement metadata catch-up, guards, fixtures and release documentation.
- [ ] Pass quick checks and hooks; commit intended changes.
- [ ] Complete independent final review of full history/diff and migration inventory.
- [ ] Complete relevant longer checks and feature-branch CI.
- [ ] Publish verified branch; await explicit HaveAPI/master integration approval.
- Deployment and new package publication: outside this request.

## Owners and next result

- `architect0` (retained Astra/xhigh, workspace_write, ready): release tooling,
  Git history, publication evidence and `design.md` proposal. Owns serialized
  HaveAPI fetch operations. Acceptance: exact heads, proven failure mechanism,
  historical uncertainty and smallest bounded correction with checks.
- Lead: records, acceptance inspection and final recommendation.
- `implementer0`: complete accepted execution package, workspace_write verified.
- `reviewer0`: independent final review when eligible, retained Sol/xhigh.
- `implementer1`: idle; no independent file boundary warrants a second owner.

## Repositories and operations

- Canonical HaveAPI clone: `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git`.
- No project branch/worktree created or registered.
- Session and environment match `2026-10-28-release-versioning-audit` and
  `/home/aither/workspace/ai/vpsfree.cz`.
- Read required session/project/Git/lifecycle/documentation/verification/team
  procedures and documentation/handoff skills; repository release instructions
  are being examined by architect.

## Risks and constraints

Published artifacts and tags must remain unchanged. Release commands may mutate
or publish; inspect source only. Historical operator intent may not be provable.
Shared workspace contains extensive unrelated changes; preserve them and stage
only this session's files if a tracking commit becomes necessary.

## Documentation and retention

Plan: [plan.md](plan.md). Architect findings/proposal: [design.md](design.md).
No application documentation changes are needed for findings alone. Leave the
session open; no lifecycle cleanup is authorized.

## Accepted investigation evidence

- Fresh remote master: `2f5156262baaf137800c17a9321e617c2b5df1d5`,
  `VERSION=0.30.0`; raw GitHub at that exact revision independently agrees.
- Latest release tag inspected: `v0.31.2`, commit
  `819bba5110e089465535ecd71ca2eb37a7d39caa`.
  Earlier tags `v0.31.0` and `v0.31.1` also exist off master; common base
  `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`.
- Architect confirmed RubyGems exact-version API returns 0.31.2 with creation
  `2026-10-28T09:17:26.825Z`; GitHub release is public/non-prerelease,
  published `09:20:14Z`. Lead web tool could read raw GitHub but could not read
  RubyGems pages/API; publication sample comes from architect's direct check.
- Final tree diff master→v0.31.2: 19 files, 165 insertions/35 deletions;
  shared metadata/dependency versions, 101 changelog lines and one performance
  lineage spec. Architect's `git cherry` shows all four application/performance
  backports have patch equivalents on master.
- Release procedure creates a release branch and changes versions there, with
  no master synchronization step or defined master version floor.
- `utils/release/artifacts.rb:151` (`Artifacts#check_tag`) checks tag identity,
  remote tag and newest release branch membership, but never master VERSION.
- Release-only commit `c9124da141adc258fbbaf67d4ec19ee3f8580849` isolates
  maintenance test fixtures from source VERSION. Lead inspected its diff:
  a metadata-only bump on master would leave tests coupled to 0.30 source.

## Proposed follow-up, unimplemented

One bounded package: catch up master to 0.31.0 using `make version` for all
component identities and constraints; restore missing 0.30.1/0.30.2/0.31.x
changelog entries; bring back the released fixture isolation fix; document that
master keeps the latest major/minor base with patch zero. Prepare major/minor
bumps on master before branching; keep patch bumps on release branches. Validate
master patch == 0 and a numeric major/minor floor against the release candidate,
so 0.31.0 master allows 0.31.2 releases. Preserve any higher major/minor master
version. The user's correction supersedes the prior 0.31.2 catch-up and
full-version-floor proposal; historical publication evidence above is unchanged.
Current parser accepts only X.Y.Z; a prerelease version convention would expand
scope and is unnecessary for this correction. Preserve tags/artifacts and
existing partial-publication recovery semantics. Exact historical operator
intent is unknown; mechanism and process omission are established.

No builds/tests or final change review were run: source was not changed.
Investigation/read-only evidence alone is exempt from automatic final review.

## Handoff

Lead accepted the architect's completed brief after inspecting the release check
and fixture-adaptation diff. No blockers remain for the requested investigation.
Next action, if requested: assign one implementer the bounded package in design.md;
implementation, review, integration and publication remain separate future work.
No tracking commit was required before project-code or external mutations because
none were performed; current findings remain in this session directory.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-release-versioning-audit/).

## Major/minor policy revision accepted

Architect revised design.md; lead inspected and accepted the proposal and focused
verification brief. In addition to release-time major/minor comparison, reuse
existing master metadata validation to enforce patch zero in master context
(including detached CI); release branches may retain nonzero patches. The design
explicitly remains unimplemented. No new investigation/runtime tests were needed
for this policy clarification. No blockers; next action is the bounded
implementation package if requested.

## Implementation start

User accepted implementation after correcting master version semantics. The
architect brief is accepted; its proposed status records investigation history.
Root workspace has no declared hook framework or active hooks; shared master
and origin/master matched after fetch. Initial tracking commit will stage only
this session's plan/state/design/portal files, preserving unrelated changes.
