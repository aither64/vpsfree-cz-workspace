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
  - add a user-visible kernel lifecycle and a separate narrow security-evidence
    interface, so the automation does not need SSH or log-server access.
- `vpsadmin-kb-captures`
  - update the WebUI documentation contract and Czech/English capture inventory
    when the kernel-history page is implemented.
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
5. Make client-side submission idempotent and review-gated. Re-running a CVE
   reconciles the same draft through the existing advisory, CVE, and node-status
   resources. The automation token cannot publish or notify users.

## Proposed architecture

### Public kernel lifecycle

Add an authenticated, read-only `node.kernel_history#index` resource and a
first-class event table instead of exposing raw `node_statuses`. Existing node
IDs, labels, and current kernel releases are already visible to logged-in users
and the public status view, so this is a safe projection when it excludes
utilization, addresses, tenant identity, and internal mitigation details.

Backfill the event table from `node_statuses` once:

- estimate each boot as `created_at - uptime` and group samples whose estimated
  boot time and monotonically increasing uptime agree;
- record a new boot when the estimate/uptime indicates a reboot;
- record a reported release change inside the same boot when `kernel` changes;
- bound an inferred change between the previous and first changed sample. Do
  not claim an exact time or label it a livepatch unless separate evidence
  verifies the cause;
- preserve gaps and confidence. Fifteen-minute persisted sampling can miss a
  short boot or only bound a livepatch transition.

Future nodectld reports make new events exact. The public resource returns a
safe timeline such as:

```text
id
node_id
event_type                 boot | livepatch | reported_release_change
booted_at
booted_release
reported_release
effective_after            exact time when known, otherwise null
observed_after
observed_before
source                     node_report | reconstructed_node_status
confidence                 exact | inferred | incomplete
current
```

The raw boot UUID, Nix store path, configuration digest, livepatch internals,
and exposure counts remain out of this user-facing projection. On the WebUI
cluster overview, make the existing kernel value a link to a per-node timeline
showing boots and indented livepatch/release changes. Advisory node rows can
link to the same timeline around `vulnerable_until`/`mitigated_since`.

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
updates the kernel event log and stores a compact internal event whenever the
semantic evidence fingerprint changes, including mitigation changes that occur
without a reboot.

Add an admin-only `node.security_evidence#index` action. It returns a
point-in-time, revisioned snapshot shaped as follows:

```text
meta
  schema_version, generated_at, evidence_revision, node_set_digest
nodes[]
  id, domain_name, role, active, evidence_observed_at, freshness
  kernel
    boot_id, booted_at, booted_release, reported_release
    vpsadminos_revision, kernel_source_revision, config_digest
    history[]             same lifecycle, with internal exact identifiers
  runtime_mitigations
    livepatches[]         id, revision, state, applied_at, verified_at
    ebpf_programs[]       id, revision/digest, hooks, state, attached_at,
                          verified_at
  runtime_kernel_state
    loaded_modules[]      module identity/version and observed_at
    security_settings[]   selected runtime settings with source/freshness
  gaps[]                  time range, missing evidence, effect on confidence
```

It returns only the active advisory node set, boot/kernel/mitigation timeline,
immutable build/configuration identity, runtime module/security state,
freshness, and confidence gaps. It does not return IP addresses, resource
utilization, individual VPSes/users, workload counts, general logs, or CVE
conclusions. The security-advisories repository combines these measured facts
with pinned vpsAdminOS/configuration and vpsAdmin policy source analysis.

Do not return `untrusted_vps` or per-node KVM-enabled VPS counts. All
user-controlled VPSes are untrusted by definition, and KVM access is the
default vpsAdmin policy, so those counts add noise rather than evidence. For a
KVM CVE, use the versioned vpsAdmin feature policy plus measured node facts
such as the node role and loaded KVM modules. If a future vulnerability depends
on a non-default optional interface, add a specifically named factual signal
for that interface rather than a generic workload category.

The unpublished central-log work remains useful for an operator-controlled
one-time cross-check/backfill, but is not a runtime dependency and does not
justify an SSH or root credential for this project.

### Draft submission and token scope

Use the existing resource actions. The repository stores the vpsAdmin advisory
ID and a digest of the last canonical draft snapshot in `submission.yml`. A
submission run:

1. reads the advisory, CVEs, and node statuses;
2. stops with a diff if they no longer match the recorded snapshot, so WebUI
   review edits are not overwritten;
3. creates or updates the advisory text, then reconciles CVE and active-node
   rows using their existing create/update/delete actions;
4. reads everything back, validates the complete node set, and records the new
   digest and source repository commit.

