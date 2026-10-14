# Source branch inventory preparation

No source feature commits or migrations have been published at this checkpoint.
The complete final commit series/diffs will be recorded after focused commits.
This inventory does not replace independent final review.

| Repository | Exact initial base | Feature branch | Intended commits |
| --- | --- | --- | --- |
| vpsadmin | c4d9b50f4e74417ed37b5fe410cca3ec1addc24e | 2026-10-05-network-ipv4-left-counter | API/schema/admission/counter/behavior/docs/scenarios; legacy UI/catalog/regression/browser |
| vpsadmin-webui | 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51 | dev/network-enabled | UI/adapters/catalogs/unit/browser/docs/inventory |
| vpsfree-cz-configuration | cde8451718d75929c931db63626b48f7de92fc4f | 2026-10-05-network-ipv4-left-counter | Two generated exact channel pin commits |
| vpsfree-kb-contracts | 873758fd6aec0c03f50a94600e0ceab97946f255 | 2026-10-05-network-ipv4-left-counter | Mechanical exact vpsAdmin contract pin |

## Migration lineage

V base schema is `ActiveRecord::Schema[8.1]` at
`20260914190000_add_node_kernel_evidence_checkpoints`. The sole new migration
`20261006120000_add_network_enabled` adds `networks.enabled`, boolean,
`null: false`, `default: true`. Core-only schema generation changes only that
column and schema version. It changes no plugin table. Down removes only the
availability column and retains addresses and ownership; policy is lost.

The new version has not been merged, released, deployed or externally consumed
in this initiative. There is no superseded committed feature migration. Its
isolated migration spec has two passing forward/reverse examples. Rewritten
local fixtures are disposable, with no schema-existence fallback guards added.

## Final reviewer packet requirements

Inventory every final base-to-head commit and final diff for all four branches.
Give exact final heads, incoming default comparison, generated pin diffs and
migration provenance. Identify any superseded commits/unused compatibility
paths explicitly. Ordinary standalone picking and metadata feature detection
remain intended supported paths. No CIDR classification path is intended.

Quick verification evidence is separate from prepared long scenario source.
Longer concurrency, VM data-preservation and desktop/mobile browser execution
remain gated on independent final committed-deliverable review. Synthetic W
fixtures are UI evidence, not real API or deployment certification. Production,
default integration and session lifecycle remain untouched.
