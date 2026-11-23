# 2026-11-23-kernel-retention-policy

## Goal

I'd like to establish rules for vpsadminos kernel retention in the vpsadminos repo. You can of course make suggestions, but I imagine it this way:

- each kernel has a date added field
- optionally, it can have a field specifying for how long / until what date it should be kept
- we'll have a way to check if the kernels are in use, this will be done specifically against vpsfree.cz cluster at vpsadmin.vpsfree.cz (api.vpsfree.cz) -- kernels that are currently used by nodes are not eligible for removal
- kernels that are older (use 30 days by default) and unused and are not the default atm can be removed
- all this should be covered by deterministic tools, so that we can run it e.g. in a github workflow to prune the old kernels weekly
- we should have a check so that the kernels have the necessary metadata, otherwise refuse to commit
- existing kernels will have their metadat aset retroactively, use time of the commit that introduced them -- this is a one time operation and you can handle that yourself

Suggest a solution.

## Affected repositories

- `vpsadminos`: proposed metadata, validation, pruning tools and workflow.
- `vpsadmin`: existing public node status contract, consulted as a reference; no API change proposed.

## Approach

Keep retention alongside the catalog. Separate collection of live usage from a deterministic decision over an explicit date, repository tree and usage snapshot. Backfill metadata from Git history before enforcing it.

Repository references are not retention exemptions. Move reusable tests to the stable default; explicitly associate truly version-specific tests and livepatches with their kernel so a single cleanup commit removes them together. The weekly workflow must commit directly to `vpsadminos:staging` once enabled; no PRs. Verify the candidate and recheck live usage and the target staging tip before an ordinary non-force push.

## Implementation order

1. Backfill catalog dates from the introducing commits and validate the whole catalog offline. Add a dedicated kernel-entry correctness workflow on PRs targeting `staging`; validate the candidate merge tree with the same checker as Overcommit. Require its status in GitHub once the workflow is installed and tested, so a missing or invalid entry blocks merging. Verify the rules also allow the separately validated direct maintenance path.
2. Update vpsAdminOS test-authoring instructions: follow the stable selector by default rather than pinning a version. Livepatch tests may pin the release they exercise. Other pins require a documented reason the test cannot follow stable. Checklist and examples should distinguish actual pins from synthetic versions or immutable historical fixtures. Convert existing reusable tests; give truly release-specific tests explicit lifecycle ownership, including their registrations and fixtures, so they are cleaned up with the kernel. Make livepatch data removable by kernel key.
3. Implement deterministic planning and transactional cleanup. The live collector is separate. A blocked or empty plan cannot write; a nonempty plan removes only eligible entries and their owned companions, and validates the resulting tree.
4. Add the weekly GitHub Actions job. Validate the exact candidate from `staging`, fetch fresh usage, and publish one fast-forward commit only if the same cleanup is still valid and the remote tip has not moved. No PR, force push, or automatic rebase. Exercise report-only and disposable-remote scenarios before enabling production writes.

See `design.md` for the implementation packages, interfaces and acceptance checks.

## Compatibility and deployment

Treat this as a repository maintenance change; no coordinated node update or vpsAdmin API deployment. Verify that metadata-only changes leave selected kernel and ZFS derivations unchanged. Reconcile API coverage with production inventory, test the direct-push credential and staging branch rules safely, and verify the cleanup fixture before enabling writes. Retention is about running kernels, not future boots; coordinate with ops at activation or during a rollout that could race pruning. Recover a pruned entry and its companion files together by reverting the cleanup commit or restoring the exact affected paths and adding a hold if needed.

## Documentation

Extend the existing vpsAdminOS kernel update guide with the metadata, checks, pruning and recovery procedures. Update the existing test-authoring instructions and contributor guidance to explain the stable-selector default, justified exceptions, and cleanup ownership. No project documentation is changed in the planning phase.

## Testing plan

Use Git fixtures for the backfill and staged-index checks for the commit hook. Test PR candidates with missing, invalid, and valid metadata and verify the GitHub rule actually blocks failing PRs. Exercise a stable-selector change to show reusable tests follow it; verify release-specific tests disappear only with their owning release. Use fixed dates and synthetic node snapshots for retention and failure cases. Evaluate Nix selectors and derivations without building kernels. Production rollout starts with a read-only coverage check.
