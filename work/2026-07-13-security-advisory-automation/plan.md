# 2026-07-13-security-advisory-automation

## Goal

Design an end-to-end, least-privilege workflow for the future
`vpsfreecz/security-advisories` repository. A Codex session in that repository
must be able to investigate a requested CVE against the deployed vpsFree.cz
platform, preserve detailed and reviewable reasoning in git, create or update a
draft vpsAdmin security advisory, and populate a conclusion for every active
hypervisor/storage node. Publishing and user notification must remain an
explicit human action outside the automation token's authority.

## Affected repositories

- `security-advisories` (new; GitHub remote not created yet)
  - primary implementation repository;
  - one durable analysis directory per CVE, source/evidence manifests,
    assessment tooling, vpsAdmin draft submission, and scoped-token bootstrap.
- `vpsadmin`
  - advisory draft/node-status API and detached action-scoped tokens already
    exist;
  - evaluate a narrow kernel-history read interface derived from existing node
    status records, so the automation does not need SSH or log-server access.
- `vpsadminos`
  - read-only platform evidence for kernel configuration, packaged kernel
    sources, livepatches, and eBPF LSM mitigations;
  - change only if investigation proves that existing node status reports lack
    evidence that cannot be derived centrally.
- `vpsfree-cz-configuration`
  - read-only deployment evidence for selected kernel revisions, node roles,
    deployed livepatches/eBPF programs, and exact production pins;
  - compare the proposed API-based history source with the unpublished
    `2026-07-10-node-kernel-version-logs` work; change only if a log backfill or
    deployment integration remains necessary.

## Approach

1. Inventory the existing vpsAdmin security-advisory actions, exact token scope
   names, node inventory, and historical status data.
2. Use vpsAdmin as a least-privilege security-evidence broker. Prefer its
   already authenticated node status channel over granting the automation any
   access to `int.log` or the nodes. Initially derive boot periods from stored
   `kernel`, `uptime`, and timestamps; add immutable boot/runtime evidence to
   nodectld reports for exact future assessments.
3. Keep detailed CVE reasoning and machine-readable conclusions in the new
   repository. vpsAdmin receives concise public text and per-node conclusions,
   not the full research notebook.
4. Consult both vpsAdminOS and production configuration for every CVE. Version
   ranges alone are insufficient: configuration reachability, container/user
   namespace restrictions, capability exposure, architecture, livepatches, and
   eBPF mitigations can change practical exploitability.
5. Make submission idempotent, transactional, and review-gated. Re-running a
   CVE updates the same automation-owned draft and reconciles node statuses;
   the automation token cannot modify arbitrary or published advisories.

## Proposed architecture

### Security evidence

Extend the periodic nodectld status payload, without removing existing fields,
with:

- `/proc/sys/kernel/random/boot_id`;
- the immutable booted-system kernel module directory/revision, distinct from
  the mutable UTS release changed by the cumulative livepatch;
- boot time and vpsAdminOS version/revision;
- a machine-readable inventory of active kernel livepatches and attached eBPF
  mitigations, including enough identity and freshness data to verify them.

The vpsAdmin receiver accepts old and new payloads during a rolling upgrade. It
stores current evidence and a compact event whenever the semantic evidence
fingerprint changes, including mitigation changes that occur without a reboot.
Existing `node_statuses` provide the initial/fallback boot timeline by grouping
samples on `sample_time - uptime`.

Add an admin-only `node.security_evidence#index` action which returns only:

- the active node set relevant to security advisories;
- each node's boot/kernel/mitigation timeline and evidence freshness;
- security-relevant aggregate exposure, such as whether/count of active VPSes
  with KVM enabled, without VPS IDs, user identities, or general node metrics;
- explicit confidence/gap markers when an old agent or missing sample prevents
  a definitive conclusion.

The unpublished central-log work remains useful for an operator-controlled
one-time cross-check/backfill, but is not a runtime dependency and does not
justify an SSH or root credential for this project.

### Draft submission and token scope

Do not grant the project the existing generic advisory create/update/CVE/status
actions: they can modify arbitrary advisories and do not themselves enforce
automation ownership or draft state. Add a single transactional action,
`security_advisory#submit_draft`, which:

