# Switch retained Codex threads to codex-lb

## Goal and authorization

The user asks to restart the existing managed threads so they use the previously
configured codex-lb provider. Preserve conversation IDs and full history, saved
models and efforts, team membership, instructions, access, worktrees, and cluster
ownership. Scope is the retained threads already loaded in the vpsfree-cz App
Server; inventory and verify exact owners before mutation. This is an operational
initiative, with no application repository changes or registered feature branches.

## Approach and decision gates

Confirm the installed Codex 0.160.0 protocol on disposable histories. Loaded
threads ignore modelProvider overrides on thread/resume; fresh threads accept
codex-lb. Establish a supported reload/unload path before touching managed threads.
Record current native configuration and exact IDs, prove that affected subjects
have no active turn, pending request, queued message, or lifecycle conflict, and
make private backups before applying the provider transition. Verify the live
provider afterward, rather than relying on stored thread metadata. If the native
protocol cannot perform the bounded operation safely, report that limitation and
preserve current operation rather than inventing ownership or bypassing refusals.

## Compatibility, deployment, and recovery

No code, schema, migration, model, or API changes are planned. The load balancer
uses the Responses API and the existing model IDs. Authentication reads the
existing private token file; subscription auth remains unchanged and has a private
snapshot from the initial configuration change. Do not rewrite histories or
retained settings to obtain a provider change. Any temporary disconnection must
preserve saved identities and supported resume behavior. Recovery restores the
old provider through the same supported path and private backups if needed.
A service restart previously killed qemu and virtiofsd processes in the Codex
unit. Do not repeat a whole-service restart or alter cluster state during this
bounded thread operation without first establishing a safe separate contract.

## Documentation and verification

Readers are the user and a future operator recovering this transition. Keep live
findings and operation evidence in state.md and private backups; no secrets or
full rollouts belong in Git. Existing runtime documentation and protocol schemas
are the sources of truth. Quick checks are disposable native protocol probes,
exact ownership/idle checks, and live provider/settings comparison. No build,
long integration test, or application implementation is planned.
