# Fixed instruction-file review

Team assignment from reviewer0 to lead:

Independent retained reviewer0 related review — fixed instruction-file contract
Session: 2026-10-03-automatic-session-slugs
Reviewer: reviewer0, saved review purpose / gpt-6.1-sol / xhigh / read_only; no override, fallback, authorship or nested reviewer. All four affected lanes reviewed directly; overall High risk. No tests, native/browser runs, writes, refs, deployment, merge or lifecycle operations performed.

Findings, ordered by severity:

1. IMPORTANT — General; Risk/verification — timeout controls can pass without reaching their intended native fault.
Commit d371a7721819ddc7becbd41eabd0486664e1edcd, codex/ephemeral_integration_test.go:585–625, 1361, 1402–1419, 1608–1615, 1653–1656, 1703–1704, 1888–1893.
New captureRPC calls synchronously run nft before forwarding request/response envelopes, while holding the proxy mutex. Each counter subprocess has an independent 100 ms budget. The timeout-config/model leaves retain a 400 ms caller budget (about 360 ms before cleanup reserve). Several permitted 80–100 ms samples during initialize/initialized/configuration can exhaust that budget before the designated config/read or model/list response is actually withheld. RunEphemeralTurn maps an inference deadline to context.DeadlineExceeded. These leaves accept that category alone and explicitly allow zero provider POSTs; no assertion proves the designated fault branch at 1417 ran while the utility was active. The separate ordinary connection can remain healthy because its request does not traverse this proxy. Therefore a leaf can report a successful timeout control while only proving an earlier handshake/configuration timeout caused by instrumentation.
This is a source-supported possible false-coverage path, not a measured timing reproduction or an explanation of the prior native failure.
Required action: record and assert that each designated real native RPC response was reached and withheld during that helper call; fail the control when it was not exercised. Keep the fixed deadline and final egress assertions. Reduce synchronous sampling cost if needed rather than accepting an earlier timeout or extending the deadline. A focused controlled slow-counter check can distinguish this path, followed by actual native evidence. Fix or explicitly discuss and record this Important finding before proceeding under the mandatory workflow.

2. ADVISORY — General; Architecture — diagnostic callbacks are not scoped to the leaf that created their proxy.
Commit d371a772, codex/ephemeral_integration_test.go:585–601, 1292–1313, 1361, 1404, 1429, 1572–1596; supporting existing lifetime behavior in codex/client.go:927–945 and codex/client_test.go:4673–4710.
The new inventory accepts callbacks based on one harness-wide diagnosticsActive boolean. run clears its IDs/phases and enables that boolean for the next leaf. Closing the client and HTTP server does not synchronously join the hijacked proxy handler; the handler joins its two readers only asynchronously. An old reader that has decoded an envelope but has not entered captureRPC can resume after the next leaf enables diagnostics. It then adds an old native phase/identity to the new leaf's inventory, with the new leaf's provider counts. diagnosticMu prevents reset during a capture already holding that lock, but does not fence a callback that enters later.
Impact is misleading phase attribution when diagnosing setup or egress changes, not a bypass of the final fixed-baseline deny assertion.
Suggested action: fence captures to the owning leaf/proxy with a generation token, or complete a bounded proxy drain before enabling the next inventory. Verify with a deliberately delayed old callback. A small ownership fix suffices; no generalized lifecycle framework is needed.

3. ADVISORY — General; Risk/bounds — the diagnostic read limit is 49, although the accepted contract says at most 48 including the final sample.
Commit d371a772, codex/ephemeral_integration_test.go:590, 609, 612–617 and 648–657.
The code allows 48 non-final capture calls to read nft. At capacity, after-utility-teardown bypasses the guard, performs another nft read, then overwrites entry 47. The existing pure test checks only that 48 entries remain. Thus retained output is bounded to 48 entries, but an event storm causes 49 counter invocations, including one additional independent 100 ms wait.
Suggested action: reserve the final slot (47 provisional samples plus the final sample), or otherwise account for actual reads within the stated cap. Verify invocation count as well as stored length. Preserve the guaranteed final sample and unchanged baseline/final comparison.

No Blocking finding. No additional finding in the public fixed-file contract, consumer ownership, scope, documentation placement or the carried-forward production paths.

