# Package D: configuration workflow adoption

Status: both workflow changes implemented, quick-checked, committed and feature
branches published. Independent final review passed all eight exact ranges with
no findings; see [review-report.md](review-report.md). Real package/live updater
verification remains pending. No default-branch integration, runtime configuration
change, package release, machine operation or session lifecycle action occurred.

## Exact ranges and source publication

| Repository | Fresh default base | Published final head | Complete series / final diff |
| --- | --- | --- | --- |
| vpsfree-cz-configuration | `50d263d4127c05163d660fae1c4b9b887584032d` | `f5bf3f026210d30c0b9b219aac47ff6490e4cddc` | One `ci: guard automated flake updates` commit; `.github/workflows/daily-update.yml` only, 53 insertions / 26 deletions |
| vpsadminos-org-configuration | `6b04b48e9c076e5525ccb7c38ce174232414f0b5` | `30ea016491f78d88037508e3a7e9c9a20d50511b` | One `ci: guard automated flake updates` commit; `.github/workflows/daily-update.yml` only, 37 insertions / 9 deletions |

Both use branch `2026-10-24-flake-update-downgrade-guard-replacement` and
canonical `git@github.com:vpsfreecz/<repository>.git` SSH remotes. Both worktrees
are under this session's worktree group. Fresh SSH `git ls-remote` after each
successful push returned its exact final head. Both working trees and indexes
are clean; [package-d-branches.json](package-d-branches.json) includes exact
paths, complete series/diff summaries and tested workflow SHA-256 values.

Every tool invocation selects the same final source:
`github:vpsfreecz/confctl/7ba361d22a4aac044cb02abf8397800bcf5726bf#confctl`.
Git blob comparisons prove both `flake.nix` and `flake.lock` unchanged from each
base. No deployment-tool pin, Nix module option, runtime software or persistent
state was changed. There are no migrations and no merged/released/deployed or
externally consumed migration versions. Each adoption stream has one final
commit, with no obsolete implementation or intermediate pin history to retain.
No supported released/deployed boundary requires an older development tool pin.

## Workflow behavior

The workflows explicitly check out `master`, retain the original lock under
RUNNER_TEMP before any Nix/dependency work, and expose an explicit provider token.
All six existing channel update calls use the pinned new guard with
`--forward-only`; all selectors, commit/changelog options, llm-agents Codex
version condition and post-update assertion remain intact.

The original tools shell is retained around update and final-check steps for
Ruby/Overcommit, with `set -euo pipefail` in both outer and inner shells. Within
that shell every guard uses an explicit `nix shell "$CONFCTL_FLAKE" -c confctl`;
none selects the old configuration tool. The org workflow now installs/signs
its declared hooks, including push configuration. Existing vpsFree dependency,
RSpec, RuboCop, audit and gem regeneration steps are retained.

After all dependency steps/hooks/tests, the final block exports
`git show HEAD:flake.lock` into RUNNER_TEMP and checks that committed blob against
the original baseline through the same pinned provider immediately before an
ordinary non-force push. A rejected or errored update/check stops later commands,
including after earlier successful local commits. A moved target makes the push
fail; the next run must begin from a fresh checkout/baseline. There is no stale
pull/rebase retry or copied ancestry implementation.

The source provider was amended once before D commits to align its guide/manual
with this committed-blob final check. The old development SHA d58181a is only
provenance; all final consumer pins use 7ba361d. See [package-b-report.md](package-b-report.md)
for exact old/new source proof, unchanged application-code evidence and the
superseded CI cancellation receipt.

## Quick verification

[package-d-workflow-check.py](package-d-workflow-check.py) executes the actual
workflow shell bodies with nonpublishing Nix/confctl/Git/dependency fixtures.
Final pinned sources passed 20 scenarios, plus YAML parsing and Bash syntax:

- Accepted updates and llm-agents up-to-date skip publish only after final check.
- Known policy rejection (3) and evidence failure (1) stop both early and late
  updates, even when earlier local commits exist.
