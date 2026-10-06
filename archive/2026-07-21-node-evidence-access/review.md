# Node Evidence Member-Access Review

## Executive recommendation

Do not make the existing top-level Node evidence resources readable by normal
users. They are an internal, lossless evidence contract and include inactive
Nodes, immutable historical snapshots, stable internal IDs, raw command lines,
Nix closure paths, the full tracked host-hardening state, loaded kernel modules,
and exact livepatch/eBPF implementation details.

Instead, follow the precedent established by
`node.kernel_history#index`: add narrow Node-scoped member projections which
force an active `node` or `storage` role and return only explicitly selected
fields. Unknown fields and newly collected evidence must remain private by
default.

Recommended member-visible data:

1. Keep the existing sanitized kernel history unchanged.
2. Expose booted and currently activated software identities for vpsAdminOS,
   vpsAdmin, nixpkgs, and system configuration, including exact public Git
   revisions and dirty state.
3. Expose a sanitized software deployment history for those same components.
4. Expose evidence freshness and a generic complete/partial/unavailable state.
5. Expose only an explicit allowlist of current boot parameters whose values
   describe a member-visible capability or a deliberately public hardening
   claim.
6. Expose only an explicit allowlist of current sysctls which members can
   observe or whose values define supported VPS functionality.

Keep raw boot command lines, unrestricted parameter/sysctl resources, full
kernel configuration, loaded modules, livepatch/eBPF internals, Nix store
closure paths, raw collection errors, and reconstruction gaps administrator
only. Publish conclusions drawn from those data through reviewed security
advisories instead.

No authorization bypass was identified in the reviewed paths. The current API
and WebUI intentionally separate sanitized member history from administrator
evidence, and the focused API suite passed 20 examples with no failures.

## Current access model

The current model is internally consistent:

- `Node::KernelHistory` is a nested API resource for every authenticated user.
  It forces active Node/storage records and projects only its row ID, event
  type, release, effective/observation interval, source, confidence, and
  current state.
- The projection excludes the boot ID, linked evidence object, source status
  ID, report/snapshot revisions, kernel source/configuration identity, command
  line, and system closure paths.
- Every top-level typed kernel-evidence resource is administrator-only. The
  shared component index applies the same restriction to parameters, modules,
  sysctls, software versions, collection errors, livepatches, and eBPF data.
- The WebUI shows Kernel history and System history to logged-in users. It
  guards boot detail, current kernel parameters, sysctls and their history, and
  software versions with `isAdmin()`.
- The Ruby API remains the actual security boundary. Direct requests by a
  normal user receive 403 even if a WebUI URL is constructed manually.
- Kernel release, Node name/FQDN, role, status, location, cgroup version, and
  several capacity/health facts are already available through the unauthenticated
  public Node status action. Member-only projections therefore should not try
  to hide facts which the current public contract already discloses.

Relevant source:

- `api/lib/vpsadmin/api/resources/node.rb`, `PublicStatus`, `Show`, and
  `KernelHistory`
- `api/lib/vpsadmin/api/kernel_evidence/component_resource.rb`
- `api/lib/vpsadmin/api/resources/node_kernel_evidence.rb`
- `api/lib/vpsadmin/api/resources/node_kernel_event.rb`
- `webui/pages/page_node.php`
- `webui/forms/node.forms.php`
- `api/spec/api/resources/node_kernel_history_spec.rb`
- `api/spec/api/resources/node_kernel_evidence_spec.rb`

## Data classification

