# Runtime implementation handoff — 2026-10-31

Runtime source and documentation are complete, quick checks pass, and the feature
head is published. Combined independent review, packaged verification,
deployment and integration remain with the lead. No machine or repository claim,
live root retirement, store GC, package selection or lifecycle action occurred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-codex-profile-generations/

## Exact source and history

- Repository: `git@github.com:aither64/dev-workspace.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-codex-profile-generations/dev-workspace`.
- Branch: `2026-10-27-codex-profile-generations`.
- Fresh base: `6f54d0c7fdb974705c120b3c1ef5372f5897d544` (`origin/master`).
- Published head: `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`.
- Final tree: `3332e5bd16bbcae71c3d120720f01da03a318c95`.
- Fresh SSH `git ls-remote origin` confirmed those exact master/feature heads
  after push. Worktree is clean.
- Complete base-to-head series: one commit,
  `c2182254 codex: retire redundant generation roots through coordination collection`.
- Final diff: 10 files, 290 insertions and 36 deletions. No superseded approaches,
  follow-up commits, repeated dependency/channel/input update streams or generated
  updates remain. No dependency pins changed. The source, tests and two owning
  documents form one logical behavior change.
- No schema/database migrations. Runtime root retirement is a new bounded,
  idempotent operation over existing symlinks, without a persistent-format change.
  This feature head has not been merged, released or deployed. It was published
  for downstream preparation; no live roots have been retired by this work.

## Behavior and boundaries

Removed both numeric history writer calls from `libexec/workspace-host`, their
helper and dead lookup. Current selection, application profiles, pending format,
admission, restart, launch evidence and forward recovery keep their existing
contracts. No Codex upgrade, process pins, new history manager, public command,
store GC or native-copy pruning was introduced.

The host supplies its strict parsed pending record to the existing coordinator
collector while holding generation and preparation exclusion. Malformed pending
state refuses before collection. Valid pending state preserves only legacy Codex
cleanup; other ordinary collection remains available. After recovery clears
pending, a later sweep can retire recognized positive-numeric direct-store links
immediately below the ordinary history directory. Current must resolve directly
to an existing store output, and the selected profile must match the collector's
package. Each removal rechecks profile identity and resolution, current target,
history directory type and exact history link target. Missing history links are
safe to retry; unknown names/types/targets and symlinked history directories are
preserved and reported. Current and ordinary profiles are not removed by the
new action. Normal existing profile-retention policy is unchanged.

Running store processes rely on ordinary Nix runtime roots and their reference
closures. The focused running-output fixture uses a live store Ruby executable
as a stand-in; it does not certify a live Codex deployment or daemon-copy
selection. Live read-only Nix-root evidence belongs to rollout acceptance.

The trusted local operator boundary from dev-workspace AGENTS applies. Checks
address ordinary configuration mistakes, concurrent writers and interrupted
operations; this change adds no hostile-administrator filesystem framework.

Documentation updated:

- `docs/codex-package.md`: ordinary profiles/current protection, runtime roots,
  pending recovery and the separate ownership of native copies.
- `docs/coordination-operations.md`: existing preview/apply entry points,
  preservation/refusal reasons, exact revalidation, retry and periodic retirement.

The lead separately applied the required writing guidance and accepted the final
prose and diagnostic strings before commit. `docs/workspace-portal.md` was checked;
its generic retained-root/state-location wording remains accurate.

## Quick verification

Commands ran from the exact runtime worktree. The interpreter was selected with
`suitable nix shell` using the already-realized Ruby output resolved from this
flake's pinned nixpkgs:

```sh
nix shell /nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9 --command ruby ...
```

Results on the final source/test content:

| Check | Result | Duration |
| --- | --- | --- |
| `ruby -Itest test/coordination_gc_test.rb --name '/codex/'` | 8 tests, 53 assertions, no failures/errors/skips | 1.80 s |
| Four assigned host files through aggregate harness below | 134 tests, 1242 assertions, no failures/errors/skips | 17.29 s |
| `ruby -Itest test/coordination_gc_test.rb` | 46 tests, 251 assertions, no failures/errors/skips | 93.47 s |
| Existing shared-admission/exclusion check below | 1 test, 4 assertions, no failures/errors/skips | 0.36 s |
| `ruby -c` on all three changed runtime Ruby files | Syntax OK | quick |
| `git diff --check` | pass | quick |

