# Backend implementation report

Status: backend implementation, coordinator quick checks/prose review and the
two explicitly authorized focused commits are complete. Mandatory review, longer
verification and release gates remain with the coordinator. No push, deployment,
integration or session lifecycle action occurred.

Identity: `dev-session current` matched this session; both environment identity
variables were absent and the trusted thread binding matched. Work is confined
to the initiative's dev-workspace worktree, based on
`924c0ec28c41dd8b56aaf17f2212b302ca614899`. Retained member settings were not
overridden. Lead plan/state/portal metadata and other initiatives were preserved.

## Delivered behavior

- ID-bearing requests durably freeze raw prompt, ordered files, scope, date,
  custom name, submitted setting presence/values, exact resolved team preset
  and input/snapshot digests. Replay precedes current catalog/upload resolution;
  changed input conflicts. Local validation precedes acceptance; initialization
  checks live availability without substituting captured settings.
- Strict private schema-1 preparation admission/status/retry/store, restart
  pause, tracked shutdown and generation checks. Capacity reserves mappings:
  512 unfinished, 10,000 total identities and bounded bytes. Terminal compaction
  precedes receipt retirement; interrupted moves reconcile before collection.
- Async text-only naming boundary, NFD fallback, UTF-8 8192-byte input limit,
  strict bounded JSON output, ten-second budget and two concurrent calls.
  Attachment-only input skips naming; saved names/reservations never change on
  retry. The live adapter belongs to the later helper unit.
- Serialized allocation under creation-then-session locks, occupancy checks,
  automatic suffixes/custom conflicts, bounded Ruby guard and exact supplied
  receipt ID/request/preset/epoch handoff. Other equal-content receipts conflict.
- Pre-slug uploads validate ready files before intent and in the atomic claim.
  Existing schema-1 initial/pending fields carry `preparation:<uuid>` ownership.
  Transactional mutation exclusion and continuous ordinary ownership transfer
  preserve files. Competing old-writer state fails recovery without discarding
  selected bytes or ownership evidence.
- Server-owned validated preparation routes safely render accepted raw text.
  Explicit-name, plan and fork validation remains on its existing path. New
  browser submission/polling/storage wiring is a later unit.

## Changed application files

| Area | Files relative to dev-workspace |
| --- | --- |
| Preparation/naming | `portal/internal/web/{preparation.go,preparation_store.go,session_name.go}`; integration in `{server.go,creation.go,creation_store.go,uploads.go}` |
| Upload ownership | `portal/internal/uploads/store.go` |
| Locks/CLI guard | `portal/internal/session/authority.go`, `libexec/dev-session` |
| Focused tests | `portal/internal/web/preparation_test.go`, `portal/internal/uploads/preparation_test.go`, `test/dev_session/preparation_reservation_test.rb`, registration in `test/dev_session_test.rb` |
| Baseline fixture | `portal/internal/web/preparation_compatibility_test.go`, `test/fixtures/preparation_baseline_test.go`, `test/preparation_compatibility.sh` |
| Lasting docs | `docs/session-preparations.md`, pointer in `docs/workspace-portal.md` |
| Dependency | `portal/go.mod`, `portal/go.sum`: coordinator resolved `golang.org/x/text v0.27.0`; moved into direct requirements for `unicode/norm` |

No existing receipt, manifest, journal, runtime-authority or catalog schema was
extended. Final Nix vendor hash awaits the consolidated dependency pin.

## Verification evidence

This member's prepared-profile invocation was refused:
`cannot connect to socket at '/nix/var/nix/daemon-socket/socket': Operation not
permitted`. Reported to lead; no bypass or ambient Go/Ruby execution.

Coordinator/watcher evidence before final source stabilization:

- Go formatting succeeded. Compile-only probe with `-mod=readonly` passed for
  web/uploads/session in seven seconds; zero tests were intentional, not a
  test-pass claim. The package shell forces vendor mode, so source checks need
  explicit `-mod=readonly`.
- Initial focused tests passed uploads and failed web at the compaction fixture;
  session selected zero tests. Log:
  `/tmp/automatic-session-slugs-backend-focused.log`.
- Failure was fixture setup order: `writeCreationProof` writes the sidecar before
  `saveCreation` had created its directory. Fixed the order; production proof
  requirements were preserved.
- Final coordinator checks passed: Go web/uploads/session (54.769 seconds;
  540 verbose run entries including nested cases), selected Ruby (nine runs,
  133 assertions, no failures/errors/skips; 2.367 seconds). Logs:
  `/tmp/automatic-session-slugs-backend-stable-go.log` and
  `/tmp/automatic-session-slugs-backend-stable-ruby.log`.
  Additional aggregate fork/receipt regressions passed 9 runs/195 assertions
  in 1.314 seconds. Direct fork_receipts_test.rb invocation lacks NullTmux;
  focused Ruby commands below use the aggregate test entry point.
