# Final visibility follow-up review packet (2026-10-07)

All intended V/W/C/K source and pin changes are committed and clean. V is
published; C/K feature publication completed too (visibility-pin-publication.exit0). This is a
new final committed-deliverable review after quick checks, before long checks.
Retained reviewer0 is independent, ready, read_only, gpt-6.1-sol/xhigh; no
model/effort override. High risk: public enumeration and tenant permissions,
existing schema/admission behavior and live-infrastructure configuration pins.
General, architecture/repetition, scope/proportionality, and risk/compatibility
lanes all apply. Read the mandatory review skill and all four lane references.
Perform review directly without nested delegation or tests/builds/mutations.

## Accepted outcome and boundaries

The follow-up hides disabled networks from non-admin Index results. IP Index
retains enabled networks, caller-owned (including detached) and already-readable
assigned addresses inside the existing permission scope. SQL filtering precedes
count and pagination. Explicit filters only narrow it. Admin inventory and all
Show/shared association permissions are unchanged, including host, history and
export endpoint continuity. Export-only association permission must not become
Index permission. No default_scope, new public field/capability, permission
expansion, schema/migration, allocation, admission or counter change is part of
the follow-up. Both UI consumers were inspected; no further UI edit is needed.

The original feature adds admin-controlled Network.enabled, true by default,
blocks new use and retains same-owner assigned-service continuity. IPv4-left
is unowned/unassigned/unreserved enabled IPv4 rows with role=public_access;
private/public classification is solely Network.role. No RFC1918 predicates.
Review actual allocation batch boundaries, lock ordering and ownership paths
against the accepted design, with prior review dispositions as context.

The new V visibility commit remains separate from the original API/legacy
commits because the user accepted this additional list policy later. Tests and
owning docs support it. Source remediations from earlier review were already
folded into the original two commits. Repeated C/K pin iterations have been
replaced by two canonical channel commits and one exact KB pin commit.

## Exact branches and complete histories

See [machine-readable inventory](visibility-final-inventory.json) for every
file and complete commit list. Final diffs/history artifacts below include the
entire branch, not only the follow-up. Require an explicit conclusion on obsolete
unmerged approaches, commit coherence and migration lineage.

### vpsadmin

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin`. Branch: `2026-10-05-network-ipv4-left-counter`.
Base `c4d9b50f4e74417ed37b5fe410cca3ec1addc24e`; head `d7d7fb66865fd1a5548a45a559f5c2be436bc470`.
[Full diff](visibility-v-review.diff); [complete history](visibility-v-review-history.log).

```text
fc4f01a025e373ba5c85a7e78ea8b61ac1e1dc1f api: add network availability admission controls
be136b6c00f03b85b7a12cc57550b4a1394a94a7 webui: expose network availability and enabled address selectors
d7d7fb66865fd1a5548a45a559f5c2be436bc470 api: restrict non-admin network and IP lists
```

### vpsadmin-webui

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui`. Branch: `dev/network-enabled`.
Base `02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51`; head `e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`.
[Full diff](visibility-w-review.diff); [complete history](visibility-w-review-history.log).

```text
e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 networking: manage network availability
```

### vpsfree-cz-configuration

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration`. Branch: `2026-10-05-network-ipv4-left-counter`.
Base `6f6aff9029cd57e1a0f9201356f7fdc9f6480671`; head `74a1a6acbc272cc73a3bca468ed10a8b93464957`.
[Full diff](visibility-config-review.diff); [complete history](visibility-config-review-history.log).

```text
4f547136e218468f302b280dcfa7457624eda7c9 inputs: set vpsadminServices to d7d7fb66
74a1a6acbc272cc73a3bca468ed10a8b93464957 inputs: set vpsadminWebui to e4c49bcd
```

### vpsfree-kb-contracts

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts`. Branch: `2026-10-05-network-ipv4-left-counter`.
Base `873758fd6aec0c03f50a94600e0ceab97946f255`; head `1f8817e5c519818f7fb156751cdacc784d998f42`.
[Full diff](visibility-kb-review.diff); [complete history](visibility-kb-review-history.log).

```text
1f8817e5c519818f7fb156751cdacc784d998f42 inputs: pin network availability vpsAdmin revision
```

## Base and pin reconciliation

C master independently advanced from original cde84517 to 6f6aff90, changing
only a release record and WebUI/devWorkspace locked metadata. Current C feature
history starts at that new exact default and preserves every unrelated input.
Its two canonical confctl setters select V d7d7fb668 and agreed W e4c49bcd;
WebUI->Services follows remains unchanged. Read generated messages/diffs as
well as [base reconciliation](visibility-config-base-refresh.md).

