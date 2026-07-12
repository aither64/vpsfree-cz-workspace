# vpsAdmin KB documentation contract state

## Session

- Initiative slug: `2026-07-12-vpsadmin-kb-contract`
- Started as the explicitly planned follow-up after completing the Czech and
  English screenshot publications.
- The current shell still carries the previous completed session slug; all new
  work is isolated under this initiative's tracking directory, branches, and
  worktrees. The global KB staging container is stopped and unowned.

## Repositories

- `vpsadmin-kb-captures`: upstream default branch verified as `master` at
  `951a5e6`; new feature branch/worktree pending.
- `vpsadmin`: affected by stable WebUI documentation landmarks and contract
  generation; branch/worktree pending.
- `vpsfree-cz-configuration`: affected later by plugin packaging; branch and
  worktree deferred until a plugin revision exists.
- `dokuwiki-plugin-vpsadmindoc`: requested as a new empty GitHub repository;
  clone/worktree pending repository creation.
- Top-level workspace: plan/state tracking on shared `master`; KB tooling
  changes, if any, will be staged path-by-path around unrelated shared changes.

## Current findings

- Production and staging configurations package the same explicit DokuWiki
  plugin list with fixed GitHub revisions and hashes, so the new plugin must be
  added to both lists.
- Existing `<page>` translation mapping is provided by `mlfarm`; the proposed
  plugin owns only vpsAdmin documentation annotations and does not replace the
  language-pairing plugin.
- `vpsadmin-kb-captures` schema 5 already provides stable semantic screenshot
  concepts, checkpoints, bilingual source pages, media IDs, hashes, and pinned
  vpsAdmin provenance. It is the natural owner for the cross-repository impact
  checker.
- The legacy PHP WebUI builds sidebar labels and routes together at distributed
  `sbar_add()` call sites. Stable landmarks should be added through explicit
  contracts/helper parameters rather than inferred permanently from translated
  text.

## Approval boundaries

- Read-only production KB inventory is allowed.
- No staging KB mutation is planned until plugin packaging and annotated local
  candidates have passed review.
- Every production KB update requires a new explicit user approval.
- Machine deployment remains operator-only; this initiative may prepare and
  build configuration but cannot deploy it.
