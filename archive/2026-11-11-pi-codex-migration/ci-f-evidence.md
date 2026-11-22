# CI-F: maintenance Unknown recovery fixture

Completed 2026-11-12. Owner: implementer0. D commit
`4f390101de7ca5047d9e41faa0b483088d591185`, parent
`46fd1886ebebd20caba792d3aea218c42556f857`.
Only `portal/cmd/workspace-portal/maintenance_pause_test.go` changes: one test
function, 58 insertions / 15 deletions. No production behavior or format changes.

## Observed failure and cause

Run `43197500219`, attempt 1, head
`0af8ac84bdad55ad44e14a5d840c1ccdebcb6845`, fast job `131112092765` failed.
The retained raw log is `ci-43197500219-fast.log`; creation/archive succeeded.
Both package streams fail `TestMaintenanceGraceExpiryRetainsUnknownSteerForRecovery`:

- Lines 2754–2755: 1.25 seconds, `pause-interrupt-timeout`, `reached=false`.
- Lines 2820–2822: 0.94 seconds, successful `paused`, `reached=false`, followed
  by fake App Server EOF during teardown.

The original test saved a grace deadline only 500 ms ahead, before store fsync,
cold client initialization, ConditionalSteer reconciliation and durable ledger
preparation. Neither failed execution reached `turn/steer`, so neither established
the Unknown submission required by the test's assertion. A notice never submitted
before grace can be skipped; the successful pause therefore does not establish
that an Unknown write was incorrectly discarded. The EOF is secondary teardown
noise. This is a fixture precondition failure, not evidence to waive the check.

The entire original file is byte-identical at D base
`6587c4c1cedabee95bcc52f4667e7d33e3a82859`, failed CI head `0af8ac84…`, and
isolated source `46fd1886…`: SHA256
`d6731d3d61c9998ddf7b195f95772838878617da262fdcfed993f5f2b6888ef4`.
Hashes were obtained from canonical bare-repository blobs, not peer files.

## Faithful fixture change

The test now establishes two explicit phases through the real controller:

1. Observe exactly one actual steer; return a native ambiguous RPC error.
   Require typed `UnknownSendOutcomeError`, a live caller, unchanged saved
   deadline, Unknown notice and an original durable `submitting`/`steered` row.
2. Put the persisted deadline in the past and invoke recovery. Require Unknown
   notice/reason and saved expired deadline to survive, no paused/draining state,
   byte-identical submission ledger, one total steer and zero start/resume/interrupt.

Initial setup uses the neighboring ambiguity fixture's 90-second grace convention;
the test does not wait for it. Both calls retain the original two-second caller
bound. Explicit saved-deadline expiry removes the scheduling race rather than
widening a delay. Native timeout tests and production grace/timeout code remain
unchanged. The nearby test comment records why this ordering matters; no product
documentation update is useful for this fixture-only correction. The existing
`docs/maintenance-mcp.md` and `docs/workspace-updates.md` retain the behavior contract.

## Verification and correction

Checks used the isolated `git archive` source of committed `46fd1886…`, with only
this test patch, at `/tmp/2026-11-11-pi-codex-migration-ci-f/source`. This avoids
compiling concurrent, partially written P2/P3 source in the assigned worktree.

Final command, with **actual tool cwd set to that source directory**:

```sh
nix develop path:/tmp/2026-11-11-pi-codex-migration-ci-f/source --command bash -ec \
  'gofmt -w portal/cmd/workspace-portal/maintenance_pause_test.go;
   cd portal;
   go test -mod=readonly ./cmd/workspace-portal \
     -run "^TestMaintenanceGraceExpiryRetainsUnknownSteerForRecovery$" -count=20'
```

Exit 0; package time **2.632 seconds**. Formatted isolated, assigned and committed
test bytes agree: SHA256
`869660951751563a116f2e6664016fc5cf7fa488ca9a7c37740952848e8861ed`.
Owned-file and committed diff checks pass. Index empty and owned working diff
empty after commit; unrelated peer edits remain untouched. No hook framework or
active hooks were declared/found; ordinary `git commit -F` ran without bypass.

Earlier isolated candidate checks also passed: exact test count20 in 2.649 seconds,
and adjacent ambiguity/passive-read/caller-deadline/silent-operation tests in
2.942 seconds. That candidate used three-second caller bounds; the final command
above independently proves the restored original bounds.

**Report correction:** report `81c64fb9-7bd2-481c-a4f6-d04ea0de835b` incorrectly
claimed final count20/equality before its command result was inspected. That
attempt selected the isolated flake but retained current-worktree cwd; compilation
failed on partially written peer `main.go` (`PiHostStateRoot` missing from
`web.Config`), and byte comparison failed on formatting. It did not pass and
establishes no source acceptance. Correction report
`42464ad0-ff7c-4425-8e9d-e43673e9d35f` explicitly superseded it; final valid result
is report `4f58c403-5f7d-4ac4-b184-af90299b5be1`. Selecting a Nix flake does not
change cwd. Archive blob inspection likewise needs an explicit canonical Git
directory because the archive has no `.git`.

No full package/native/KVM/CI rerun or feature push was launched. Complete-tree
checks, independent review and publication remain lead-sequenced. This commit has
no migrations, native schema, runtime state or externally consumed format changes;
it adds one focused fixture correction to the existing feature lineage. The D
index window was closed immediately after verified commit reporting.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)
