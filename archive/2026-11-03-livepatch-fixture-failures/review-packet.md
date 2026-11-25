# Final review packet: current-build livepatch tests

Status: final review ready. All intended changes are committed, quick checks
and final hooks passed, and worktree is clean. No long tests started.

## User scope and result to assess

The user first requested investigation, then rejected freezing Nixpkgs and
retaining a historical-offset test lane. They requested a concrete plan and
subsequently authorized it with `implement it`. The accepted implementation
removes the historical v7 whole-file allowlist from ordinary CI and replaces
candidate-dependent offsets with nine finite, validated current-build sites.
Current-source witness strength, predecessor/boot identity, runtime integrity
and recovery must remain. No production input/pin change, merge, deployment
or lifecycle action is authorized. Do not approve scope solely because it was
included in an internal design.

Affected repository: canonical `git@github.com:vpsfreecz/vpsadminos.git`.
Target default is staging; no integration approval exists.
Worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos`.
Base: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
Final head: `4fc0f375de34f92dd59aef94080e874b302c720c`.
Complete series: one commit, `tests/livepatch: qualify current module probe sites`.
Complete diff: 16 files, 2056 insertions and 180 deletions. All paths match
package ownership; no producer/input/lock/migration paths changed. Message-only
amendments retained the same source tree and one final commit; no published
or deployed intermediate content exists.

Read this session's [plan](plan.md), [design](design.md),
[implementation plan](implementation-plan.md), [state](state.md),
[ELF feasibility](probe-elf-feasibility.md) and
[semantic probe contracts](probe-redesign.md). The earlier input-freeze and
historical-lane proposals are withdrawn; they are not acceptance requirements.

## Review lanes and selection

Overall risk: high because the test-only kernel probes redirect execution and
must preserve guest stack/ownership semantics, and false qualification would
misrepresent livepatch correctness. Production code and persistent state are
unchanged. Use general, architecture/repetition, scope/proportionality and
risk/compatibility lanes, reading every corresponding reference under the
mandatory-change-review skill. The finite internal resolver and JSON record
must remain proportional to actual test consumers, not grow into a generic
instrumentation or review-state system.

Selected reviewer: retained independent reviewer0, gpt-6.1-sol / xhigh,
read-only source, no model/effort overrides or nested reviewer. The lead will
reverify exact session identity/roster/readiness before the explicit assignment.

## History and migration inventory

One coherent feature commit is present: the new resolver, independent controls
and all consumers jointly establish one current-build test contract. There is
no standalone public helper feature or separate dependency-update stream. The
implementation packages were parallel ownership boundaries, not shipping
history stages. All package edits are staged together after source freeze to
avoid triggering Overcommit's repository-wide stash/reset for tracked unstaged
changes. Hooks remain enabled.

No database migrations, production protocols, schema/format migrations,
dependency/channel/pin updates, deployed intermediates, external consumers of
an intermediate schema, or obsolete feature iterations are intended in the
series. Independently inspect the complete base-to-head history and final diff;
explicitly conclude on obsolete history, repeated-update streams and migration
lineage (including `no migrations`). No prior independent final review occurred. Final hooks passed warning-free;
tracked unstaged changes were empty so Overcommit did not enter stash/reset.
The final index/worktree and nonignored untracked inventory are clean.

## Quick-check evidence and boundaries

- [A result](package-a-result.md): declared hooks installed/signed; Nix/YAML/
  bash/Ruby syntax; normal producer unchanged with IFD disabled; 14 actual
  workflow capture/identity controls (real hashing/JSON assertions, realization
  stubbed); eight actual consumer digest controls; latest official compatible
  action refs verified, no action-ref changes.
- [B result](package-b-result.md): packaged resolver and declared siteChecks;
  final clean source-directory check has 21 independent controls passing. The
  actual published current module, verified immutable SDK vmlinux and original
  FUSE produce all nine records, source hashes unchanged. Actual generation
  took about nine minutes due to structured DWARF relocation processing.
- [D result](package-d-result.md): independent tiny ELF/DWARF/assembly sources
  exercise placement, debug/register changes, true special livepatch relocation
  sections, inline ambiguity, original callee scheduling, wrong widths, unsafe
  frames, liveness and strict identity cases. No kernel fixture builds.
- [C result](package-c-result.md): 26 focused consumer specs pass after repairing
  the declared native RUBYLIB path. Nix/Ruby syntax, formatting and focused
  RuboCop pass. Helper compilation uses verified frozen SDK and boot compiler:
  two external module CCs and one AS only, no kernel/config rebuild. All 49
  probe imports and 19 pernet imports match SDK CRCs. Both common and fragment
  consumers accept the actual B JSON. No live guest behavior is claimed.

The fixed boot output/dev cache endpoints returned HTTP 404. Actual CLI proof
used pinned tracked archives restored by current Nix into owned scratch, with
archive and binary hashes verified. This does not realize the unchanged boot
helper or candidateSites derivation. A dry-run would build old Nix support
packages first; no unrelated old-Nix/kernel build was launched. Full packaging
and runtime checks remain pending after review. Assess this limit explicitly.

No long VM or qualification test has started. Future acceptance must prove
FUSE original-callee identity, exact caller filtering, reliable stack and
unlocked-copy-state behavior; TCP live sample reachability/wide bound and full
receiver integrity; unchanged state/race/callback/recovery assertions and full
existing matrix. Host controls or static ELF evidence do not replace these.

## Required review focus

Assess correctness and sufficiency directly, including structured compressed/
relocated DWARF parsing, special livepatch object/ordinal handling, instruction
and frame predicates, finite register-role liveness, ABI member facts, actual
producer identity flow and safe failure behavior. FUSE uses the original
callee's safe entry with an exact caller return-PC filter before count/capture/
hold; TCP observes the completed wide arithmetic result and verifies reception.
Do not accept entry-only evidence or a hidden historical fallback.

Project documentation changes are in docs/os/testing.md. The lead directly
applied the user-facing writing skill after facts settled. Other raw logs,
source/derivation receipts and temporary SDK paths remain session evidence,
not project documentation or commit-message transcripts. No rollout occurred.

Return ordered Blocking/Important/Advisory findings with source references and
explicit history/migration conclusions. Remain read-only; implementers own fixes.
