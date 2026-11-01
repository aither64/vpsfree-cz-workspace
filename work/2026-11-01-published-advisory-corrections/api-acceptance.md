# API, client and KB acceptance

Current API `49f5a29e5a7d85559d06d31496acb5c08895bcda` and KB
`5276b64b9cab0d29bc14968730eccf88c230059d` are clean, quick-checked and pushed.
The three-path standalone-form layout correction is folded into B; A is the same
`9415cf28` object. Retained affected review passed with no findings in
`layout-final-review.md`. **Final local acceptance passed:** strict exact-pin KB
exit 0 in 453.13s; real legacy advisory script exit 0 in 1387.69s, all **18
Playwright cases passed**, native `expected_success`. Services/node1 exited 0
and were destroyed; node2 never started and was destroyed. No owned test process,
guest, driver or utility remains. All four project worktrees are clean.

Hosted KB Check passed; API integration remains in progress at the final snapshot.
Managed CI attempt 1 failed in the unchanged fixture precheck; its one diagnosed
job retry is attempt 2, job `125007871097`, queued at the final snapshot. No CI
success is inferred and no waiting/repeated retry is authorized. Compact final
packet: `verification-final.md`. Prior `006454` / `17d06` strict and 11/1/6
browser failure plus all earlier failures remain retained below.

API full/core, complete client and modern results remain retained for their
actual tested inputs with reviewed source/derivation/bundle proofs. Prior strict
fixture, readiness and notification-selector failures remain explicit below.
The affected readiness review and narrow assertion reconciliation passed; no
runtime/guard was relaxed. Current native failure logs were snapshotted, owned
guests exited/destroyed, and the exact runner-path process scan was empty. Guest
trace/screenshot artifacts did not survive; no trace inspection is claimed.

## Completed batch

Fresh Luna/low watcher `01a1988f-3072-7441-81b8-7c4427f988c0`, catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
native utility `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`;
actual launch verified `danger-full-access` / `never`. It owned one sequential
stop-on-failure batch. Total elapsed 3517.70 seconds (58m38s); exit 0, no remaining
operation. No timeout, retries, runner changes or source changes during the batch.

| Check | Exact head | Result | Wall time |
| --- | --- | --- | --- |
| Full-plugin advisory model/concurrency/resource/outage specs | `c8efabeb01ccca66b19425ee429e834d23cf3688` | 88 examples, 0 failures, 0 pending | 1152.87s |
| Core advisory model/concurrency/resource specs | same | 79 examples, 0 failures, 0 pending | 939.73s |
| Complete client RSpec | `0b771120bb2a878c012512b685208124c2b4263b` | 298 examples, 0 failures, 0 pending | 914.40s |
| Strict pinned `nix develop -c bin/check` | `beeb258c72f84105b73b75fc4837e18b87e81cf2` | exit 0 | 477.09s |

Commands are the exact released commands in `verification-brief.md`, with
documentation/native JSON formatters added for RSpec evidence. The full/core
API commands selected three shared files and the full-only outage plugin file.
There was no mutable KB source override or `--allow-missing`.

Both API runs used automatic isolated temporary MariaDB 11.4.12,
`tx_isolation=REPEATABLE-READ`, `innodb_snapshot_isolation=0`; external
`DATABASE_URL` and configured database.yml were rejected before launch. Ruby
3.4.9, Bundler 4.0.23, RSpec 3.13.6, HaveAPI 0.32.1. Effective generated lock
hashes: full `c800cb1e88ed4375cb90049aa84f9f0bca65d36bfe54b9dc331dfed1154419a0`,
core `9ff97d9b998c7169302cf28f08c0bb3ef814dac660eec526ca7caec2d2200e05`.
Named nested-transaction rollback, published/retracted membership and concurrent
writer/delete tests ran successfully; the earlier CI defects were not waived.

