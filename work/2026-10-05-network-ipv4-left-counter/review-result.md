# Independent final source review — 2026-10-06

Reviewer: retained reviewer0, review-purpose/read-only, gpt-6.1-sol/xhigh.
Session binding and roster verified. High overall risk: schema, resource
admission, concurrency, ownership and mixed-version deployment. General,
architecture/repetition, scope/proportionality, risk/compatibility lanes reviewed
under mandatory-change-review. Reviewer read guidance, packet, design, complete
histories/diffs and representative consumers. No source/tracking edits, tests,
builds, fetches, publication, deployment or lifecycle operations by reviewer.

Reviewed original exact heads (pending fixes excluded):

| Repository | Base | Reviewed head |
| --- | --- | --- |
| vpsadmin | c4d9b50f4e74417ed37b5fe410cca3ec1addc24e | 6b3628af665049dc095ba985ef0fbe8a22286863 |
| vpsadmin-webui | 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51 | 811742f50cce2b7724784d0a674c8d4d5dcb6273 |
| vpsfree-cz-configuration | cde8451718d75929c931db63626b48f7de92fc4f | dea15f88c38341ecfd3e5030c700d1fee3d854a7 |
| vpsfree-kb-contracts | 873758fd6aec0c03f50a94600e0ceab97946f255 | ef72876da07dae61449502e2d03856d1d3b133e4 |

## Findings and disposition

No Blocking findings. All four concrete findings accepted for narrow fixes by
implementer0; verification/commit evidence remains pending.

1. Important, risk/compatibility: Vps::Update#chown_vps guards VPS IPs but later
   transfers dataset/subdataset exports via Export.user_id. Export endpoints
   belong to NetworkInterface.export and effective ownership follows Export.user.
   A disabled private endpoint can therefore change owner. Capture those
   endpoint IPs/networks in the original sorted batch before IP locks, check
   current identity/enabled state, cover unowned endpoint atomic rejection and
   retained same-owner service. Source: V819d66b0, update.rb:221-225,309-330;
   export.rb:11-14. This is within accepted ownership admission semantics.
2. Important, general: legacy admin-cluster availability scenario expects
   Disabled/Enabled row text, but the cell has only boolean_icon image and Edit.
   Align assertions with the actual availability cell/icon state. Source:
   V6b3628af, admin-cluster.spec.cjs:216,223; cluster.forms.php:242-247;
   functions.lib.php:604-610. No global boolean UI rewrite required.
3. Advisory, general/architecture: progressive suggested free IP query takes
   first50 before locally removing disabled rows. Disabled early IDs can displace
   all enabled suggestions. Use advertised network_enabled before the existing
   limit, retain stale client guard and successful old-API omission. Source:
   W811742f5, useProgressiveSuggestedIpQueries.ts:62-74. No exhaustive inventory
   enumeration requested.
4. Advisory, general/risk: NetworksPage ignores capabilityQ.error/isError;
   initial failure resembles unsupported old API, cached errored refetch can
   retain active availability control. Show error/retry and avoid relying on
   stale capability data after failure. Cover error versus successful old API.
   Source: W811742f5, NetworksPage.tsx:391-398,966-970.

Root confirmed both Important source paths before assignment and accepted both
Advisory fixes. Skill step9 direct focused verification is intended; rerun only
affected lanes if actual remediation expands assessed design/contract.

## Whole-branch and migration conclusion

Reviewer inspected all original base-to-head series and final diffs. V has two
coherent API and legacy commits; W one coherent feature commit; C two generated
independent input commits; K one exact revision update. No superseded approach,
fixup series, obsolete branch-only compatibility path or abandoned migration
remains. Old-API capability handling is intentionally supported. C's old V pin
advances across existing upstream composer.lock/php-packages.nix changes at
c4d9b50f, not additional feature-authored work.

V sole migration20261006120000 directly follows20260914190000, adding final
NOT NULL/default-true bool with reversible change and no stale-schema guards.
Core schema changes only column/version. Feature is absent from retained
origin/master and no local release tag contains API commit. Session declares
no release/deployment/external consumption beyond disposable tests; reviewer
found no contrary local evidence, production provenance remains unverified.
W, C and K: no migrations.