Reviewed source and contract conclusions:
- Current clean exact heads are codex-web d371a7721819ddc7becbd41eabd0486664e1edcd, dev-workspace 8acd722029f3c1d0abd8c2801b734a554a4a2eef, extension 2e3733ade1bac712f0b852d1960a681e5bca5076, workspace 725db6717a82524776f1a687ae9ff96515168b79.
- Read the mandatory skill and all four full lane references, applicable unchanged workspace guidance/routes, affected repository guidance and documentation placement guidance. Reviewed plan/state, the accepted nonempty-file design correction, latest utility checkpoint, complete inventory, exact narrow deltas, actual committed code/tests/docs and pins. Narrow artifacts match the actual committed deltas; final/incoming artifacts match recorded current bases/heads. Unaffected worker/browser/upload/recovery and deployed lineage conclusions are carried forward.
- codex/ephemeral.go:29–32 and 340–366 define one provider-owned fixed nonempty text and validate exact size plus a len+1 bounded read before connecting. Canonical/private placement, regular owned 0600 single-link checks remain. The trusted local caller must preserve path and bytes through bounded teardown. The actual consumer portal/internal/web/session_namer.go provisions a unique per-call private file with the provider constant and removes its scratch directory after the helper returns. No duplicated consumer text rule or configurable arbitrary content was introduced.
- Pinned native core/src/config/mod.rs:3992, 4059, 4574 establishes that both file loaders run and reject empty/whitespace contents before explicit prompt precedence. Explicit base instructions still win after loading; blank inline compact_prompt normalizes away and the nonempty file supplies the compact prompt. Compaction is not disabled. This source diagnosis supports the correction; it is not observation of the original RPC error, proof of its complete cause, or a native pass.
- Both file-valued overrides remain. The restriction policy change is its synthetic file placeholder, not a tool policy change. Automatic model naming, disabled file/network action tools, pure clock, immediate question rejection, unchanged model/effort/catalog/binary and normal inference transport boundaries remain as accepted. I found no need for an empty-file compatibility shim, native patch, configuration lease or administrator-hardening framework under the trusted-operator boundary.
- Fixed diagnostic categories, numeric codes and bounded safe IDs avoid storing arbitrary error text/data/parameters/prompts/config/credentials. The error categorizer inspects a bounded prefix. I found no new lock cycle: diagnosticMu acquires h.mu, releases h.mu around nft, and relevant new provider paths release h.mu before capture. The findings above concern timing, leaf ownership and actual invocation accounting. Samples cannot attribute packets to utility versus native background activity.
- Owning docs/reference.md accurately explains the bytes, lifetime and model/compact precedence, with unchanged explicit HTTP/SSE fallback limitations; runtime docs/session-preparations.md explains provisioning/cleanup. Temporary failures, exact checkpoint state and rollout preparation remain in session records. Durable explanations are discoverable through owner documentation.

Explicit complete-history and migration conclusion:
- Assessed complete base-to-head histories and final/incoming diffs, not just the corrected tip: provider 4c170393→d371a772 (1 unit); runtime 924c0ec2→8acd7220 (7 units); extension 8f8d8ecf→2e3733ad (5 units); workspace a51fa51e→725db671 (1 unit).
- The provider directly introduces its final nonempty-file utility contract. Obsolete unapplied empty-file approaches, compatibility shims and superseded follow-up commit series do not remain. Adapter/test/docs and exact provider dependency updates are folded into their respective owning runtime units; the backend, adapter, dependency, frontend recovery, uploads and inherited seven-line race fix have coherent separately reviewable purposes. No commit-split finding.
- Exact consumed runtime 4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 and extension ancestry through 399c33023a568a8d7a21e4e4df52829628720a28 are preserved. The previously reviewed supported policy/storage/bootstrap migration lineage remains sound; production team-runtime bytes and runtime contract are unchanged by this correction.
- NO NEW MIGRATIONS for this delta or incoming feature: no DB, receipt/upload, state-root, namespace, host/lifecycle or package-policy schema migration, and no intermediate unapplied schema retained. This does not erase the supported already consumed ancestry.
- Workspace now has a51fa51e as its actual merge base. I verified the old f5 pin patch and rebased 725 patch are equal and the current-master-to-head diff changes only flake.nix/lock. The earlier upstream tracking-deletion/rebase qualification is resolved; unrelated records remain outside the feature patch.