Raw evidence lives in
`/tmp/2026-11-01-published-advisory-corrections-acceptance/`: `batch-status.json`,
`batch.py`, `watcher-result.md`, native RSpec results/environment JSON, per-step
logs, flake metadata and shell derivation receipts. API source store path is
`/nix/store/vj9xg1b9rslrfbmf2kdi47pg4ryipiz8-source`; API shell derivation is
`/nix/store/j3x5dlqj8cgrmwffbbh23mw8c2d88g88-vpsadmin-api.drv`.
Full actual derivation JSON is `api-original-shell-derivation.json`; all three
source/input graphs, trees and flake lock hashes are retained in that directory.

Duration expectation was revised from rough minutes to tens of minutes after
the lead supplied measured prior core RSpec duration 11m33s. The actual local
HTTP-heavy full/core/client sequence took about 50 minutes plus strict KB.

## Exact current-head CI defect

API workflow `41340446069`, head `c8ef`, full/foundation job `124949441559`:
1460 examples, 1 failure, 3 existing pending, seed 23310. Sole failure is
`spec/api/endpoint_coverage_spec.rb[1:1:1]`: the unchanged strict inventory
reports missing `security_advisory#delete` and `security_advisory#retract`.
These intended actions already have executed resource specs. All other 25 matrix
jobs passed, including both platform-operations modes and full plugins.

Aggregate job `124960583443` found 13 manifests and all 417 eligible paths in each
mode, but correctly failed because the full matrix failed. It is not a topic
partition defect. Retained exact failed logs, manifest, native result and
environment artifacts are `ci-full-foundation-*` and
`ci-topic-aggregate-failed.log` in the acceptance directory. No old-job rerun.

The lead accepted adding exactly two entries to
`api/spec/api/covered_endpoints.yml`, without changing runtime, pending rules,
coverage assertions or public behavior. Patch prepared outside the worktree
until the complete existing client/KB batch reached its safe boundary. Final
focused endpoint check, A fold/B replay, pin refresh, input comparison and strict
KB verification will be appended here.

## Accepted bookkeeping successor

Final API range:
`097226b22edf8b59f80b5dfaa55265e9d0cac633..4cf556e56b522722db18ebf1f1bb5859523e8b4c`.
Complete series is A `03dd433f3fa97c3129283b10c8df1df1378f3719`, followed by B
`4cf556e56b522722db18ebf1f1bb5859523e8b4c`. The entire old `c8ef` to new `4cf`
diff is two covered-inventory entries. B's binary patch is byte-identical;
range-diff and an alternate-index reconstruction prove final tree
`413a8a9198823576efe46b16690e7432c35a7248`. Normal Nix-root amendment hooks
passed, including both locale health checks and RuboCop. No migrations, obsolete
fixup or added dependency stream. Old tested head remains reachable via
`2026-11-01-published-advisory-corrections-runtime-verified`.

Focused full-plugin `spec/api/endpoint_coverage_spec.rb` passed: one example,
zero failures/pending; YAML parsed. The fresh exact verification operation took
66.16s. An earlier tooling-only attempt stopped before this test because mixed
Nix warning/JSON output reached the temporary evidence parser. Separating stderr
fixed that parser; initial evidence is retained and no application behavior was
changed. Fold/replay took 67.74s. An ambient-shell push hook rejected its signature;
the remote stayed unchanged. Retrying in the required repository root Nix shell
passed normally without hook bypass or signature/source modification.

Both fresh targets were unchanged (`097226b` API, `ce2c8cd` KB). SSH feature
lease-push and independent `ls-remote` proved the exact final heads. No default
branch was changed. Comparison snapshots were refreshed.

### Runtime evidence reuse

The 88/79-example API results above were actually executed at `c8ef`, not `4cf`.
The lead directly inspected and accepted carrying them forward after comparing:

- Complete tracked blob/mode graph except the sole changed inventory file:
  identical; all loaded runtime, spec and DB helper files are unchanged.
- Actual original/final parsed shell derivation JSON: byte-identical, including
  builder, source inputs and dependency derivations; SHA256
  `30d5a1bd662c539f4e091713b4d9ab2ab35b32095622d2c350cab8690de2bd2d`.
