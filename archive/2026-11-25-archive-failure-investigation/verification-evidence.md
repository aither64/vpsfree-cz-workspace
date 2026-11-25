# Package E: final verification and artifacts

Owner: implementer0. COMPLETE FOR ACCEPTANCE: all four frozen targets passed
in one Nix invocation, exit0,15:04:23Z–15:35:08Z (1845s,30m45s). Independent
final review passed with no findings before this batch. No source edits,
input changes, default integration, machine claim, activation or live lifecycle
action are part of E. Lead owns state/table and later authority; D/F retain
composition and current deployed-state/lineage diagnosis.

## Frozen inputs and admission

- Runtime: `f6d60bf87002fb1896599f35f0284743c16d7e6f`.
- Workspace: `18275679109c2adda4084af1ea7474e21be98b4e`.
- Configuration context: `6f6cb452e17ca663114a07013a0402ef85a7fee3`.
- Runtime source: `/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`.
- Runtime source NAR: `sha256-JZJQaci1y3dGVSQwHbdHS8X0IDFpyrz+dk3rqntZJOE=`.
- Complete immutable input graphs: [D candidate evidence](deployment-evidence.md)
  and its ignored `candidate-inputs.json`; no graph was changed for E.
- Final review: [review.md](review.md), retained reviewer0/Sol/xhigh, all four
  lanes, no findings. This batch is the released post-review verification.

Before launch, `dev-session current` and both environment identity markers
matched the exact bound session/workspace; saved implementer0 workspace_write
was reverified. Runtime and workspace worktrees were clean at the frozen heads.
Immutable `git+file` evaluation independently matched the recorded package/VM
and application derivations. Composition identity was evaluated in the same
frozen workspace. No source refresh/rebase was performed.

| Target | Exact evaluated derivation | Expected output |
| --- | --- | --- |
| runtime-package-check | `/nix/store/rn1872lrbs1g0jzszr3jg756f6f5gfss-dev-workspace-0.2.0.drv` | `/nix/store/y9gn3ari8scg9gxfp410lv89gz2y5mzv-dev-workspace-0.2.0` |
| archive-lifecycle-vm | `/nix/store/gnkq2g5ljyf6abi1mfip5i5nns42ysy2-vm-test-run-dev-workspace-session-archive-lifecycle.drv` | `/nix/store/phblfnanyj5yf1isfqz6qj3k1y0y4by1-vm-test-run-dev-workspace-session-archive-lifecycle` |
| composed-application | `/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv` | `/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0` |
| site-runtime-composition | `/nix/store/26hx1kp1xlmsklpx2zmz991m6qj3krn7-workspace-pi-runtime-composition-tests.drv` | `/nix/store/nxf02z6jccv47rzwzkl5gx3zadq67jya-workspace-pi-runtime-composition-tests` |

D's accepted complete graph receipt is retained byte-for-byte at
`/tmp/archive-failure-e-3mcseu33/frozen-D-input-receipt.json`, SHA-256
`85bbcf71ab121b72aff9eabbde0add9db0a2fad67a8a6b3209acc799c8a8256e`.
The runtime lock remains available from the immutable source above. Raw exact
four-target Nix derivations are `target-derivations.json` in the same directory,
SHA-256 `f87c0df4692ba5a1ab3ab9286dc5cf60aa98dbe10ade6774568bcf9c5089b75c`.

All four outputs were absent before the batch. Exact preflight refs/identities
are retained at `/tmp/archive-failure-e-3mcseu33/prepared.json`.

Lock SHA-256 identities:

| Graph | SHA-256 |
| --- | --- |
| dev-workspace | `ca7f6a807e2a32d76deb463a44677023e3fac2236ce93c82426c54307aefa51f` |
| workspace | `f411b1b56173b128a85d4c18a17869d12d9eca4add6ba1b2a843ab8b6c426919` |
| vpsfree-cz-configuration | `8f3738f6c1f9a583fc4692cb0f67de4a9db7e46dbccb896bcdb021d09546b0f3` |

## Existing CI and reuse boundary

Lead established completed final CI run `45636961676`, attempt 1, workflow
`354263807`: essential application contracts and session-creation smoke passed;
extended archive/recovery was skipped. Root owns those bounded CI reads; E
started no duplicate CI watcher. Root explicitly confirmed no exact package
derivation/input/output receipt beyond that success, so the prepared package
check remains included. Nix may reuse exact valid/substitutable results; do not
attribute reuse to CI without its missing receipt. The isolated archive VM is
required separately and was previously unrun.

## One native operation and exact command

Operation ID: `6f46454b-9508-4b45-a999-990b376cb87c`.
Canonical cwd: `/home/aither/workspace/ai/vpsfree.cz`.
One ordinary Nix invocation, with all immutable target refs:

