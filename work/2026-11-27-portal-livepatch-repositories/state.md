---
lifecycle: complete
---

# Repository tab repair delivered

The fix is deployed on aitherdev and all three exact final feature heads are
merged into their remote masters. All 13 Linux review bases were applied through
the supported CLI. Live browser acceptance confirms the core branch has 13
commits and 9 changed files, and renders comparisons and source previews.
There are no remaining blockers or delivery tasks.

## Phase checklist

- [x] Diagnose the wrong 2019 Linux baseline and design a compatible correction.
- [x] Implement explicit bases, independent loading, errors, tests and docs.
- [x] Pass focused checks and resolve independent final review findings.
- [x] Pass final CI, composed application checks and scoped host build.
- [x] Deploy matching system and application generations without reboot.
- [x] Apply 13 verified bases and pass live browser acceptance.
- [x] Fast-forward and push all three approved masters; verify exact remote heads.
- [x] Release all claims and remove the two temporary merge checkouts.

## Scope and authorization

The user requested investigation and a plan, then directed: “aitherdev can be
deployed using vpsfree=cz-configuration, the plan should merge it when it's done
and verified,” followed by “proceed.” The plan names dev-workspace/master,
aither64/vpsfree-cz-workspace/master and vpsfree-cz-configuration/master.
The later “ok” approves preserving deployed extension 39470c6 and including its
workspace pin. All integrations stayed within that scope.

This conversation created the tracking-only initiative with no native lead or
retained roster. No team was invented or borrowed. Implementation remained with
the originating lead; independent review and verification watchers used the
installed catalog policies. The session remains available; no archive or deletion
was requested or performed.

## Delivered revisions

Feature branch in each repository: `2026-11-27-portal-livepatch-repositories`.
Feature worktrees remain under `worktrees/2026-11-27-portal-livepatch-repositories/`.

| Repository/worktree | Final head, proven on remote master |
| --- | --- |
| aither64/dev-workspace / dev-workspace | `066691a37851742bbc47179c32b0077b0b0a016f` |
| aither64/vpsfree-cz-workspace / workspace | `71c5e5fcfdfb9bb1b1fbc38e5a6a17643e77379d` |
| vpsfreecz/vpsfree-cz-configuration / vpsfree-cz-configuration | `0a2ed34c91c7019e89d6d04195f9da31677b1fc4` |

Fresh remote equality was verified after each non-force SSH push on 2026-11-27.
Runtime history has two functional commits; workspace has one runtime and one
extension pin; configuration has one generated pin. No obsolete updates or
migrations remain. The workspace rebase over unrelated tracking-only master
`eaa302627` preserves both reviewed patches exactly. Final comparisons were
captured before integration. Local and remote feature refs are retained.

Repository claims `00a0f65c-31bb-4b73-bef0-85270bc8ab1f`,
`88aa7be0-834e-446c-b63f-4a92eb096af0` and
`ce4d9406-01e8-48e6-8147-7e3ca8c3ecb2` are released. Shared workspace integration
held the tracking lock and proved that unrelated working-tree diffs and the empty
index were preserved. Owned dev-workspace-merge/configuration-merge checkouts
were removed after remote proof and claim release.

## Verification and review

- Focused Go repository/web checks and browser fixture passed. Ruby review-base
  checks passed: 2 runs, 30 assertions. Syntax, formatting and diff checks passed.
- Final-runtime CI [46027037518](https://github.com/aither64/dev-workspace/actions/runs/46027037518),
  attempt 1 at `066691a3`, passed essential application contracts and session
  creation smoke. Extended optional jobs were skipped. The earlier local full
  Ruby/package batch was canceled at a superseded head; it is not a passing result.
- Exact combined application, deployment-contract and cluster-provider-composition
  builds passed. Scoped aitherdev host build passed; no unexpected kernel build.
- Independent reviewer `/root/final_review`, catalog `gpt-6.1-sol/xhigh`, completed
  general, architecture, scope and risk lanes. High risk reflects new private
  selection state and matched deployment. No unresolved Important/Blocking finding.
  Narrow cache identity and readable-HEAD corrections were folded into the owning
  commit and directly regression-tested. The same reviewer accepted the combined
  deployed-extension composition. See [review.md](review.md) and the historical
  [review packet](review-packet.md).
- Accepted Advisory: cold ordinary automatic comparison observation can still
  repeat a slow merge-base lookup. Explicit review bases bypass that path. No
  manifest/lifecycle migration, source ref change or global timeout increase.

Live browser acceptance exited 0 with no page errors. It verified the old durable
comparison pair, core history and totals, refresh, nine-file branch comparison,
rendered CodeMirror source, individual commit comparison, new saved URL reopening,
and independent vpsAdminOS loading. The first harness used Playwright's default
five-second assertion; the diagnostic run exposed an obsolete Monaco selector.
Corrected assertions use the actual CodeMirror content and 30-second budget.
No product correction was needed. Raw logs, report and screenshots remain local.

## Deployment and repair

See [rollout.md](rollout.md) for exact artifacts, administrative recovery and
service continuity. System/profile deployment and its recovery are complete.
Machine claim `19a7b50b-01f4-4719-8e5b-e05fd0b80906` was released at
2026-11-27T16:26:01Z, before browser acceptance and merges, under site policy.
All 13 registrations were validated again before setting the exact ancestor
`1dfea587406b7dd79973831d1677fb2418e5e9aa`; [review-bases.md](review-bases.md)
records per-branch evidence. Linux and linux-bpf correctly have empty comparisons.

## Documentation and handoff

The runtime's README-linked docs/dev-sessions.md documents the CLI, selection
precedence, immutable links and retained state. docs/workspace-portal.md documents
loading, version compatibility and errors. Configuration has only its generated
input update; rollout receipts remain here. [plan.md](plan.md), [design.md](design.md)
and [findings.md](findings.md) retain rationale. Initial tracking commit was
`35be004e2`; delivery records are consolidated into the final checkpoint.

[Repaired Repository tab](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-livepatch-backport-process/?tab=repositories).
Reload an already-open page to load the deployed JavaScript.

[Stable initiative URL](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-27-portal-livepatch-repositories/).
