# Automatic counts and exact previews: final follow-up review

No Blocking, Important or Advisory findings. The final heads may proceed to
their planned package, CI and deployment verification. This review does not
claim that the final heads have been deployed or integrated.

Reviewer: `/root/counts_final_review`, retaining the assigned
`gpt-6.1-sol` / `xhigh` settings and independence from the original review.
High overall compatibility/deployment risk; general, architecture and repetition,
scope and proportionality, and risk and compatibility lanes. Reviewed directly
without nested agents. Applicable unchanged guidance and the original report
remain in this context; the updated packet, repository instructions and review
skill/lane references were consulted for this follow-up.

## Exact final series

| Repository | Complete base | Final reviewed head |
| --- | --- | --- |
| dev-workspace | `02881b401955ff0db71bb74f6fb84f6e475a7879` | `db4b0fa62633b925e1917ec880737e1776f82cc8` |
| workspace | `42c76e8cb61e0d2063a3d25b4b448e66abee523f` | `3bdad4b138a346482e98be906660f8526020835b` |
| vpsfree-cz-configuration | `5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c` | `55b83513b863c704c845e65e956b8230482f173e` |

Each complete range contains one commit. Inspected their full commit lists,
messages, complete consumer diffs, runtime range-diff and exact runtime tree
delta against the previously reviewed head. An explicit excluding-path diff
returned no differences outside `portal/internal/repository/review_diff.go`.
The earlier runtime review therefore covers every unchanged portion of the
complete final runtime diff, rather than only a selected subset of its files.
All three tracked worktrees are clean. Local merge bases and fresh read-only
SSH remote checks confirm the stated bases are still remote master and the
published feature branches select the final heads above.

Whole-series/history conclusion: the final branches directly introduce the
accepted counts behavior and the bounded preview correction. No obsolete
unmerged approach, fixup, intermediate protocol or unused compatibility path
remains. The preview flag fixes a demonstrated failure in the same large-Linux
review acceptance path; folding this small correction into the owning feature
does not introduce an unrelated subsystem or conceal a separate deployment
mechanism. Commit rationale now describes that final behavior.

**No migrations.** No database, persistent schema, manifest, saved comparison or
operation-journal change exists. There is no intermediate migration to preserve
for merged, released, deployed or externally consumed state.

## Delta and retained lane conclusions

At `portal/internal/repository/review_diff.go:52`, `--full-index` expands the
object names on Git's patch index line. The parser at line 56 consumes only
`@@` hunk headers, so that output formatting change leaves its input contract
and validation unchanged. The command still receives the same verified full
blob identities, diff algorithm, hunk options, text policy and no-external-diff
or textconv options. It uses the same bounded runner, deadlines and output cap.
No new revision lookup, fetch, filesystem path input or permission boundary is
introduced. The short adjacent comment records why the flag is necessary.

The supplied live measurement attributes the timeout to abbreviation searches
and reports the same frozen blob diff at 3.61 seconds versus 0.161 with full
hashes and identical hunks. Existing focused diff/content tests exercise the
actual Git command and the hunk parser, including newline/unicode and
inconsistent-stat cases. The packet records their successful Nix run in 0.673
seconds. This is an appropriate conventional Git fix with limited maintenance
surface; no custom abbreviation logic or new abstraction is needed.

All unaffected four-lane conclusions in [the original report](counts-final-review.md)
remain valid for these final heads: automatic counts, immutable shared cache,
snapshot authorization, stale-response rejection, suspension/retry, preview
count preservation, proportional scope, additive endpoint and asset delivery,
working-change captures, mixed-version behavior and rollback restrictions.
The host-operator trust assumption and remote-client protections are unchanged.

Documentation placement/preservation conclusion also remains valid. README and
the linked portal reference are byte-identical to the reviewed versions, so no
entry point, contract, prerequisite or recovery restriction was removed. An
internal patch-index formatting flag needs no new user-facing prose contract;
its lasting rationale belongs beside the command. Measurements and deployment
status properly remain session evidence. No upgrade path is retired.

## Pins, consolidation and deployed lineage

The final consumer diffs select runtime `db4b0fa6` and NAR
`sha256-oikFACN3yLS8JwMk/p5NzQ7kzjaH53H97AYmb2mm7sQ=`. Workspace retains its
direct nested runtime URL and extension `0c7168f3`; configuration retains its
existing dev-workspace/devWorkspace channel. No sibling input, follows path,
native Codex choice or user-profile application ownership changes.

Confirmed the local `2026-11-10-portal-linux-review-performance-counts-deployed`
refs resolve to the exact deployed predecessors:

- runtime `4dd6c7577c4e6c6f607f07c5227b553f17975cce`;
- workspace `bf0574e49ac555e7eb36afbbbb486828e1c5d7b6`;
- configuration `f74dd69e590eb53e79743eed70ca9224e852b3af`.

Those predecessors were unmerged, and their rollout evidence remains retained.
The final runtime preserves all their behavior plus the preview flag; the two
consumer deltas only advance the selected runtime identity. No supported state
or API version requires an intermediate commit in the final branch history.
Repeated-stream conclusion: the superseded consumer updates have been
consolidated into one final update per owning branch. Preserving deployed refs
and execution evidence does not retain redundant pin commits in these ranges.
The already merged bases were not rewritten.

The deployed predecessor must remain distinguishable from these newly reviewed
heads. As the packet requires, complete and verify a new deployment of the
final composed system/profile before claiming final deployment lineage or
releasing its machine claim. The older deployment or its CI result alone does
not establish that proof.

## Verification limits

Independently ran `git diff --check` over all three final ranges; all passed.
Inspected source, tests, preserved refs, current remote heads, consumer locks,
the updated packet and deployment/build records. No tests, builds, deployment,
source edits or lifecycle mutations were launched during this follow-up; only
this report was written. The supplied final deployment-contract result is
successful. Final-head CI, package verification, redeployment and live Linux
preview acceptance remain delivery work; the earlier feature CI applies to
its recorded predecessor. Host timing measurements are not latency guarantees.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-portal-linux-review-performance/
