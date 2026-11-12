# Exporter final independent review

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh/read_only, thread 01a1c742-93c5-7c50-b59e-f792fafd9624.
Mode: final committed-deliverable review of exporter package I only; high risk; general, architecture/repetition, scope/proportionality, risk/compatibility lanes.
Reviewed range: 7c5a8e74e44a704cceb99cd05716af6800d78efd..9a5b3d1c5a970d7bdc8c4771f0c24f3d9ec2b052.
Decision: no Blocking findings; one Important finding requires a narrow fix or explicit recorded decision before continuing. One Advisory coverage gap. No deployment or integration approval is implied.

## Findings

### I1 — Important — General / risk — rate pacing bypasses the finite driver deadline
Commit 9a5b3d1c5a970d7bdc8c4771f0c24f3d9ec2b052, scripts/benchmark.py:271–274 (preceding deadline check at 260–261).

The rate-controlled path calls time.sleep(delay) without limiting that sleep to the remaining run deadline. A valid low offered rate can keep the driver and its exporter/rsyslog children alive long after --timeout and defer the finally cleanup. For example --records 2 --rate 0.001 --timeout 2 can enter a roughly 1000-second pacing sleep before the next deadline check. This contradicts the advertised finite-run timeout and the explicit requirement to bound fixture ownership.

Independent read-only reproduction: parsed the committed script with Python AST, executed only its existing pacing block with started=100, sequence=1, rate=.001, now=100 and deadline=102, replacing sleep with a recorder. It requested sleep=1000 seconds with only 2 seconds remaining. No process/service was launched by this reproduction.

Smallest fix: limit pacing waits to the remaining deadline and raise the existing finite timeout once it is exhausted, entering normal finally cleanup; do not add a scheduler/framework. Check the low-rate/short-timeout case with a fake clock or a tiny finite owned fixture, including prompt child reaping. Fold the narrow correction into the owning unmerged commit if appropriate and rerun relevant quick checks. This direct remediation does not itself need another whole review.

### A1 — Advisory — General / risk — captured HTTP fixture is not checked
tests/runtime.rs:94–140; tests/fixtures/http.json; src/http.rs:54–58.

The only HTTP regression exercises GET /metrics, content type, partial-header clients and server stop. The captured http.json is never consumed, so fallback status/body and configured gzip negotiation are not regression-checked despite the broader contract fixture evidence. There is already an incidental difference: pinned tower-http 0.6.11 does not add Vary for the two-byte fallback below its default compression threshold, while the Ruby fixture records Vary: Accept-Encoding there. The known monitoring consumer uses ordinary GET /metrics, so I found no current consumer break from this header difference.

A small in-memory router assertion for the supported fallback and gzip behavior would close the meaningful gap; explicitly exclude incidental headers if they are not part of the supported contract. No full upstream HTTP conformance suite is warranted. The lead may accept this as a recorded residual gap.

## Scope and proportionality

Compared the actual user request recorded verbatim in plan.md and subsequent implementation/no-deployment decision in state.md with the full diffstat and milestones before detailed hardening. Requested scope is complete Ruby-to-Rust replacement, equivalent rsyslog metrics, better measured flood performance, Rust tooling/CI and the single configuration consumer; no broker, durable state, fleet rollout or unrelated Ruby removal.

The final diff has 64 files, +3475/-1440, including 1086 generated Cargo.lock lines and complete removal of the roughly 1419-line Ruby runtime/test/tooling surface. The recorded I execution milestone is approximately 21:21–21:52 UTC, about 31 minutes, with contract capture, implementation, quick checks, publication and CI delivered; longer verification is explicitly separate. These approximate dispatch milestones do not establish exact active working time.

The implementation remains proportionate: one FIFO/state owner, ordinary host maps and cached handles, maintained parser/metrics/HTTP dependencies, a small fixed diagnostic namespace and one finite driver. No speculative broker, persistence layer, collector plugin framework or production transport-policy change was introduced. The TCP/UDP/local driver modes address the actual central producer paths. Do not expand cardinality policy or add transport infrastructure merely to resolve hypothetical future load. Correct I1 within the existing driver.

## Source and behavior conclusions

Read all source files, tests, fixtures and shipped documentation, the complete commit message/history/diff, the original Ruby parser/collector/expiry/entry-point contracts, and the retained Ruby fixture capture script. No repo-local AGENTS.md exists in the exporter tree. Read the applicable workspace procedures and all four mandatory review references. Session current was confirmed from the assigned tracking directory; environment identity variables were both absent and the exact trusted binding matched. Live roster confirms the retained identity/settings and independence.

- The actual captured startup/triggered/expired exposition and Rust assertions cover all 18 literal legacy names, HELP/type/label sets, metadata-only families, empty namespace, escaping, startup zeros and retained expired zeros. Golden normalization is limited to order and equivalent numeric rendering for these finite samples.
- Source comparisons confirm host/FQDN first-match routing, additional WebUI opt-in, vpsAdminOS gates, detector ordering/exclusions, LXC prefix ID behavior, one-per-message WebUI classification and the final-newline command case. The deliberate first-record, malformed-record and kernel PID/forwarded fixes are explicit.
- Framing is bounded per configured line, rejects oversized input once through LF, resets incomplete input on EOF, and closes the old descriptor before backoff. Capacity enlargement refusal is nonfatal and actual capacity is exposed. Reopen/idle processing services expiry. One owner orders updates/monotonic renewal/strict expiry and handles already-read records on shutdown.
- Fatal input errors propagate to process failure through main, rather than leaving a permanent HTTP-only process. HTTP uses separate runtime/encoding work and detached response bytes; connection/encoding admission and connection lifetime are bounded. Cached handles avoid registry lookup for existing series. Slow clients do not own ingestion state.
- These bounds do not bound total memory: dynamic series/caches remain retained, and registry gather/new-series creation can contend. No new cap/eviction is required by this review. A very large encoding job and combined FIFO/HTTP load have not been independently stress-tested here.
- No additional concrete exporter runtime correctness/security defect was found within the supported contract. Review is not a performance or end-to-end losslessness certification.

