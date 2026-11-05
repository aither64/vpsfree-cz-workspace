# Final affected installed-service diagnostic review

## Findings and disposition

**Blocking D1 — the diagnostic wrapper makes the original native cleanup proof
unreachable. OPEN at reviewed d07e8f2d.** General lane; also affects scope and
verification risk. Source:
`nix/tests/session-archive-lifecycle.nix:404-429`, commit
`d07e8f2db5b8045a10aa65cdc2df5efe83909e29`.

The added details GET and try/except are dedented out of the existing registered
candidates/descendants subtest. All nineteen original trailing statements at
lines 411-429 are now inside the exception handler after its unconditional
raise at line 410. A successful count assertion skips that handler; a failed
assertion raises before the original tail. Neither path can execute the HTML
privacy assertion, invocation-mismatch refusal/files-preservation check,
same-operation retry, native stopped/retired proof, unrelated-service preservation,
revival proof or fixture foreign-service stop. The subtest can appear successful
after only its CLI count check, contrary to the diagnostic-only scope.

The evaluated script has the same defect: exception handler at line 361,
unconditional raise at 363, followed by nineteen unreachable original statements.
Syntax checks pass because the code is legal Python. The retained fixture control
compares assertion expressions through ast.walk, which ignores control-flow
reachability, and executes only the extracted diagnostic function.

**Smallest remedy:** keep the GET and failure-local try/except inside the original
with-subtest body; indent only its assertion/diagnostic/raise one level deeper,
then keep the original tail as ordinary sibling statements after the try/except.
Preserve the one GET and exact original assertion. Add a focused structural or
existing-control check that a successful details assertion reaches the original
privacy/invocation path, with the remainder outside the exception-after-raise
body. No new harness or product behavior is needed.

Sent promptly to lead; lead accepted Blocking D1 and assigned A this exact narrow
remedy. Source/VM build gate remains held. A's mutable remediation is excluded
from this review and is not certified here. Lead can close the requested narrow
fix through skill step 9 focused source/check/source-identity inspection; a new
boundary requires affected follow-up review. **Do not start long observation on
this reviewed defective source.**

No additional Important or Advisory finding was identified in the Go diagnostic,
privacy, sampling or documentation changes. The overall source gate is not
accepted while D1 is open. This report supplies no publication, candidate-build,
VM retry, deployment, integration, machine-release or lifecycle permission.

## Identity, guidance and exact source

Retained independent `reviewer0`, purpose `review`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, saved
`gpt-6.1-sol` / `xhigh` / `read_only`. Fresh live roster revision 27 confirms
ready state and settings. No override, fallback, substantive authorship or nested
agent. Before session-record access, `dev-session current` printed exact bound
slug `2026-11-02-session-temporary-service-cleanup`; both environment markers
matched that slug and `/home/aither/workspace/ai/vpsfree.cz`, agreeing with the
trusted developer binding.

Read full mandatory-change-review and all four lane references, applicable
workspace/repository guidance, current plan/state and final design including
sampler clarification, authoritative receipt, immutable source/diff, existing
cache/process-group ownership, actual quick evidence and failed-driver inventory.
Unaffected prior service/capacity/machine/rootless/creation/pin conclusions are
reused. Risk is High for privacy and host/consumer verification, without changing
saved reviewer effort.

Repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Affected range:
`0872c5079396fa5763f3ae8d9a30b506010106d1..d07e8f2db5b8045a10aa65cdc2df5efe83909e29`.
Head tree: `a3da172e966038aa566ab12a9da9c250071565fe`.
Whole range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..d07e8f2db5b8045a10aa65cdc2df5efe83909e29`.
Exactly six changed paths, 384 insertions/33 deletions: existing diagnostics and
service-reader Go files/tests, existing archive VM fixture, and the existing
workspace-portal diagnostic paragraph. Whole branch: 96 files, 8156 insertions/
426 deletions. Review binds submitted immutable d07 only.

## General correctness and producer outcome preservation

The service read adds a services timing stage while keeping the public loader,
strict decoder, command arguments/cwd/environment, unknown count semantics and
identity-before/after checks intact. Independently compared full decoder and
loadServicePage functions: byte-identical to 0872. Entire cache, process-group,
bounded-buffer and Ruby service-owner files are also unchanged. Producer 5-second
deadline, success TTL, flights/bytes limits, native owner budgets and cancellation
contracts remain their existing values.

The small serviceOutputBuffer wrapper delegates the same bounded-buffer Write
and records observed byte counts/limit failure without retaining more contents.
Stdout remains limited to 1 MiB; stderr remains truncated at 4096 bytes. Helper
completion is awaited by processgroup.Run before the counters/process state are
read. Failure classification uses the actual producer context at that boundary,
then records fixed start/exit/output_limit/deadline/canceled outcome before
returning the original coarse service error. Strict decoding failure records
projection/invalid; identity and cache-wait failures receive their own categories.
No raw error string crosses the new diagnostic boundary.

The first HTTP waiter's context is retained only for trace/correlation; the cache
still owns the producer context and cancellation. Coalesced waiters do not acquire
invented producer identities. Documentation correctly says the correlation names
the request that started the shared flight, including after that waiter departs,
and does not identify every waiter. Trace fields/stages use the existing mutex;
correlation/start are immutable. The cache-wait conversion cannot erase an
already-recorded producer context fact. A producer completing after the HTTP log
has a separate opportunity to emit its outcome.

## Architecture, proportionality and privacy

The concrete installed failure discarded the precise helper/context/parse branch,
so a bounded diagnostic addition is justified before choosing any correction.
This extends the existing read-diagnostics owner and existing reader seam. One
local buffer wrapper, one fixed service-failure recorder and one shared sampling
helper serve the actual callers. No new logging framework, collector, CLI,
configuration switch, schema, probe or generalized retry mechanism is introduced.
The tests target owned error conversion and cancellation rather than duplicating
an upstream native implementation. D1 must be corrected; the rest of the design
is proportionate to the demonstrated evidence gap.

Stage/outcome switches admit only fixed vocabulary. New production records contain
correlation, stage/outcome, elapsed milliseconds, numeric exit code and byte counts.
They contain no helper stdout/stderr, argv/environment, paths, labels, units,
cgroups, registry/native IDs, credentials or raw errors. Existing display payloads
and ownership semantics are not broadened. No successful producer heartbeat is
added. Unknown/malformed public projection still refuses as before.

The separate lastServiceLog atomic timestamp is inside the existing diagnostic
state. Its 1/sec admission is independent of the existing portal_read 1/sec
admission, so a coarse read log cannot consume the producer slot; combined rate
is bounded at two records/sec. cache_wait stays on the per-request trace rather
than emitting a producer record. Independent concurrent producer failures may
still be sampled out; docs explicitly preserve that limitation. The implementation
does not claim every failure or waiter is logged.

The failure-local VM projection selects exact booleans/count range, status and
strictly shaped correlation/timing fields. Header read is bounded to 4096 bytes;
service journal is limited to 80 records/32768 bytes. It extracts fixed/numeric
fields from matching correlation records, keeps at most two, and prints no raw
header/journal body or exception text. There is no extra GET/poll/service launch.
This helper's safe projection is useful, but D1 currently places it around the
wrong control-flow structure and prevents required later proofs.

The existing documentation paragraph accurately describes fixed metadata,
independent rates, origin correlation, late producer outcomes and sampling.
No new documentation bundle or operational procedure is introduced. Main's prose
pass is retained; this review found no further documentation issue.

## Verification and causal limits

Matched authoritative final-receipt SHA256:
`466b637e697a5b3432a1eec265e5005142e5a4cb7ffb866fbcfc50a99fed5307`.
All six quick-manifest source hashes match the exact committed immutable source.
Read actual command, manifest, result and Go JSON events: 29 top-level tests /
47 cases, zero failures/skips, package 6.328 seconds; full batch exit 0 in
35.974743 seconds. Cases cover real helper start/nonzero exit/5-second deadline,
projection/size/identity/cache, departed/shared waiters, independent sampling and
secret canaries. These are retained author/watcher results; I ran no checks.

The initial sampler-test failure is honestly scoped to reusing one trace for a
second hypothetical producer; its correction does not weaken production. The
wrong-CWD watcher preflight launched no tests. Neither is hidden as a successful
run. The stored evaluated script parses and pure safe-evidence controls pass,
but their assertion-text comparison missed D1. That quick evidence cannot support
an unchanged-native-proof claim until the focused reachability remedy is verified.

The retained installed-driver command log SHA256 is
`7396fb17a83b62c924e7a363618ca3791a2f6b43d47c066edf0c38a3a47444c9`;
readonly inventory SHA256 is
`a231d06b0957de5bd82c887b81e2c5fd81cbd567a7bde584f553cada815fd64e`.
They bind exact deployed SITE hyjx/runtime0872 to one exit-1 run after
1076.437336 seconds. CLI count3/len3 preceded details known=false/value0 and
servicesKnown=false at the original assertion. CLI 6.92s and details 5701.07ms,
including 5034.72ms unattributed, fit a 5-second producer deadline but do not prove
it. The actual helper branch remains UNKNOWN: stderr/exit/context/headers were
not retained. This diagnostic source is evidence collection, not a producer fix.

Generic0872 fast/creation/archive success remains valid for its exact scope; the
failed installed SITE verification is not accepted. Health/Team/roster and native
PID continuity passes do not substitute for that failed proof. No candidate VM,
new selected package, new pin or final installed success has been established.
A later nonreproducing diagnostic pass would cover only its own attempt and
would not identify the original failure branch automatically.

## Complete history, migration and consumer provenance

Independently inventoried all seven commits:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources/Team UI.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — registered service owner/lifecycle.
3. `5b4b711748343f4ffe88b96c50d88a9f98eeb04d` — dependent portal/package integration.
4. `530ff55fd467b1a453f8f2aa882ffaa45daba244` — capacity proof and fixture support.
5. `2718f833f54d87c4df9cbb81b48569094a30cd05` — machine claims.
6. `0872c5079396fa5763f3ae8d9a30b506010106d1` — rootless stop.
7. `d07e8f2db5b8045a10aa65cdc2df5efe83909e29` — safe service diagnostics.

All six deployed commits are exact ancestors; d07's direct parent is deployed
0872. The separate diagnostic commit is coherent follow-up to an actual installed
failure. Do not rewrite those deployed ancestors. The saved seventh diff equals
the actual committed delta, SHA256
`2627ce70cec7e98a65b417ab6a6e28c045609961f352125cbca4f3fc37470e73`.
No obsolete history, abandoned approach or transitional update stack remains in
this submitted series. D1 is a correctness defect, not grounds to preserve a
superseded unconsumed follow-up: its requested narrow remedy should fold into the
owning local diagnostic commit while retaining reviewed-source evidence. Any
future superseded local follow-up must likewise be consolidated.

**No database migrations.** The diagnostic delta adds no persisted format,
public JSON API, schema or capability. Previously accepted service schema 1 and
supported retry/claim schema-1/direct schema-2 provenance now includes actual
0872 production selection. Those supported readers/contracts remain unchanged;
there is no new transitional migration or obsolete conversion. Migration lineage
is sound under the retained content conclusions.

**No new or repeated dependency/input update stream.** Runtime flake.lock,
go.mod/go.sum selections remain unchanged through this range. Consumers remain
workspace684ac, extensionf8da and configab447 selecting 0872, with policy/catalog/
full graphs certified by review-final-pins.md. Diagnostic d07 is local, unpublished
and unselected; no hypothetical pin or selected equality is accepted.

## Immutable source and operational boundary

Independently recomputed source NAR:
`/nix/store/2aqz0x3029y871dffx3lldx4pnkjskka-source`
→ `sha256-a2MbpkGC8ANKzUcU+ii2nE5c/UbWa5vebIUswxVU49w=`.
All 679 Git entries match immutable bytes, symlink targets and executable modes,
with zero missing/extra entries. Full nine-node graph, raw edges/follows and
originals are identical to deployed0872; lock SHA256 is
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.
The active source-root resolves to this exact source and remains intact.

Recorded deployment is system96304/configab447 plus SITEhyjx/workspace684ac/
extensionf8da. Lead retains the held machine claim
`5af5ab4e-b640-41b2-a8d0-3284c0955ba9` because installed verification is incomplete.
This review neither inspects nor changes live ownership, selected paths or
processes. Historical first ambient invocation effects remain UNKNOWN independently;
later isolated evidence does not certify them.

No reviewer tests, builds, evaluations, GH/CI/native/live probes, cleanup,
source/Git/store mutations or nested agents were performed. Only read-only source,
static AST/history/hash/evidence inspection and this permitted report write.
Prior reports and roots remain unchanged. Session stays open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
