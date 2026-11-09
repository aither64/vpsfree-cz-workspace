# Final affected review: first-prior-origin diagnostic

## Findings

**No new Blocking, Important or Advisory findings** in the reviewed four-file diagnostic delta at `1285b9640fbbf3aba08491f548aee3b5a0914cce`.

The implementation preserves the maintenance refusal/authority boundary while retaining bounded evidence before the reducer discards its original cause. This is approval of the diagnostic source within the scope below, not a cause diagnosis, native acceptance or execution release.

## Exact source and review boundary

- Repository/worktree: `git@github.com:aither64/dev-workspace.git`, `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace`.
- Final head: `1285b9640fbbf3aba08491f548aee3b5a0914cce`.
- Tree: `9c976f1826f43e7e327f3e4196dd92df722cfac1`.
- Direct parent: `3145caa8fcf23b1e825eb54fe9176258f58c6b7f`.
- Affected comparison: `e7e533f05ccc653f1b0f8273b40f9e729aba7d64..1285b9640fbbf3aba08491f548aee3b5a0914cce`: four files, +232/-11.
- Complete current range: `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..1285b9640fbbf3aba08491f548aee3b5a0914cce`: five commits, 127 paths, +26172/-161. Actual merge base is exact 3bb.

I checked HEAD/tree/parent and clean worktree/index directly. The supplied affected.diff and full.diff both equal the actual Git comparisons. Main receipt SHA256 `8217ffe2f87be427269e97932f4340c453911c43a11a51a1c0e55ba27dec5779` and B packet SHA256 `b30b32a27a067172214d385384b19503d451d91912f6dc7706d583f65bc34710` match; all five main artifact hashes, all 17 B artifact hashes, all four current source hashes and all seven frozen-input hashes match.

This is an independent affected final review of the new internal diagnostic boundary. It reuses the unchanged implementation/SDK assessment from `review-maintenance-runtime.md` SHA256 `5e68b0dbaca95b056ed8b0c0dd8f905e35fe82bb2ba1cdd563bb8608926f1eef` and main's R1–R3 step-9 closure `0e72529a26f1091997c73aff96a6163e4b1d3ddc4b0014bd7b8ff601882b7505`. I matched the closure's source hashes to current files; this review does not repeat the unrelated implementation or SDK audit.

Session identity was verified first from the exact bound tracking directory: `dev-session current` printed `2026-11-03-lead-wakeup-delivery`. Both shell markers were absent, consistent with the trusted developer binding to the exact workspace/session. Reviewer0 retained saved **gpt-6.1-sol / xhigh / read_only**, with no override, fallback or nested reviewer. Capacity was confirmed to the lead.

I read the current packet/state, mandatory skill and all four lane references, applicable instructions and the exact affected code/tests/consumer context; unchanged procedures and prior source conclusions were reused within their permitted boundaries. All work was read-only. No tests, evaluations, builds, native/browser/VM calls, Git mutations, publication, CI, claims, profile/live actions, peer records or lifecycle operations were performed.

## General lane: behavior and regression evidence

The changed production code is confined to `portal/internal/maintenance/observation.go` and the in-process wrapper in `portal/internal/web/activity_maintenance.go`. The other two files are the reducer regressions and the existing native fixture's diagnostic projection.

At `observation.go:55–84`, first-origin retention is write-once for an existing watch. A prior scoped/global poison records the supplied event's scalar provenance. When unfinished items become prior effects at completion or the next start, the helper chooses the earliest retained start sequence, with deterministic ID tie-breaking, before the old item map is discarded. It retains no prior map or event history.

I independently compared `ObservationSnapshot`, `Snapshot` and the original `invalidate` body against e7: all are byte-identical. The Apply diff wraps the existing invalidation/poison paths with metadata capture and adds diagnostic item start fields; it does not change their conditions, ordering of authority transitions, or coverage/readiness classification.

The new tests cover the actual information-loss alternatives: unknown scoped event before a turn ID followed by a valid start, and unfinished prior items followed by a valid next start. They assert the original uncovered/not-ready refusal as well as retained origin. Additional controls cover first-cause stability, detached returned values, no command/instruction retention, clean reads, loss with absent method provenance, generation/watch reset and multibyte truncation. These are meaningful behavior regressions rather than substitutes for native execution.

The original native fixture deadline, source-start condition and acceptance ordering are unchanged. Its new `firstPriorOrigin` field does not participate in the wait predicate: `snapshot.Covered` still decides success.

## Architecture and repetition lane

The reducer owns the diagnostic because it alone sees the original event and the item map before erasure. `Observation.PriorOrigin` returns a scalar value under the existing observation mutex; `Server.ActivityPriorOrigin` delegates without creating an observer, reconnect, native read, callback or transport.

Repository-wide references to the new accessor/data show the existing fixture diagnostic as its only non-test consumer. Production owner/control and Snapshot consumers do not read it. There is no new HTTP/MCP/private-control endpoint, observer option, diagnostic authority, event dispatcher or storage path.

Snapshot and prior-origin reads are separate and can describe different instants. Each carries its own generation/sequence provenance, and the consumer uses the latter only for logging. A false/missing diagnostic is not interpreted as clean state; neither the wrapper nor fixture promotes it into coverage, readiness or idle proof. This is the correct boundary for a non-atomic diagnostic read.

