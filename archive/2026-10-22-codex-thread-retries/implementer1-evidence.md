# Final exact-head CI reconciliation (one query per run)

CI run39832302919 attempt1 at final
`d819ad044ef7fcc7bb4a111dc7676fe251383249` completed **success**.
Creation120011312545, fast120011313037 and archive120011313196 all completed
success. Host120011445577 completed skipped; this is distinct from the lead's
separately owned ongoing local VM check. Source remains clean at tree
`6f1f05da60b09743d3716eb1a0adf794b90cf5a3` and frozen.

[One-shot final metadata](implementer1-d819-ci-final-once.json),
[superseded metadata](implementer1-b695-ci-superseded-once.json) and
[reconciliation receipt](implementer1-final-ci-reconciliation.json) preserve
exact jobs/statuses/hashes. Superseded b695 run39831251707 still reported
in_progress, despite its listed jobs completed. A single policy-required
cancellation attempt was again rejected HTTP403 by the token; prior rejection
is preserved, no credential workaround attempted. No current-head cancellation,
CI poll/wait/rerun, source edit/test/build/native run or watcher-log inspection.

---

# Package B final correction receipt (published d819)

Current source is `d819ad044ef7fcc7bb4a111dc7676fe251383249`, clean tree
`6f1f05da60b09743d3716eb1a0adf794b90cf5a3`, SSH published and direct remote
verified. Fresh upstream base remains `bf6d4b0c49600c15e17fe71248807ef43424e932`.
Source and refs are now frozen for lead-coordinated affected final review.
No native rerun, long suite, build, C pin, claim, merge, deployment or lifecycle
operation was performed. C remains frozen3f. This is source completion and quick
verification; whole native acceptance remains failed/incomplete.

The [final structured receipt](implementer1-d819-final-receipt.json) records
all four commits, exact trees, A metadata, checks, case manifest and artifact
hashes. The original core and capability commits are unchanged. Runtime test/docs
corrections are folded into the owning runtime commit; the final A c1f pin remains
one isolated commit with a cmp-identical patch to b695's pin. There are no database
migrations or production/core/schema/API changes from731. Final private schema1
and capability1 still require nonzero epochs and UUID-keyed charges, reject
preliminary shapes, and have no externally consumed predecessor.

## Run3b diagnosis and fixture corrections

The corrected-CWD batch at731 [failed](native-verification/run-3b-731bb742/result.md):
LiveSwitchReconnect passed, TurnRetryController failed constructing its retained
portal with `http://fixture.local` while product validation requires HTTPS.
Its actual trace established loaded `systemError` capacity failure, one genuine
automatic acceptance, exact schema3 submitting ledger and completed continuation.
It did not reach retained resolver recovery or optout assertions. These remain
unproved until a fresh lead-owned utility native campaign after final review.
Original run3 launch failure and all run1/run2/run3b evidence are retained.

The test fixture now configures HTTPS. Its non-native actual constructor
regression also exposed missing private transition.lock and inherited host
provider catalog setup; it creates a private0600 lock and uses the established
absent-catalog fixture isolation. No product HTTPS/lock/provider check is weakened.
Both initial focused failures and corrected race passes are preserved in the
[initial](implementer1-run3-first-focused.log),
[neighbor race](implementer1-run3-race-focused.log),
[setup regression](implementer1-run3-setup-regression.log) and
[final quick](implementer1-run3-final-quick.log) logs.

## Managed contention and documentation

Twelve root/member × send/queue × manual/automatic/unknown scenarios use actual
managed SendWithOptions/QueueWithPolicy, actual backend/controller/A continuation,
independent websocket clients and the common durable admission+ledger paths.
Native barriers wait outside the fixture mutex. Manual wins cancels/supersedes
with zero automatic start/steer. Automatic owns excludes manual native mutation
through receipt persistence, then the same waiting manual path follows normal
steer/queue semantics. Unknown automatic acceptance retains the real exact
submitting ledger and holds manual input until exact-ID reconciliation. Existing
cross-process, roster, resolver, settings and status tests remain intact.
Lead directly accepted the exact portal paragraph explaining implicit native
turn/start steering/settings and the managed-writer fence boundary.