```sh
nix build --no-link --print-build-logs --json \
  'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/dev-workspace?rev=f6d60bf87002fb1896599f35f0284743c16d7e6f#checks.x86_64-linux.package' \
  'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/dev-workspace?rev=f6d60bf87002fb1896599f35f0284743c16d7e6f#checks.x86_64-linux.session-archive-lifecycle' \
  'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/workspace?rev=18275679109c2adda4084af1ea7474e21be98b4e#default' \
  'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/workspace?rev=18275679109c2adda4084af1ea7474e21be98b4e#checks.x86_64-linux.pi-runtime-composition'
```

The single-operation launcher uses shell timestamps, captures the original
Nix exit status, and writes complete stdout/result JSON and stderr logs. Script
`/tmp/archive-failure-e-3mcseu33/run.sh`, SHA-256
`1dfc74dbd4896c95e15c6754d0d6f24eac08034bc6df790e5d14e813fd275025`.

Fresh standalone native watcher: `01a2133c-4d3f-7f20-be4c-5f9ab1a400c1`.
Its installed policy package is
`/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`, catalog
`1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`,
utility `dw_c699c3bf36ffc569cca1d7f83580bf68e6fffbb536cfad0d`.
The separate utility record and native TOML were read from that same selected
package. Actual native launch header verifies gpt-6-luna/low,
sandbox danger-full-access and approval never. Installed maximum is one; no
nested agent or second watcher was started. Parent native CLI tool session is
`85962`; parent stayed active through terminal result and effect reconciliation.

Expected duration: roughly 10–15 minutes pending substitution. No arbitrary
quiet timeout. Actual unexpected local kernel compilation is an authorized stop
and escalation; downloaded/substituted kernels are not compilation. Any failure
returns to its owner for diagnosis and lead coordination before another attempt.
The watcher observes only, with no diagnosis/retry/source changes/deployment.

## Evidence and current result

Final result: passed, all four target drv/output identities matched and are
registered valid; no target remains incomplete. Complete disposable evidence:

- `prepared.json`: refs, revisions, exact target identities and prior existence.
- `run.sh`: exact one-shot launcher.
- `build.log`: full Nix stderr/build/test output.
- `build-result.json`: Nix JSON realized output identities.
- `command-status.json`: authoritative original exit status and timestamps.
- `watcher-native.log`: complete native launch/observation transcript.
- `watcher-result.txt`: final result and owned cell/session accounting.
- Optional `escalation.json`: only if a concrete failure or >15-minute risk
  reassessment requires it.

All are beneath `/tmp/archive-failure-e-3mcseu33/`. No live service or managed
session lifecycle action is launched; VM lifecycle operations are isolated test
fixtures. Final reconciliation will bind actual outputs, checks/results, full
logs and all completed/remaining operation-owned sessions before acceptance.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/

## Safe-boundary duration reassessment

Actual one-shot start from the original native receipt: Unix1795619063,
2026-11-25T15:04:23Z. At Unix1795620097 elapsed was1034 seconds (17m14s).
The watcher's prose saying “beyond20 minutes” was not supported by its own clock;
parent uses the exact receipt/timestamp instead. Its earlier escalation.json
was created at439s, before the intended15min threshold, and had stale stage
text; it is evidence of that observation, not the authoritative current stage.

Read-only `nix path-info --json` now independently proves three exact expected
outputs realized/registered: runtime package check, composed application and site
composition. Full receipt: `/tmp/archive-failure-e-3mcseu33/reassessment-realized.json`.
The application NAR is `sha256-RkOrVrQUH16XU9dN3JhiFumWgZGJGI2KyvgLRpUWIQs=`;
package-check NAR `sha256-ND/d6MNX3JKp4zb8mdaag2VlTW8v5bS7PQ9VqddiPdo=`;
composition NAR `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=`.
Each registered deriver equals the prepared table. This establishes those target
realizations, not aggregate success while the original command remains active.

Only archiveVM remains. Original watcher log receipts show advancing guest
timestamps400.880552→605.208665 and the contended-archive browser revival step;
preceding commands passed. Frozen test source lines432–456 identify that phase.
Remaining required cases cover restart/worker interruption, unwritable parent,
checkout-removal recovery, registered-service cleanup/delete/automatic archival
and tracking-Git recovery. No failure marker or local kernel build was reported.
Continue the original necessary isolated VM: normal observed progress explains
the overrun and no shorter check can establish its still-unrun acceptance cases.
Next milestone: current revival completes, then remaining fixture cases and VM
terminal result. Reassess at20min elapsed/next meaningful boundary or concrete
failure. No new command, retry, source edit or quiet-time cancellation. Parent
reassessment receipt is `reassessment.json` in the operation directory.

