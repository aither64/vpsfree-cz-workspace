---
lifecycle: active
---

# Portal mode refresh

Phase: implementation setup. No merge direction has been given.

- [x] Investigation and approved implementation plan.
- [ ] Implementation and quick checks.
- [ ] Independent final branch review.
- [ ] Packaged/browser checks and published-head CI.
- [ ] aitherdev deployment and live verification.
- [ ] Explicitly approved integration, if requested.

`dev-session current` found no current session and neither environment identity
variable is set. This conversation creates its own initiative rather than reusing
another session. Initial plan/state committed before session or project mutation.
The lead owns this bounded implementation and design; no specialist edits are
needed. Independent review and verification watchers use installed catalog policy.

Root cause: `renderThread` clears `currentMode` when rollout metadata expires and
immediately replaces the controls with an unmanaged Checking mode notice. The
shared notice helper already provides retention and visibility-sensitive delays.

Next: create/register owned worktrees and implement the accepted behavior.
