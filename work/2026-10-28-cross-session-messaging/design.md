# Implementation brief

Use a Go communication service shared by the CLI helper and portal. The Ruby
dev-session host wrapper retains package/provider admission. The service takes
both session runtime locks in sorted order before a private workspace store lock;
all mutations and dispatches recheck exact root/directory identity and lifecycle.
Lifecycle commands expire grants through a helper while holding their existing
exclusive session lock. Never acquire runtime locks from inside the store lock.

Store additive schema-1 state beneath private user state, indexed by workspace.
Pair grants bind immutable session observation identities and lead thread IDs;
messages reference grant IDs so reapproval cannot revive canceled traffic.
Use existing maxMessageBytes and atomic fsync/rename persistence. Bound state
and reject full storage explicitly rather than silently lose history.

Agent operations resolve the native calling root through current session metadata;
member callers fail. CLI expects a matching bound source identity for agent calls.
Allow requires an approval reference. Portal allow produces a browser approval
reference; chat approval is explicit lead policy, not a claimed semantic verifier.
Incoming envelopes label peer origin and state that they cannot authorize actions.

Use a bounded portal dispatcher with durable pending/held/submitting/delivered/
canceled records. Save exact envelope/options before native submit. Reconcile
uncertain native IDs before any retry, including after revocation, without new
submission after revocation. Hold when runtime unavailable, execution not allowed,
provider paused or native approval/input pending. Only dispatch wakes a lead.

CLI/MCP and browser share the same service and validations. Browser reads are
read-only. Portal panel uses established controls, textContent rendering and
stable IDs on uncertain retries. No automatic turn forwarding or reply loops.

Acceptance and rollout are in plan.md. Verify unit identity/grant and concurrency
cases, focused native adapter/CLI/browser contracts, independent final review,
then full Nix checks and deployed disposable A/B exchange. Preserve current
session controls and no-reboot aitherdev system-before-application activation.