## Consumer / compatibility boundary

Inspected representative configuration default 3c088a4b71881b3649441ce3c4e92c71757708e6 package/service/log-host source plus its actual alert/scrape consumers, and the same-session prepared service/docs as context. Old consumers use FIFO JSON settings and literal names/pulse gauges; the prepared --config/--listen Type=simple launch agrees with the new binary and deliberately removes unsupported Puma notify/watchdog behavior. FIFO, account, port and host labels remain the consumer-owned boundary.

C2's exact Rust package pin/source/hash and final committed configuration are still pending. This report does not finally review the uncommitted consumer or certify its final build/input graph. Exporter replacement can coexist with existing senders and monitoring without coordinated node updates, subject to measured pinned-producer behavior. No state conversion is introduced. Cutover must retain one reader; counters/pulses reset in either direction, and software rollback cannot recover already lost FIFO events. Rsyslog short writes/overflow/restart and UDP loss remain upstream risks, accurately disclosed rather than claimed solved.

## Whole-branch history and migrations

Independently verified HEAD and merge base, complete base-to-head log, final diff and range-diff against superseded 3372f218f5d6ced94bfa5e732c5b8ede320b19c4. The reviewed branch contains one functional commit introducing the final design directly. The superseded pre-review candidate differs only in driver receipt bookkeeping and is absent from the reviewed series. No obsolete approaches, compatibility shims, fixup chain or transitional history remain in the current series.

The runtime, Ruby removal, Cargo/toolchain, parity tests, hooks/CI, docs and finite verification driver form one reviewable replacement; supporting artifacts belong with the behavior they build and validate. C2 is correctly separate. There are no repeated dependency/channel/pin update streams; Cargo.lock represents the one final graph. No superseded pin commits require retention or further consolidation.

No migrations. Neither old nor new exporter introduces a persisted application schema/format, and there are no migration files or intermediate state transitions in the full branch. No reviewed candidate is reported merged, released or deployed; no externally consumed intermediate migration is present. Source agrees with the no-migration inventory.

## Documentation placement and preservation

1. README is a useful purpose/start entry point and links reference, verification and fixture provenance; it keeps the existing-FIFO/single-reader prerequisite and listener exposure beside startup guidance.
2. Lasting input/config/metrics/expiry/failure semantics belong in exporter docs/reference.md; developer/test/measurement instructions belong in docs/verification.md; fixture provenance belongs beside fixtures. Site cutover/rollback belongs in the separate configuration operations guide. Execution heads/results remain in session packets/state.
3. Shipped exporter reference is usable without private session access and contains no temporary branch status.
4. Commands and runtime descriptions generally match source and evidence. Measurements are explicitly future work; tiny debug smokes are not represented as capacity results. I1 is the concrete timeout fidelity exception; A1 limits HTTP fixture coverage.
5. Original README had only the named-pipe purpose, so no existing recovery prerequisite/anchor was lost. New docs preserve loss, EOF, single-reader, capacity, reset and rollback limits.
6. The supported Ruby-to-Rust recovery contract retains the prior generation and same FIFO/state/log paths in consumer operations context. No old persisted-state migration or retirement is invented; C2 final operations fidelity remains for its separate review.
7. One owning exporter reference explains the public contract, with working local links; consumer site operations remain separate. Hook guidance correctly distinguishes standalone clones from linked-worktree shared config.

Conclusion: documentation placement and preservation are sound, subject to the concrete timeout exception and recorded HTTP coverage gap. No lost supported recovery path was found. The disclosed shared hooksPath correction cannot independently prove that no earlier custom setting was overwritten, because its old value was not captured; current effective override is absent and this historical uncertainty is retained, not silently certified.

## Independent checks and remaining gates

- Fresh read-only SSH ls-remote confirms feature head 9a5b3d1c5a970d7bdc8c4771f0c24f3d9ec2b052 and master 7c5a8e74e44a704cceb99cd05716af6800d78efd.
- Exporter tree/index are clean; git diff --check passes. Checked executable modes for hook/check/driver.
- Inspected final amended-commit hook log: formatter/Clippy plus all 12 tests pass. Re-ran the existing compiled in-memory contracts binary: all seven contract tests pass in 0.03 seconds, including pinned Ruby wire parity. This reuses the existing binary, not a new exact-source build.
- CI log reports run 42908713683 success; packet binds its exact head/attempt. I did not independently query GitHub's run/head metadata. Existing finite driver receipts show counts and clean child exits for the recorded tiny smokes; they are not capacity evidence.
- Read-only AST pacing reproduction confirms I1 without sleeping, modifying files or starting services.
- No application edits, file writes, nested agents, builds, long tests, production access, deployment, merge, lifecycle action or cleanup were performed.

After I1 is fixed or explicitly decided: C2 must pin the final reviewed/fixed published head and receive its own final review. Then V still needs matched release Ruby/Rust measurements, three matched repeats, ordinary/OOM/cardinality profiles, normal/slow scrapes and RSS trends, actual pinned-rsyslog size/overflow/reconnect/restart/partial-write experiments, observed-stage loss accounting and promtool where available. Source review does not close these gates.

This role is read-only, so the requested exporter-final-review.md was not written. Please save this report verbatim at work/2026-11-10-rust-syslog-exporter/exporter-final-review.md and reconcile decisions/fix evidence in state.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/