- Entire locked dependency graph: identical. Final source store path changes to
  `/nix/store/l803b595ypvhclfsq4miya6ssm15dyk9-source` as expected for the metadata
  edit; this is not a claim of whole-tree/source-store equality.
- Actual full/core Ruby, Bundler, RSpec, HaveAPI and generated effective-lock
  environment JSON: equal in each mode to the corresponding successful run.

`api-verification-reuse.json` binds these comparisons, actual tested and successor
heads, graph digest and environment values. The new inventory consumer itself ran
freshly. Lead reconciliation is in `review-reconciliation.md`; no broad reviewer
or unchanged API/client/modern suite was repeated.

### Final KB pin

Final KB range:
`ce2c8cd9358c3636e5d39343e595df813a0b197f..41097bd4cd973ecaa185905114e481aed5c3c536`.
Exactly one consolidated pin commit, five files, +8/-8. All five locations select
API `4cf556e56b522722db18ebf1f1bb5859523e8b4c`. Selected NAR hash is
`sha256-ca7p76i4HFwFhFotsilOFYD1NCWA1dMG33O5JUzFRBk=`.
JSON/YAML/Nix parsing and full lock-graph checks passed. Other nodes, root follows,
the explicit OS `6bdf458fd9105379860234ff33d352e55844f08f`, capture provenance,
assets and pages are preserved. No declared hook framework is bypassed.

Original `beeb` strict PASS remains recorded for its actual pin. Final strict
check is required and running on `41097`, followed only after success by
`./test-runner.sh test 'webui#security-advisories'` on `4cf`. Fresh Luna/low watcher
`01a198ce-4270-7e53-849a-8d2cd7daa213`, explicit verified full-access/never policy,
owns the operation. Status/logs are `final-acceptance-status.json`,
`kb-final-strict.log`, and `legacy-browser.log` in the acceptance directory.
Final KB derivation is
`/nix/store/kz6amvjs94kjwrr617f52l22glv6cxa3-nix-shell.drv`; actual JSON/input graph
is retained. Stop first failure, no generic quiet timeout; unexpected local kernel
build escalates and stops the exact owned operation.

New API CI: API Specs `41346942447`, integration `41346942509`, i18n
`41346942403`, RuboCop `41346942651`, PHP `41346942412`. New KB Check
`41347050630`, Managed runtime `41347050757`. Superseded own-head integration
`41340446005` and KB Managed `41340595741` were selected for cancellation only
after final feature pushes. Current runs remain untouched. No new CI success is
claimed from merely queued/running status.

## Final strict KB fixture failure and owned-process reconciliation

First final run on `41097`/`4cf` exited 1 after 71.69s, before legacy started.
The 34-test `tools/test-machine.rb` suite had one failure, seed 47448:
`RunnerSessionTest#test_first_valid_stop_notifies_once_when_its_acknowledgement_hits_a_closed_client`
at line 1025, `Expected false to be truthy`. The primary assertion immediately
follows `Process.spawn` and `ProcessIdentity.read(pid)`; the readiness wait is
after it. The helper reads `/proc` stat/executable/argv separately. Later native
observation of the surviving runner showed the expected executable and every
launch option. Source and observation support a startup/exec snapshot race;
the original failing tuple was not retained, so its individual mismatching field
cannot be reconstructed.

Cleanup uses that original tuple to decide whether to send TERM. It skipped the
signal and then timed out waiting for an acknowledgement drain that had never
started. Retained first evidence showed `complete=false`, `gone=false`, phase
`starting`, one claim and a control socket. The watcher's initial claim that no
operation remained was therefore corrected, not accepted.

Only the exact owned synthetic runner was reconciled: PID 3144022/start ticks
16708641, run `67f9d2f9-243e-4b28-ac8e-9868891311ed`, instance
`4725a7a2-5225-46ce-abbb-53071f30bb90`, artifact
`3485536a-2bc7-45e4-a58a-00f33d9bbc4b`, with direct child PID 3144077/start
16708665. A fresh complete native identity and parent-child check preceded
pidfd-bound SIGTERM. Exit was observed; both runner and child are now absent.
This was native disposal of a failed synthetic fixture, with no session lifecycle
action or other-session resource access.