An interrupted run may leave an incomplete draft, which is acceptable because
it is not visible to users and publication validates completeness. Re-running
converges it. After review feedback, Codex first incorporates the canonical
WebUI changes into the committed analysis/submission files, then performs the
same reconciliation. The client refuses to alter a published or retracted
advisory.

The runtime token therefore needs these existing actions:

```text
node.security_evidence#index
security_advisory#index
security_advisory#show
security_advisory#create
security_advisory#update
security_advisory_cve#index
security_advisory_cve#create
security_advisory_cve#delete
security_advisory.node_status#index
security_advisory.node_status#create
security_advisory.node_status#update
security_advisory.node_status#delete
```

The evidence response is authoritative for node identities and labels, so
`node#index` is unnecessary. `security_advisory#index` is used only to recover
or verify the stored advisory ID by CVE. `security_advisory_cve#update` and
`security_advisory.node_status#show` are unnecessary because CVEs are reconciled
by create/delete and node rows are returned by index. The token has no generic
node/VPS access, publication, mail, retraction, user/session creation, or `all`
scope.

As a small general API hardening, make the existing advisory, CVE, and node
status mutation actions reject non-draft advisories. Add an optimistic
precondition (canonical content digest or revision covering parent and child
rows) so a human edit between the client's read and write produces a conflict.
These protections improve the existing API without introducing a parallel
submission endpoint.

Token issuance and self-revocation are authentication-provider operations, not
resource action scopes. `bin/create-token` performs the interactive password
and optional TOTP exchange directly against HaveAPI, requests only the resource
scopes above, and stores the returned token outside git at
`$XDG_CONFIG_HOME/vpsfreecz-security-advisories/token.json` with mode `0600`.
It never prints the token or enables shell tracing. A permanent token is
reasonable for sporadic CVE work because its server-side authority is narrow
and revocable; the script also accepts an explicit lifetime and renewal
interval.

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

### User-facing advisory text

Render summary, description, and response from a structured impact assessment,
but keep the final prose natural and specific to the CVE. The audience controls
individual VPSes while administrators control the shared kernel, so every
advisory should answer:

- what access an attacker needs inside a VPS before reaching the bug;
- whether successful exploitation can grant UID 0/capabilities only in the
  VPS's user namespace;
- independently, whether there is a realistic path to credentials or code
  execution in the initial user namespace/node, and whether that enables
  access to other VPSes;
- whether exploitation or failed attempts can cause node-wide denial of
  service even when node compromise is not realistic;
- whether hardening such as init-on-alloc/free, slab freelist hardening, or
  stack initialization prevents the trigger or merely makes reliable
  exploitation harder;
- likely failure modes of attempted exploitation, such as a NULL pointer
  dereference, general protection fault, kernel oops, or node instability, when
  supported by the bug analysis;
- that node kernel reports are monitored, while making clear that monitoring
  detects failures and is not itself a mitigation or proof that no attempt
  occurred;
- the exact administrator response: fixed booted kernel, livepatch/eBPF
  mitigation if applicable, per-node time, and whether users need to act.

When true, explicitly tell users that no guest kernel update or VPS reboot is
needed because vpsFree.cz manages the shared node kernel. Do not claim that no
exploitation was attempted unless monitoring evidence was actually checked,
and phrase absence of observed kernel faults as evidence rather than proof.
Keep exploit mechanics and full reasoning in `analysis.md`; public text should
explain risk and response without becoming an exploitation guide.

Record these impact conclusions independently in `assessment.yml`:

```text
impact.vps_root             yes | no | unknown
impact.node_escape          not_reachable | no_known_path | plausible |
                            realistic | demonstrated | unknown
impact.cross_vps_access     yes | no | conditional | unknown
impact.node_availability    none | possible | likely | demonstrated | unknown
```

Do not infer node escape from the CVE's "local privilege escalation" label, a
memory-corruption class such as UAF, or a proof of concept that merely prints
UID 0. The analysis must identify which user namespace owns the resulting
credentials/capabilities and what additional primitive would be needed to
cross into the initial user namespace. A strong kernel read/write or code
execution primitive can make escape plausible, but that is a separate
conclusion which must be justified.

## Preliminary CVE conclusions

These are source/configuration conclusions, not final node statuses. Final
submission requires the boot and mitigation timeline from vpsAdmin.

