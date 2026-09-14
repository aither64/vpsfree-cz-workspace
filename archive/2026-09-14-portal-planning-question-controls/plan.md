# Hide the composer while answering Codex questions

## Goal and accepted behavior

Implement the user-approved plan from the investigation: every answerable question
replaces the standard prompt and controls in Plan and Default modes, including
asynchronous questions. Keep one compact Interrupt button in the first question
header. The user authorized implementation and deployment to aitherdev, with
feature branches and the session initially left open and unmerged. The user
subsequently authorized default-branch integration and cleanup.

Priority: answerable questions, then eligible completed-plan decisions, then the
ordinary composer. Restore the composer after the last question disappears unless
a completed plan takes precedence. Leave approvals, terminal-only requests and
unanswerable/error cards with ordinary controls available. Preserve prompt and
answer drafts, uploads, focus, validation, automatic resolution and snooze.

## Affected repositories and approach

- dev-workspace: host-owned composer visibility, question header/Interrupt layout,
  responsive styles and focused browser regression.
- vpsfree-dev-workspace: pin the committed/pushed runtime revision.
- workspace: pin the committed/pushed extension revision in a dedicated feature
  worktree, preserving site configuration and installed extensions.
- codex-web: inspected shared provider, unchanged source and input pin.

One private view controller owns visibility for both plan and pending rendering.
Retain the composer DOM and move its existing Interrupt element. Restore focus
from removed questions without stealing focus from transcript reading; account
for disabled controls losing focus while a response is in flight. Remove the
obsolete short-window compaction rule; preserve scrollable question content and
fixed wizard actions.

## Compatibility

Browser presentation only. No persisted-state/on-disk format, database/schema,
API/client/CLI/Terraform contract, protocol/message, NixOS option or runtime
identity changes. No coordinated node or machine update and no migration.
Old/new browser assets remain usable because the unchanged template and existing
hidden-attribute CSS support the new behavior. New headers only require cosmetic
CSS; old JavaScript retains preceding behavior with the new CSS. Static assets
already use no-store. Existing state remains readable on rollback.

## Verification and review

Use Nix tooling for JavaScript syntax and focused Go/API checks. The committed
opt-in Playwright regression uses the actual template, CSP, assets, event stream
and upload service with controlled thread/pending responses. Cover question
arrival/refresh/removal, failure/reconnection, multiple asynchronous questions,
drafts/focus/attachments, Interrupt, completed plans, desktop/short/mobile layout
and a viewport equivalent to 200% zoom.

After all changes and pins are committed and quick checks pass, run the required
adaptive review with gpt-5.6-sol at xhigh. Resolve required findings before long
integration checks. Run packaged Nix checks, inspect feature CI, then verify the
assembled package and deployed asset hashes plus browser behavior.

## Deployment and handoff

Deploy the composed site package through the installed stable command:
`workspace-host switch --source <initiative workspace worktree>`.
No vpsfree-cz-configuration edit or NixOS deployment is required. Preserve the
previous profile for rollback and honor lifecycle/generation/concurrent-session
checks without forcing interruptions. Keep unrelated dependency pins unchanged.
Record exact feature heads, package/profile generation, tests and live health.

The user now authorized default-branch integration and cleanup. Capture exact
comparisons, fast-forward the reviewed heads to default branches, verify CI, and
archive through dev-session. Retain branch refs and useful evidence; remove clean
worktrees and transient build logs. Preserve unrelated shared-checkout changes.
