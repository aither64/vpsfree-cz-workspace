# Nix temporary roots and GitHub runner GC

Related initiative: `work/2026-08-03-gh-runner-gc`

## Symptom

`nix-store --gc --print-roots` can report thousands of roots such as
`"{temp:PID}" -> /nix/store/...` during a large evaluation or build. A sampled
PID may be gone by the time it is checked.

## Cause and interpretation

Nix 2.34 keeps NUL-separated store paths in per-process files under
`/nix/var/nix/temproots`. The owner holds an exclusive `flock`. Root discovery
tries to take that lock without blocking; if it succeeds, Nix removes the stale
file and ignores its contents. If it fails, the owner was live at discovery
time and the paths are valid temporary roots.

A later root listing with no temporary roots confirms that the owning operation
ended normally. Do not delete temporary-root files manually.

## Runner-specific findings

Plain `nix-collect-garbage` does not delete old profile generations. On the
vpsadminos.org runners this allowed many complete NixOS system generations to
remain rooted. Use an explicit retention policy such as
`--delete-older-than 14d` when that rollback window is accepted.

The reported `root/channels-1-link` is a separate current profile generation,
so age-based generation pruning will retain it. The current configuration and
vpsAdminOS workflows use flakes; check `nix-channel --list` and remove the
legacy channel only after confirming no operator workflow still uses it.

vpsAdminOS CI builds create `os/result/toplevel`. Because the self-hosted runner
workspace persists under `/run/github-runner/runner`, the latest completed job
can keep a full system closure rooted between jobs. Remove completed-job output
links before the boundary GC, or add an `if: always()` cleanup step in every
relevant workflow.

The runner GC timer is intentionally deferred during workflow jobs. Busy
runners can therefore starve timer-driven GC. Prefer a synchronous conditional
GC at the completed-job boundary, after output-link cleanup, while retaining
the root timer as a fallback and for old root/system profile pruning. Ordinary
liveness-respecting collection can be requested by the unprivileged runner via
the Nix daemon, so the completion hook does not need sudo. Size the free-space
reserve for the largest observed live job; live temporary roots cannot be
safely reclaimed.