Final Nix quick selectors (all pass):

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly -race ./internal/workspacecodex -run '^TestRetry(ManagedInputContendsWithController|WarmSettings.*|LoadedTerminalStatusController)$' -count=1 -timeout=50s
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry -run '^Test(PrivateStoreRestartAndAdmissionExclusion|AdmissionFenceAcrossProcesses|Controller.*)$' -count=1 -timeout=25s
TMPDIR=/tmp go test -mod=readonly -race ./internal/web -run '^TestTurnRetry(RootAdmissionSharesRosterOperationFence|ResolverRecoversExactNativeLedgerBeforeOrdinaryGate)$' -count=1 -timeout=30s
TMPDIR=/tmp go test -mod=readonly -race -tags live_switch_integration ./cmd/workspace-portal -run '^TestNativeRetry(PortalSecureSetup|ReceiptBarrierRequiresSuccessfulReceipt)$' -count=1 -timeout=20s
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNative(LiveSwitchReconnect|TurnRetryController)$'
```

Results:21.646s/4.836s/6.892s/1.225s/0.044s/0.045s; both expected native names listed.
Pin contract/diffcheck also passed. These checks tested b703a8e5, exactly b695's
committed tree. The later browser-only correction below changes no Go source or
pin; final d819 checked tree is6f1f05da. No declared hook framework was bypassed.

## Prior731 CI and the final test-only correction

Run39825681410 attempt1 at731 failed fast job119988219484. Archive and creation
passed; host skipped. Complete [job log](implementer1-731-ci-job119988219484.log)
(3332lines), [failed-step log](implementer1-731-ci-failed.log) and
[metadata](implementer1-731-ci-run.json) are preserved. Failure:71browser cases,
70pass; `Disable fences a delayed old Enable across tabs before local storage or
unsubscribe side effects`, registration stage, expected deferred release callback
function, observed undefined after100setImmediate turns. The test and production
notification module were blob-identical at upstream base/731/b695. The bounded
spin did not establish async completion. Enable awaits native WebCrypto digest
before registration, but the old log lacks phase evidence: crypto delay is a
source-backed candidate, never a claimed empirical root cause.

Lead released one narrow test-only correction: explicit stage-entry Promise,
existing supported2000ms test timeout, synthetic phase diagnostic. Deferred
permission and registration callbacks signal entry only after release is installed.
All later cross-tab Disable/storage/unsubscribe assertions remain unchanged.
[Exact selector and complete71-case log](implementer1-731-ci-synchronization-quick.log):

```sh
cd portal
node --check internal/web/attention_browser_test.cjs
node --test --test-name-pattern='^Disable fences a delayed old Enable across tabs before local storage or unsubscribe side effects$' internal/web/attention_browser_test.cjs
node --test internal/web/attention_browser_test.cjs
```

Exact case1pass/0fail/0skip,288.437639ms; complete71pass/0fail/0skip,7954.224506ms.
b695→d819 changes ONLY that test(+7/-5). The [binary patch](implementer1-b695-ci-sync.patch),
[range diff](implementer1-b695-to-ci-sync.range-diff),
[reviewed b695 bundle](implementer1-reviewed-b6956520.bundle),
[reviewed731 bundle](implementer1-reviewed-731bb742.bundle) and
[complete731→d819 range](implementer1-731-to-d819.range-diff) retain history provenance.

A pin: c1f415ad5602c23e6443cced73cb59267a796f05; Go/Nix/source NAR verified from
published source, only codex-web lock node changes; vendor contents differ from
prior665 only in modules.txt. Exact metadata is in the structured receipt.
Current CI is a snapshot only: final d819 run39832302919 queued; superseded b695
run39831251707 in_progress. Its requested cancellation was rejected HTTP403
(Resource not accessible by personal access token). No final-head cancellation or
CI wait occurred.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/>

---

# Package B native3 launcher result: current phase

Source remains `731bb742e07b4374cb8ee9a3a1379eb751cf44c4`, tree
`67a58609dd374702984ae871b47e08977ca9abf8`, clean and unchanged. Lead reports
the material affected review passed at731. Run3's B batch is a launch failure,
not a B test failure: [runtime.jsonl](native-verification/run-3-731bb742/runtime.jsonl)
is empty, [stderr](native-verification/run-3-731bb742/runtime.stderr) says Go
cannot find the main module from the workspace root, and no test executed.
Original logs are preserved. No source fix is justified by this result.

Lead owns a deterministic corrected cd-to-B/portal script and fresh utility
batch in a separate unique directory. B did not launch or retry native tests,
change app files/refs, or duplicate a process. C remains frozen3f. Actual B
native controller verification is still outstanding; source-owner follow-up
resumes if a genuine corrected native test failure surfaces. A's source-unit
results and follow-ups remain with implementer0/lead/architect.

# Loaded-terminal status correction receipt (published731)

Final B head `731bb742e07b4374cb8ee9a3a1379eb751cf44c4` is committed, SSH
published, remote verified and clean. The saved architect run2 contract and lead
release cover this material protocol correction. Intended A/B source units are
complete and focused checked; same-reviewer affected general/architecture/risk
review is required before native run3. No native3, long suite, build, deployment,
claim, merge or lifecycle action occurred. C stays frozen3f until the native
campaign succeeds, under lead's source-unit verification policy.

## Final source/history/input inventory

Base and fresh remote master remain `bf6d4b0c49600c15e17fe71248807ef43424e932`,
with installed `483d4e7eafeda974dfe19de45687795562072d7d` ancestry retained.
Complete final four-commit series:

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core/store/policy, exact unchanged.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — package capability, exact unchanged.
3. `0f752d7e928458992ef98b76ec40ff1740d0acf7` — runtime integration/proof/tests/docs.
4. `731bb742e07b4374cb8ee9a3a1379eb751cf44c4` — sole final A dependency pin.

[Verified reviewed3f bundle](implementer1-reviewed-3f2153a4.bundle) retains the
original source range requiring this base. [Full old/new range-diff](implementer1-3f-to-status-correction.range-diff)
compares both complete four-commit series. Core/capability exact SHAs are unchanged;
only owning runtime and the final single pin changed. There are no retained
fixups/intermediate dependency streams. Reviewed old3f tree is
`356958ff8da7119d03289eebf9d8ed267be24a92`; final tree
`67a58609dd374702984ae871b47e08977ca9abf8` equals tested pre-fold003cb429's tree.
`git diff --exit-code 003cb429 HEAD` is empty. Final committed-head checks pass.
History changes are material and require the affected review; no patch-equivalence
review reuse is claimed for the new protocol predicate.

Delta from3f: ten files, 239 insertions and 22 deletions. Final base-to-head:
40 files, 5440 insertions and 18 deletions. Direct B product change is limited
to `retryBackend.Check` delegating to A's exact loaded-failed observation helper,
with the main-approved diagnostic. Native fixture wait consumes that same helper
and retains bounded diagnostic evidence. Additional tests exercise the real
adapter/controller/native-wire composition; shared fixture extends only test RPC
support. Portal paragraph uses the lead's exact direct writing pass. Five pin
metadata files select A consistently. No core/schema/I3/quota/lifecycle/CLI or
public B API change exists. Private schema1/capability1 prerelease provenance and
native ledger schema3 remain unchanged; no migrations, defaults, resets or
preliminary-format compatibility are added. There are no database migrations.

No hook framework is declared or bypassed. SSH force-with-lease required exact
reviewed3f. Subsequent remote read proves731bb74 and unchanged master. Own index
and worktree are clean. Old reviewed61de/e0fb/cca/85 ranges, bundles and native
run1/run2 original artifacts remain preserved in the historical receipts below.

Final A `665fd35e3b29e07c29cd990c2067a3dba295fbf7` metadata independently fetched:

- Go `v0.0.0-20261022174139-665fd35e3b29`.
- Module sum `h1:f/EidDRWElptMLPzfruEDa4i+bPxzXunaUwm7xmrvpg=`.
- go.mod sum `h1:SfoFFfEnXQusGm701eWJpCbrkwia5g1biF5KD9RIqr0=`.
- Source NAR `sha256-cqEMNpK9xm1hb4Z1qgog1AqGPbuvJvc5fuBBNcBYqP0=`,
  lastModified1792690899, source `/nix/store/9dpap5hf7hqrlxnvps7rfx6qnhxawxqw-source`.
- Vendor NAR `sha256-CHVIE5thHZknsvi1uSHlPGgd2C88kA42ar7uOZ7bhVc=` generated
  by `go mod vendor -o /tmp/codex-thread-retries-vendor-665fd35e` and hashed.

The Go download/hash receipt is retained in
[first focused log](implementer1-status-first-focused.log). Nix updated only the
codex-web source node; all other locked nodes/edges compare equal to reviewed3f.
Native source pin remains Codex0.163.0. Vendor changes are exactly A
`codex/{turn_state,continuation}.go` and modules.txt, matching the new public
helper and continuation predicate; no unrelated vendored changes exist.

## Corrected status contract and evidence

Pinned native source distinguishes loaded `systemError` from cold `notLoaded`.
It preserves the error flag after completion until another turn starts. The
shared `TurnState.IsLoadedFailedTurn(expected)` accepts only a nonempty exact
latest expected failed turn on raw idle/systemError. It does not normalize
status, classify an error, prove authority or grant general execution. B's
exact error allowlist, historical context/settings, epoch/binding/provider/
socket/policy and managed lifecycle/admission remain decisive. Native queue,
prompts and unresolved ledger still hold the A dispatcher. I3's separate exact
active/inProgress warm-continuity witness is unchanged. No resume/reset/dummy
turn obtains an idle status.

[Run2 diagnosis](implementer1-native-run2-diagnosis.md) explains the source-backed
contract mismatch and diagnostic insufficiency. Run2 did not retain the actual
failed tuple, so no empirical systemError result is claimed. Native runs1/2
remain failed/incomplete; no successful controller scenario is inferred from
source fixes or fake tests. PATH warning is nonfatal source behavior and is not
established as either failure's cause.

## Exact quick checks before affected review

All in repository Nix development shell:

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./internal/workspacecodex -run '^TestRetryLoadedTerminalStatusController$' -count=1 -v -timeout=30s
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1 -timeout=50s
TMPDIR=/tmp go test -mod=readonly -race -tags live_switch_integration ./cmd/workspace-portal -run '^TestNativeRetryReceiptBarrierRequiresSuccessfulReceipt$' -count=1 -timeout=30s
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNative(LiveSwitchReconnect|TurnRetryController)$'
TMPDIR=/tmp go test -mod=readonly ./cmd/workspace-portal -run '^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/web -run '^TestShippedBrowserClientMatchesSessionAPI$' -count=1
```

