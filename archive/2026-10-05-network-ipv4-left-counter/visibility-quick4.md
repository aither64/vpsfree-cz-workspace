# Visibility quick4 contract correction and checks

Quick3 core seed 36954 ran 226 examples: 223 passed and three failed. Full mode
was skipped. The actual JSON and log identify these existing example IDs:

- spec/api/resources/ip_address_spec.rb[1:2:1:7]: VpsAdmin::API::Resources::IpAddress Index with disabled free inventory counts visible rows and traverses all visible pages
- spec/api/resources/ip_address_spec.rb[1:3:1]: VpsAdmin::API::Resources::IpAddress Show preserves disabled free, owned and assigned details without widening permissions
- spec/api/resources/ip_address_assignment_spec.rb[1:2:1]: VpsAdmin::API::Resources::IpAddressAssignment Index preserves active and historical disabled-network associations within owner permissions

Only assertions/action-level count coverage within those three examples changed.
No fixture definitions, product code, docs, migration/schema or other examples
changed since quick3. Supported includes coverage through IP/Host Index and export
associations remains intact. Earlier quick and operation artifacts are preserved.
The exact current complete eight-path source diff is visibility-quick4.diff.

## Existing contract and direct count check

IpAddress.Show and IpAddressAssignment.Index do not call with_includes. HaveAPI
0.29.8's active_record adapter therefore uses ar_parse_includes([]) and renders
unresolved associations. Show now asserts the permitted IP IDs and unresolved
network ID, then separately calls Network.Show to verify its disabled state.
Assignment history retains the exact owned active/history rows and their
associated IP IDs; foreign Show denial follows the existing allowed HTTP
200/403/404 plus status=false contract.

HaveAPI action.rb validate_metadata_type filters metadata using authorization.
IpAddress.Index's non-admin whitelist omits count, so the HTTP request has no
total_count. The corrected example preserves that response contract and every
cursor traversal. It constructs the real IpAddress::Index action using the
mounted test API's server, actual API version/path, real member context and
limit=1 input. It calls authorized?(SpecSeed.user) and validate!, verifies the
validated limit, then calls the production action.count. That method executes
the actual restricted query.count, which must return all three visible records
before pagination. No query/current-user mocks, bypass or new capability are
introduced. The same example also checks admin HTTP total_count=6 with limit=1,
confirming unchanged full-inventory metadata behavior.

## Frozen execution packet

After root inspection, a fresh watcher may run:

```bash
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-quick4.sh
```

The wrapper runs scoped syntax/lint for the two corrected spec files, then only
the three corrected core examples at seed 36954, then all five complete resource
files in full mode at seed 9346. The other 223 unchanged core passes remain
recorded in quick3 JSON; root owns final evidence interpretation. Quick2 lint
remains required for unchanged Ruby targets.

TMPDIR=/tmp and the existing automatic unique database/helper cleanup remain
unchanged. Logs/native JSON and per-step/aggregate statuses stay in tracking,
with no overwrites and stop-on-first-failure. The same eight-path/source-head
and unchanged migration/schema guard runs before/after. No runtime check,
commit/ref/publication/pin/CI/lifecycle operation has been launched here.