- Coordinator gofmt included the tagged fixture. Ruby libexec syntax, Bash
  fixture-runner syntax and `git diff --check` passed. Main-context prose review
  completed; current coordinator doc edits are preserved.

Final focused inventory: 14 web tests (11 preparation, three naming), four
upload tests and seven Ruby guard tests. Coverage includes blocked nonblocking
admission, setting snapshots, replay before catalog/uploads, conflicts/capacity,
intent/name/reservation/receipt crash gaps, foreign receipt refusal, upload claim
recovery/GC, claims/collisions, CLI refusal and real cross-process creation-lock
contention, generation/shutdown/restart, fallback/output bounds, semaphore
concurrency and actual ten-second queue timeout, mapping bounds/interrupted move.

The exact-baseline fixture exists but has not run. It extracts portal source
from the exact base into disposable files; no serving package is downgraded.
It executes baseline strict reader/collector/Delete/Append/Complete/Create/
Prepare, then requires current HTTP recovery/retry to refuse competing state
and retain bytes and submissions. The ordinary upload test only establishes
current-reader behavior and makes no old-source proof claim.

## Exact suitable commands

Run from the assigned dev-workspace root in the prepared repository-derived
profile. Every test selector names existing nonzero tests. The naming selector
includes a known ten-second budget test.

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c go -C portal test -mod=readonly ./internal/web ./internal/uploads -run '^Test(SessionPreparation|SessionName|PreparationUpload)' -count=1
nix develop /tmp/automatic-session-slugs-runtime-env -c go -C portal test -mod=readonly ./internal/session -run '^TestRuntimeLockUsesHostOnlySessionFile$' -count=1
nix develop /tmp/automatic-session-slugs-runtime-env -c go -C portal test -mod=readonly ./internal/web -run '^Test(Creation|DirectCreation|DirectTeam|BrowserCreation|LoadCreations|CompletedCreation|PendingLegacyVirtualCreation)' -count=1
nix develop /tmp/automatic-session-slugs-runtime-env -c ruby test/dev_session_test.rb --name '/preparation_reservation/'
nix develop /tmp/automatic-session-slugs-runtime-env -c ruby test/dev_session_test.rb --name '/portal_start_persists_receipt_bound|portal_creation_retry/'
nix develop /tmp/automatic-session-slugs-runtime-env -c ruby test/dev_session_test.rb --name '/portal_fork|portal_creation/'
git diff --check
```

After mandatory review, coordinator/watchers can execute the isolated fixture:

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c bash test/preparation_compatibility.sh
```

It selects `TestPreparationCompatibilityFixtureWrite`,
`TestPreparationBaselineFixture`, `TestPreparationCompatibilityFixtureRecover`.
Full package/race/browser/protocol/live checks belong to later orchestration.

## Deviations, gaps and commit proposal

No consequential design deviation selected. The user confirmed model naming
with file/network action tools disabled and immediate question rejection; pure
clock may remain. The architect supplement is finalized. Helper implementation
is outside this unit; exact-binary isolation proof is a later release gate,
not an unresolved preference. Mocks make no literal no-tools claim.

Remaining: mandatory independent review; baseline fixture execution after review;
exhaustive filesystem-write fault injection, race/package regressions,
browser/helper/protocol units, final vendor hash and release checks.
These recovery tests construct durable crash-gap states; they do not claim every
fsync/error boundary was injected.

Completed coordinator-approved focused split:

1. `a90570e5868a033a9978c57bd6476278c03b165b`
   `uploads: reserve initial files for accepted session requests` — transactional claim,
   mutation exclusion, transfer/conflict handling and upload tests.
2. `c5472c4f520e4e92b1fc05bfb3184eb74bc9458b`
   `portal: prepare sessions before choosing their names` — store, naming/API,
   workers, receipt/retry integration, lock helpers, CLI guard, HTTP/naming/Ruby
   tests, dependency, lasting docs and isolated tagged fixture/runner. These
   changes form the durable creation protocol. Final vendor hash remains with
   the consolidated dependency/helper pin.

No declared hook framework; `core.hooksPath` unset and only sample hooks found
in the bare repository. Both commits used temporary message files and
`git commit -F`; no hook bypass. Final application worktree/index was clean at
backend handoff. No migrations or superseded approaches in this two-commit
series. Feature release/readiness is not claimed. The next authorized unit is
the public ephemeral helper/runtime naming adapter, kept outside these commits.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/>

Coordinator consolidated the checked aggregate Ruby entry-point correction in
`test/README.md` into the unpublished portal backend commit. Current head is
`c5472c4f520e4e92b1fc05bfb3184eb74bc9458b`; the earlier unpublished
`8c0d3fc` is superseded, with no separate supported iteration. Previous backend
checks remain applicable because the consolidation changed documentation only.
