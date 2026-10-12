# Design and verification brief

## Scope and contracts

Implement the approved initial subscription/Snajpa catalog and workspace-wide
routing switch. The sidebar always describes the effective active provider.
The existing info dialog has a preview select box plus an explicit Switch button.
No per-thread provider controls, browser credential editing, LB reset redemption,
Codex upgrade, default integration or forced interruption are included.

The host Nix module writes a nonsecret catalog at
/etc/dev-workspaces/codex-providers.json (schema 1). Entries contain id, label,
kind (subscription/codex-lb), base URL and token file for LB; no raw secrets or
browser-controlled executable paths. Built-in subscription ID is openai; retain
codex-lb as Snajpa's existing native ID. LB native definitions use Responses,
disable websockets and read the referenced token through the native auth helper.
Native config/auth in ~/.codex remain untouched. Missing catalog preserves old
runtime behavior; selection/preview of unavailable definitions is refused.

Private provider state below the user-state root is keyed by registered workspace
name and bound to its canonical root/socket. Schema 1 records the active provider
and at most one durable request. Request fields include UUID idempotency identity,
target catalog digest, phase, blockers, timestamps and recovery snapshot reference.
Phases distinguish waiting, applying, applied, canceled, failed and recovery-required.
Request/cancel/status go through the stable workspace-host provider command; a
separate user service owns waiting/application independently of browser/portal life.
The worker does not hold the global transition lock while waiting. Cancellation
and applying admission share the request lock: cancellation loses once applying
has been durably accepted. Different concurrent targets require cancel/resubmit.

GET /api/codex-providers returns only public names/IDs, active identity and operation
status. GET /api/codex-limits accepts an optional configured provider ID; omitted
means active routing. POST provider-switch and cancel accept bounded IDs and use
exact-origin checks. No browser socket, cwd, token, path or URL is trusted.
Cache reads per provider/catalog/credential identity, coalescing requests for 30s.
Browser preview caches remain separate from active sidebar state and reject late
responses for an earlier selection. Existing visible minute refresh timing stays.

Subscription metrics use native account/rateLimits/read even while LB is active
(verified successful on the deployed server). Native duration fields determine
window labels. Existing reset actions remain available only for active subscription.
LB metrics use GET base_url/usage with the referenced Bearer token server-side.
Show own API-key quotas separately from upstream aggregate quota; prefer explicit
upstream_limits over mirrored legacy aggregate rows in limits. account_pool_usage
percentages are remaining, not used. Preserve row units/windows/model scopes/reset
times; missing/hidden values mean unavailable, not unlimited. No dashboard credential
or dashboard API is needed. Keep totals/estimated cost labeled as reported usage.

## Transition invariants and data flow

Inventory current active tracking roots and saved nonremoved members through
existing manifest/roster/receipt authority. Read native metadata without implicitly
activating cold histories. Include every loaded native thread in safety checks;
unowned/ambiguous writers block restart rather than being migrated by guesswork.
Active turns (including sleep/waits), pending requests, queues, active goals,
unresolved submissions and unfinished lifecycle/creation/package work block apply.
While waiting, allow ordinary work to continue and publish those blockers.

For application, take the existing exclusive transition lock and verify exact
current profile generation. Re-read catalog, ownership and activity. Probe target
authentication/connectivity and retained-model compatibility without spending an
inference request. Record exact original per-thread routing/model/effort/policies,
the originally loaded set and terminal restoration identities before mutation.
Root policy remains application-owned; members rebind saved roster model/effort,
instructions and access. Preserve directory/environment/runtime roots and approval
settings. Provider overrides must not reset reasoning effort to the global default.

Reserve the durable applying journal; all portal/CLI mutation admission and implicit
loading honor that reservation after taking their usual locks. Quiesce managed
terminal clients. Inspect the complete Codex cgroup: only the proven native daemon
may be stopped; VMs/unrelated processes block the operation. Do not stop the portal,
tmux, clusters or goals. Stop the shared daemon and obey its writer-lock release.

Use the exact active profile's native binary in isolated temporary App Server
processes to cold-resume the exact inventoried IDs with explicit modelProvider and
preserved settings. Capture effective resume responses; native metadata alone is
not proof of loaded routing. Exit private writers before the shared server starts.
Persist active selection, start the shared server with workspace-scoped catalog and
provider overrides, restore original clients, and verify routing/settings before
success. Terminal restore failure is reported separately from verified applied
routing, with supported sync/recovery instructions and no false success.

On provider failure, native cold resumes compensate every touched thread to its
original provider/settings, preserving any appended history. Restart original
routing and restore terminals. Persist the journal if compensation cannot be
verified; refuse conflicting writers until explicit recovery completes. Boot and
service startup must respect an applying journal so recovery precedes ordinary
thread activation. Compatible package updates preserve waiting intent; target
catalog changes fail the request rather than changing its meaning. In-flight
applying journals exclude package transitions. Runtime contract advertises provider
state schema/transition policy and target generations must support existing state.

All application creation, fork, activation, reconnect and revival paths supply the
workspace selection explicitly and preserve saved model/effort. Observer clients
remain read-only. Generic codex-web exposes explicit provider fields/results and
an application-owned resume hook; it does not own workspace catalogs or switching.

## Acceptance and verification

Quick focused Go/Ruby/browser contracts: configuration validation/redaction, origin
protection, idempotency/cancel races, per-provider caches, popup preview independence,
LB units/percentages/deduplication, stale responses, waiting blockers, wrong owner,
generation changes, unsafe cgroups, journal recovery and retained policy preservation.
Protocol request corpus/generated schemas validate the selected 0.160.0 binary.
No production provider mutations during development checks.

After committed whole-branch independent review, run isolated native integration
cases in both directions with exact history-prefix/settings checks, crash injection,
writer-lock refusals, boot recovery, and old/new state-reader/package compatibility.
Run packaged checks and scoped aitherdev build/dry-activation through a fresh utility
watcher. Preserve current cluster ownership; stop unexpected local kernel builds.

Publish exact client/runtime heads. Update the workspace nested runtime pin while
preserving extension/sibling/follows identities; configuration uses channel
'dev-workspace', role 'devWorkspace'. Run check-dev-workspace-deployment on final
locks. Deploy the host catalog/module from the configuration feature worktree and
select the application from the workspace feature worktree's user-profile package.
Require an idle restart-safe service inventory for rollout; retain recovery refs and
journals. Validate both previews, then guarded subscription/back-to-Snajpa switching.
Keep all feature branches unmerged pending explicit integration direction.