The fixture, `cluster/lib/kb_process.rb`, `cluster/lib/devcluster_runner.rb` and
`bin/check` blobs are byte-identical at recorded base `ce2c8cd`, earlier strict
PASS `beeb`, and final `41097`. The five pin files are the only branch changes.
No runtime, fixture, inventory guard or test command was changed. The lead
authorized one fresh strict check after diagnosis/reconciliation, retaining the
first failure and stopping on any further actual failure. The new watcher owns
`final-acceptance-retry.py`; `final-retry-acceptance-status.json` and
`kb-final-retry-strict.log` are its separate evidence. Legacy remains conditional
on strict success. Original failure, raw fixture evidence and native process
tuples remain in `kb-final-strict.log`, `kb-first-failure/` and
`orphan-fixture-reconciliation.json`.

The authorized unchanged-head strict retry PASSED, exit 0, 557.2s (9m17s), on
KB `41097bd4cd973ecaa185905114e481aed5c3c536` selecting API
`4cf556e56b522722db18ebf1f1bb5859523e8b4c`. No fixture/runtime/test guard was
changed, and the first failure is retained above. Fresh watcher
`01a198d2-6ea9-74b2-bf9a-15f9da685262` then captured the declared legacy runner
derivation (exit 0, 4.3s) and launched the released legacy advisory command in
the same operation. At the checkpoint, legacy was active for 184.8s; its inner
build/browser phase was unavailable from the compact runner status, so no phase
or success claim was inferred. Complete result/native runner receipts follow on
completion. No duplicate raw-log monitor or additional utility was launched.

Final API CI `41346942447` on `4cf` completed SUCCESS: all 26 full/core topic
jobs and the coverage aggregate passed (27/27). This verifies the two missing
inventory entries on the successor source; the original failed `c8ef` workflow
and diagnosis remain retained. Snapshot is `ci-final-current-api.json`. Final
KB hosted Check `41347050630` also passed; its Managed runtime job was still
running at this snapshot. The successful integration workflow `41346942509`
skipped actual tests for the manifest-only push, so it is not browser acceptance.

## Legacy readiness failure and committed successor

The legacy command on `4cf` exited 1 in 1365.02s. Native run
`/tmp/os-test-runner/os-test-webui-fd1a3b33` records one failed script before
Playwright: healthy API HTML uses `API versions`, but the unchanged readiness
helper waited for `API description`. No browser example count is claimed; the
watcher's unrelated 1460-RSpec-example statement is discarded. Services and node1
both record native `qemu_exit` status 0 and `destroy`; node2 never started and was
destroyed. No process refers to the exact owned run directory. Exact VM/runner
inputs are in `legacy-first-inputs.json`, full native logs remain in the run
directory, and the API journal is `legacy-api-journal.log`.

The lead accepted changing only the existing readiness observation to stable
root OPTIONS JSON `?describe=versions`, preserving deadline/curl errors/caller
interface and continuing to wait on malformed/error responses. Final API head is
`0111e97768982701a30634c2277c1c364230067a` (A `9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8`
plus byte-equal B); final KB pin head is
`fd9267bf43009a567e4b958aaec296bf0a60a8ee`. Both are clean, feature lease-pushed
and SSH-proven on unchanged targets. Full history/tree, exact helper diff,
meaningful focused quick checks, API input reuse proof and five-pin graph checks
are in `readiness-review.md` and `acceptance/readiness/` artifacts. No runtime,
public API, migration or prose change. The retained affected review is requested;
no longer check has run on these successor inputs yet.

New exact-head CI identities: API Specs `41351014848`, integration `41351014860`,
RuboCop `41351014858`, i18n `41351014847`, PHP `41351014871`; KB Check
`41351185161`, Managed runtime `41351185245`. These were listed without waiting.
Only superseded own-head KB Managed `41347050757` was selected for cancellation;
current runs remain untouched. All older failed/passed receipts retain their
actual tested heads.

## Reviewed final verification release

