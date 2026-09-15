# Bulk exemption removal correction review

Initiative: 2026-09-09-ip-release-mechanism. Read plan.md, state.md and
review-redesign-results.md for the completed four-lane review. This rerun is
limited to the subsequent removal correction. Use gpt-6-astra/xhigh, read-only,
no subagents, credentials, cluster mutations, long integrations or lifecycle
operations.

Repository worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin
Baseline: 5e15045a67278569ef45fb5a2246291ff510887e
Head: a75bb80d5d4ce76e95c766199bc35e798fab956e

The live browser passed navigation, creation preview, bulk setting, actor IDs
and select-all restoration. Removing failed before HTTP: the PHP client rejects
explicit null on a required input even if nullable. Verified in 0.29.6 and
upstream 0.29.8. The correction replaces null signaling in the newly introduced
campaign batch action with an explicit remove boolean (default false). Setting
still requires a nonblank reason via the existing model. Missing, null or blank
reasons cannot clear existing exemptions. UI removal omits reason and sends
remove:true. Shared batch logic, locking, authorization, historical actor fields,
and the pre-existing single-address HTTP action are unchanged.

The batch null-removal interface was only present in the unmerged feature and
this disposable cluster. Deploy API before WebUI and refresh discovery. Mixed
old/new versions reject removal and keep exemptions. Schema and state unchanged.

The owning docs/ip-release.md documents the explicit flag and validation.
Localization adds only the Remove exemption API parameter label (CS:
Odstranit výjimku). Changes remain in the existing API/WebUI commits of the
accepted eight-commit series. No generic client/dependency release or new repo.

Unchanged overlay head: 715c063396fa49277852b98d36347c8bec5160d3.
KB current exact pin: 46279da7f53a3f2620d263696422fd7fb828b1b6 (5e15045a6);
it will be mechanically repinned after the reviewed correction is final.

Quick checks: campaign request specs 12/0 (seed 58936); final null/missing/blank
case 1/0 (seed 9059); Ruby lint, PHP/JS syntax, localization and normal commit
hooks passed. The tracked worktree is clean.
The existing browser scenario includes bulk add/remove across both owners and
will run again after review. The first attempt on the immutable older source stopped at the preview helper;
the hosted artifact confirms the same test issue. The independent live browser
reproduced removal validation failure after successfully reaching bulk actions.

Risk remains high: administrator protection removal over retained allocations.
Rerun general, architecture (API/client interface) and risk/compatibility lanes.
The scope lane is not rerun: this substitutes explicit signaling within the
already reviewed single bulk action; no new operation, shared abstraction,
repository, client framework or deployment mechanism is introduced.

The first isolated browser run failed before bulk removal: its submitForm helper
uses Locator.all() without waiting for newly navigated controls. The captured
page includes the Preview addresses button. Replaced only the three new campaign
creation submits with scoped getByRole(...).click(), which waits. No shared test
helper changes. The live browser already reached creation and bulk operations.
