# Completed: client documentation and CI fixes

Merged into HaveAPI/master at029f79b31cec93167f07e43e571c36b5f42d5b80. Fresh SSH proof confirms the CI-fix feature at the same head and the retained documentation headcb43ae2367b12e22e602d69312bfd1f7331b4995 as its literal ancestor. Required hooks passed; merge claim7d22c7b0-2bbb-4195-964e-ae3e6f1c0935 is released, revision3.

The large performance-env attempt was rejected and removed. The accepted fix uses a standard benchmark Gemfile/lock and small Nix shell, with exact push before/after comparisons and a documented new-branch fallback. Ruff versions are aligned and guarded against future drift. Final review and its focused correction are complete.

All11 final-head checks passed. Performance tested the actual08355a22..029f79b3 push:14/14cases and28/28 timing comparisons pass, exact87-gem runtime. The manually dispatched release workflow only tested/built packages; nothing was released or published. See [state](state.md), [review](simplified-final-review.md) and [packet](review-ci-fixes.md); raw evidence is under artifacts/minimal-final-ci/.

No remaining work, watcher, command effects, claims or deployment. Session remains open, with refs/worktrees retained; no lifecycle cleanup authorized or performed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-client-readme-improvements/)