[First matrix](implementer1-status-first-focused.log): 52 subcases PASS4.399s,
no failed setup or assertions. Both statuses × capacity/cyber with actual
managed queue admission, native-style rollout/receipt, backend/controller and A
continuation; exactly one start/accepted result for positives. Cold, active,
unknown status, wrong/newer turn, nonfailed/inProgress, unknown code, missing
binding, provider mismatch, native queue, real pending request and foreign
prepared ledger prevent starts; queue/prompt/ledger holds remain present.
No automatic resume/settings/policy mutation occurs. Real output request checks
the original model/effort and exact visible continuation.

[Final focused races](implementer1-status-final-quick.log): core4.058s,
workspacecodex18.330s, web7.402s; fake receipt-barrier race1.225s; tagged compile
0.047s, both native names list0.051s; notification0.207s, browser1.088s.
[Exact final-head log](implementer1-status-final-head.log): matrix4.447s,
tagged compile pass, native names list0.046s, pin and whitespace pass.
Core/source/template/format consistency checks passed. No native test executed.

[Publication Actions snapshot](implementer1-status-publication-actions.json):
current731 run39825681410 in_progress, not awaited or canceled. Superseded3f
run39818601167 completed success; other old runs are completed. No superseded
queued/running workflow requires cancellation.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

# Historical run2 protocol correction preparation

Lead released the architect's saved exact `IsLoadedFailedTurn` contract.
B's uncommitted product diff calls the shared helper in Check and the native
wait; raw native status, classifier, I3, quota, schema and ordinary fences are
unchanged. The actual backend/controller/continuation-wire matrix is written
for both loaded statuses and both eligible codes plus negative holds. Main
lead's exact portal paragraph and diagnostic wording are applied. Compilation
and final checks await the published A helper pin; no temporary shim is used.
The reviewed3f range is retained in a verified bundle. No native rerun, product
publication or downstream C edit has occurred in this phase. Affected independent
general/architecture/risk review is required after final commits and quickchecks.

# Run2 diagnosis at published 3f2153a4

Published source remains `3f2153a44e87bcd60c40ac5dcc660f214ccf04fa`.
Native run2 is failed/incomplete: existing reconnect PASS2.95s, retry fixture
FAIL90.21s waiting for literal loaded idle; runtime command exit1/95seconds.
No new retry scenario passed. No native rerun occurred. The source-backed
sticky systemError candidate has been escalated; lead assigned architect0's
exact contract design and holds all product/status edits and publication.
No dummy turn, status reset, resume workaround or cold-hold relaxation is allowed.

[Run2 diagnosis](implementer1-native-run2-diagnosis.md) retains exact original
logs/hashes, pinned-source anchors and the distinction between source evidence
and unlogged runtime observations. PATH-alias warning is nonfatal by source and
not established as the timeout cause. Uncommitted test-only diagnostics now
retain bounded actual status/errors, passive loaded/rollout setup facts and the
last polling evidence; [tagged compile](implementer1-run2-diagnostics-final-compile.log)
passes0.044s. No source ref or product code changed. Next action is implement
the accepted saved A/B status predicate brief once lead releases it, then
focused checks/commits/affected review before fresh utility native verification.
C stays frozen until the final A/B native campaign passes, per lead.

# Historical native fixture correction receipt (published 3f2153a4)

Final corrected head `3f2153a44e87bcd60c40ac5dcc660f214ccf04fa` is SSH published,
remote verified and clean. The initial native run remains failed; no native
rerun occurred. Lead released the source-diagnosed test-only fixture correction
and the sole mechanical final A pin. Lead's direct step9 inspection and a fresh
utility native run remain required. No product/core/schema/API change, native
hold relaxation, build, deployment, resource claim, merge or session action ran.

## Final native-correction series and proof

Base/fresh origin master remains `bf6d4b0c49600c15e17fe71248807ef43424e932`,
including installed `483d4e7eafeda974dfe19de45687795562072d7d` ancestry.

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core, exact unchanged commit.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — capability, exact unchanged commit.
3. `cc0b59d5c4e9adb80ba9a7d9e711504b104701a0` — runtime, native-test fix folded.
4. `3f2153a44e87bcd60c40ac5dcc660f214ccf04fa` — sole consolidated final A pin.

The previously reviewed e0fb range is preserved in
[verified bundle](implementer1-reviewed-e0fb1238.bundle), with the same base
prerequisite. [Complete old/new range-diff](implementer1-e0fb-to-native-fixture.range-diff)
contains only the owning runtime test correction and final dependency metadata.
There are no retained fixups or intermediate pins. Old61de/cca/85 ranges,
bundles and evidence remain below; the original failed run files are unchanged.
The e0fb tree was `638bcedaf954b1d6c23033082c257b90eddc452f`; final tree
`356958ff8da7119d03289eebf9d8ed267be24a92` equals tested pre-fold5430781's tree.
`git diff --exit-code 5430781 HEAD` is empty. Final committed-head checks pass.

