# Retain browser tooling during acceptance

Workflow: repository browser acceptance using Nix Chromium, playwright-driver and
review-ui assets. Reusing raw store paths from a previous handoff failed at launch
because garbage collection had removed those paths, including editor build assets.

Restore tools from the repository's pinned nixpkgs with `nix build --inputs-from .`
and task-owned outlinks. Build review-ui.nix with that same input when its bundle
is absent. Use the outlinks for the module, executable and asset directory during
acceptance, and remove them after final verification. The installed portal embeds
its assets; retaining its package does not retain every separate build output.

Verification: restored tooling passed all 23 compact-layout component checks.
Initiative: work/2026-09-12-portal-review-experience/compact-plan.md.