W main independently advanced to 5d853740 with a separate dependency patch and
mobile/language changes. The accepted backend-only follow-up retains W's exact
feature head and source; it was not rebased or published here. Record this
limitation rather than infer current-release readiness. Network W still includes
the earlier baseline proxy-addr 2.0.7 until appropriate branch reconciliation;
upstream now contains the independently merged a7361bb2 patch. No new runtime,
trust-policy or dependency work is included. K's five revision records and actual
fresh devShell source match V; fingerprints/page content/PNGs are unchanged.

## Migration provenance and compatibility

Sole feature migration: 20261006120000_add_network_enabled, immediately after
20260914190000_add_node_kernel_evidence_checkpoints. Final schema adds the
NOT NULL/default-true boolean directly. The follow-up preserves all schema and
migration bytes (visibility-migration-provenance.txt and quick4 freeze); no
transitional migration or stale-schema guard was introduced. Local retained
refs do not contain the feature on default or in a release. Declared consumption
is disposable tests only, no production deployment; production provenance is
not independently established. W/C/K have no migrations.

Upgrade guidance requires the schema before enforcing API, all allocation
writers before first disable, then compatible controls. Old writers ignore the
flag; rollback to them while pools are disabled loses enforcement. UI rollback
preserves enforcement. No coordinated node update is required. Show/list
visibility remains within old permissions; older clients can continue current
operations. Counters/API response arithmetic retain their existing shape.

## Documentation and consumers

Owning V docs: docs/ip-locking.md#network-availability (updated list-vs-Show
semantics), docs/upgrade-network-availability.md, docs/README.md. The accepted
brief is design.md's non-admin refinement; plan.md/state.md retain scope and
operational readiness. Prior full UI docs and EN/CS copy remain in W. Actual
legacy IP list and Show-based route editor, W UserNetworkPage/detail adapters,
API ownership/assignment/host/export/history resources are representative
consumers. C flake.nix maps the two real channels; K owns exact semantic/visual
contracts. Use actual pinned consumers, not inferred lists.

## Quick verification

Visibility quick2 syntax/scoped RuboCop for all seven Ruby targets passed.
Quick3 core seed36954: 226 examples, 223 unchanged passes and three new contract
assumption failures. Root traced HaveAPI 0.29.8: these Show/history actions keep
associations unresolved and the existing non-admin input whitelist omits count
metadata. Only those three assertions/count coverage were corrected; product,
fixtures, docs, migration and other examples stayed unchanged.

Quick4 scoped lint passed; corrected three core examples passed at seed36954;
full five resource files passed 226 examples at seed9346, zero failures/pending
or outside errors. Native JSON example IDs match exactly across full/core;
visibility-example-parity.json reconciles prior223+corrected3. The real authorized,
validated Index action.count is tested with limit1; no query/user mock or new
HTTP count capability. All visible cursors and unchanged admin HTTP count remain.
Evidence: visibility-quick4-* log/JSON/exit, visibility-quick2-ruby-syntax-lint.exit.
V normal hooks passed. C canonical commits passed normal hooks and complete lock
graph guard. K fresh-shell bin/check passed; actual source path is in
visibility-kb-effective-v-source.path. K commit used normal Git with verified
absence of declared/active hook framework.

Original exact older-head evidence is in fixture-final-verification.md and its
receipts: API matrix, admission races, allocation/ownership/migration specs,
React synthetic desktop/mobile/browser build, route/export VM scenarios and12
config consumers. Do not claim those receipts certify newly changed queries or
new C generations. Old review findings/dispositions are in review-result.md.
This review does not certify prior unchanged KB images or deployment.

## Remaining proof and non-goals

No default integration, deployment, network retirement, production attribution,
PR management outside W, provider/package activation or cluster lifecycle action
is authorized. User explicitly keeps projects in feature branches; workspace
policy was separately integrated. Preserve existing branches/history evidence.

After final review, planned fresh checks cover12 channel consumer builds and
exact migration/restore/legacy selectors if real capacity remains sufficient:
vps/migrate-with-data-check,
storage/restore-after-reinstall-with-descendants-remote,
webui#admin-cluster. Retain payload/sentinel/checksum/IP assertions, no substitute
selector or memory-profile adapter. Current read-only capacity is sufficient but
must be checked at each fresh start; prior interruption was before VM assertions.
Do not await CI.

The two member IP-list KB images remain blocked on a supported owned capture
runtime; raw legacy helper startup does not meet generation/socket ownership
requirements. No copying state, forged records, lifecycle bypass or capture was
performed. A green static contract does not certify the new Enabled column image.
Production revision/writer inventory and retirement list remain external.

Report severity-ordered findings with exact file/line/commit and lane, then
whole-branch/history/migration conclusions and remaining evidence limits. Read-only
role prevents tracking edits; send the report to root for preservation.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