Delta from e0fb: seven files, 205 insertions and 29 deletions. Only
`turn_retry_native_integration_test.go`, `turn_retry_native_proxy_test.go` and
five mechanical pin files changed (`flake.nix`, `flake.lock`, `portal/go.mod`,
`portal/go.sum`, `nix/workspace-portal.nix`). The diff excluding those exact paths
is empty. Final base-to-head diff: 39 files, 5223 insertions and 18 deletions.
The source stream retains four logical commits. No hooks declared/bypassed.
SSH force-with-lease required exact e0fb; subsequent remote read proves final3f
and unchanged master. Own worktree/index are clean. C ownership remains with
implementer0, notified of the exact final head; no C edits by B.

Private schema1/capability1, required epochs/keyed charges, no-predecessor
prerelease provenance and native ledger schema3 remain unchanged. There are no
database migrations or added preliminary compatibility paths. Neither B nor A
has a product/API/schema delta in this correction; A's direct lead-inspected
change is one native-test nil-to-empty environment map.

## Exact final A input graph

- Published A SHA `b6d3a92ff85edbcd661b193c2319951eb4a71725`.
- Go `v0.0.0-20261022165208-b6d3a92ff85e`.
- Module sum `h1:4yUJFjAkN0HrhqzCm/Ahn4mIYmCn575wfho9cJdEsgc=`.
- go.mod sum `h1:SfoFFfEnXQusGm701eWJpCbrkwia5g1biF5KD9RIqr0=`.
- Source NAR `sha256-+spYLvVf3GNpJR0Y9GN01AxeNqnOyTD8RAtR0CUjY6w=`,
  timestamp1792687928, source
  `/nix/store/ilwjswz2wc7bh0r95ws0kjwggkz7gr53-source`.
- Regenerated vendor NAR `sha256-jkLE8bzUevxNx/LcZ80p70u3ZH4k4eZq23rw8Bcjtb8=`.

[Go download receipt](implementer1-final-a-module.json) independently resolves
the published SHA and both sums. `nix flake update codex-web` generated only its
source lock change; all other locked inputs/edges are unchanged. Source NAR
was independently hashed and matches the owner report. Vendor generation used
`go mod vendor -o /tmp/codex-thread-retries-vendor-b6d3a92f` followed by
`nix hash path`; [hash log](implementer1-native-final-vendor-hash.log) retained.
The complete diff against the prior generated vendor tree is **only** the
modules.txt pseudo-version line; all vendored product files are identical.
Go/Nix pin contract and whitespace checks pass.

## Run1 diagnosis and authorized correction

[Source diagnosis and original log hashes](implementer1-native-run1-diagnosis.md)
preserves runtime exit1/8seconds, existing reconnect PASS2.87s and new retry
FAIL0.99s. The old assertion printed Store.Load error nil, discarded Step error,
and retained no native turn/start reply/state. It does not prove actual dispatch
or an empirical cold/unload cause. Closing the only subscriber before fresh
dispatch violates the fixture's loaded premise; native idle auto-unload is a
source-confirmed possibility. Product holds remain strict. The old proxy could
also replace a native rejection; the original log does not establish it did.

Correction keeps the native subscriber through controller/store reconstruction,
cold-reads the exact loaded idle failed source before due dispatch, and retains
actual client restart after acceptance. Proxy only hides a nonempty successful
native receipt and records its exact identity; errors/missing receipts pass
through with bounded diagnostics. UnknownSendOutcome type, one native start/
acceptance, hidden history, exact native schema3 submitting UUID/action/text
digest and ordinary admission refusal are asserted before recovery. The real
retained portal worker must recover the exact receipt. Native history must then
contain exactly one matching continuation input and provider request count must
not increase. No ledger is manufactured or rewritten by the test.

## Focused correction checks (no native execution)

Repository Nix shell, exact final-head commands:

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly -race -tags live_switch_integration ./cmd/workspace-portal -run '^TestNativeRetryReceiptBarrierRequiresSuccessfulReceipt$' -count=1 -timeout=30s
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNative(LiveSwitchReconnect|TurnRetryController)$'
```

[Final-head log](implementer1-native-final-3f2153a4-head.log): fake proxy race
PASS1.224s, tagged compile-only PASS, both required native names listed0.042s,
pin and whitespace checks PASS. [Final pin quick log](implementer1-native-final-quick.log)
has all three fake outcomes accepted/rpc-error/missing-receipt PASS with race
1.154s, compile0.037s/list0.046s, notification consumer0.176s and shipped browser
1.004s. Earlier fake normal0.072s and race1.213s were green. Test diagnostics
and fake-server evidence establish the proxy contract only; actual native
acceptance/recovery/opt-out still require a new utility run. No assertions are
waived and no missing native case is counted as success.

[Post-publication Actions snapshot](implementer1-native-final-actions.json):
current3f run39818601167 is in_progress, not awaited or canceled. Superseded e0fb
runs39815568428/39815566005 completed successfully; earlier runs are completed
failures. No superseded queued/running run needs cancellation.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

# Historical fixture receipt (published e0fb1238)

Final feature head is `e0fb1238bd17cc3b29cc7d59ddaa9784c89ef939`, SSH published
and verified by a subsequent remote read. The worktree and index are clean.
Lead accepted I3 authority review at `61de5e28` with no findings, then released
only the two test-fixture corrections diagnosed from prior failed CI. Production
behavior, core/schema, public contracts, capability and A source/pin are unchanged.
Lead's mandatory-review step9 confirmation is the next review action; no
independent rerun merely to confirm these narrow requested fixture fixes.

## Final exact range and test-only delta

Base/fresh remote master: `bf6d4b0c49600c15e17fe71248807ef43424e932`, preserving
installed `483d4e7eafeda974dfe19de45687795562072d7d` ancestry. Final four commits:

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core, unchanged exact SHA.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — capability, unchanged exact SHA.
3. `cc00214a4975e993a234eb2876f39c490257f28a` — runtime with fixture support folded.
4. `e0fb1238bd17cc3b29cc7d59ddaa9784c89ef939` — sole final A pin, unchanged patch.

The prior independently reviewed range is preserved in
[verified 61de bundle](implementer1-reviewed-61de5e28.bundle), requiring the same
base. Its tree is `401177e01abbba13009e4a197d694b15d0e58839`.
[Full old/new range-diff](implementer1-61de-to-fixtures.range-diff) proves the
runtime-only fold; no fixup or extra pin stream remains. The dependency stable
patch ID is still `54bed62a7a4a2053fde96119c5b8d6f018a21082`, selecting FINAL A
`d2d74f931cc50e39345c6c15931748062ee51951`.

The reviewed-to-final delta is **two test files, two insertions, one deletion**:

- `portal/cmd/workspace-portal/coordination_test.go` explicitly supplies the
  notification fake's selected `modelProvider: notification-fixture` on every
  thread/read, covering both active and idle delivery cases.
- `portal/internal/web/server_test.go` copies retry.js with the conversation
  module's other dependencies; import and API assertions remain intact.

`git diff --exit-code 61de5e28 HEAD -- . ':!portal/cmd/workspace-portal/coordination_test.go' ':!portal/internal/web/server_test.go'`
is empty. This establishes no production/documentation/pin delta. Final tree
`638bcedaf954b1d6c23033082c257b90eddc452f` equals tested pre-fold commit
`d15bd09`'s tree; `git diff --exit-code d15bd09 HEAD` is empty. The complete
base-to-head series is 39 files, 5047 insertions and 18 deletions.
SSH publication used exact lease `61de5e28`; remote confirms final e0fb and
unchanged master. No hooks are declared/bypassed. There are no database
migrations; private schema1/capability1 prerelease provenance and native ledger
schema3 remain unchanged. No release/deployment/external-consumer boundary was
added; prior retained ranges/bundles below remain historical evidence.

## Previously failing selectors now pass

All commands ran in the repository Nix development environment:

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./cmd/workspace-portal -run '^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$' -count=1 -v -timeout=30s
TMPDIR=/tmp go test -mod=readonly ./internal/web -run '^TestShippedBrowserClientMatchesSessionAPI$' -count=1 -v -timeout=30s
TMPDIR=/tmp go test -mod=readonly ./cmd/workspace-portal -run '^Test(RootThreadSettingsKeepLeadPolicySeparateFromModel|ThreadEnsureInitialUsesOrdinaryRootTurn)$' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/web -run '^TestSessionPreparationShippedBrowserHTTP$' -count=1
```

