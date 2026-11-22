# Retain the Playwright package while preparing browser checks

During `work/2026-09-14-auto-archive`, a Playwright package fetched in an earlier
`nix shell` was no longer present by the time the browser script ran. Node was
still available, but `require('@playwright/test')` failed because the recorded
package path and its browser closure had disappeared. Nix had no durable GC
root for that shell-only dependency.

Build `nixpkgs#playwright-test` with `nix build --inputs-from <worktree>
--out-link <initiative>/playwright-tools`, then use the NODE_PATH and
PLAYWRIGHT_BROWSERS_PATH values from that package's `bin/playwright` wrapper.
The wrapper also identifies the matching Node executable. Keep the output link
until the browser check completes; remove it during transient cleanup.
Refetching with the root restored the package and matching browser closure.
