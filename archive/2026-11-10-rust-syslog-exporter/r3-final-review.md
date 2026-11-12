# R3 affected final independent review — I3 compatibility correction

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh/read_only, native thread01a1c742-93c5-7c50-b59e-f792fafd9624.
Risk: high. Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Complete reviewed provider range: 7c5a8e74e44a704cceb99cd05716af6800d78efd..891db6b82ccd37e985507c654050143e165041a7.
Affected substantive comparison: 6ecada0a9d2f6457a11031a3a4ffc341584fb29c..891db6b82ccd37e985507c654050143e165041a7.
Final tree: 4b28b6924e042ebf7582b9a0a91eea0bbbddc429.
Accepted design.md SHA256 independently verified: c63269ba0005b647836f8b8e718e33d368c22e145588790d57739e68eff50f65.

## Findings and disposition

No Blocking, Important or Advisory findings in the I3 affected source, tests, documentation or final provider history.

R2/P2's source-level requirements are implemented: ASCII shorthand/strip and colon-zero behavior now match the agreed Ruby results, and intact alert signatures can survive invalid bytes in a body without repairing invalid header identities or joining interrupted signature fragments.

R3 final source review is complete. It does not block the lead's next dependent consumer preparation and release-verification steps. It does not close deployment verification of the still-running3hk artifact, certify successor performance, grant integration/activation authority or assert universal byte-label equivalence.

Preserve the earlier complete exporter, C2 and I2 reviews for independently unchanged scope, plus R2/P2 evidence. This report reviews the substantive successor rather than calling it equivalent to deployed6ec.

## Identity, guidance and actual scope

Reverified dev-session current from the assigned session directory and the exact trusted thread/workspace binding. Both DEV_SESSION identity variables are absent. The live roster confirms the same ready independent review-purpose member, saved model/effort/access and native thread; no override or delegation was used.

Read/reused applicable workspace guidance and the mandatory-change-review skill with all four lane references, plus the actual plan/state, accepted D7, current owner packet, compatibility/parity disposition, changed code/tests/docs and source/check/history receipts. No exporter-local AGENTS.md exists.

Compared the original fast same-metric replacement request and later explicit fix/essential-service direction with the diff before detailed hardening. I3 is10 files, +438/-39 versus6ec, mostly focused regressions. Recorded source release was about22:44Z and the final commit is22:58:31Z; focused all-target compilation/checks129s, full quick68s and final active hook8.38s are explained milestones, not an unexplained broad campaign.

The change stays within D7: one raw-header/body boundary, standard borrowed/lossy text, exact finite ASCII/strip corrections, one fixed counter and relevant fixtures/docs. No new dependency, queue, worker, option, transport, nested-RFC5424 decoder, codec framework or speculative cardinality policy was introduced. The diagnostic has a concrete purpose after bodies stop being whole-record rejections; it is not an additional monitoring subsystem.

## Parser and body policy assessment

src/parser.rs:27–38 finds literal ASCII separators in raw bytes and validates the outer date/host before routing. The ordinary branch validates the raw program at48–53. Header strings borrow from validated input; invalid header bytes are not replaced into a known host/program or label. Empty required fields still reject. Outer timestamps retain the accepted RFC3339 subset.

The supported svlogd recognizer at5–7 is an anchored bytes regex with explicit ASCII digits. It inspects the prefix without requiring the whole remaining body to be valid UTF8. Once recognized, inner host/program are strictly decoded at42–46. Prefix date/time bytes are already constrained by the ASCII match. A nonmatching prefix retains ordinary fallback; the implementation does not promote header-looking text later in an ordinary body. There is no recursive nested RFC5424 interpretation, and the two exact user records remain program1.

PID matching now uses [0-9] at11. Namespace whitespace at8–10 is exactly the agreed six ASCII characters while other Unicode text remains literal. These corrections avoid the confirmed Arabic-digit kernel normalization and NBSP namespace-label drift. Existing ASCII PID/kernel and accepted forwarded-kernel normalization remain.

Only the selected raw body passes through String::from_utf8_lossy at68, stored as Cow<str>. Valid bodies are borrowed and unchanged; there is no new common-path body allocation. Invalid bodies are decoded once into owned text. Every collector and body-derived label sees the same decoded text via Message.body; no collector re-decodes it independently.

Standard U+FFFD replacement preserves a nonempty separator at invalid sequences. Consequently an intact ASCII signature before/after invalid bytes remains searchable, whereas deletion cannot synthesize a signature across the invalid span. Invalid sequences inside a command/namespace/id can affect its label text as explicitly documented. Distinct invalid sequences and literal U+FFFD may coalesce; the code/tests/documentation do not present this as lossless Ruby byte-label equivalence.

The raw FF nodectld case now reaches message count and crash detection, while the interrupted Daemon cra<FF>shed case does not flare. This resolves the agreed operational concern without accepting invalid header identities or broadening header grammar.