The retained reviewer independently accepted the final `097..0111` and
`ce2..fd9267` ranges, protocol/deadline/caller behavior, source/shell/lock
equivalence and complete consolidated histories, with NO findings and NO
MIGRATIONS. Full report: `readiness-final-review.md`.

Lead released a fresh related batch on exact API
`0111e97768982701a30634c2277c1c364230067a` and KB
`fd9267bf43009a567e4b958aaec296bf0a60a8ee`. Fresh Luna/low watcher
`01a198fd-e375-7661-a686-e6ee73b840f5`, actual verified full-access/never policy,
owns strict `nix develop -c bin/check` followed only on success by the single
real legacy advisory script. Separate evidence is under
`acceptance/reviewed-final/` in the existing temporary artifact root. Earlier
fixture and readiness failures remain intact. No unchanged API/client/modern
long suite is repeated. Compact watcher-owned milestones expose observed phases
without a second raw-log observer.

Final exact-pin strict KB PASSED on `fd9267` selecting `0111`, exit 0 in
456.7s (7m37s). Declared runner derivation capture passed in 3.0s; the same
watcher then started the legacy command, active for 254s at the compact-status
checkpoint. No inner build/VM/browser phase or browser success was inferred from
this status. Native current-run result/cleanup/count evidence remains pending.

The final batch then completed: strict PASS 456.69s; legacy runner derivation
PASS 2.95s; actual legacy command FAILED in 1040.94s (total batch 1500.65s).
Playwright reported 7 passed, 1 failed, 10 did not run. First failure was
`publishes with mail disabled and editable published time`, at spec line 376,
waiting for `Update failed` inside `content(stalePage)`.

Source diagnosis: `content()` targets `#content-in`, while the actual template
renders notifications in sibling `#perex` (`webui/template/template.html:161`).
The spec already imports and uses `expectNotification`, which targets `#perex`.
The three new assertions at lines 376, 380 and 417 use the wrong region. The
proposed bounded correction replaces those calls with the existing notification
helper and preserves all expected-state/revision and repeat-submission checks.
No API/runtime failure is inferred from this assertion failure, and no retry
was launched before diagnosis/ownership coordination.

Current native output uses the deterministic directory
`/tmp/os-test-runner/os-test-webui-fd1a3b33`; its latest 13 files were copied to
`reviewed-final/native-failure/` before any later attempt. Prior readiness-failure
wrapper/API-journal/input receipts remain separate; the native directory itself
was reused by the runner. Playwright screenshot/trace paths printed by the
watcher were inside the guest's `/tmp`, absent on the host after destruction;
no screenshot/trace inspection is claimed. The native log retains the received
DOM diff and error context. Final test definition was
`/nix/store/q3qp6mw0dr4g77mczgf1dbk9m7p50h1a-os-test-vpsadmin-webui.json`.

Native services and node1 logs both prove `qemu_exit` status 0 and `destroy`;
node2 never started and was destroyed. No process references the exact owned
run directory. Watcher ended, no local operation/guest remains. The source heads
are still clean `0111` / `fd9267`. Current-head API CI succeeded 27/27; later
CI snapshots remain separate from this failed real browser acceptance.

## Three-assertion successor

Implementer1 delivered the frozen spec-only correction using existing
`expectNotification` for the three `Update failed` assertions, retaining all
revision/state/repeat-submit assertions. Pinned-shell node syntax and exact
three-replacement/whitespace/runtime-hash checks passed. Implementer0 inspected
the exact diff, amended B with normal hooks (64.41s), and lease-pushed the final
feature head:

- API `006454821ee35b291def4bfafee19cd0553bc7b2`, with A unchanged as exact object
  `9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8` on base `097226b`.
- KB `17d06c8bcd5a645601898316acf722708c6defc8`, one five-pin commit on base
  `ce2c8cd`, selecting that API head.

The entire `0111..006454` diff is three assertion replacements, with expected
tree `c8c6e8056e513f52894e60afc0b726c43814555e` reconstructed independently.
API, WebUI runtime and test-runner subtrees are unchanged. Actual API shell
derivation and locked dependency graph are equal; previous effective bundle and
runtime-test evidence remain bound to their actual observed/tested heads.
`acceptance/notification/reuse.json` and exact delta/range/fold receipts preserve
this proof. No migration or product/public-contract change.

