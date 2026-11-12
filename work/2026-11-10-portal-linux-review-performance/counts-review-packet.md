# Automatic counts: final review packet

User requires additions/deletions automatically in overviews and diff headers,
including collapsed/unopened files, to judge changesets. Initial content-only
counting was rejected. Existing authorization covers aitherdev deployment and
merge of these three repositories after verification. No stage-2 subsystem.

Initiative: 2026-11-10-portal-linux-review-performance. Lead owns application code;
this original threadless session has no retained roster (team list refuses a
missing lead thread). Original application reviewer no longer exists in the live
native list. Use fresh installed-catalog review fallback gpt-6.1-sol/xhigh.
Installed catalog at /nix/store/a0nhkz2khja7qp17vw5fh1p8327i10iw-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json:
default delegated, reviewer purpose review, model gpt-6.1-sol, effort xhigh.
Risk high for additive browser/API and deployment composition compatibility.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.

Worktrees are /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-10-portal-linux-review-performance/<repository>.
Tracking plan/state/design/rollout are under the corresponding shared work path.

| Repository | Review base | Final head |
| --- | --- | --- |
| dev-workspace | 02881b401955ff0db71bb74f6fb84f6e475a7879 | 4dd6c7577c4e6c6f607f07c5227b553f17975cce |
| workspace | 42c76e8cb61e0d2063a3d25b4b448e66abee523f | bf0574e49ac555e7eb36afbbbb486828e1c5d7b6 |
| vpsfree-cz-configuration | 5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c | f74dd69e590eb53e79743eed70ca9224e852b3af |

Each range has one commit: runtime automatic counts with cohesive tests/docs;
workspace selection; generated confctl channel pin. Inspect full base..head log
and diff for each. Initial feature commits are already merged into remote master
and deployed, so they are not rewritten. No migrations, database/state/protocol
changes, obsolete unmerged approaches or repeated unmerged update streams.
Each pin is the sole follow-up update in its stream. Preserve native Codex,
extension 0c7168f3, sibling inputs/follows and user-profile ownership.

Design: bounded exact-rename numstat read enriches cloned metadata; existing
single-flight/LRU caches share counted files between summary and counts endpoint.
Metadata/history remain independent of counts and preview content. Snapshot
registration/scope authorization and existing 4-job/4-request/deadline/output
limits remain. No fetch/maintenance. Browser starts counts automatically, resumes
suspended requests and rejects stale responses. Explicit failure/retry; known
counts survive preview failures. Worktree captures unchanged. New endpoint is
additive; assets versioned together; persisted formats unchanged. Existing legacy
rename links retain their representation and separate cache. Runtime is the owner;
its browser is the endpoint consumer. Workspace/configuration select the runtime
through existing nested input/channel. No other endpoint consumer found.

Quick checks passed in runtime Nix shell: gofmt; node syntax; repository URL/
metadata mounted contracts; focused Go metadata/parser/summary/cache/missing-blob
checks; actual Playwright TestQuestionBrowser/repository_review_live_browser_test.cjs
(7.3 seconds), including collapsed-file automatic counts, summary/count suspension,
stale results, retry and preview count preservation. First browser invocation had
missing NODE_PATH; corrected to pinned Nix Playwright. One fixture expected an
unavailable count after its stub preview supplied no counts; fixture now explicitly
fails that preview to exercise the intended unavailable case. No rerun without
diagnosis. git diff --check passes. Configuration's Overcommit hooks pass; runtime
and workspace declare no hooks. Both effective locks select 4dd6c757 and matching
NAR; deployment checker passes with absolute source roots.

Documentation inventory: automatic count behavior/failure/compatibility → portal
users and maintainers, reference → runtime README.md and docs/workspace-portal.md
→ focused API/browser checks. Existing README links preserved. Individual rollout
and exact evidence → operators, execution → shared state.md/rollout.md. No new
runbook, persisted schema or upgrade path. Writing skill applied by lead.

Live source evidence: NFS frozen vpsadmin range has 2 files +349/-4 (12 ms);
vpsadminos 15 files +4311/-37 (21 ms). Earlier Linux 3,223-file numstat probe was
1.644 s / 554,104 KiB peak RSS. Candidate live API acceptance remains after review
and package build. These are host measurements, not latency guarantees.

Review directly without nested agents. Remain read-only except your report at
work/2026-11-10-portal-linux-review-performance/counts-final-review.md. Report
severity/path evidence and explicit complete history, migration, repeated-stream,
documentation placement/preservation conclusions. Do not run long integration
checks or deployment. Local operator is trusted; remote clients remain untrusted.

## Final preview correction (supersedes the heads above)

Final ranges retain the same bases and one consolidated commit per repository:
- dev-workspace: db4b0fa62633b925e1917ec880737e1776f82cc8.
- workspace: 3bdad4b138a346482e98be906660f8526020835b.
- vpsfree-cz-configuration: 55b83513b863c704c845e65e956b8230482f173e.

All are committed/published; clean tracked worktrees. The only runtime delta
from reviewed/deployed 4dd6c757 is --full-index and its explanatory comment in
review_diff.go. A live Linux preview timed out during abbreviation formatting;
the exact immutable blob diff took 3.61 seconds, versus 0.161 with --full-index.
Hunks are unchanged. Existing focused diff/content Go tests pass in Nix (0.673s).
Final deployment contract passes. Both locks select db4b0fa6 and NAR
sha256-oikFACN3yLS8JwMk/p5NzQ7kzjaH53H97AYmb2mm7sQ=; all other inputs retained.
The earlier full counts feature CI 43265715007 passed all applicable jobs.
New head CI 43272216960 is running; final package/redeployment are after review.

Earlier heads 4dd6c757/bf0574e49/f74dd69e were deployed but never merged. Their
refs are retained as 2026-11-10-portal-linux-review-performance-counts-deployed
in each owning local repository, with rollout evidence retained. New heads
contain the earlier behavior plus the narrow preview fix; no format/migration
or supported behavior is removed. Pins were consolidated to one per branch,
not retained as repeated updates. A new verified deployment is required before
claim release. Whole-branch history/migration conclusions must bind final heads.

Please review the final committed series and delta directly; keep earlier
four-lane conclusions where unaffected, and explicitly assess this final
history and deployment lineage. No new prose contract is needed for an internal
output-only Git flag; its code comment records the rationale. Write a separate
counts-final-review-r2.md, preserving your original report. No nested agents,
long tests, deployment or source edits.