The full collector suite exceeded the expected quick-check duration. It completed
successfully and was reported immediately; no rerun is needed merely because of
that overrun. Subsequent long/uncertain batches belong to a fresh utility watcher.
The repository declares no hook framework; core.hooksPath is unset and its hooks
directory contains only sample files. No declared hooks were bypassed.

Exact host command, after loading all aggregate helper definitions:

```sh
nix shell /nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9 --command ruby -Itest -r./test/workspace_host_test -e 'names = WorkspaceHostTest.instance_methods.grep(/^test_/).select { |name| WorkspaceHostTest.instance_method(name).source_location.first.match?(%r{/workspace_host/(profile_transition|agent_team_registration|live_switch|commands_and_locks)_test.rb\z}) }; ARGV.concat(["--name", "/\\A(?:#{names.join("|")})\\z/"])'
```

Existing concurrent session admission and preparation/package exclusion:

```sh
nix shell /nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9 --command ruby -Itest test/workspace_coordination_test.rb --name test_collection_shares_generation_with_sessions_but_excludes_preparation_and_switches
```

New coverage includes changed/unchanged switches without numeric roots, unchanged
forward retry, preview without changes, retirement while a store executable is
running, current/profile preservation, valid-pending skip and clearing/retry,
malformed strict-pending refusal, unknown layouts, stale profile/current/history
target refusal, absent-link idempotence and recreated legacy-root retry.

Harness/setup lessons: standalone assigned host files depend on helpers loaded
by `test/workspace_host_test.rb`; initial direct file invocations therefore
reported missing constants/methods. Loading that aggregate and filtering by
source file fixed invocation without modifying fixture architecture. Calling
`runnable_methods` before Minitest initializes its seed also fails; the final
command uses ordinary `instance_methods` for selection. `nix develop --no-build`
is not a supported flag in this installed Nix; pinned output selection above
worked and required no tool build. These failed setup/invocation attempts do not
invalidate the successful final checks.

## Post-review verification for the lead

Do not run these before combined committed-deliverable review. Run long or
uncertain commands through the lead's fresh watcher, retaining exact derivation
and input receipts. These are existing exported checks, not new launchers:

```sh
nix build --no-link --print-build-logs \
  .#checks.x86_64-linux.ruby-workspace_host-0 \
  .#checks.x86_64-linux.ruby-coordination_gc-0 \
  .#checks.x86_64-linux.ruby-workspace_coordination-0 \
  .#checks.x86_64-linux.ruby-workspace_coordination-1
```

This batch packages full profile-transition/recovery and collector/admission
coverage. Budget roughly 2–5 minutes after cached tools; this is an estimate,
not a measured packaged run. The collector source suite alone took 93.47 s.
Existing `session-creation` covers naming failure/manual recovery; no naming
implementation or native contract changed here. If the lead's verification
brief requires fresh VM evidence rather than reusable existing receipts, its
exact command is `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation`
(rough planning budget 10–30 minutes depending on build/cache state).

For applicable existing package/closure checks, exact attributes are
`checks.x86_64-linux.codex-package` and
`checks.x86_64-linux.host-package-contract`, invoked with the same `nix build`
flags. Reuse valid unchanged derivation/input receipts where available; their
first-build duration is uncertain. No long Nix/integration check or native GC
campaign was started by implementer0.

## Runtime input graph

The complete graph, follows edges, nar hashes and root mapping are in committed
`flake.lock` at the final head; SHA-256 of its bytes is
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.
No lockfile modification occurred. Locked node revisions:

| Node | Revision |
| --- | --- |
| nixpkgs | `f20cd90e28fe0403873f473b29e42662cd86e8c4` |
| llm-agents | `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314` |
| codex-web | `d3a29bee90ef00a08816920408c596152339a637` |
| bun2nix | `07a5bfc8ac36c5370199343fa620b69f63186e33` |
| flake-parts | `024633cd702b10285db5cb19b40ad48d2399ba60` |
| nixpkgs_2 | `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4` |
| systems | `d36eeed142f88b5a636f2e3856a53c61654cf29b` |
| treefmt-nix | `0d6d739a833ba9a9c93034862e4a7b061a062a1c` |

The composed workspace and configuration heads/pins, exact application/system
outputs, deployment results and integration ancestry evidence remain separate
lead/downstream receipts. There is no deployed-head equivalence mapping for this
runtime range because it has not been deployed or rewritten.
