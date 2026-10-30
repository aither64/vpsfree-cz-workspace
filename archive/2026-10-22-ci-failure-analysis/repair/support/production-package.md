# Production-origin impermanence source package

Source-only checkpoint on feature HEAD
`87e6bd4a5f5a117be5885d7a1a15ab602dde91e0`. The four assigned files are finished;
no Git window, evaluation, build, publication or VM was selected or run.
Architect owns design.md; lead owns final selection and whole-branch review.

## Exact source and quick checks

| Application path | SHA256 |
| --- | --- |
| tests/suite/upgrade/production-impermanence.nix | 183f4815158457da9fcca2f2576c7809aa8b8f6838d3838a60e0a4c7843d7be9 |
| tests/all-tests.nix | cf3b7c561fdad25a8272d2ce462ef10baa51e8c8712cfba89103c5409dbe0e0d |
| tests/suite/upgrade/common.nix | bebb502682621e712b7df48c29904a7c0beff6608d88f1abd0e4d2baae889035 |
| docs/os/testing.md (includes unchanged peer hotplug passage) | bbf4279e3075372a390ae5ed84ef33f1affbcf4a30220622614edbb2ce3c9215 |

`production-quick-checks.json` records exact commands and all exits0: three
Nix parses and Nixfmt checks, full embedded Ruby syntax and RuboCop lint
(1 file/0 offenses), diff whitespace, 38 actual-source assertion checks and
41 static source-boundary checks. Prepared discovery Nix/Bash/Ruby also parse.
The new daemon birth parser uses raw stat and rpartition, with spaces-in-comm,
recycled-PID and ambiguous-PID checks. No awk field-number parsing remains.

The 38 checks use retained historical raw fields with explicitly synthetic
public none preference and stable cgroup membership. They verify source logic,
not a production run. They exercise selected ownership, root/process/payload
mutations, precorrected-state refusal, new-run guards, reload bytes/inode
no-rewrite rejection, and real held-FD atomic unrelated-GC replacement. Changed
acquired ownership fails; an unsampled future pathname change is not detected.

Static checks prove the exact23 wrapper hashes and registrations are preserved,
common's net change is tags only, historical names occur only inside their
literal opt-in, diagnostics have their separate unchanged gate, production has
two ordinary v1/v2 instances, setters precede start, and the peer hotplug20line
passage and historical diagnostic files are byte-identical. Actual native
Nix discovery/CI selection has not run. The initial static-driver expected-tag
string was corrected to match the original conditional tag expression; it
required no product source correction.

Only the owned216 historical common insertions were removed after proving
insertion-only ownership against the frozen backup. Source and earlier29check
receipts remain in production-relevance-hold/ and ordinary-acceptance*.
Historical wrappers, pins, opt-in diagnostic and immutable baseline snapshot
are unchanged. Peer qualification/recorder work is untouched.

## Scenario and limits

The existing native template/machine from exact production
`2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` supplies stable/default6.12.113 and
locked inputs. The local candidate uses configuration=null and forces the
stable profile. One stopped NixOS24.05 impermanent CT gets all setters, including
public cpu-package none, before start; the preference remains through candidate
restart. Actual stale BASE/false/nullCPU plus validID/uniqueGCTEMP/privateRoot
is required before switch, without YAML synthesis or semantic retry.

One candidate activation retains boot kernel/ID and the live run/root/owner/data;
only saved selection may repair. One daemon reload requires unchanged bytes
and file identity/metadata. Candidate restart is sampled immediately before
other setters/readiness actions; newID/newTEMP must already be saved. Persistent
payload survives, old ephemeral payload is absent; a distinct new payload and
one reload preserve the new run. Native old-root retirement, stop and deletion
complete the flow. No historical boot, unrelated guest workload, rollback or
custom-boot runtime addition is selected; refusal/race/custom-boot units retain
their stated coverage. No runtime pass, production inventory or candidate
packaging proof follows from this source checkpoint.

## Two logical commits, peer documentation separate

Exact stage-specific bytes/messages are under production-commit-packets/;
production-commit-packets-sha256.json lists their hashes.

1. Historical default scheduling safety: common tags, catalog movement and
   owning historical-doc changes. Use historical/ (3 paths), with no registration
   or prose referencing the new fixture. This independently removes default/ci
   historical scheduling while preserving the wrappers.
2. Focused production validation: add the new fixture, its ordinary two-instance
   catalog registration and production explanation. Use production/ (3 paths),
   based on packet1. No missing-fixture commit boundary.

The production/ doc intentionally omits owner2's20line hotplug paragraph. Its
exact paragraph is retained separately as peer-hotplug.md (SHA256
a00f99a4e931e8be61d23b636f9b544b4a2ddd57cae94d9b0856b38b29b88eef), for folding
with owner2's logical units. If owner2 precedes these commits, use the exact
historical-with-peer/ and production-with-peer/ doc alternatives so neither
commit stages/removes peer prose. The latter equals the shared current doc.
Do not double-own that paragraph.

