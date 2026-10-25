# Final session naming review packet

## Outcome and user decisions

Implement useful automatic naming under one absolute 30-second deadline starting
before queue admission. Preserve native retry progress; permit at most one safe
fresh utility attempt (two calls total), with 200ms cancellable backoff and one
second inference plus250ms cleanup remaining after backoff. Freeze provider,
input, model/effort/schema and settings across both calls. Native progress never
starts a second call. Ultimate failure must stop before identity reservation and
reuse manual slug entry/Retry naming with accepted inputs preserved. No generic
or heuristic fallback. Existing session identities remain unchanged.

User requested the implementation and aitherdev rollout through configuration;
no default-branch integration, reboot or session lifecycle action is authorized.

## Scope, boundaries and consumers

Initiative: 2026-10-20-workspace-session-naming. Read plan.md/state.md/design.md
and the affected repositories' AGENTS.md before reviewing. Worktrees are beneath
worktrees/2026-10-20-workspace-session-naming/{codex-web,dev-workspace,workspace,vpsfree-cz-configuration}.

codex-web owns native ErrorNotification/early identity/terminal settlement and
private proof metadata behind additive CanRetryEphemeralTurn(err) bool, retaining
RunEphemeralTurn signature and errors.Is categories. dev-workspace imports/pins
that client and owns queue/deadline/provider resolution/retry policy/manual flow.
Workspace composes the extension/runtime; configuration's existing channel selects
the matching host contract. Discover any additional actual consumers from imports
and pins; assess the shared interface at those pinned revisions.

Trust boundary: local workspace administrator is trusted; remote protocol/input
validation, concurrent operations, wrong identity, cleanup and interruption remain
relevant. No Codex/model upgrade, new product API, wire/persisted schema, database
migration, broad retry framework, account/provider reconfiguration or PHP change.

## Review assignment

Final committed deliverable review after quick checks, before parent-launched long
integration tests. Risk HIGH: native protocol, owned execution/cleanup, additive
cross-project interface and deployment ordering. Eligible retained reviewer0 uses
saved gpt-6.1-sol/xhigh/read_only, no override or fallback. Apply all four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review/SKILL.md and each lane reference in full. Perform
review directly without nested agents. No source edits, CI reruns, live runtime
calls, activation or lifecycle actions.

The complete final inventory is final-inventory.json, with final diffs and
history files alongside it. Require its exact heads and clean source status before
starting. Inspect complete base-to-head history, final diffs, authored vs inherited
workspace ancestors, superseded approaches, repeated pin streams, supported state
boundaries and explicit migration conclusions. Mechanical pin-content exemptions
do not exempt whole-branch history. Give explicit obsolete-history, pin-stream
and migration conclusions; state no migrations where applicable.

## History and provenance

A should have one focused functional commit including tests/docs/native fixtures.
B should have one generated dependency commit FIRST, then one owning functional
commit with tests/docs/packaged fixtures. Workspace and configuration should each
have one final runtime update. Config messages remain generated, including their
changelog and allowed long revision lines. Preserve inherited shared-master
coordination commits; they are not this feature's fixup/pin iterations.

Pre-review intermediate A b81f8058/ee119a01 and B268f2e87/d9ea3925 were development
publications only, never merged/released/deployed. A was consumed by this same
initiative's provisional B pins; no known supported external consumer or state
boundary requires the old refs. Obsolete C pin commits were unpublished and
regenerated/amended from the proper predecessor. Final inventory must confirm
all source fixups and repeated update streams have been consolidated. No migrations
or deployed feature lineage exist for this initiative before the planned rollout.

## Verification evidence and pending gates

Read package-a.md, package-b-handoff.md, package-c.md and their exact commands/
heads for final quick evidence. A focused unit, generated-native schema corpus,
fixture compilation and targeted fixture-contract checks passed. B focused Go,
syntax/format/fixture payload and overlay compile-only checks passed; preliminary
local replacement checks were superseded by final no-replacement checks. C lock
composition, formatting/hooks and cross-project deployment-contract checks must
bind final heads in its report. Main-agent English writing pass accepted A reference
and B preparation/portal/package prose; no product UI labels changed.

Important old CI failure: provisional B268 Check39810261469 passed fast/archive
but native-progress creation failed after512ms. See package-b-provisional-ci-failed.log
and design.md's source-backed diagnosis. Native ServerOverloaded without structured
retry advice is terminal; retry ceilings alone do not make progress. Both A/B
fixtures now add response.error.headers={"retry-after":"1"} ONLY for native progress;
terminal/fresh/persistent cases omit advice. Test-only retry ceilings remain in
disposable launchers. Product provider/model/catalog/isolation policy is unchanged.
Inferred two-terminal-call exhaustion is consistent with the failure but exact old
RPC/request counts were unavailable. New compact response-mode/count diagnostics
must remain synthetic and secret-free. Review the corrected fixtures as well as
production code; queued CI is not a passed check.

After findings are resolved, a fresh retained-policy Luna/low watcher will run
verify-native.sh (owned namespace fixture before protocol fixture), packaged
session-creation and applicable flake/CI checks. These parent-controlled long
checks have not run yet; automatic branch CI may run independently.

## Documentation and rollout

A owning contract: docs/reference.md. B owning contracts:
docs/session-preparations.md, docs/workspace-portal.md, docs/codex-package.md.
Current configuration local guidance is docs/operations/codex-providers-aitherdev.md;
its old workspace-coordination-aitherdev.md was deliberately removed at c1057731.
Use the selected installed coordination/operations guides and workspace deployment
procedure; do not restore obsolete site guidance.

Build final committed system/application artifacts before machine ownership when
supported. Acquire vpsfree:aitherdev, dry-activate/switch system without reboot,
verify live system/profile, then switch the composed application with exact
session/claim identity. Preserve active conversations/guest processes and current
native/catalog/extension inputs. Keep forward-recovery artifacts and claims under
selected runtime retention policy; deployment never grants merge approval.

Session-only package-b-live-naming-smoke.md and companion discovery/overlay files
prepare a real selected-provider call through the deployed private child. They
create no registered session and require no lifecycle cleanup. They have only
been compile/syntax checked, not executed. Review their proposed operational
boundary if relevant; they are verification evidence, not a product API.

Report findings by severity and lane, with exact paths/commits. Blocking and
Important findings need concrete current-contract evidence. If clear, state no
findings and list remaining native/VM/live-provider/CI gaps. Do not claim deployment
or readiness from code inspection alone.

## Final coverage qualification

Read package-b-coverage-inventory.md. Existing tests exercise portal admission
under a shared generation lock, real collector sweep exclusion of preparation/
candidate grants, and generation-change refusal. These lie outside the naming-only
quick selector and await normal package Go/Ruby checks. There is no existing single
fixture submitting real portal creation during an actual paused collector sweep.
Do not claim combined end-to-end concurrency from the creation VM alone. Lead is
arranging a minimal disposable post-review verification probe for that acceptance
item; no product code is being edited for it during this review. Assess this
explicit gap and the unchanged lock boundary under the risk/scope lanes.
