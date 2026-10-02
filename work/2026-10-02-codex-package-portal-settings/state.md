---
lifecycle: active
---

# Codex package and portal settings state

Phase: initiative setup. Implementation and deployment are authorized; default
branch integration is not authorized.

## Phase checklist

- [x] Diagnose installed 0.159.2 and missing package manifest/runtime files.
- [x] Confirm complete-package startup and desktop/mobile layout preferences.
- [x] Identify exact upstream issue and pending package PRs.
- [ ] Create initiative and assign retained design/implementation members.
- [ ] Commit initial plan/state and create dedicated feature worktrees.
- [ ] Record design and implement packaging, UI, pins and documentation.
- [ ] Complete quick verification and independent whole-branch review.
- [ ] Complete packaged/browser/live checks and aitherdev build.
- [ ] Deploy system and user-profile application; verify live behavior.
- [ ] Ready for use, awaiting explicit default-branch integration direction.

## Authorization and boundaries

User request: "Implement the plan." The accepted plan includes aitherdev system
deployment through vpsfree-cz-configuration and separate user-profile workspace
deployment. Preserve other initiatives and unrelated shared checkout changes.
No session was bound to this conversation at the start: environment identity
was absent and dev-session current returned "no current dev session found".
Create a separate dated initiative rather than adopting another session.

## Initial evidence

- Hostname aitherdev; system Codex and workspace-private Codex both 0.159.2.
- Upstream llm-agents.nix 0.160.0 revision:
  6334544a4bfd921086a252caccc6c1c6eb1d18c7.
- Existing installed package lacks codex-package.json and bundled rg and uses
  an escaping bwrap symlink. The same recipe remains in upstream main.
- Main, queue and thread-history SQL migration file hashes are unchanged
  between Codex 0.159.2 and 0.160.0.
- Upstream packaging issue #9887 and PRs #9889/#10132 are open and unmerged.
- No implementation, service changes or deployments yet.

## Next action

Commit these initial records, initialize the delegated session, inspect its
saved roster/access and assign design. Register dedicated project worktrees.
