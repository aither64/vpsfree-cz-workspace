# Operations page and reservation badges — final review

Initiative: 2026-10-13-workspace-coordination, root /home/aither/workspace/ai/vpsfree.cz.
Review the completed committed follow-up through all four lanes: general,
architecture/repetition, scope/proportionality and risk/compatibility. Read the
mandatory-change-review skill and every selected reference yourself, plus shared
AGENTS/procedure routes and local AGENTS for the affected repositories. No nested
agents or mutations. Remain the same independent standalone GPT-6 Astra/xhigh
reviewer; installed catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd
still selects lead_reviewed/reviewer (read_only, gpt-6-astra, xhigh). The initiative
is threadless and has no team roster, so this retained standalone fallback remains
applicable. Parent verified the catalog and your retained prior identity/report.

User request: move Operations to a subpage and menu entry beside Automatic
archival; badge/tag session-list machine holders. User selected machine
reservations only, excluding brief merge/execution locks. Accepted design and
verification brief are appended to work/2026-10-13-workspace-coordination/design.md;
plan/state and rollout/live evidence are in that tracking directory.

Implementation: authenticated read-only /operations, shared menu, Handoff link
and no inline coordination panels on index/Handoff. Existing lifecycle progress
is preserved. Active and completed jobs remain active-first. Derived portal
reservationHolders includes ownerId, slug, portalUrl and machine/state rows for
all current holders before history truncation. Reuses Store.lifecycle_owners for
active/archive incarnation matching; requested/released reservations and foreign
owners are excluded. Browser has one visible-only five-second reader, reuses
cached badges after index-card refresh and retains successful display with a
warning after failed reads; hidden/navigation responses are canceled and ignored.
No persisted schema, reservation release, scheduler/admission, workers, notification
or mutation approvals change. The host operator remains trusted; assess remote
input/authentication and ordinary concurrent/mistaken ownership boundaries.

Quick checks passed in the runtime Nix shell: Node regressions 3/3, Ruby badge
projection 3/27 and focused Go Operations/Automatic archival route checks. Log:
operations-quick.log (status 0). First Ruby test assumed insertion order despite
sorted ledger UUID serialization; deterministic historical fixture IDs fixed it.
Initial Go test and unchanged Automatic archival test read the real host provider
catalog; the supported DEV_WORKSPACES_CODEX_PROVIDERS override isolates them.
README documents that focused-test setup. Saved failed evidence is retained.
Final composition check operations-composition.log passed, and only the intended
runtime lock node changed in workspace/configuration. Configuration hooks passed.

Whole-branch inventory: operations-inventory.json contains all four exact bases,
heads, complete series, final patches and old-to-new range-diffs. Inspect them and
explicitly conclude on whole history and migration lineage. Original runtime core
and portal fixups were folded into their owning commits, so final runtime still
has two commits and introduces the final page directly. Workspace keeps one
composed-input selection and a separate policy/docs commit. Configuration's single
pin was regenerated through dev-workspace/devWorkspace from its documentation
predecessor, preserving the generated message/hooks. Temporary pin checkout was
removed. Extension is unchanged at c697acc7 and retains its earlier cleared review.
No obsolete approaches/fixups or redundant intermediate pin updates are intended.
No migrations: nothing merged/released/deployed/externally consumed needs a schema
transition. Prior deployed exact revisions and source roots remain supported and
retained separately in rollout/live evidence, not extra feature-history pins.

Owning component is generic dev-workspace; the browser consumes its Ruby-derived
read-only projection through Go's existing coordination API. The site workspace
consumes the runtime through its direct nested override, preserving extension
c697acc7 and sibling inputs. Configuration's devWorkspace selects the matching
host contract without installing the user application. Extension adapter/contract
interfaces are unchanged. Docs: runtime README, docs/coordination.md and
workspace-portal.md; site workspace docs/coordination.md; configuration's existing
aitherdev operations guide was checked and remains accurate. Individual rollout
history remains in tracking/rollout.md.

Risk classification: high due to the additive public read interface and live
self-deployment compatibility; behavior change is otherwise bounded presentation.
After review, parent will run package verification and no-reboot coordinated
system/profile redeployment under the original deployed_review reservation.
No default-branch integration, ownership release, reboot or closure is authorized.
No new UI controls, queue policy, generalized status framework or team changes.

Report findings by severity and lane with file/line references and residual gaps.
Review all applicable scopes directly; do not rubber-stamp the packet. Return your
report to the parent without writing initiative records or source files.
