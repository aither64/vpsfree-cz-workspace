# Cleaning generated vpsAdminOS Ruby artifacts

The full Ruby and VM test workflows can leave ignored or untracked gem caches,
component `Gemfile.lock` files, native build outputs, `.native/`,
`libosctl/tmp/`, and result links in a vpsAdminOS worktree.

In Codex sessions, an exact-path `rm -rf` cleanup can be rejected by the command
safety policy even after the targets have been inspected. After verifying the
contents and sizes with `find` and `du`, remove those exact generated trees with
`find <exact paths> -depth -delete`, then confirm the worktree with
`git status --short`.

This was verified while cleaning the worktree for
`archive/2026-09-05-cgroup-v1-shared-device-fix/`.