All mutation/access uses the existing mutex and watch lifetime. Removal/replacement and generation reset discard the retained origin; subsequent reads return a detached struct containing no mutable maps, slices or pointers. No new lock order or wait is introduced.

## Scope and proportionality lane

The actual e7 failure demonstrated that a valid source-start observation ended in `prior-effects-unresolved` after the reducer had erased the information needed to distinguish earlier poison from unfinished prior items. That is a concrete evidence gap in the current acceptance investigation.

The chosen correction is proportional: one first scalar origin per existing bounded watch, two small start-provenance fields in existing item entries, a read-only accessor and four diagnostic lines in the existing fixture projection. There is no trace buffer, persisted event stream, second observer, broad logging framework or speculative cause fix. No optional hardening or additional framework is needed.

Nearby type/accessor comments explain volatility, lifetime, absent provenance and lack of authority. That is an adequate owning documentation location for this internal read boundary; no product operation changed that would require another operations document. Existing maintenance/update documentation retains its supported limits.

## Risk and compatibility lane

At `observation.go:55–65`, every retained textual field is capped at 256 bytes; truncated values are cloned, partial UTF-8 is removed and `Truncated` is set. Generation and sequence are scalar integers. The origin parser selects only thread/turn/item identity/type/status, method/boundary and reason; arguments, content, commands, settings, instructions and raw frames are not retained in this diagnostic.

Item status is retained only for existing admitted item entries; the existing status validation still controls whether an item enters the map. The new fields are diagnostic only. Total origin storage follows the existing bounded watch count; it does not grow per event.

Global invalidation may lack thread/turn/item provenance, and missing fields stay empty. The implementation does not invent a current turn, normalize an absent method into a guessed cause, clear uncertainty or treat a retained origin as proof of the current blocker. Truncation is an explicit evidence limit, not an identity comparison mechanism.

The SDK, module/sums, Nix graph/vendor selection, native/model/catalog, host and control-wire interfaces are unaffected by this delta. Existing Snapshot/owner authority, leases, startup, claims, Stop, admission, continuation and recovery behavior retain their reviewed boundaries. The original three runtime findings remain covered by main's accepted direct closures; none is reopened or waived here.

## Complete history, consolidation and state lineage

The current complete series is:

1. `e18a1e8de4d599df830e6ac390c9ab306d23d891` — tracking-directory test deadline isolation.
2. `58e87f9d3ccc1aac262b29f587a1d0553257a554` — durable monitor capability.
3. `f161ede8a6ea4cf540edcb7ece81ebb76f064a05` — separately adopted passive archive-hydration diagnostic.
4. `3145caa8fcf23b1e825eb54fe9176258f58c6b7f` — final maintenance SDK and independent historical fixture input.
5. `1285b9640fbbf3aba08491f548aee3b5a0914cce` — coherent final maintenance implementation with its supporting tests/diagnostics.

The first four commits are unchanged; the final maintenance commit was amended. Earlier reviewed/failed heads, including e7, remain separate refs/receipts rather than extra fixup commits in current ancestry. The new diagnostic supports that capability's evidence boundary and introduces no separate product subsystem.

**Obsolete history:** no obsolete prototype, transitional migration, superseded pin chain or abandoned compatibility approach was introduced by this amendment. Whole-series coherence/consolidation conclusions continue within the reused implementation and inspected affected boundary.

**Repeated streams:** none. There remains one final production SDK c3c2 selection. Historical SDK d3 belongs to the independent genuine 3bb test graph, not a repeated production-update stream. No dependency/pin/generated-input change occurs in the diagnostic delta.

**Migrations:** **no database migrations or seeds**. Prior-origin metadata is volatile process state with no persisted diagnostic format. Existing final private maintenance schema1 and its readers/recovery remain unchanged, as do public/monitor/submission/service/retry/claim formats. No intermediate diagnostic schema or compatibility shim remains. Historical donor external consumption is still unproved; this review makes no global absence claim and removes no supported format.

These are source/history conclusions, not retrospective deployment acceptance or proof that an amended head was literally merged.

## Evidence and remaining limits

I read the final logs: observation 0.237 s and activity/web 1.364 s passed on the frozen inputs. Tagged command compilation passed 0.059 s with **no tests run**. Formatting/whitespace/input guards are retained in the hashed packet. Original dirty-tree/system warnings and the ignored Nix cache-busy warning remain disclosed; the final committed tree is clean and matches the tested source receipt. I did not rerun those checks.

Both original cause-evidence receipt hashes match: e7 diagnostic `370e3b7a...` and D interpretation `466f6250...`. They establish the prior-effects information loss and the need for this diagnostic; they do **not** identify a named actual event/item cause or establish a fix. The original 90-second native failure remains a failure. No native call on 1285 has yet tested this diagnostic or proved maintenance acceptance.

A subsequent capture may reveal a truncated/missing/stale diagnostic or a different lifetime cause; it must be interpreted with its generation/sequence and separate Snapshot sample. It cannot justify weakening unknown-effect refusal or treating terminal native state as global cell quiescence. Prior unreported-cell/archive limits, old failures and deferred R5 remain unchanged.

**Disposition:** affected all-four-lane final source review complete with no new findings. Any next native capture, long acceptance, publication, final W/C composition or live activation remains separately lead-released. This review itself authorizes none of those actions and no session lifecycle change.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