| Data | Recommendation | Reason |
|---|---|---|
| Sanitized kernel history | Expose as-is | Already designed and tested as a member projection; it communicates upgrades, rollbacks and evidence precision without returning the underlying host snapshot. |
| Current kernel source revision | Expose in a new public software/boot profile | It is needed to resolve custom or backported kernels accurately. The Linux/vpsAdminOS sources are public, and the kernel release is already public. |
| Current kernel configuration digest | Safe but optional | The digest reveals no option values and can bind a public review to exact evidence. Show it only with an explanation; otherwise it is an opaque rollout-cohort identifier with little member value. |
| Kernel configuration options | Keep administrator-only | A complete or freely queryable option catalog is a precise map of compiled host attack surface. Security advisories already request and publish only options relevant to a reviewed conclusion. |
| Software identities: component, generation, version, revision, revision provenance and dirty state | Expose | All four source repositories are public. Exact revisions let members verify deployed source and distinguish the booted system from an activated-but-not-booted update. Dirty state is important because it warns that the linked revision is not a complete reproduction. |
| Software deployment history | Expose through a sanitized projection | The same transparency value as kernel history applies. Return component, booted/current generation, before/after version and revision, and the observation interval; omit evidence/event associations and source revisions. |
| `booted_system` and `current_system` Nix store paths | Keep administrator-only | Exact closure paths add host/build fingerprinting and may enable retrieval and inspection of full closures, while public source revisions provide the useful verification identity. |
| Evidence `observed_at` | Expose | Users need freshness context. Exact Node `last_report` is already public, so this adds little operational information. |
| `received_at` | Usually omit | It mainly describes the internal reporting pipeline. A generic stale/partial state is clearer; administrators retain the exact ingestion timestamp. |
| Evidence completeness | Expose as `complete`, `partial`, or `unavailable` | Users should not mistake missing evidence for a safe/default value. Derive this server-side without returning raw error text. |
| Raw evidence errors | Keep administrator-only | Reasons are reporter-controlled strings rather than a public redaction contract and can describe internal paths or collection failures. They also enumerate operational blind spots. |
| `evidence_revision`, `snapshot_revision`, schema version and evidence IDs | Keep administrator-only | They are internal consistency and association mechanics, not useful member-facing facts. |
| Boot ID | Keep administrator-only | It is a stable boot correlation identifier with no member-facing purpose. |
| Raw kernel command line | Keep administrator-only | The reporter captures `/proc/cmdline` without redaction. Current boot flows can contain `init=` Nix store paths and PXE `httproot=` data; future boot tooling could add internal URLs, network configuration, recovery data, or credentials. |
| Unrestricted parsed kernel parameters | Keep administrator-only | Parsing does not remove sensitive values. A future parameter automatically becomes API-visible, so widening this resource would fail open. |
| Explicitly allowlisted current boot parameters | Expose cautiously | Actual boot state can verify public configuration and hardening claims. The allowlist must be owned by the API/public contract, match exact names, and omit unknown parameters by default. |
| Full current sysctl inventory | Keep administrator-only | It aggregates host-only hardening, crash behavior, module loading, address-disclosure controls and exploit mitigations. Some values contain exact Nix store paths, such as `kernel.modprobe`. |
| Explicitly allowlisted member-observable sysctls | Expose current configured/effective state | Values which a tenant can already read or test, or which define supported VPS functionality, add transparency with little new reconnaissance value. Availability and configured/effective mismatch are useful. |
| Full sysctl history | Keep administrator-only initially | Historical weakening and exact change intervals are operational/security telemetry. A later member history can reuse only the same safe-name allowlist if a concrete user need emerges. |
| Loaded kernel modules | Keep administrator-only | The inventory reveals optional attack surface and hardware/feature presence beyond the public service contract. |
| Livepatch module IDs, changed symbols, load/transition state | Keep administrator-only | These fields map exact runtime mitigation coverage and gaps. Publish the reviewed per-CVE outcome, not the raw defensive implementation. |
| eBPF program descriptions, object names, pinned links and attachment state | Keep administrator-only | This is a detailed map of platform-specific defenses and their attachment points. It materially reduces discovery work for bypass attempts. |
| Reconstruction state, source status IDs and gap intervals | Keep administrator-only; expose only generic confidence/completeness | Precise sampling gaps describe internal evidence blind spots. The sanitized history already reports whether each public time is exact, inferred or incomplete. |

## Software versions

Software identities are the strongest candidate for immediate member access.
The reporter supplies only four deliberately defined components:

- vpsAdminOS;
- vpsAdmin;
- nixpkgs; and
- system configuration.

It supplies both the booted closure and the currently activated closure. This
is materially useful: a Node can have an update activated without having booted
its new kernel/system, and a single generic "current version" would hide that
distinction.

All revision targets used by the vpsFree.cz deployment are public repositories.
The WebUI already has safe HTTPS commit-link handling for vpsAdminOS, vpsAdmin,
nixpkgs, and a deployment-configured system-configuration repository. The
review also verified current GitHub visibility for `vpsfreecz/vpsadmin`,
`vpsfreecz/vpsadminos`, `vpsfreecz/linux`, and
`vpsfreecz/vpsfree-cz-configuration` as public.

Recommended public fields:

- evidence observation time;
- generation (`booted` or `current`);
- component;
- version, when supplied;
- exact 40-character revision, when supplied;
- revision source (`native` or `confctl`), primarily for API consumers;
- dirty state; and
- a safe commit link generated from the existing configured HTTPS mapping.

The current WebUI table can be reused visually, but it should call a new
member-safe Node-scoped API action. Administrators may continue using the
existing lossless resources and history.

Sanitized deployment history is also acceptable for members. It should mirror
the public kernel-history pattern: force one active Node, return only the
displayed before/after identities and time interval, and leave event/evidence
IDs and closure paths private.

## Boot parameters

Do not expose the raw command line or make `node_kernel_parameter#index`
member-readable. Both are a generic capture mechanism with no redaction
guarantee.

The current source illustrates why an allowlist is necessary:

- normal boots include public posture parameters such as strict IOMMU,
  preemption, cgroup behavior and slab merging;
- the generated command line also includes the exact `init=` Nix store path;
- netboot/crash handling reads and propagates `httproot=`; and
- other common boot parameters can carry root devices, network addresses,
  recovery locations or credentials.

A public action can instead return exact name/value pairs for a small,
code-owned allowlist. Suitable initial categories are:

- cgroup-mode and dynamic-controller behavior;
- SMT/CPU vulnerability mitigation mode;
- IOMMU enablement and strict/passthrough mode;
- kernel preemption mode;
- LSM/lockdown selection; and
- slab-merging hardening.

The allowlist should contain exact parameter names, not prefixes or a denylist.
In particular, do not expose `init`, `root`, `resume`, `ip`, `BOOTIF`,
`nfsroot`, `httproot`, `rd.*`, `crypt*`, arbitrary `systemd.*`, console or
debug/recovery routing parameters. Unknown and newly introduced parameters
must remain administrator-only until reviewed.

Only the current boot needs this public projection initially. Historical raw
parameter snapshots have less member benefit and expose past defensive states.

## Sysctls

Do not make `node_sysctl#index` or `node_sysctl_change#index` member-readable.
The current reporter has a fixed 34-name inventory, but the API deliberately
accepts any well-formed dotted sysctl name. The public contract would therefore
grow silently whenever the reporter is expanded.

The tracked set mixes several different kinds of information:

- tenant-visible feature switches and quotas;
- generic hardening values;
- host crash, panic and warning behavior;
- module loading and kexec controls;
- pointer/address disclosure controls; and
- exact handler paths such as `kernel.modprobe` and potentially
  `kernel.core_pattern`.

An initial public allowlist should be limited to settings whose effect is
directly observable from a VPS or explicitly defines supported VPS
functionality:

- `kernel.io_uring_disabled`;
- `kernel.io_uring_group`;
- `kernel.unprivileged_bpf_disabled`;
- `kernel.perf_event_paranoid`;
- `kernel.dmesg_restrict`;
- `kernel.yama.ptrace_scope`;
- `net.netfilter.nf_log_all_netns`;
- `user.max_user_namespaces`;
- `user.max_net_namespaces`; and
- `vm.unprivileged_userfaultfd`.

The exact list should receive a product/security review before implementation.
It can later include additional directly observable filesystem behavior such as
the `fs.protected_*` controls. Values which primarily describe host exploit
mitigation or failure handling should continue to be disclosed only in the
context of a reviewed security advisory.