| CVE | Platform assessment | Upstream 6.12 fix |
| --- | --- | --- |
| CVE-2026-23111 (`nf_tables`) | Reachable to an unprivileged VPS through user and network namespaces with `CONFIG_USER_NS` and nftables enabled. Init-on-alloc/free and slab hardening make exploitation less reliable, but do not make the UAF non-exploitable. Nodes are fixed once booted into 6.12.70 or a kernel containing the fix. | 6.12.70, `1444ff890b4653add12f734ffeffc173d42862dd` |
| CVE-2026-46242 (Bad epoll) | Unprivileged epoll UAF/free-to-wrong-cache path is reachable. The write can target a reused live object, so allocation initialization is not a sufficient mitigation. 6.12.93 is affected; 6.12.95 contains the fix. | 6.12.95, `9324de74a3a59b9fde9b62ee45ebaa71458ba2e5` |
| CVE-2026-53362 (IPv6) | Unprivileged UDPv6 splice/`MSG_MORE` path is present. The overwrite is within a live skb allocation, so init-on-alloc/free does not block it. 6.12.93 is affected; 6.12.95 contains the fix. | 6.12.95, `46f201f8b4c39633a1fa3dc12459f506d470993d` |
| CVE-2026-53359 (KVM) | The trigger is tenant-reachable because new VPSes default to KVM enabled and nodectld grants `/dev/kvm`, so a tenant controls KVM userspace/memslots and its nested guest. Reachability alone does not establish node escape; the KVM UAF primitive must be assessed separately for VPS-root, node-escape, cross-VPS, and denial-of-service impact. 6.12.93 is affected; 6.12.95 contains the fix. | 6.12.95, `2ad3afa40ac6aa340dada122f9abfa46c0a6eb35` |
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

The implementation uses additive vpsAdmin migrations, a schema-versioned
optional nodectld payload, and exact non-production configuration pins. The
deployed sequence is:

1. migrate/deploy the tolerant vpsAdmin receiver and new API resources;
2. deploy the node-side vpsAdmin package so exact evidence begins to arrive;
3. deploy vpsAdminOS/configuration metadata files on nodes;
4. run the idempotent historical reconstruction task;
5. collect evidence and resolve every `unknown` before syncing any CVE draft.

Mixed old/new versions are supported. Old nodectld payloads continue updating
ordinary node status while security evidence remains missing/stale. A future
unsupported evidence schema is ignored without rejecting the status. Missing
vpsAdminOS/configuration metadata is returned as an explicit gap rather than a
false conclusion. No coordinated all-node reboot or update is required.

- Advisory repository files and tooling add no runtime or persisted platform
  state outside vpsAdmin drafts.
- Any vpsAdmin API addition must be additive. Existing clients and older
  nodectld payloads continue to work unchanged.
- The kernel-event table and evidence fields are additive migrations. Backfill
  is restartable/idempotent and retains source/confidence instead of rewriting
  `node_statuses`.
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
- The visible kernel-history page requires the canonical
  `vpsadmin-kb-captures` WebUI workflow, durable documentation-contract update,
  and Czech/English screenshot review.

## Testing plan

- Verify exact action scopes from the live API description and exercise a
  generated token against an allow/deny matrix without printing the token.
- Test reconstruction from 15-minute status samples: first observation,
  ordinary reboot, same-kernel reboot, same-boot UTS change, clock skew, missing
  samples, rapid reboot, and idempotent repeated backfill.
- Test that all logged-in users can read only the sanitized kernel history and
  that unauthenticated requests and sensitive fields are rejected/absent.
- Unit-test kernel boot grouping, version comparison (including stable-branch
  backports), incomplete history, clock/uptime tolerance, node-set drift, and
  mitigation composition.
- Test semantic evidence events for reboot, livepatch and eBPF changes; verify
  that a mutable UTS release cannot masquerade as a newly booted kernel.
- Test runtime module/security-state reporting and verify that the evidence
  response contains no tenant/workload counts or identities.
- Use recorded API fixtures for deterministic advisory create/update/reconcile
  tests; require explicit opt-in for writes to a real API.
- Test idempotency, partial-failure recovery, dry-run output, and refusal to
  publish.
- Test review iteration: clean resubmission, stale revision conflict, human
  WebUI edit, reconciliation, and hard refusal after publication/retraction.
- Test each vpsAdmin API change in its focused RSpec topic and run RuboCop and
  repository hooks before commit.
- After intended code changes are committed and quick checks pass, run the
  mandatory standalone change review before long integration tests.
- Integration-test against a dev vpsAdmin API and verify that only a draft is
  created, every active advisory node gets one status, removed nodes are not
  silently retained, and the scoped token is denied unrelated and publish
  actions.
- Verify the token can perform only the listed advisory/CVE/node-status reads
  and draft mutations, while the allow/deny matrix rejects publication, mail,
  retraction, non-draft mutation, and all generic node/VPS/user resources.
