# Network-permission failure: bounded diagnosis

Owner: implementer3, 2026-10-24. Scope: read-only native/platform diagnosis;
architect0 owns remedy decisions. No foreign-session team addressed or records
edited; no prompts, conversation history or credential values inspected.

The reported failure is confirmed on the exact retained root thread
`01a163b4-e2c6-7081-b9cb-e7a0e78eab4b` of
`2026-10-22-limit-autostart-alerts-to-boot`. Native diagnostic row `837463993`
records **2026-10-24T10:33:34.880958126Z**, process
`pid:3387667:2336fd49-362b-4fcb-bba3-81ce451a3648`, target
`codex_core::session::turn`, `core/src/session/turn.rs:887`, with diagnostic:
`Fatal error: application network permission was revoked`.
See [sanitized evidence](evidence.json).

This is native application-policy enforcement. Upstream `rust-v0.163.0`
[`http-client/src/network_policy.rs:41`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/http-client/src/network_policy.rs#L41)
defines the exact phrase as `NetworkPolicyDenied::Revoked`, a deterministic
denial. `Fatal` has no native retry delay
([`protocol/src/error.rs:406`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/protocol/src/error.rs#L406)).
The message does not establish an operator permission change or filesystem
sandbox denial. Eight distinct threads on the same process logged this fatal
in the bounded 10:33:33–10:33:35 UTC interval.

The semantic error differs from raw `EMFILE`. Existing owner0 evidence records
a socket-accept `EMFILE` at 10:33:34.383697Z, **497.261126 ms before** the
affected root's fatal. A cascade is plausible: failed local requirements
load/compose calls `fail_application_policy`; its controller becomes unavailable
and revokes outstanding permits
([`application_network.rs:44`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/application_network.rs#L44),
[`network_policy.rs:150`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/http-client/src/network_policy.rs#L150)).
Account invalidation or a newly restrictive policy can also revoke permits.
**The initiating reload, error and invalidation path were not captured in the
scoped diagnostics, so EMFILE causation remains unproved.** Exact-root auth
reloads immediately beforehand reported `changed: false`; no auth content was
read. This does not exclude another trigger.

Smallest source-supported recovery candidate, for architect/lead authorization:
after the accepted descriptor relief, use the ordinary supported `config/read`
path to reload current requirements successfully, then manually continue the
**same retained conversation**. `ConfigManager::read` calls
`load_config_layers`, which refreshes and publishes application policy
([`config_manager_service.rs:118`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/config_manager_service.rs#L118),
[`config_manager.rs:503`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/config_manager.rs#L503)).
Successful publication enables new permits; an already revoked request stays
revoked. This recommendation is source-backed, **not executed or verified on
the affected thread**. No evidence currently requires new identities, wider
permissions, logout or daemon restart. A failed reload should retain its exact
error for diagnosis before another remedy is chosen.

Reused [owner0 journal evidence](../incident-emfile-625e1f52/journal-network-correlation-decoded.json)
and [same-PID descriptor relief](../incident-emfile-625e1f52/live-nofile-relief-20261024T105239Z/result.json).
No FD sweep or repeated journal query was performed. Source URLs, exact hashes
and relevant excerpts are in [native-source.json](native-source.json).
No live mutation, reload RPC, retry, signals, restart, cleanup, source edit,
build, test or CI was performed.
