# Question composer change review

## Requested outcome and decisions

User approved the complete plan in plan.md: every answerable question replaces
normal prompt/settings controls in both Plan and Default modes, including async
questions. Keep exactly one Interrupt button in the first question header.
Questions take priority over completed-plan decisions, which take priority over
the composer. Preserve drafts/uploads/focus and answer semantics. Approvals,
terminal-only requests and errors without an answerable wizard retain controls.
Deploy the assembled package to aitherdev; do not merge/archive or interrupt
unrelated sessions. The user explicitly selected all questions and the header
Interrupt location.

## Scope and committed revisions

Initiative: 2026-09-14-portal-planning-question-controls. Tracking root:
/home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-portal-planning-question-controls

- dev-workspace: base `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a`, head `df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-planning-question-controls/dev-workspace`.
- vpsfree-dev-workspace: base `916223fce1c5b7b78578ca8a16aaaa472c68b08c`, head `89a03581b13056fa83114e592f2e2993e6a87887`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-planning-question-controls/vpsfree-dev-workspace`.
- workspace: base `f523eddf3e1d1cdebf445992318247030e11c7f3`, head `1e01e557cac5527666d5b1e35fa52fadcdbb81af`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-planning-question-controls/workspace`.

Each repository has one feature commit: generic behavior plus its regression;
organization runtime pin; site extension pin. Tests and focus remediation are
inseparable support for the requested behavior. Pin updates are separate commits
in their owning repositories. All worktrees are clean.

## Ownership and consumers

The host portal owns its question wizard and standard form. The shared codex-web
provider remains at 6335da93acdcc82cc26200d2fbc7f479655aa7c3; no provider source,
public Go/HTTP/browser API, validation or request protocol changes. The runtime is
consumed by vpsfree-dev-workspace via its dev-workspace flake input/mkPackage, and
the site workspace consumes that extension through its own mkPackage/siteConfig.
The two downstream commits change only those pins. SiteConfig, extensions, all
unrelated providers, Nixpkgs and Codex package inputs are retained.

## Implementation boundary

A private createComposerView owns form/plan visibility and the Interrupt element.
It derives answerable questions from rendered wizard cards, retains DOM for the
composer, transfers focus from hidden or removed controls, and preserves focus
identity/selection across changed pending snapshots. Respond restores focus lost
by disabling an answer control when the user has not focused elsewhere. Wizard
answer encoding and automatic-resolution/snooze behavior are unchanged.

No redesign of question pagination, permissions, queues, session lifecycle,
connection recovery, upload transport, model settings or authorization. No new
user-facing prose. Avoid fixes for unrelated existing optional-note semantics:
under the current wizard, an option must be selected for its note to encode as an
answer. Browser tests select an option before its note. Existing question geometry
cap and fixed action layout remain.

## Quick verification

- Nix development environment: focused Go tests for shipped browser API, session
  rendering and plan decisions/implementation passed after the final change.
- node --check passed for app.js and question_browser_test.cjs; git diff --check
  passed. No declared hook framework or executable custom hooks were present.
- Actual Chromium/Playwright regression passed (22.07 seconds), using real portal
  template/CSP/assets, real TLS/SSE/upload handlers and controlled thread/pending
  API responses. Covers blocking/async questions, repeated snapshots, multiple
  questions, response failure, disconnected snapshots, focus/selection and prompt
  drafts, in-progress uploads, Interrupt, nonquestion/error requests, completed
  plans, and 1440x1000, 1280x720, 1280x540, 390x844, 640x360 viewports. Last viewport
  represents the CSS layout available at 200% zoom on a 1280x720 display.
- Browser evidence: browser-results.json and browser-verification.log. The test
  is committed as opt-in PORTAL_BROWSER_TEST=1 so standard Go checks do not gain
  a mandatory Chromium dependency. This run used matching Nix-packaged Node,
  Playwright and browser outputs; no browser download.
- Organization and site nix flake check --no-build passed; only expected pin
  nodes changed. See implementation-revisions.json for exact heads.
- Feature pushes required for immutable downstream Nix pins automatically started
  existing CI. Local long packaged/integration checks and deployment have not
  started; they wait for review reconciliation.

## Risk, compatibility and deployment

Overall high conservatively because this includes a live package deployment and
browser asset compatibility verification; there is no new security/state risk.
Select general, architecture, scope and risk lanes. Use gpt-5.6-sol at xhigh in
fresh standalone reviewers, no nested delegation.

The local workspace operator is trusted. Remote clients remain untrusted; origin,
request validation, identity and upload protections are untouched. No persistent
state/schema/protocol migration, host contract or NixOS module change. No node
coordination required. The existing template/hidden CSS supports the new script;
new CSS affects header presentation. Static portal assets already have no-store.
Existing state remains readable by the prior package.

Deploy the composed site package through installed workspace-host switch --source
<site initiative worktree>, retaining the previous profile. No system
configuration repository change is needed or authorized merely for this UI fix.
Honor package/lifecycle/concurrent-session preflights; never force interruptions.
Verify deployed assets, health and browser behavior and retain branches/session.

## Reviewer task

Read the mandatory-change-review skill and your assigned lane reference. Review
these exact committed ranges, repository rules, plan and evidence. Perform your
own review without subagents. Write findings to the assigned review file and send
back a concise result, with severity, source locations, rationale, and residual
test gaps. Do not edit source or other sessions' records.