D regenerated only its selected input, with JSON/YAML/Nix/full graph checks
passing and all other nodes/follows/OS/capture/page provenance preserved.
Both final heads are clean, SSH lease-pushed and remotely proven; fresh targets
were unchanged. Previous reviewed heads remain under `-pre-notification` refs.
No optional artifact hook or diagnostics framework was added: the lead kept the
successor limited to three lines. The guest-artifact limitation remains explicit.
Current native logs, DOM error, template and existing helper establish this
failure's diagnosis. Longer checks await direct narrow successor inspection.

Lead direct narrow inspection accepted the complete `0111..006454` three-line
delta, unchanged A/two-commit history, actual notification/content/template
owners and `fd9267..17d06` pin graph. Reconciliation is in
`review-reconciliation.md`; no new boundary or migration requires broad review.
Fresh Luna/low watcher `01a1991e-039a-7a52-8f47-9a961105014b`, actual verified
full-access/never, now owns strict final KB `17d06` followed only on PASS by the
real legacy script on `006454`. Evidence is separate under
`acceptance/notification-final/`; earlier first failures remain unchanged.

Initial exact-head CI snapshot: API PHP `41354378274` and i18n `41354378266`
passed, integration `41354378361` running; no new API specs/RuboCop run selected
for this spec-only delta. Exact successful `0111` matrix and proven identical
API inputs are retained honestly. KB Check `41354478819` running, Managed
`41354478820` queued. Complete same-branch inventories (33 API, 14 KB runs)
found zero superseded active runs. Old `0111` integration and `fd9267` Managed
runs are confirmed completed/cancelled; current runs are untouched. No CI wait
or manufactured rerun.

## Strict final process-discovery fixture failure

The released `006454` / `17d06` batch stopped at its first command, strict
`nix develop -c bin/check`, exit 1 in 50.48s. No legacy build, guest or browser
started. `tools/test-runtime.rb` reported 101 runs, 1252 assertions, one failure,
seed 7086:
`ProcessDiscoveryTest#test_workers_at_each_level_discover_exact_child_identities_without_threads_or_siblings`
at line 373, `Expected true to not be truthy` for `observation[:incomplete]`.

The preceding exact child-identity and collected-record assertions passed.
The fixture handshakes its nested worker after spawning a grandchild, without
waiting for every process's native task set to settle. The unchanged discovery
helper correctly marks a pass incomplete if a listed task disappears or its
task set changes. The failure path is consistent with startup task churn; no
original task IDs were retained, so the individual changing task cannot be
reconstructed. This is an observed failing fixture, not a passed strict check.

`tools/test-runtime.rb`, `cluster/lib/kb_process.rb` and `bin/check` blobs are
byte-identical at base `ce2`, prior strict-PASS `fd9267`, and final `17d06`.
The branch still changes only five source pins. No process-discovery runtime,
guard, fixture, timeout or source correction was made. Fixture ensures close
the root input and reap its root, nested children and unrelated sibling; there
was no cleanup warning or matching owned operation remaining. No guest started.

First evidence is separate in `acceptance/notification-final/`: `status.json`,
`kb-strict.log`, `console.log` and watcher result. The lead received source and
assertion-path diagnosis plus its observation limit. No blind rerun, optional
runtime repair or weaker check was attempted; the next bounded diagnostic/check
disposition remains with the lead.

The lead accepted the explanation as supported timing evidence, not proof of
the original changing TID, and authorized one fresh related operation on unchanged
heads: only the failed method with seed 7086, then only on PASS strict `17d06`,
then only on PASS legacy `006454`. No instrumentation, runtime/fixture source,
inventory guard or timeout change is allowed. The fresh watcher owns this
sequence in `acceptance/notification-diagnosed/`; a focused or strict failure
stops it without another retry. Prior failures remain separate.

