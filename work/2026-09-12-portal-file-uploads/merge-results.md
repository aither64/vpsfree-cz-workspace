# Merge and cleanup

All five repositories were fast-forwarded into remote master. All feature branch
refs are retained, and all nine feature/temporary worktrees and configuration
bundle/build caches were removed with non-force git worktree remove.

- codex-web: ee9ab42791a84b79315d952501264a6cbafc8695
- dev-workspace: 8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f
- vpsfree-dev-workspace: 37f3bfa21079b217aef15a4c2e75ed7451b9d156
- workspace: 0dbe3990e3d3716c1da25a37f72e7f2040eaa499
- vpsfree-cz-configuration: b0252827958a4cc231a2a0bb56ae3a1844db8ae8

Configuration was rebased onto upstream's two dependency updates; all six patch
comparisons remained identical. Its aitherdev build passed at generation
2026-09-13--16-11-38. Provider/runtime/organization flake checks passed in fresh
target worktrees, including runtime host-module VM tests. Workspace deployment
pin/hostname checks passed. Provider/runtime master CI passed; organization master
CI was still running at the last check. The user requested that we finish
without waiting; the remote workflow remains running independently.

The already deployed application remains unchanged. Uploaded files in private
workspace state were retained. Unused/incomplete uploads expire after seven days
of inactivity; the collector runs at startup and hourly. Files referenced by
sent/queued prompts have no time-based expiry. Explicit removal or deletion of
the owning session removes them; session archival and worktree cleanup retain
them. Storage root on aitherdev:
/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads.

Tracking and the conversation remain available; no archive/delete was requested.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-file-uploads/
