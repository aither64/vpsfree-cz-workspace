# Portal provider selection and limits preview

## Authorized outcome

The user approved implementation of the conversational plan, including rollout on
aitherdev through vpsfree-cz-configuration and the workspace user profile.
Initial choices are the existing Codex subscription and codex-lb on Snajpa.
The popup previews any configured provider without changing routing; its explicit
Switch button records a workspace-wide request that waits automatically until idle.
A pending request is cancelable before application. Include codex-lb usage metrics.
No default-branch integration, lifecycle cleanup or forced interruption is approved.

## Projects and implementation

codex-web owns generic explicit provider selection/effective runtime settings.
dev-workspace owns the provider catalog, private workspace state, durable worker,
limits adapters, guarded native transition, portal UI and recovery contract.
workspace owns the composed user-profile pin. vpsfree-cz-configuration owns the
matching host input and aitherdev provider definitions. Preserve the extension pin.

The lead owns design and source edits; this tracking-only initiative has no saved
roster. Use the installed review fallback and utility watcher policies when required.
The implementation/verification brief is [design.md](design.md).

## Compatibility, rollout and documentation

Use additive versioned provider state/journals and publish compatibility requirements
in the runtime contract. Existing installation without selection keeps its current
routing. Preserve global config/auth, thread IDs/history/model/effort/member access.
No native version upgrade. Recovery uses native APIs and never overwrites histories.

Run quick checks, commit, publish and complete mandatory independent whole-branch
review before longer checks. Keep feature configuration unmerged during rollout.
Deploy host definitions with confctl, verify composed input identity, then select the
user-profile application in a safe idle window. Never kill VMs to deploy or switch.

Readers are portal users/operators and runtime/client maintainers. Put lasting
behavior/recovery in project docs; site configuration/rollout instructions in the
configuration repository. Keep dated verification and rollout evidence here. Apply
vpsfree-user-facing-writing after technical facts are settled.