## Collector, diagnostic and framing assessment

src/collectors.rs:157 obtains one borrowed view of the already decoded body. Existing detector strings, program/OS/opt-in gates, precedence, timing and counter/flare operations are otherwise untouched.

LXC extraction at182–189 explicitly handles no colon -> empty, positive colon -> preceding prefix and colon0 -> whole body. trim_matches contains only NUL and the six agreed ASCII whitespace characters. This restores both NBSP preservation and the separately accepted Ruby0..-1 quirk; no new numeric-ID validation was added. Byte indexing at an ASCII colon is a valid UTF8 boundary.

src/input.rs:67–75 increments body_decoded exactly once for a successfully parsed owned body, before Engine.process performs known-host routing. Header/parser failures cannot increment it; unknown-host repaired records do. Multiple invalid sequences in one body count one record. The diagnostic is an ingestion-record measurement, not a count of replacement code points.

src/metrics.rs:199,216–219,242 registers one fixed unlabeled counter with a precise HELP string. Legacy SPECS/handles and encoder content were independently verified unchanged. No payload-derived diagnostic dimensions or payload logs were introduced. Existing utf8 rejections now cover header decoding, consistent with the new body policy.

Framer bounds and LF/EOF processing are unchanged except the decode-counter wiring. Complete raw frames are length-checked before parse/decoding; oversize discard and partial-tail rejection still occur on raw bytes. A multibyte sequence split across reads is reconstructed before decoding. Lossy output is linear and at most three output bytes per input body byte; allocation is bounded by the configured one-record limit, not an unbounded queue. This does not establish a total cardinality memory cap.

## Regression quality and verification

Inspected all changed tests directly. They assert actual parser fields, representation, collector outcomes, exposition labels and diagnostics rather than mirroring only a helper.

The six added focused tests cover:
- Valid bodies/literal U+FFFD staying borrowed, invalid/truncated bodies using owned replacement text and LF retention.
- Invalid outer timestamp/host/program and recognized svlogd inner host/program rejection; recognized forwarded invalid body acceptance; ordinary fallback and Unicode-prefix nonrecognition.
- Both exact233-byte user records remaining program1/no kernel flare, plus direct FQDN/kernel, kernel[], ASCII PID, leading-MSG-space/OOM and isolated svlogd controls.
- U+0661, NBSP namespace and LXC labels, ASCII/NUL strip, colon-zero/no-colon/normal-colon outcomes.
- Intact versus interrupted nodectld signatures, one decode count per parsed record, unknown hosts, no decode count for invalid headers and unlabeled counter exposition.
- Replacement-label coalescence, body-derived namespace/id/command values, split/truncated UTF8 framing, raw byte limit, oversized recovery and incomplete EOF.

The real FIFO regression additionally ingests an invalid UTF8 body and verifies the nodectld flare and new diagnostic while preserving split/coalesced records, EOF/reopen, capacity fallback and shutdown coverage. This is meaningful coverage of the changed input/alert contract; exhaustive upstream decoder conformance testing or an allocation-counting framework is unnecessary.

Independently reran only the six focused in-memory tests from existing compiled binaries:2 parser tests passed in0.01s,4 contract tests passed in0.09s. No build, temporary service or test-file write was performed. Reusing those binaries is supplementary quick evidence, not an independent exact-source release build proof.

Inspected the final active amend-hook log: formatter/Clippy and25 tests pass (8 library,11 contracts,6 runtime). Focused/full check receipts agree. Current-head CI was unknown/pending in the supplied checkpoint, and the previous6ec observer's HTTP502 is not a passing new-head check. I did not wait for or independently query CI, and do not certify it green. Review completion does not require pretending the provider outage/queue was resolved.

Fresh SSH ls-remote independently confirms published feature891db6b8 and unchanged remote master7c5a8e7. Final local HEAD/tree match the packet, index/worktree are clean and the complete-range whitespace check passes.

## Complete final history and migration conclusion

Independently inspected the complete base-to-head log, final diff, affected diff, series/patch/range-diff receipts and old/new source identities. rev-list confirms exactly one commit891db6b8 with direct parent7c5a8e7. There is no obsolete intermediate provider commit, fixup chain, transitional compatibility stream or superseded dependency/pin update retained in the final series.

The runtime replacement, Ruby/tooling removal, fixtures/checks/docs and agreed compatibility corrections remain one coherent result. The current corrections and diagnostics support that same public input contract; no unrelated feature is bundled. The commit describes the final behavior and, as the user requested, includes measured comparison prose with the required qualification.

The deployed6ec is preserved by refs/dev-sessions/2026-11-10-rust-syslog-exporter/deployed-pre-i3; I independently verified the ref resolves exactly to6ecada0a9d2f6457a11031a3a4ffc341584fb29c. Original reviews/deployed3hk/gsw receipts and recovery source are retained. Old6ec is a sibling predecessor history, not a literal ancestor merged into891db6b8. This substantive successor needs its own verified release/deployment and final lineage evidence.