The authorized unchanged focused method PASSED with seed 7086: one run,
17 assertions, zero failures/errors/skips, 2.5s including Nix setup. Strict
final KB then PASSED on `17d06` selecting `006454`, exit 0 in 484.2s (8m04s).
No source, fixture, helper, inventory guard or timeout changed. The same watcher
`01a19921-1a3f-7062-b390-8f02989e8dc9` captured the runner derivation (PASS 3.2s)
and started the legacy command, active 75s at its compact-status checkpoint.
Original failing observations remain explicit; this success does not reconstruct
their missing task IDs. Final native browser/cleanup evidence follows.

The subsequent legacy run on unchanged `006454` failed in 1257.39s. Actual
Playwright counts are **11 passed, 1 failed, 6 did not run**. The three corrected
notification assertions passed; the workflow advanced to `adds and removes
published node membership only when explicitly selected`. At spec line 478,
`node_101_add.check()` found a visible/enabled/stable checkbox, but the sidebar's
helpbox Edit link repeatedly intercepted pointer events. No force click, hidden
sidebar or increased timeout was used. This is actual pointer-action/layout
evidence; the product correction remains with the B owner under lead assessment.

Current native output was again copied into a separate
`notification-diagnosed/native-failure/` snapshot (13 files), retaining full
call log and received DOM. The printed trace/screenshot paths were guest `/tmp`
and absent after cleanup, as already documented. Services and node1 both record
`qemu_exit` status 0 and `destroy`, node2 never started and was destroyed. The
watcher exited; no retry or overlapping source edit was made. Lead assigned
implementer1 the bounded layout diagnosis and received the evidence handoff;
implementer0 retains sole Git/A/D and final verification. No further suite or
utility is released while that candidate is assessed.

The lead accepted the bounded product candidate: stable name only on the
standalone node form and scoped max-width/horizontal overflow in the existing
stylesheet, preserving all columns, input sizes, payload/guards and sidebar.
Implementer1 owns form/CSS and an existing-case form-bound regression plus
focused PHP/CSS checks, then freezes its handoff. Implementer0 retains serialized
B amendment (A exact unchanged), one D pin stream and final checks. This is a
runtime layout change, so the committed quick-checked successor needs retained
affected independent review before strict final KB/legacy retry. No force click,
sidebar hiding, generic CSS, optional collector or new framework is accepted.

Layout source/quick handoff is complete and committed. API final B is
`49f5a29e5a7d85559d06d31496acb5c08895bcda`, A exact unchanged
`9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8`; final tree
`0ac9a9144e394a8c963db71a49d059e48ebec23c` reconstructs the accepted three-file
patch on `006454`. Normal hooks passed in 65.52s. D is one consolidated pin
commit `5276b64b9cab0d29bc14968730eccf88c230059d`, selecting exact API head with
five files/+8/-8 and all unrelated graph/provenance preserved. Both feature
lease-pushes and remote proofs succeeded on unchanged targets; old reviewed/tested
heads remain under `-pre-layout` refs. Final comparison snapshots refreshed.

Full affected packet, synthetic geometry/image, quick/proof paths and explicit
runtime verification limits are in `layout-review.md` and `legacy-layout.md`.
Independent review is requested before any longer check. New CI identities:
API integration `41358612359`, PHP `41358612246`, i18n `41358612247`; KB Check
`41358727268`, Managed `41358727216`. Only superseded own-head integration
`41354378361` and Managed `41354478820` were selected for cancellation after the
pushes. Current runs are untouched; no CI wait/relaunch. No local operation or
utility remains at this review checkpoint.

Retained reviewer completed `layout-final-review.md` with NO findings, assessing
actual form/CSS/callers, native/synthetic evidence, full history/input/pin proof
and NO MIGRATIONS. Lead released one fresh related operation on exact API
`49f5a29e5a7d85559d06d31496acb5c08895bcda` and KB
`5276b64b9cab0d29bc14968730eccf88c230059d`. Fresh Luna/low watcher
`01a1994d-da96-76c1-88c7-ebb7d4f75a5a`, explicit verified full-access/never,
owns strict KB followed only on PASS by the real legacy script. Separate evidence
is `acceptance/layout-final/`; previous failures and artifact limits remain.
No unchanged API/client/modern suite, optional collector or forced interaction.

