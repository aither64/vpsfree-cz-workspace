# W: codex-web source and verification evidence

Final source and quick-check milestone accepted by lead at `f78eae3`. Final
independent review and native acceptance remain pending. Exact published source
is clean. The observed pre-existing SQLite startup race is corrected by the
second logical commit; exact-new-head CI passed. This is not a
release-ready conclusion.

## Source and published dependency

- Repo: `git@github.com:aither64/codex-web.git`; remote default `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/codex-web`.
- Feature: `2026-11-08-codex-version-update`.
- Base: `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`.
- Published head: `f78eae3415d20b98503f11e9fe251e3111bfe4da`.
- Complete series: `7e3143bd508153d8c1860b2a916029ee9b8c455b`,
  `codex: add prompted naming compatibility for 0.167`, then
  `f78eae3415d20b98503f11e9fe251e3111bfe4da`,
  `codex: serialize SQLite initialization before connection pragmas`.
- Git tree: `c8b3b64289b92ad5aee213a60eaff257d547aae3`.
- Fresh fetch before push retained the same origin/master; feature descendants
  checked and exact feature/default remote refs verified after SSH push.
- Exact GitHub Nix source: `/nix/store/2y2a7df1yv9aadbb10ykwibx465wb17g-source`;
  narHash `sha256-1QVZzEjeu/cjlcTlGTQyMGIuuPqKZ1YsXtOJV59ZROM=`.
- Go pseudo-version `v0.0.0-20261108230351-f78eae3415d2`;
  sum `h1:aMt3t21u+m0Yf6mHc/O9RG9deTtAuyEZMyZqPlc5f7U=`;
  go.mod sum `h1:z4to20c2m2G4k2YusCQCw3g7z1g63EugO4dmjTgo+dM=`.
  Resolved with `go mod download -json` from a disposable non-module cwd.

Eleven files, +227/-70: catalog refresh helper, new 0.167 prompted provenance,
native ephemeral/state/conditional-steer fixtures, API doc comment, update skill
and reference; SQLite initialization ordering, two regression tests and storage
documentation. No API/policy/receipt-format changes, catalog JSON edits or new
database migrations. The two commits have independent purposes; no obsolete
fixup history or superseded pin streams exist.
This new feature revision has not been merged or deployed. No migration was
introduced, merged, released, deployed or externally consumed by W. Existing
strict 0.163 and prompted 0.164/0.165 selectors/resources remain available.

## Exact candidate and shared schemas

- Codex package `/nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0`;
  native `libexec/codex/bin/codex`, version `codex-cli 0.167.0`, SHA-256
  `13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10`.
- Reconstructed prepared-source receipt:
  `/nix/store/a8rqnjz5jkqnr8fjab07a4bzrd0kid4f-codex-rs`. This incorporates
  llm-agents derivation patches/substitutions; it is not the original fetched
  source or a separately built-source output. R owns its full graph/receipt.
- One generated exact-native experimental schema directory, shared with R/C:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-08-codex-version-update/codex-native-0167/schemas`.
- Config schema SHA-256
  `66ed795352d32f2464778acd2e332b7fafe644246d540cdceec4663c56cfbc16`.
- Full candidate .165/.167 catalog: 539696 bytes, SHA-256
  `1384625c0b6b3e67d3c60da29becea2b017f2c283fc1e2d05b8edafb4698eb10`.
- Canonical strict full fixture unchanged, SHA-256
  `943ca7fe1d19ed019054158303f0dbbd80b3bef43b3aa425a71aa7cb3fb52c2b`.
- Canonical derived Luna unchanged, 62680 bytes, SHA-256
  `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.

## Completed checks

