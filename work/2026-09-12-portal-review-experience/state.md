---
lifecycle: active
---

# Portal review experience

## Current status

All approved features are implemented, committed, pushed and deployed as
profile29 on aitherdev. The exact final package is
`/nix/store/prpvck3v35xbvyz60gfwprz9p3lsagal-dev-workspace-0.2.0`.
All final CI checks pass. Mandatory review is complete with no unresolved
Blocking or Important findings. The real creation fixture proved recovery
of its already-created plan session without replay and passed the isolated
old/new package checks. Passive blocking-question observation passed; answering
that question after the test portal restarted remains unverified. All owned fixtures and temporary GC roots are removed. This consolidated
coordination checkpoint records the implementation and verification.

The session stays open and all feature branches remain unmerged. No archive,
delete, branch deletion or default-branch feature integration is authorized.
Shared coordination checkout remains on master; preserve unrelated changes.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-review-experience/

The verified current session uses slug `2026-09-12-portal-review-experience`,
workspace `/home/aither/workspace/ai/vpsfree.cz`, and shared thread
`01a09541-d1ba-7e32-a634-6f915c2da0a4`. Initial tracking commit: `e0d3dee`.
`dev-session current` matches when both session environment variables are set.

## Repositories

All feature branches are named `2026-09-12-portal-review-experience`. Worktrees
are under `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/`.
All four repositories are registered in portal.yml, clean and pushed over SSH.
Their heads contain the explicitly fetched remote default branches.

| Project | Final head | Worktree |
| --- | --- | --- |
| codex-web | 83770217d63f2c206689d2c569e1c81950544504 | codex-web |
| dev-workspace | d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2 | dev-workspace |
| vpsfree-dev-workspace | a30de6c62d2bcd1ff41ee48018c595140c6d4042 | vpsfree-dev-workspace |
| workspace | 9edf553f03b94b69ac96bb4d986eddccd3fa90b5 | workspace |

Initial bases are recorded in portal.yml. Final review packets retain their
exact reviewed ranges. The workspace feature is based on the initial shared
coordination commit; subsequent coordination records are maintained on master.

## Delivered behavior

- Questions have a taller scrolling body with Back/Next/Submit outside it.
- New, fork and plan-new requests navigate to their destination immediately,
  with initialization stages, errors and explicit retry before a manifest exists.
- Repositories use two desktop columns and one narrow column. Local native Git
  supplies branch commits, GitHub links, expandable message bodies and bounded
  per-commit or whole-branch comparisons. CodeMirror supplies self-hosted split
  and unified views, line numbers, colors and file navigation. Split is remembered
  by default. The approved standard unified gutter behavior remains unchanged.
- Typed web searches and subagent interactions render in the conversation.
- Current root-turn message/tool counts, observed work, closed waits and the
  current wait are separate. Unobserved history stays unclassified. Current
  trailing idle time is excluded from completed waiting totals.
- Messages is the initial output filter.

Native Git required no new Git library. CodeMirror and its build dependencies
were checked for active maintenance and pinned. diff2html was not selected.
Dependency sources, limits and accepted decisions are in plan.md.

## Verification and reviews

All mandatory general, architecture, scope and risk reviews used fresh
`gpt-5.6-sol` reviewers with `xhigh` effort. Reconciliation and exact delta
reviews are retained in review-reconciliation.md and linked review packets.
Final causal deletion architecture/risk and deployed goal-normalization
general/risk reviews reported no findings. Earlier findings were fixed or
explicitly reconciled before long acceptance.

- Final Nix package: every Go package passes; 296 Ruby tests / 2,979 assertions
  and 73 host tests / 438 assertions pass, with 12 and 3 declared skips.
- Full generic flake check passed. Host-module idempotency VM passed in
  321.90 s using cached kernels. Later changes do not affect the host contract.
- Installed Codex 0.154.0 experimental schemas/model defaults pass. The selected
  binary's actual fresh-thread protocol check passed in 1.254 s.
- Controlled full-handler browser acceptance passed at desktop, short, mobile
  and zoom-equivalent viewports, including fixed question actions, actual
  answers, typed events, counters/timing and frozen archived activity.