[Exact final-head log](implementer1-ci-fixtures-final-head.log): notification
both active=false/true PASS, package0.212s; shipped browser PASS0.975s.
[Nearby checks](implementer1-ci-fixtures-nearby.log): root settings/initial
package0.059s; preparation-browser HTTP0.877s. Formatting and whitespace checks
pass. [Initial correction log](implementer1-ci-fixtures-focused.log) also passed
both previously failed selectors (0.197s/1.077s). No assertions were weakened.
Prior failure attempt/job/log SHA proof remains in
[the read-only diagnosis](implementer1-prior-ci-diagnosis.md); no failed job was
rerun as validation.

No native compile repeat was needed for two fixture-only changes; unchanged
native fixture compile/list evidence at reviewed61de remains below. No native,
long suite, build, deployment, resource claim, merge or lifecycle action ran.
C final repinning belongs to implementer0, notified of the exact published head;
B did not edit C. The immediate post-push
[Actions list](implementer1-ci-fixtures-publication-actions.json) returned `[]`;
the [exact prior-run snapshot](implementer1-61de-ci-superseded-status.json)
shows superseded61de run39814474141 in_progress. The authorized cancellation
attempt was rejected with HTTP403 `Resource not accessible by personal access
token`; [the exact rejection](implementer1-61de-ci-cancel.log) is retained.
Cancellation is therefore unconfirmed and that old run may continue. No
final-head work was canceled or awaited.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

# Historical I3 receipt (published 61de5e28)

I3 is implemented, committed, focused/race checked and SSH published at
`61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b`. Independent affected authority review
is pending. Native fixtures remain **unrun**. No long verification, deployment,
merge, resource claim or session lifecycle action was performed.

Read-only follow-up of the completed prior CI runs found two consumer-fixture
defects still present at this head: missing modelProvider metadata in the
coordination notification test and missing retry.js in the browser contract's
copied module list. Both were outside the previous focused selectors. Complete
logs, exact run/attempt/job identities, source evidence and correction candidates
are in [the prior-CI diagnosis](implementer1-prior-ci-diagnosis.md). Source/refs
remain frozen at61de pending lead's release; no rerun or correction was performed.

## I3 exact range, series and provenance

The base and freshly fetched remote master remain
`bf6d4b0c49600c15e17fe71248807ef43424e932`, retaining installed
`483d4e7eafeda974dfe19de45687795562072d7d` ancestry. Own feature branch is
`2026-10-22-codex-thread-retries` in the registered dev-workspace worktree;
remote remains `git@github.com:aither64/dev-workspace.git`.

Complete final series, oldest first:

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core, unchanged exact commit.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — capability, unchanged exact commit.
3. `5347f5ddacf321216b818a1e8a0373b7edbb3304` — owning runtime, I3 folded here.
4. `61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b` — sole final A pin, unchanged patch.

The reviewed `cca49782ebd2d5135352cea4cb140548b36f7de9` range is preserved in
[its verified bundle](implementer1-reviewed-cca49782.bundle), requiring the
recorded base. [Complete old/new range-diff](implementer1-cca-to-i3.range-diff)
compares both four-commit ranges from that base. Only the runtime patch changed.
The pin stable patch ID remains `54bed62a7a4a2053fde96119c5b8d6f018a21082`.
Core/schema, capability, I1/I2 and all A API/source/input pins are unchanged.
No fixup or repeated dependency stream remains. The original `85f6f73` review
range and its separate remediation comparison remain preserved below.

The exact I3 delta is three files, 550 insertions and seven deletions:
`portal/internal/workspacecodex/turn_retry.go`, its new production-wrapper test
`turn_retry_settings_test.go`, and `docs/turn-retry-recovery.md`. The complete
base-to-head diff is 37 files, 5045 insertions and 17 deletions. Final tree
`401177e01abbba13009e4a197d694b15d0e58839` equals tested pre-consolidation
commit `1c25485`'s tree; `git diff --exit-code 1c25485 HEAD` is empty.
Final committed-head checks also pass. No hook framework is declared and no
hook was bypassed. SSH force-with-lease required the exact old `cca49782` ref;
the subsequent remote read proves `61de5e28` and unchanged master. Worktree and
index are clean.

Private final schema1/capability1 provenance is unchanged: no merged, released,
deployed or externally consumed predecessor; earlier shapes were disposable
fixtures only. There is no migration, compatibility shim, quota reset or public
contract change in I3. Existing native ledger schema3 is unchanged. There are
no database migrations. C pins belong to implementer0; B did not edit them.

## I3 behavior and focused evidence

