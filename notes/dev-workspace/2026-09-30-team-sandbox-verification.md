# Team-member sandbox verification limits

During `2026-09-30-portal-review-improvements`, a workspace-write team member
could edit the `dev-workspace` feature worktree but could not enter `nix develop`:
the default Nix fetcher cache was outside its writable paths, and a task-local
`XDG_CACHE_HOME` then reached a Nix daemon operation denied by the sandbox.
Go tests that open HTTP or Unix sockets also failed under the member's network
restriction. These failures did not establish an application defect.

The member ran socket-free focused checks with the installed Nix-profile Go,
direct Nix-store Node and installed Ruby, using a task-local Go cache under
`/tmp`. The lead entered the repository's Nix shell and runs socket-based
checks from the lead environment. Keep source edits delegated to the verified
workspace-write member; use the lead environment for checks that need the Nix
daemon or loopback sockets.

The shell sets `GOFLAGS=-mod=vendor`, but the source worktree has no `portal/vendor`
directory. For a focused source check, override it with `GOFLAGS=-mod=mod`.
The lead verified this with `go test ./internal/web -run
TestShippedBrowserClientMatchesSessionAPI -count=1` under `nix develop`; it
passed after the override.

Related initiative: `work/2026-09-30-portal-review-improvements/`.
