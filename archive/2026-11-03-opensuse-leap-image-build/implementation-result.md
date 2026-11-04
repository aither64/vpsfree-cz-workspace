# Implementer0 Milestone 1 result

Source package committed and published for independent final review. Long
regression has not run on this final series. Device-unit root-cause/fix work
is separate Milestone 2, owned by implementer1; its test source is unchanged.
No merge, deployment or production image publication occurred.

## Exact source and final series

- Repository/target: `vpsfreecz/vpsadminos`, `origin/staging`.
- Branch: `2026-11-03-opensuse-leap-image-build`.
- Worktree: `worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`.
- Base: `dd188397abe37d0bc33f4c5dfb3605206ce5e326` (fresh target unchanged).
- Commit 1: `4c2a38bc02d1d10c208d478c01ec90057995825e`,
  `image-scripts: use Leap 16.0 for Leap builds`.
- Commit 2/final head: `57871a8e3f8f429e86e3ad6abf16de99a44e9416`,
  `image-scripts: add opensuse-leap-16.1`.
- Final tree: `7e88b628393dfd7771800d23a7bc423ef23b109e`.
- Full diff: five files, 23 insertions and 2 deletions. No WIP/fixup or
  dedicated-builder commits remain in the final series.

Commit 1 only changes `builders/opensuse-leap/config.sh` from leap-15.5 to
explicit leap-16.0. Existing no-op setup remains. Commit 2 adds the 16.1 image
build/config, repository registration/tag move and explicit distro matrix entry.
The new image uses `BUILDER=opensuse-leap`; the session-added dedicated builder
is absent. Existing image definitions, shared helper, lockfiles and device-unit
test are unchanged. Native config parsing confirms exactly three consumers:
15.6, 16.0 and 16.1, each targeting its own Leap release.

## Quick checks and publication

- Shell parsing passed for shared builder config/setup and new image build/config.
- Both changed Nix files parsed; whitespace check passed.
- Native config parser resolved shared builder `opensuse/leap-16.0` and each
  image `opensuse/leap-15.6`, `leap-16.0`, `leap-16.1`, x86_64.
- Consumer search found exactly those three, with no dedicated builder reference.
- Both commits used temporary message files and active repository Nix/Overcommit
  hooks. Nixfmt and commit-message hooks passed without warnings. Prior full
  Ruby lint passed; Ruby source/config is unchanged.
- Earlier native discovery proved the same new 16.1 image/matrix names; runtime
  template/discovery code is unchanged. If listing is required for the new
  three-image selector, the lead delegates the uncertain-duration native listing.
- A raw `git restore` completed owned file restoration but its post-checkout hook
  refused outside the Nix environment; effects were inspected before proceeding.
  No duplicate restore or hook bypass; all final commits/push used repository Nix.
- Fresh fetch before publication confirmed target still at the recorded base.
  SSH force-with-lease explicitly required old AA head; remote `ls-remote`
  verified final head `57871a8e3f8f429e86e3ad6abf16de99a44e9416`.
- Worktree clean and attached to the feature branch. No repository claim was
  needed for independent feature work; no default branch was changed.
- Superseded AA runs `41690940390` and `41690940549` are confirmed
  completed/cancelled. Final-head runs `41705503484` and `41705503560` were
  left untouched (queued at the last cancellation reconciliation).

## Historical lineage and compatibility

The previously tested dedicated-builder range was
`dd188397abe37d0bc33f4c5dfb3605206ce5e326..aa963dce42859ae4251cdfaded91920d67b3a46e`.
The final range is the same base through `57871a8e3f8f429e86e3ad6abf16de99a44e9416`.
`git range-diff` shows a new separate shared-builder commit and the new-image
commit with obsolete dedicated files removed and its reference corrected.
AA-to-final diff is four paths, 2 insertions and 5 deletions. This is substantive
scope change, not an equivalence certificate or final runtime validation.

Stable patch IDs: builder commit `b64d96addb1fa3f6344db4b2a6d08d1afe34ec92`;
new-image commit `dc1ebce3445cca71f54e16c869dd4af154d42501` (the original
new-image patch). The complete series still needs whole-history review.

Retained backup refs under `refs/backup/2026-11-03-opensuse-leap-image-build/`:
`reviewed-f0e1656`, `failed-leap-builder-fe9182d`, and
`tested-dedicated-aa963dce4`. Original review/failed/tested records and native
logs remain intact. [Historical implementation summary](implementation-result-aa963dce4.md)
retains previous exact ranges, input graphs and results.

No migrations, API/protocol changes, persistent host-state format changes or
configuration/dependency pins. The builder-release update stream is consolidated
in one logical commit. Shared existing 15.6/16.0 build environments intentionally
change; existing containers/published images do not. No coordinated fleet upgrade.
Builder IDs hash the name only and reuse ignores release, so tests require fresh
state. Later authorized operations must recreate the exact idle managed builder;
rollback has the same cache caveat. See the accepted [design](design.md).

## Evidence retained and remaining work

AA's primary 16.1 image run passed 15/15; its 8 GiB export identified Leap 16.0 /
RPM 4.20.1. Those are superseded supporting evidence, not final shared-builder
regression. [Extraction receipt](candidate-extract-recovery-result.md) binds
builder stream `d279c082fb997e17996af6fe00f8b54d23a847247c2498090a24b3f26538dbe2`,
candidate `254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`
and repo tar `36069c59b286fdeb81988e87482b519bb8fcea62a916e0a1d0eaac819e0c57d3`.
No claim that the old boot lockup's exact cause was fixed.

The [partial matrix](candidate-matrix-result.md) ran only old-candidate start-stop
(pass) and device units (loaded/inactive eth0, status 3, then polling timeout).
Both cases' PTY/shell/console snapshots are `aa963dce4-{start-stop,device-units}-*.log`.
[Device diagnosis](device-unit-diagnosis.md) preserves raw observations/hashes;
its suggested expected-failure extension is withdrawn. No such edit was made.

After committed-series review, a fresh lead-owned watcher should list/run the
three image tests using the separate exact-head modules:
`shared-leap-revision-57871a8e3.nix` and
`shared-leap-verification-57871a8e3.nix` (the latter forces only 8192 MiB RAM).
Both parse; AA revision/export/input files are unchanged historical artifacts.

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/shared-leap-verification-57871a8e3.nix ./test-runner.sh test --jobs 2 --stop-on-failure --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-shared-leap 'image-scripts/test@opensuse-leap-{15.6,16.0,16.1}'
```

This new state must not reuse the old name-keyed 15.5 builder. Check current RAM
and shared memory; two guests require 16 GiB each in those budgets and 8 vCPUs,
plus reserves. Lower jobs to one when needed. Stop genuine OOM, bootstrap errors
or unexpected local kernel builds; no automatic retry. Final candidate-backed
checks follow final artifact export and Milestone 2's accepted fix boundaries.

No project prose was useful beyond the conventional scripts; operator/cache,
verification, recovery and exact evidence are in the session design/receipts.
Session remains open and active; no lifecycle operation was performed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/