Exact final KB Managed CI `41358727216`, job `125004296897`, failed before
managed VM tests in its repository precheck `nix develop -c bin/check
--allow-missing`. The unchanged acknowledgement-loss fixture failed at
`tools/test-machine.rb:1025` (seed 8022; 34 runs, 1192 assertions, one failure),
with the same secondary cleanup timeout at line 1117. Runtime (101/1263) and
closure (19/150) suites passed first. This matches the earlier diagnosed immediate
post-spawn identity snapshot failure; source/helper bytes remain unchanged.
The full exact failed-job log is `layout-final/ci-kb-managed-failed.log`.
Artifact API returned zero artifacts; the logged runner `/tmp` JSON path/hash is
retained but the JSON itself is not downloadable. No remote process inspection
or mutation, source fix or CI rerun was attempted. This is an explicit failed CI
precheck, not successful managed-runtime coverage; local strict/legacy evidence
remains a separate operation.

Local strict exact-pin KB on `5276` selecting `49f5` PASSED, exit 0 in 453.1s
(7m33s), with no fixture/guard/source change. The same watcher captured the
declared runner derivation (PASS 3.2s) and started legacy acceptance, active 55s
at the compact-status checkpoint. Failed Managed CI precheck remains explicit;
this local pass does not claim managed VM coverage or reconstruct the missing
original identity snapshot. Current real browser/native cleanup result follows.

After inspecting the exact retained failed log, the lead authorized one retry
of only Managed job `125004296897`. Immediately before submission, run
`41358727216` and that job both proved attempt 1 completed/failure on exact
`5276`, with no newer retry. GitHub job-rerun API returned HTTP 201 Created.
One immediate metadata acknowledgement proves the same run is now attempt 2,
head unchanged, queued at `2026-11-01T23:00:12Z`. Before/job/ack/after JSON and
HTTP response are in `layout-final/managed-*-rerun*` artifacts. Attempt 1 remains
failed; no managed VM coverage or retry success is claimed. No CI wait, observer,
repeated retry, source/workflow or remote-process mutation. The local legacy
operation continues unchanged. A later repeated CI failure must remain explicit.

## Final local result and cleanup

The released final batch PASSED on exact `49f5` / `5276`, exit 0 in 1844.06s:
strict KB 453.13s, runner derivation 3.18s, legacy advisory command 1387.69s.
Actual current Playwright output reports **18 passed (10.0m)**, including the
remaining membership, retired-row removal, timestamp/CVE and retract/delete
flows. Native result is `expected_success`; one script/one native example passed.
No prior partial count is substituted for this final execution.

Native definition:
`/nix/store/qby9fzk9y3021xb00nzkah8yc7v2062h-os-test-vpsadmin-webui.json`.
Runner derivation:
`/nix/store/88cifs3zcrd25xqx63h3k5ackdcjdpiw-test-runner.drv`.
Complete guest closures, derivations, kernels and definition hash are retained in
`layout-final/native-inputs-cleanup.json`; all 13 native files were snapshotted
to `layout-final/native-final/`. Services and node1 logs prove QEMU exit status 0
and destroy. Node2 never started and was destroyed. Final native process scan
found no owned runner/QEMU/virtiofs/Ruby/Python process. The watcher's inability
to locate destroy confirmation was reconciled by direct native-log inspection.
Guest trace/screenshot absence remains the recorded limitation; native complete
counts and logs establish this final pass.

Final source/branch/status JSON proves all four project worktrees clean at their
exact submitted heads; API and KB remote heads were independently reverified.
Same-branch inventories contain zero superseded active runs. Final CI snapshot:
49f5 PHP/i18n and 5276 KB Check passed, API integration `41358612359` in progress;
Managed run `41358727216` attempt 2 / job `125007871097` queued. Attempt 1's failure
and missing artifact/original-tuple limitations remain explicit. No further tests,
CI wait, retry, source/head, default-integration, deployment or lifecycle change.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
