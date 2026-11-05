# Machine reservations without a packaged machine catalog

**USER ACCEPTED; IMPLEMENTATION + DEPLOYMENT AUTHORIZED — 2026-11-03.**
Implementation is not yet verified. The user directed implementation and deployment
of this latest cooperative naming proposal. The authoritative typed interfaces,
compatibility and owner packages are now frozen in the
[execution contract](design.md#machine-identity-execution-contract); that contract
supersedes the illustrative format/API choices below. Default integration and
session lifecycle actions remain unauthorized. This remains a separate feature
from service cleanup and capacity retry.

## Recommended rule

Derive a machine resource automatically from configuration, in this order:

1. If configured, use the explicit global `labels."dev-workspace.lock-id"`.
2. Otherwise use **canonical repository origin + exact canonical configured
   machine name/selector**.

Use this same default whether the machine's hostname is `vps`, an FQDN or absent.
A configured target may itself be named by its FQDN; it still belongs to its
repository namespace. Hostnames, DNS, SSH addresses/ports and display labels do
not select the locking namespace. No target connection, machine-ID read, DNS/PTR
lookup, hardware inventory or per-command identity probe is needed.

For example, using existing canonical JSON/digest conventions:

```text
machine:repo-target:v1:<digest([canonicalOrigin, canonicalMachineName])>
machine:shared:v1:<digest([explicitSharedLockId])>
```

The digest only encodes an unambiguous tuple; it is not proof of physical identity.
Version the derivation and use the same function for claims, compatibility and
profile checks. Never include a checkout path, common Git directory, branch,
commit, session or workspace in the portable key. Common Git directory and source
revision remain ownership/admission evidence, as in existing repository claims.

| Configuration | Result |
| --- | --- |
| Two worktrees/clones of the same canonical repository, same configured target | Same lock, even on different branches or in different registered workspaces. |
| Different repositories each have a target/hostname named `vps` | Different locks. |
| One repository has several machines whose OS hostname is `vps` | Their distinct configured selectors, such as `site-a/vps` and `site-b/vps`, distinguish them. Do not use the nonunique OS hostname. |
| One configured target gains a domain, IP or SSH alias | Lock stays unchanged while repository identity and configured selector stay unchanged. |
| Two repositories or two configured targets intentionally deploy the same machine | Put the same explicit shared lock ID in all participating target configurations. |

This deliberately accepts the user's assumption that cross-repository overlap is
rare. Different configuration names do not automatically converge on physical
identity. A real overlap needs a shared override; forgetting it can permit parallel
deployment. Conversely, reusing a configured selector for another machine retains
the logical lock. These are cooperative naming rules, not physical discovery.

## Source-supported minimal implementation

The required metadata already exists in pinned confctl
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`:

- `Machine.name` is the canonical configured name; `target_host`/`target_port`
  are separate routing fields (`lib/confctl/machine.rb:36–55,96–109`). Require one
  exact target and use the resolved canonical name, not an unexpanded selector,
  glob, caller alias or display label.
- `cluster.<name>.labels` is already an extensible attribute set
  (`nix/modules/cluster/default.nix:142–147`). The optional shared ID therefore
  needs no confctl option/schema change. Read it as a bounded nonempty string;
  compare it exactly and reject malformed values. It is configuration-owned,
  not an arbitrary per-claim/per-session override.
- The generic runtime already validates registered repository ownership and its
  canonical SSH origin (`workspace-coordination.rb:117–125,808–891`, installed
  `0q7rc75dh4mjrxpb37m1hchfwcbmpa7a`). Reuse those rules: SCP/SSH URL forms converge,
  host case is normalized, `.git` is removed, GitHub path normalization is retained.
  Do not invent another repository canonicalizer or use local clone names as IDs.

No FQDN classification, IDNA policy or hostname normalization is needed for this
rule. If an FQDN is chosen as an explicit shared ID, participating configurations
must use the same stable string. No inferred equivalence from DNS or routing.

## Proposed request flow

Keep the existing acquire/status/wait/release workflow. Add a configuration target
form instead of requiring a packaged machine name. Illustrative new request:

```json
{
  "schema": 2,
  "requestId": "11111111-1111-4111-8111-111111111111",
  "label": "Deploy configured target",
  "repositories": [],
  "machines": [{"repository": "vpsfree-cz-configuration", "selector": "cz.vpsfree/machines/aitherdev"}]
}
```

`dev-session coordination acquire SESSION --as-is --request claim.json --json`
uses the registered repository and its pinned adapter to resolve metadata locally,
derive the resource and record the source/selector/resource mapping. An optional
read-only preview can show the derived key before acquisition; it needs no separate
identity-registration store. The adapter must not call today's build/copy/native
`inspect` operation merely to derive a lock. Existing labels/name metadata suffice.

Preserve the current package/session-generation and repository proof checks.
Recheck the local mapping before atomic admission under the existing ledger mutex.
Once accepted, request-ID retries, held/waiting resources and their source mapping
stay frozen; a changed request or mapping cannot silently retarget that claim.
Normal configuration/deployment authorization and retained artifact checks remain.
Waiting notifications and release semantics are unchanged. These resources are
global across registered workspaces sharing the coordinator's state; separate
coordinator state roots still need a common authority to coordinate each other.

## Renames, existing locks and profile activation

Changing a configured selector or canonical origin intentionally changes the
namespace. Plan that change explicitly: retain a stable shared override or bridge
the old and new resource while old ownership/recovery exists. Do not infer a rename
from equal hostnames, addresses or coincidentally similar source content. Changing
or adding an override is also a resource-identity change, not a harmless label edit.

Existing catalog names/IDs and held/waiting claims, legacy reservations, sealed
attempts and recovery commands keep their original keys and formats. The one-time
upgrade maps those known legacy targets to the new derived resource and preserves
conflict aliases, so new claims cannot bypass an old hold. Publish/recheck bridges
under existing coordinator locking; conflicting or unresolved mappings refuse.
Retain the old catalog decoder for original operations. This compatibility bridge
is not a new mandatory catalog or enrollment step for every future machine.

The existing `profileMachine` mapping can resolve to the same derived logical ID
for its configured repository/target, with its legacy alias preserved. Profile
activation continues to require the owning held machine claim under its existing
transition locks. It does not require SSH or a local machine-ID probe. This is one
profile-host mapping, not a package list of every deployable machine.

Keep legacy request/claim readers and exact recovery paths. New dynamic requests
need explicit package capability protection against older interpreters that only
understand catalog machines; freeze the precise format/capability seam before any
future implementation. Never rewrite held keys, discard evidence or release
reservations merely to complete migration. Original system/profile ordering,
forward recovery, machine retention and explicit integration requirements stand.

## Boundaries and later checks

Minimal owners are **dev-workspace** (logical resource derivation, request/claim
and profile compatibility) and **vpsfree-dev-workspace** (local confctl metadata
resolution). The consuming workspace needs a one-time policy/selection update to
remove the mandatory packaged machine list. **No confctl source change, native
mutation guard, target identity registry or new deployment framework is required.**
New ordinary machines are configured in their owning repository as usual; only
intentional shared targets need the optional shared label.

Future focused fixtures should prove convergence across clones/worktrees/branches,
separation of unrelated repositories with `vps`, unique selectors with duplicate
OS hostnames, stable keys after hostname/address changes, exact shared overrides,
changed-source/request refusal, atomic alias contention and legacy held/waiting/
reservation exclusion. Cover profile ownership, interruption, replay and incapable
package refusal using existing Ruby claims/host and extension adapter tests.
Assert derivation makes no SSH/DNS/native calls. No checks were run for this revision.

## Superseded alternatives and evidence

The earlier authenticated native-ID/physical-continuity proposal is rejected as
the default: it adds probes, identity state and deployment guards beyond the user's
chosen cooperative contract. An automatic global-FQDN/default-repository fallback
is also rejected: it adds classification and changes namespaces when a host gains
or loses a domain. Stronger physical/inventory guarantees remain a separate future
requirement, not a prerequisite for this proposal.

Current restriction: workspace `config/coordination.nix:13–23` compiles aitherdev
into `coordination.json`; generic `Catalog.machine` accepts only those aliases,
and `claim_resources_for` emits `machine:<catalog id>` (installed runtime
`workspace-coordination.rb:741–788`, `workspace-coordination-claims.rb:127–134`).
The installed extension adapter already resolves `ConfCtl::MachineList` and checks
an exact `Machine.name`; its existing native `inspect_machine` is not needed by
this proposal. Source references: installed tools `9019d7wm0c40q59vrnlf1clwp7q00xrd`,
extension docs at `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`, and pinned confctl above.
This record preserves proposal rationale. Architect changed only design documents;
implementation, checks, publication and rollout belong to the assigned owners.
