# Archive failure: active native watcher rejected as a managed team member

The archive failure is an interaction bug between native descendant shutdown and
managed automatic-retry admission. The watcher was legitimately owned by the
session; it was not supposed to be in the retained team roster.

## Observed sequence

- Portal preparation reported ready: six of six checks, zero blockers, no repair
  turns. Receipt `8ef38791646bb344d6d0880a414e7c9b88f44d72a4f12831ef52ebb06cfc18c7`,
  operation `eee092a6346cbc1e5e2def280080477fc0528fc837eec3a382b0489aa33fb004`.
- Systemd unit `workspace-archive-<receipt>-1.service` started at
  2026-10-28 10:38:17 UTC and exited 1 at 10:38:22 UTC. Its exact stderr was
  `workspace-portal: managed admission is outside the retained team`, from
  `workspace-portal thread quiesce-explicit` for root
  `01a181a7-2ddc-7852-a8c7-56c27709c461`.
- Executor package was
  `/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`, built using
  runtime source `4a002f52c3b55099540aa99708d5fcf29f7b2456` per its rollout record.
- Last held-prompt capture was for `01a1820a-566f-7c31-bbb5-ece2d361a0ee` at
  10:38:22.281 UTC, immediately before the failure. Its native `session_meta`
  names `/root/master_ci_finish` and the exact retained root as parent. Its turn
  started at 10:24:38.183 UTC and completed normally at 11:54:23.740 UTC.
  It was therefore active when archival tried to interrupt it.
- Earlier captures were the root and two completed native watchers,
  `/root/profile_activation_watch` and `/root/master_ci_watch`. All four saved
  queues had zero entries. The retained roster contains architect0, implementer0,
  implementer1, observer0 and reviewer0; none is this native utility.
- The source runs this shutdown before creating the archive cleanup/journal.
  There is no target `.archive.json` or `.archive-cleanup.json`, no tracking-sync
  receipt and no archived tracking directory. Active tracking and five owned
  checkouts remain. A session-recovery hold and browser preparation record remain.

Evidence sources: the named systemd unit journal; private state under
`~/.local/state/dev-workspaces/{portal,session-recovery,archived-prompts,codex-teams}`;
the watcher's native rollout under `~/.codex/sessions/2026/10/28/`; and the affected
session's `state.md`, `portal.yml` and `rollout.md`. Only relevant metadata and
task lifecycle events were extracted; prompt bodies are not copied here.

## Code path and introduction

At runtime revision `4a002f52`:

1. `libexec/dev-session:2066` calls `quiesce_explicit_archive!` before preparing
   the archive journal. The helper at line 9295 stops the managed terminal,
   establishes recovery state, and invokes the Go `quiesce-explicit` command.
2. `portal/cmd/workspace-portal/main.go:1052` stops the root, then calls
   `QuiesceNativeDescendants`. That function in
   `portal/internal/workspacecodex/archive_explicit.go:217` proves ownership using
   native parent links, then calls `QuiesceExplicitArchive` for each descendant.
3. `archive_explicit.go:199` calls `c.Interrupt` only when the child has an active
   turn. Completed utilities never enter the failing branch.
4. `portal/internal/workspacecodex/turn_retry.go:651` wraps interruption in
   `cancelRetryAdmission`; line 550 invokes `retryAdmission`, whose line 103 calls
   `RetryPolicyResolver` before taking the retry-state lock.
5. The configured resolver in `portal/cmd/workspace-portal/main.go:91` permits
   the retained root or a ready, nonretiring roster member. A native watcher
   matches neither, so line 133 returns the observed error.

The interruption wrapper was introduced by commit
`aafaf4195d695c4641ce4f9342d56a1786f237c3` on October 22, titled
`portal: continue new managed failed turns through durable retry admission`.
The observer wording change did not introduce this path. Reusing admission for
cancellation unintentionally narrowed existing archive shutdown authority.

The admission restriction itself is valid for starting/retrying work: the retry
guide explicitly excludes native children from automatic continuation. The bug
is requiring that same authority to stop a proven owned child.

## Why checks missed it

Archive readiness does not exercise interruption of an active descendant. The
focused active-archive tests instantiate `NewWithOptions` without installing the
production `RetryPolicyResolver`, so `retryAdmission` takes its no-resolver path.
The descendant-ordering test also uses pathless metadata and does not exercise
an actual active native turn. The command-level test uses pathless root metadata
and an empty loaded-child list. These tests cover pieces independently, but not
the configured CLI plus an active native utility.

## Recommended correction

Provide an explicit lifecycle interruption path for native descendants whose
ownership has already been proved from the retained root. Keep managed root and
member interruption under retry cancellation and uncertainty reconciliation.
For native utilities, use the established parent-chain proof to authorize stopping
the turn, without requiring membership or granting managed retry authority.

Keep cancellation serialized against managed admission where applicable. Do not
silence all resolver errors, accept any thread sharing a directory, add temporary
watchers to the roster, or broadly bypass retry fencing. Revalidate identities
under the existing lifecycle operation and preserve parent-first interruption,
repeat discovery, child-first retirement, held prompts and paused goals.

Regression coverage should invoke the configured command/client with a real
retained root fixture, roster and active native child. Assert shutdown succeeds,
the child is interrupted before retirement, and its queue is retained. Also
cover a child spawned during shutdown, an unrelated same-directory child that
must remain untouched, managed retry cancellation, uncertain admission refusal,
and resumption after a lost interrupt reply. The new test should fail with the
observed error before the correction.

This should be a runtime-only behavioral correction without a journal/schema
change; implementation must confirm that assumption and retain recovery under
existing package-generation locks. Normal independent review and relevant tests
are required before deployment. Diagnostics should identify the offending child
and shutdown phase instead of reporting only the parent command.

## Recovery recommendation and limits

The watcher completed later, so retrying the ordinary portal archive operation
after fresh validation may now pass this particular branch. This is a workaround,
not prevention. Do not edit the roster, browser receipt or recovery hold to force
completion. No archive retry, agent interruption, source fix or deployment was
performed during this investigation. Another blocker could appear on retry.
