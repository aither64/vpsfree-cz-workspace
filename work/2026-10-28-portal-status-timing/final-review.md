# Independent final review

## Findings

1. **Blocking — the detached runner cannot resume a selected package whose native startup failed.**
   General and risk/compatibility lanes. In operational checkpoint
   `e52def60358f0a84ecb8a31d490aa09cbf59edac`,
   [rollout.md:764](rollout.md#L764) skips idle waiting only after publication
   intent, and [rollout.md:800](rollout.md#L800) always re-enters the ordinary
   `workspace-host switch`. It never starts the selected native service before
   that retry. A copy/schema/space refusal in ExecStartPre happens after the old
   native has stopped and the candidate profile has been selected. The next
   ordinary switch runs `activate_candidate` admission again; its
   `quiesce_sessions` invokes `thread require-execution-idle` against the absent
   backend (`libexec/workspace-host:715`, `:2402`, and
   `libexec/dev-session:9245` at runtime `8c597b6f`). It therefore refuses before
   reaching the hook that could finish publication and restart native. The
   documented same-job forward recovery is incomplete both before publication
   intent and after a partially completed exchange. Add an explicit,
   journal-aware selected-service recovery step and cover failure after native
   shutdown, before publication, and between the two exchanges. Preserve the
   existing claim/transition checks and the prohibition on restoring old data.

2. **Blocking — writer exclusion misses ordinary embedded CLI writers during the copy.**
   Risk/compatibility lane. In the same checkpoint,
   [rollout.md:608](rollout.md#L608) classifies native writers only when argv
   contains the separate `app-server` token. The runner holds only managed-daemon
   lifecycle and Unix App Server startup locks
   ([rollout.md:778](rollout.md#L778)); the descriptor scans before and after the
   copy are instantaneous checks ([rollout.md:681](rollout.md#L681) and
   `:692`). Codex 0.165's ordinary `codex exec` initializes the state database
   and starts an **in-process** App Server (`codex-rs/exec/src/lib.rs:716`,
   `:1022` in source `j4xcz959sk3k5isb6q29gpyivjym37j9-source`). Its argv has
   no `app-server` token. The native startup lock is conditional on
   `AppServerTransport::UnixSocket` (`codex-rs/app-server/src/lib.rs:666`).
   Consequently an exec that starts and finishes between the two descriptor
   scans can change a rollout or database while partitioning without being
   detected. A new thread or later write can then remain only in the original
   backup, absent from the published homes, while acceptance compares against
   the earlier inventory and passes. This is an ordinary concurrent command,
   within the stated trusted-operator boundary. Establish an effective
   maintenance exclusion for the supported embedded/direct writer paths, or a
   source-stability admission that refuses publication when those writes occur.
   Exercise a short-lived writer entirely inside the copy interval; a test of
   a descriptor held open during a single scan does not cover this case.

3. **Important — committed VM fixtures still configure and inspect the stock home.**
   General lane, runtime `8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5`.
   `nix/tests/session-creation.nix:266` queries `~/.codex/state_*.sqlite`, while
   `:288` and `nix/tests/session-archive-lifecycle.nix:137` write the mock-provider
   configuration only to `~/.codex/config.toml`. The shipped runtime now uses
   `state/codex-homes/fixture`, so these packaged creation/archive checks cannot
   validate the new contract as committed. Provision the fixture's private home
   and inspect that database/history. Retain the stock token location only where
   the host provider catalog intentionally selects it. The lead reported the
   corresponding CI failures and was preparing fixture fixes during this review;
   those uncommitted fixes are outside the reviewed ranges.

No additional Important or Advisory findings. The first two findings concern
the one-time operational source rather than a request for a permanent migration
framework. Review does not authorize executing it.

## Scope and proportionality

The scope matches the accepted outcome: one private native home per registered
workspace, exact portal Codex 0.165, consistent storage selection through native,
naming, providers, recovery and managed terminal paths, matching consumer pins,
and an installation-specific conversion. There is no permanent migration API or
new shared-home compatibility mode. The frozen schema inventory is substantial
but appropriate to preservation of five native databases. Keeping operational
source in this rollout record and lasting storage/package behavior in the owning
project guides is appropriate. The issues above are inside the accepted
concurrency/recovery boundary; no hostile-local-filesystem defenses are requested.

Home selection belongs to dev-workspace. codex-web supplies version-compatible
generic client/utility behavior and is consumed through both the runtime's Nix
source and Go pseudo-version. Configuration imports devWorkspace's host module
and `mkCodexPackage`; the workspace composes the application through the
unchanged vpsFree extension. Actual lock graphs preserve that direction and
select the same runtime/codex-web revisions. The small storage argument glue in
Ruby and Go has explicit integration boundaries and focused assertions; no
additional extraction is required by this review.

## Reviewed commits and whole-branch history

All four lanes were read and applied directly: general,
architecture/repetition, scope/proportionality and risk/compatibility. This was
a high-risk review because it changes persistent state ownership, authentication
separation and deployment/recovery ordering. Reviewer: fresh standalone
`/root/final_review`, gpt-6.1-sol/xhigh, read-only review behavior under the
installed full-access execution policy. Fallback reason: the initiative has no
eligible retained reviewer; the supplied installed catalog digest
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`
selects `delegated/reviewer`. No nested agents were used.

| Repository | Base | Reviewed head | Complete series |
| --- | --- | --- | --- |
| codex-web | `58300182763a01de7248ddf7c6cb9a4f0c6216cb` | `ba8dfdd27daa7ab3f4350f7a2627984b6b7f84cf` | One compatibility/provenance commit |
| dev-workspace | `d0e4318cb1872feb69f3109f032870c310f14bdf` | `8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5` | One private-home/exact-native selection commit |
| configuration | `7a254c88b0b54a32300a319b3e4ed32936d9b004` | `dcb5982fd4325d57cda79693fa4da27c7a955413` | Generated pin `f455dcc8f3e3aba685d1f569cc2903696b409b69`, then credential path `dcb5982f` |
| workspace | `e52def60358f0a84ecb8a31d490aa09cbf59edac` | `e826d3b2ede493995ee7e435826360b20ad878e4` | One composition pin commit |

I inspected the complete listed series and final diffs, plus the explicitly
assigned committed operational source at shared checkpoint `e52def60358f0a84ecb8a31d490aa09cbf59edac`.
The workspace rebase is patch-equivalent: `git range-diff` reports `=` between
the former `c2bfb715..5deaee4f` and current `e52def603..e826d3b2` ranges.
There are no obsolete unmerged approaches, fixup sequences or unused interim
compatibility paths in these ranges. The runtime's combined private-home and
native/naming prerequisites are acceptable as the single cutover contract
described in the packet; configuration's independent functional change is split
from its generated pin update.

**Repeated-pin conclusion:** no repeated update streams remain. Each affected
logical input is updated once per consuming repository. The transitive
codex-web/llm-agents lock changes follow the selected runtime. Source and Go
codex-web pins agree; the workspace and configuration select runtime `8c597b6f`;
llm-agents is `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`; extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3` is unchanged. No deployment/publication
exception was needed to retain intermediate dependency commits.

**Migration-lineage conclusion:** no new project-owned SQL migrations.
Upstream native 0.165 includes migration 62,
`state/migrations/0062_threads_attached_parent.sql`; the packet records that
stock already applied it to the shared source. The one-time partition requires
the exact current schema and reproduces that schema rather than introducing an
intermediate version or stale-development guards. Its supplied provenance is
unexecuted, unmerged, unreleased, undeployed and not externally consumed; there
is no earlier operational version requiring retention. That lineage is coherent,
but operational correctness remains blocked by findings 1 and 2. Recovery must
stay forward-only after candidate profile selection, including before the first
home exchange. An older shared-home package is not a supported rollback target.

## Evidence and remaining gates

The working rollout equals its committed blob. I independently recomputed all
six fenced-block SHA-256 values and verified byte-for-byte equality with the
raw Python/JSON files: inventory, partition, cutover, acceptance, tests and
schemas. All matched. The database partition reconstructs exact schemas,
compares retained values, preserves unknown stock records, checks foreign keys
and copied rollout contents, and uses durable inode-bound exchanges to avoid
replacing newer stock writes during an exchange retry. Those mechanisms do not
by themselves resolve the writer-admission finding.

Quick Go/Ruby/schema/config/catalog/vendor/composition and seven synthetic
migration results are evidence supplied by the packet; I did not relaunch
builds, native integration, migration tests, live services or message delivery.
During review the lead additionally reported passing runtime fast/package CI,
the fixture failures above, and an unrelated asynchronous uploads-browser check
under diagnosis. No source fixes or later hashes have been reviewed here.

After addressing findings, remaining gates include exact native 0.164-to-0.165
saved-state resume/fork, prompted naming and managed lifecycle checks, packaged
creation/archive/recovery checks, failure/resume coverage for the actual outer
runner and hook, final committed system/application builds and pin validation,
fresh source inventory and capacity admission, claimed deployment, partition
conservation and isolation, every owned thread readable, both affected activity
endpoints, and browser/tmux/provider/team acceptance. The same-attempt retry
uses the existing digest-checked receipt and requires durable `accepted` state;
that live reconciliation and retry remain unexecuted. Passing review or checks
will not grant master integration, forced interruption, reboot or backup deletion.

This review is complete for the ranges above; the deliverable is **not ready
for migration/deployment** until the Blocking findings are resolved and the
remaining applicable release gates pass.