- Repository browser checks passed split/unified, two/one columns, stacked
  lazy diffs, last-file navigation, body expansion, read-only behavior and CSP.
- Real new/fork/plan-new HTTP responses took 14.8/42.7/12.6 ms; browser navigation
  took 300/255/239 ms. Delayed initialization kept the destination responsive.
- The real accepted plan survived source changes, restart and explicit retry.
  Its trailing newline exposed a portal/CLI digest mismatch. The final fix
  matches Ruby strip exactly and recovered the same receipt/thread/attempt,
  frozen plan, binding/evidence and one initial submission without a CLI call.

Final CI links and exact heads are in ci-final.json. Commands and detailed
results are in packaged-validation.md, conversation-browser-verification.md,
repository-review-verification.md and creation-integration-results.md. Earlier
implementation commands, intermediate heads, review findings and diagnosis are
preserved in implementation-history.md.

Real blocking-question observation passed with the browser on another session:
waiting grew for the held interval while working time stayed flat, and the
prompt remained unchanged. An artifact-only Selenium stale-element error
after option selection closed the test portal's interactive connection. The
exact turn remained waiting after reconnect, but the original request was no
longer delivered to the new portal connection. The real answer/closed-wait
subcheck is unverified. The owned turn was interrupted through the ordinary
API after exact identity checks; no further question was sent. Controlled
browser answer/closed-wait checks passed separately.

Actual head -> base -> head acceptance passed: the old package read all three
canonical sessions, replayed the source without duplicating its initial request,
and created only the fourth intended thread before a conflicting head receipt
could bind. Rollforward preserved the canonical composer, rejected stale retry,
created no false completion evidence, and retained all three ready identities.
No production changes follow the deployed d3bfd0f fix.

## Deployment and compatibility

`workspace-host switch --source <workspace feature worktree>` installed
profile29 through normal generation, runtime/cluster and Codex preflights.
Authenticated HTTPS, all four repository histories/comparisons, activity and
assets pass. Router, portal, Codex and tmux user services are active.
Profile28 retains the previous feature package pwi8v7s and profile27 retains
the pre-feature package aamx7bq. No system configuration changed.

A live rollback from profile28 was refused before mutation because another
session had an active turn. No forced interruption or repeated attempt was
made. The isolated old/new fixture passed compatibility checks; a real registered
profile rollback requires an idle workspace and is not claimed here. See
deployment-results.md and live-feature-checks.json.

Canonical session/lifecycle/journal formats are unchanged. Private receipts
freeze exact request/deletion identity; retries cannot recreate an explicitly
deleted destination or replace a separately completed canonical session.
Timing keeps private compact per-turn summaries without automatic expiry.
The goal normalization fix preserves captured plan bytes and old raw receipts.

## Limits and cleanup

Historical periods without complete observation remain unclassified. Retained
per-turn timing files and very large deletion histories have documented scaling
costs; no unrelated purge policy was introduced.

The selected Codex showed an exact missing-cwd filtered-history lookup timeout
against the large shared history. The same request returned in 3.9 ms in an
owned clean metadata home. Its upstream cause remains unestablished. A private
native/portal reconnect also left historical Plan mode inconsistent with the
next live turn; observer-shaped resumes did not emit a mode change in the
diagnostic. These acceptance limitations and any bounded retries stay in the
real creation report. They did not justify changing production Codex settings
or weakening creation identity checks.

All controlled-browser and real-creation fixtures are removed. Cleanup proved
exact ownership of all four private threads, tmux sessions and the App Server;
all threads were inactive and no fixture process remained. The private home,
workspace, sockets, TLS, raw outputs and credential symlinks were removed while
leaving their authentication targets and all shared services untouched.
Root removed the remaining 86 task-owned temporary files, generated schema
directories and package/browser GC roots after checking process references.
The installed profile retains the deployed package. Curated evidence remains
under this initiative; registered worktrees and branches remain available.

Next action: user review of the deployed features. Keep this initiative active
and open for follow-up; no feature integration or archival has been performed.