The successful explicit settings owner may inherit only the existing verified
loaded witness when cold reads prove the same exact nonempty active/inProgress
turn before and after unequivocal settings success. Provider, socket, authorized
policy/MCP, common instructions and managed execution permission are rechecked.
Epoch advance, old-turn consumption and nil binding are saved before native
effects even with Pending=nil. Promotion changes only the binding's epoch/digest;
old snapshots, queued admissions and uncertain tuples remain unchanged. The
native sessionId is never a generation witness. Turnover, cold/idle state,
missing proof, failed/uncertain RPC or failed checks/persistence retain the hold.
No extra resume/rebind/native policy write or default-derived authority is added.

All commands ran in the repository Nix shell. Exact commands:

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./internal/workspacecodex -run '^TestRetryWarmSettings' -count=1 -v -timeout=30s
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1 -timeout=40s
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNativeTurnRetryController$'
```

[Final validation log](implementer1-i3-final-validation.log): production selector
2.531s; races core4.565s/workspacecodex8.480s/web7.566s; native-tag compile-only
pass and exact native fixture listed (0.059s). [Final committed-head checks](implementer1-i3-final-head.log):
production2.680s; tagged compile/list pass (0.047s); pin contract and whitespace
checks pass. Earlier [full retry selector](implementer1-i3-final-quick.log) passed
3.154s. Gofmt reports no changes. No native case ran.

Four top-level new tests cover eight root/member positive model/effort/both-mode
paths, 22 conservative continuity refusals, pre-effect persistence refusal and
preservation of an uncertain old tuple. Prior MCP/instructions/access binding is
established through actual managed ActivateThread. Positives call actual
UpdateThreadSettings, native acknowledgement and active QueueWithPolicy, then
exact native-style rollout/context and client-ID/content history through the
real backend and Controller. Old queue failures are rejected; new-epoch failure
schedules and passes Check with the requested settings. FIFO and old snapshots
are unchanged. Proof/scheduling emits no resume/settings/policy/queue mutation.
Refusals include pre/post cold/idle, completion/automatic queue turnover,
provider/socket/policy/MCP/access/common changes, missing prior proof, authority
and postcheck errors, failed/unknown native settings and failed promotion save.

Two fixture corrections preceded the final green evidence: QueueEntry contains
an attachment slice, so equality assertions use DeepEqual; the uncertain tuple
fixture's Begin clock now reaches its capacity deadline rather than incorrectly
dispatching at observation time. These were test setup errors, not product
failures. Main lead's exact direct writing pass paragraph was applied before
commit; no diagnostics or status copy changed.

Post-push [Actions snapshot](implementer1-i3-publication-actions.json) shows the
new head queued, and completed failures for old `cca49782`/`85f6f73`. There was no
superseded queued/running run to cancel. No CI wait or rerun was started.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

# Historical B1/I1/I2 remediation receipt (published cca49782)

The accepted final-review corrections B1/I1/I2 are implemented, focused checked,
consolidated into the original owning commits and SSH published. Affected-lane
independent review remains outstanding. Native fixtures remain **unrun**.
No long verification, deployment, merge, claim or session action was performed.

## Current exact source and historical comparison

- Current head: `cca49782ebd2d5135352cea4cb140548b36f7de9`.
- Base: `bf6d4b0c49600c15e17fe71248807ef43424e932`; final SSH fetch still
  reports this origin/master. Installed `483d4e7eafeda974dfe19de45687795562072d7d`
  remains an ancestor.
- Branch/worktree/SSH remote are unchanged from the original packet below.
- SSH `git ls-remote` verifies the current exact head; working tree/index clean.
- Old fully reviewed head: `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`.
  [Verified original bundle](implementer1-reviewed-85f6f73.bundle) retains its
  feature ref and requires the recorded base. It contains the genuine reviewed
  old commits, not a reconstructed claim of equivalence.
- [Old/new complete range comparison](implementer1-reviewed-to-final.range-diff)
  compares both complete four-commit ranges from that base. Core/runtime patches
  deliberately change; they require affected-lane review, not equivalence reuse.

Current complete series, oldest first:

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core/store/policy/tests.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — package capability.
3. `c493a41a75de6e1ff857c32b29620ee7862d362a` — runtime/admission/fixture/docs.
4. `cca49782ebd2d5135352cea4cb140548b36f7de9` — single final A dependency pin.

Corrections were folded into commits 1 and 3. No fixup commits remain.
Capability old/new stable patch ID is
`c98df1ec8b8d41855d9263096f4fddebc5d45c76`; dependency old/new stable patch ID is
`54bed62a7a4a2053fde96119c5b8d6f018a21082`. Those two patches are unchanged;
only ancestry changed. The codex-web stream still selects only FINAL A
`d2d74f931cc50e39345c6c15931748062ee51951`, with identical Go sums/Nix lock/vendor
hash. No A source/API change, extra pin stream or downstream C edit was made.

Old-to-new delta: 14 files, 1281 insertions, 110 deletions. Complete final
base-to-head diff: 36 files, 4502 insertions, 17 deletions. Added code is primarily
required regression fixtures. The consolidated tree
`8bbdd72dde0b8c7046d1b6fea7859318b9fd6b1f` exactly matches the tested pre-rebase
remediation tree; `git diff --exit-code fdd8288 HEAD` was empty. Full-range
whitespace check passes. No hooks are declared; no hooks were bypassed.
A post-force-push GitHub Actions list for this exact feature branch returned
`[]`; no superseded queued/running workflow existed to cancel and no CI wait
was started. Command: `nix shell --inputs-from . nixpkgs#gh --command gh run list --repo aither64/dev-workspace --branch 2026-10-22-codex-thread-retries --limit 20 --json databaseId,headSha,status,conclusion`.

## Corrected contracts and private format provenance

I1: a separate internal reconciliation-only admission takes transition/runtime/
roster/conversation/thread locks and exact retained identity. It only settles the
saved tuple with existing A Reconcile/DiscardPrepared APIs. It cannot dispatch,
resume, steer or write settings. The worker then reacquires the unchanged strict
ordinary resolver before any possible fresh dispatch. Foreign unknowns and cold,
stopped, generation, lifecycle and execution holds remain effective.

B1: settings intent proves the current native thread/turn identity, durably
advances a nonzero epoch and consumes the active/failed turn before the settings
effect, including Pending=nil. Every prior admission, including native queues,
loses automatic authority; the queue itself/FIFO remains untouched. Old tuples
are immutable for reconciliation; current binding establishment cannot retrobind
old empty admissions. New managed admission captures the new epoch. Preference,
enrollment and quota survive failed/unknown settings replies and restart.

