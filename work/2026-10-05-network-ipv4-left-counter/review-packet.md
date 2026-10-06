# Corrected committed source packet

All intended hand-written source, API/schema, UI, configuration and contract pin
changes are committed; quick checks pass. Review before deliberate long runtime,
capture and build verification. [branch-inventory.md](branch-inventory.md) contains
exact heads, complete histories/final diffs, and migration provenance. Generated
visual evidence remains a selected post-review verification deliverable.

## Request and accepted boundary

Implement administrator-controlled network availability and correct the shared
public IPv4 inventory counter. The user explicitly chose network roles as the
sole public/private classification. No numeric address classification or extra
retirement heuristics belong in this change. Include both application channels
in vpsfree-cz-configuration. See design.md and plan.md for the accepted brief.

Network.enabled is additive, non-null and true by default. Omitted updates must
preserve disabled state. Writes are administrator-only; state is readable and
exact filters are optional. No default_scope or automatic retirement.

Disabled networks reject new automatic allocations, detached-owned reuse,
explicit assignments including actor-less callers, ownership grants/transfers
including VPS owner changes, and owned registration. Unowned inventory staging
is allowed. Existing ownership, assigned routes/service, host-address management,
release/disown, rollback, and trusted same-owner assigned-address continuity
through migration/restore/replacement/swap remain supported. Historical detached
addresses and new replacement/clone allocations cannot use that exception.

Admission locks networks with shared current reads before exclusive IP rows,
preserving sorted network/IP and parent-before-host reservation order. Retained
transaction-local maps and separate destination candidate IDs prevent later
pool expansion across migration/swap, create families, all clone interfaces,
standalone multi-address allocation and export retries. Final current identity
and eligibility checks follow reservation. Disable-before denies new use;
admission-before may finish after disable. No public bypass is introduced.

PublicStats.ipv4_left remains an integer allocation-row count, shared by both
index pages: unowned, unassigned, unreserved rows in enabled IPv4 public_access
networks. Private roles contribute zero. Location, purpose, pick policy and
maintenance can affect per-VPS availability but do not redefine this statistic.

Both UIs show availability and administer it only when API capabilities support
the field. Legacy mutation uses confirmed CSRF-protected POST. Available selectors
filter enabled pools and reject known disabled stale results, while owned and
assigned inventory remains visible. Missing state on older APIs is unknown;
unsupported fields/filters must be omitted.

## Repositories and commit boundaries