## Accepted architecture and compatibility

vpsadmin owns admission/statistic. Both public pages retain integer ipv4_left;
role is sole public/private classification. Counter excludes reservation, owner,
interface, disabled/private/IPv6. Retained maps/candidate IDs are explicit
transaction-local state and inspected batches avoid late network-set growth.
Continuity exposes no public bypass. C changes only two intended locked nodes,
follows preserved. K five revision records agree, fingerprints/pages/bitmaps
unchanged. Go client pinned1d9240f3d27b (Terraform consumer) ignores additive
JSON fields and ipv4_left stays int64; existing requests omit new parameters.
No node protocol change/coordinated node upgrade. Schema then all writers before
first disable; old ignoring-writer rollback while disabled pools exist is unsafe.

Structural debt disposition accepted: reviewed UserNetworkPage hash
046865da62cc7c0cbf14db481e918e507edf6cf73ecab81daf0fced586b170f4, measured683
lines, prior691 allowance lowered to683; original e7ce3d73 origin and<=500
removal condition retained. Modified-byte provenance note is explicit, model/
baseline unchanged, no cap growth/new exception. Action component coverage
matches assigned/detached behavior.

## Remaining proof

Reviewer inspected quick evidence, did not rerun: W42 tests, V72 examples with
0failures/2existing pending, migration/hooks/check receipts. Real SQL race
interleavings, VM continuity/data-preservation, browser desktop/mobile/CS/EN,
actual API capability cache/error behavior and full configs remain unexecuted.
Existing pending cases are remote clone snapshot retention and multi-interface
migration; no certification implied.

Two existing member IP-list KB images need regeneration and visual inspection.
Capture runtime remains blocked by workspace lifecycle ownership/generation
requirements; static green is insufficient. Generated refreshes need image/
validation inspection; substantive capture/scenario/page changes need applicable
review. No production attribution, retirement list, deployed writer inventory,
publication/deployment/merge or final branch readiness is certified.

## Direct remediation verification

Root inspected the narrow source corrections and exact tests. Export endpoints
join the initial sorted network/IP/host batch; effective ownership changes
require enabled. Root/child backup-pool fixtures cover enabled transfer, disabled
atomic denial and same-owner running continuity. Browser state checks target
the specific availability cell's one image. Suggestions use advertised filtering
before limit with native ReactQuery capability deduplication, stale disabled
response rejection and old-API omission. Capability failure/retry is visible;
cached pending/fetching/error state cannot send availability edits while other
fields remain editable. No new copy, public API contract or admission bypass.

Frozen remediation quick2 passed syntax/lint,14VPSupdateexamples,51Reacttests
and full ci:quick including docs/types in3m15s; logs remediation-quick2-*.
Final commit/pin consolidation is complete. Skill step9 applies: the fixes
implement the review's already-assessed behavior without expanding the design,
so unaffected lanes are not rerun. Root verified final histories/tree equality/migration blobs and the complete C/K pin diffs against this tested source. Runtime verification is cleared at the exact heads in branch-inventory.md.

### Narrow fixture corrections and actual browser proof

Following the completed review and accepted direct corrections, runtime checks
exposed two test-fixture defects. The concurrency spec used an untyped manually
initialized TransactionChain; it now uses the standard typed builder and joins
all owned workers before scoped cleanup, with restoration diagnostics. Both
core and full-plugin runs passed all 13 concurrency and five Create examples at
the failing CI seeds. No production admission or schema behavior changed.
The browser fixtures now describe real HaveAPI PUT action metadata rather than
a single-key object that the generic adapter unwraps as a namespace. Product
adapters and copy are unchanged. Desktop and mobile each passed four synthetic
cases; production build passed, and four EN/CS captures were inspected.

Root inspected these narrow test repairs under workflow step 9. They do not
introduce a new design, contract, admission bypass or accepted boundary. V
be136b6c00f03b85b7a12cc57550b4a1394a94a7 is consolidated to two logical commits;
W e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 to one. W's final delta after browser
proof is evidence-only prose; tested application/e2e bytes are unchanged.
No migration lineage change occurred. VM/legacy-browser/configuration builds
and the blocked KB images remain outstanding.