I2: charges are UUID-keyed. Positive exact never-submitted proof is required to
renew that same UUID at the current clamped time before outbound. Unknown native
submissions never resend. Acceptance/reconciled acceptance anchors that ID's
charge once to conservative receipt observation time, covering network delay;
duplicate receipt observation neither adds a slot nor moves its anchor again.
Other equal-timestamp IDs remain distinct. Up to one retained old reservation
plus 30 other records fits the bounded store; dispatch still refuses 30 other
live charges. No elapsed-time quota rearm or replacement UUID is introduced.

Final prerelease private schema is **1**, capability `turnRetryStateSchema=1`,
as explicitly directed by lead and saved by architect. State/Binding/Snapshot
require nonzero epochs and digest inclusion; bindings match the current epoch,
while retained old snapshots may only reconcile. Charges require unique UUIDs,
positive timestamps and correspondence with charged Pending. Preliminary missing
epoch/anonymous charge shapes fail closed. There is no conversion/default/quota
reset or iteration-compatibility shim. This shape has no deployed/released/merged
or external predecessor; only disposable test records ever consumed the earlier
shape. Existing native ledger schema 3 and unrelated formats remain unchanged.
There are **no database migrations**.

## Remediation validation and native gate

All below are repository Nix development shell commands. Final logs:

- [Final focused races](implementer1-remediation-final-race.log): core 4.152s,
  workspacecodex 2.423s, web 7.185s; exit zero.
- [Final web/compile/list/pin checks](implementer1-remediation-final-quick.log):
  affected web 5.127s, tagged compile-only passed, expected native fixture listed
  0.050s, pin consistency and whitespace checks passed. A harmless ignored Nix
  evaluation-cache SQLite busy diagnostic occurred in the shell startup;
  command results were successful.
- Earlier complete new core package 1.107s and complete workspacecodex package
  7.185s passed. Final new core tests are included in the final race selector.

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/web -run 'Test(TurnRetry.*|CreationlessConversation.*|Recovery.*|.*Conversation.*|.*PlanImplementation.*)$' -count=1
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNativeTurnRetryController$'
```

Real resolver regressions exercise creation-less root AND retained member with
actual workspacecodex observation and schema-3 A ledger: prepared, absent,
submitting after native acceptance/lost usable reply, cancelled, cold, stopped,
foreign same-thread/other-member unknowns, genuinely unknown history and package
generation replacement. Tests prove that strict mutation admission fails before
own exact reconciliation, owned receipts recover without another start, and
foreign unknowns keep the ordinary gate closed. Their native stub rejects every
resume/steer/settings/queue activation RPC. Provenance regressions cover active
and failed-but-unobserved Pending=nil executions, model/effort/both mode directions,
failed settings RPC, native autoqueue turnover after the identity read, old empty
binding rejection, post-barrier managed queue proof and durable restart shape.
Quota tests cover 299/301-second dispatch delay, 29/30 other live IDs, same-time
IDs, backward clock, conservative network-delay acceptance, unknown no-resend,
once-only delayed reconciliation reanchor, overflow and preliminary shape errors.

The native `TestNativeTurnRetryController` now uses an owned test-only WebSocket
receipt/history barrier: the real daemon accepts a turn, its usable reply is
removed and exact history is held, leaving A's ledger submitting. After client
restart the barrier opens and the **real portal scheduler/resolver** must recover
the same receipt without another provider request. The helper/fixture compile;
no native run or empirical inheritance/receipt claim has been made. Top-level
fixture name remains unchanged and it has no named subcases. Native execution
remains after affected-lane final review under the watcher brief.

One new settings fixture initially stalled because its fake returned a settings
error and stopped servicing subsequent RPCs on the still-open connection. The
owned test process was interrupted for diagnosis (not a native/live session);
the fake read loop was corrected and test contexts bounded. Final focused/race
checks pass. An initial resolver test assertion assumed Pending survived a
completed turn; it now checks the durable exact accepted snapshot, allowing
ordinary completed-state advancement. Production holds were not relaxed to
make either fixture pass.

Lead directly applied the required writing skills to the new guide paragraphs
and eight bounded diagnostics, and supplied the exact corrected settings
paragraph before these commits. Status mappings remain unchanged. The required
next action is affected general/architecture/risk review on this exact current
head and old/new range; longer verification and C repinning are lead/peer-owned.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

---

# Original reviewed package B packet (superseded source head)

The following preserves original evidence for reviewed85f6, not current readiness.

# Package B final source and verification evidence

Implementation, operating docs, focused checks and SSH feature publication are
complete. Independent final review and post-review native verification remain
outstanding. No native fixture execution, package build, deployment, merge,
resource claim or session lifecycle action was performed by this package.

## Exact source and history

Repository: `git@github.com:aither64/dev-workspace.git`.
Branch: `2026-10-22-codex-thread-retries`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace`.
Base: `bf6d4b0c49600c15e17fe71248807ef43424e932`.
Published final head: `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`.

Final SSH fetch kept origin/master at that base. Both the base and installed
`483d4e7eafeda974dfe19de45687795562072d7d` are ancestors of HEAD.
`git ls-remote origin refs/heads/2026-10-22-codex-thread-retries` returned
`85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`. Index and working tree are clean.
Initial lead tracking gate: `4be0b2f3ae8257e8f0aaa9c1bd3a20bc376f4ea1`.

Complete series, oldest first:

1. `259fcd636ecb4afa0c7c4a2384c6f91d7ef8b353` — `turnretry: retain bounded retry policy and admission state`.
2. `1f76716cdec2348d65039220cfc33616702b1e80` — `runtime: require retry-capable package transitions`.
3. `0398d16bb166ccc2e16b683b9d45672172961d0c` — `portal: continue new managed failed turns through durable retry admission`.
4. `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9` — `deps: pin codex-web failed-turn continuation support`.

Core policy/store and package capability are independently reviewable. Runtime
admission, settings proof, adapter, cancellation, native fixture and operating
docs jointly establish the execution boundary and form one integration commit.
Final diff: 33 files, 3331 insertions, 17 deletions. Full-range diff whitespace
check passes. This repository declares no hook framework.

Unpublished core fixups were folded before review: the previously reported
`aac0629` iteration is superseded by `259fcd6` and absent from the series.
No obsolete intermediate implementation remains. The sole dependency stream is
codex-web, consolidated in the final commit at FINAL A
`d2d74f931cc50e39345c6c15931748062ee51951`; no intermediate25f pin commit exists.
Nix source/lock, Go module/sums and vendor hash move together. Other locked
inputs remain unchanged.

- Go: `v0.0.0-20261022145556-d2d74f931cc5`.
- Source NAR: `sha256-O3GWvvYTSDKG3Ybsj0xbmEzGMLLSF09wv4iKc2DeIsU=`.
- Vendor NAR: `sha256-E0SeFk5IWAfvK4zbU9E/d5wODCS5i1NGqQj8btaw6ho=`.