All language checks used the repository Nix environment. Fresh watchers used the
selected installed `/nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0`
catalog digest `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
verification utility Luna/low and explicit full-access policy. Every launched
operation completed with no remaining owned cells or tool sessions.

- Exact-native generation and validation: `nix develop --command bash
  /tmp/codex-w-0167-schema-check.sh`, exit 0, 25 seconds. Script verifies binary
  SHA/version, generates schemas, runs `test/codex_protocol_contract.py` and
  `test/codex_ephemeral_config_contract.py` against the prepared source.
  Full corpus/consumed shapes pass; 55 fixed restrictions and literal MCP
  enabled pass. Log `/tmp/codex-w-0167-schema-check.log`.
- Helper run for 0.167 passes. Disposable copied helper/resources run .165,
  .167 twice: output/provenance reproducible, every historical canonical JSON
  and provenance file unchanged. `git diff --exit-code BASE --` those resources
  also passes. No widened catalog content or invented version-specific bytes.
- `nix develop --command bash /tmp/codex-w-0167-quick-check.sh`, with
  `TMPDIR=/tmp` inside shell: exit 0, 43 seconds; full Go packages pass,
  tagged deterministic fixture helpers/compile pass, browser syntax and all
  109 browser tests pass. Request-corpus coverage-only check passes.
  Log `/tmp/codex-w-0167-quick-retry.log`, SHA-256
  `de94698886b5fedd3194a63cc863efc998ba06d3b7d3ba9f59fe6623aacb163a`.
- Tagged check selector:
  `go test -mod=readonly -tags=codex_integration ./codex -run
  '^(TestEphemeralIntegration|TestPromptedEphemeralIntegrationToolObservation$)'
  -count=1 -timeout=120s`. This excludes native integration entry points.
- `git diff --check` passes. No declared hook framework or active configured
  hooks were found; commit used `nix develop --command git commit -F FILE`
  with no bypass. Source, review and publication remain distinct milestones.

Initial quick batch stopped at unchanged
`TestQueueDeletionResponseLossReconcilesAfterClientRestart`: the Nix TMPDIR
prefix made its Unix socket path 108 bytes. Exact test passed with short TMPDIR,
then corrected full batch passed. Original log
`/tmp/codex-w-0167-quick-check.log`. Existing lessons
`notes/codex-web/2026-10-03-nix-shell-unix-socket-paths.md` and
`notes/codex-web/2026-10-25-go-nix-environment.md` describe the correction.
No product edit or assertion change was made for this environment failure.

## CI startup contention finding

[Check run 42532327561](https://github.com/aither64/codex-web/actions/runs/42532327561),
attempt 1, exact published head, failed its flake job at
`TestConditionalSteerConcurrentClientsShareOneClaim/database=true`,
`conditional_steer_test.go:543`: `database is locked (5) (SQLITE_BUSY)`.
Failed log: `codex-web-ci-42532327561.log` in this session. It was downloaded
before any rerun; no remote rerun was submitted.

Bounded diagnosis authorized by lead, no repository edits:

- Current exact head, focused `nix develop --command env TMPDIR=/tmp go test
  -mod=readonly ./codex -run
  '^TestConditionalSteerConcurrentClientsShareOneClaim/database=true$'
  -count=20 -timeout=60s`: 2/20 failures, 1.299 seconds.
- Disposable git archive of exact base, same command with `-count=30`:
  3/30 failures, 2.110 seconds; `/tmp/cw-w-diag/baseline.log`.
- Temporary Go overlay adding error-stage labels, 4/30 failures. One explicitly
  reports `initial user_version/connection bootstrap: database is locked (5)
  (SQLITE_BUSY)`; `/tmp/cw-w-diag/current-overlay.log`. A broader label overlay
  then passed 20 repetitions, 1.520 seconds, `/tmp/cw-w-diag/current-stage.log`;
  passing nondeterministic repetitions do not establish correctness.
- The fixture starts two clients against a nonexistent database.
  `openSubmissionDatabaseLocked` constructs a lazy SQLite connection with
  busy_timeout, journal_mode(WAL), synchronous(FULL). The driver already sorts
  busy_timeout first. `initializeSubmissionDatabase` first queries user_version,
  triggering connection pragmas, before creating/checking schema and acquiring
  predecessor import flocks. Existing retained DB contention tests preinitialize
  the database; they do not exclude this cold-start path.

All diagnostic commands ended. Baseline archive path is recorded in
`/tmp/cw-w-diag/baseline-path`; overlays/logs remain disposable evidence. No
further pre-fix reproducer runs planned. Lead accepted architect's W1 startup
serialization brief, implemented by the second commit. The original conditional
test's cold setup/assertion remains unchanged; a baseline failure did not excuse
the supported production concurrency defect.

## W1 correction and validation

The same sorted, context-aware predecessor flocks now precede the first SQLite
query and its lazy connection/WAL initialization. Locks remain held through
schema/import/fence completion, then release before ordinary transactions and
network requests. The ready branch uses the existing locked verifier; the
redundant later lock/phase reread and unused wrapper are removed. No new lock,
generic retry, driver/version change, database schema or stored format is added.
Old binaries retain their pre-lock startup race. Recovery remains forward-only.

Exactly three W1 files, +91/-30: `codex/submission_migration.go`,
`codex/submission_database_test.go`, `docs/submission-storage.md`. Existing
WAL/FULL/busy-timeout/max-one-connection, version-0 atomic initialization,
fail-closed version-1 validation, import journals/backups and receipt semantics
remain unchanged. No migration history was rewritten.

- New deterministic first-open regression holds an actual predecessor flock,
  requires bounded cancellation and nil installed store, proves no SQLite
  header/schema/sidecars/fence, releases lock, then proves successful retry.
  Against a temporary overlay of pre-W1 production source it fails with a
  28672-byte database initialized while blocked. Log
  `/tmp/cw-w-diag/pre-w1-regression.log`. Corrected test and cold distinct-attempt
  regression pass (0.249 seconds).
- Fresh watcher ran exactly once: `nix develop --command bash
  /tmp/codex-w1-focused-check.sh`, exit 0, approximately 60.2 seconds, tested
  `7e3143b` plus diff SHA-256
  `e0a70fec70f2706694daf356b7531948d7faee18cad5f2f6409d35890c51cfa7`,
  which became `f78eae3` without intervening edits.
- One bounded `go test -mod=readonly ./codex -run
  '^TestConditionalSteerConcurrentClientsShareOneClaim/database=true$'
  -count=100 -failfast -timeout=120s` passes (6.570 seconds).
- Focused `TestSubmissionDatabase*`, `TestSubmissionAdmission*`, durable
  admission cancellation and conditional-steer cancellation pass (6.552 seconds).
- Ordinary Go suite, tagged deterministic/compile helpers, request-corpus
  coverage, browser syntax and 109 browser tests pass. Earlier exact-native
  schema/config/catalog evidence remains applicable; those inputs did not change.
- Watcher command session 49232 exited 0 with no other running effects. The
  requested original disk log was not created; result/output are retained in
  watcher native thread `/root/w1_check_watcher` tool history and completion
  report. The watcher later wrote `/tmp/codex-w1-focused-check.log`, explicitly
  marked reconstructed/partial with omitted lines, SHA-256
  `475bf90b3c1ac4330b3aebd712bc7a08e9daa8f09c1765276ed21eeb83c846a4`
  (final watcher report and local read; the earlier partial reconstruction had
  a different hash before the watcher completed it).
  It is not a complete original log. This limitation was reported honestly;
  no check was repeated to manufacture a log. Lead accepted retained output.
- Corrected exact-head CI is
  [Check 42533307656](https://github.com/aither64/codex-web/actions/runs/42533307656),
  attempt 1, `f78eae3415d20b98503f11e9fe251e3111bfe4da`: completed success.
  The run completed before a watcher was launched; terminal status was read
  directly. The earlier failed run is terminal and retained as root-cause
  evidence. No unmodified remote rerun was submitted.

## Remaining gates and ownership

### Prepared post-review native batch (not executed)

Pre-gate retention update: a later read found new native `22139ip` and prepared
source `a8rq` absent, consistent with collection. R is the sole owner restoring
and rooting those exact inputs; W does not retrieve/build or duplicate their
roots. Earlier executed schema checks remain recorded at their actual identities.
Do not run the prepared batch until R supplies its restored exact receipt and
lead releases the post-review gate.

R subsequently reports both exact inputs restored and valid. Candidate native
SHA-256 matches `13fc360e...05b10`; prepared `a8rq` was re-added from its original
preserved private reconstruction and reproduced the identical store path.
Patch/config/catalog hashes were reverified, config/catalog equal restored
fetched `j9bh`. R owns verified roots in this session's `gc-roots/`:
`native`, `fetched-source`, `prepared-source`, `llm-source`, `runtime-source`,
`provider-source`. No tests/probe/activation accompanied restoration. Native
execution still requires explicit post-review lead release.

W created indirect session GC roots under `gc-roots-w-native/`, with exact
targets in `gc-roots-w-native/receipt.json`. Registered roots were verified for
the existing old native and assembled package, old llm-agents source and patch,
iproute2, nftables, SQLite and exact reviewed codex-web source/catalog. No absent
input was realized, no retrieval/build or verification suite launched, and all
root operations ended. No roots or session data were removed. One root named
`old-native-drv` was created using the existing derivation; Nix resolves that
command to its output, so the receipt correctly identifies this as a duplicate
old-native output root rather than pretending it directly roots a .drv.
`keep-derivations=true` retains its known derivation. This harmless root remains;
no cleanup was performed. A registration verifier initially expected the .drv
target, stopped after root creation, then inspected and recorded the actual
effect before continuing. `nix-store --query --roots` also reported Nix's
automatic stale indirect-pointer pruning; no explicit collector/lifecycle or
root-removal command was issued.

Ready command from the clean codex-web worktree:

```sh
nix develop --command bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-08-codex-version-update/codex-web-native-0167.sh
```

The session-owned script pins exact head, new binary/hash, reconstructed prepared
source and immutable reviewed-provider Luna catalog. It runs sequentially:
namespace ownership, prompted .167 low, prompted .167 high, conditional steer,
and .165-to-.167 state/readback. A fresh watcher must launch it only after lead
release. Logs: `codex-web-native-0167/01-namespace.log`, `02-prompted-low.log`,
`03-prompted-high.log`, `04-conditional-steer.log`, `05-state-upgrade.log` beneath
this session, plus watcher's combined command/exit receipt. The state fixture
also prints its separate retained private evidence directory; preserve that
path and manifest when it runs. No batch has been launched yet.

Prerequisites are the repository Nix development environment (Go/CGO/compiler),
Linux unprivileged user/network/mount/PID namespaces and private nftables
mount/firewall operations. Exact existing tool executables are recorded in the
script: iproute2 7.0.0, nftables 1.1.6, SQLite 3.53.1. The first ownership test
proves namespace stop/join before native utility runs; no fallback to host
networking or relaxed teardown is allowed. The fixture supplies private homes,
cwd, synthetic unauthenticated providers and explicit subprocess environments.
It never uses a live Codex home, serving daemon or real-provider credentials.

Old exact native is available:
`/nix/store/94pabrw3ff2xy0kg05rgxjch2p1g6ids-codex-0.165.0/libexec/codex/bin/codex`,
SHA-256 `647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652`.
The deployed assembled copy has identical bytes; its public bin/codex is a
wrapper and is not the fixture executable. Old llm-agents source
`/nix/store/6xb99l21zqwilx52r3m1d1797vpa9xdw-source` is available and selects
revision `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`. Actual old derivation
`/nix/store/c1ql1zd4dph4f28wrlx98ilkr1m3v4dg-codex-0.165.0.drv` records fetched
source `/nix/store/j4xcz959sk3k5isb6q29gpyivjym37j9-source` (not currently
realized), daemon-nix-store.patch (available), store/output substitutions,
chatgpt recursion limit 256 and Cargo optimization substitutions. This exact
derivation/native receipt is passed as old provenance; the state fixture consumes
the binary, not old source files. No old source retrieval/build was launched.
If full old-source bytes are required for the final rollout record, retrieve
that exact existing input separately rather than infer a replacement source.

Expected batch duration is roughly 3–6 minutes after environment preparation;
five existing outer test limits total 15 minutes (each 180 seconds), excluding
Go compilation. The state fixture has a 150-second internal context, conditional
steer 60 seconds, namespace readiness/stop and utility calls have their existing
shorter bounds. Those are fixture limits, not authority to extend a failed run.
Stop on the first nonzero check, missing prerequisite, ownership/teardown error,
source/hash/settings mismatch or unresolved command effect; report its exact log
and remaining effects. No automatic retry, constraint weakening or later stage
after failure. An old-reader success is separately recorded cold-read coverage,
never rollback/write/mixed-version approval.

W retains ownership for final review findings and
post-review native checks. Lead owns packet completeness and final review
invocation. No native suites or local packaged long checks have run yet.
After review: namespace ownership control, exact .167 low/high prompted native
selectors, exact conditional-steer acceptance and .165-to-.167 state fixture,
with separate old-reader observations. Retain forward-only recovery and do not
claim tool isolation from prompted checks. R owns real-provider naming and
system/profile acceptance; neither is supplied by fake transports/schema checks.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-codex-version-update/
