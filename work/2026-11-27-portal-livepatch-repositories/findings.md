# Livepatch repository tab diagnosis

Investigation on 2026-11-27; target session
`2026-11-18-livepatch-backport-process`. No source, registration, Git ref or
package changes were made. Normal portal GET requests may populate its existing
comparison cache/store, as they do when browsing.

## Confirmed cause

The deployed generic dev-workspace portal chooses the merge base with locally
available `origin/master` before considering the recorded initial base for active
Linux registrations. Its local origin/master is a historical October 2019 commit
(subject: `[vpsAdminOS] Enable trusted xattrs for 1st-lvl userns`). This is the wrong
review baseline for current backport work. Its merge base with the observed
linux-core head is `3b1f00aceb7a67bf079a5a64aa5c6baf78a8f442` (October 2019).

At observed linux-core head `2904ad84b510af32ee889812560861507059ce2c`:

| Comparison | Changed paths | Feature commits |
| --- | ---: | ---: |
| Portal-selected 2019 merge base to head | 88,014 | Not counted |
| Recorded initial base `1dfea587406b7dd79973831d1677fb2418e5e9aa` to head | 9 | 13 |

Path counts used bounded `git diff --name-only -z --no-renames BASE HEAD` reads
with lazy fetching, optional writes and auto-maintenance disabled. These metadata
reads completed in about 1.4–1.7 seconds. The initial-base commit count used
`git rev-list --count BASE..HEAD`. Branches remain active and can advance.

The reader permits 5,000 files and 4 MiB command output; the 88,014-path comparison
exceeds the bounded review contract. Linux-core summary and durable comparison
GETs returned HTTP 422: `This comparison exceeds the review limit. Review a
smaller commit locally.` The final comparison probe took 3.424 seconds.

A separate cold/read-contention symptom is a four-second Git command deadline:
linux-core history initially returned HTTP 422 in 4.045 seconds, while its exact
head resolved and a direct merge-base read succeeded in 6.616 seconds. Later
history reads succeeded, so this was not evidence of a missing head. Reader
resolution and generic HTTP error mapping obscure timeout causes.

## Why the tab appears stalled

The session has 28 registrations: 13 Linux and 15 vpsAdminOS. The browser eagerly
queues histories in sequential batches of eight. Replaying those batch GETs
produced durations 8.465, 8.386, 0.099 and 0.049 seconds. All histories succeeded
in that replay, but Linux histories included unrelated old upstream history and
later repositories waited behind the slow Linux batches. Concurrent summary
requests and repeated failed requests can add load; that additional effect was
not benchmarked.

The details request also enriches all repositories under a shared five-second
budget, followed by a one-second comparison-observation budget. Logs repeatedly
show approximately six seconds for repo_status and misleading `review head is
unavailable locally` / `repository has no recorded comparison base` errors.
That observation pass cannot reliably perform multi-second Linux merge-base
reads within one second.

This is not a confirmed total portal outage. vpsAdminOS history returned HTTP 200
in 0.059–0.067 seconds; summary returned 200 in 0.078 seconds with 22 commits and
213 files; its durable comparison returned 200 in 0.022 seconds with 213 files.
No full browser automation was performed. The investigation confirms Linux
comparison failures and delayed batch loading, not every possible client-side
symptom.

## Recommended solution

1. Give repository review an explicit comparison baseline independent of the
   delivery/default branch. For these backport branches, use verified recorded
   starting SHAs, including the existing `1dfea587...` base for linux-core, after
   checking each branch's intended scope. Preserve existing default-branch and
   lifecycle/publication semantics. Do not guess bases for registrations that
   lack evidence. A review-specific override should take precedence over the
   default-branch merge-base calculation without globally changing ordinary
   feature-branch semantics.
2. Preserve exact base/head durable links and define compatibility with already
   saved comparisons. Simply running capture-comparison is insufficient today:
   active, unmerged Pair returns its default-branch merge base before looking at
   saved comparisons; the writer also refuses replacing a different exact saved
   pair. Implement the override through a supported command/schema, not manual
   edits to private saved records. Old links should continue to describe their
   original pair; new views should use the selected review baseline.
3. Keep limits, but distinguish timeout, missing data, absent baseline and excessive
   comparison size in the UI. Load requested/visible repositories independently
   within a bounded queue so healthy repositories are not held behind slow batches.
   Cache/coalesce merge-base calculation by canonical repository and exact input
   SHAs; avoid redoing it in the one-second status-observation pass. Consider a
   measured deadline adjustment only after selecting the right base.

Do not solve this by changing the lifecycle default branch, guessing historical
initial bases, increasing the file cap to accept an 88k-file review, or increasing
all timeouts. Refreshing commit graphs may improve traversal but does not correct
the comparison scope. No maintenance operation was attempted.

Acceptance for a follow-up fix: linux-core at the recorded head shows 13 commits
and 9 changed files with usable file previews; ordinary feature comparisons and
old durable links retain their behavior; a slow or unavailable repository does
not hold healthy cards; errors identify the actual failure. Review partial-clone
missing-blob behavior separately if a selected file preview needs absent content.

## Source and evidence

Running binary:
`/nix/store/qd92rjc86aiw663nmn5vpmbcg8fc5sfb-dev-workspace-0.2.0/bin/workspace-portal`.
Its derivation resolves to source:
`/nix/store/5s0dg74qrxj8q3pz24j3kh98bhdnjwfg-source`.

Relevant paths under that exact source:

- `portal/internal/repository/review.go`: limits at lines 24–29, Git deadline and
  queue at 155–185, Resolve error wrapping at 207–268, Pair at 283–332.
- `portal/internal/web/repository_review.go`: generic errors at 171–185;
  15-second HTTP deadline at 263; history/pair creation at 471–523.
- `portal/internal/web/repository_comparisons.go`: saved exact-pair immutability,
  CLI capture, and automatic comparison observation.
- `portal/internal/web/server.go:1682`: five-second enrichment and one-second
  automatic comparison observation.
- `portal/internal/web/static/repository-review.js:323`: sequential batches;
  `:890`: eager hydration; `:910`: head checks that requeue failed histories.
- `docs/workspace-portal.md:388`: documented comparison limits, independent
  history/summary requests and local-only object reads.

Read-only HTTP probes used the running portal's Unix socket and normal session
repository-history, repository-histories, repository-summary and durable
repository-comparison GET endpoints. An initial probe accidentally used 24-character
repository IDs; corrected probes used the actual 32-character SHA-256 prefix.
An initial comparison GET used a history snapshot in the worktree-snapshot route;
that expected 409 was excluded and the correct durable review route reproduced
422 for Linux and 200 for vpsAdminOS.

Two optional `git show -s` metadata probes hit their ten-second bound; commit
metadata was subsequently obtained with bounded `git cat-file commit` reads.
No full builds, tests, browser sessions, fetches in the source projects, repairs
or deployment were needed. Source/default comparison metadata remained unchanged.