Pins and remaining gates:
- Runtime Go pin v0.0.0-20261003234027-d371a7721819 and runtime flake source select the exact reviewed provider. vendorHash is sha256-wD6K+dw9W1zhBzFHwFGeNQ/HLGcDfVjdmyE2bhDomAw=. Runtime lock comparison changes only codex-web.
- Extension/workspace still package the prior ca0f3bc9 / 42be6ee5 / 2e3733ad composition. Their final exact consumer repins, assembled resources/source verification, package and CI checks remain mechanical release gates after native proof. These reviewed source heads are not a newly built/activated assembled package. Installed public helper hashes are stale; the unchanged candidate Codex 0.160.0 binary is reused for the corrected helper.
- Parent quick logs were inspected, not rerun: provider 12 top/74 test-and-subtest passes; tagged pure fixture 5/47; adapter and actual published-pin adapter each 5/12, all zero fail/skips. Pure fixture coverage excludes the actual native entry. Pinned config/schema and protocol coverage evidence does not replace native execution.
- Native ordinary control's eight sentinels/Luna-low passed at the prior checkpoint. The utility matrix has NEVER passed. All 36 prior leaves failed setup before inference; the original native RPC error and owner of denied packets remain unobserved. The corrected helper requires an actual native rerun with all matrix/positive/egress/persistence gates intact and meaningful timeout-control reachability.
- Existing actual Chromium creation/team, runtime race, old-source compatibility and host-VM evidence concerns unchanged paths and is carried forward. No new native, full package, deployment, live canary, merge or lifecycle result is claimed.
- Successful WS frames, continuation caches/reconnects and hostile WS delivery remain outside explicit HTTP/SSE fixture coverage. The later positive live-model canary must use unchanged serving transport and demonstrate model-generated naming rather than deterministic fallback.
- No default integration or lifecycle action is authorized. Parent owns reconciliation and recording. Reviewer remains available; session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/

## Lead reconciliation

The lead accepts the Important verification finding and both Advisory diagnostic
findings. A bounded fixture-only remediation is assigned to retained
implementer0. Preserve the actual fault reachability, original deadlines and
fixed deny-counter assertions; fence late callbacks and account for the final
sample in the existing bound. No native run may start before the lead inspects
and verifies the fix. This is direct remediation under mandatory review step9;
a new design or expanded boundary would require affected-lane review under step10.

## Direct remediation inspection and first quick check

Implementer froze a fixture-only diff at turn01a1043c-b048-7b12-b260-069f0d611e54.
The lead read the full diff: explicit active-call response proof, nonblocking
single-flight private counter sampling, leaf generation fencing and47provisional
slots plus the guaranteed final slot. Public helper, runtime, policy, model,
metadata, transport and native400ms/final-deny assertions are unchanged. Pure
regressions deliberately block a counter and delay old captures/results.

The owning Nix7group focused -race run exited1in1.633s. Six groups and58test/subtest
cases passed without a race report. Only the two new earlier-handshake negative
controls failed: they expected DeadlineExceeded but observed the static existing
ErrEphemeralServer after0.37s, with no target response proof. This is a negative
fixture expectation failure, not a native result. Retained implementer0 is
correcting only that expectation at turn01a1044d-2379-7562-aac9-50ac38a30f69;
positive controls and actual native timeout assertions remain strict. Log:
`/tmp/automatic-session-slugs-fixed-file-remediation-quick.jsonl`.

## Reconciliation complete

The two negative controls now observe an actual initialize request at the
nonresponding peer, require failure and reject target-response proof. They do
not force an unrelated handshake error category. The lead read this correction;
positive and actual native timeout checks remain unchanged.

Corrected owning Nix -race check passed all7top-level groups/61test-and-subtest
cases, zero failures/skips,2.629s. Log:
`/tmp/automatic-session-slugs-fixed-file-remediation-corrected-quick.jsonl`.
All three review findings are closed by direct inspection and meaningful focused
verification under step9. No new public design or boundary was introduced, so
step10 does not require an unchanged-lane review rerun.

The fixture-only fixes were folded into the provider's single owning unmerged
unit: local5f6c7e255c2bd18361107cf322be1ec3e3e91ea2. Its delta from reviewed
d371a772 changes only ephemeral_integration_test.go. All17public Go files and
policy remain byte-identical to the independently reviewed fixed-file source.
The retained pre-remediation ref preserves d371a772. Runtime8acd7220, extension2e,
workspace725 remain clean/unchanged. No new migrations or superseded follow-up
series; consumed lineage and all other review conclusions remain intact. This
clears the source gate for native observation; it is not a native isolation pass.