- Commit-hook failure stops remaining update/dependency/publication work.
- Final policy rejection/error prevents push.
- llm-agents post-update Codex version mismatch stops publication.
- A dependency-stage committed lock regression is rejected even if the worktree
  differs; uncommitted worktree drift cannot substitute for checking HEAD.
- An ordinary push rejects simulated remote movement without retry.
- Exact pinned inner tool, token inheritance, selectors, changelog policy,
  original baseline and committed final snapshot paths are asserted.

This verifies orchestration and failure propagation. It does not substitute for
real provider/Nix, Git history/remote movement or package/runtime execution.
Fixtures isolate only their own YAML-converter stdlib Ruby environment from
Bundler variables; actual workflow and runtime probe environment is preserved.

Compact results: [package-d-quick.log](package-d-quick.log). Both ordinary
pre-commit and commit-message hooks passed in the declared Nix environments;
only soft 72-column message warnings occurred, with every line below the
workspace's 80-column limit. Each commit staged only its workflow. All unstaged
tracked diffs and staged whitespace checks were clean. No broad reset/stash,
hook bypass, long suite or package build was used.

## Setup, action refs and environment evidence

Session identity was rechecked before package work and after interruption;
current slug, both environment fields and trusted workspace/thread binding
matched. Both worktrees were created from fresh SSH defaults. Post-checkout hooks
initially refused missing locked gems after physical creation. A fresh Luna/low
utility performed only authorized `nix develop` dependency/hook setup; both
passed (58s vpsFree, 34s org). Registration retries then succeeded, preserving
those worktrees. Logs: [package-d-shell-vpsfree.log](package-d-shell-vpsfree.log),
[package-d-shell-org.log](package-d-shell-org.log). No hook bypass or competing
worktree occurred. The org shell's untracked `.bundle/` configuration was
preserved and excluded via local Git metadata, not committed as source.

Official upstream action documentation and SSH refs were read before changing
`uses`. Latest compatible major refs are:

