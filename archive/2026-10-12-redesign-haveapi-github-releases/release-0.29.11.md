# Corrected HaveAPI 0.29.11 release execution

User authorization: on 2026-10-19, the lead explicitly requested integration of
the new fix into haveapi/master, advancement of haveapi-0.29 and annotated
v0.29.11. The user replied "continue". That direction covers those exact targets
and new tag. Publication still requires the user's fresh protected release
environment approval in GitHub. The earlier 0.29.10 approval is not reused.

Prepared source: 7fb218e28a86ab1d27de74ccb92c2a45063a4f78, on retained feature
2026-10-19-haveapi-0.29.10. Target base b27a031fa03d8d985a3abd2679ce2fc14fe53602.
Two logical new commits: 2b745b7 draft lookup fix/regressions, 7fb218e version and
changelog. New master fix is 526648131af45df68c25ac0042a52f22c7a81df5 from c14e7d3.
All four independent review lanes accepted both complete ranges with no findings;
whole-history, repeated-stream and no-migrations conclusions in draft-fix-review.md.
Full component/package checks and all 10 expected safe CI runs passed; see
draft-fix-verification-summary.md. Source and diff hashes rechecked before action.

Master integration submitted through selected-package coordinator as
30712947-5d77-4f21-8bfc-c380849e9e51. It stopped before jobs/Git writes in hook
preparation, repeating the diagnosed Ruby ABI/default JSON dependency mismatch.
Only the isolated source's ignored dependencies/config/lock are being repaired;
tracked source and review evidence remain unchanged. Resume the same request.

The installed coordinator catalog covers haveapi/master, not this separately
registered release target. Release-line/tag mutation uses the repository's SSH
fast-forward procedure; no catalog or registration target is changed. It must
preserve v0.29.10, its draft and original files. Use a fresh detached temporary
target checkout, hooks active through the verified source Nix/Bundler shell,
then atomic non-force branch/tag push. Retain refs/worktrees and keep session open.

Status: master fix integrated at5266481 through completed coordinator run.
Repository hook setup repaired only ignored dependencies, with both exact-order
probes passing. Completion event922cc1f3-7050-c821-d8bc-366319538f32 acknowledged.
Fresh read-only SSH confirmed master5266481, supported latest release0.29 still
atb27a031 and immutablev0.29.10 unchanged. All three gem and npm0.29.11 endpoints
returned404; required reviewer aither64 and sole tag rulev* rechecked.

Created fresh detached worktree worktrees/<slug>/haveapi-release-target-0.29.11
atb27a031 and ff-only advanced to7fb218e through the source Nix/Bundler hook
environment. Annotatedv0.29.11 plus haveapi-0.29 pushed atomically without force;
patch11-integrate-and-tag.sh/log/status (exit0). Source/diff still matches final
review and source worktree clean. No master version bump. Fresh Luna/low watcher
owns tag CI/build/approval-boundary observation in patch11-watch-wrapper.log/status.
No approval was submitted by the lead.
The v0.29.11 tag run must build its own retained originals, with its own run_id;
never substitute local dist, safe branch artifacts or v0.29.10 originals. Observe
the new run to the human approval boundary, verify its own manifest/hashes,
then supply the approval link. After approval, confirm all registry/PHP receipts,
public GitHub assets and asynchronous Packagist indexing. Diagnose every failure
before retrying. No cross-registry transaction is claimed.

Fresh SSH post-push proof: master5266481; release branch and peeledv0.29.11
7fb218e; annotated tag objectdf335479937a43f93e508ee19b93ba11f0fed8c3. Existing
v0.29.10objectcd6a5f4c and sourceb27a031 unchanged. Temporary target and all refs
retained; source worktree clean.

## Tag candidate verified; human approval pending

All seven ordinary tag workflows passed. Release run39305802582 passed build,
tests, packaging, upload and verification, and now waits for aither64 in protected
release. Watcher handed ownership to lead. Original artifact12212609441 saved to
patch11-tag-artifacts/ and CLI-verified with actual runID39305802582, source7fb218e,
version0.29.11. Manifest hash and approval link: patch11-tag-approval.md. Fresh API
check confirms pending release; no publication or approval by the lead. Next
human action is Approve and deploy; then observe publication and verify receipts.

## Approved publishing attempt failed before any registry write

User approved in GitHub and reported "done and it failed again". The draft was
created, then the paginated REST lookup still returned no exact intended-tag
match. prepare_github:198 raised nil.fetch. Credential and registry/PHP steps
were skipped. All exact0.29.11registry endpoints returned404. Failure evidence is
patch11-publish-attempt1-final.json and patch11-publish-attempt1-failed.log;
approval proof patch11-approvals.json. GitHub CLI's exact v2.102.0 implementation
resolves pending draft tags via GraphQL then gets REST metadata by databaseId.
No blind rerun, retag or replacement artifacts. Correct helper first; existing
tag source cannot be changed. Current investigation/design is in state/design.