Vendor hash command in the repository Nix shell:
`cd portal && go mod vendor -o /tmp/codex-thread-retries-vendor && nix hash path /tmp/codex-thread-retries-vendor`.
That owned disposable directory and temporary commit-message files remain as
generation evidence. No session cleanup was performed.

## Final quick checks

Commands below ran through `nix develop --command bash -c` from the worktree.
All final commands exited zero. Logs are siblings of this record.

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*|Recovery.*|.*Conversation.*|.*PlanImplementation.*)$' -count=1
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1
go test -mod=readonly ./cmd/workspace-portal -run 'Test(RootThreadSettings.*|ThreadEnsureInitial.*|Provider.*|ScopedProvider.*)$' -count=1
go test -mod=readonly ./internal/workspacecodex -run 'TestRetry.*' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/turnretry -count=1
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNativeTurnRetryController$'
```

- [Normal focused log](implementer1-final-go.log): core0.146s, workspacecodex0.113s, web2.368s.
- [Race log](implementer1-final-race.log): core1.253s, workspacecodex1.272s, web1.626s.
- [Command regression log](implementer1-final-command.log):1.516s.
- [Final admission log](implementer1-admission-final.log):0.105s, after avoiding unnecessary pre-initial history reads.
- [Exact committed-head core/compile/list log](implementer1-final-head-compile.log): complete core0.333s; tagged compile0.045s; expected native fixture listed0.045s.
- [Contract/syntax log](implementer1-final-contract.log): Ruby1run/5assertions/0failures/0errors/0skips,0.053443s; Ruby syntax OK twice; node syntax, pin consistency and diff check exit zero.

Contract/syntax commands from the worktree root:

```sh
ruby -Itest test/workspace_host_test.rb -n /retry_records/
ruby -c libexec/dev-session
ruby -c libexec/workspace-host
node --check portal/internal/web/static/app.js
bash nix/check-codex-web-pin.sh portal/go.mod v0.0.0-20261022145556-d2d74f931cc5 "$(command -v jq)"
git diff --check
```

Earlier successful evidence includes the complete workspacecodex unit package
(6.542s), affected team Assign/Configure/Access/Remove selector(0.909s), complete
core race package(2.642s), actual cross-process lock exclusion, and complete core
normal tests(0.314s). No broad checks or CI waits were started before review.

Coverage includes enrollment/completion races and old-failure exclusion;
opt-out/re-enable; complete capped capacity schedule; durable30-send rolling
quota with uncertain sends, backward time and no exhaustion timer rearm;
restart/cancellation identity; corruption/version/scope rejection; cross-process
admission; provider/access/instructions/context mismatches; actual queue settings
versus enqueue defaults; steer context/settings and receipt restart; managed
model/effort/mode intent cancellation; HTTP origin/authority; native-child
exclusion; generation rejection; root roster-operation contention; and worker
reservations preventing concurrent duplicate jobs for one conversation.

## Failed checks and corrections

- Direct Ruby `test/workspace_host/profile_transition_test.rb -n /retry_records/`
  failed with `NameError: TransitionHost`: that file depends on its aggregate
  loader. The corrected exact aggregate command above passes five assertions.
- A web regression exposed a nil embedded optional fake client. Added nil-safe
  RetryAvailable/capability guards; the affected selector now passes.
- That run also failed Unix socket bind under Nix TMPDIR plus long fixture
  names (path exceeded Unix socket length). The same selector using
  TMPDIR=/tmp passes, earlier2.157s/final2.368s; no production path changed.
- The root roster contention test initially used a fake lacking the team
  interface; using the existing retained-conversation fake corrected it.
- The new settings-intent test initially referenced a nonexistent convenience
  constructor, then had incomplete fixture manifest provenance (plan/client
  version absent). Corrected fixtures exercise the real wrapper and prove
  pending work cancels even when the native settings mutation is rejected.
- Final inspection corrected steer receipt snapshot digest refresh, native
  sandbox rollout spelling (kebab-case, distinct from v2 request encoding),
  and repeated scheduler jobs for one thread. These fixes were folded before
  review. Exact history also binds contributing inputs to their executed turn
  and retires old proved inputs; unbound queue evidence remains retained/bounded.

## Native manifest and remaining gate

`TestNativeTurnRetryController`, in
`portal/cmd/workspace-portal/turn_retry_native_integration_test.go`, tag
`live_switch_integration`, is one top-level fixture with no named subcases.
Compilation/listing only are complete. It has never been executed.

The fixture selects the pinned executable through LIVE_SWITCH_CODEX, uses
private state/socket and an allowlisted child environment, and contacts only a
no-auth loopback synthetic Responses provider. It asserts managed creation and
initial failure, actual continuation preserving model/effort/mode, exclusion of
old failures, persisted scheduled UUID/deadline across client restart, actual
accepted receipt reconciliation after simulated application result-save loss
without another provider request, and opt-out before a later deadline.
No real provider key or policy-violating input is used.

After review, require go test -json top-level PASS and no skip under the fresh
watcher, per [native-verification.md](native-verification.md). The failure wire
and native inheritance contract remain source-confirmed, not empirical test
results. A owns the larger generic native campaign and native-direct CAS probe.

## Authority, docs and state provenance

Guarantees cover managed portal/CLI/retained-team operations sharing admission
and package generation. Exact historical native context plus the saved successful
managed provider/instructions/MCP/access binding is authority within that
boundary; display caches are never authority. Unmanaged direct native writers
can change loaded settings or race without CAS and are outside the guarantee.
Observed mismatches, unidentified input, changed socket epoch and recovery/queue/
provider holds fail closed. No managed admission path was deliberately excluded;
actual native compatibility remains the post-review gate.

Project explanations: README entry link, docs/workspace-portal.md controls and
schedule, docs/turn-retry-recovery.md persistence/locks/settings/uncertainty/
managed-authority/forward recovery. Lead directly applied the required writing
skills to all final prose, status reasons and defensive diagnostics before commit.

There are **no database migrations**. Existing native submission schema3,
recovery/roster/manifest/lifecycle formats retain their versions. New separate
private retry state is schema1, never merged/released/deployed/externally
consumed; only disposable fixture state exists. turnRetryStateSchema=1 gates
package selection whenever retry records exist, including cancelled records.
Forward recovery uses a matching compatible package; cancellation never deletes
uncertain identities or resets enrollment.

Final review must conclude on the complete four-commit history, consolidated
pin stream, state/migration provenance, interfaces and shared lock ordering.
Lead owns later verification/deployment/integration assignments.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
