# Unexecuted no-build discovery check

This query imports the actual committed candidate catalog and native test
modules. It projects only names and test/script tags; it does not realize a
JSON derivation or evaluate machine resources. Run only after the lead selects
a fresh watcher and freezes the exact committed candidate source. The new file
must be tracked at that head. Record HEAD, source NAR/hash, flake.lock hash and
input graph. A dirty checkout or a changed source head invalidates the selection.

Use the existing Nix client in the repository environment. The proposed native
query is:

```sh
nix-instantiate --eval --strict --json \
  --option allow-import-from-derivation false \
  --option builders '' --option fallback false \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/production-discovery.nix \
  --argstr source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-production-commit
```

Prefix every invocation with this exact environment cleanup:

```sh
env -u VPSADMINOS_ENABLE_LIVEPATCH_TEST \
  -u VPSADMINOS_ONLY_LIVEPATCH_TEST \
  -u VPSADMINOS_LIVEPATCH_SINGLE_SERIES_MODULE \
  -u VPSADMINOS_ENABLE_SCHED_PROXY_EXEC_TEST \
  -u VPSADMINOS_ONLY_SCHED_PROXY_EXEC_TEST \
  -u VPSADMINOS_ENABLE_SCHED_PROXY_EXEC_LOCK_BADNEIGHBOR_TEST \
  -u VPSADMINOS_ONLY_SCHED_PROXY_EXEC_LOCK_BADNEIGHBOR_TEST \
  -u VPSADMINOS_ENABLE_HISTORICAL_UPGRADE_TESTS \
  -u VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS \
  -u VPSADMINOS_CONFIG \
  timeout --signal=INT 90s nix-instantiate ...
```

Replace the final `nix-instantiate ...` with the exact native command above.
For each opt-in invocation, put its single literal `NAME=1` before `timeout`.
The fresh watcher redirects each result to its own receipt files and checks
that each client ended before launching the next.
The first invocation has both upgrade gates unset. The second adds only
VPSADMINOS_ENABLE_HISTORICAL_UPGRADE_TESTS=1. The third adds only
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1. No other opt-in or ONLY selector is set.
Retain each stdout JSON and stderr separately with exact exit/time and hashes.

Compare the JSON using the catalog's 23 preserved names in
production-source-restore.json: default names contain none of them and contain
exactly production-impermanence@v1/@v2 as the production instances; historical
opt-in adds exactly those 23 and leaves diagnostic names absent. Each historical
script's combined test+script tags must be upgrade/manual without ci. Production
scripts must include upgrade/ci in all three results. The diagnostic opt-in adds
exactly the two existing diagnostic names, leaves historical names absent and
has no ci script. Feed each combined-tag object to the actual candidate
TestRunner::Cli::TagFilters.new(['ci']).pass? method from
test-runner/lib/test-runner/cli/tag_filters.rb; every historical and diagnostic
script must be rejected, each production script accepted. This tests the native
selector, rather than treating the static source check as discovery proof.

Watcher limits proposed for separate selection: 300 seconds total, one Nix
client at a time, 16 MiB stdout + 4 MiB stderr aggregate retained output,
2 GiB physical source/evaluation growth ceiling and 40 GiB free floor. Sample
resources during each command; preserve effects on cancellation and stop before
any unexpected realization/kernel build. IFD is disabled and builders empty;
source/input fetches and evaluation may still occur. Any IFD request, changed
inputs, output/growth bound or timeout is a failed preparation, not permission
to realize, change the query or retry. No build, VM, image download, native
runner build, source change or Git mutation is selected by this proposal.

Actual machine RAM/SHM/CPU/all disks/cache/closure forecasts remain a separate
metadata admission; these tag-only projections cannot establish VM readiness.
