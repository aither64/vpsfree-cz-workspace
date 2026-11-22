# Root a candidate package before a long workspace switch

Initiative: `work/2026-09-26-codex-queue-ledger-capacity/`.

`workspace-host switch --source <workspace worktree>` built its candidate with
`nix build --no-link --print-out-paths`, then spent over a minute on preflight
and session transition. At `nix-env --profile ... --set <candidate>`, Nix said
the candidate path was unavailable. The path had existed when the switch used
`File.realpath`; it was absent from the store immediately after failure.
Garbage collection of the unrooted output during the interval is the likely
cause, though no GC event log was captured.

The old user profile and portal stayed active, but the failed switch had
stopped/disabled the workspace auto-archive timer. Restore the timer if a
retry is not immediate. For the successful retry, build the exact workspace
package first and hold it with a temporary out-link:

```sh
nix build .#default --out-link /tmp/<task-specific-link> --print-out-paths
workspace-host switch --source <absolute-worktree-path>
```

Verify the selected profile points to that output, the portal and timer are
active, then remove only the task-specific link. Do not roll back a package
that may have written state above an older binary's format limit. The durable
runtime improvement would be to have `workspace-host switch` root its own
candidate through preflight and release that temporary root after profile
selection or restoration.