No migrations. No migration paths, new persisted schema/cursor/format or intermediate state transitions were introduced. Old/deployed and corrected exporters remain in-memory only, with restart/reset and unrecoverable FIFO-loss limits unchanged. No transitional migration requires retention. No repeated provider dependency/channel/pin stream exists.

Independently derived the complete old/new changed-path set: exactly the ten assigned paths. The other25 tracked paths are identical. Manifest/lock/profile/toolchain, shell/check script, driver, HTTP, main and config hashes agree with their retained inputs. Cargo.lock SHA256 remains031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e; no dependency graph change is hidden in this correction. Legacy metric definitions/encoder are independently byte-identical.

The new full tree4b28b692 and src tree884d4981 differ substantively from deployed tree5d3e6ed8/src13622702. Unchanged-scope evidence is valid only within its demonstrated inputs and behavior; it does not certify this complete successor binary.

## Documentation placement and preservation

1. Reachability: the unchanged README links reference, verification and fixture provenance. The new paragraphs remain in those existing reachable pages.
2. Audience/owner: enduring header/body policy, ASCII/strip semantics, decoded-record diagnostic and label coalescence belong in exporter docs/reference.md. Test procedure belongs in docs/verification.md; user-record provenance belongs beside fixtures. Site activation/recovery and one rollout's evidence remain outside these feature paragraphs.
3. Lifetime: added source-reference text is usable after the initiative and contains no temporary branch or acceptance status.
4. Fidelity: reference matches actual raw boundaries, borrowing, lossy decoding, signature separation and count placement. The fixture bytes independently match the two original233-byte SHA256s. Test descriptions agree with the exercised cases.
5. Preservation: existing first-record, malformed/timestamp, framing, HTTP, memory, single-reader, reset and recovery caveats remain. No required operational instruction or public anchor was removed.
6. Applicability: this explicitly supersedes the earlier whole-record invalid-body rejection; it does not claim arbitrary byte-label equivalence or a new persisted migration/rollback conversion. Existing recovery paths are not retired.
7. Authority: one provider reference owns semantics, with existing local navigation retained. Session records own exact release/rollout results. No duplicate consumer parser contract or new receipt directory was introduced.

Conclusion: documentation placement, preservation and fidelity are sound. Original performance paragraphs are retained but explicitly attributed to oldfaf/6ec-equivalent source and Nix3hk. They do not claim891db6b8 performance. Later measured prose must bind the actual tested successor and preserve any message-only refresh evidence.

## Residual limits and next gates

D7's U+FFFD label coalescence, strict invalid-header rejection, RFC3339 subset, malformed-header boundary and program1 nested-header behavior remain explicit supported-policy choices. Replacement does not detect producer truncation/concatenation, provide durable replay, preserve cross-restart counters or cap total dynamic-series memory. Finite fixtures are not universal Ruby equivalence.

The source/CLI/config/service/HTTP/legacy metric boundary relevant to C4 is otherwise unchanged. Final consumer source/hash selection and applicable pin/derivation/input proof remain owner work after disposition; this report does not review an unpublished/unpinned C4 as final. Do not build or deploy a stale consumer/provider pair.

V3 still needs the exact final Nix package, focused final-binary parity against the retained Ruby baseline and corrected vectors, the prescribed small matched ordinary/OOM batch and the existing65-second two-consumer scrape smoke. Reuse older HTTP/transport evidence for independently unchanged scope; do not repeat an unrelated whole matrix without a relevant changed input/failure. Previous3hk measurements cannot certify the changed parser/common-path cost or rare decoding path.

The actual3hk/gsw essential service remains the retained healthy current/fallback according to the lead-owned evidence; I performed no production access or health check. No activation is part of I3/R3/C4/V3. Future lead-owned cutover must preserve one reader, rollback source/closures, immediate health/continuity verification and existing exact lineage/release contracts.

No source/report-file writes, nested agents, builds, services, production operation, integration, machine/repository claim, cleanup or session lifecycle action was performed by this reviewer. Please persist this report and record R3 disposition/remaining gates in existing session records. Implementer0 retains correction/finding ownership.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/

## Reviewer-confirmed provenance correction

The original report above is preserved. Reviewer0 confirmed its historical
`src13622702` abbreviation was pre-I2, not deployed6ec. Native Git resolves
`6ecada0a9d2f6457a11031a3a4ffc341584fb29c:src` to
`f563642a228e19e368b7f3b7ad638ef866f0bc89`, and corrected891 source to
`884d49817329697fdcb4dbda28a3120a0ba23f50`. Full old/new trees, exact ten-path
delta, findings and acceptance remain unchanged. Reviewer reran no review/check
for this metadata correction. Lead's authoritative exact891 CI43116296064 success
arrived separately; the reviewer's no-independent-CI-query statement stands.