- creates or updates only an automation-owned draft identified by a stable
  external key such as `security-advisories:CVE-2026-46242`;
- refuses published/retracted advisories and never accepts publication, mail,
  or state-transition fields;
- validates and replaces the complete CVE and active-node conclusion set in
  one transaction;
- rejects node-set drift, missing/duplicate nodes, and stale optimistic-lock
  versions instead of silently overwriting human review changes.

The long-lived runtime token then needs only these scopes:

```text
node.security_evidence#index
security_advisory#submit_draft
token#revoke
```

The evidence response is authoritative for node identities and labels, so
`node#index` is unnecessary. The token has no generic node/VPS reads, advisory
reads or writes, publish/retract/mail action, user/session creation, or `all`
scope. `submit_draft` supports a non-mutating dry-run response and returns the
draft revision, so a separate advisory read scope is also unnecessary.

`bin/vpsadmin-token create` will accept a temporary operator bootstrap token in
memory, verify the live API action inventory, create a detached scoped token,
and store it outside git at
`$XDG_CONFIG_HOME/vpsfree-security-advisories/token` with mode `0600`. It must
not print the token or enable shell tracing. `bin/vpsadmin-token revoke` uses
the runtime token's self-revoke authority. A permanent detached token is
reasonable for sporadic CVE work because its server-side authority is narrow
and revocable; the script can also support an explicit finite lifetime.

### Repository shape

Keep the new repository private while assessments or drafts may be embargoed.
Use a small Ruby CLI so it can reuse the generated vpsAdmin/HaveAPI client and
the workspace's established tooling:

```text
AGENTS.md
README.md
flake.nix
Gemfile
bin/security-advisory
bin/vpsadmin-token
lib/security_advisories/
schemas/assessment.schema.json
advisories/CVE-YYYY-NNNNN/
  analysis.md
  assessment.yml
  sources.yml
  submission.yml
spec/
```

`analysis.md` holds the detailed human reasoning. `assessment.yml` records
immutable source revisions, affected/fixed commit ancestry, config and trigger
reachability, hardening and runtime mitigation evidence, per-node evidence and
confidence, and the conclusion. `submission.yml` contains only the concise
bilingual vpsAdmin text and node conclusions.

The CLI workflow is `new`, `collect`, `validate`, `render`, and `submit`.
Submission defaults to dry-run and requires an explicit apply flag. It never
publishes. Every assessment must distinguish a control that prevents the bug's
trigger from hardening that merely reduces exploitation reliability; version
strings alone are not sufficient because stable backports and custom kernels
exist.

## Preliminary CVE conclusions

These are source/configuration conclusions, not final node statuses. Final
submission requires the boot and mitigation timeline from vpsAdmin.

| CVE | Platform assessment | Upstream 6.12 fix |
| --- | --- | --- |
| CVE-2026-23111 (`nf_tables`) | Reachable to an unprivileged VPS through user and network namespaces with `CONFIG_USER_NS` and nftables enabled. Init-on-alloc/free and slab hardening make exploitation less reliable, but do not make the UAF non-exploitable. Nodes are fixed once booted into 6.12.70 or a kernel containing the fix. | 6.12.70, `1444ff890b4653add12f734ffeffc173d42862dd` |
| CVE-2026-46242 (Bad epoll) | Unprivileged epoll UAF/free-to-wrong-cache path is reachable. The write can target a reused live object, so allocation initialization is not a sufficient mitigation. 6.12.93 is affected; 6.12.95 contains the fix. | 6.12.95, `9324de74a3a59b9fde9b62ee45ebaa71458ba2e5` |
| CVE-2026-53362 (IPv6) | Unprivileged UDPv6 splice/`MSG_MORE` path is present. The overwrite is within a live skb allocation, so init-on-alloc/free does not block it. 6.12.93 is affected; 6.12.95 contains the fix. | 6.12.95, `46f201f8b4c39633a1fa3dc12459f506d470993d` |
| CVE-2026-53359 (KVM) | Real tenant-to-host candidate: new VPSes default to KVM enabled and nodectld grants `/dev/kvm`, so a tenant controls KVM userspace/memslots and its nested guest. Per-node classification must include actual KVM-enabled VPS exposure. 6.12.93 is affected; 6.12.95 contains the fix. | 6.12.95, `2ad3afa40ac6aa340dada122f9abfa46c0a6eb35` |
| CVE-2026-43499 (GhostLock) | Unprivileged futex PI/requeue path is reachable. The dangling waiter/PI state is not neutralized by heap initialization. Nodes are fixed once booted into 6.12.86 or a kernel containing the fix. | 6.12.86, `6d52dfcb2a5db86e346cf51f8fcf2071b8085166` |