For each public setting, show `available`, `configured_value`,
`effective_value`, and the existing configured/effective comparison. Use the
current snapshot only at first. Do not accept an arbitrary requested name and
then decide whether to render it in PHP; selection and authorization must occur
inside the API query/output contract.

## Remaining typed evidence

The resources which are not currently rendered in the WebUI should remain
administrator-only:

- full kernel configuration options;
- loaded modules;
- livepatch modules and their individual changed symbols;
- eBPF mitigation programs, object names and link attachment state;
- raw collection errors;
- exact internal Node kernel events;
- history reconstruction state and gaps.

The `security-advisories` consumer demonstrates the safer transparency model.
It requests only kernel configuration names declared by a dossier, evaluates
only sysctls relevant to the vulnerability, and publishes a reviewed per-Node
conclusion. This provides members with actionable security information without
turning the API into a general inventory of every host defense and optional
attack surface.

## Scope and authorization design

Public projections should be available to all authenticated members for all
active Node and storage hosts, not only the Node currently hosting one of their
VPSes.

Reasons:

- all active Node names, roles, locations and current kernel releases are
  already publicly visible;
- authenticated members already receive kernel and cgroup history for every
  active host;
- an own-VPS restriction is weak because placement changes and a member can
  observe their current host directly; and
- whole-fleet visibility is the useful transparency property.

Inactive/retired and service-only Nodes must remain excluded, matching the
current kernel-history contract.

Do not change an existing top-level resource from `admin` to `user`. Several
of those queries include inactive hosts unless the caller supplies an optional
filter, and their output schemas expose private associations and metadata.
Suggested API shape:

```text
GET /nodes/{node_id}/software_versions
GET /nodes/{node_id}/software_history
GET /nodes/{node_id}/boot_profile
GET /nodes/{node_id}/sysctls
```

Each action should:

- require authentication;
- resolve `Node.where(active: true, role: %i[node storage])` in the API;
- define an independent output schema with no admin evidence association;
- apply server-side exact allowlists;
- return freshness/completeness explicitly;
- return 404 for inactive, retired, mailer or other service Nodes; and
- omit unknown future fields by default.

The WebUI may show Software versions, Boot profile and VPS-visible sysctls in
the existing Node sidebar for all logged-in users. Administrator pages can keep
their current full parameter/sysctl tables and evidence drill-down, clearly
labelled as internal detail.

## Compatibility and rollout for a later implementation

- Add the new API actions before enabling member WebUI links.
- During a rolling deployment, a new WebUI must tolerate an older API which
  does not yet advertise the actions.
- Do not alter the stored evidence schema or reporter protocol for this access
  change.
- Existing admin resources and automation-token scopes should remain stable.
- Older API clients ignore the additive actions; generated clients can adopt
  them in a later release without changing existing methods.
- Rollback removes only the new read actions/UI links and leaves evidence and
  history intact.
- Any visible WebUI implementation must follow the
  `vpsadmin-kb-captures/docs/webui-change-workflow.md` documentation contract.

## Verification performed

- Reviewed all typed Node kernel-evidence resources and shared authorization
  helpers at vpsAdmin `88f03da44`.
- Reviewed the Node WebUI page guards, parameter/sysctl/software renderers, and
  browser/regression coverage.
- Reviewed the vpsAdminOS reporter's exact collected fields and 34 tracked
  sysctls from current source.
- Reviewed current public vpsFree.cz Node kernel parameters and the generation
  of security evidence from `config.boot.kernel.sysctl`; no production Node or
  production API data was queried.
- Reviewed the current `security-advisories` evidence collector and evidence
  contract at `06ddc840`.
- Verified all software revision targets used by the WebUI point to public
  repositories.
- Ran:

  ```text
  nix develop .#api -c bundle exec rspec \
    spec/api/resources/node_kernel_history_spec.rb \
    spec/api/resources/node_kernel_evidence_spec.rb
  ```

  Result: 20 examples, 0 failures.
