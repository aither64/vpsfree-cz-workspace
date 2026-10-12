# Portal Codex provider selection

## Goal and scope

The user asks for provider selection in the portal and provider identity beside
Codex limits. Implement the reusable portal/runtime in dev-workspace and native
client support in codex-web. The proposed selector applies to the whole registered
workspace, including retained roots and members; an optional scope question is
pending. Use a separate initiative because this conversation has no existing
session binding. The completed operational switch remains separate.

Show configured provider IDs and names, including the built-in subscription
provider. Keep credentials and executable authentication configuration server-side.
Display effective routing and any pending change clearly. Account subscription
limits must not appear to describe a custom provider which does not report them.

## Design and safety requirements

The selected native App Server ignores provider overrides on loaded threads.
Provider application needs a guarded reload operation, preserving exact retained
conversation IDs, histories, models, effort, instructions and member access.
Never archive conversations or use a service restart that kills development VMs.
Refuse active turns, pending requests, queued work, active goals, lifecycle/package
conflicts and additional processes in the Codex service cgroup. Leave the portal
and tmux running. Use native APIs for retained provider changes, not database or
rollout rewrites. Record recovery state before a runtime mutation and recover the
shared server if a transition is interrupted. Native writer locks remain binding.

Confirm ownership, persistence and runtime-generation boundaries in the existing
code before choosing the durable format. Keep provider defaults scoped to one
workspace; do not silently modify other registered workspaces or authentication.
Use only configured provider IDs, server-owned sockets/paths and exact-origin
mutation protection. Record the final design and verification brief before edits.

## Compatibility, deployment and recovery

Consider old/new portal clients, package generations, provider-state and operation
journal schemas, native experimental protocol, and rollback loading of persisted
state. Keep additions backward compatible where possible and document any required
ordering or refused downgrade. Source changes remain on dedicated feature branches.
Publishing branches and checks does not authorize default-branch integration or
live deployment. No live provider change is needed to develop this feature.

## Verification and documentation

Use protocol-schema/request tests for provider reads and overrides; unit/contract
tests for selector validation, secret redaction, account-limit attribution, busy
refusals, settings retention, interruptions and service recovery. Browser checks
cover the sidebar and compact popover. Run quick focused checks, commit, then the
mandatory independent whole-branch review before long integration/build checks.
Use a fresh utility watcher for long or uncertain verification.

Readers are portal users and operators plus developers maintaining the provider
transition. Update the portal guide/README and native-client documentation where
the behavior is owned. Keep dated deployment details in this initiative and
credentials/full histories out of tracking. Preserve unrelated shared changes.
