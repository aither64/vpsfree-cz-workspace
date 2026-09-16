# Filter transport correction: bounded review rerun

Read mandatory-change-review/SKILL.md and your lane reference. Review only the
committed correction from vpsAdmin 9840cdf08b9dbdb825bac0da04aa74281d3c4e2a to
be21bc8b9e4101ca6b35654ad6f52147dea87213 (API ad203b205), with relevant context.
Companion KB bce530f8af8778ddc77fae9b89510f50225d4a5d replaces e098f688 and only
pins this exact vpsAdmin revision; full bin/check passes. Overlay unchanged.

All worktrees, base commits, accepted scope, deployment and ownership contracts
are in review-refinement-packet.md. All four lanes reviewed the full refinement;
findings and remediation are in review-refinement-results.md. The eight-commit
series and first six prerequisite commits are unchanged.

The default/multi-select preview must work through HaveAPI PHP client 0.29.6,
which supports scalar GET values but stringifies raw arrays. Correction:
Candidates versions/networks/locations are comma-separated String parameters;
UI converts its validated arrays before the request. Internal model arrays still
work. Empty network/location lists mean unrestricted; versions default to 4.
API docs and EN/CS descriptions record the scalar query representation. No
shared client change, fallback framework or additional repository is introduced.

Member Notice history uses an explicit id/event/subject/created_at whitelist,
matching the request/address response boundary; its existing fields were safe.
This directly resolves the architecture advisory. The Notice history name stays.

Quick verification: API default/multiple/invalid filters and notice keys 3/0,
seed10265; real pinned PHP client transport 1 test/2 cases, no network; formatting
and all commit hooks pass. The final tree equals the checked pre-fold tree.
Browser integration and deployment have not started yet. A bounded disposable
campaign-table reset is prepared to remove the former label while preserving
all existing campaign/request/notice/address rows and both VPSes.

High risk because the new endpoint input contract changes; review
with gpt-6-astra/xhigh. General, architecture and risk lanes rerun. Scope boundary
is unchanged; the completed scope review required exactly a local transport fix.
Do not expand into unrelated prior mechanisms. Report findings with severity and
concrete evidence, or none with residual gaps. No edits, credentials, screenshots,
external/cluster mutation, long tests, subagents or lifecycle actions.