All worktrees are beneath
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/`.

| Repository | Initial base | Final source head |
| --- | --- | --- |
| vpsadmin | c4d9b50f4e74417ed37b5fe410cca3ec1addc24e | be136b6c00f03b85b7a12cc57550b4a1394a94a7 |
| vpsadmin-webui | 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51 | e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 |
| vpsfree-cz-configuration | cde8451718d75929c931db63626b48f7de92fc4f | dd10d88073da3aed6c4512e938abe4374422aab1 |
| vpsfree-kb-contracts | 873758fd6aec0c03f50a94600e0ceab97946f255 | 291566b2c0bd43389802f607852fd9a4f8241752 |

V separates API/schema/guards/count and supporting tests/docs from legacy UI,
catalogs and browser/regression coverage. W is one focused frontend change.
C has two generated channel pin commits; K has a mechanical exact source pin.
Supporting tests, migration and invariant/upgrade documentation stay with their
owning behavior. No unrelated dependency or daemon/module changes are intended.

The only new migration is 20261006120000_add_network_enabled. It has not been
merged, released, deployed or externally consumed in this initiative; isolated
disposable migration tests are development evidence. Require the complete final
inventory and provenance before a whole-branch conclusion. W/C/K have no new
migrations.

W includes a reviewed downward ratchet of one existing structural-debt entry.
The small address-action extraction and disabled-state badges reduce the page
from 691 to 683 measured lines. Lead inspected the exact changed source and
accepted its recorded hash, lowered allowance, unchanged baseline/debt origin
and removal condition. No new exception or budget growth/audit-model change.
Assess the proportionality and truthful provenance of this limited disposition.

## Ownership, consumers and documentation

vpsadmin owns enabled admission and the shared public statistic. Legacy PHP and
the separate React UI consume additive HaveAPI state, filters and metadata.
Existing CLI/generated clients can omit the new fields; no node protocol or
route command changes are made. Configuration maps vpsadmin/vpsadmin to
vpsadminServices and vpsadmin-webui/vpsadmin-webui to vpsadminWebui. The frontend's
vpsadmin input continues following vpsadminServices. K pins exact V source in
its existing revision records and normal flake lock, checking documentation
impact without blindly refreshing fingerprints.

Owning V explanations: docs/ip-locking.md#network-availability and
docs/upgrade-network-availability.md, linked from docs/README.md.
W updates docs/design/{API_CONTRACTS,REQUIREMENTS,EVIDENCE_MATRIX,WORKFLOWS,
IMPLEMENTATION_INVENTORY}.md and its dated docs/work-log entry; REQ-071 and the
REQ-050 extension describe current availability and detached revalidation.
See kb-impact.md for external documentation impact and contract results.

Upgrade the additive schema before enforcing API writers, then replace every
allocation writer before disabling a pool. Deploy compatible controls afterward.
Mixed old/new writers are safe only while all networks remain enabled. Old API
rollback while disabled pools remain would lose enforcement and is unsafe.
UI rollback preserves backend policy. No coordinated node update is required.
Production contributions, deployed revision and operator retirement list remain
unverified; no deployment, network disable, KB publication or merge is authorized.

## Verification and reviewer assignment

Quick evidence and failures/fixes are in state.md and scoped log artifacts:

- V eight focused API resource/model files: 108 passed, one counter fixture
  failed and was corrected; the affected counter case then passed. Migration
  forward/reverse: two passed. These are isolated real SQL with synthetic objects.
- V seven affected allocation/create/clone/export/migration/swap/replacement
  files after final batch-boundary changes: 72 examples, no failures, two existing
  pending contracts (remote clone snapshot retention, multi-interface migration).
- Ruby syntax/lint: 34 files clean; CI selector 16 tests/55 assertions passed.
  Final full-plugin API/PHP locale health and scoped Nix formatting pass.
- Legacy PHP: 98 of 99 tests passed initially, one new template stub failed;
  corrected CSRF class then passed four tests. Scoped PHP syntax/formatter pass.
- W five focused unit/DOM files: 42 passed. Full ci:quick passed, including all
  application/tooling/adopted-browser/BFF type checks, quality and locale gates.
  Final prose-only documentation audit: 68 documents, 71 requirements passed.
- C both generated exact pin commits passed hooks; full lock diff changes only
  the two intended locked inputs. K bin/check passes, with no semantic drift,
  60 concepts/120 image variants and unchanged fingerprints.

The original review preceded deliberate runtime verification. After narrow
fixture repairs, core/full SQL runs each passed 18 concurrency/Create examples;
React desktop and mobile each passed four synthetic cases and the production
build passed. VM continuity/data checks and legacy browser checks remain. Final C/K pins match published V/W feature heads and their complete diffs were
inspected; all worktrees are clean. Synthetic fixtures do not certify a deployed API. The KB member IP
list gains an Enabled column, so existing networking/ip-address-list Czech and
English captures must be regenerated after source review despite semantic green.
Inspect/validate generated artifacts and arrange any required final artifact
review before branch readiness. No production KB write is authorized.

Overall risk: high (schema, admission/ownership policy, concurrent SQL locking,
cross-project API compatibility and writer upgrade/rollback order).
Applicable lanes: general, architecture/repetition, scope/proportionality, and
risk/compatibility. Read mandatory-change-review/SKILL.md and all four references.
Eligible retained reviewer0 is independent, read-only, gpt-6.1-sol/xhigh; verify
the live roster again before assignment and retain saved settings.

Review the completed committed trees and complete base-to-head histories across
all four repositories. Explicitly conclude whether obsolete unmerged history
remains and whether migration lineage is sound, including no migrations for
the other repositories. Return severity-ordered concrete findings and residual
test gaps; no nested reviewers or source changes.

## Review gate disposition

Original independent final review is preserved in review-result.md and review-original-packet.md. All four narrow findings were corrected, directly inspected, and verified under mandatory-change-review step 9. Remediation quick2 passed 14 VPS owner-change examples and 51 React unit tests, plus syntax/lint and full ci:quick. Final histories preserve reviewed logical splits with exact tested-tree equivalence. Generated final C/K pins and their entire transitive diffs were inspected; unrelated nodes/follows are unchanged. No new design, contract or bypass was introduced. Long verification is cleared at the exact heads above; no merge or deployment is authorized.