No Git mutation has occurred. On a lead-granted serialized window: refresh
parent/index/peer byte+mode+path inventory and frozen four-file hashes; use an
owned isolated clean detached checkout and normal installed/signed Overcommit
hooks. Copy only the packet's paths; write each prepared message to a temporary
file and use git commit -F. Verify each committed diff, packet hash and parent.
Before feature-only FF preserve exact accepted bytes, restore only owned tracked
old blobs and remove only the exact owned new fixture, then FF; restore peer
state only from authenticated byte snapshots if needed. No stash/reset/clean,
foreign-path staging, hook bypass, push or default merge. Reconcile all command
effects, verify empty index and peer bytes/modes/pathset, explicitly release
window before separately serialized native clean-worktree removal.

## Native no-build discovery proposal, unexecuted

The exact one-shot command is:

```sh
VPSADMINOS_DISCOVERY_EXPECTED_HEAD=<lead-selected-exact-final-head> \
  bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/run_production_discovery.sh \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-production-commit
```

The head value must be supplied only after all intended source is committed and
frozen. The script refuses dirty tracked/untracked source or existing output
receipts. It runs native catalog/tag projections serially for default,
historical-only opt-in and diagnostic-only opt-in; all other catalog controls
and VPSADMINOS_CONFIG are explicitly unset. Each query has90s INT timeout,
IFDfalse/builders-empty/fallbackfalse. The checker calls the actual candidate
TagFilters#pass? implementation with combined native test/script tags. See
production-discovery-proposal.md for exact query/env and acceptance boundaries.
Fresh lead watcher required:300s total,16MiB stdout+4MiB stderr aggregate,
2GiB physical source/eval growth ceiling,40GiB free floor; sample and stop for
unexpected realization/kernel build or threatened reserve. Fetch/evaluation
can occur; no build/VM/JSON realization follows. An error preserves receipts
and requires diagnosis, not retry. These are scheduling-selection checks only.

## Mandatory packaged-byte admission before any VM, unexecuted

Keep this in separately selected metadata/preparation, without runtime source
machinery. A target path/version alone does not prove repaired bytes. Record
production and exact final reviewed candidate Git/source NAR, lock hash and
complete locked input graph, full system/gem derivations, src and output paths.
Also record optional local test config visibility, explicit stable profile,
actual kernel/ZFS/initrd/test-shell and candidate daemon recipe identities.
Current Git-only hashes are in production-git-byte-prerequisites.json; rebind
the candidate entry to the final committed source before selection. The old
production start writer SHA256 must remain
bf83dc707880182198799228ebd801dc3501d4c8b36de41a8d60c79acdfeb6e1.

For BOTH selected boot and candidate toplevels, after separately authorized
preparation supplies actual outputs:

1. Trace the actual osctld runit service from that toplevel to its referenced
   pkgs.osctld/bin/osctld. Resolve symlinks, retain canonical paths and SHA256 of
   service and wrapper. Inspect the wrapper's bundle/GEM_HOME/GEM_PATH and
   gemspec references without executing a different ambient bundle. Follow the
   selected output's nix-store --query --requisites closure and require a unique
   active osctld gem on that resolution path. Merely finding an osctld gem
   elsewhere in a closure is insufficient. Record actual test-shell transport
   service bytes for both systems and verify compatibility with the runner.
2. Use read-only `nix derivation show` on that actual gem drv to record src,
   outputs and every input; retain the complete graph. For each path below,
   compare Git blob -> actual drv src/<path> -> actual realized gem/lib/osctld
   counterpart by SHA256 and bytes (`cmp`). Use `rg --files <actual-gem-output>`
   to locate exact files; refuse absent/duplicate/wrong-resolution candidates.
   Do not assume the production recipe matches the candidate recipe.

   - osctld/lib/osctld/commands/container/start.rb
   - osctld/lib/osctld/container/run_configuration.rb
   - osctld/lib/osctld/pool.rb
   - osctld/lib/osctld/garbage_collector.rb

Candidate packaging uses os/overlays/osctl.nix repoPath through
ruby-source-gem-config.nix and os/packages/osctld/default.nix. Its existing
postPatch changes freeze/unfreeze, not these four files; no gem metadata repin
is needed. Require exact equality for these four. Record expected versus actual
hashes separately and refuse mismatch; do not infer equality from source alone.
Production must retain the old writer, candidate must consume the reviewed
writer/reader/GC source. No such src/realized proof has yet been executed for
this template. The previous846bb preparation proves neither of these outputs.

Separate admission must then measure native JSON's complete RAM/SHM/CPU and all
disks, exact image archive hash, cache/build allowlist and actual new/closure/
transient physical bytes. Zero/missing native resource metadata is not a resource
reservation. Lead owns serial VM selection and bounded guardian/cleanup. No
historicalVM, metadata realization, input/pin/workflow change or publication is
selected by this source package.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/

Packet correction: production-packet-correction.json proves only the20line peer
insertion is excluded and the entire baseline suffix from qualification
shutdown diagnostics remains byte-equal in all four staged doc variants.
The earlier heading-to-EOF extraction was a packet-only error; do not use its
obsolete hashes. Shipping source hashes remain unchanged.