At15:25:18Z elapsed1255s (20m55s), the original watcher receipt advanced
guest605.208665→825.387689 through later scenarios to the
`2026-10-25-preflight-permissions` browser archive in the unwritable-parent
refusal subtest (frozen test source aroundline491). Preceding VM setup/permission
commands completed, with no failure/kernel-compilation report. Three exact
registered targets remained complete; only the required VM remained. Continue
the original necessary suite with next milestone permission refusal followed by
checkout-removal and remaining service/tracking recovery; reassess at25min or
next meaningful boundary/failure. Root also reports accepted G mechanical refresh
`30b74dc3`/`fdcb0a2c` preserves exact app/composition derivations and complete
inputs; E retains its frozen original heads for the same result binding.

At15:29:17Z elapsed1494s (24m54s), original watcher receipts advanced
guest825.387689→1143.795323 to `2026-11-02-service-archive` fixture start/worktree
setup (registered-candidate cleanup subtest aroundline529). Unwritable-parent
and checkout-removal recovery phases advanced. No build/kernel error was
reported. Continue original required VM to service cleanup/interrupted retry,
then delete/automatic archive/tracking-Git cases; next meaningful boundary or
30min reassessment/failure. The estimate was low; observed advancing scenarios
support continued necessary verification rather than a hang or rerun.

At15:33:49Z elapsed1766s (29m26s), original watcher receipts advanced
guest1143.795323→1341.785858: registered-service archive/cleanup progressed to
confirming the unregistered fixture service remains active, then browser revival
of `2026-11-02-service-archive` near the end of that subtest (lines529–570).
Only required VM remains, without a failure/kernel report. Continue original
command to CLI delete interrupted-service recovery, automatic service cleanup
and tracking-Git retry; reassess next meaningful milestone/35min or failure.

## Final reconciliation and acceptance handoff

The exact original invocation completed with exit0. Authoritative shell receipt
starts at Unix1795619063 (15:04:23Z), ends at1795620908 (15:35:08Z),1845 seconds
(30m45s). `build-result.json` has exactly the four prepared derivation/output
pairs. Parent independently compared every pair and registered deriver through
`nix path-info --json`; no result depended on a branch/tree-only assumption.
The VM driver reports its test script finished in1689.35s and ordinary QEMU
cleanup completed in0.77s. No local kernel compilation or retry occurred.

| Target | Registered output NAR |
| --- | --- |
| runtime-package-check | `sha256-ND/d6MNX3JKp4zb8mdaag2VlTW8v5bS7PQ9VqddiPdo=` |
| archive-lifecycle-vm | `sha256-pQpattmS9VmO3ZIQUFn66az8GSmB4IvYhTTCFn6SUmo=` |
| composed-application | `sha256-RkOrVrQUH16XU9dN3JhiFumWgZGJGI2KyvgLRpUWIQs=` |
| site-runtime-composition | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |

The app's registered references match the accepted deployed-input boundary:
Codex `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0`,
worker `/nix/store/y3a1wlsbp8gj3j5raq7b9nm806a4fpvc-dev-workspace-pi-worker`,
runtime source `hh81k6...`, workspace source `cv964n61y041iyi3gp4nb76rgjhnx2nc-source`,
extension source `nma0v...` and tools `fjr83w...`. Full exact paths/references
are in final-path-info.json and the frozen complete D graph receipt above.
Eleven realized retained metadata/contract files were compared byte-for-byte
with the immutable installed1zn1a51 package: claim/integration/coordination
contracts, agent-team catalog, machine policy, Pi runtime/worker/provider/model
metadata. All match; raw names/SHA256s are retained-contract-comparison.json.
The composition check also passed against the realized selected app.

Native watcher reported completed inner tool session4635 and no remaining
owned processes/sessions. Parent outer tool session85962 completed exit0;
all parent wait cells completed. Former outer/native/script/Nix PIDs
3537591/3537609/3541076/3541105 are absent. The VM driver cleanup is recorded in
the full build log; no live/registered session service was launched or stopped
by E. All known operation-owned work is accounted for; no uncertain effects
remain. No session or utility lifecycle cleanup/archival was requested or run.

`completion.json` binds exact heads, command status, all target identities/NARs,
source/input receipts, utility/tool IDs and SHA256/size for every primary raw
artifact. The full build log is7,284,300 bytes, SHA256
`d9ee7b95da07d1bfd5b6689b564d885ace5815c06c5c450941b1267e9c9bbd9b`.
Final path-info receipt SHA256
`b7dfa126e082033215cd0c756ae7e9cc08b0fe2fb6e53576f1c8faf18c3606f1`.
These raw artifacts remain local under the operation directory; no code/input
commit was needed or changed. Long duration was the required multi-scenario
isolated lifecycle VM progressing to completion, not a reason to repeat checks.

E is complete for lead acceptance, with capacity for one next package after
acceptance; no new work is queued. D/F/lead own later compatibility freshness,
accepted G reuse, integration/claim/activation and actual usability. This result
is test/artifact evidence, not proof of deployment, a live archive/revive smoke
or permission for any session lifecycle action. No E source edits, added tests,
default integration, machine claim or deployment were performed.