- [actions/checkout v7](https://github.com/actions/checkout): tag v7 is
  `3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1); its
  [action metadata](https://github.com/actions/checkout/blob/v7/action.yml)
  selects Node 24.
- [actions/cache v6](https://github.com/actions/cache): tag v6 is
  `55cc8345863c7cc4c66a329aec7e433d2d1c52a9` (v6.1.0). Official restore/save
  examples use v6; Node 24 requires runner 2.327.1 or later.
- [cachix/install-nix-action v31](https://github.com/cachix/install-nix-action/releases):
  signed major tag peels to `75c75c31ebece974e48ebc36b4ad125bd97bd97b`, same
  as current 31.11.3. It remains a composite Bash action on Linux.

Both jobs use GitHub-hosted `ubuntu-latest`, the upstream supported examples'
runner type. There is no self-hosted/container Node runtime constraint here and
no reason to retain an older major. Only the org workflow needed checkout/cache
ref bumps; vpsFree already used v7/v6. The Nix action remains v31 in both.
The ambient installer version is not proof of the Nix prepended by confctl's
package wrapper; actual package evidence remains a post-review requirement.

Quick old tools-shell smoke checks observed RUBYOPT and BUNDLE_GEMFILE absent
in both configuration shells; their current old packaged confctl paths were
`/nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl` (vpsFree) and
`/nix/store/9r7w7d05wjn9y8kh4l78gk6nigk2cbw6-confctl/bin/confctl` (org).
This is environment/source compatibility evidence, not new package proof.
IRC's shell intentionally exports Ruby/Bundler settings and its actual pinned
new-package invocation must still be tested without clearing them.

## Documentation and remaining verification

The authoritative contract remains confctl's
[guarded input guide](https://github.com/vpsfreecz/confctl/blob/7ba361d22a4aac044cb02abf8397800bcf5726bf/docs/flake-inputs.md#guarded-automated-updates)
and manual, owned by B. No configuration module behavior or operator deployment
procedure changed; no duplicate README or operational document was needed.
Lead completed its direct writing pass on the new workflow step names and
provider guide/manual. Per-rollout evidence belongs here, not in either
configuration repository's reusable documentation.

Prepared exact commands are in [package-d-live-checks.md](package-d-live-checks.md)
and [provider-runtime-probe.sh](provider-runtime-probe.sh), whose Bash syntax
passes. They cover both old configuration shells, IRC's known Bundler boundary,
actual pinned executable/source/input graph/bundled Nix receipts, old channel
outputs and both real nonpublishing configuration workflow patterns. Together
with C's [five-pattern preparation](package-c-live-checks.md), all seven patterns
have a concrete post-review verification brief. These commands were prepared
only; no live update/build/VM/CI dispatch occurred. C is also preparing its
bounded standalone five-pattern driver and Terraform VM smoke command. The lead
must serialize those with B/D runtime verification through fresh Luna watchers.

The lead-owned final independent review covered all complete final ranges,
graph/transaction/provider/publication contracts, whole-branch history and
explicit no-migrations conclusions, with no findings. Longer suites and real
package/workflow/target-movement checks now follow under serialized lead launch.
No branch is
claimed ready for integration; integration still needs explicit direction.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>

## Prepared probe preflight correction

Lead preflight requested an explicit per-consumer input. Exact reviewed lock
graphs confirm vpsFree's stable root `nixpkgsStable` (the `nixpkgs` alias follows
it), org's root `nixpkgs`, and IRC's chained alias `nixpkgs`. The runtime probe
now requires/export `PROBE_INPUT` and asserts exactly one matching JSON row with
a full 40-hex-character revision. The command brief specifies each input,
channel-probe flag and distinct receipt directory. Production/staging roots in
vpsFree are not substituted for its stable input.

Metadata is now validated in memory before writing its receipt, including
rejecting accidental raw GITHUB_TOKEN/GH_TOKEN values without printing them.
Environment receipts still print only Ruby-variable presence booleans. Focused
offline probe checks passed for all three requested consumer inputs; wrong-row,
null-revision and short-revision fixtures reject; clean metadata writes and
credential-bearing metadata rejects without a file or token output; missing
PROBE_INPUT fails before Git/Nix/receipt work. Bash syntax passes. No actual
package, Nix or live operation was run by this preflight. Application commits
and review ranges are unchanged.

## Prepared executable D verification

[package-d-post-review.py](package-d-post-review.py) and its
[verification manifest](package-d-verification-manifest.json) now bind the exact
reviewed config heads/trees, workflow/source/lock blobs and hashes, complete lock
graphs, provider graph, runtime probe and each original/transformed shell block.
The driver's SHA-256 is
`4ebf3d4005650be41610fed02ef58b8a8d311596a1244ce66c616dfaee37a75d`;
manifest SHA-256 is
`e077eabe3008e195980e7794f07bc3a4343e66869e17029fc62aae25920a1655`.

The [command brief](package-d-live-checks.md) gives four separate serialized
operations: actual package inside each old config shell, then each complete
nonpublishing workflow pattern. Execution requires the completed review receipt
and C's successful exact-provider startup receipt, preserving the actual old
shell and pinned inner package. Each operation clones the exact reviewed source
into an owned `/tmp/flake-update-guard-d-*` path and disables its push URL.

The two known hosted-runner `sudo mkdir/chown` GC-root setup lines are omitted
per workflow, as is its final push. A read-only preflight verified the existing
executing-user GC-root directory ownership and write/search permissions on this
host; execution repeats that check and refuses a mismatch. There is no global
host mutation or sudo shim. The manifest records those exact omissions and
nonexecuted hosted checkout/Nix-installer/cache actions; all guard/channel,
llm-agents/dependency/commit/final-check shell logic is unchanged.

Preparation-only compile, JSON/hash checks and `bash -n` for all 12 shell blocks
passed in [package-d-driver-preflight.log](package-d-driver-preflight.log).
No package build, actual package invocation, live candidate, clone, privileged
command or publication was executed by this preparation. No utility was launched;
the lead retains serialization and acceptance. Application heads/review ranges
are unchanged.
