# Foundation final review — G+S

Independent reviewer0 report, retained gpt-6-astra/xhigh/read_only, all four lanes
at High risk. Delivered through report_to_lead and persisted by the lead because
the reviewer remained read-only. Exact committed ranges reviewed:

- HaveAPI:209a7ac0c2fe6cd1b78735f50b5e60d979309543 →
  7cffd0b6b6959abf5b5af810ba81004b8defc13c.
- SDK:e5786f69b7c223c3bb5b1de99b7f97186eec368a →
  383e8556208f330472961077cce4dcb546231c8a.

Blocking:none. Important:one. Advisory:one. This is final review of the completed
foundation before real HTTP/archive integration, not whole-initiative readiness,
integration/publication/deployment approval. W source is outside this review.

## Findings

**Important R1 — explicit help without a method selector can describe the wrong
action.** General and risk/compatibility. G ir.rb:195–203 accepts query.nil? and
preserves selector-less explicit help. PUT update help
/api/v1.0/widgets/{widget_id} generates OPTIONS without ?method=PUT. Shared
snapshot.rb:104–107 permits it. server.rb:880–885 selects by method only when
selector exists; Show/Update sharing a path can return the first matching action.
Capability fields/authorization may therefore describe another operation.
Current vpsAdmin capture has selectors and is unaffected, but generic generator
contract is affected. Smallest remedy: reject explicit selector-less action help,
retain absent-help fallback, add GET/PUT shared-path regression. Narrow rejection
requires focused owner checks/lead inspection, not full re-review. Prepared
uncommitted fix is outside these reviewed heads.

**Advisory A1 — carry only output names needed for collision checks.** Scope and
architecture. G emitter.rb:244 emits full output Field records, but runtime.ts.erb:76
only reads field.wire_name for object-output namespace collision detection.
S contains4609records,480396bytes compact JSON versus56725bytes corresponding
name arrays before restricting to actions with object metadata. Static descriptor
measurement, not compressed bundle result. Root client composes all actions, so
unused kind/required/nullable/emitted-name properties add browser parse/allocation
work without response validation. Prefer relevant wire names, no new registry,
validation framework or broad optimizer. Nonblocking; planned bundle measurement
still required.

## Scope and ownership conclusion

User requests full WebUI SDK adoption and generator-origin client behavior.
G26files(+475/-62), S689files(+61177/-11449), chiefly generated. Handwritten
mechanisms address demonstrated live capability/local-error/typed-receipt/metadata
configuration/current0.32runtime needs. No speculative subsystem/backend expansion.
Phase evidence shows delivered design,double capture,committed foundation/quick
checks; no scope-driven stall established. Parallel clocks not summed.

HaveAPI owns protocol/runtime; generator owns reusable SDK facilities; S remains
generated with unchanged thin executor adapter. WebUI owns auth/renewal/cache/
paging/uncertain-write policy. Reviewer inspected actual WebUI f2765d3f HaveAPI0.32
and TS5.9 pins, adapter/discovery,node/network capabilities,VPS receipts; also API
610a96f docs adapter/released0.32generator/client pins. Existing consumers are not
silently repinned; W adoption remains separate.

## Correctness and compatibility conclusion

Apart from R1, root/action descriptions use versioned executor,recorded help,
encoded placeholders/shared aliases without discovery caches/retries. Naming
reservations cover root describe/emitted declarations. Ordinary IO/path/options
for all519actions match base after whitespace normalization except intended
300empty GlobalOutput types become extensible through ActionResult; strict empty
data output preserved. ClientInputError checks precede executor,executor failures
not relabeled,no replay. Metadata retains extension keys; override coherent across
global/object request and immediate declared object-list projection. Raw envelopes,
Custom values,nested associations untouched. Payload/permission validation remains
consumer responsibility. No new persisted state/API default/coordinated node update.

## History, update streams and migrations conclusion

Each complete base-to-head series has exactly one commit, bases are actual merge
bases. G facilities/tests/docs/current runtime support form coherent commit; S
one0.3generator/runtime/provenance/generated stream consolidated. No repeated update
streams/superseded approaches remain. G message-only18b8d966/e5b7d31/final7cff share
identical trees and intermediates absent from series. No retained intermediate pin
required. **No migrations** introduced. Capture inventories are source evidence,
not new migrations. No transitional lineage/obsolete compatibility path. Narrow
fixes/regenerated pins must stay consolidated before final readiness.

## Independent evidence

Session identity verified against trusted binding with both env markers absent;
roster revision61 reviewer0 ready/review-purpose/saved Astra/xhigh/read_only.
No fallback/nested reviewer. Full workspace/repo/skill/all4lane instructions read.
Static independent verification:675generated manifest file hashes,tooling/schema/
provenance digests,byte-identical schema versus Sbase,unchanged declarations.
Reconstructed generatorSHA89ae36c11883979150bd6963a078052a270e5d0d27f7e7853a667997c027193f,
shared schemaSHAe12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c.
Published JS0.32runtimeSHA9285eab56e435ee86a501a24808e15496d44521881a032090003a1108511f016.
Capture graphs/quick logs inspected; no app tests/builds/HTTP/source/Git mutations.

## Remaining checks

Reported quick G73source+24release/lint/hooks, Sregenerate/check/build/TS6+5.9/
13client-release/1source-refusal do not replace real published-runtime wire/docs
or exact-archive actual HTTP/dual-compiler checks. Resolve R1 then run those on
final regenerated candidate and retain exact inputs/archive. Wpilot/isolated API
member-admin/browser/bundle/finalWreview still required in its phase. Publication,
remote generator fetchability and approved integration separate.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/

## Lead disposition

R1 accepted: generator owner0 implements exact rejection/regression/docs and
consolidates unpublished owning commit. A1 accepted as small direct simplification:
output-name arrays only for relevant collision checks, unchanged semantics and
no optimizer. Owner0 checks; owner1 regenerates from final exact head, repeats
changed-module affected quick checks, consolidates S, preserves old candidate
receipt and prepares new immutable candidate. Lead directly inspects narrow fixes;
no redundant full rerun unless remedy expands reviewed contract.