The custom 6.12.95 kernel revision currently pinned by the configuration
contains all five upstream fixes. None of the currently configured cumulative
livepatch or eBPF mitigation programs covers these five CVEs. A repository pin
does not prove which kernel a node actually booted, so it cannot by itself set
a node to `not_affected` or `mitigated`.

Alternatives under evaluation:

- query the existing `node.status#index` action directly and aggregate client
  side (no vpsAdmin code, but broader data disclosure and large transfers);
- add the narrow security-evidence action over existing status rows first,
  then enrich it with immutable node-reported identity and runtime mitigations
  (recommended);
- retain the central-log index only for a one-time historical cross-check or
  backfill, mediated by an operator rather than a permanent automation login;
- rely on mutable `/proc/sys/kernel/osrelease` alone (rejected because the
  cumulative livepatch changes the UTS release without changing the booted
  kernel).

## Compatibility and deployment

- Advisory repository files and tooling add no runtime or persisted platform
  state outside vpsAdmin drafts.
- Any vpsAdmin API addition must be additive. Existing clients and older
  nodectld payloads continue to work unchanged.
- The initial specialized read endpoint over existing `node_statuses` needs no
  migration and supports an ordinary rolling API deployment and rollback.
- Deploy vpsAdmin's tolerant evidence receiver/schema first, then nodectld and
  production pins gradually. Old payloads remain valid and visibly lower
  evidence confidence. Rolling back nodectld leaves additive stored fields;
  rolling back vpsAdmin must not make nodes fail to submit legacy fields.
- Evidence history is append-only/audit data. Establish retention before
  implementation, and ensure rollback can ignore records created by newer
  nodes.
- The automation never receives root/SSH access to `int.log` or nodes. Any
  historical log import is an operator-controlled, separately authenticated
  action with a different credential and exact scope.
- vpsAdmin publication remains compatible with current manual review: draft
  creation/population is automated; publish and optional mail stay manual.
- Kernel/livepatch/eBPF evidence is pinned to immutable git revisions in each
  CVE analysis so later repository changes do not silently rewrite a past
  conclusion.

## Testing plan

- Verify exact action scopes from the live API description and exercise a
  generated token against an allow/deny matrix without printing the token.
- Unit-test kernel boot grouping, version comparison (including stable-branch
  backports), incomplete history, clock/uptime tolerance, node-set drift, and
  mitigation composition.
- Test semantic evidence events for reboot, livepatch and eBPF changes; verify
  that a mutable UTS release cannot masquerade as a newly booted kernel.
- Test aggregate KVM exposure against legacy-disabled, new-default-enabled,
  stopped/deleted, and migrating VPSes without returning tenant data.
- Use recorded API fixtures for deterministic advisory create/update/reconcile
  tests; require explicit opt-in for writes to a real API.
- Test idempotency, partial-failure recovery, dry-run output, and refusal to
  publish.
- Test each vpsAdmin API change in its focused RSpec topic and run RuboCop and
  repository hooks before commit.
- After intended code changes are committed and quick checks pass, run the
  mandatory standalone change review before long integration tests.
- Integration-test against a dev vpsAdmin API and verify that only a draft is
  created, every active advisory node gets one status, removed nodes are not
  silently retained, and the scoped token is denied unrelated and publish
  actions.
- Verify the token allow/deny matrix includes denial of existing generic
  advisory create/update/CVE/status actions and all VPS/user resources.
