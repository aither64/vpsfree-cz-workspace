# CI failure investigation design

Current phase: authorized root-cause repair. The repair section below supersedes
the earlier investigation-only execution limits; those sections and findings
remain the record of what was established before implementation.

### Current production relevance decision and execution hold

The user's production-relevance direction supersedes earlier selection of the
historical upgrade validation matrix. Do not select another 3cc/3cb predecessor
boot or expand the ordinary-upgrade assertions while the focused replacement
is prepared.
Owner3 preserved the completed uncommitted assertions, checks and hotplug docs
at `repair/support/production-relevance-hold/`; no source is discarded or
rewritten. Its earlier design acceptance is a completed checkpoint, not a
current requirement to execute those historical cases or commit that expansion.

The lead verified configuration master
`cc31347a0cd3180ea314d768ca04eba481a88ce6` against a fresh SSH remote-ref
observation. Its production channel selects vpsAdminOS
`2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`. Exact local source inspection,
with lazy fetching disabled, confirms this current production source still
saves the run before selecting the impermanent dataset; only a successful CPU
scheduling assignment supplies the later incidental save. The pin also removes
the earlier unsafe mount-table adoption. Therefore the writer repair and narrow
authenticated reader/GC protection address a current production-origin state,
not merely an obsolete predecessor. Whether an individual live CT carries stale
state still requires observation; the source defect does not prove every node
or CT is affected.

All existing `upgrade/from-6.12*` and `upgrade/from-6.18*` wrappers select frozen
3cc or 3cb revisions. The via-6.18 case boots 3cc, activates 3cb userspace, then
the candidate. `common.nix` boots the predecessor's actual kernel and activates
candidate userspace without replacing the running kernel. These remain
historical compatibility tests, but none is exact current-production 2ab to
candidate validation. Kernel release labels alone do not identify the source
or deployment boundary. Historical first-switch and Podman captures remain
evidence of their declared samples, not proof of current production behavior.

Owner0 completed exact-source profile tracing, accepted by the lead. The 2ab
stable default is Linux 6.12.113, source
`1dfea587406b7dd79973831d1677fb2418e5e9aa`, with ZFS
`481845fca6ae3f61ca2262c1a5693a58ae364650` and its declared patch. The selected
production imports do not enable the unstable 6.18.49 profile. Configuration
`configs/node/kernels.nix` has empty explicit boot/runtime maps, but runtime
selection can read ignored `kernels.json` from PWD or the source directory.
PXE boot selection instead falls back to the OS default. Thus 6.12.113 is the
source-representative default/fallback test kernel; neither the committed
configuration nor this test establishes actual live node kernels.

Both cgroup v1 and v2 are configured in production. For example prg/node19 (v1)
and prg/node21 (v2) share the same AMD/1t profile imports, so the mode difference
cannot be dismissed as an obsolete predecessor. Use this as source evidence for
two modes of one focused scenario, not as proof of live topology or a reason to
reproduce the nodes' entire hardware/tuning configuration. The source package
below is selected; machine queries, fetching, evaluation and runtime remain
unselected.

The default test catalog still includes the historical upgrade cases with the
`ci` tag. The existing CI workflow triggers on affected source/test pushes and
pull requests and selects the unfiltered `ci` tag by default. The no-historical-
boots direction therefore also constrains future automatic CI selection and
publication planning; a local VM hold alone is insufficient. No CI cancellation,
workflow edit or deletion of historical test registrations is selected here.
Lead must resolve that scheduling boundary before a publication that triggers
these cases.

#### Selected source package and proposed minimum runtime validation

The lead assigned owner3 the four-path source package below. It prepares one
native production-origin impermanence scenario with two existing-template
instances, cgroup v1 and v2, for separately selected serial execution. Boot the
exact current-production OS 2ab stable/default 6.12.113 tuple, create one
impermanent NixOS container, then activate the exact reviewed candidate
userspace while retaining the booted kernel and running container. Explicitly
identify candidate configuration/profile and packaged osctld bytes; do not
inherit an unstable CI override or use frozen 846bb as the target. This is a
test of the configured production source boundary, not a deployment inventory
or live-kernel-equivalence test. It boots neither historical 3cc nor 3cb.

The one-container flow has these acceptance points:

1. Create known persistent and ephemeral payloads under the production writer.
   Use a supported no-CPU-assignment setup so an incidental scheduler save does
   not mask the defect. Observe, without rewriting YAML, valid saved run ID,
   stale BASE/cleanup-false, unique same-ID GC TEMP owner and authenticated live
   private-root/process identity. If this state is absent, report that the run
   did not cover stale-state repair; do not synthesize it or silently retry.
2. Switch once to candidate userspace. Require the same running init birth,
   namespace/root, ZFS identity, GC owner and both payloads, with only the saved
   dataset/cleanup selection repaired. One ordinary candidate daemon reload
   must preserve this now-correct selection and live state without a rewrite.
3. Restart that container under the candidate. Before configuration/readiness
   setters can save state, require a new ID/TEMP already persisted, unique GC
   ownership, persistent payload retained and old ephemeral payload absent.
   Create a new ephemeral marker, reload only the daemon once, and require the
   new run/root/owner and payloads unchanged. Verify normal old-root retirement
   and final native stop/cleanup. No general activation/rollback matrix or
   additional distro/nested workload is part of this scenario.

The supported no-assignment setup is per-container: after creating/importing
the stopped impermanent guest, run
`osctl --pool tank ct set cpu-package niximpermanent none` before its first
start. Finish start-menu, networking and other configuration setters while it
is stopped. Keep `none` through the candidate restart. Exact 2ab CLI accepts
this value; `CpuScheduler#assign_package_for` returns without an assignment,
so `schedule_ct` does not perform its conditional run-configuration save.
This needs no global scheduler disable, artificial CPU topology or host-profile
override. Require public `cpu_package_set == "none"`, null
`cpu_package_inuse`, and null raw runtime `cpu_package` after start. Sample the
actual stale selection before any post-start configuration setter; ordinary
`ct exec` payload writes need no such setter. The same setup makes the later
candidate-writer assertion independent of an incidental scheduler save.

Retain the existing focused writer/reader/publication/GC race/refusal units as
the failure-path coverage. Custom boot remains unit-only until separately
selected; no new image lookup follows from this design. A candidate-only
fresh-start/reload run is also useful if no production baseline boot is allowed,
but leaves production-to-candidate runtime continuity explicitly unverified.
Do not replace missing runtime proof with the unrelated container-module
generation test `dist-config/nixos-persistence-upgrade`.

The selected application boundary is one focused native test template,
`tests/suite/upgrade/production-impermanence.nix`, its two registrations in
`tests/all-tests.nix`, and a short owning explanation in `docs/os/testing.md`.
Use the existing test-template/RSpec machinery; no new runner API, generic
capture framework, production pin or configuration-repository edit is needed.
Port only the useful held raw-state/ownership assertions from owner3's preserved
work. Do not repin `common.nix` or run its unrelated guests/activation breadth.
The lead permits owner3 to remove only its own 216 held common insertions after
verifying the frozen backup, leaving a historical tag-only net change. The
backup and completed-check evidence must remain intact. Historical scheduling
and the focused scenario are separate logical owners.

To preserve historical coverage without default execution, move the
23 existing `upgrade/from-6.12*`/`from-6.18*` registrations into one conditional
list enabled only by `VPSADMINOS_ENABLE_HISTORICAL_UPGRADE_TESTS == "1"`.
In historical `upgrade/common.nix`, use `upgrade` and `manual` tags rather than
`ci`; a new production template has its own ordinary `ci` tag. The existing
diagnostic opt-in remains separate. The environment gate removes historical
cases from default unfiltered discovery; the manual tag also prevents ordinary
`-t ci` from selecting them when discovery is explicitly enabled. Preserve all
historical wrapper pins and source. This needs only catalog/tag/documentation
changes, not a CI workflow rewrite or a default change to the runner.

Quick checks must prove default discovery and `ci`
selection exclude historical cases, the explicit opt-in exposes them as manual,
and the focused template has exactly the two selected cgroup instances. Run
normal syntax/lint/hooks and focused actual assertion checks before commits and
whole-branch final review. Metadata/cache graphs, actual RAM/SHM/all-disks/store
forecasts and exact candidate bytes precede any separately selected runtime;
unplanned kernel builds remain a stop. The source package is authorized; test
evaluation, Git operations, builds, publication and VMs remain unselected.
Historical execution remains held. Publication and unfiltered CI remain held
until both historical selection exclusion boundaries are proven and the lead
selects the next operation.

#### Exact source acceptance checkpoint

Architect0 accepts owner3's completed four-path source package against
`repair/support/production-quick-checks.json`: production template SHA256
`183f4815158457da9fcca2f2576c7809aa8b8f6838d3838a60e0a4c7843d7be9`,
catalog `cf3b7c561fdad25a8272d2ce462ef10baa51e8c8712cfba89103c5409dbe0e0d`,
historical common `bebb502682621e712b7df48c29904a7c0beff6608d88f1abd0e4d2baae889035`,
and full documentation
`bbf4279e3075372a390ae5ed84ef33f1affbcf4a30220622614edbb2ce3c9215`.
The 38 focused source checks, 41 static checks, embedded Ruby lint and Nix
parse/format receipts apply to these unchanged bytes. The daemon reload check
uses the robust process-stat birth parser, including names containing spaces.

The corrected commit variants also pass direct inspection. Historical no-peer
documentation is `79d72cc0637890bc1d096dcab4a85ba8470642d817b1cfafad346cd6151a5f70`;
production no-peer documentation is
`dd1b0d4adfdf2fc179777f19aa42ad14c31eb7e4cbb0a3e8360d0b16d963ea00`.
Each corresponding peer variant differs by exactly the accepted 20-line hotplug
insertion. All four preserve the complete baseline documentation suffix from
the existing shutdown-diagnostics heading. The earlier truncated packet
variants are superseded by `production-packet-correction.json` and the updated
`production-commit-packets-sha256.json`; shipping source did not change.

This is design/source acceptance for the lead's two-owner commit selection,
not independent final review or execution approval. Native discovery must use
a separately frozen clean committed source, with strict dirty/head guards and
a selected bounded supervisor; peers' dirty files do not justify weakening
those guards. Production/candidate service, wrapper, resolved gem, source and
realized four-file byte comparisons in `production-package.md` remain mandatory
before any VM. Git-only prerequisite hashes were checked against both exact
revisions; they do not establish realized package equality. Publication remains
held until native discovery proves both historical exclusion boundaries.

The accepted source is now committed as historical scheduling
`595bafea97f31aab3c34438db3f64fca78a9e94b` followed by focused production
validation `4de50f0046052d377780a3be3a9aeec37ad86f6e`. Architect inspection
confirmed the retained isolated checkout is clean at that head and its four
committed files match the accepted variants, including documentation without
the peer hotplug insertion. Owner3 reported both Git windows released.

The frozen discovery package prepared for lead selection is in
`repair/support/production-discovery-ready.md` and `.json`; all listed hashes
were checked. Its guardian caps retained stdout/stderr and checks readable
members of the native process group. It records permission gaps without
refusing solely on those gaps, and does not prove absence of escaped own
references. The separately selected watcher must reconcile actual child
identities and exact owned argv/cwd/root/fd references after results, errors,
cancellation or guardian loss, retaining uncertainty rather than treating an
empty group or guardian exit as effects ended. The 300/90-second deadlines
request authenticated INT and escalate after five seconds without automatic
TERM/KILL; they are not completion guarantees. The 2-GiB shared-free-space
decline is explicitly not an owned-allocation quota: foreign frees can mask
growth. These qualifications remain part of lead admission; no native query,
publication or VM was launched by architect inspection.

The lead subsequently selected that discovery operation once. All three native
catalog queries exited zero, but the Ruby checker failed before completing the
selection gate: the projected source identity attributes contained `outPath`,
which Nix JSON serialization coerced into store-path strings. All three retained
results name the same candidate and production source paths; revision, NAR and
lock/input records were not retained in those identity objects. This is an
observation-format failure, not completed selection proof.

Owner3 owns the narrow correction and final effects reconciliation. A separately
selected identity-only projection should use a non-special `sourcePath` or
`storePath` field at both source and nested input levels, authenticate exact
4de/2ab revisions, and bind its paths to the strings in all three retained
results. The native selector must then consume the original names/tags and
supplementary identity evidence. Do not repeat the catalog queries or remove
identity checks to obtain a pass. Publication remains held while this proof
and reconciliation are incomplete.

Architect inspection accepts the prepared identity-only query/checker in
`repair/support/identity-supplement-frozen.json` for lead selection. The query
uses ordinary identity keys and binds exact revisions/source paths; the checker
retains raw-catalog hashes, complete lock equality, root input coverage and
native tag selection. Hash-verified lock bytes from immutable local Git avoid
depending on a source store path after client exit. The candidate store path's
reported disappearance has no established timing or cause, and forcing input
identities may fetch sources not forced by the original coerced records.
The shared-free-space qualification therefore remains relevant.

Before the prepared combined effects scanner supplies final reconciliation,
its read-only observer exemption must reject coreutils command-dispatch
overrides as well as matching executable and invocation name. Those overrides
can change the operation represented by a familiar read-only alias; absence of
a writable descriptor does not establish a read-only operation. Owner3 owns
this bounded scanner refinement and inert classification checks. It does not
require changing the frozen identity query/guardian or repeating catalogs.

The selected identity-only query subsequently failed once, before its checker:
native exit 1 after 1.369 seconds, because the local candidate flake did not
expose `rev`. The earlier source acceptance of that assertion is superseded.
Nix documents revision metadata as present only when applicable; an absolute
local source reference is not sufficient commit attestation. This failure does
not invalidate the retained catalogs or supply their missing identity proof.
Owner3's corrected `a8bbbeb2` scanner then found the original four and new one
child identities absent, with no remaining groups or readable canonical own
argv/cwd/root/fd references. Its 674 permission gaps remain a qualification;
architect did not repeat the scan.

The minimal supported correction for a separately selected identity operation
is an explicit immutable local Git reference:

```text
git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-production-commit?rev=4de50f0046052d377780a3be3a9aeec37ad86f6e
```

Use this only to supplement the original catalogs, not to evaluate them again.
The native Nix 2.34.9 manual documents this reference form, Git revision
metadata and the NAR hash of the resulting source tree. Keep the original
absolute source directory as the supervisor's literal clean-checkout binding;
construct the Git reference separately for `builtins.getFlake`. Owner3 owns
the narrow query/checker/supervisor correction and quick inert checks.

Acceptance requires all of the following, without a fallback that relaxes them:

- Before and after the query, local read-only Git checks establish HEAD
  `4de50f0046052d377780a3be3a9aeec37ad86f6e`, actual tree
  `e5e074bad8c74a27eb3dc422e44cb8e08389a245`, empty staged and unstaged
  differences, and no nonignored untracked files. Preserve the same literal
  source directory and existing source/hash/session guards. Git inspection
  disables lazy fetching; no checkout, ref or source edits are part of this
  operation.
- The native Git flake must report that exact revision, a SHA-256 NAR identity,
  and source path `/nix/store/vp408cmsdyd625lcrr4kizrn7rklzm7j-source`.
  Require exact source-path equality before forcing the full input projection.
  This connects the immutable commit's content-addressed source to the path
  retained by all three original catalog queries. Do not inject a claimed
  revision, accept null revision, or accept a different source path. If Git and
  the original source select different bytes, stop and diagnose that difference;
  do not silently substitute a new source graph or repeat the catalogs.
  The original catalogs retained no NAR hash: record the native supplement's
  actual hash, without claiming a direct comparison with an earlier recorded
  hash. No extra archive, export, realization, root creation or full-tree copy
  is required for this content-address binding.
- Keep exact production revision `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`
  and `/nix/store/96g5h6c9kzwsr3n1cgsvzyq44wzyzixa-source`, complete lock
  comparison against the retained immutable Git bytes, and the existing full
  root-input projection. Use ordinary `sourcePath` keys at both levels. Do not
  require a later reread of source paths that may be unavailable after exit.
- Hash-check the three original catalogs and run the native tag selector only
  over their retained names and tags. A successful supplement proves identity
  for that exact 4de discovery checkpoint. It does not prove realized daemon
  bytes, the final later candidate head, a machine configuration or runtime.

Preserve both failed attempts and their effects receipts. Prepare a distinct
attempt with the existing bounded stream/deadline/space supervision and final
canonical-reference reconciliation; no automatic retry, catalog query, build,
VM, source fetch expansion or cleanup is selected by this design. Source/input
fetches inherent in the proposed identity projection still require the lead's
bounded operation selection. Keep the 120-second total, 90-second query,
5-second checker/reap limits and 2-MiB stdout plus 1-MiB stderr caps. The
40-GiB free floor and 2-GiB shared-free-space-decline guard do not establish a
cumulative owned-allocation limit; exact new source/input allocation remains
unknown. A differing path, revision, NAR, tree, lock or
input contract fails closed and retains evidence. Quick preparation must cover
missing/wrong native revision, wrong source path/tree, changed source before
or after the query, and unchanged retained catalog bytes. Publication remains
held pending actual identity and native-selector acceptance.

Architect inspection of the prepared immutable-Git package receipt `d032cf5f`
verified all ten listed file hashes and the intended query/checker/scanner
boundaries. One supervisor finalization defect must be corrected before source
acceptance: after catching a failed post-query source check, it rereads the
source lock outside that catch while constructing its final receipt. A missing
or unreadable lock would suppress the receipt and its native child identities.
Reuse the captured source-state hashes, retain the post-check failure and
nonzero outcome, and add an inert finalization case for the unavailable lock.
This changes failure reporting only; the strict identity requirements and both
prior attempts remain intact. No query or live effects scan is selected by the
inspection.

The finalization correction is source-accepted at guard `2edb8bad` and receipt
`de75a626`: captured lock hashes and separate primary/post-source errors preserve
the child receipt and nonzero result when the source disappears. Four inert
actual-finalization checks cover the failure and reproduce the old lost receipt.
The lead then selected the immutable-Git query once. Revision 4de passed, but
its actual source path was
`/nix/store/inmh3a3yx9kpxixks36g837pq6a0a567-source`, so the exact `vp408`
assertion refused and the selector did not run. All six recorded child
identities were subsequently absent with no readable canonical own references;
713 permission gaps qualify that effects report.

Owner3's read-only layout comparison found the materialized Git source matches
all 2400 immutable 4de blobs and executable modes, with no extras. The isolated
checkout matches those files and has only its `.git` pointer as an observed
extra. Original `vp408` is unavailable, so neither its content nor a `.git`-only
explanation of the hash difference is proven. Preserve both distinct source
paths, all failed receipts, the original catalogs and this qualified diagnosis.
The lead explicitly stopped reconstruction of the vanished checkpoint: do not
prepare or run the proposed native NAR/hash reconstruction or another supplement.
After remediation and the new final head, the lead may separately select fresh
native discovery of all three gates once from an explicit immutable Git source.
Do not claim equivalence or identity acceptance for the old catalogs. Publication
remains held, and final packaged-source/input/realized-byte proof stays separate.

### Final f746 immutable-source selection checkpoint: preparation selected

The lead selected source-only design and owner3 preparation for the actual final
candidate `f74629fa4046089e2c53d0cb0e3ba7ef5b178e82`, tree
`1bbd234662cbe595e781dcba4c0b43c5a839f15e`, parent
`39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17`. Read-only Git inspection confirms
these identities. The primary handoff attained this state despite its native
batch exit1; the cache-tree assertion failure and mutation were reconciled and
the lead released the Git window. Do not retry that operation. The first seven
owners are unchanged; the lead's narrow recorder-remediation disposition and
accepted C55a/docs e7d/PASS73/rnaq-to-lpz compile/selected CLI evidence stand.
This package neither reopens product review nor repairs incomplete monitoring.

**Only preparation is selected.** Every native metadata evaluation, tool plan,
substitution and selector execution needs a separate lead selection after its
literal frozen package is inspected. The lead has selected the metadata-only
resource allowance below for preparation and possible later bounded admission;
this does not select native execution or tool materialization. Owner3 owns
new session-local preparation under
`repair/support/final-head-discovery-1/`; architect0 owns this design. No product,
runner, workflow, recipe, lock, history, old helper or old receipt is editable.
No new framework, catalog, registration layer or source worktree is needed.
Preserve the dormant `repair/support/final-head-discovery-proposal.md` and stopped
4de evidence. Neither `vp408` nor `inmh` is an expected final source path, and
their equivalence remains unproved. No old catalog becomes final proof.

After same-session binding and roster32 ready/workspace-write verification,
architect0 delivered this source-only assignment to implementer3 with message
`19190dc4-682f-4e1d-acfb-290f2da4b221`, acknowledged by receipt
`01a16b6d-1fbd-7a22-b233-f3b82501d0b6`. Saved member settings were unchanged.

#### Exact origin, native projections and selection predicates

Use the existing primary checkout as the literal read-only Git origin:

```text
git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos?ref=refs/heads/2026-10-22-ci-failure-analysis&rev=f74629fa4046089e2c53d0cb0e3ba7ef5b178e82
```

Both session guards and pre/post read-only HEAD/tree/branch/cleanliness checks
must agree. Disable Git lazy fetch and optional index writes. Pin the branch
explicitly instead of relying on Git's default-ref discovery; `rev` remains the
immutable authority. Do not accept a path-flake's missing revision, dirty source,
declared revision, moving HEAD, changed lock or a different selected source.
Preparation binds the expected bytes directly to immutable f746 Git objects.

The metadata query imports that native Git flake's `tests/all-tests.nix`, with
its own `inputs.nixpkgs.outPath`, `system = "x86_64-linux"`, `configuration = null`,
and the existing default suite/test/framework arguments. Preserve the accepted
lazy projection: all catalog names, plus each `upgrade/` entry's test-level tags
and every script's tags. Do not force `.json`, machine resources, rendered test
bodies, target toplevels or closures. `test-runner/nix/lib.nix`'s full metadata
projection includes resources and is unnecessarily broad here. This is a
projection of the actual catalog, not a replacement catalog or synthetic test.

For each of the three serial native queries, unset these ten controls first:
`VPSADMINOS_ENABLE_LIVEPATCH_TEST`, `VPSADMINOS_ONLY_LIVEPATCH_TEST`,
`VPSADMINOS_LIVEPATCH_SINGLE_SERIES_MODULE`,
`VPSADMINOS_ENABLE_SCHED_PROXY_EXEC_TEST`,
`VPSADMINOS_ONLY_SCHED_PROXY_EXEC_TEST`,
`VPSADMINOS_ENABLE_SCHED_PROXY_EXEC_LOCK_BADNEIGHBOR_TEST`,
`VPSADMINOS_ONLY_SCHED_PROXY_EXEC_LOCK_BADNEIGHBOR_TEST`,
`VPSADMINOS_ENABLE_HISTORICAL_UPGRADE_TESTS`,
`VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS`, and `VPSADMINOS_CONFIG`.
Do not print arbitrary inherited environment or use a shell hook. Record the
selected controls, literal argv, source identity, stdout/stderr and native exit
for each gate once; stop on failure without repeating successful catalogs.

| Gate | Only additional control | Required native result |
| --- | --- | --- |
| Default | none | No historical or diagnostic name; the complete upgrade-name set is exactly `upgrade/production-impermanence@v1` and `@v2`. |
| Historical | `VPSADMINOS_ENABLE_HISTORICAL_UPGRADE_TESTS=1` | Default names plus exactly the 23 strings in f746 `all-tests.nix`'s historical block, no removals or diagnostic cases. Every historical script is `upgrade`/`manual` and rejected by native `ci`. |
| Diagnostics | `VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1` | Default names plus exactly `upgrade/from-6.12-guests-first-switch` and `upgrade/nested-podman-sandbox`, no removals or historical cases. Every diagnostic script is manual and rejected by native `ci`. |

Both production cases must have nonempty scripts, combined `upgrade`/`ci` tags
and native `ci` acceptance in all three gates. Check complete upgrade sets and
exact differences, nonempty script coverage, string/list types and duplicate
names; extra or omitted entries fail. The Podman diagnostic need not carry
`upgrade`: its actual source has only `manual`. Do not import old total counts
167/190/169 as final observations. Freeze the 23 expected names from the current
committed block; the old restoration manifest is only a comparison source.

Run the actual final-source `TestRunner::Cli::TagFilters.new(['ci']).pass?` on
the new native metadata. Load the hash-bound final `test_script.rb` as well so
its existing `TestScript` initializer supplies test+script tag concatenation;
minimal metadata carriers supply only the other constructor fields. They must
not replace either native selection method or invent input tags. Require the
actual checker to consume all scripts in all three new JSON files and retain
its per-script decision/exit. Pure fixtures or static grep do not pass this gate.

Committed SHA256 bindings checked independently during this design:

| Path | SHA256 |
| --- | --- |
| `tests/all-tests.nix` | `cf3b7c561fdad25a8272d2ce462ef10baa51e8c8712cfba89103c5409dbe0e0d` |
| `tests/suite/upgrade/production-impermanence.nix` | `183f4815158457da9fcca2f2576c7809aa8b8f6838d3838a60e0a4c7843d7be9` |
| `tests/suite/upgrade/common.nix` | `bebb502682621e712b7df48c29904a7c0beff6608d88f1abd0e4d2baae889035` |
| `test-runner/lib/test-runner/cli/tag_filters.rb` | `e7959116ed4822fbb09d52e9cb8866f124fc9c32abafeee6b05518b3e7ec1f43` |
| `test-runner/lib/test-runner/test_script.rb` | `0998d3351e8a65c0aefd27237fddb11fdee6f91b4c6f59e50d799ff7bd7528e3` |
| `flake.nix` | `3912bd79c5ce127c9bbd646d46bad234d1266e51163ba1558ccfde5552a6de3b` |
| `flake.lock` | `fd0361f861091aa982959b422df27e76748ee26946923cdbd9ef2509b7474be1` |

#### Copied source, lock graph and provenance boundary

In every gate use ordinary `sourcePath` keys at every record level: never emit
an identity object with special `outPath` serialization. Require actual native
candidate revision f746, source path and SHA256 NAR identity. Retain actual
values instead of predicting a final store path. Candidate and production
identity/lock/input records must agree across all three gates. Bind actual
materialized candidate file content, symlink targets and executable modes to
all 2404 immutable Git entries, with no missing/extra source files; `.git` is
not part of this exported source. Keep the native NAR separate from Git tree
and ordinary file SHA256 identities. No custom NAR reconstruction, source
archive/export or equivalence normalization is needed. Missing materialized
source or failed byte comparison refuses; it does not authorize restoration.

Require production revision `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`, its
native source path/NAR and exact full lock bytes SHA256
`1f40189015dddb525ff76687908f056e4757a0d57a485c309c40a8bb9ce91ad2`.
This lock and candidate lock were independently rehashed from their immutable
Git objects. Retained lock copies may supply expected bytes after verification;
they do not supply a new native source identity. Read/hash the native source's
lock while available and retain evidence; do not add a late unguarded reread
that can erase the primary error or child status.

Project the complete native candidate and production input graphs, not just
five root input names. Each has seven locked nodes: the five root inputs
`impermanence`, `netlinkrb`, `nixpkgs`, `nixpkgsUnstable`, `ruby-lxc`, plus
`impermanence.inputs.home-manager` and `impermanence.inputs.nixpkgs`.
The last is distinct from root nixpkgs; home-manager's nixpkgs follows it.
Compare full root lock JSON/bytes, node sets, original/locked records, edges,
`flake=false` flags and follows resolution. Every resolved native node must
have its actual source path/revision/NAR equal the matching locked rev/NAR;
the follows alias must resolve to the same identity. All these locks have
concrete revisions, so null/missing revisions are failures, not a general
fallback for non-flake inputs. Use this fixed native input projection, not a
new resolver or registry. Do not silently substitute root nixpkgs for the
impermanence dependency or drop unused declared candidate/production inputs.

The opt-in tag queries also import frozen predecessor test constructors from
3cc31e39ba2880a311a1a5889521d2bc0d7e3e0f and
3cb830e596a7fed900bec49f50c9b6cf51e76bb5. Account for those metadata source
imports with native revision/source/NAR and complete lock bytes in the gates
that need them; do not force them in default merely for symmetry. Their tags
are evaluated using the catalog's supplied candidate nixpkgs. Distinguish
those constructor imports from their unforced machine/build/input outputs.
The diagnostic's frozen 846bb activation target and via-6.18 activation source
remain source declarations, not evaluated runtime identities in this projection.
Do not fetch/evaluate those targets just to enlarge the proof. Any additional
source forced by the bounded projection must be named and explained before
acceptance; an incomplete graph is not silently labelled complete.

This proves the final catalog and selected native tag semantics at a specified
source/input graph. It proves neither test image/profile closure nor packaged
osctld contents. The template's store-path candidate reference is content-bound
by the final exported tree; no separate path-flake revision attestation is
invented. Later preparation must still prove production/candidate service ->
wrapper -> bundle/GEM_PATH/gemspec -> unique selected gem/closure and exact four
changed realized files. Production stable6.12.113/cgroup v1+v2 remains configured
source evidence, not live-node/kernel inventory. No historical boot is selected.

#### Small execution packages and proposed finite envelope

Prepare these dependencies without executing any of them:

1. **Metadata:** one fixed query and a literal driver for the three serial
   projections, plus source/input/lock checks and raw receipts. The existing
   retained Nix client is
   `/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix-instantiate`.
   Its argv is `--eval --strict --json --option allow-import-from-derivation
   false --option builders '' --option fallback false --option max-jobs 0`,
   then absolute `repair/support/final-head-discovery-1/catalog.nix`, then
   `--argstr source` and the complete immutable URI above. The empty builders
   value is one empty argv element. Freeze expanded absolute argv/environment
   arrays in the packet. IFDfalse and zero builders/jobs forbid realization;
   native source materialization/fetch remains possible and must be budgeted.
2. **Tool-only contingency:** prefer the retained Ruby3.4.9 executable
   `/nix/store/m0nfdb4mhfgwkgss4ymyqmvviwy30i6y-ruby-3.4.9/bin/ruby`
   with its JSON/default-library closure, loading only the two authenticated
   final Ruby source files. Fresh later admission must verify availability;
   prior use is not a cache guarantee. If unavailable, stop. Owner3 may prepare
   a separate exact tool-only derivation/closure/dry-run proposal from retained
   identities; missing metadata or insufficient margin returns to lead. Do not
   run `nix develop`, realize the runner/dev shell, install gems or automatically
   substitute tools. Any later substitution must have a separately accepted
   exact allowlist/forecast, zero source builds, max-jobs0/builders empty and
   fallbackfalse. Kernel/ZFS/SDK/compiler or unrelated sources are prohibited.
3. **Selector:** the literal Ruby command loads the final-source checker and
   consumes only the new hash-bound catalog/identity files. If tools are already
   authenticated, this may be the last five-second command of the metadata
   batch. Otherwise retain completed metadata and select the tool/checker step
   separately; do not repeat the three queries. No full runner or VM is needed.

Recommend the existing 300-second overall discovery envelope, at most90 seconds
per Nix query and5 seconds for the selector, including source checks in the
overall deadline. Five seconds after requested authenticated cancellation is
an escalation threshold, not proof of termination. Reuse a fixed accepted
control pattern for this one operation, preserving originals; do not develop
a monitoring framework or repair historical guards. The fresh catalog Luna/low
utility owns the sole launch/handle and observations. Lead selects the exact
frozen operation and utility separately; owner3 must not launch a second watcher.

Retain client hard1GiB/noSwap, sampled whole exact daemon+actual client current
<=8GiB for admission and >=12GiB for cancellation, and strict fresh host
MemAvailable >=20GiB admission/<16GiB cancellation. No baseline subtraction,
protected builder PID/RSS, hard aggregate, reservation or unsampled peak claim.
Use aggregate retained stdout16MiB/stderr4MiB, plus at most12MiB for bounded
source manifests, samples/status/effects, within32MiB total. Include utility
logs in this ceiling; cap its own emitter separately and continue draining
pipes after cap refusal. No finite RLIMIT_FSIZE or uncontrolled shell trace.

Retained disk evidence, without a fresh capacity query:

- [Recorder assessment](repair/hotplug/recursion-build-1-owner-assessment.json)
  `eb45e8c2` / [raw bundle](repair/hotplug/recursion-build-1-owner-retained-data.json)
  `7befcab3`: cumulative positive
  shared decline3465981952B, 98 named maxima totalling1534898176B, last actual
  guard sample free135133073408B. `result.last_retained_free`136250007552B is
  its earlier input anchor, not its end sample.
- [Fold assessment](evidence/impermanence/owner8-recursion-fold-v2/owner-assessment.md)
  `aa0d1cd6`: free136643362816 ->136639381504B, decline3981312B.
  The preceding observed increase gives no refund.
  [CAS assessment](evidence/impermanence/owner8-recursion-fold-v2/primary-handoff-v1/owner-assessment.md)
  `564b3f6e`:
  free136633495552 ->136627523584B, decline5971968B.
- The positive gap between fold end and CAS start is5885952B and must also be
  charged. Thus carry is **3481821184B**, leaving **813146112B** under the existing
  4294967296B stop. All unsampled/interstage movement remains unknown, and none
  of these shared changes is attributed to our operation. The latest anchor
  is136627523584B. Preserve all98 maxima and later retained named-path maxima;
  grow the ledger monotonically without clearing/refunding old entries.

**Selected by the lead after reading this complete design:** use512MiB
(536870912B) as a metadata-only planning allowance, retaining the4GiB cumulative
stop and separate4GiB known-subset stop. This applies over the whole metadata
operation without resetting the allowance or ledger between gates. Execution
and any tool materialization/substitution remain unselected. The original
planning rationale follows unchanged. The last measured final isolated tree
allocated347021312B; one new source-sized materialization plus32MiB evidence
leaves156295168B within that allowance. This is planning arithmetic, not a
copy/fetch peak bound: temporary copies or missing nixpkgs/input sources can
exceed it. No present source/cache availability is assumed. The retained
remainder leaves276275200B beyond the allowance before any new observed gap.
The former2GiB recorder-build allowance cannot fit and is not silently reused.

Before Popen and again before metadata/FIFO admission, charge the positive gap
from the latest retained endpoint, refresh named maxima, and require
`charge + 536870912 <= 4294967296`, free>=43GiB, known subset<4GiB and all strict
identity/RAM/log predicates. Charge every later sampled decrease; increases,
deletions, deduplication, foreign frees or GC never refund carry. Runtime
charge>=4GiB, known subset>=4GiB or free<40GiB requests authenticated own-client
cancellation. The read must precede a fresh startup-deadline check. A tool plan
must fit the then-remaining allowance with explicit margin;512MiB does not
authorize any tool fetch. If source/input materialization or tool planning
cannot fit, hold and return the exact need to lead. No automatic ceiling rise,
polling, GC, cleanup or retry follows. Hidden/past allocation stays unknown;
neither ledger nor shared decreases proves a complete owned quota.

#### Completion, preparation acceptance and later gates

Reuse the established ownership rules: actual launcher/timeout ancestry, exact
argv/executable, PID+birth and named invocation/cgroup inode before admission
or cancellation; no name/timing guesses or assumed systemd forwarding. PGID
change leaves the same PID/birth live. Signal only the authenticated own native
timeout, never a daemon/guessed builder/foreign reference. Missing identity,
escaped/unknown liveness, persistent errors or deadline breach preserves the
handle, primary failure and bounded escalation. Pending startup is limited to
the exact accepted unbound tuple and existing five-second deadline; it never
clears failure or reopens after binding. Every setup/finalization error must
retain native status, independent pipe progress and evidence.

Both outcomes require the selected bounded readable canonical argv/cwd/root/FD
reconciliation plus fresh native/known-birth/named-scope/canonical-cgroup/BOTH-EOF
reconciliation after it. A nonself positive actual PID/birth remains observation-
only liveness, not signal authority. Unresolved positives, overflow or missing
identity hold and escalate; do not abandon them or repeat broad scans. Preserve
protected/FD/argv/race/nonatomic limitations. Native success, selector success
and monitoring completion are separate fields. Old monitoring remains INCOMPLETE.

Owner3's frozen source-only return must include exact commands/hashes, bounded
driver/control diff against its reused pattern, fresh literal operation paths,
query/checker/source/lock/input bindings, ledger with the added5885952B gap,
preservation proof and an explicit list of still-unselected operations. Prepare
checks for wrong/missing revision/NAR/source/lock/node/follows, special outPath
coercion, unexpected names/script-level ci leakage, changed copied bytes,
missing tools, positive-gap/no-refund/allowance equality and failure retention.
The lead now permits owner3 only cached Bash `-n` on proposed Bash files,
Python AST parsing of source/embedded code, and hash/mode/preservation/static
binding inspection as source preparation checks. Do not execute a validator,
observer, selftest, inert suite, Ruby helper, Nix parse/eval/query, probe or
native selector. Prepare exact small inert/native command proposals for a
separate lead selection. No architect checks or implementation takeover is
selected by this update. Synthetic checks, if later selected, remain
preparation evidence only.

There is no persistence/API/ABI/deployment change or rollback action in this
package. Failure retains source, roots and receipts without replay or cleanup.
Publication/unfiltered CI/default integration/deployment/runtime remain held.
The later one-container production-v1/v2 campaign, full machine/cache/closure
admission and actual service/gem byte proof are dependent gates, not implied
execution. The lead owns state/handoff integration; this design records the
architect milestone without changing the session lifecycle.

#### Frozen final-head-discovery-1 source assessment: acceptance withheld

Architect inspection of [the prepared package](repair/support/final-head-discovery-1/ready.md)
is complete. This is source acceptance, not mandatory product review or native
proof. All23 frozen file byte/mode/size bindings and16 preserved originals match.
The inspected identities are:

- Frozen manifest: `8c1147da1b5398eeb9d50d9a5b0aac07bf2f6c1d51e8b39b8af29bad623c2fdb`.
- Receipt: `ada2d0d837e9ab7397f23e7557f28e0c9945f9b3cb069d17a12527d41361569c`.
- Observer: `c8f9873fe1c1aefcac5b67323c202a96b910f8b35c91df39b02b1747e62802a8`.
- Driver: `f3d5a699becbe46674e4156dec7e4565b4f76457153b74bf8d88ed156d4c87a2`.
- Catalog: `1285be3574d20a0f755e275b64b127cde5734e26c54d1061c47972ba1dccc96b`.
- Checker: `b82015b34bfba6be06746b204ce1559b78bf077047013efc6b105a832f2b6d22`.

The source/selector boundary fits the selected design: immutable f746 URI,
three separate gates, every projected script passed through final TestScript
and TagFilters, exact production2/historical23/diagnostic2 expectations, complete
candidate copy comparison and full candidate/production locks with seven native
nodes/follows. Both predecessor constructor roots are confined to opt-in
metadata. The2404 manifest entries match immutable Git paths/modes/blob IDs
(2343 regular,56 executable,5 symlinks); all four frozen root locks match their
immutable Git bytes. No old4de catalog/path identity is reused as proof.
Fixed argv/environment and source-only tool identities are explicit. These are
source conclusions; no native NAR/source/selector result exists yet.

The ledger retains carry3481821184B, endpoint136627523584B and all98 original
maxima1534898176B; eight later maxima bring the named total to2680176640B.
The512MiB allowance, positive-gap/no-refund arithmetic,4GiB stops,43/40GiB free
space,8/12GiB shared-service sum,20/16GiB host availability and hard client1GiB
with no swap remain selected. This inspection creates no fresh capacity/cache
evidence. The276275200B planning margin can disappear before admission; the
same lifetime allowance remains required at each phase, without a reset.

Four concrete correction groups prevent acceptance. **The lead has now selected
exactly these four groups and the two accompanying admission/evidence details
below for owner3's source-only correction.** The original findings and frozen
identities remain the inspection baseline. Owner3 must preserve all23 original
files, modes and hashes, including frozen.json and receipt.json, before edits.
Frozen line numbers below refer to the files above, not to a replacement.

1. **Pending startup RAM sampling:** `observe.py:365-366` requires canonical
   cgroup absence for every non-active state. The retained exact
   loaded/inactive/empty-invocation/empty-ControlGroup startup-pending state
   legitimately permits a present tentative cgroup (`scope_kind:48`,
   `inspect_scope:302-339`). It therefore fails immediately in the new sampler.
   For only that accepted unbound state, validate/count its tentative memory
   and retain observed children without binding or admitting. Zero client
   charge requires actual cgroup absence. Keep the five-second limit, prior
   failure latch and all post-binding refusals unchanged.
2. **Serial child retention and finalization:** `driver.py:144-176` leaves
   loop-condition poll, cadence, wait and final clock/poll outside the guarded
   child-control paths. An exception can exit with the original child live;
   final clock/poll errors can skip closes/status. Sink-close errors are merely
   recorded after the success assertion, so a stderr flush/close failure can
   still permit the next gate and overall success. Keep that same Popen and
   independent drains until actual exit and both EOFs, including control
   errors. Guard final steps independently, attempt all closes, preserve the
   primary and native status, and make every close/receipt failure fail closed
   with no later query. Do not add driver signal authority or another launch.
3. **Persistent clock error bypasses escalation:** after guarded clock reads,
   `observe.py:461-462` calls the clock again before the `clock_failed` branch.
   A persistent failure reaches the outer catch every iteration, bypassing
   cancellation, fresh liveness reconciliation and the one-shot escalation/
   effects path. Derive deadline decisions from a guarded fresh observation;
   unavailable time must reach sticky failure/escalation without requiring
   another successful clock read. Continue drains/liveness with the retained
   handle. Keep the existing300/90/5/+5 limits and one signal/scan attempt.
4. **New effects inputs must not defeat reconciliation:**
   `observe.py:524-542` parses optional started/batch/raw metadata before the
   base scan. A capped/truncated raw JSON can have native exit0 and still abort
   all-readable scanning. Retain the parse error and incomplete-reference
   qualification, but attempt the one base scan using fixed references and
   every valid observed identity. Separately, query timeout births added at
   `524-528` exist only in the scanner's local set. `effects_once:416-417`
   latches a surviving query birth without retaining it for later liveness;
   the next ordinary iteration may return while that previously unsampled
   birth is still live and has no readable canonical hit. Persist every valid
   additional query PID/birth as observation-only liveness, never as target or
   signal authority. Live/unknown blocks return; missing identity, overflow or
   unavailable positive coverage retains sticky hold/escalation. Keep exactly
   one scan and fresh ordinary reconciliation after it, with no rescan,
   foreign signal, release API or ownership inference.

The proposed `inert_checks.py` has useful validator fixtures but does not
exercise these changed control paths; its standalone allowance arithmetic
does not test actual admission. **The lead now selects one final exact-current
small actual-control inert suite**, using the existing literal Python `-I`
inert_checks.py argv under the cached five-second timeout,1MiB merged-log cap,
core0 and unlimited FSIZE. Native filesystem/process/clock/signal/subprocess
boundaries must be faked or poisoned; bind source and suite before/after and
the resulting log. AST/Bash-n/static preparation checks remain allowed.
Cover pending-present to active within5s, pending-absent and forbidden
late/post-bound states; actual pre-Popen/per-FIFO allowance equality/+1,
positive gap/no refund and a delayed read crossing the startup deadline; child
missing-birth/sink/cap/poll/cadence/final-close/status errors with both drains,
primary/native retention and no next launch; persistent clock failure reaching
one escalation/scan; malformed optional JSON still reaching the base scan; and
an actual-shaped query PID700/birth70 absent from the sampled set remaining
live/unknown after scope exit, then absent. Include first-settlement at the
deadline so pre-scan observations cannot establish post-scan completion.
These are focused preparation checks, not systemd/kernel/Nix conformance.

Two admission/evidence details should accompany that narrow correction packet:
the sample cap/write currently follows FIFO admission (`sample:373-377`), so
do not claim that this iteration's sample-evidence failure prevents admission;
check/record that evidence before issuing the token, followed by the fresh
deadline check. Also fix the future utility's literal log destination under
the counted package directory, or explicitly include its bounded external
logs; `logical(P)` alone cannot account for unspecified utility log paths.

The selected correction boundary remains the existing fixed driver/observer,
inert source, brief and binding receipts. Query1285be35/checkerb82015b3, source
manifest2404, all locks/tools/names, native argv/environment, product, old helpers
and every selected resource limit remain frozen. Owner3 owns implementation;
material deviations return to lead before edits. Delivery to ready/write
implementer3 is confirmed under message
`c0988a31-926f-4701-91ef-0b7eabf91746` (turn
`01a16b8e-53ab-7a20-892c-858248e30f32`). Return the corrected frozen
package and exact source/test/log/preservation bindings for fresh focused source
acceptance. This selection authorizes neither architect tests/takeover nor
native guard, Nix parse, Ruby syntax, query/evaluation, cache/fetch/build,
process/scope/capacity/scan/probe, Git mutation, runtime or cleanup operations.
No resource increase, tool fetch, old guard repair or general monitor framework
is selected. This assessment and selection update edited only this design
record; the architect ran no tests, parsers, helpers or native operations.
Native evaluation/selector and later packaged-gem/production runtime gates
remain unselected; historical monitoring remains INCOMPLETE and unchanged.

#### Corrected final-head-discovery-1: source accepted

Focused architect acceptance closes the four selected correction groups and
both accompanying details. This supersedes the withheld-source disposition
above for this exact package only; all original findings/evidence remain.
No native execution or mandatory product-review conclusion is implied.

- Frozen manifest: `18f8f636e1669773a615de8dde261ec673ed8e7791073b60bb2c475c9a617c96`.
- Receipt: `e948be1392938d0fac14a13e566047104ccbbe3bdfa467b9965a05df90196936`.
- Observer: `9f6b310178388604106849211233144115e79c1667c6bcc67bdc879e0e66f241`.
- Driver: `aaf778b88a38f2b6b8055526da25544807ba7321b44ec5ffa0581c16cb92669e`.
- Inert suite: `28bbc805b68f3cc22633a49b4dc3e849be7b71c627f3fa9322ad62d4da3a4efa`.
- Results: `175df278d92bcb867add4bd670299954a4c1e53d40380d309b1f713ff4590b0f`.
- Raw merged log: `7d149599b54bbd87acf605d7d6c70008913f66cd9322eb518e181f18d0a7405a`.

Independent static inspection matched all89 frozen hashes/modes/sizes, the25
original files under correction-1-originals, and all16 earlier artifacts.
Catalog1285be35/checkerb82015b3,2404-entry manifest, four locks, tools, names,
environment, run.sh, ledger and reused observer remain byte/mode identical.
commands.json changes only by adding literal counted P/utility-run stdout,
stderr and event destinations. Native argv and resource settings are unchanged.
The driver changes only its existing run function; the observer changes the
selected pending/sample/effects/supervision paths and adds the local optional
input collector. No general framework, product or old-helper change emerged.

Pending-present accounting now validates/counts tentative memory and children
without binding/admitting; actual absence alone permits zero, and slow reads
recheck the existing five-second window. Sample evidence cap/write precedes
FIFO admission, whose deadline read follows resource/identity/evidence reads.
The serial driver retains each same child and both drains through poll/cadence
errors, independently attempts wait/clock/closes/receipts, preserves primary
and native status, and prevents the next gate on finalization failure. No new
signal authority is introduced. Guarded timing reaches one-shot escalation and
the existing cancellation/liveness paths even when the clock remains unavailable.

Malformed optional metadata now records sticky incomplete coverage while the
single base scan is attempted. Valid additional query births enter only the
observation set before scan results; live/unknown blocks settlement without
granting signal authority. Missing identity/overflow/unavailable coverage holds
remain sticky. Every scan trigger still requires a later ordinary native,
known/reference-birth, named-scope, canonical-cgroup and both-EOF reconciliation.
One launcher, at most one authenticated outer-timeout signal attempt, the
independent drains, failure latch and finalization safeguards are preserved.

The retained5412-byte log and results bind the final39 actual-control cases to
the exact current driver/observer/suite before and after: producer0, reader0,
zero reported poisoned-boundary attempts. Source inspection confirms meaningful
pending/admission, sample-before-token, child/finalization/no-next-gate, persistent
clock, malformed-input/base-scan, query700/70 live/unknown-to-absent and post-scan
cases. The pre-Popen fixture executes an identical extracted statement prefix;
the sticky-hold cases add only a test-side loop prefix, verify unchanged
production AST, and stop at the fourth fixture tick. They prove a bounded hold
prefix, not arbitrary-duration completion. Exercised native boundaries are
faked/poisoned; these are neither systemd/kernel/native-Nix proof nor a pass of
the earlier validator mutation matrix. Interim failures and invalid capture7
remain retained. No test, parser or helper was rerun for this acceptance.

Evidence qualification: proportionality.json retains a stale
`unchanged_AST_functions` entry for inspect_scope, which this correction does
change. Do not cite that entry as equality proof. This acceptance rests on the
actual inspected function/diff and exact-current case bindings; the stale list
does not create a remaining executable-source blocker or require a test rerun.

Carry3481821184B/endpoint136627523584B/named maxima2680176640B and the512MiB
lifetime allowance remain intact with positive-gap charging/no refunds. The
4GiB stops,43/40GiB free space,8/12GiB whole-daemon/client samples,20/16GiB host
availability, hard client1GiB/noSwap,300/90/5/+5 timing and32MiB/64KiB evidence/
emitter limits are unchanged. Fresh admission may refuse; no cache or capacity
assumption, hard aggregate/peak, complete owned allocation or ended protected
effects proof is added. Native final source/NAR/locks/selector and effects
verification still require separate lead selection. Old monitoring stays
INCOMPLETE; later packaged-gem and production-v1/v2 runtime gates remain held.

#### Superseded dev-session literal: narrow correction proposal, not selected

The one selected attempt of frozen18f8f636/receipte948be13 exited1 at
observe.py91. [Retained owner assessment](repair/support/final-head-discovery-1/utility-run/owner-assessment.json)
and1376-byte stderr SHA256
`f1d50d8782cd7797646741ba766ecbed6e4278dcbed021222424a40daaeb5cef`
record the superseded-package refusal from the frozen dev-session command.
stdout is empty. setup-failure.json is268 bytes, SHA256
`c7ed025d9bba7d2033f8d779227c5225dd4ef454a5585376ff391091997a068c`.
The reported <1second duration is retained utility evidence, not a fresh timing.
Source ordering places this failure before package/source verification, any
capacity/RAM/scope reads, creation of native/observation/FIFO, and the launcher
Popen. The dev-session child did run and returned nonzero; neither metadata
queries nor selector nor effects scan ran through this path. Retained path
absence is not broad process/protected-effects proof. No automatic retry follows.

Readlink/byte inspection resolves the public entry as:

```text
/home/aither/bin/dev-session
 -> /home/aither/.local/state/dev-workspaces/profile/bin/dev-session
 profile -> profile-185-link
 profile-185-link -> /nix/store/1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0
```

The current immutable command is
`/nix/store/1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0/bin/dev-session`,
580 bytes/mode0555/SHA256
`95926e957f8e798b4058aba35949d7c9564932521dc7674503297fd3681eb028`.
The old ns3rb6k9 command is580 bytes/mode0555/SHA256
`bb501844689ad15786c230a8e9f1c6550b8cc4dbb30f1a608ca88a437c30d7fb`.
Their wrapper bytes differ only by replacing the package root in the extension
catalog export and workspace-host exec target. This is a current static
resolution, not standing validity for a later attempt. The retained team policy
catalog and saved member settings are separate from the active command package
generation; refresh neither the team nor its catalog to repair this literal.
Never remove the generation/session check or force its old generation through.

Proposed owner3 boundary, requiring lead source-only selection before edits:

- Preserve the entire failed package, all89 frozen identities, original
  frozen/receipt, accepted39-case and quick-syntax evidence, utility logs,
  setup-failure and owner assessment first, with byte/mode/hash manifest.
  Keep original bytes and dispositions; do not overwrite or relabel the attempt.
- Replace only driver.DEV's ns3rb6k9 literal with the current immutable1zkafvr6
  command and update only tools.json's dev-session identity. Preserve the other
  five tool records. Record the public/profile symlink chain as provenance;
  do not replace the fixed execution argv with PATH lookup or a moving alias.
  Update directly dependent hashes/brief/diff/frozen/receipt records, keeping
  source controls, native argv/environment, query/checker2404-copy/locks/names,
  run.sh and resource/authority logic unchanged.
- The outer utility attempt and its evidence paths are consumed. Propose a
  fresh utility identity and literal P/utility-run-2 stdout/stderr/events plus
  P/setup-failure-2.json for a later attempt; both remain within existing
  aggregate accounting. These are diagnostic-path substitutions only, not
  new control logic. The existing exclusive setup-failure writer and utility
  redirections cannot safely reuse their occupied evidence names.
- Source ordering supplies no reason to rename the unlaunched native unit,
  native/observation paths or FIFO, which would unnecessarily alter native
  argv. It does not authorize their reuse: only a separately selected later
  operation may reuse them after its existing fresh canonical absence and
  scope checks pass. Do not create or consume any proposed identity now, and
  do not clear paths or weaken refusal to make them available.

Required static return: exact original-preservation manifest; old/new public
chain and wrapper identities; literal-only driver/evidence-path diff; unchanged
control/function bodies after accounting solely for those literals; unchanged
query/checker/manifest/locks/names/other tools/native argv/environment/ledger;
all new dependent receipt hashes. Retain the39-case evidence bound to its
original source; a new hash is not a new test pass. No test/parser rerun is
justified by changed string literals alone, and none is selected here. Any
control change or wider command-generation dependency returns to lead first.

Preserve carry3481821184B/latest endpoint136627523584B/all named maxima2680176640B
and every later retained maximum. This early failure supplies no new capacity
sample and does not establish zero cost. Backup/preparation/evidence growth
remains charged by existing maxima and positive gaps at later admission,
without refunds/reset or a ceiling increase.512MiB remains the lifetime metadata
allowance; all4GiB/43-40/RAM8-12/host20-16/client1GiB-noSwap/time/log limits stand.

Only this design was edited; no correction was dispatched. The thread-required
public current/env binding was rechecked before session-file access. Apart from
that mandated public guard, the investigation used readlinks and file bytes;
no old/new DEV invocation, other package helper, probe, test or native operation
was performed.
Fresh source acceptance, lead execution selection and a fresh utility are
required before any later launch. A further generation change must fail closed
and return to lead; no dynamic repinning, automatic replay or old-guard repair.

#### Generation refresh inspection: one startup bytecode blocker

Focused source inspection of frozen
`b72ce1a0fd0160e0b40391077bf9dcf6cab093f86a09a0422484a8e0080c41f3` /
receipt `2e727099400f327e8cf4a1dc1342bda9b8a0d85f6147177f48295556ed30f156`
withholds acceptance for the single issue below. All213 current frozen
hash/mode/size bindings and114 snapshot path/type/mode/byte identities match.
The105-file/2131191-byte failed-package snapshot preserves the permanent
attempt1 and its original checks. Whole-source byte comparison independently
confirms only the selected DEV substitution in driver6a9935aa and diagnostic
literals in observer62219fce. All19 protected source/evidence paths match;
commands5e0b03ae changes only utility-log paths, tools96e19fd1 only dev-session.
Native argv/environment, catalog/checker2404-copy/locks/names, other five tools,
ledger/resources and accepted controls remain unchanged. Historical39/syntax
results retain their original bindings. No stale proportionality claim is used.

The refreshed frozen manifest now includes the live
`__pycache__/driver.cpython-313.pyc`, SHA256
`955cdac0977ae20539827ecc7144420a777ea4cf8542361c70393a7cdfa1f214`,
27575 bytes/mode0644 in an owned0755 directory. Its timestamp-based header
(flags0) records source mtime1792806565 and size16778; the current driver has
mtime1792808140 and size16778. Its cached bytes contain the old ns3 DEV root,
not the replacement1zka root. Thus it is stale at this exact source state.

Observer line90 uses SourceFileLoader through spec_from_file_location and
exec_module before line92's frozen verification. The frozen sole utility argv
is Python `-I` observe.py; it neither supplies `-B` nor sets
sys.dont_write_bytecode. Exact retained Python3.13.15 importlib source
`lib/python3.13/importlib/_bootstrap_external.py:1155-1170` recompiles stale
source and calls `_cache_bytecode` when bytecode writes are enabled. A normal
writable-cache import therefore changes this now-frozen file before verifying
it. If DEV succeeds, the ensuing frozen hash check refuses; if DEV refuses
again, the package has already attempted this cache mutation. This is static
source/header evidence, not a reproduced launch or an effects observation.

Minimal proposed correction, **requiring lead selection**: add `-B` solely to
the outer utility Python argv (`python3.13 -I -B /absolute/P/observe.py`) and
update its direct command/brief/frozen receipts. Preserve the stale cache and
all snapshots byte-exact; do not delete it or exempt a changed frozen file.
This suppresses the import's bytecode write while keeping observer/driver
source, native child argv, all controls and the generation guard unchanged.
The later Bash-launched driver is a script, not this dynamic import. No broader
loader/framework change is needed. Verify the exact added flag/static bindings
after selection; do not infer a new test or native pass from this proposal.

No helper, parser, test, cache/capacity/process/scope query, scan, Git mutation,
signal or native retry was run for this inspection. Only session binding/roster
coordination and static file reads were used; only this design was edited.
Neither new diagnostic paths nor unlaunched native identities were consumed.
All existing carry/maxima/no-refund,512MiB allowance and resource limits remain
unchanged. Fresh focused source acceptance and separate lead/fresh-utility
execution selection remain necessary; no correction was dispatched.

#### Outer -B correction: focused source accepted

The single bytecode blocker above is closed for frozen
`01421b9647b5f6e4f2053557283a375830a97c9357a905eede92f5c75156e75c` /
receipt `1f68be6dba437ef0e89ab2f534be753a5f800280cd4564b098a1e50b2699efdd`.
Independent static inspection matched all220 current frozen byte/mode/size
bindings. Of the prior213 entries, only commands.json and ready.md changed;
their originals plus prior frozenb72ce1a0/receipt2e727099 are preserved in
bytecode-flag-1-originals with the matching inventory. The other211 entries,
including observer62219fce, driver6a9935aa and live stale bytecode955cdac0,
remain exact. No cache was deleted or exempted from frozen verification.

Commands SHA256
`4501749f31e55c959ce894ca979714b21b2bcb00c901eb0ca2a6f627b16859f1`
adds only `-B` immediately after `-I` in the sole outer utility argv:

```text
/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 -I -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/final-head-discovery-1/observe.py
```

The current receipt agrees with that argv. Removing only this flag makes the
complete commands JSON equal to its preserved predecessor. The brief/diff49cab662
and proof0a840fba correctly describe the same change. The explicit Python flag
disables the dynamic import's bytecode write before frozen verification while
retaining the existing generation/session guards and observer/driver controls.
Native child argv/environment, source/locks/tools/query/checker2404-copy/names,
all resource/carry/maxima/no-refund constraints and preserved failed-attempt
evidence remain unchanged. Historical39/syntax evidence stays bound to its
original source; no current execution pass is inferred. No stale proportionality
claim is used.

This is static source acceptance of the generation refresh plus the outer flag,
not a native result. No parser, test, helper, immutable DEV probe or native
operation was run for acceptance. Fresh lead execution selection and a fresh
utility remain required; existing fresh absence/identity/generation/resource
checks must pass without clearing paths or assuming reuse. Current installed
generation, available capacity/cache, actual selectors/source graph and effects
remain later observations. No automatic retry or cleanup follows.

#### Attempt2 startup refusal: bounded correction proposed, design only selected

The lead selected this retained/source-only design, not implementation, checks
or another native attempt. The accepted owner assessment is
[attempt-2-owner/owner-assessment.json](repair/support/final-head-discovery-1/attempt-2-owner/owner-assessment.json)
`f122f8cdb64ac13c9749dc9290ce5b7ea8f3d6f69f668cfc17556603f42c8049`,
bundle `74152d4c` and binding `314acc2e`. Frozen01421b96/receipt1f68be6d and
all220 bindings remain the permanent failed baseline. Observer62219fce returned1,
native returned-15 after one authenticated timeout TERM; no phase was admitted.
The result5dee9d9a/effects88b543af and missing utility events remain unchanged.
Readable reconciliation found the known timeout absent, scope collected,
canonical cgroup absent and BOTH_EOF, with protected/FD/race gaps. This is not a
guard PASS or proof that protected effects ended. No further scan is needed for
this design.

Source337 requires an exact Bash child on the first active-scope snapshot.
Only timeout3431952/birth1211652997 was retained. The startup request proves
that run.sh reached its pre-FIFO write sometime, not its birth or the first
membership/exec ordering. A fork/visibility race is plausible, not proved;
there is no retained first cgroup.procs/candidate mismatch record. Neither a
missing executable nor a wrong argv, FIFO, generation, source or query failure
is established. The proposal addresses the premature assertion without
declaring any of those possible explanations resolved.

**Proposed local state and integration.** Keep scope_kind and its existing
unbound loaded/inactive/empty-invocation exception unchanged. Within
inspect_scope, distinguish `active-timeout-pending` from ordinary `active`:

1. Only startup_proven=false, admitted_phases empty/phase_index0, no prior
   failure and the original live Popen handle can enter it. The fresh elapsed
   time must be strictly less than5s from the existing started value. Do not
   reset started, extend the deadline, add a timer/sleep or launch another child.
2. The named scope must already satisfy the exact active Id/invocation/canonical
   cgroup/inode checks and all hard client limits. Bind that tuple normally and
   retain it while pending. Every later observation must match it. Inactive,
   missing, changed or unreadable bound identity cannot become pending; the
   existing collected-state reconciliation does not imply startup success.
3. Authenticate exactly one timeout from the current membership and fresh
   launcher details using existing native_authority: exact argv, resolved exe,
   canonical cgroup, PID/birth and supported original launcher ancestry. If a
   target was already authenticated, the fresh target must have the same
   PID/birth; never overwrite it with a replacement. A saved target alone is
   not evidence for a new pending observation. Retain it for the unchanged
   cancellation reauthentication even when a later startup check fails.
4. Zero exact Bash children may wait only when the bounded, fully readable
   membership contains the authenticated timeout and, if distinct and present,
   its exact original systemd-run launcher. Any extra unexplained member,
   vanished/skipped member, duplicate/overflow, permission/parsing error or
   partial candidate makes this absence ambiguous and refuses. In particular,
   an argv/exe/parent/cgroup mismatch must not be filtered out and then called
   zero candidates. No pre-exec clone, mv helper, foreign process or likely
   descendant gains an exception by name/timing. This conservative state may
   still refuse another intermediate snapshot; it does not promise admission.
5. A unique exact Bash PID/birth with argv=[BASH,D], exe=BASH, parent=the same
   timeout PID and exact cgroup completes the existing startup proof, only
   before5s and without a prior failure. Multiple or mismatched driver
   candidates refuse. Keep other already-supported accounting on the ordinary
   exact-Bash path; this is not a new general descendant classifier. A request
   file is neither process identity nor permission to issue a token. No new
   pending tolerance applies after startup proof or admission.

Merely removing the assertion is insufficient: current sample calls admit for
any active scope and admit requires startup_proven. The new pending kind must
retain actual present-cgroup memory accounting, daemon/host sampling, positive
disk charges, maxima, logs and both pipe drains, while never calling admit or
opening/writing the FIFO. Require the same pre-admission disk/RAM/identity/log
predicates for continuing this narrowly pending state; never count its client
memory as zero. Before admission the ordinary exact-Bash path still writes the
current sample successfully, then performs the existing fresh resource/timeout
identity/deadline checks and token operation.

Recheck the original5s deadline after membership/identity reads and again after
resource reads and successful sample evidence, including the zero-driver path.
At exactly5s, native exit, a clock/read/write error or earlier failure, latch
incompleteness in this iteration. Do not wait until the next cadence or use the
300s operation deadline as a startup extension. A late exact chain may remain
useful for safe cancellation but never clears the first failure or admits work.
Preserve one Popen, at most one freshly authenticated direct timeout TERM,
PID/birth liveness independent of PGID, independent drains, original/native
status, one escalation/effects scan, sticky observation-only reference holds,
fresh ordinary reconciliation after every scan trigger and guarded finalization.
No signal authority is added for Bash, other members or scan-discovered PIDs.

**Bounded refusal evidence.** Retain first and latest pre-admission membership
observations, plus the first refusal's observation through existing state,
samples/first-failure/result receipts. Record stage, elapsed, raw named-scope
properties, bound/current tuple, membership PIDs and each read outcome. For
readable members retain PID/birth/PPID/PGID and separate exact-timeout,
exact-driver, exe/argv/parent/cgroup match results; record skipped read stage,
exception type/errno and whether a birth was obtained. Capture evidence before
the assertion that may fail. Proposed bounds are4096B membership text,16 entries
and16KiB per summarized observation; overflow itself refuses, not truncates to
an accepted zero-match result. Use bounded exe/cgroup text and argv byte length,
digest and fixed-field match flags for nonmatching argv, not arbitrary argument
or environment dumps. First/last/refusal retention and sample copies remain
inside the existing6MiB sample/12MiB other/32MiB aggregate limits. Failure to
write evidence fails closed without replacing the primary or skipping drains,
cancellation or reconciliation. This adds fields to the fixed observer, not a
logger, registry, process discovery pass or new framework.

**Fresh operation identity and owner3 file boundary.** Attempt2 consumed the
old observation directory/FIFO and native scope identity. Do not edit, clear,
rename, relaunch or reuse the failed package. Propose a sibling package
`repair/support/final-head-discovery-3/` (P3, named for the third attempted
observer operation), with these literal future destinations:

| Purpose | Proposed identity |
| --- | --- |
| Native output | P3/native |
| Observation/FIFO/request | P3/observation, admission.fifo and request.json beneath it |
| User scope | ci-failure-final-head-discovery-3.scope |
| Canonical cgroup | /user.slice/user-1000.slice/user@1000.service/app.slice/ci-failure-final-head-discovery-3.scope |
| Utility diagnostics | P3/utility-run-3/{stdout.log,stderr.log,events.jsonl} |
| Prelaunch failure | P3/setup-failure-3.json |

These are proposed names, not observed absence, created paths or consumed
identities. Preparation must refuse an occupied P3 instead of clearing it;
later selected native execution must still freshly prove its own scope/path
absence. Preserve the entire old package in place and first inventory/snapshot
its regular bytes, symlinks and modes under P3/attempt-2-originals, including
all220 frozen entries, raw failures, owner bundle/bindings/carry and historical
39/syntax evidence. The old FIFO stays in place: retain its type/mode metadata
without opening it or creating a replacement IPC object in source preparation.
Do not follow external symlinks or import old native results as new results.
Count preservation/preparation bytes in the existing evidence/disk budgets.

After separate lead selection, owner3 would own only the new package's
observer startup/evidence integration, focused inert fixtures, literal root/
scope/diagnostic references in run.sh/commands, run hash and dependent frozen
receipts/brief/proof, and ledger carry-forward. Driver.py can stay byte-exact:
its P derives from __file__. Native argv may differ only in the explicit new
package paths and scope name, with a field-by-field relocation comparison;
query and selector options/ordering and environment bytes stay exact. Preserve
outer cached Python `-I -B`, static tools including DEV1zkafvr6/SHA95926e95,
catalog1285be35/checkerb82015b3, source2404 manifest, full candidate/production/
constructor locks, expected catalog names/three gates and immutable f746/tree1bbd.
Do not refresh DEV preemptively or bypass a generation refusal. A demonstrated
generation obstacle returns to lead for a separate literal decision. Product,
Git, old helpers/receipts, selectors, input validation and old4de STOP remain
outside the boundary. No deployment/API/ABI/migration or rollback action is
introduced; failure retains artifacts and does not authorize cleanup or replay.

**Resource anchor, unchanged ceilings.** Use the immutable retained
[resource-carry-forward.json](repair/support/final-head-discovery-1/attempt-2-owner/resource-carry-forward.json)
SHA `2e18dec2fc5852143996b27218121074ac8ded9ff690612f3749251273925288`:
carry3520598016B, latest ordinary free endpoint136588767232B and all107 named
maxima totalling2686197760B. Map last_retained_free to the new ledger's existing
last_free field without changing its meaning. Preserve every old path/value,
including P1; only add/increase maxima. Effects free136588800000B was earlier
than the last ordinary sample and cannot replace the anchor. Remaining774369280B
less the same lifetime512MiB allowance leaves237498368B before any new positive
gap or preparation growth. All three completed numeric samples were after
cancellation/collection with client0; they establish no active admission RAM
values or future capacity/cache availability.

Before Popen and FIFO, charge the positive gap and every subsequent sampled
decrease, require charge+536870912<=4294967296, known subset<4GiB and free>=43GiB;
increases/absence/deletion/GC/foreign frees never refund. Keep runtime cumulative
and known-subset stops>=4GiB and free<40GiB; client hard1GiB/noSwap/CPUquota2,
whole exact daemon+client <=8GiB admission/>=12GiB stop, host available>=20GiB
admission/<16GiB stop,300 total/90 per query/5 selector/+5 escalation,32MiB
aggregate evidence and64KiB own emitter. Pending receives full accounting
inside those limits. These remain sampled/coarse non-atomic measurements, not
owned aggregate containment, protected-effects or unsampled-peak proofs. No
budget reset, automatic increase, tool fetch or zero-cost preservation assumption.
Insufficient fresh margin returns to lead without admission or polling.

**Proposed checks and acceptance, all unexecuted.** First compare old/new
hashes/modes and every immutable input; retain a literal relocation map and a
small source/control diff. Unchanged authority, scope_kind, drain, serial driver,
effects, liveness and finalization bodies must compare exactly where unaffected;
list any required local changed statement instead of claiming whole equality.
Static source/AST/Bash-n checks and the following ONE current small inert suite
require lead selection; no checks are authorized by this design assignment.

Extend the existing actual-control suite at P3/inert_checks.py, rather than
create another harness. Proposed argv is the same cached Python3.13 `-I -B`
with the absolute P3/inert_checks.py, no case-filter arguments, under the
retained cached5s timeout,1MiB merged log, core0/unlimitedFSIZE envelope. Freeze
the full expanded argv, source/test before-after hashes, exit and raw log. Use
actual inspect_scope -> sample -> admit and the existing supervise path with
native filesystem/process/clock/signal/subprocess boundaries faked or poisoned;
no copied substitute decision implementation. The focused additions must show:

- Active exact timeout-only at <5s retains tuple/handle/actual client memory and
  all resource charges but issues no token even with a startup request; a later
  unique exact Bash within the original5s completes proof and sample-before-token.
- Missing Bash through exactly5s; a membership, RAM, disk or evidence read that
  advances the clock across5s; late Bash; native exit; prior failure; bound tuple
  loss/inactive transition; reused timeout birth; duplicate/wrong Bash fields;
  foreign/skipped/unreadable/overflowed membership all refuse without a token.
  Assert the first membership and precise mismatch/skip survive the refusal.
- Pending resource/admission failure, sample/receipt/clock error and repeated
  failure preserve the first reason and same handle; independent pipe progress,
  at most one exact-timeout TERM, one scan and fresh postscan settlement remain.
  Include no-refund/fresh-gap and equality/over-limit admission checks using the
  new carry; fakes must not manufacture real capacity evidence.

Reuse the relevant existing control cases in that one full small run; do not
repeat historical suites separately or claim they ran on corrected source.
Any test-only bounded-loop escape must remain outside production catches with
an exact AST binding. These checks establish fixed control behavior with fake
boundaries, not native systemd/kernel scheduling, selectors or complete runtime
conformance. Return frozen source/check package for fresh architect acceptance;
lead separately selects any utility/native operation after that acceptance.
No implementation assignment, source edit, parser/test/helper execution, live
inspection or retry was dispatched by this design. The lead owns state/handoff
integration; session and member settings remain unchanged.

#### P3 focused source assessment: two local membership blockers

Following the lead's source-preparation selection, owner3 froze P3 and the lead
requested this focused source acceptance. **Acceptance is withheld for the two
concrete changed-path defects below.** This is not a new product review. No
correction, test rerun or native attempt is selected by this assessment.

Exact inspected bindings:

| Artifact | SHA256 |
| --- | --- |
| P3 frozen.json | `6d58c61cd3f1fa99361a7a4e174e950674437856aefd7d7c38552945c7fd58e5` |
| P3 receipt.json | `f54d98d79f36aca7d53f20c74a1f28e694beb2e68becd19c78e60c78ddda3c0e` |
| P3 observe.py | `01ecaa6fe36825807cf83717b012bbd2491b04ab4ddacf4ef1edda834aeafb07` |
| P3 inert_checks.py | `98d8402c0641fbdc8fecf099c3fab40946acacd8902b603f48e3c3f942753b34` |
| P3 suite-results.json | `54c2ad96b009219f43919788991f03645b012be021d5eee643faefb8132d59fe` |
| P3 final-suite.merged.log | `4877a761c4f545cca8e8120d6e3e71736c01ed8c9ae93d6a98b69c7d9dd51546` |

Independent static inspection matched all279 current frozen content/mode/size
bindings, all220 old P1 frozen hashes, the entire262-path P1 inventory's
type/mode metadata and all238 regular files against the preserved snapshot.
The FIFO was not opened. Eleven source/input files compare byte-exact to P1,
including driver6a9935aa, query/checker, manifest, names, environment, tools and
four locks. The actual complete normalized observer diff matches the retained
observer-control.diff; its26 unaffected function claims are consistent with
that byte comparison. Run/command relocation stays literal and narrow. The
ledger's full107-entry map,3520598016 carry and136588767232 endpoint compare
exactly to immutable carry2e18; the sum is2686197760. No fresh capacity or runtime
absence conclusion was obtained by this acceptance inspection.

The intended active-timeout-pending path is otherwise within the selected
design: exact same-handle/scope/timeout, no prior failure or admitted phase,
strict original5s deadline, actual client memory and full pending resource
gates, no FIFO call while pending, and fresh deadline/handle checks after sample
evidence. The two local helpers are proportionate. Authority, one launch/TERM,
drains, scan/hold/fresh-postscan and finalization controls remain in place;
supervise's direct delta only adds evidence to its result. These accepted
portions do not resolve defects in the membership inputs they consume.

1. **Skipped ordinary members misalign processes and evidence.** At
   [observe.py:380](repair/support/final-head-discovery-3/observe.py), every PID
   appends a row, but after startup a FileNotFoundError continues without
   appending to procs. Line405 then zips procs with the unfiltered members list.
   With startup_proven=true and membership [8,2,3], where8 disappears and2/3
   are the valid timeout/Bash, procs=[2,3] pairs timeout2 with row8. That row has
   no driver_argv, so line407 raises KeyError. A supported ordinary exit race
   therefore becomes a sticky observer failure and can cancel valid metadata.
   This is a static counterexample, not a claim that a native run exhibited it.
   Keep each successfully read process associated with its own row (a local
   pair or PID-indexed lookup); skipped rows remain diagnostics but cannot
   supply another process's match fields. Preserve the existing post-startup
   FileNotFound handling and strict pre-admission refusal; do not broaden
   process tolerance or add discovery.
2. **A captured partial birth is omitted from liveness reconciliation.**
   [startup_member at observe.py:320](repair/support/final-head-discovery-3/observe.py)
   records PID/birth at322 before argv/exe/cgroup/stat.after reads. If any later
   read fails, inspect_scope rethrows at384 before adding the identity to known
   at394. The captured birth remains only in startup diagnostics, not known or
   reference_births. The existing skipped/unreadable fixtures already obtain
   PID8/birth80 and then fail the argv read, but stop after checking diagnostics.
   If that observed birth remains live or becomes unreadable after leaving the
   scope, an otherwise collected/native-ended/BOTH_EOF state plus a scan without
   rediscoverable canonical references can let the observer return without
   reconciling it. Primary failure prevents PASS; it does not prevent abandoning
   an already observed live/unknown birth. Preserve every actually obtained
   PID/birth before a later field, cap or evidence error can discard it, using
   existing observation-only liveness. It must not become timeout, ownership or
   signal authority. Reuse the existing bounded collection/overflow hold rules;
   no rescan, new timer, registry or privileged proof is needed. A later reused
   PID is distinct; same-birth live or unknown must keep the original handle
   and existing escalation/hold until ordinary reconciliation or lead action.

The80-case raw log is correctly bound to the exact current observer/suite,
producer0/reader0,11482B and zero poison attempts; before/after hashes agree.
The suite meaningfully exercises inspect_scope -> sample -> admit, pending
resource errors through actual supervise/cancel with fake os.kill, one scan and
fresh postscan, startup time/identity/error boundaries and no-refund admission.
It does not cover the post-proof skipped-row alignment or continuation after a
partially read birth. Historical39/syntax evidence and failed/interim runs are
retained without a current-source or native-conformance claim.

Minimal proposed correction package, requiring lead selection: preserve this
frozen P3/receipt/suite/raw first; change only local membership pairing and
retention of observed partial births, plus affected existing fixtures/brief/
bindings. Add a post-startup skip before timeout/Bash that preserves correct
identity association, and an actual startup_member partial-read failure whose
captured birth remains live, then unreadable, after native/scope/CG/EOF settle.
The latter must block return through the existing one scan and fresh ordinary
iterations, keep first failure and signal authority unchanged, then resolve
only when that same birth is absent/reused. Cover a completed member's later
diagnostic-cap failure as well; do not test only a synthetic missing-birth row.
Run no checks for this assessment; a later exact-current small suite and static
binding checks need explicit lead selection. All f746/query/selector/source/
lock/tool/argv/environment/resource contracts, carry/maxima and old evidence
remain frozen. Fresh source acceptance still precedes any utility/native choice.

#### Corrected P3 membership package: focused source accepted

Both local blockers above are closed for frozen
`57f3c1bbbedff310950167361f5939187b1f9982d97fd745658ab48409902485` /
receipt `63d14addfb674a49112b93c2208c00efa5a037e37e60d6bfccb59af9b6f73f6b`.
The accepted observer is
`bb9e42adb6e22778bcba63a7454e3aed664366a2c98c314eb38b015930967dcd`;
the current suite is
`24efb94be0c84aac6b0b42ab530b1a1de22a7690f52c8364ffbf7d9ab9777768`.
This accepts the source package within the selected fixed-operation boundary,
not native execution, product review, source/input graph or selector results.

Successful `(process,row)` pairs now travel together through matching. A
post-proof FileNotFound diagnostic row cannot shift timeout/Bash evidence;
pre-admission skipped members still refuse. startup_member captures each valid
PID/birth in the existing reference_births collection immediately after the
first stat, before row fields, argv/exe/cgroup/stat.after reads and later caps
or receipts. Both startup and ordinary membership use that instrumented read.
Capacity128 overflow latches the existing sticky reference hold and failure.
These observations do not acquire ownership, timeout/driver selection or signal
authority. Existing reference_liveness blocks return while the same birth is
live or unreadable, and resolves absence/reuse without a second scan or timer.

Independent static comparison matched the complete actual local diff to
membership-control.diff `ea75dc4b` and the cumulative P1-relative observer diff.
Only startup_member and inspect_scope changed relative to observer01ecaa6f;
all other functions/module constants are outside that actual delta. In
particular, pending admission/resource/deadline checks, native_authority,
cancel, drains, first-failure handling, liveness, one scan/fresh-postscan and
finalization retain the previously inspected controls. The change remains
local and proportionate; there is no whole-control equality claim against P1.

All323 current frozen SHA/mode/size bindings matched independently. All279
baseline bindings also matched through the preserved-original mapping.
Preservation inventorydc48/prooff4ee retains33 original root files/982610B,
with nested P1 evidence and old logs in place. The original262-path/238-file
P1 snapshot/all220 bindings and both historical failed attempts remain retained;
the FIFO has only its metadata in the preservation inventory and was not opened.
Driver6a9935aa/query1285/checkerb820/manifest2404/names/environment253/tools96e
and four locks still compare byte-exact to P1. Run c6c and ledgeradc5 are exact
to the prior P3. All commands fields are exact except the descriptive selected
suite evidence label; outer Python-I-B, native argv and environment are unchanged.

The current92-case evidence is correctly bound to the accepted observer and
suite, with before/after hashes equal: results
`442e1e78a54e41a076d60d1d1bce744f27c44083bbf3b1a619b64f42f940cb07`,
raw log `30a8ce06b8aa334236b562e1151c823d8034da0bb000ecd848daaa7b5d4d9526`,
13286B, producer0/reader0 and zero poison attempts. The12 additions cover the
post-proof skip and actual partial argv/exe/cgroup/stat.after or completed-read
cap failure, followed through actual supervise/cancel/drains/reference liveness.
The observed8/80 remains live then unknown after native exit, scope/cgroup
collection and BOTH_EOF; a scan that does not rediscover it cannot release the
handle. Absence/reuse permits later ordinary settlement. The fixtures also
check first-reason retention, the same handle, one strict timeout TERM, one
scan, fresh postscan and a bounded prefix of the sticky overflow hold. The
test-only loop hook is outside production catches; its removal is bound to the
unchanged production supervisor AST. These are meaningful fake-boundary control
checks, not native systemd/kernel timing or complete runtime conformance proof.
The80/39/syntax/interim evidence keeps its original historical bindings.

The ledger again compares exactly to anchor2e18: full carry3520598016,
last free136588767232 and all107 maxima totalling2686197760. The same lifetime
512MiB planning allowance leaves retained margin237498368 before future positive
gaps/preparation growth. All4GiB stops/43GiB admission/40GiB floor, whole-service
RAM8/12GiB and host20/16GiB gates, client hard1GiB/noSwap,300/90/5+5 deadlines,
32MiB aggregate evidence and64KiB emitter remain unchanged. No refund, fresh
capacity/cache assumption or protected/hidden/unsampled-effects proof follows.

This inspection used static retained-file comparisons only; no test, parser,
helper, DEV probe, Nix/query, process/scope/capacity inspection, scan, Git or
native operation ran. Only this design acceptance was edited. Fresh utility
and native selection remain the lead's separate decision; their ordinary
generation/identity/absence/resource admission may still refuse. No automatic
retry, budget increase, cleanup or repair of old monitoring status is authorized.

#### P3 resource refusal: retained disposition and next-verification proposal

**Lead selection recorded:** after reading this full section, the lead selected
the narrow no-Nix `final-head-source-validation-1` source/check preparation for
implementer3, delivered as message `4f90dd54`. Owner3 owns the fixed package;
architect0 only records this decision. Actual execution remains **UNSELECTED**.

For this one already-present-source validation only, the lead selected
**6442450944B (6GiB) for each separate disk stop**, preserving full carry
5752246272B, last endpoint134358052864B and all120 maxima totalling5881446400B
from immutable anchor `33e87b83e3dcb1b390e5cb4b016c6bb634b003a1a2e864864c80732e4263d6d5`.
The same512MiB lifetime allowance leaves153333760B before fresh positive gaps
and preparation growth. No refund, reset or reduction is permitted. All other
identity, RAM, free-space, time, evidence, cancellation and settlement limits
below remain unchanged. This selection does not revise P3 retrospectively or
authorize the remaining two queries, cache/tool fetching or runtime work.

The local bounded accounting, fixed evidence inventory and retained-default
validation boundaries below are selected exactly as written. Owner3 may perform
the specified static preparation checks and ONE small actual-control inert
suite with native boundaries faked/poisoned. No additional design expansion,
helper/native execution, probe, query or scan is selected. Owner3 must return a
frozen packet for fresh source acceptance; a future utility/native operation
still requires separate lead selection. No checks or implementation are assigned
to architect0 by this update. The original proposal, rationale and permanent
P3 failure disposition follow unchanged as the historical basis for this choice.

**Design only; no implementation, check or native operation is selected by this
section.** The lead accepted the qualified P3 assessment
`768cba0eddb533e24f7e29636f876a761a57808691e2bc5a31d64a64cebc1758`,
[carry-forward](repair/support/final-head-discovery-3/attempt-3-owner/resource-carry-forward.json)
`33e87b83e3dcb1b390e5cb4b016c6bb634b003a1a2e864864c80732e4263d6d5`,
binding `e08d8a9a` and bundle `88aec288`. Static reads/hash comparison in this
assignment match these records, observer `bb9e42ad`, driver `6a9935aa` and raw
default `0e21ef83`. Frozen `57f3c1bb` / receipt `63d14add`, all323 source
bindings, failed raw and historical checks remain unchanged. Public session
binding and the same-session ready/write roster were verified; saved settings
remain unchanged. Only this design subsection is edited; lead owns state
integration, and implementer3 remains the prospective implementation owner.

Handle63194 ended outer1/native-15 after105.741427s. Startup/default were
admitted. Sample47 at37.733290s first exceeded the cumulative disk stop:
4333158400 >=4294967296; the other five stop predicates were false. One
authenticated timeout TERM was attempted. Escalation at43.43s and its three
live reference births describe that historical observation. Later ordinary
reconciliation records all six references absent, no holds, collected scope,
absent canonical cgroup and BOTH_EOF. This supports the lead's qualified
readable settlement, not guard PASS, protected-effects completion or a current
live-process inference. No further reconciliation/scan is needed or selected.

The84 retained samples include a37.677274s gap from68.009115 to105.686389.
Source `sample()` processes default exit0/BOTH_EOF even after cancellation,
recursively walks discovered sources, then walks all maxima again, before RAM,
evidence and fresh deadline checks. Twelve unique native source roots account
for3184951296B of the late3185020928B named-total increase; repeated visits to
the same pathname are collapsed by `maxima[path] = max(...)`. Repeated walking
can delay supervision but does not itself charge that pathname repeatedly.
No subcall timings prove which read caused this gap. Shared decline and named
maxima are separate tripwires, not amounts to add together. No retained inode/
extent evidence establishes a refundable hardlink/reflink or overlapping-tree
error. Path maxima may include pre-existing/shared bytes and different-time
peaks; neither metric proves total unique owned physical allocation. Preserve
both unchanged, including every maximum and all unsampled/protected limits.

**Budget decision required before any future admission.** The new immutable
anchor is full carry5752246272B, last recorded free134358052864B and all120
named maxima totalling5881446400B, retaining all107 inherited entries. Carry
equals3520598016 +28319744 initial gap +24576 pre-Popen gap +2203303936
positive ordinary decreases. The free value was read earlier within the final
non-atomic sample;105.686389s is not its read timestamp. Subsequent assessment
and preservation growth has not been measured. Charge every later positive
endpoint gap and sampled decrease; increases/deletion/GC never refund anything.

| Contract/option | Cumulative headroom | After the same512MiB allowance | Named-maxima headroom |
| --- | ---: | ---: | ---: |
| Selected4GiB (4294967296B): HOLD | -1457278976B | -1994149888B | -1586479104B |
| Proposed6GiB (6442450944B), **no-Nix retained-source validation only** | 690204672B | 153333760B | 561004544B |

The selected contract cannot admit another operation. Waiting for free space
alone cannot repair these monotonic predicates. Recommend source-only
preparation of the bounded accounting change and retained-default validation,
keeping native work HELD. If the lead wants a finite next native verification,
the smallest whole-GiB envelope accommodating the retained carry plus the
unchanged512MiB allowance is **6GiB for each separate disk stop**, restricted
to reading already-present bound sources and writing capped evidence. This is
an explicit optional revision, not selected or retrospectively applied to P3.
Its153333760B (~146.23MiB) residual is consumed by future gaps/preparation;
the512MiB is planning allowance, not a write quota or measured peak. Fresh
admission must still refuse if that margin is gone. Missing source/tool bytes
stop without restoration, substitution, query or automatic retry.

Do not extend that6GiB proposal to the two unexecuted queries: P3 alone charged
2203303936B ordinary shared decreases, and its twelve named source trees total
3184951296B. Three stderr cache-copy messages prove source materialization in
P3, not future availability or attribution. Constructor-source materialization,
temporary copies and future shared movement have no adequate retained bound
for a full continuation within the proposed margin. No larger ceiling is
recommended from these records. Remaining-query admission needs a separate
finite planning decision; no automatic escalation of limits, capacity polling,
GC, tool-only realization or cache assumption follows.

For that optional no-query operation, retain free>=43GiB before Popen and every
FIFO admission/free<40GiB cancellation, whole exact daemon+client8GiB admission/
12GiB cancellation, host available20/16GiB, client hard1GiB/noSwap/CPUquota2,
300s total/+5s escalation,32MiB aggregate evidence and64KiB emitter. Before
Popen and FIFO, charge the positive gap from134358052864 and require
`full_charge + 536870912 <= selected_ceiling`, named maxima strictly below
their separately selected ceiling, and all other strict gates. Runtime equality
at either ceiling cancels. The original4GiB constants remain authoritative
until the lead explicitly selects both replacements. Sampled whole-service RAM
is neither an owned aggregate nor a reservation; retained free/RAM observations
do not establish fresh admission or peaks.

**Proposed local accounting boundary.** Replace recursive full-tree work in
the supervisor's `sample()` path with one resumable, bounded accounting pass;
do not introduce another process, worker pool, new signal target or monitoring
framework. The fixed observer continues to own one native handle and its
existing direct-timeout authority. This changes tree-observation timing and
must be selected explicitly; stale/partial totals must never be labelled a
fresh complete sweep.

- Every ordinary iteration first progresses both pipes, native/known/reference
  liveness, exact scope and cheap free/RAM/log/deadline checks. Charge free-space
  decreases immediately and deliver any failure/cancellation/escalation through
  existing controls before optional tree work. Tree failure cannot suppress
  another drain, liveness refresh or first-reason receipt. Keep fresh ordinary
  reconciliation after the single effects scan and all existing finalization.
- Bound one accounting slice by4096 metadata entries and50ms of monotonic time,
  whichever is reached first, with checks before/after each filesystem action;
  process at most one slice between ordinary supervision passes. Use incremental
  directory iteration, no recursive `sum`, eager directory list or unbounded
  sort. No symlink traversal. Bound traversal depth64, named roots256, retained
  cursor/path state8MiB, and total visited entries2000000/active accounting work
  30s within the unchanged300s envelope. Reaching a slice boundary preserves a
  cursor and yields; exceeding a whole-pass bound or a single action returning
  after50ms latches incomplete accounting and stops further optional traversal.
  These are proposed conservative refusal limits, not measured throughput or a
  guarantee that the full inherited map fits. Inability to fit returns to lead.
- Read new gate status/raw incrementally with at most64KiB of combined metadata
  per gate (retained default raw16438B/status10443B fits), max16KiB per read,
  max4096B per pathname and the fixed expected identity-root/edge structure.
  A completed status is consumed once; duplicate native source paths/follows
  enqueue one path, not another recursive traversal. Bound parsing by those
  byte limits; malformed/capped/unexpected identities fail closed. Keep late
  successful raw after cancellation as evidence, with accounting pending;
  do not begin a new expensive walk just to enrich a failed attempt's final row.
- Preserve per-path maxima and raise them with each partial lower bound;
  restarting a sweep never adds its subtotal again or reduces a maximum.
  Record root, cursor, entries, bytes, elapsed work, complete/pending/error and
  last complete observation. Partial zero, disappearance or a read error cannot
  discharge inherited values. Pending/failed accounting blocks admission and
  successful verification. Complete a bounded refresh before Popen and a
  phase-appropriate complete refresh before FIFO, then fresh cheap resources
  and elapsed checks; do not stretch the existing5s startup deadline to finish
  a walk. Any reuse of a completed immutable-store observation needs unchanged
  canonical/type/filesystem identity and explicit age/provenance; mutable paths
  need the new phase's completed observation. If this cannot satisfy startup,
  report the obstacle instead of admitting with stale totals.
- Remove hidden recursive work from `local_physical`, `logical(P)` and receipt
  cap checks on this path too: use the frozen preparation inventory plus a
  fixed bounded inventory/counters for this operation's mutable evidence files.
  Proposed cap96 mutable evidence entries; unexpected entries/types refuse.
  Include utility logs and reserve attempted receipt/output bytes without
  refunds. Keep the existing32MiB/12MiB-other/6MiB-samples/64KiB-emitter limits,
  independent drains after caps, and bounded first/latest accounting evidence.
  No repeated whole old-source traversal may hide inside failure reporting.

A synchronous filesystem call cannot be given a hard wall-time guarantee by
these cooperative checks. If it blocks, only its eventual return can record
the overrun; the independent native timer is not proof of observer cadence.
This residual must remain explicit. A hard guarantee against blocked storage
would require a different execution boundary and is not proposed here. Clock,
permission, type, overflow and evidence errors latch failure; incomplete tree
accounting is retained as unresolved accounting, never zero or a completed
budget proof. After cancellation it need not force an endless tree walk or
prevent a terminal INCOMPLETE receipt once the existing process/EOF/scope/
reference settlement predicates are satisfied. Live/unknown births or sticky
reference ambiguity still retain the handle and escalate exactly as before.
No accounting cursor supplies ownership or changes the one-scan rule.

**Retained default reuse and remaining proof.** Preserve raw
`0e21ef8370ec05b961112137a18d2db0a2da4b67833276f6924cc7aec91b39c1`
with its actual started/status/failed batch receipts. Query native0/BOTH_EOF and
the static v1/v2 upgrade-ci/full-lock/seven-node comparisons are genuine partial
evidence. The128 repeated cancellation entries and overflow are one latched
failure, not128 independent query failures. `run()` raised before
`check_identity`/`copied_source`; no default-complete or three-gate PASS exists.

The next useful validation can consume those exact bytes without executing
default Nix again. Keep the original failed status verbatim; write a separate
validation receipt, not a fabricated successful native status. Reuse the
existing identity/copied-source predicates: candidate f746/tree1bbd, native
source `/nix/store/xdbmyp84w9zasqpiqj3420r538yksbch-source`, observed NAR
`sha256-WMD5deXzowI9D17NfQOLvBe+TbMoGQFPhVq0CZhzCPw=`, full2404 Git blobs,
modes, symlink targets and exact directory set; candidate/production materialized
lock bytes, complete seven locked nodes/edges/follows and native revisions/NARs.
Recorded production source is `96g5h6c9kzwsr3n1cgsvzyq44wzyzixa-source` at2abbe3cc.
Bound content hashing to1MiB reads with cancellation/elapsed checks between
chunks, manifest-declared file lengths/counts and the original300s lifetime;
check expected size before reading a potentially oversized file. Missing,
changed or unreadable materialization refuses without fetching. Native NAR
identity remains distinct from Git/file hashes; no custom NAR reconstruction.

Still needed afterward: one historical native projection (exact23/manual/ci
exclusion), one diagnostics projection (exact2/manual/ci exclusion), both3cc/
3cb constructor identities/locks, cross-three-gate full identity equality, then
the unchanged actual final `TestScript` + `TagFilters` checker on every script
in the retained default and both new catalogs. Keep original native argv,
environment controls and90s/query/5s/checker proposals; no such query is selected
now. Future aggregate proof must name each operation and reused raw binding,
not represent them as one successful P3 batch. Packaged service -> wrapper ->
resolved gem/four changed realized bytes and production-origin v1/v2 VM gates
remain later dependencies. Historical boots, stopped4de reconstruction,
publication/default integration/deployment/runtime remain held.

**Prospective owner3 package; no dispatch.** If selected, prepare one fixed
no-query package at `repair/support/final-head-source-validation-1/`, native
scope `ci-failure-final-head-source-validation-1.scope`, with fresh `native/`,
`observation/admission.fifo`, `utility-run-1/` and `setup-failure-1.json` under
that new root. These are proposed names only, not an absence check, reservation
or consumed identity. Outer argv remains cached Python `-I -B` plus that root's
absolute `observe.py`, no arguments; freeze its complete expanded launcher/env
before acceptance. Adapt the current fixed observer/run/driver only for bounded
accounting and literal retained-source validation phases; no executable Nix or
Ruby-selector phase in this optional6GiB package. A later
`final-head-discovery-4` may be proposed for the two remaining queries/checker
only after its own budget and exact commands are selected; no generic resume
mode or release/handoff API is needed.

Preserve the complete failed P3 packet/raw/bundle/carry first, with FIFO metadata
only; leave all old paths/helpers/roots untouched. Copy the full120-value ledger
with exact anchor33e87b83, never a reduced or deduplicated replacement. Retain
query/checker/source-manifest/locks/names/environment/tools bytes and product
f746; only literal new paths, bounded accounting/validation controls and their
dependent receipts/tests may differ. A changed generation, missing tool, source
or resource prerequisite returns to lead before implementation expansion.

Propose one small exact-current actual-control inert suite under the existing
cached5s timeout/1MiB merged-log/core0/unlimited-FSIZE wrapper, all native FS/
clock/process/subprocess/signal boundaries faked or poisoned. It must exercise
actual supervisor/accounting integration: late exit0 raw after cancellation
starts no traversal; a huge synthetic directory yields at each slice while
both drains, same handle, liveness, cheap stop and one authenticated TERM remain
reachable; every byte/entry/depth/time/cursor bound and clock/read/write error
refuses without lost maxima or new admission; new partial totals can trip the
stop; free increases never refund; pre-FIFO accounting/resources/deadline remain
fresh; pending accounting settles only as INCOMPLETE after one scan and a fresh
ordinary iteration, while an observed live/unknown birth still holds. Include
retained raw provenance/failure preservation, wrong byte/mode/lock/follows and
missing-source cases with zero Nix launches. Bind source/test/log before-after;
historical92 remains historical. Static AST/Bash-n/preservation checks and this
suite are proposals, not run or newly authorized by this design. Source
acceptance and a fresh policy Luna utility/native selection remain separate
lead decisions. No application, compatibility, deployment or rollback contract
changes; recovery is preservation and explicit lead disposition, not retry or
cleanup.

#### Retained-source-validation-1 frozen source assessment: acceptance withheld

Static inspection of the selected no-Nix package finds four local blockers.
No correction, check rerun or native operation is selected by this assessment;
implementer3 remains the owner after an explicit lead correction selection.
Only this design record changed. Session/environment binding was verified;
saved settings and all frozen package/failed-operation bytes remain unchanged.

Independently matched core SHA256 bindings:

| Artifact under `repair/support/final-head-source-validation-1/` | SHA256 |
| --- | --- |
| `frozen.json` | `7fac6c7634b2838bc603d752fd9a0075c23dcbaa829281b7f5258fef10935abe` |
| `receipt.json` | `4986837da45cd59003cbb2ece74bfae2053e100f6bd28420c205bd30ac17064e` |
| `observe.py` | `6418640b47198f5c71881cd1eeced135b570a5eaa3ffadcad4a89723df8eac84` |
| `driver.py` | `53a7043563085003050105cb81b6012e6ab33205fa5a1904c0012750a6338080` |
| `inert_checks.py` | `bf14e7006434e50383305a9f7f2eceb3c6d2c7d715fded5969228371935cc507` |
| `final-2.merged.log` | `90514c9dea005eb14c19e9d0a56bd51dd3d92c6ac12a3dbb994250335958ba8b` |

1. **Manifest initialization prevents launch.** Observer line355 reads
   `driver.M['head']`, but importing the new driver leaves `M=None` (driver
   line5). The bounded manifest load occurs in `source_state()` only after
   `driver.START` is initialized; those calls currently follow the dereference.
   Every otherwise-valid invocation reaching this line fails before accounting
   or Popen. Initialize the existing driver deadline and bounded source snapshot
   before comparing its loaded head, retaining all manifest/provenance checks.
   Cover the actual observer bootstrap starting with `M=None`, with every native
   boundary faked/poisoned; current fixtures manually populate the driver state.

2. **The resource ledger is lost across startup and on prelaunch refusal.**
   Main lines377–403 accumulate positive free-space decreases in `s['decline']`
   during the pre-Popen sweep. `supervise()` line791 resets that field to zero
   and `last_free` to the original `initial`. For free observations100→90→100,
   a recorded decline10 disappears at the handoff; a later100 cannot recover it.
   Preserve the same accumulated decline/latest endpoint across that boundary,
   or fold it exactly once without a refund or duplicate charge. Also preserve
   the already-observed full carry, latest endpoint, complete maxima map and
   partial-accounting state if pre-Popen preparation refuses: current first/
   latest accounting receipts contain cursor summaries, and the outer setup
   failure receipt (line1029) contains only an error, so that path can lose newly
   observed charges/maxima entirely. Use bounded existing evidence paths and
   in-memory values, retain the primary reason, and perform no new traversal or
   resource read in the error path. Add actual handoff and prelaunch-failure
   cases with decrease/rebound/decrease and partial named growth; verify exact
   no-refund/no-double-charge accounting and evidence-write failure semantics.

3. **Root handling rejects a retained GC-root symlink.**
   `accounting_fingerprint()` lines126–130 rejects every root symlink before
   its own blocks are charged. The inherited ledger includes
   `/tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder-recursion-build-1`
   at4096B; retained recorder assessment lines22–23 identify its output target
   `/nix/store/lpz9w1ypglskjqgw6hzcs7q99a15mvi5-livepatch-first-hotplug-recorder-1`.
   If that preserved link remains present, this accounting pass necessarily
   refuses. This is a retained-layout compatibility finding, not a new live
   presence observation. Count the named link itself with `lstat`, preserve its
   maximum and bounded identity evidence, and never traverse its target or reuse
   it as an immutable directory observation. Keep strict no-follow directory
   identity/type checks. Test live-target and dangling root links plus directory
   substitution refusal. Do not delete the root, remove its ledger entry or
   reduce a maximum to avoid the refusal.

4. **Active-timeout-pending lost its admission resource checks.**
   P3 `sample()` lines492–504 required pending admission headroom/free43GiB/
   daemon+client8GiB/host20GiB and fresh live-handle/<5s checks. New `sample()`
   line279 and `accounting_then_admit()` line292 apply runtime stops, allow a
   slice, then return when startup is unproved. Strict admission checks now occur
   only in `admit()`. A pending observation at daemon9GiB, host18GiB, free42GiB
   or exhausted allowance can therefore be forgotten if it recovers before
   exact Bash proof, weakening the selected pending contract. Restore those
   pending checks before optional traversal, retaining present-client charging,
   the original deadline/live handle, sticky first failure and no FIFO open/token.
   Test each admission-only boundary while runtime predicates remain below their
   stops, using actual sample/accounting integration; later recovery must neither
   clear the failure nor admit. No broader inactive-pending tolerance is proposed.

The no-query boundary is otherwise appropriate: driver has no subprocess/Nix/
Git/Ruby-selector execution, binds retained raw `0e21ef83` and failed status
`caa43c84`, and writes a separate validation result. Its exact2404 content/mode/
symlink/directory, materialized-lock/seven-node/follows checks and bounded chunks
retain the selected meaning. Frozen source-state snapshots are not live Git
proof; retained native NAR identities are not recomputed by a custom serializer.
Byte comparisons match unchanged catalog1285be35/checkerb82015b3/manifest8e1cc5f3,
names/environment/tools and all four locks against P3. The two other catalogs,
actual TestScript/TagFilters, service/gem and VM gates remain unproved/held.

The full observer/driver diffs support the local cooperative design; this is
not whole-control equality. Control proof3b14dd38 lists21 normalized unchanged
authority/member/partial-birth/scan functions and the actual changed functions.
The no-follow cursor, bounded slices/active work, fixed evidence inventory,
cheap controls before optional work, failure suppression of further traversal,
same handle/one authenticated TERM, observation-only reference holds and one
scan followed by fresh ordinary reconciliation remain the intended boundary.
The corrections above require no worker, new signal authority or framework.
Cooperative checks still cannot bound a blocked filesystem syscall or prove
that the inherited map fits startup5s; no actual cadence/fit/peak claim is made.

Current suite-resultse933c172 binds47 actual-control cases to the exact sources
and suite above, with identical before/after hashes, producer0/reader0,2906B raw
and zero poison attempts. These are meaningful slicing, cheap accounting, FIFO,
supervision/cancellation/holds, provenance and copied-content refusal cases,
but omit the four transitions identified here. `current-final-*` is the retained
interim46 binding; `final-2.*` is current47. Historical92/80/39/syntax and interim
failures remain historical. Propose one corrected exact-current small suite
adding these missing actual transitions under the existing fake/poisoned bounds;
no rerun was performed or authorized by this inspection. Preserve current47 and
all old bindings before any selected edit.

Preservation d81de9a0/3299ecf8 records all429 old P3 paths/all323 bindings,108
copied files totalling5688831 logical bytes, nested-original references and FIFO
metadata only. Fixed inventory042f20cf reserves7773467 logical bytes across173
files/17 directories, including self-caps. The lead verified all171 frozen
entries; this inspection independently matched the core hashes and immutable
comparisons above, not a second all171 verification. Full carry5752246272,
endpoint134358052864 and all120 maxima5881446400 remain anchored to33e87b83;
each separate6GiB stop and the same512MiB allowance retain153333760B residual
before future gaps/preparation. No refund, ceiling change, cache assumption,
fresh capacity claim or operation retry follows. All RAM/free/log/time limits,
P3 INCOMPLETE disposition, hidden/protected/unsampled qualifications and future
lead-selection requirements remain unchanged.

#### Retained-source-validation-1 four-correction assessment: terminal receipt gap

The lead selected the four preceding corrections for owner3. Focused static
inspection of the returned package closes the manifest initialization, ledger
handoff, root-link and pending-admission defects. **Source acceptance remains
withheld for one narrow terminal-evidence accounting gap**, with one related
fixture correction. No package edit, check rerun or native operation is selected
by this assessment. Session/environment and roster32 ready/write bindings were
verified; saved settings remain unchanged. Only this design record is edited.

Independently matched SHA256 bindings under
`repair/support/final-head-source-validation-1/`:

| Artifact | SHA256 |
| --- | --- |
| `frozen.json` | `c66c14a1eef97074ba5b48fe6ae458e665430f3611138b8296be5140c6e9baa2` |
| `receipt.json` | `d81e14fd763e0de31e26dad6061241fdeb5e415e013efaf69fedde2c01312af9` |
| `observe.py` | `0fc9bb0fb581b20110f8293a322458b7de7193e8afbc15faa3e0832e37577d3b` |
| `inert_checks.py` | `448c08d3f7d6045759eaaee03320fa4f47d2a9c0a1c41f2e99fcdf97d526c55f` |

Actual old/current source comparison reproduces local diff42e019ea exactly.
Bootstrap now sets driver START and obtains the bounded source snapshot before
head comparison; the unchanged driver's `M=None` path is exercised by the
actual-prefix fixture, including wrong-head refusal. Prelaunch and supervisor
retain the same decline/latest endpoint without resetting or folding carry;
the actual-prefix-to-supervisor case verifies10 retained bytes plus5 later
bytes, not a net decline. The setup-error snapshot captures the already-observed
full charge, all maxima, latest free, partial accounting/cursor and first reason
before attempting output; it introduces no fresh resource read or traversal.

Root links charge their own `lstat` blocks before later identity failures,
capture bounded readlink length/digest, and skip target traversal and immutable
directory reuse. Expected type/device/inode/mtime plus no-follow directory
checks retain substitution refusal. Live-target/dangling/repeated-phase fixtures
exercise those paths without target metadata access. Pending admission now
rechecks full headroom/free43/RAM8/host20/present-client/live/<5 conditions in
sample, before an optional slice and after accounting evidence. Sticky failure
prevents later recovery from slicing or opening FIFO. The six pending refusal
cases cover admission-only resource breaches, native exit and exact5s.

**Remaining blocker: setup receipt bypasses the selected evidence budget.**
`setup_failure()` lines1086–1087 directly writes up to1048576B. It neither
reserves nor charges that output in `WRITE_ATTEMPTS`/`EVIDENCE_MAX`, and does not
check the12MiB other-evidence budget. Inventory893dfa6d reserves only the fixed
self-manifests (frozen/evidence inventory/receipt); listing the future setup
filename in `MUTABLE_NAMES` is not a reservation. A prelaunch receipt can exhaust
the accounted budget and cause refusal, after which this new terminal writer
still emits additional unaccounted bytes. No later sample runs to account for
them. Its separate1MiB serialization bound does not preserve the unchanged
aggregate/no-refund contract.

Minimal proposed correction, requiring lead selection: reserve this one bounded
terminal record inside the existing12MiB/32MiB accounting before normal evidence
can consume its space (the existing1MiB output cap is a possible reserve), and
account its single attempted write from already-held state without any new FS,
resource or traversal read on the error path. Do not refund unused reserve,
erase the primary failure or drop the full observed resource snapshot to fit.
Retain the current prelaunch snapshot and fixed error pathname; no new registry,
worker, retry, larger cap or generic writer framework is needed. Preparation
inventory9321690B leaves3261222B below12MiB before mutable evidence; this arithmetic
does not establish fresh physical/free-space headroom or reserve future writes.

The related fixture currently proves failure before writing, not the claimed
injected write failure: `FailedSink` at inert_checks.py334 inherits `Sink` at41,
which has no context-manager methods. Therefore actual `with ...open('xb')`
raises TypeError before its `write()` runs. Keep the historical result intact;
use a context-capable fake sink and explicit write-called assertion for the
corrected case. A focused bounded check should cover successful serialization
of full state, write failure retaining the primary/snapshot, and terminal-reserve
accounting at the existing budget boundary, with every native boundary poisoned
or faked. No check is run or authorized here.

Suite-resultsc72a1a42 and raw
`b7281332f3acf694fbd81bbeb94573e3a9fbe56d184d27155fa32fc34f956d34`
bind the current60 cases (47+13),3778B, producer0/reader0/poison0, with identical
source/test before-after bindings68d42b8e. The AST assertions bind the bootstrap
and pre-Popen statement prefixes to actual production source; native boundaries
are fake, so these remain bounded control evidence, not full startup/systemd/
store proof. The fixture issue narrows one case's claimed coverage and does not
invalidate the other transitions. Interim blocked poison attempt, remaining33,
historical47/46/92 and all earlier logs retain their original bindings.

Driver53a70435/run/native argv/environment/root/scope/ledger/resource proof and
retained bindings are byte exact. Independent comparisons also retain P3 catalog,
checker,2404 manifest, names/tools and four locks. Commands changed only the two
executed-suite evidence paths. Direct diff/control proof8f3303de limits changes
to the six existing functions and two local helpers named by the selected brief,
plus the two in-memory references; authority/member/partial-birth/drain/reference/
one-TERM/one-scan controls are unchanged. This is precise local equivalence, not
whole-control equality. No framework or product boundary expansion appeared.

Preservation66a61a00/inventory70b49e00 retains all171 old bindings and46 original
root files1072024B, all429 old P3 paths and FIFO metadata only, without nested
recopy. The lead's all240 current binding verification is not claimed as a second
independent all-file audit here. Fixed inventory242 files/21 directories includes
the stated self-caps. Full carry5752246272/latest134358052864/all120 maxima
5881446400/anchor33e87b83, separate6GiB stops only for this no-query operation,
same512MiB allowance and153333760B residual before fresh gaps remain unchanged.
All other RAM/free/log/deadline limits and blocked-FS/unsampled/protected/fit
qualifications remain. Failed P3 is still INCOMPLETE; later queries/selectors,
service/gem/VM, publication and integration remain held. Owner3 corrections,
fresh frozen source acceptance and eventual native selection stay with the lead.

#### Retained-source-validation-1 terminal correction: source accepted

**Focused source acceptance granted for the exact package below.** The lead's
selected terminal-reservation correction closes the remaining blocker at1797;
the four earlier corrections remain accepted. This is source acceptance only,
not native operation selection, source-store validation, selector execution or
systemd/kernel proof. The preceding findings and frozen historical identities
remain intact. Session/environment and roster32 architect0/implementer3
ready/workspace-write bindings were verified; saved settings are unchanged.
Only this acceptance record was edited, with no check or operation execution.

Independently matched SHA256 bindings under
`repair/support/final-head-source-validation-1/`:

| Artifact | SHA256 |
| --- | --- |
| `frozen.json` | `e04d49349f0a062268ab41e682160db97d5954c6b61c8adeb5959049cd1fb3c3` |
| `receipt.json` | `066a9a7e628b046eaadff8be1c6a94dd4ef370a7a24ea23dd859e59ed6fc59c5` |
| `observe.py` | `04e8bc81faf02ab8741743d8cc5d1e6364cb8119a12e37960e2b4554b8ea1ec8` |
| `inert_checks.py` | `f6cafdf25bb0a8393a3408064011e2576354c2e6c4d29ca8a84b3e8a6a072470` |
| `suite-results.json` | `1dfd498ddc6eaa10f2d844a07439798297f6eee855aaa4cd16cdb30852b50425` |
| `terminal-test-1.merged.log` | `996b93bf22f4e3144402b0378130159decfa19e17dc5c43f26608b467176a8dc` |

The terminal1MiB charge is initialized in the module before bootstrap and is
included by `evidence_size()` in the existing12MiB/32MiB consumers, including
when the file is absent. It cannot refund unused bytes. The single guarded
terminal attempt charges serialized length once in `WRITE_ATTEMPTS`, taking
the maximum against that same reserved entry rather than adding another1MiB.
The primary reason, full already-observed carry/latest endpoint/all maxima and
partial accounting/cursor are captured before IO. The error path performs no
new filesystem/resource/traversal read and does not call the normal evidence
scanner. An early-bootstrap failure invents no resource observation.

Successful, failed and short writes all consume the one attempt; a second call
returns the first in-memory result without serialization, charge or IO. An
oversized full snapshot remains in memory with the refused attempted length,
without open, truncation, smaller fallback, retry or cap increase. Receipt IO
failure still cannot guarantee a durable terminal file; the retained snapshot
and failure do not become an effects-ended or successful-operation claim.

Direct comparison against preserved observer0fc9 reproduces local difff560a7cb
exactly. Only `evidence_size()` and `setup_failure()` function bodies changed,
with fixed reservation/attempt module state; no function or authority was added.
Proof91deea6e's precise local boundary agrees with the diff. Main bootstrap,
ledger handoff, root-link/pending corrections, accounting cadence, one handle/
one authenticated TERM, member/partial-birth/reference/drain controls and one
scan followed by fresh ordinary reconciliation are unchanged. This is a
proportionate fixed-operation correction, not whole-control equality or a new
framework.

Current71 evidence is meaningfully bound: results1dfd498d/raw996b93bf record
4510B, producer0/reader0/poison0, and identical before/afterad0d0923 source/test
bindings. The retained60 plus11 cases exercise actual terminal serialization of
the full120-value ledger, write OSError, short write, early bootstrap, oversized
snapshot, one attempt, no unused-reserve refund/double addition, and normal
budget equality/+1 followed by the reserved terminal path. Context-capable sinks
and explicit write-called assertions close the prior fixture gap. Aggregate32MiB
cases correctly acknowledge that the12MiB predicate is already stricter in
those fixtures. All native boundaries remain faked/poisoned; these are bounded
actual-control checks, not a native or complete-conformance pass. Historical60
is explicitly qualified as context-entry TypeError for its old receipt case;
its raw and all earlier/interim evidence remain unchanged. No rerun was made.

Preservationa5f07381/inventory40a10f5f retains all240 historical bindings and11
changed root originals248927B, all429 old P3 paths/nested snapshots and FIFO
metadata only. Independently matched the preserved c66c/d81e/0fc9/448c/c72a
identities and historical rawb728. The lead's all262 current/all240 historical
binding audit remains distinct from this core/diff/immutable inspection.
Inventory157652a8 covers264 fixed files/23 directories:9824560B fixed logical
reservation plus1048576B terminal equals10873136B, leaving1709776B below12MiB
before mutable evidence. The existing manifest self-caps remain conservative;
the terminal reserve is a separate single counter entry, not a duplicate fixed
file row. This arithmetic does not prove fresh physical/free-space headroom.

Independent byte comparisons retain driver53a70435/run/native arguments/root/
scope, environment, catalog/checker/2404 manifest, locks/names/tools, ledger,
resource proof and retained bindings. Commands differ only in descriptive
executed-test evidence paths. Full carry5752246272B/latest134358052864B/all120
maxima5881446400B/anchor33e87b83 remain unchanged. Both separate6GiB stops apply
only to this no-query validation; same512MiB lifetime allowance and153333760B
residual precede all future positive gaps and preparation growth. No refund,
reset, future cache assumption or automatic ceiling increase is accepted.

Native execution remains **UNSELECTED**. Any later selected attempt must still
pass fresh identity/absence, complete phase accounting, charge-plus-allowance,
free43GiB/RAM8GiB/host20GiB admission and the unchanged runtime6GiB/free40/RAM12/
host16/client1GiB-noSwap,300s/+5s and evidence limits. Startup5s/30s active
accounting fit and blocked-syscall cadence remain unproved; sampled/protected/
hidden allocation qualifications stand. Retained P3 remains INCOMPLETE, and
the two queries, actual TestScript/TagFilters, service/gem/VM, publication and
integration remain separate held gates. No further source blocker was found
within this selected correction boundary.

#### Missing candidate prerequisite: retained disposition and recovery decision

**Recommendation: retain the partial evidence and HOLD native validation and
restoration.** This is a design-only decision brief; no implementation, check,
fetch, re-evaluation, restoration, retry, new root or owner3 assignment is made.
Source-accepted e04d4934/receipt066a9a7e and all existing helpers/roots remain
frozen. Session/environment and roster32 ready/write bindings were verified;
saved settings remain unchanged. Only this design subsection is edited.

Read and hash-matched the sibling
[prerequisite refusal](repair/support/final-head-source-validation-1-prerequisite-refusal.json)
`a9eac2e110b76f086685ab5893f71ec507f5709048eaa6ec1b4558c693ec61a8`.
It records TWO combined watcher preflights: the first has empty stdout and no
retained exit; the second exits42 without per-path failure identity. Neither
launched the observer/native command, created an operation handle or created
runtime/log directories. The later targeted metadata observation reports ENOENT
for the exact candidate and a regular0555/15776B Python file. It does not identify
which earlier prerequisite failed, establish interpreter/runtime capability or
explain when/why the source disappeared. No new free-space endpoint, allocation,
refund or cleanup proof follows. Do not retry the combined guard to obtain a
different outcome or alter the accepted validator to accept a missing source.

**What remains valid without materialization.** Preserve P3 raw
`0e21ef8370ec05b961112137a18d2db0a2da4b67833276f6924cc7aec91b39c1`,
failed status `caa43c840e964aa3ab5ddf47a3199c1a3d45923bcb3b65cfd3cdb57fde4c39b3`,
the native0/BOTH_EOF observation and its permanent cancellation/overflow failure.
Retained default names/tags and full native candidate/production lock/node/follows
projection remain historical partial evidence. Manifest8e1cc5f3 binds2404 Git
entries to f746/tree1bbd; it is a byte/mode/target specification, not a copy of
the source contents or a fresh materialization proof. No default-complete,
three-gate or native-selector PASS may be inferred. A retained-byte-only
disposition can record these facts now without running a reduced validator,
constructing substitute successful receipts or re-evaluating default metadata.

The exact restoration target, if separately selected, remains:

- Commit `f74629fa4046089e2c53d0cb0e3ba7ef5b178e82`, tree
  `1bbd234662cbe595e781dcba4c0b43c5a839f15e` and the frozen2404-entry manifest.
- Native path `/nix/store/xdbmyp84w9zasqpiqj3420r538yksbch-source`, native NAR
  `sha256-WMD5deXzowI9D17NfQOLvBe+TbMoGQFPhVq0CZhzCPw=` and candidate lock
  SHA256 `fd0361f861091aa982959b422df27e76748ee26946923cdbd9ef2509b7474be1`.
- The original immutable local Git URL at design391, including the explicit
  feature ref and f746 revision. A dirty/path-flake checkout or an arbitrary
  copy is not an equivalent origin. Stopped4de/inmh/vp408 evidence supplies no
  final source identity or recovery acceptance.

**Supported route versus missing proof.** Retained P3 driver/catalog source
establishes the pinned Nix2.34.9 `nix-instantiate --eval --strict --json` route
with IFD false, empty builders, fallback false and max-jobs0, using
`builtins.getFlake` on that exact URL. This is a Nix re-evaluation/materialization
primitive, not a source-only read or a no-fetch guarantee. A smaller expression
could request only `{ sourcePath = root.outPath; rev = root.rev; narHash =
root.narHash; }`, asserting all three expected values, without importing the
catalog. However the retained sources do not establish that `getFlake` itself
avoids input-lock fetching/materialization. I therefore do **not** certify that
fallback as a root-only restoration command within the proposed small stage.

The desired smaller operation is one native fetcher/prefetch of the exact local
Git root, followed by native path/NAR identity and the already-frozen source
validation. It must not evaluate outputs, traverse the input graph for fetching,
build a derivation, clone a remote repository, restore SDK/kernel/toolchain/ZFS
inputs or silently substitute another source. Targeted static reads of the
retained Nix package's HTML and uncompressed/compressed man-page locations for
`nix3-flake-prefetch` found no files; this is only a documentation-location gap,
not proof about the installed command's existence or capability. No Nix help,
store listing, source fetch or cache query was used. A version-matched retained
manual/source reference is still required before supplying a certified literal
root-only argv and its allowed-effects list. Do not invent flags or infer an
offline/no-input-fetch guarantee from the original evaluator's max-jobs0.

No existing retained binary-cache location/NAR archive is established for xdb.
A future cache-copy route would require its own exact source endpoint, native
NAR/reference/signature and size evidence; no availability or fetch selection
is implied. Git export plus `add-path`/NAR import is a different copy/import
operation with additional coexistence cost and native hash verification, not
the original fetcher's proof. It is not recommended here. The accepted no-Nix
validator cannot perform any of these operations, and needs no source rewrite.

**Finite resource disposition.** Preserve immutable33e87b83 full carry
5752246272B, endpoint134358052864B and every120 maximum totalling5881446400B.
The6GiB/6442450944B separate stops and SAME512MiB/536870912B lifetime allowance
apply only to the accepted no-query validation. Its residual153333760B precedes
unknown preparation/preflight/documentation growth and all later positive gaps.
An increased free-space reading cannot refund earlier shared declines or the
named candidate's347009024B retained maximum. That maximum is a past observed
allocation reference, not a new measurement or guaranteed restoration size.

| Planning scenario, not a measurement or selected operation | Cumulative carry plus same allowance | Relation to6GiB |
| --- | ---: | ---: |
| Existing carry +512MiB | 6289117184B | 153333760B residual |
| Above +one347009024B source allocation | 6636126208B | 193675264B short |
| Above +two347009024B allocations +32MiB evidence | 7016689664B | 574238720B short |

Two such allocations without the allowance or evidence already give
6446264320B, exceeding the cumulative6GiB stop by3813376B. A restoration that
finishes below the runtime stop can nevertheless leave insufficient headroom
for a later unchanged512MiB validation admission. Do not consume the allowance
as though it were permission to waive that next admission predicate.

For comparison only,7GiB/7516192768B cumulative would leave499503104B after
the two-copy+32MiB+same-allowance scenario. **No7GiB ceiling is selected or
recommended for execution yet:** two copies are an illustrative coexistence
scenario, not a proven bound on Git-cache, unpacking, temporary/store/database
or foreign shared movement. Under that scenario the named6GiB stop could stay
unchanged: the same root's old maximum is already carried, while one distinct
temporary347009024B maximum plus32MiB would total6262009856B. Never remove an
old entry, refund its blocks, deduplicate without proof or reset to a new stage
ledger. Any later finite revision must explicitly select cumulative and named
limits separately, carry every observed gap/maximum forward, and preserve enough
headroom for the next validation. These arithmetic options do not authorize it.

**Minimum prerequisites for a later proposal, not checks selected now:**

1. Read a version-matched native root-fetcher/prefetch implementation/manual
   establishing its exact argv, local-ref/revision handling, input/submodule/
   promisor/network behavior, native NAR/path result and temporary/cache effects.
   If it cannot be bounded to the exact local root, stop rather than use the
   broader evaluator as an implicit substitute.
2. Separately authorize a finite read-only origin/object check for f746 and its
   manifest2404 blobs/ref, with no lazy fetch or Git mutation, plus literal
   required tool identity checks. Current object/tool availability is not proved
   by historical hashes or Python execute-mode bits. Do not scan the store or
   query caches. Check the exact candidate and production roots/lock files
   needed by the accepted validator; its node-identity comparisons use retained
   metadata, so this does not require refreshing every locked dependency.
3. Obtain one explicitly selected fresh resource admission observation and a
   bounded temporary/coexistence estimate for the chosen root-only operation.
   Charge the positive endpoint gap from134358052864 and all subsequent
   decreases, with no refund. The present records cannot support native recovery
   under the existing no-query authorization. Lead must choose a separate finite
   restoration budget and a carry-forward route that can still admit validation,
   or retain HOLD. A capacity wait alone cannot repair a monotonic budget deficit.

If those prerequisites support recovery, owner3 may later be assigned a new
fixed package such as `repair/support/final-head-source-restoration-1/`, with
fresh operation/scope/evidence identities and the unchanged accepted validator
as a separate consumer. That name is only a proposal, not an absence check or
reservation. The package must freeze its single native materialization argv,
environment and allowed root, bind native expected path/NAR/revision, preserve
all original packets/raw, and retain qualified cancellation/effects evidence
under the existing policy watcher/control pattern. Keep client1GiB/noSwap,
whole exact daemon+client8/12GiB, host20/16GiB, free43/40GiB, finite300s/+5s
and bounded32MiB evidence unless an explicit later design decision changes them.
No hard owned-RAM/peak/blocked-filesystem guarantee or protected-effects-ended
claim follows. Missing another source/tool stops and returns to lead; it does
not widen the restore graph, fetch tools, increase a ceiling or launch a retry.

Lead's necessary decision is HOLD with the genuine retained partial evidence,
or select the bounded documentary/origin/resource prerequisite preparation for
a separate restoration proposal. No owner3 dispatch or native command is made
here. After any selected restoration, unchanged validation still needs separate
fresh admission and execution selection; its new result must name restoration
provenance without rewriting P3. The remaining two native catalogs/actual
TestScript+TagFilters, service/gem/production VM, publication/integration and
session lifecycle remain held.


#### Nix 2.34.9 documentary prerequisite: supported root prefetch, recovery still held

**Lead selected only this bounded documentary investigation after accepting the
preceding HOLD/partial disposition.** The documentation gap is now resolved:
upstream Nix2.34.9 supports `nix flake prefetch --json <flake-url>` as a native
root-tree materialization primitive without locking flake inputs or evaluating
outputs. This establishes a command proposal, not a selected restoration or a
fresh origin/resource check. Registries, complete local Git object/history
availability and finite store/cache/coexistence costs remain prerequisites.
The accepted e04d4934/066a9a7e validator and all old packets/roots/raw remain
unchanged; no owner3 assignment, retry or source preparation is made.

**Documentary provenance and bounds.** Session/environment match and roster32
architect0/implementer3 ready/workspace_write were reverified; saved settings
were not changed. Twelve specifically named HTTPS GETs targeted only
`raw.githubusercontent.com/NixOS/nix/2.34.9/`: eleven HTTP200 bodies total
231022B, largest66227B, and one HTTP404 for
`src/libflake/flake/flakeref.cc` (zero retained body bytes). The actual file is
`src/libflake/flakeref.cc`, listed below. That404 is a path-location miss, not
a missing feature. Each request used a30s total timeout and1048576B cap, with
no redirect/retry/crawl/search; total is below8MiB. Bodies were read in memory
and SHA256-hashed, not installed or saved as a source/tool checkout. These are
official exact-tag references, not a moving latest branch or proof of a signed
tag/installed package source commit. Retained tools.json binds the installed
2.34.9 canonical binary to
`6b20a492de8d0b2cf67e68d4cad1773a132753aa2909d8ddcdd44345c869e171`;
package patches/library provenance and current availability were not checked.

| Exact-tag reference | Body bytes | SHA256 |
| --- | ---: | --- |
| [src/nix/flake-prefetch.md](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/nix/flake-prefetch.md) | 946 | `fa3d9063ed8bd055269df72e08e309448b80ec26a2224111a4e7172785bad375` |
| [src/nix/flake.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/nix/flake.cc) | 66227 | `3d17abc8a92a6d3b42f6808750ad7d3e1e8bcabc3070d7d4169d7816c6c9d4eb` |
| [src/libfetchers/git.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/git.cc) | 42962 | `cf2a1c4cefd2172a176203f09b3e57befb7964e9a600bdc720ef4b4afb30a811` |
| [src/libfetchers/fetchers.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/fetchers.cc) | 16633 | `65a92870de452842d1e1d74b13439979a036e6d4ffd3976f62229998ca26fbea` |
| [src/libfetchers/fetch-to-store.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/fetch-to-store.cc) | 4758 | `c111f081878742d982bf12381ee371f0897f47d0ed4e3f341f3b87792d792a15` |
| [src/libfetchers/git-utils.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/git-utils.cc) | 54312 | `1ea3ed7c4c9ecf5b25f682d744ad70d704a3f37ba239a8d0ef5173bb0596c355` |
| [src/libflake/flakeref.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libflake/flakeref.cc) | 12693 | `1ac02653507600a28f6310415c5e3403f30dece7d7857f799ec6f0d158635935` |
| [src/nix/main.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/nix/main.cc) | 18972 | `59026f920ce966dbb8f462cf614b2ca95c42703d3ad3300af3c4d76a7614ad14` |
| [src/libfetchers/cache.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/cache.cc) | 4860 | `538818bc60e5d712bde16e4c7c1c4e0af70b5c70bfede531eb0280bd81dfd83a` |
| [src/libfetchers/registry.cc](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/registry.cc) | 7523 | `b92ad8a6f67b5bdb58fa77d7512e4aa1a7569ee265c6156aca8ce6d9b26d04a0` |
| [src/libfetchers/include/nix/fetchers/fetch-to-store.hh](https://raw.githubusercontent.com/NixOS/nix/2.34.9/src/libfetchers/include/nix/fetchers/fetch-to-store.hh) | 1136 | `e25a147198cf9f385f9838ff3615445c95ce27f0b80ac9147bcf492c066cda4e` |

**Supported argv proposal, never executed here.** The minimal primitive is the
canonical `bin/nix` below, followed by `flake prefetch --json` and the exact
original immutable URL as one argument:

```text
/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix
flake
prefetch
--json
git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos?ref=refs/heads/2026-10-22-ci-failure-analysis&rev=f74629fa4046089e2c53d0cb0e3ba7ef5b178e82
```

Each line above is one argv element, not a shell script. Use canonical
`bin/nix`, not the retained `nix-instantiate` argv0: main.cc dispatches legacy
commands by executable basename before new-CLI handling. A future frozen
package must explicitly provide the required nix-command/flakes features and
its effective configuration. Supported `--offline` and
`--option flake-registry ""` are useful proposed constraints before the
subcommand, but are **not a complete no-network policy**. No new prefetch flag,
`--refresh`, evaluator fallback, path-copy substitute or altered URL is proposed.
The minimal primitive omits `--out-link`; that documented optional flag creates
an output link/root on a local filesystem store. Any new retention root needed
between restoration and validation must be separately named/selected before
freezing that stage, not inferred as permission to alter existing roots.

**What the inspected implementation establishes.**

- flake.cc `CmdFlakePrefetch::run` (1498-1527) parses/resolves one reference,
  calls its lazy fetcher/accessor, then `fetchToStore(..., FetchMode::Copy)`
  and obtains the native NAR from store path info. It does not call
  `lockFlake`, read/evaluate the root's flake inputs/outputs or build a
  derivation. `getEvalState()` supplies settings here; that call is not proof
  of catalog evaluation. The manual also permits roots without flake.nix.
  This is root-only regarding the flake dependency graph, not a claim of zero
  auxiliary filesystem, registry or store effects.
- git.cc `inputFromURL`, `getRepoInfo` and `getAccessorFromCommit` accept
  explicit ref+rev. For an existing non-bare local file repository, with
  `_NIX_FORCE_HTTP` not1, the code opens that repository and reads the exact
  revision. It neither exports dirty working-tree files nor substitutes HEAD.
  With rev supplied, it does not resolve the ref to select the revision and
  leaves a FIXME for checking rev ancestry of ref. Therefore successful
  prefetch would not independently prove current branch ancestry/HEAD/tree.
  Those origin facts remain a separate prerequisite tied to f746/tree1bbd
  and the frozen2404 manifest.
- Effective submodules/LFS/exportIgnore/allRefs defaults in the inspected
  getters are false. The original URL leaves them disabled; do not enable
  them to repair missing data. No submodule traversal or LFS smudging is on
  that branch. `getShallowAttr` also defaults false in executable source,
  despite this tag's adjacent attribute documentation saying true. Preserve
  the actual source behavior and original URL, not a new shallow flag:
  missing revision-count cache entries can cause a parallel traversal of
  all ancestor commits (`GitRepoImpl::getRevCount`), in addition to the root
  trees/blobs. “2404 files exist” alone does not establish that prerequisite.
- Local commit/tree/blob reads use libgit2; inspected missing-object paths
  throw, with no explicit local-branch Git fetch fallback. `lazyFetch`
  denotes accessor creation; Copy subsequently consumes the tree. This is
  not proof of installed libgit2 promisor/backend behavior or object
  completeness. Preserve GIT_NO_LAZY_FETCH=1/GIT_OPTIONAL_LOCKS=0 from the
  retained environment, but do not present Git-CLI environment controls as
  a demonstrated libgit2 network guarantee. A later bounded prerequisite
  must refuse incomplete/promisor/unsupported alternate-object arrangements,
  rather than hydrate them or change the URL. Do not infer present repository
  configuration from this source inspection.
- Bare/local-without-.git paths or force-HTTP take a different branch:
  gitv3 cache creation/locking and possible Git CLI fetch, including temporary
  repository initialization. Those are outside the intended local-direct
  proposal. The actual source branch and config must be established before
  any later materialization; a file:// spelling alone does not guarantee it.
  No Git-cache clone or remote fetch is selected as a fallback.

**Registry/network boundary is consequential.** Prefetch unconditionally calls
`originalRef.resolve`; flakeref.cc routes resolution to registry lookup.
registry.cc considers flag/user/system/global entries before its final
direct-input check, and can rewrite a fully specified Git input. The global
registry may itself download a file and add a cache root. Empty
`flake-registry` suppresses that global registry, not the user/system
registries. The prefetch path does not pass its lockFlags into resolution;
do not infer that a similarly named lock/evaluator registry option disables it.
A later exact environment proposal must establish no applicable flag/user/system
rewrite and suppress global download before allowing this primitive. Comparing
JSON afterwards cannot undo an already fetched foreign source.

main.cc's `--offline` sets useNet=false, then changes substitution, freshness
and transfer defaults only when their settings are not already overridden.
It does not create network isolation or gate the Git CLI fetch branch.
Consequently offline alone cannot certify no fetch; effective substitution and
registry settings plus the direct/local-complete path need separate selection
and verification. The twelve-file budget is exhausted; no further source,
library or configuration investigation is silently added.

**Native identity and effects for a later stage.** JSON exposes top-level
`storePath`, `hash`, `original` and `locked`. The field named `original`
contains the *resolved* reference's attributes, so retain the literal requested
URL independently and compare both returned attribute sets to that request.
Require type/url/ref/rev unchanged, locked rev exactlyf746, top-level hash
`sha256-WMD5deXzowI9D17NfQOLvBe+TbMoGQFPhVq0CZhzCPw=` and exact path
`/nix/store/xdbmyp84w9zasqpiqj3420r538yksbch-source`. Do not require an
invented JSON `narHash` field: this command's native hash is `hash`.
A zero exit with a mismatch is refusal, not equivalence.

fetch-to-store.hh defaults to NixArchive and name source; fetch-to-store.cc
uses SHA256 and a content-derived store path with no references. It may reuse a valid
fingerprint/cache result, otherwise calls store.addToStore and queries native
path info. It can add a temporary GC root and update source-hash metadata;
git.cc also caches lastModified/revCount. cache.cc opens/creates
fetcher-cache-v4.sqlite with configured WAL behavior. Thus even the intended
local branch permits store import/database/temp-root and bounded fetcher-cache
metadata effects; it is neither a read-only check nor a source derivation build.
The store/daemon import's temporary-copy layout and physical peak were not
proved by these files. No assumption of one-copy allocation, empty cache,
cache hit or no daemon-side overhead is justified. Native path-info NAR plus
a later complete manifest byte/mode/symlink/lock comparison retain distinct
roles; the existing no-Nix validator is not replaced.

**Minimal next decision and unchanged HOLD.** The documentary prerequisite is
complete at the release-source level. Lead may separately select a finite
read-only prerequisite for the exact tool/provenance and effective registries,
the non-bare local origin/ref/revision plus necessary local object/history
coverage, and a finite resource/coexistence estimate. Nothing in this assignment
selects those checks or restoration preparation. A registry redirect, missing
object, unsupported promisor arrangement, absent tool or insufficient finite
margin returns to lead; no remote hydration/cache query/evaluator retry follows.

Full carry5752246272B, last endpoint134358052864B, all120 maxima5881446400B and
the SAME512MiB allowance remain anchored to33e87b83, without refunds or new
measurements. The6GiB stops still authorize only already-present-source no-query
validation. Its153333760B residual precedes all unknown gaps/preparation growth;
even the historical347009024B one-source allocation exceeds that residual by
193675264B before auxiliary effects. Documentary support does not select6GiB
fetching or a7GiB ceiling. Recovery stays HOLD pending an explicitly selected
finite contract with room for subsequent unchanged validation. Retained P3
partial evidence/permanent failure, later two catalogs/native TestScript+
TagFilters, service/gem/production VM and publication/integration/lifecycle
remain as previously recorded. This changes no product compatibility or
deployment behavior and leaves the accepted validator/source packets frozen.


#### Finite read-only origin/config/object prerequisite — execution brief only

**Subsequent lead selection — source/check preparation only.** Lead read the
full brief and assigned owner3 bounded preparation of the fixed
`final-head-source-prerequisite-1` packet under message `dd300f12`. The exact
brief, static checks and ONE small fake-boundary actual-control suite are now
selected for owner3; native filesystem/process/clock/signal/subprocess boundaries
in that suite remain faked or poisoned. Architect records this decision only:
no implementation takeover, tests, extra HTTP or native checks are selected
for architect. Owner3 must return the frozen exact packet for fresh source
acceptance before any separate operation-selection decision.

Lead explicitly extends the SAME separate 6GiB (6442450944B) cumulative and
known-subset stops and SAME 512MiB (536870912B) lifetime planning allowance
ONLY to this read-only origin/config/object prerequisite alongside the accepted
no-query validator. This is a finite scope extension, not an added allowance,
refund, reset, fetch/restoration authorization or permission for the remaining
queries. No 7GiB ceiling is selected. The new ledger must bind both immutable
33e87b83 and endpoint receipt4e685a34, carry5840527360B with latest endpoint
134269771776B, and preserve all120 inherited UNREFRESHED maxima totalling
5881446400B. Residual65052672B is before all later positive gaps and preparation
growth; no current fit, RAM, maxima or admission proof follows. The whole new
durable packet remains <=8MiB inside the existing32MiB lifetime evidence cap.

This selection supersedes only the original preparation/check and budget-scope
status below. All original rationale, limits, provenance uncertainty and failed
evidence remain. Actual operation, current Git/config/object probes, resource
resampling, restoration and validation execution remain UNSELECTED; the
installed-provenance and temporary-space HOLD is unchanged. Accepted validator,
raw evidence, roots and saved settings remain untouched.

**Selection/status at the original brief.** Lead selected this source-only brief, not its preparation
or execution. No Nix/Git/helper/object check, extra HTTP request, owner3 dispatch,
restoration, capacity resample or test is authorized here. Roster32 and the
session/environment binding were reverified without changing saved settings.
Only this design is edited. The preceding twelve-file release-source inventory
is reused; installed source/patch/library equivalence and store temporary-space
bounds remain unproved. This prerequisite can produce partial evidence, never
authorize restoration or replace the frozen e04d/066a no-Nix validator.

**Static observations used to name the finite scope.** A bounded read of the
literal worktree `.git` file says
`gitdir: /home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git/worktrees/vpsadminos4`;
that named directory's `commondir` file says `../..`.
These are pointer bytes, not fresh Git/object/ref validation. Readlink of the
two named system Nix files gives `/etc/static/nix/nix.conf` and
`/etc/static/nix/registry.json`. A bounded, value-redacted system nix.conf
excerpt showed `experimental-features = nix-command flakes`,
`fallback = true`, `sandbox = true`, and configured builder/substituter
keys. It is not a complete effective-settings or running-daemon receipt.
No registry contents, Git objects or repository status were queried.

Use these literal abbreviations below; they are fixed paths, not discovery:

- W = `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos`.
- D = `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git/worktrees/vpsadminos4`.
- C = `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git`.
- G = `/nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin/git`.
- R = `f74629fa4046089e2c53d0cb0e3ba7ef5b178e82`;
  T = `1bbd234662cbe595e781dcba4c0b43c5a839f15e`;
  B = `refs/heads/2026-10-22-ci-failure-analysis`.
- M = the existing2404 manifest
  `8e1cc5f3ae1daf241851dbfbe78c1b3d64be3ddff0ce80408e9bf48ace0cc243`,
  read from the frozen validation packet, never reconstructed from a checkout.

**Proposed package boundary for a later choice.** Owner3 could prepare one
fixed `repair/support/final-head-source-prerequisite-1/` packet, referring to
old immutable evidence by hash/path without copying old source trees again.
This proposed name has not been checked/reserved/created. Freeze the following
literal command table, input manifest, environment, limits, file allowlist and
secret-safe receipt schema before asking lead to select execution. No changes
to the validator, old helpers, query/checker, product or source tree. A later
fresh policy watcher may supervise the selected operation; this brief adds no
registry resolver, generic monitor, release API or new signaling authority.

The proposed stage is read-only against repositories/configuration/store;
only a separately selected fresh evidence directory may be written. Limit the
whole prerequisite to120s plus the existing5s escalation allowance, within the
existing300s outer ceiling; each command gets the smaller of its listed limit
and remaining stage time. Preserve hard client1GiB/noSwap, original authority/
handle/drain/first-failure/finalization requirements, and applicable unchanged
RAM/free-space admission rules. These are proposed bounds, not a duration,
physical-fit or blocked-filesystem guarantee. A cap/timeout/error is INCOMPLETE
and stops later commands, without retry, hydration, automatic maintenance or
limit increase. Unresolved owned effects retain the existing hold contract.

**1. Literal tools and static provenance, no execution of Nix.**

Read/hash only the already-named canonical Nix and Git binaries, the
nix-instantiate symlink, existing tools.json and M. Nix must remain regular0555,
4024904B and SHA256
`6b20a492de8d0b2cf67e68d4cad1773a132753aa2909d8ddcdd44345c869e171`;
Git regular0555/4753856B and
`f97ba8863b93a05b4193c5c436d95c62bb3879c96024753d764cf74d1594e027`.
The symlink target must remain `nix`. Cap M at1MiB and tools.json at64KiB;
require M's retained hash and exactly2404 entries before using any object IDs.
Cap each binary read at8MiB and their aggregate at16MiB, hash in64KiB chunks,
retain before/after file identity and byte count; any mismatch refuses before
Git execution. No ldd, loader, version,
help, Nix database/deriver query or sibling-store discovery.

Keep separate receipt fields for retained binary identity, upstream2.34.9
reference hashes, installed source revision, applied patches and libgit2
provenance. The last three currently have no established exact static source
pointer: record UNPROVEN, not a fabricated empty patch set or equality to tag.
Do not follow arbitrary ELF strings or search the store for a derivation.
This gap blocks restoration certification even if the independent read-only
origin/object portion later completes.

**2. Named configuration and refusal gate before object-bearing commands.**

The only proposed static file subjects are:

| Purpose | Named subjects |
| --- | --- |
| Nix system/user configuration | `/etc/nix/nix.conf`, `/home/aither/.config/nix/nix.conf`, `/etc/xdg/nix/nix.conf` |
| Nix registries | `/etc/nix/registry.json`, `/home/aither/.config/nix/registry.json` |
| Git configuration | `/etc/gitconfig`, `/home/aither/.gitconfig`, `/home/aither/.config/git/config`, C/config, D/config.worktree |
| Exact worktree/object indirection | W/.git, D/commondir, D/gitdir, D/HEAD, C/HEAD, C/objects/info/alternates, C/objects/info/http-alternates |
| History/replacement hazards | C/shallow, D/shallow, C/info/grafts, D/info/grafts, C/packed-refs, D/packed-refs; direct entries only in C/refs/replace, D/refs/replace and C/objects/pack |

No recursive configuration discovery or includes. Freeze a maximum8-link
resolution per named subject, accepting only the recorded W/D/C paths and
ordinary `/etc`, `/nix/store`, or the named user's configuration paths;
record the exact resolved chain. Refuse escape, loop, FIFO/device, unexpected
directory, unreadability or change during read. Optional missing configuration
is recorded ENOENT, never treated as evidence about missing Git objects.
Require the source .git/commondir links to resolve to exactly D/C.
An existing linked worktree can legitimately use a bare common repository:
do not reject C/config solely for core.bare=true. The origin W must instead
prove non-bare/inside-worktree through the explicit Git command below.

Limits: pointer files4096B each; config files64KiB each; each registry256KiB,
at most1024 entries; packed-refs1MiB each; total static text4MiB and64 file/link
subjects. Enumerate only the three named directories above, at most4096 total
direct entries, no descendant walk or pack-content scan. Reject any replacement
entry (including packed refs/replace), any graft/shallow file, any alternate
file (even empty, conservatively), and any .promisor sidecar. Reject
extensions.partialClone, remote.*.promisor, partial-clone/filter declarations,
Git config include/includeIf, Nix include/!include, config-selected object
indirection or unclassified parse ambiguity. Do not follow include targets.
Known benign worktreeConfig/repository-format fields are recorded rather than
confused with promisor state. Unsupported extensions or repository format stop.

Receipt output never contains raw config, credential/helper values, headers,
tokens, remote URLs or environment dumps. Record whole-file SHA256, byte count,
identity, setting names and secret-safe semantic verdicts; only preapproved
booleans/numbers/feature names and fixed local paths may be displayed.
No per-secret-value digest. Unclassified values are withheld and relevant
uncertainty refuses; do not “redact” after writing a raw log.

For registries, require well-formed version2, unique JSON keys, maximum16 nesting
levels and4096B strings, within the stated file/entry limits.
The smallest sufficient local proof accepts only empty registries or entries
whose `from.type` is `indirect`: those cannot match this starting Git input
under the inspected Input equality/contains logic. Refuse direct-Git or other
unclassified entries rather than implement general normalization/rewrite
semantics. Unmatched `to` values are not traversed or printed. Flag registry
must have no overrides in the frozen future argv. Proposed global registry is
empty via explicit `--option flake-registry ""`; its currently configured
URL/path may be classified and redacted but is never fetched or followed here.
Any nonempty selected global registry is outside this packet and returns to lead.

Distinguish the **planned settings projection** from actual installed or daemon
effective settings. The future prefetch proposal must freeze required features,
global-registry disablement, explicit no substitution, empty builders,
fallback=false, max-jobs0 and IFD=false; observed system fallback=true cannot
stand as that contract. The exact child environment must replace, not merge,
ambient values. Retain literal HOME/user/PATH/daemon endpoint and
GIT_NO_LAZY_FETCH=1/GIT_OPTIONAL_LOCKS=0; admit no _NIX_FORCE_HTTP, NIX_CONFIG,
unaccounted Nix config/path override, GIT_DIR/WORK_TREE/COMMON_DIR/OBJECT_DIRECTORY/
ALTERNATE_OBJECT_DIRECTORIES, replacement namespace, config-count/parameter
injection or credential/transport helper override. Report only presence/type
verdicts, never secret values. Do not change HOME.

The twelve obtained files establish registry resolution, not the installed
configuration loader's complete precedence or daemon's startup settings.
Unknown loader/patch/override behavior remains UNPROVEN and keeps recovery
held; no Nix show-config/help/evaluation is part of this prerequisite.
CLI protocol/config controls below concern Git CLI only and are not libgit2
network isolation. No native claim is upgraded from a static file match.

**3. Exact proposed read-only Git argv and coverage.**

For every row use this common argv prefix, with W and G expanded literally:

```text
G --no-optional-locks --no-replace-objects
  -c protocol.allow=never -c protocol.file.allow=never
  -c core.fsmonitor=false -C W
```

Use the exact retained environment.json allowlist plus GIT_TERMINAL_PROMPT=0 and
GIT_PAGER="", with no inherited additions. No optional filter/textconv,
network helper, shell expansion, Git maintenance or index/status command.
Do not enable an alternate or fetch
a promised object to satisfy a failure. A Git CLI unsupported-option failure
is retained and stops; it does not select alternate flags or a retry.

| Order | Suffix argv | Required result | Subdeadline / stdout cap |
| --- | --- | --- | --- |
| 1 | `rev-parse --is-bare-repository --is-inside-work-tree --absolute-git-dir --git-common-dir --show-object-format` | false, true, exact D, common path resolving to C, sha1 | 5s /16KiB |
| 2 | `symbolic-ref --quiet HEAD` | exact B | 5s /4096B |
| 3 | `rev-parse --verify HEAD^{commit}` | exact R | 5s /4096B |
| 4 | `show-ref --verify --hash B` | exact R | 5s /4096B |
| 5 | `rev-parse --verify R^{tree}` | exact T | 5s /4096B |
| 6 | `ls-tree --full-tree -r -t -z R` | root tree's complete directories and2404 manifest leaves | 15s /4MiB |
| 7 | `rev-list --parents R` | complete reachable ancestor-commit graph including R | 20s /4MiB |
| 8 | `cat-file --batch` | full native object bodies for the bounded exact OID set below | 60s /bounded streaming bodies |
| 9–11 | Repeat only rows2,3,4 after all reads | same B/R/R, no intervening selected mutation | 5s each /4096B each |

This is at most eleven serial Git children, never parallel/unbounded launches.
Rows9–11 are planned before/after identity evidence, not retries or busy polling.
Recheck hashes/identities of the same static gate subjects at the end, under the
same aggregate limits; no new subject/path discovery. A changed config/ref or
membership list invalidates the snapshot. This does not prove atomicity,
absence of ABA mutation or future origin state. Dirty worktree contents are
neither read nor substituted: the target remains explicit R.

Row6 must have exactly M's paths, Git modes and blob IDs, with no duplicate,
unknown leaf, gitlink/submodule, extra path or missing entry. Permit only
100644/100755/120000 leaves; each path at most4096B, directory set exactly the
parents of M, at most8192 directories. Include T plus all returned tree IDs in
the batch. Row7 permits at most32768 unique commits,64 parents per commit and
4096B per line; any truncated/missing/overflow graph refuses. Its closed parent
set alone is not enough: commit-graph acceleration can avoid reading bodies.

Build one deduplicated batch input of only those tree IDs, M's blob IDs and
the row7 commit IDs; cap45000 IDs and2MiB stdin. Never use batch-all-objects.
Feed one bounded OID request at a time while draining stdout and stderr; do not
block writing the entire request set against a child blocked on its response.
After the last complete response, close stdin and require both output EOFs and
native exit0 within the same deadline. Retain the same handle on every error.
Each response must match the requested OID/type/declared size and exact framing;
missing/ambiguous/short/extra output is refusal. Stream blobs in64KiB chunks,
compare their complete SHA256/length to every matching M entry, and recompute
Git SHA1 over the native type/size/body for every object. Symlinks are blob
bytes, never followed; executable mode comes from row6. Do not log object bodies.

For commits, validate the full body hash and header tree/parent records,
deduplicate IDs, require every raw parent to be in the row7 set and the row7
parent list to agree. R's parent must be the retained
`39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17`; its tree must be T.
The resulting closed, completely readable ancestor set is the revCount
availability evidence; it is not a cached count or proof of Nix/libgit2 speed.
Historical commits' file trees/blobs are not traversed: revCount needs commits,
while materialization needs only R's complete tree/blobs.

Processing ceilings are explicit refusal thresholds, not measured source sizes:
M's total leaf bytes must be <=384MiB and each blob<=64MiB before row8 starts;
aggregate commit bodies<=16MiB/individual256KiB; aggregate tree bodies<=16MiB/
individual1MiB. Batch body stream<=416MiB plus4MiB protocol framing.
The current assignment does not calculate those sums or assert that they fit.
Hash/discard streaming data, bound graphs/buffers; never accumulate or write
the full source. If a required tree/history exceeds these finite bounds,
report the actual bounded need and HOLD, without raising limits.

**Receipts, supervision and later checks.** Proposed durable evidence cap8MiB
for the entire new packet, inside the existing32MiB lifetime evidence ceiling;
no additional allowance or refund. Include commands/environment-withheld-key
policy, binary/static-file bindings, exact source/manifest binding, per-command
exit/byte-count/digest, bounded graph/tree/object digest summaries, first refusal,
and a single final prerequisite result with separate origin/config/object/
installed-provenance verdicts. Keep stderr at64KiB per child/512KiB aggregate;
retain count/digest and approved reason classes, not potentially secret raw
diagnostics. Maintain independent drains on failure/cap and the same child
handle through final wait/close; no next row after failure. Cancellation and
unresolved handles use the existing selected policy, not a new signal authority.

Owner3's future source packet must freeze exact driver/commands/static rules
and preservation bindings before any execution selection. Proposed quick
checks, also unselected now: static argv/no-network-helper/source binding and
one small fake-boundary actual-control suite for missing/promisor/alternate/
replace/shallow/include/registry ambiguity, tree/manifest/blob mismatch, ancestor
closure/body mismatch, chunk/byte/time limits, late child/pipe errors, secret
redaction, unchanged source bindings and first-refusal preservation. No Nix,
real Git objects, filesystem walk, network or process probe in that suite.
A source-accepted packet still needs lead's separate native selection; its
successful Git evidence would not certify Nix, restoration, source NAR, the
three catalogs/selectors or later service/gem/VM gates.

**Renewed resource anchor and recovery disposition.** Lead supplied and I read/
hash-matched the sibling
[one-endpoint receipt](repair/support/final-head-source-recovery-endpoint-1.json)
`4e685a34b54f9a242f1fc478fa7a315aad35773d5513be8a11a50fe7488c44b1`.
Its single successful statvfs observation is134269771776B free; positive gap
from134358052864 is88281088B, giving full cumulative charge5840527360B.
The next positive-gap anchor is134269771776B. All120 maxima totalling5881446400B
remain inherited and UNREFRESHED. Under6GiB6442450944, remaining before allowance
is601923584B; after the SAME512MiB536870912 allowance only65052672B remains.
This supersedes the previous153333760 residual prospectively, not the old raw
receipt. Preserve the previous bare-command127/sample0 refusal too.

The endpoint is not RAM/identity/maxima/admission/current-fit evidence. Its own
receipt and all later preparation/unobserved growth are charged at the next
separately selected observation, without refund or ownership attribution.
If lead later selects preparation, a new ledger must reference both33e87b83
and this endpoint receipt, carry5840527360/latest134269771776 and the complete
unchanged map; it may not edit the frozen validator's ledger or invent fresh
maxima. This brief takes no additional capacity reading.

No6GiB fetch/restore permission follows, and no7GiB choice is made. Even one
historical347009024B source allocation exceeds the renewed post-allowance margin
by281956352B before cache/temp/evidence costs. The proposed read-only prerequisite
is also unexecuted; its small evidence cap is not fresh resource admission.
Missing candidate, installed provenance/patch/libgit2 uncertainty and unproved
temporary/coexistence bound continue to hold restoration and validation.
The next lead decision can be only bounded source preparation of this packet,
further explicitly scoped evidence for a remaining blocker, or continued HOLD.
No operation dispatch is made here.


#### Parent-component resolution clarification — proposed, awaiting lead selection

Lead requested this narrow design before owner3 changes draft controls.
Inspection is limited to the new packet's `policy.py` StaticGate and its
existing brief. Draft `read` calls Path.lstat/open on whole paths: those
operations follow parent links, while its eight-link loop sees only the final
component. The draft also counts each final-link expansion as a subject.
Its three hazard-directory accesses have the same parent-path issue.
The initial fake suite0/0 is retained preliminary evidence, not final source
readiness or coverage of this gap. No implementation/test/live-parent read,
new HTTP, owner3 dispatch or native selection is made here.

**Scope and counter meanings.** Metadata lookup of each component needed to
resolve an already fixed subject, or that subject's approved symlink target
chain, is permitted resolution work. It does not add a file-content subject,
configuration include, directory listing or permission to inspect siblings.
The source boundary remains StaticGate's23 STATIC files and three DIRS, with
their two already planned snapshots. Only DIRS may be enumerated, once per
planned snapshot, under the existing cumulative4096-entry cap. Use the same
bounded resolver to obtain those three directory descriptors; no other scandir,
walk, glob or search is allowed.

On selection, replace the ambiguous “64 file/link subjects” label with these
independent limits, charged before calls and never reset/refunded on failure:

| Meter | Exact proposed bound |
| --- | --- |
| Named subject access attempts | <=64 for the whole stage; each file read or one of the three directory inventories counts once per planned snapshot, including ENOENT/failure. The current schedule is52, not64 arbitrary names. |
| Named file contents | Existing4MiB aggregate across both snapshots and existing per-file caps, unchanged. Ancestor metadata is not file content. |
| Path syntax | Original, target and expanded current pathname <=4096 filesystem bytes; each ordinary component<=255B; <=64 components in the active resolved-plus-pending path. No NUL/control characters or URI syntax. |
| Component visits | <=256 per named-subject walk; <=16384 over the stage, including restarts and proof replay. |
| Symlink chain | <=8 followed edges cumulatively across ALL parents and final components of one original subject, without reset on redirection. The second snapshot must replay that same chain, not discover eight new edges. Each replay walk is also <=8; stage follow count<=512. |
| Metadata operations | <=2048 attempts per walk and<=131072 over the stage, including stat/lstat/readlink/open/fstat, witness rechecks and descriptor closes. Failure/ENOENT attempts count. |
| Link-target bytes | <=4096 per readlink result; <=4MiB aggregate including witness rereads, separately from file-content accounting. |
| Held descriptors | <=128 for the resolver, with serial walks; no stage-wide cache of open paths. |
| Resolution evidence | <=64KiB per original subject across both snapshots, <=1MiB cumulative including partial/refusal evidence, inside the already selected8MiB packet/32MiB lifetime cap. Reserve a small fixed refusal record before consuming this subcap. |

The eight-link bound is a bound on the complete subject chain, not a new budget
for each parent or recursive call. Re-reading a recorded edge to prove stability
does not authorize a different target; its syscall/bytes still consume the
metadata/target-byte meters. A second-pass chain difference refuses. These caps
are upper refusal limits, not assertions that an arbitrary64-subject/depth64
input can complete. All operations remain inside the existing120s prerequisite
deadline and applicable outer limits; check cancellation/deadline before and
after each potentially blocking metadata/read operation.

**Fixed component walk and containment.** Use one small local descriptor-relative
walker for these named subjects, not Path.resolve/realpath followed by a normal
open. Start from a held root-directory descriptor. Visit each basename with
no-follow stat relative to a held, authenticated parent; open intermediate
directories with O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC (O_PATH is suitable on this
Linux target), fstat the returned descriptor and compare it to the entry just
observed before descending. Keep the needed ancestor/edge witnesses until
the leaf read or directory inventory and its proof checks finish.

For a symlink, charge the common subject link meter before readlink relative
to its held parent. Retain its before identity, bounded target, and after
no-follow identity; mismatch/type change refuses. Resolve a relative target
against that actual resolved parent, not the original textual path. An absolute
target restarts at the held root with the unconsumed subject suffix; it does
not create a new subject or reset any counter. Expand components in order:
skip “.”, and handle “..” by popping already authenticated ancestor descriptors.
Never normpath an unresolved `component/..` pair across a possible symlink.
Do not open “..” to roam to a new parent.

Every prospective target must stay within the previously approved target roots
(/etc, /nix/store, the named user's configuration paths, and exact W/D/C), using
component boundaries rather than string-prefix lookalikes. Prefix ancestors
such as /home are transit metadata only on the exact route to an approved
subject/target; they confer no content/listing access. A relative “..” must
not escape its approved root, and no walk may pop above /. Absolute approved
root-to-root translations remain possible for the known configuration chains.
A repeated symlink edge or repeated expansion state refuses as a loop; no
probing alternate paths after an escape/dangling/loop failure.

Repository root/pointer policy stays exact. Metadata walking does not select a
different W, D or C. W/.git contents must still name literal D, D/commondir must
still be `../..` resolving exactly to C, and D/gitdir must name W/.git.
The commondir text is an existing, separately validated Git pointer, not
permission to treat arbitrary config content as another path. Relocating a
repository root or following any include/other file-content pointer is outside
this correction and returns to lead.

**Leaf access and proof.** Open a final regular file relative to the same held
parent with O_NOFOLLOW|O_CLOEXEC and nonblocking read flags, then fstat and require
the same regular-file identity before reading any data. Existing type/size/
chunk/content limits still apply. Directory inventory uses its authenticated
directory descriptor, not a reopened pathname; keep exactly the three existing
enumerations. Validate dev/inode/type/mode and relevant timestamps (including
ctime), leaf size where applicable, and the held descriptor versus named-entry
relationships before and after consuming content. Recheck the traversed
symlink targets/identities and retained ancestor witnesses through held parents.
Do not accept bytes or a membership result if any proof is missing or changed.

Optional absence is only an identified missing original component under a
validated parent, with a bounded stable witness. Missing components while
resolving a symlink's target are dangling-target refusal, not optional ENOENT.
Once an approved directory target has fully resolved, an absent original
optional suffix can be recorded separately. Permission errors, ENOTDIR,
unexpected types, ambiguous absence and changes never become benign absence.

NOFOLLOW plus held descriptors closes implicit parent-link traversal; textual
chain equality alone does not. Before/after observations still do not prove an
atomic namespace snapshot, defeat every ABA/rename/mount race, or bound a blocked
filesystem syscall. A final type substitution can be detected before data read;
ordinary open/fstat cannot promise zero open-side effects for every hostile
special-file race. Do not claim stronger protection or add openat2, proc-fd
reopen tricks, new roots or a filesystem framework to obtain it. An obstacle
requiring those changes returns to lead before edits.

Reserve one close-operation credit when acquiring each descriptor, within
both metadata caps. Cleanup consumes those reserved credits even after other
budgets/deadlines fail; exhausting the traversal budget must not skip closes.
Attempt every owned close once, retain the primary failure and bounded close
errors, and perform no new pathname inspection in an error handler. No retry
or successful receipt can clear the first refusal.

**Secret-safe evidence and affected checks.** A bounded chain record contains
the fixed original subject ID, pass, component/edge order, approved-root class,
before/after identities, operation/link/byte totals, and exact byte-length/
SHA256 binding of accepted link targets. Display raw paths only when they are
fixed approved literals or explicitly safe retained path labels; derived paths
can use opaque record IDs and digests. Never echo a rejected raw target, URL,
config value or exception filename/strerror containing an unapproved path.
Use fixed reason codes/errno and retain the bounded partial witness before
raising. Config contents remain governed by the existing redaction policy.

Owner3 may change only the local StaticGate resolution/inventory integration,
its bounded evidence fields and the directly affected fake fixtures after lead
selects this clarification. Preserve draft/interim sources and the initial
suite/log bindings first. Native Git ROWS/PREFIX, STATIC/DIRS membership,
environment, observer authority/control, resources and old packets remain fixed.
Any needed cross-boundary change is a material deviation requiring lead first.

Refine the already selected small suite with actual-resolver fake calls for:
parent plus final nested links (combined exactly8 succeeds, ninth refuses);
absolute and relative approved targets; “..” semantics and root escape;
dangling targets versus optional suffix absence; loops; changed parent/link/
leaf identities and directory substitution; exact operation/evidence budgets
plus cleanup on exhaustion; and secret target/error withholding. Assert that
whole-path Path.open/resolve and extra enumeration are never used. Fake or
poison all native filesystem/process boundaries; verify dir_fd/NOFOLLOW and
held-parent relationships rather than only testing string normalization.
Retain source-before/after and test/log bindings, with static proof that the
native command list, subject/enumeration list and resource/authority constants
are unchanged. No real check or new broad conformance suite is selected here.

Full carry5840527360B/latest134269771776B/all120 UNREFRESHED maxima5881446400B,
the same separate6GiB stops/512MiB allowance and residual65052672B before later
gaps remain unchanged. The correction grants no additional disk allowance or
native/resource sampling. Owner3 remains paused on this correction pending
lead choice; unrelated already selected source preparation can continue.
### Selected disk budget for the recursion-corrected package build

**The lead explicitly selected this contract and source-only preparation in the
assignment beginning "Lead read FULL proposed diskbudget section".** Actual
realization remains UNSELECTED. This replaces only the cumulative shared-disk-
decline ceiling for one exact recorder build; preceding limits remain historical.
The selected quick checks are limited to the source and inert boundaries below.

The lead accepted [metadata assessment](repair/hotplug/recursion-metadata-1-owner-assessment.json)
`ca8458ad3b4955d62af1b0a84524f4ad2dba52d87f0d6affdb34938105d09845`
and [qualified disposition](repair/hotplug/recursion-metadata-1-lead-disposition.md).
Retained plan `666f7e3d09dface6e6a7aadd573d56e415f41c32644745f08d59d76d873b070d`
binds the sole build to
`/nix/store/rnaqxd765cjb3sxrafk9dyq08mnp50xw-livepatch-first-hotplug-recorder-1.drv`
(SHA256 `fee3c0ad1387668e57baf30e4d9cdeb98b956de87041cbb561807ecedb8e3722`),
with intended output
`/nix/store/lpz9w1ypglskjqgw6hzcs7q99a15mvi5-livepatch-first-hotplug-recorder-1`.
The output was absent at the accepted observation. Its eleven approved tool
substitutions forecast 136MiB download and 1.4GiB unpacked. Neither that forecast
nor previous tool materialization establishes future cache availability,
physical allocation, compiler RSS or protected effects.

Use the selected **4GiB (4294967296-byte) cumulative shared-decline stop**, retaining
the entire 1942851584-byte carry. The old 3GiB ceiling leaves 1278373888 bytes
(1.1906GiB), insufficient even for the unpacked forecast. The selected ceiling
leaves 2352115712 bytes (2.1906GiB), without any refund or attribution assumption.
Use **2GiB (2147483648 bytes) as a planning admission allowance**: 1536MiB for
the rounded-up unpacked forecast, 160MiB for downloads, 64MiB for all capped
logs/evidence, and 288MiB for this small C/BPF build, output and allocation
overhead. This leaves 204632064 bytes (195.15MiB) beyond the allowance at the
retained checkpoint. These components are planning assumptions, not measured
maxima or additional independent quotas. The unchanged known-path ledger last
totalled 1532309504 bytes, leaving 2762657792 bytes under its separate 4GiB stop.

Fresh predicates for a separately selected operation:

- Preserve the full shared-decline carry and every named physical maximum.
  Charge any observed positive gap from the last retained free-space endpoint
  to the fresh admission sample, then every positive decrease between samples.
  Free-space increases never reduce the accumulated charge. Interstage and
  unsampled movement remains unknown; endpoint accounting does not reconstruct
  it or assign it to this operation.
- Before launch and again before FIFO admission, require cumulative charged
  decline plus the 2GiB allowance to be at most 4GiB, fresh filesystem free space
  at least 43GiB, and refreshed known-path maxima below their unchanged 4GiB
  stop. Refuse on required unreadable/inconsistent evidence. Historical free
  samples do not satisfy fresh admission. During execution, cancel at cumulative
  shared decline >=4GiB, known subset >=4GiB, or free space <40GiB. These are
  separate sampled safeguards; none proves a whole-owned allocation bound.
- Preserve client hard1GiB/noSwap, absolute whole named daemon plus actual client
  memory.current <=8GiB for admission and >=12GiB for cancellation, host
  MemAvailable >=20GiB for admission and <16GiB for cancellation, strict required
  MemTotal/Available validation and exact service/client identity. No baseline
  subtraction, hard aggregate, protected-builder identity or peak claim follows.
- Preserve sole exact drv/eleven-approved-substitute subset checks, one job/two
  cores, default secure build directory, fallback=false, IFD=false, native540s/
  client600+5s, and logs48MiB plus16MiB reserve within64MiB. Any later selected
  native plan check must refuse other source builds or substitute paths; current
  preparation needs no cache query or reevaluation. The metadata operation's
  separate 1GiB limits are historical, not the build's resource contract.

The extra GiB makes a bounded attempt plausible without assuming cached tools;
it does not promise completion. Foreign movement, transient downloads, physical
overhead or hidden allocation can consume the margin. If fresh admission lacks
the 2GiB allowance or another predicate fails, hold and report the exact failed
predicate. Do not poll for capacity, reset carry, increase the ceiling again,
run GC or retry automatically. Cancellation addresses only the authenticated
owned timeout; uncertain protected effects retain evidence/roots and require
lead reconciliation.

Implementer2 owns the selected source-only adaptation of the accepted build4
driver/watcher/control pattern, brief and carried-budget evidence to this exact
plan and fresh owned recursion-build1 identity. Preserve all old source, helpers,
results and roots before adaptation; the metadata observer remains historical.
Bind source `/nix/store/vfgz3w0fxyva7hq4kmhslnqhg0gyd788-source`, C `55a154cc`,
docs `e7d938be` and native header `82ac9ea1` to the complete hashes in the accepted
assessment. Any actual cache gate belongs to the later selected operation and
must freshly refuse other builds or paths outside the approved eleven-path set.
The frozen source package must show the finite constants, complete carry/maxima,
unchanged identity/cancellation rules, exact graph and CLI-only command, plus
focused inert boundary checks for admission at/over the allowance, stop equality,
positive-gap charging, no refund after a free-space increase and the pre-FIFO
recheck. The lead selects Bash-n, guard AST/hash binding/preservation proof and
ONE current pure/inert suite exercising actual affected decisions with native
subprocess/filesystem/process/clock/signal boundaries poisoned or faked. Compare
unchanged authority/control AST where possible. These are not native guard,
systemd or kernel proof. Return frozen driver/watcher/brief/carried budget,
literal argv and all hashes for separate lead inspection and execution selection.
No actual guard, subprocess probe, process/scope/capacity/cache query, Nix,
evaluation, fetch, build, Git, runtime or cleanup is selected. No generic monitor,
recipe/BPF/header/qualification change, owner0/owner8/first7 history edit or
metadata-helper repair is selected. Material deviations return to the lead
before edits. Metadata monitoring remains
INCOMPLETE with missing terminal status and qualified protected views; the
accepted metadata graph is not a completed supervision or package-build result.

#### Recursion-build1 focused source acceptance

Architect source acceptance is granted for the frozen package below, with no
remaining concrete blocker in the selected adaptation boundary. This is not
mandatory product review, native guard/systemd/kernel proof or execution
selection. Full driver, guard, brief, budget, diffs, preservation inventories
and current inert evidence were read without invoking them or rerunning checks.

| Artifact under `repair/hotplug/` | SHA256 |
| --- | --- |
| `run-recorder-recursion-build-1.sh` | `bc2aa240de44cf7f352bee3005069cd38bd3b66e3c91f6410ab6a70be9239548` |
| `watch-recorder-recursion-build-1.py` | `bd1c837a82a9e7ec627ec2194f8619e00162d88d941f6c6e0839a7f050e96916` |
| `recorder-recursion-build-1-watcher-brief.md` | `c75dd948385a684ed71597e81f269280989d97d3c5573ef584476c582a2ef669` |
| `recorder-recursion-build-1-preparation/carried-budget.json` | `90ef9af3618ba9213e5bf59f113a3411a0cb0660ae9796f0e63b5c67eb87d3f2` |
| `recorder-recursion-build-1-preparation/final-preparation.json` | `1085ba2dbb9215dd4674c8b82dc252128a3b904dd14d96471dd3e901adb2037c` |
| `recorder-recursion-build-1-preparation/preparation-proof.json` | `672f0e007aec6d07b52ac01780b63062f7c99f2cedfc04ee9925a0cab93333b9` |
| `recorder-recursion-build-1-preparation/self-test.log` | `f9a0250deb774cd1a104aafe5180cf9b44fbd9f2b064b1e9bf2115ff966f29e7` |

Independent read-only comparison confirms full1942851584-byte carry, endpoint
136250007552, all98 named maxima and1532309504-byte seed. Positive initial and
subsequent gaps accumulate; free increases and absent paths cannot refund them.
Refreshed disk admission runs before Popen and before FIFO, with the selected
2GiB allowance/4GiB ceiling,43GiB free admission and strict known-subset limit.
Runtime stop equality at4GiB and free<40GiB remain explicit. The final disk read
precedes the existing fresh five-second startup check, so a slow read cannot
extend admission. Exact retained plan/driver/source hashes and the later fresh
sole-build/approved-eleven-substitute gate preserve the intended C/BPF and
CLI-only operation without assuming cache availability.

AST comparison confirms unchanged RAM, handoff, PID/birth signal authority,
liveness and one-launch control; the supervisor delta is only the selected disk
recheck before the existing deadline. Both embedded driver Python blocks remain
identical to build4. Six original copies,64 source/raw/root identities and exact
stored diffs match independently. The recorded single run has240 assertions:
220 prior labels retained plus20 focused disk assertions, with current guard and
driver hashes matching the before-run binding and final proof, and empty stderr.
The focused cases use actual charge/admission methods and supervisor decisions
with explicit fake native boundaries, including no token after failed admission
and a slow disk read crossing5s. These are assertions, not240 native scenarios
or comprehensive fault coverage; no test was rerun for this acceptance.

Keep the package frozen for separate lead execution selection. Fresh capacity,
cache and native process observations remain unperformed. The finite allowance
is planning only; known-path/shared-service samples do not establish whole-owned
allocation, protected-builder identity/effects or unsampled peaks. Metadata's
missing terminal status remains INCOMPLETE. The accepted build4 terminal control
pattern and required utility effects evidence are preserved without a historical
status repair or stronger completion claim. No product/history edit, native
query/build/probe, process scan, signal, cleanup or lifecycle action followed.

### Fixed metadata observer assessment: four narrow corrections selected

Source inspection of the one-operation observer
`repair/hotplug/recursion-metadata-1-preparation/operation-command/observe.py`
at SHA256 `109757c65078ab023153e9676773bdbb89831952251bbcbd9498a1f488a6a72e`
does not yet accept it for execution. The brief is
`c3f2139deef0671242d2afb45b5381d31ec3c6ccecd2500f9c37ce25041946c0`.
The lead selected exactly the four corrections below under owner2 task
`50971f87-ab43-463c-b306-5f032b2ba46b`. Preserve the original observer/brief
bytes at these hashes and the findings below; their execution acceptance remains
withheld. Owner2 may correct only the observer, brief and owned preparation
evidence. No metadata operation identity has been consumed by this selection.

A fixed command enforcing the selected observations is proportionate after
utilities omitted them. Its one Popen, literal child argv and reused bounded
scanner need no general monitoring framework. Independent read-only comparison
confirms driver `13105c450fb309d70223314478a25560ab1f01165e4b3fa393df1bf8dcca0d9d`
is byte-exact, the brief is append-only, and all 36 named preserved identities
are unchanged. The 29 pure decision assertions are useful but do not exercise
the actual loop's error/finalization paths or establish native systemd behavior.

The following concrete paths require correction within this observer/brief and
its existing preparation evidence only:

1. **Failed observations must still make bounded progress.** At lines 117-129,
   failure to read the initial launcher birth skips both stream readers. If the
   launcher exits before that read, every later iteration repeats the failure,
   never reaches either EOF, and cannot finish even after native exit and scope
   collection. Separate initial identity/receipt failure from independent pipe
   draining and known-birth reconciliation. Preserve missing startup identity as
   INCOMPLETE; do not reconstruct it. At lines 206-214, persistent control errors
   can spin without the normal cadence; at line 181 the deadline merely latches
   failure, and notification is conditional on cancellation failure at 194.
   Every first failure needs a one-shot bounded escalation/status record, even
   when no timeout was authenticated or the native client already exited.
   Keep one handle and one launch, attempt cancellation only under the existing
   authority, and pace the error path too. At the unchanged 305-second native
   deadline, unresolved effects must be explicitly reported to the owning
   utility. Retain supervision while unresolved; do not convert this into a
   new kill deadline or return that abandons a live/unknown operation. Attempt
   the existing bounded effects scan once on settled completion or the explicit
   unresolved escalation boundary; do not hide it behind an unreachable success
   condition or add repeated scans/retries.

2. **Finalization must preserve evidence on errors.** Lines 215-221 and 229-230
   put wait validation, closes, clock/result construction and result write
   outside the protected final path. An exception/interrupt there can skip the
   effects scan or lose the result. Retain primary failure and native status;
   guard each finalization step, attempt both stream closes and sample close,
   and attempt the existing effects scan even after another finalization error.
   A missing/unwritable receipt remains INCOMPLETE with a bounded fallback, not
   success or an excuse to relaunch. Do not return if liveness is unknown.
   Interpret the existing scan's retained known-birth states, canonical cgroup
   and named-scope result, not only its first positive-reference records at
   224-227. An observed surviving/unknown owned birth, present/unknown operation
   scope or positive-record overflow is incomplete. General protected-process,
   FD/argv and non-atomic scan gaps retain the already accepted qualifications;
   this does not require a privileged or unrestricted scan.

3. **Cap the observer's own output.** `stream_bytes` caps child stdout/stderr,
   not repeated `os.write` at 208, scanner printing at 370 or final printing at
   230. A persistent error can therefore exceed the stated observer cap. Apply
   one fixed cumulative output budget to the observer's diagnostics, escalation
   and terminal summaries, independently of the existing child-stream cap.
   Emit short receipt references instead of dumping full results. A failed
   diagnostic write must not bypass supervision or recursively print errors.
   Preserve EOF draining and report capped evidence as incomplete; do not
   replace this with a new logging framework.

4. **Enforce the existing startup deadline at successful observation.** Lines
   151-163 can bind identity and set `startup_proven=True` after five seconds;
   line 164 then skips the deadline failure. Check fresh elapsed time before
   recording successful startup proof. A late otherwise-valid chain can inform
   safe cancellation but cannot establish timely startup or clear first failure.
   Preserve the exact unbound loaded/inactive/empty-identity pending tuple and
   five-second budget, never reopen pending after binding, and require no prior
   latched failure for the pending classification. There is still no FIFO:
   metadata may run before the first sample, and unknown startup is incomplete.

Cancellation authority itself remains narrow: fresh PID/birth, exact timeout
argv/executable/cgroup, exact named invocation and canonical cgroup inode, and
the original launcher's actual exec-or-parent relationship. Changed PGID is not
absence or authority for a group signal. Failure to authenticate this tuple
escalates; it never authorizes systemd forwarding assumptions, another target
or another signal. Preserve at most one TERM attempt. Native 300+5 timeout,
child argv/body, graph and resource thresholds remain unchanged. Known block
maxima and positive shared-free decreases remain separate, without refunds or
hidden-allocation/peak/protected-effects-ended claims.

Prepare focused inert cases through the actual control/finalization path using
the existing local fake boundaries: birth-read failure after immediate child
exit with both EOFs still drained; receipt/stream failure without skipping the
other stream; persistent inspection/control error with one bounded escalation
and paced retained handle; failures/interrupts in wait, each close, clock and
result writing with the scan still attempted; observer-output exhaustion;
scanner own-birth/scope/overflow evidence; and a valid first startup chain read
after five seconds. Keep native filesystem/process/signal/clock/subprocess
operations poisoned. Do not count pure classifier tests as loop fault coverage.
The lead explicitly selects preparing and running this bounded actual-control
inert suite as part of source preparation, with native filesystem, process,
signal, clock and subprocess boundaries poisoned or faked. It is neither a
native probe nor full runtime proof. No new interface, dependency, product
source, generic helper, Git mutation, cleanup or runtime investigation is
selected. Owner2 returns a new frozen package for separate architect source
acceptance. The preserved driver, native argv, graph, resources, 300+5 timer,
one Popen and at most one TERM remain unchanged. Actual observer execution,
native query and metadata evaluation remain separately unselected.

#### Selected post-scan reconciliation and test-binding correction

The lead selects the two remaining post-scan blockers and historical-suite
evidence correction under owner2 task
`dcaa536c-f849-4fcd-80a2-98ed840a04b0`. Preserve the preceding four findings and
their correction evidence. The inspected replacement observer
`a330923624688b5ff39ca4e1605182c3812e8f6680908858eb50e4792a79f0a7`
and brief `e68b65d64b1299e58c5273596e15e8402463ad6adff16f195a9d51915a467663`
remain frozen originals whose execution acceptance was withheld.

Accepted portions of that inspection remain recorded: independent pipe progress
despite missing one-time launcher birth, paced same-handle error handling,
bounded first-failure/deadline notification, independently guarded finalization,
64-KiB cumulative/2-KiB per-emission observer output separate from child streams,
fresh startup deadline/no-prior-failure pending, scanner failure propagation,
and unchanged strict native timeout cancellation authority. These are source
conclusions, not proof of native execution or systemd behavior.

Correct only the following remaining paths:

- Require a fresh ordinary reconciliation iteration after the one effects
  attempt, regardless of whether settlement or the 305-second/clock escalation
  triggered it. In a330, escalation calls the scan before the completion check;
  `effects_attempted` can then permit return using pre-scan scope/EOF/native
  observations. Post-scan completion must freshly reconcile the original handle,
  named scope, canonical cgroup, both EOFs and all retained observed births.
  Do not clear prior failure, repeat the broad scan or introduce another timer.
- Retain every scan-discovered non-self actual PID/birth as observation-only
  liveness evidence, including positive references absent from the sampled
  known set. Such a process may have escaped/reparented before sampling and
  must not be abandoned because the old set and scope are empty. This adds no
  ownership inference or signal authority: native TERM still requires the
  original strict authenticated timeout tuple. Missing-birth/positive-overflow
  ambiguity must hold and escalate pending lead reconciliation. Do not invent
  identities, signal foreign processes or add a generalized handoff/release API.

Correct the test provenance precisely: `0dc8967c` identifies the binding JSON,
not the interim source. Its source `e3390364` and log `085e4f06` were independently
verified; historical suite `14e94142` bytes were not accounted for in the inspected
package, and current suite `56642d70` is not claimed to have run then. Owner2 may
perform only a bounded lookup within owned preparation evidence for the exact
original suite, or mark it unavailable. Preserve history; do not reconstruct or
invent an executed fixture. The final 12-case result bound to a330 is valid
retained inert evidence, but becomes historical after this edit.

The new branches and binding gap justify one current full small actual-control
inert suite plus focused cases, bound to exact final observer, test and log
hashes. Include an escalation-triggered scan followed by changed scope/liveness,
and a real-shaped positive PID/birth absent from sampled known identities that
remains live after native exit and scope collection. Demonstrate retained
supervision until actual fake settlement; missing-birth/overflow remains held
for lead reconciliation. Native filesystem/process/signal/clock/subprocess
boundaries stay poisoned or explicitly faked; label pure checks separately.
No recorder PASS73 rerun or new native/systemd/runtime proof is selected.

Scope remains the fixed observer, append-only brief and owned preparation
evidence. Driver, native argv, graph, resource thresholds, one Popen, at most
one TERM and native 300+5 seconds stay frozen. No observer execution, query,
evaluation, Git mutation, live scan, cleanup, broader investigation or architect
helper takeover is selected. Owner2 returns a frozen corrected package for a
separate focused source acceptance. Material obstacles return to the lead.

### Selected recorder program-recursion completeness correction

The lead selects this source-only correction of the Important finding in
[the committed remediation review](final-review-remediation.md), without a
waiver. The reviewed candidate is
`19562b6449f01ca4939d57f70ee59de8af13880f`, tree
`3e04ce2bd85f871c3f40f86db5668f30684100a4`; the shared feature remains `9bea27c9`.
This extends the two-grace shutdown design below and supersedes its earlier
"no further source change" acceptance. Neither the review nor this decision
establishes an observed recursion drop, CPU127 loss or cause of the kernel WARN.
CAS, publication, runtime, Git mutation and helper-monitor changes remain held.

Exact Linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`, read locally with
`GIT_NO_LAZY_FETCH=1`, distinguishes two loss sources:

- `kernel/trace/trace_kprobe.c:1350-1353,1739-1762` exposes kprobe `kp.nmissed`
  and return-probe `rp.nmissed` through the live perf link. These counters do
  not include the BPF dispatch suppression below.
- The recorder's perf-kprobe path calls `trace_call_bpf` at line 1669.
  `kernel/trace/bpf_trace.c:110-128` increments attached programs' miss counters
  when the per-CPU BPF recursion guard suppresses their execution. Raw dispatch
  at `:2315-2330` increments the suppressed program's counter separately.
  Neither suppressed call reaches the recorder's ring or map accounting.
- `kernel/bpf/syscall.c:2279-2320` increments and sums per-program misses over
  all possible CPUs, independently of the run-time-statistics enable switch.
  Normal program load at `:2767` uses `bpf_prog_alloc`; allocation at
  `kernel/bpf/core.c:139-163` requires zeroed per-CPU statistics or fails.
  `syscall.c:4614-4617` exposes the sum as `bpf_prog_info.recursion_misses`.
  This is proof for these raw/kprobe paths, not every BPF attachment type.

Use the existing libbpf 1.7.0 interfaces `bpf_object__for_each_program`,
`bpf_program__fd`, `bpf_program__name`, `bpf_program__type` and
`bpf_prog_get_info_by_fd`. The installed `include/bpf/bpf.h:526-543` specifies
zero-initialized input and in/out `info_len`. Exact kernel
`syscall.c:4560-4617,4841-4846` fills the available prefix, including program
type/id and recursion misses, and returns the actual copied length. The miss
field is filled before the restricted-capability information branch. Existing
owned program FDs remain valid through link destruction until
`bpf_object__close`; link handles must still be destroyed once and nulled.
No registry lookup, duplicate/pinned descriptor, statistics toggle or new
privilege path is needed.

Preserve QUERY before attachments and the existing shutdown sequence: disable,
GLOBAL grace one, live-link kprobe snapshot, destroy/null every raw and perf
link, GLOBAL grace two. Only after successful quiescence, while the object still
owns its program FDs, read every program's native recursion counter. Final ring,
map and byte checks and ordinary free/fsync/close remain in this same stable
phase. A program-counter failure must not suppress the other final checks or
owned teardown, or clear any earlier failure/monotonic abort. A failed barrier
or destruction still prevents authoritative stable accounting; do not add a
fallback or claim that a best-effort read proves completeness.

The program iterator must not produce a vacuous or partial success. Enumerate
every object program, including all four raw and eleven perf programs, once;
never silently skip an unloaded/invalid FD. Check coverage against the existing
raw and perf attachment-array counts, without another name registry or a magic
15-program list. Require the corresponding raw-tracepoint/kprobe family counts.
The successful attachment path already resolves every required name from those
same arrays. Missing/extra programs or missing descriptors are incomplete.
For each zero-initialized info request, require successful native return and
returned length at least
`offsetof(struct bpf_prog_info, recursion_misses) + sizeof(info.recursion_misses)`
and no greater than the supplied buffer. A zero-filled unsupported tail is not
zero-miss evidence. Do not require a whole newer userspace struct when the
returned prefix covers the required field. Require nonzero native program ID
and native type matching that owned program's libbpf type. Names identify
diagnostics; do not compare a long libbpf name to the kernel's truncated name.
Continue reporting other programs after a failed read. Any nonzero miss count,
API error, invalid identity/type, short response or incomplete coverage fails
the capture even if all live-link misses are zero and map/byte totals agree.

Keep existing `probe=... missed=...` output and its live-link capture-cutoff
scope. Report program ID/name and `recursion_misses` distinctly. Program counters
cover the whole loaded-program lifetime through successful detach/quiescence,
across all CPUs; they may conservatively include setup, disabled-window and
non-CPU127 suppression. Do not subtract a baseline, label these capture-window
or CPU127-only counters, or combine them with kprobe misses as interchangeable
evidence. The stricter rejection is intentional completeness enforcement.

Owner2 exclusively edits `tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.c`
and the existing CPU-hotplug diagnostic section of `docs/os/testing.md`, plus
the existing session-local actual-C checker and its evidence. Before editing,
retain byte/mode/hash copies of candidate19562b C `4bf11e25`, docs `a5fddc49`,
checker, old include, scripts and existing raw results. Preserve the docs prefix
and full following suffix. BPF/header/recipe/qualification, event ABI, build-ID,
CPU guards, output/deadline limits, attachment scheme, first seven source/history
owners and owner0 packet/scripts stay unchanged. No new shipping source file,
framework, kernel patch, runtime probe or monitoring helper is selected.

Extend the existing actual-C boundary check with fake program iteration/FD/info
calls, retaining its existing 41 shutdown/error/abort cases. Required cases:

- All programs report validated zero counters and existing link/map/byte checks
  agree; success remains possible. Each raw and perf program can independently
  report a nonzero miss and force failure with zero link misses and matching
  maps/bytes, including a late increment completed at grace two.
- Missing/empty/extra program coverage, invalid FD, API failure, missing native
  ID, wrong type and absent/short info fail closed. Exact field-end length is
  accepted; one byte short and an oversized reported length are rejected.
  Earlier failed program reads do not skip later reads or final owned cleanup.
- Failed grace/destruction yields no stable program-counter claim. Preserve
  partial attachments, output/drain/accounting errors, all destructor attempts,
  prior/late abort and SIGUSR1 behavior. Exercise the actual new helper rather
  than a rewritten algorithm; retain the old omission as regression evidence
  where the existing authenticated fixture permits it.

Prepare source/AST/Bash syntax checks, hashes and an exact bounded cached-tool
command. Native C compile, executing the mock binary, packaged compile/CLI,
new derivation evaluation and actual loading remain separate lead selections;
do not run them as part of preparation. Mocks can verify userspace checks and
ordering, not kernel synchronization or real loss-free recording. Return the
frozen source/check packet and preservation proof for lead selection. A material
obstacle or scope change returns to the lead before edits. The later owner8
amend must fold this correction into its logical owner, preserve first-seven
history and update validation honestly; no ninth fixup is selected. The retained
reviewer's affected-lane rerun remains a later lead/policy decision.

Compatibility is limited to stricter diagnostic success criteria and additive
stderr evidence. There is no persistent format, migration, fleet coordination,
deployment ordering or event-decoder change. Existing raw artifacts stay
readable; old binaries cannot establish the new completeness obligation. No
deployment, recovery cleanup or session lifecycle action follows from this
source-only decision.

### Selected recorder shutdown correction after final review

Reviewer0's final inspection of `9bea27c9` identified a recorder completion race:
the control-map disable precedes ring consumption and map/missed-hit reporting,
but an invocation already past the enabled check may submit afterward. Pin-map
error writers also run outside that enabled check. The lead selected the
following bounded correction in the existing recorder logical owner. Owner2
owns `hotplug-recorder.c`, necessary source comments and the existing diagnostic
documentation; no BPF layout, attachment scheme, kernel pin or binary ABI change
is required. There is no new framework or syscall fallback.

The exact frozen boot uses Linux
`a2384967b90f24d2470c9eb15f0e66d938df7e08`. Its retained authenticated config
SHA256 `c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969`
has `CONFIG_MEMBARRIER=y` (line 279) and `CONFIG_NO_HZ_FULL` unset (line 109).
Source inspection establishes these specific API constraints:

- `kernel/bpf/syscall.c` raw/perf link operations at 3566 and 3760 have no
  detach callback; `link_detach` at 5388 returns `EOPNOTSUPP`. Therefore
  `bpf_link__detach` cannot supply the required operation on this kernel.
- Raw release at 3498 unregisters the tracepoint, while link reclamation at
  3019 defers an RCU grace period. Closing alone is not a userspace completion
  barrier. Perf release at 3579 removes the BPF program and closes its event;
  destroying the link also removes the interface used to read its missed count.
- `kernel/trace/bpf_trace.c:110` (`trace_call_bpf`) and `:2315`
  (`__bpf_trace_run`) execute these non-sleepable BPF programs under normal RCU.
  `include/linux/tracepoint.h:225` also covers scheduler tracepoint dispatch
  with preemption disabled. Kprobe callbacks and missed-count updates execute
  in the corresponding non-sleepable probe handler context.
- `kernel/sched/membarrier.c:649` implements `MEMBARRIER_CMD_GLOBAL` through
  `synchronize_rcu()` when more than one CPU is online. Its single-CPU shortcut
  does not leave a concurrent non-preemptible probe handler on another CPU.
  The exact boot/config restriction is essential; do not substitute expedited
  or private membarrier operations, sleeps or assumed portability to other
  kernels. Query support before attaching and fail closed if unavailable.
- `PERF_EVENT_IOC_DISABLE` is not an alternative barrier: in
  `kernel/trace/trace_kprobe.c:1657`, BPF execution precedes the perf-event list
  check, and the kprobe `TRACE_REG_PERF_DEL` operation at 1792 is a no-op.
- Exact libbpf 1.7.0 `src/libbpf.c` was inspected from its official release URL
  (400281 bytes, SHA256
  `025be63c78cb7bad472368d4c3027c7cf50a591e80d87ff9e6112ff934b8c59b`).
  `bpf_link__destroy:11103` invokes its link-specific destructor and releases
  the handle. The perf destructor at 11226 disables and closes its private perf
  FD and link FD; raw FD destruction at 11132 closes the link FD. Do not retain
  pointers after destroy or invent dup/disconnect semantics. This was a bounded
  source read, with no package realization, probe or native recorder execution.

Implement this shutdown ordering while keeping the ring, maps and output open:

1. Disable recording; preserve an error if the map operation fails.
2. Complete `MEMBARRIER_CMD_GLOBAL`, using the ordinary native syscall with
   zero flags. This closes the capture cutoff: every pre-disable admitted
   producer and capture-window missed-count update has completed.
3. While perf link descriptors are still valid, read and report their native
   missed counts. This is the capture-cutoff snapshot after the first grace
   period. It includes all capture-window misses and may conservatively include
   disabled-window misses before the read. It is not a count of the complete
   probe lifetime through destruction. Nonzero/missing/wrong-type evidence
   makes the capture incomplete. If the first grace fails, do not call a
   best-effort counter read authoritative; retain failure.
4. Attempt destruction of every acquired perf and raw link exactly once, even
   after another operation fails, and null each released handle. Do not use
   the unsupported explicit link-detach operation. No duplicate or pinned
   link ownership is introduced.
5. Complete a second `MEMBARRIER_CMD_GLOBAL` after all link destructions. This
   waits for remaining raw/perf callbacks, including pin-map-error writers
   outside the recording gate. A failed barrier or destruction prevents any
   claim that subsequent accounting is stable.
6. Consume the remaining ring and read final map counters/byte equality only
   after successful quiescence, then free the ring/object and fsync/close the
   output. Keep best-effort evidence clearly incomplete on failure. Preserve
   original abort, timeout, output-cap, callback and write failures; cleanup
   must never upgrade failure to success.

No fixed wait duration proves either grace period. A syscall blocked behind a
kernel stall is incomplete execution owned by the separately selected watcher,
not a reason to add an unsafe fallback. Preserve the existing event format,
build-ID/CPU127 guards, deadlines, required observations and size limits. Document
the capture-window scope of missed counts and why both barriers are necessary.

Focused regression preparation must exercise the actual C cleanup code with
small native-API fakes, without loading BPF: release a pre-disable admitted event
and its emitted count at grace one, require it in the final output; increment
missed evidence by grace one and require failure; release a pin-map error at
grace two and require final-map failure. Exercise both producer families,
partial attachment/null handles, each failed or unsupported barrier, map-disable
failure, missing/wrong-type counter evidence, destroy/drain/output failures and
preservation of prior abort status. Reproduce the old false-complete ordering.
Use no timing sleeps or order-only oracle. A compact session-local check can
include the actual C cleanup and fake only the native boundaries; no reusable
mock framework or new shipping test file is selected. Mock results verify the
userspace protocol, not the exact kernel synchronization proof above.

Owner2 prepares the source change, focused check and exact cached-tool native
compile/check command and resource forecast. Builds, tests that compile native
code, VM/BPF execution and Git mutation require the lead's separate package
selection. The old `q4...` binary and frozen admission image/launcher contain
the pre-fix recorder and cannot validate corrected source; keep runtime held.
When selected, fold this caused correction into recorder owner `9bea27c9` after
an exact backup ref and old/new history/tree comparison, preserving health
parent `81235fe7` and all unrelated content. No shipping fixup commit is wanted.
The lead also selected validation text for all eight commit bodies; that history
work and final-review disposition remain lead-owned. The final review is not
complete merely because this narrow design is accepted.

Architect source acceptance: owner2's prepared C SHA256
`4bf11e25f04d444b5af5ac4cc506ab566c13ba50d96e67bf2c72c5b774005b00`
and testing documentation SHA256
`a5fddc497e44614a04478752b1b042e8c3848ef5c13506d77ced36798b8280bb`
conform to this selected protocol. QUERY precedes attachment; both producer
families are destroyed once and nulled; either barrier or destruction failure
prevents stable final accounting. Map-disable failure retains an explicit
incomplete result even if later teardown permits stable maps to be inspected;
its missed-hit output is not proof of a successful capture cutoff. The abort
latch cannot be cleared by a later SIGUSR1. The BPF/header/recipe/qualification
bytes, documentation prefix and full following suffix match reviewed `9bea27c9`.

The prepared session-local check directly includes the shipping cleanup helper
and fakes only native boundaries. Its 41 cases cover late raw/perf event delivery,
missed evidence, out-of-gate pin-map errors, partial ownership and failure paths.
The old `report_losses` and `done` bodies are byte-exact extractions of the
authenticated reviewed C, so the old false-complete case tests the actual former
ordering. Check source `cba46a46`, old include `3ee25442` and native command
`81d83188` match the full hashes in
[owner2's frozen packet](repair/hotplug/review-shutdown-fix.md). This acceptance
is source inspection only: no native compile or mock was run by the architect.
The separately selected bounded check, corrected packaged build, logical-owner
fold and review reconciliation remain pending; kernel/runtime admission is still
unproved. No further source change is required by this acceptance inspection.

Corrected recorder realization monitoring, lead-selected contract adjustment:
the retained metadata checker passed for sole source-build drv
`/nix/store/zm13vhsm8d1rsfnxihpf6pqsvk4yrmhf-livepatch-first-hotplug-recorder-1.drv`
and output
`/nix/store/kpkcdfxp2g9w1a3s6z67ci7fvj36rnc8-livepatch-first-hotplug-recorder-1`,
with eleven tool substitutions (136MiB compressed, 1.4GiB unpacked). Owner2
cannot read protected daemon/builder cwd, fd and environment records, and has
no passwordless sudo. The original promise of an authenticated per-builder
PID/birth/RSS aggregate is therefore not established before launch.

Bounded read-only interface inspection found the installed Nix 2.34.9 public
`BuildResult` exposes status, outputs, timing and optional CPU time, but no
builder PID/birth/cgroup/RSS contract. Its logging header exposes activity IDs
and generic fields, not a documented process-identity binding. Do not decode an
activity ID as a builder PID or promote debug text, process names or timing to
ownership proof. Exact installed libstore derivation `wdjv5sml...` references
source `jmm4j1jg...`, which is absent; no source fetch or empirical build was
selected to discover private behavior. This inspection establishes no supported
unprivileged per-build identity route, rather than proving none could exist.

The exact systemd service does expose readable accounting:
`ControlGroup=/system.slice/nix-daemon.service`, `MemoryAccounting=yes`,
`Delegate=yes`, `MemoryMax=infinity`, `MemorySwapMax=infinity`. A single
preparation read saw `memory.current=1859944448`,
`memory.peak=19999731712`, `pids.current=17`, and zero memory OOM counters.
These values describe the shared daemon service, not this pending build; the
peak covers earlier work. The installed configuration does not enable
`use-cgroups` (documented default false). Neither that fact nor service
membership establishes a fresh drv-to-builder identity or excludes privileged
migration from the observed subtree. No service/cgroup limit was changed.

The lead explicitly selected the following narrower claim for this small,
fixed-graph build in the assignment headed **EXPLICIT LEAD CONTRACT SELECTION**.
This authorizes source-only driver/watcher preparation; realization remains
unselected:

- Keep the client scope's actual 1GiB/no-swap hard limit. Sample its named
  `memory.current`, `memory.peak`, `memory.events`, `memory.max` and
  `memory.swap.max`; record the cgroup and operation identity.
- Retain 3GiB as a conservative sampled cancellation threshold for the sum of
  the entire named daemon service's `memory.current` and the owned client
  scope's `memory.current`, including all nested cgroups counted by those
  files. This includes foreign activity and charged file cache. Do not subtract
  a baseline, subtract shared usage or call it per-build RSS, a hard limit, an
  unsampled peak bound, or proof of an authenticated builder aggregate.
- Refuse launch if the required fields are unreadable, the shared daemon
  identity/cgroup changes, or the sum already reaches the threshold. During
  execution, loss/change of those fields or threshold breach cancels only the
  authenticated owned client through the selected native cancellation path;
  never signal the shared daemon or guessed builder. Explicitly retain the
  residual protected-builder identity/RAM/effects blind spot. Service-wide
  samples are useful context and a coarse tripwire, not its removal.
  Bind the exact service's MainPID/birth and canonical ControlGroup identity,
  and the owned client's PID/birth/scope identity. Verify the client scope's
  limits before starting the Nix operation. The two current-value reads are
  sampled, not atomic; independent lifetime peak values are not a simultaneous
  aggregate peak.
- Preserve the exact immutable drv, eleven substitute-only prerequisites,
  one source build, max-jobs1/cores2, no fallback or remote builders, native
  540s and outer600+5s deadlines, bounded logs and fresh40GiB free-space floor.
  Record known owned physical files with `st_blocks * 512` and shared free
  space separately. Hidden store/sandbox allocation remains unknown; neither
  shared free-space decline nor visible files establish a cumulative owned
  physical bound. Preserve the existing disk qualifications and cancellation
  policy instead of silently upgrading their evidence.
- Final evidence names the native result, exact client PID/birth/group and
  readable canonical references, plus the inaccessible protected views.
  Successful client completion is not an inspection of every daemon child;
  cancellation or uncertainty does not establish their termination. Retain
  evidence and roots for owner reconciliation, with no automatic cleanup.

This explicitly replaces the earlier unproved 3GiB sampled owned-aggregate
claim. Owner2 owns source-only preparation of the bounded driver/watcher under
the selected contract. It requires no recipe, local-store, privilege, daemon
configuration or general monitoring framework change. Realization, BPF/VM
execution, retries and cleanup remain unselected. The lead selects any concrete
frozen execution package separately.

Prelaunch inspection of guard `2d2e8466` / driver `0d0b9e37` found the following
bounded supervision corrections. These hashes remain frozen and are not accepted
for launch. The selected shared-service contract and product source are
unchanged. The lead selected this source-only correction brief and assigned it
to owner2 as `4c3c0c16`, limited to the existing helper, driver and brief.

- Separate PID/birth identity from observed PGID and scope membership. A known
  PID/birth that changes group is still a surviving owned process. Group/scope
  escape is unresolved evidence and a cancellation reason, not absence.
  Direct-PID signal authority uses PID/birth; it does not require unchanged PGID
  and gives no authority to signal a changed or guessed process group.
- Do not rely on `Popen(systemd-run --scope)` returning the native timeout PID
  or on SIGINT to that launcher being forwarded. The exact installed 260.5
  manual describes synchronous execution with systemd-run as parent, without
  this PID/forwarding guarantee. Its source `s8lxzd3r...` is absent; no empirical
  launch or source fetch established the implementation detail. Add only a
  small startup handoff from the actual driver before its existing FIFO wait.
  Bind that driver's PID/birth, its immediate native timeout parent, exact
  expected cached executable/argv, ancestry to the retained Popen handle and
  named client cgroup. The same observed chain can cover an exec or synchronous
  parent launcher without assuming which occurs. Retain the launcher handle
  for supervision, and address cancellation only to the authenticated native
  timeout PID/birth. All existing memory/identity checks still precede FIFO
  release and any Nix command. A failed handoff remains unadmitted.
- Enclose every post-Popen step in the operation's error/finalization path,
  including initial process read, identity receipt, stream setup and final
  result writes. Preserve primary failure, handle, known births, scope and
  admission state. Evidence failure is incomplete supervision, never success.
  If child liveness is unknown, retain/escalate the watcher instead of returning
  through an unhandled exception. Preserve a bounded stderr fallback if a
  receipt cannot be written; no cleanup or broad signal fallback follows.
- Classify collected/inactive scopes explicitly. The current helper requires
  every systemctl result to be zero, so normal collection can instead leave
  an indefinite error loop. Accept an explicit named not-found result only
  with canonical bound-cgroup absence and reconciliation of every known
  PID/birth; arbitrary nonzero, permission or parsing errors are unknown.
  A present unit must still match its bound identity. Final canonical effects
  checks required by the watcher brief apply to failed and successful outcomes,
  and protected daemon gaps remain qualified.

Focused inert checks should exercise these actual control paths with faked
native boundaries: exec/parent launch forms; invalid ancestry or handoff; same
PID/birth with changed PGID; immediate child exit; failure at initial identity,
receipt and stream setup; explicit scope collection versus inspection failure;
and final evidence failure. No build, signal, process probe or general framework
is needed to check these branches. Lead report `3d5a2bd0` carries the findings
underlying the selected correction. Owner2 returns a frozen corrected package
with the inert actual-control evidence, preserving the original hashes and the
product/graph/resource contract. The lead selects any actual operation
separately. No further interface investigation, probe or helper takeover is
selected; no product or execution-package edits were made by the architect.

Selected diagnostic-only follow-up (`a23ea073`): after the corrected package's
focused source acceptance, owner2's retained-only diagnosis `52305e6e` found that
the first retained authenticated exec-form chain and its replay pass, including
the resolved coreutils executable with the expected timeout argv. The guard
did not retain the stage, invariant name and values at its first failure.
Consequently, a later valid authentication cannot establish whether an earlier
latched failure preceded it, and the exact primary invariant is unrecoverable
from these records. Do not infer failure ordering, cause or a resource breach.

The lead selected edits only to the existing helper, brief and owned evidence
to retain an explicit first-failure stage/name and bounded expected/observed
scope, handoff and pre-FIFO values. Actual-control inert checks cover the first
iteration and a changed second read, preserving the first failure even when
later observations pass. Every admission, identity, cancellation and resource
rule remains unchanged; this improves evidence without weakening a refusal.
Preserve failed raw records and frozen hashes. Owner2 owns the edit; no duplicate
diagnosis or native inspection is needed. No product, driver, graph or resource
change, native retry or use of fresh attempt paths is selected. Any material
design deviation returns through architect0 and the lead before implementation.

Lead-selected RAM contract revision: owner2's
single capacity snapshot
[recorder-capacity-snapshot-1/snapshot.json](repair/hotplug/recorder-capacity-snapshot-1/snapshot.json)
records daemon `memory.current=6329794560` bytes, already above the selected
3GiB threshold before this build. That snapshot proves no attribution or cause.
The one further read authorized for this design decision, at
`2026-10-23T20:22:33.297496+00:00` (0.023s), returned:

| Field | Bytes / identity |
| --- | --- |
| Host MemTotal | 101227433984 (about 94.3GiB) |
| Host MemAvailable | 59874398208 (about 55.8GiB) |
| Whole daemon memory.current | 6356430848 (about 5.92GiB) |
| Whole daemon memory.peak | 19999731712; service-lifetime context only |
| Daemon hard RAM/swap limits | Both `max`; unchanged |
| Daemon PID / birth | 1299969 / 1188973808 |
| InvocationID | d55bfc9e04274325bb8b73d581bf79e3 |
| Canonical cgroup device / inode | 21 / 4157972 |

The named service was active with memory accounting enabled at the same
`/system.slice/nix-daemon.service`; all read memory-event counters were zero.
Its identity values match owner2's retained snapshot. Fields are non-atomic and
this is one observation, not a stability, attribution or future-capacity claim.
No process scan, polling, privilege or Nix operation was used.

For the unchanged one-recorder/eleven-substitute graph, the lead explicitly
selected the following replacement of the **3GiB RAM tripwire only** in the
assignment headed **EXPLICIT RAM CONTRACT REVISION SELECTED**:

- Set the absolute sampled whole-daemon-plus-client ceiling to **12GiB
  (12884901888 bytes)**, without subtracting any baseline or foreign usage.
  Refuse admission unless that sum is **at most 8GiB (8589934592 bytes)**,
  preserving at least 4GiB to the ceiling before releasing the existing FIFO.
  Before the client exists, apply the same admission ceiling to daemon current;
  repeat with both actual cgroups before admission. Cancel at a sum >=12GiB.
- Require fresh host **MemAvailable >=20GiB (21474836480 bytes)** for admission
  and cancel if it falls **below16GiB (17179869184 bytes)** during the operation.
  These leave the same 4GiB planning margin above a substantial explicit host
  reserve. Record MemTotal and MemAvailable from `/proc/meminfo`; missing,
  malformed or inconsistent required fields refuse/cancel. This host-wide
  estimate is a separate coarse safeguard, not a reservation or owned-RSS
  measurement. Do not infer that memory below the floor is an observed incident
  pressure threshold or that staying above it guarantees against OOM.
- Keep the actual client hard limit at **1GiB/no swap**. The 4GiB allowance is
  a conservative planning assumption: up to that client limit plus 3GiB for
  the selected small C/BPF build and tool-materialization effects. The eleven
  substitutions are 136MiB download/1.4GiB unpacked, not measured compiler RSS.
  No compiler/kernel/SDK source build is permitted. The snapshot leaves about
  6.08GiB from observed daemon usage to the selected absolute ceiling; even a
  fully charged 1GiB client fits the admission ceiling. The build allowance is
  unproved and must not become a promised peak or completion bound.

This selected contract uses the host's observed spare capacity to admit the fixed
small operation while retaining a numeric service-wide stop and host reserve.
Foreign activity or charged cache can still cause cancellation; no attribution
is made. Sampling can miss peaks, protected builder identity/containment/effects
remain unknown, and cancellation of the authenticated native timeout does not
prove protected daemon effects ended. Preserve the same service/operation
identity checks, first-failure evidence, direct-timeout PID/birth authority,
roots retained on uncertainty and no automatic retry/cleanup.

The graph, native540/client600+5 deadlines, log caps, client CPU limit, known
physical accounting and independent **3GiB shared-disk-decline** tripwire,
43GiB fresh disk admission and40GiB disk floor remain unchanged. No daemon
limit, recipe, product, local store, GC, privilege or monitoring-framework
change is selected. Owner2 is assigned source-only guard/brief/inert-check
preparation and a fresh build3 operation identity under these exact thresholds.
The original failed packages/evidence remain preserved. No extra capacity
snapshot, interface investigation, framework or helper takeover is needed.
Actual realization remains unselected: the lead selects the frozen build3
execution package separately after preparation and source acceptance.

Lead-selected bounded startup classification: retained
build3 `first-failure.json` and `result.json` establish that the first recorded
failure was `scope.classify/present-invocation`: query rc0, exact named unit,
`LoadState=loaded`, `ActiveState=inactive`, empty InvocationID and ControlGroup,
no bound identity, and canonical expected cgroup already present. The result
retains `admitted=false`, native exit-2 and the same primary failure. Later
authenticated driver/timeout records do not erase it. This is a concrete
startup-observation refusal before Nix admission, not a product/build or
resource failure. No new live observation is required for the correction.

Introduce only `startup-pending` for that exact property tuple while the
launcher remains live, no identity has ever been bound, admission is false,
no prior failure is latched, and elapsed time is below the existing five-second
startup deadline. Missing properties, nonzero query status, wrong unit,
permission/parsing errors, unexpected nonempty identity/path values, and other
load/active states are not covered. In particular, do not invent tolerance for
`activating`, `failed`, or named-not-found with a present canonical cgroup.

For this tuple, canonical-cgroup presence and absence have distinct meanings:

- Present is the build3 observation. Keep `cgroup_absent=false`; read and retain
  its canonical device/inode, all required memory fields and readable children
  as tentative observations, without assigning a bound scope identity. Do not
  demand settled client limits solely from this pending snapshot; record them,
  and require the exact1GiB/noSwap limits before active binding/admission.
  Field/canonicalization/permission failures still fail closed. The actual
  memory.current remains charged in the sampled whole-service sum.
- Absent is an allowed unbound variant of the same exact tuple, not an observed
  build3 fact. Retain actual canonical absence and no client accounting yet;
  zero contribution means only no cgroup charge at that sample. It does not
  establish process absence, successful completion or admission. Continue the
  unchanged daemon/host/disk/log checks and known-birth supervision.

On both paths retain a bounded pending observation, drain existing streams and
reconcile known births through the same supervision loop. Do not bind an empty
InvocationID, authenticate admission from a tentative cgroup, signal merely for
this pending tuple, or mark the run successful/absent. Transition to ordinary
active binding only after the exact named active scope, nonempty invocation,
canonical cgroup, actual driver/timeout ancestry/birth/exe/argv and all selected
hard-limit/resource gates pass. After the first binding, every identity loss
remains an immediate failure even before FIFO admission; pending never reopens.

The five-second budget starts at the existing operation start, is never reset,
and includes native property reads. Check fresh elapsed time before admission
so a slow observation cannot release the FIFO after the deadline. At expiry or
launcher exit before admission, latch the explicit startup/early-exit failure
with the last pending observation and preserve native cancellation, retained
supervision and qualified final effects. Add no sleep, retry, new launch or
deadline extension. The existing supervision sampling cadence is unchanged.

The lead selected owner2's source-only implementation brief, limited to the
existing classifier/caller, pending observation and actual-control inert cases:
retained present-cgroup tuple to valid active admission; the absent variant;
pending through deadline or early exit; and the same tuple after binding,
wrong/nonzero/malformed states and unreadable required fields failing closed.
Assert no FIFO release, no false absence and no primary-failure clearing from
pending. Product, driver build commands, graph, RAM/disk/log thresholds and
all failed evidence remain unchanged. Owner2 prepares a fresh build4 package
identity with this correction, preserving build3 and carrying the cumulative
budget/evidence forward. The lead's accepted owner assessment reports a later
valid active observation at0.5529s with full chain and hard limits; this does
not erase the earlier refusal or establish the same cause for build1. No
duplicate diagnosis or scan is needed. Actual build4 execution remains
unselected and requires the lead's separate frozen-package selection.

Architect0 owns this brief; the lead owns acceptance, plan/state/portal and all
Git mutations. Initial records are committed as `e8d72331`. Session identity was
verified with `dev-session current` and both matching environment markers:
`2026-10-22-ci-failure-analysis`, `/home/aither/workspace/ai/vpsfree.cz`.

## Scope and boundaries

Deliver source-supported causal explanations, recurrence evidence and a useful
test assessment for three failure families. This is an investigation: read
canonical Git objects and existing artifacts, retrieve historical GitHub
metadata/logs/artifacts, and write only this session's assigned evidence and
findings. No application edits, tests, builds, VM diagnostics, reruns, production
operations, merges, pins, deployment or lifecycle actions are selected.
Longer disposable diagnostics must first be proposed with exact scope to the
lead/user. Leave both sessions open and all source-session files unchanged.

The read-only handoff root is `../2026-10-20-kernel-check/`. Run `39767770407`
belongs solely to its existing watcher: consume preserved evidence but make no
new per-run remote observations, polling, downloads or cancellation for that
run. Historical listing may contain it; exclude it before collection. Its
merge waiver neither makes CI green nor resolves causality.

Source identities: vpsadminos target
`846bb469505789ba0b2a405fa5905ba6d8253006`, base
`55c5046514d06fe9398a022c1622bdaae5228841`; historical seed
`b81c43ff6865a033268072f55cd94ad763d0630b` / run `39600028637`.
Read `repos/vpsadminos.git` using exact revisions. No fetch or worktree is
needed; request missing source objects through the lead. Linux is reference
only. Read exact-revision AGENTS.md before substantive source work.

## Interfaces, invariants and causal boundaries

| Family | Protected behavior and component boundary | Evidence limit to preserve |
| --- | --- | --- |
| Impermanent guest upgrades | An old daemon's running container and ephemeral root survive target userspace activation; runtime configuration loading and API export must describe the same running root. Kernel and boot identity remain old. | Five temporary-to-base dataset reports and retained init PIDs do not distinguish reporting fallback, lost metadata or changed mounts. Historical recurrence does not exclude current generic-service interaction. |
| Nested Podman | The predecessor can create a networked system container, then preserve a nested application workload through activation. Separate guest network prerequisites from Podman and target activation. | DHCP sandbox denial precedes failed ifup, no IPv4/default route and readiness timeout. Target service never executes in this path; exact denied syscall/policy and introducer remain unresolved. |
| AMD aged-scale livepatch | CPU teardown must leave one runnable stopper and no pinned tasks; livepatch qualification must preserve workload progress and kernel health under stress and hotplug. | Warning precedes incoming v7 but follows current OS boot with frozen 6.12.95.6/v6. The runnable count is two, only migration/127 is named; scheduler-entity accounting means this does not prove a second task exists. Successful offline and later activation do not clear the violation. |

Source continuity is not runtime equivalence. A missing log is not proof of
nonexecution. Distinguish an observed first error, source-proven mechanism,
inference and unresolved trigger. Do not turn a candidate into an incident
cause without linking it to the recorded execution. Test-purpose conclusions
must distinguish safety, data continuity and observability guarantees.

Final source discriminators, supported and qualified in the linked lane findings:

- Impermanence: the old and current writers persist base-dataset metadata before
  selecting the in-memory temporary root, with a later save conditional on CPU
  scheduling. Setup uses `zfs create`, not a ZFS clone. Whether those stale bytes
  were reloaded in these runs remains unproved without runtime YAML. Earlier
  passing target `3ae196d60b2811e52cbb75a204108df629dca42d` contains
  `adopt_run_conf` / `adopt_live_root`; removal at
  `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` deliberately reverts unsafe
  first-prefix-match mount adoption. Passing history could therefore mask the
  writer defect by target-side repair. Compare that source boundary explicitly;
  do not propose restoring unsafe mount adoption to recover passing assertions.
- Podman: immutable predecessor Linux
  `fbda79346b89b2d2486edd22e4bbbca0154d96b7` contains AUTH_GUARD EACCES
  branches for PR_SET_NO_NEW_PRIVS and seccomp authenticated-transition entry.
  Source configuration selects the option for 6.18, but actual binary config,
  guard rejection and failed call remain unrecorded. Distinguish this candidate
  from ordinary NNP/capability preconditions and filter rule denials.
- Hotplug: frozen `kernel/sched/deadline.c` counts scheduling entities through
  `inc_dl_tasks` / `dec_dl_tasks`; the fair server is not a task_struct, and
  `sched_cpu_dying` stops it after the warning. Entity/server accounting is a
  concrete alternative to a missing task, not the established cause. Capture
  fair-server/CFS/DL state alongside task/pinned evidence in any later proposal.

## Independent packages and write ownership

| Owner | Brief | Exclusive deliverables |
| --- | --- | --- |
| implementer0 | [Impermanence](lane0-impermanence-brief.md) | `impermanence-findings.md`, `evidence/impermanence/` |
| implementer1 | [Nested Podman](lane1-podman-brief.md) | `podman-findings.md`, `evidence/podman/` |
| implementer2 | [AMD hotplug](lane2-hotplug-brief.md) | `hotplug-findings.md`, `evidence/hotplug/` |
| implementer3 | [History and utility](lane3-history-brief.md) | `history-findings.md`, `recurrence.tsv`, `evidence/history/` |

Architect0 writes only this design, lane briefs and dispatch/acceptance notes.
Lead alone edits plan/state/portal, synthesis and the shared Git index. Owners
report to the lead, send architectural deviations to architect0 and coordinate
artifact requests with implementer3 through verified same-session messaging.
No new members or automatic reviewer assignment. Saved roster settings remain
unchanged. Every new substantive assignment verifies the live roster first.

Implementer3 is sole historical GitHub collector; others request exact run/job/
artifact needs and continue local source work meanwhile. Download once into
run/attempt/artifact-ID paths, record source URL/time/size/hash and extraction
limits, then share immutable local paths. Never overwrite retained source
evidence. Small lane-owned source excerpts can live in each lane's evidence
directory; no shared finding edits.

## Historical sampling and evidence strength

Begin with 10–15 relevant recent completed runs per family, including staging
and relevant feature heads. Declare selection rule/window before classifying;
include failures, passes and relevant prebuild/cancelled/unexecuted rows rather
than selecting only matches. Report if retention or availability prevents the
target sample. Current preserved run is context, outside the historical sample.

One recurrence row is a run/attempt/job/test observation, with run/job URLs,
exact head and branch, date, predecessor/kernel/livepatch identity where known,
first-error phase/signature, result category, duration, local evidence and
strength. Separate `executed-pass`, `exact-signature-failure`, `other-failure`,
`unexecuted`, `cancelled`, `prebuild-failure` and `unavailable-evidence`.
A workflow conclusion alone does not establish individual test execution.
Use primary logs/native results as strongest execution evidence; source proves
possible mechanics; metadata establishes job status only. Report denominators
per test/family and attempts separately; the five cases within one run are not
five independent runs. A repeated symptom does not establish flakiness,
harmlessness, a common root cause or baseline equivalence.

## Minimal diagnostic proposals, not selected executions

Owners refine these to exact source-validated paths/commands and discriminating
outcomes. Prefer existing evidence first; identify what cannot be recovered.

1. Impermanence: one representative `upgrade/from-6.12-guests` disposable
   scenario, only through first activation/assertion. Capture before/after raw
   run-configuration `config.yml`, file identity, API JSON, init PID plus process
   birth identity, `/proc/<init-pid>/mountinfo`, root source/ZFS identity and
   persistent/ephemeral marker contents. Capture timestamped sysctl service log,
   `/run/service/sysctl/{applied,done}`, check outcome and managed-value readbacks
   without triggering an extra apply. Separate bytes lost on disk, loader
   fallback with intact bytes, API-only mismatch and real mount/data change.
   First propose this one case; a later accepted repair needs all five cases
   plus graceful/abrupt daemon restart and cleanup regressions.
2. Podman: one disposable predecessor `3cb830e596a7fed900bec49f50c9b6cf51e76bb5`
   container at the failing Debian image identity, stopping before package
   installation or target activation. Preserve package/image hashes, effective
   LXC/seccomp config, credentials/NoNewPrivs/Seccomp status, and exact syscall,
   arguments and errno for dhcpcd sandbox setup using a bounded process trace.
   Capture address/routes and service journal at first permanent error. Do not
   disable seccomp as a proposed fix without proving the denied mechanism.
   Identify whether failure is PR_SET_NO_NEW_PRIVS, filter installation or a
   filtered syscall; bind EACCES to actual credentials, NNP, binary-config and
   AUTH_GUARD state before assigning it to a policy mechanism.
   Regression acceptance covers supported image/predecessor policy, network
   readiness layers, nested workload continuity and security confinement.
3. AMD: first inspect retained callback/task/affinity traces. If insufficient,
   propose one explicitly bounded reproduction of the exact aged-scale-v6
   preparation through first CPU127 offline, before v7 insertion, preserving
   frozen binary/toolchain/module identities. Specify bounded scheduler/hotplug
   traces and loss counters that identify task wakeups/migrations, teardown
   callbacks, runnable count, CFS/DL/fair-server entity state and pinning at
   failure; distinguish a real extra task from entity/accounting state. Identify instrumentation
   requiring a kernel build as a separate proposal. Record boot/service/stress
   sysctl values at phase boundaries. No repeated stress lottery. A repair must
   preserve both hotplug cycles, transition bounds and zero new kernel faults;
   timing success alone is insufficient.

## Compatibility, deployment and recovery implications

This work changes no runtime state, schema, wire protocol, API, CLI, generated
configuration or pin. No coordinated node update is required by investigation.
Any proposal changing runtime config must support the old writer/new reader
and downgrade reader, retain running-container mounts, and define cleanup
without deleting live roots. Never equate a daemon restart with container
restart or a userspace switch with kernel replacement. Network proposals must
respect predecessor image/daemon/kernel combinations and sandbox guarantees.
Do not silently retarget a historical upgrade case to erase a supported path.
Kernel/livepatch proposals must preserve exact boot ABI, quarantine and recovery
constraints; forced transition/unload is not an accepted recovery shortcut.
Any later rollout needs separate design/authorization, ordering, rollback
criteria and explicit statement if coordinated machine updates are necessary.

## Acceptance and checks

Every lane supplies: a concise explanation for a reader unfamiliar with the
test; exact source/observation chain and remaining uncertainty; relevant
recurrence rows; invariant and user importance; actual assertion coverage and
gaps; measured runtime/setup/maintenance/noise costs; a justified keep/revise/
remove recommendation; prioritized concrete proposals with minimum diagnostics
and regression acceptance. Existing warning/assertion severity cannot be waived
merely to make CI green. Removal needs unsupported/redundant-contract evidence.

Quick checks are read-only citation/line/hash validation, phase ordering and
identity consistency, coverage/category accounting, and cross-lane reconciliation.
No product tests, builds or longer checks are selected. No automatic final
review: the deliverable is investigation/findings/evidence only. Lead accepts
material decisions and the final user-facing synthesis. Session remains open.

## Investigation acceptance handoff

Architect acceptance is complete for [impermanence](impermanence-findings.md),
[Podman](podman-findings.md), [hotplug](hotplug-findings.md) and
[historical recurrence/test utility](history-findings.md), with the shared
[recurrence table](recurrence.tsv). The impermanence cost comparison was
corrected to separate script, ordinary whole-test and benchmark whole-test
observations; its causal conclusions and current failure-time sum are unchanged.

The fixed historical sample has 15 workflow runs and 111 observations, with
per-case execution and phase denominators and source-current exclusion. The
lead accepted the available execution count without expanding collection.
Historical passes differ in target recovery source or lack immutable guest
image identity; recurrence is not a controlled causal comparison.

The proven persistence defect is distinct from missing runtime YAML/root/data
evidence. Podman's exact failed prctl/policy and the hotplug task/entity/count
trigger remain unresolved. Hotplug fails at the post-transition health check;
later downgrade/removal and normal complete cleanup phases did not execute.
Diagnostics remain unexecuted proposals requiring separate selection. No
acceptance blocker remains for these bounded findings; lead reconciliation and
the user-facing synthesis retain lead ownership. No lifecycle action is selected.

## Authorized repair phase

The user now directs finding the remaining root causes and fixing them, resumed
after a wait. Session-owned diagnosis, code/tests/docs and feature publication
are authorized. Integration, deployment, production changes/configuration pins and
session lifecycle actions are not authorized. A proved repair may require a
component packaging/input update: report its owner and compatibility to the lead
for feature-scope selection, rather than silently changing it. Do not touch the source session's
branch, records, runtime state or current-run watcher. Keep this session open.

The lead freshly provisioned and registered
`worktrees/2026-10-22-ci-failure-analysis/vpsadminos`, branch
`2026-10-22-ci-failure-analysis`, from remote `origin/staging` at
`846bb469505789ba0b2a405fa5905ba6d8253006`. The local canonical `staging`
branch was older and is not the chosen base. Worktree source/index were clean;
checkout occupies 331 MiB. The add command's hook-signature failure occurred
after checkout/registration; implementer3 owns its reconciliation and exclusive
Git setup window. No other member runs Git mutations until lead releases it.

The exact-base AGENTS.md, relevant upgrade/container/livepatch/testing docs and
`docs/os/patch-series-policy.md` govern the repair. Reuse the workspace
procedures already read; reread changed guidance. The monitor and mandatory
review skills govern long operations and final review. Keep existing Markdown
findings/design/state and native checks; no new generalized ledger, review
harness or parallel tracking system. Native tests and small task-specific
diagnostic recorders are implementation, not review machinery.

### Scope and component choices

vpsadminos is the initial implementation repository. Linux remains exact-source
reference during attribution. If a proven kernel defect requires code changes,
report the owning kernel range, existing logical patch/upstream provenance,
source paths, intended behavior, ABI effects, build/copy size and validation to
the lead before creating a separate session-owned Linux worktree. Do not edit
canonical bare repositories or another session's checkout. No component pin,
frozen fixture identity or historical predecessor pin changes are selected.

The frozen 6.12.95 boot binary, notes, SDK and v6 module are a single compatibility
boundary. A source edit/rebuild changes identity even if `uname` is unchanged.
Dynamic recording must preserve that boundary. A diagnostic kernel needs a
separate matched SDK/module/identity design and budgeted lead selection; it
cannot replace exact-frozen qualification or reuse modules by bypassing guards.
An incoming v7-only edit cannot correct a warning that occurs before v7 loads.
Likewise current daemon changes cannot fix predecessor-only DHCP execution.

### Repair interfaces and invariants

**Impermanence writer.** Persist the complete finalized run selection (dataset,
run ID, distribution, cleanup flag) before the root becomes a running workload,
independently of CPU scheduler assignment. Keep existing on-disk fields readable
by old/new daemons. Custom `ct boot` and failed preparation must retain their
existing lifecycle; do not add indiscriminate saves to every setter. The logical
owner is container start/run configuration, with meaningful reload regressions.

**Legacy live-state recovery.** The target must support immutable old writers;
fixing new writes alone leaves existing live containers broken. Before changing
recovery, implementer0 must provide the exact algorithm and race/GC proof to
architect/lead. This is an internal design dependency, not a new user-permission
gate. Required contract:

- Bind the actual live init process using stable process/proc handles and birth
  identity, verifying it remains the same process throughout inspection. Read
  its mount namespace/root, not an arbitrary host mount or dataset prefix.
- Resolve a candidate from that authenticated root and match it to the exact
  ZFS dataset/device/root identity and container ownership. Reject descendants,
  foreign roots, old-run candidates and ambiguity. Descriptor/device/inode
  checks must account for ZFS bind-root layout and process exit/PID reuse.
- Reconcile valid saved run ID, existing GC records and live identity before
  repair. Preserve the existing run ID/GC ownership when valid; never invent
  a fresh ID and re-register a live dataset on a prefix guess. A missing record
  needs a separately proved unique ownership path, not silent reconstruction.
- Make metadata repair atomic relative to this container's stop/start and GC
  view. Do not hold unsafe lock combinations or perform destructive cleanup
  on contradictory/missing evidence. Preserve the workload/live storage and
  report a controlled recovery error where identity cannot be established.
- Prefer the smallest demonstrated supported repair: stale base selection with
  valid saved run ID and matching existing GC ownership. Do not create a
  general-purpose recovery framework. Separate valid saved metadata, stale base selection, missing fields/file and
  conflicting records. State which cases can be repaired and which require
  operator intervention. An unresolved-case refusal must not itself trash the
  live root or silently report a valid base-backed model.

Recovery must retain the authenticated `ProcessIdentity` through installation.
The existing numeric `RunConfiguration#init_pid=` constructs new handles and
cannot be called after recovery validation. A small internal install helper in
`run_configuration.rb` may share its existing lease/retirement protocol: the
normal setter constructs its identity, while recovery installs a duplicate of
the retained handles. The caller keeps its original; the duplicate is either
transferred to run ownership or closed on refusal/exception. Close replaced
identities outside the protected region. Preserve checks before allocation and
after lease waits, lock ordering and retirement wakeups. Never call installation
while holding a lease on that same run. Final authentication must remain adjacent
to installation/publication, with no intervening blocking probe or lease wait.
Tests cover no second numeric construction, independent duplicate lifetime,
rejected-install closure, replacement/retirement races and ordinary setter
behavior. This is a refinement within the existing invariant and file scope;
reader edits were held for the actual capture assessment below.

The lead accepted a bounded pool-level refusal safeguard after source inspection
showed that omitting a failed container import lets GC classify its records as
unused. A per-container hold also misses conflicting records naming the same
dataset under another owner. Use one monotonic, in-memory retirement-inhibited
flag on that pool's GC instance when container loading/recovery fails before
the worker starts. Fence every GC retirement route, including periodic/manual
prune and queued explicit free, preferably at the common destructive sink;
return non-success so registered ownership records remain intact. Keep worker
draining, normal stop and new registration persistence functional. Synchronize
parallel import failures without holding locks across process/ZFS probes.

The flag lasts for this import only. A fresh Pool/GC instance must reauthenticate
all container loads; only a fully successful import resumes collection. No new
schema, ownership reconstruction, manual release or generic recovery command is
introduced. Report both the omitted/unmanaged container and inhibited temporary
dataset collection. This delays unrelated reclamation intentionally; it does
not restore datasets already in the trash bin. A skipped explicit free without
a persisted GC record cannot promise automatic collection after reimport.
Tests cover both retirement routes, conflicting aliases, missing/malformed
load evidence, failed retry, and a fresh successful import. This acceptance
does not remove the actual stale-file/private-root capture prerequisite for
reader implementation.

The lead has separately authorized preparation of the GC primitive before that
capture: implementer0 may edit only `osctld/lib/osctld/garbage_collector.rb` and
`osctld/spec/osctld/garbage_collector_spec.rb` for the monotonic inhibition flag,
common retirement-sink guard and focused unit coverage. This unit does not need
the eventual root-layout facts. Prove real queued work is consumed without
retiring datasets or deleting registered records, duplicate aliases cannot
bypass the guard, and ordinary uninhibited collection/add/save/stop still work.
Use bounded synchronization and a positive retirement control, not sleeps or an
immediate stop that prevents the queue item from executing. A fresh GC instance
starts uninhibited; actual import/reimport-trigger tests wait for that wiring.

Do not wire a recovery trigger, modify pool loading or implement the reader or
identity installer during this bounded unit. The identity installer remains
gated on actual capture and demonstrated reader necessity. Keep the intermediate
GC helper uncommitted or fold it into the final impermanence logical owner under
the lead's Git window; no unused mechanism may ship. Root-layout capture remains
the first VM priority, with existing resource/root-retention boundaries unchanged.

**DHCP entry attribution.** Reproduce one original-predecessor container start
with exact image provenance or honestly mark a new image sample. The minimum
first result is which of PR_SET_NO_NEW_PRIVS and PR_SET_SECCOMP fails, its args,
errno and ordering. Trace parent/child credentials and actual NNP/config/filter
state as available. A ptrace-sensitive guard means trace outcomes require that
qualification. Distinguish ordinary filter preconditions, AUTH_GUARD entry and
outer filter/LSM. Do not disable seccomp, add privileges, switch to static IP or
silently retarget the predecessor as a repair. Once attribution is established,
propose/implement the narrow owning-component fix with explicit supported
predecessor/image handling; escalate kernel-source scope and packaging needs.
Following daemonized children with foreground `strace -f` can keep the wrapped
oneshot service alive after `ifup` exits. Separate trace-linked syscall failures
from wrapper-induced service timeout; preserve the original parent/exit behavior
where a supported tracer mode permits it, or label this observer effect. Missing
or capped snapshot fields are evidence gaps, not successful state observations.

**Hotplug attribution.** Preserve CPU127's original first-offline/v6 boundary.
Record locked rq runnable/pinned and class counts, fair-server entity/timer
state, relevant wake/enqueue/dequeue/migration/callback stacks and trace loss.
The count-two dump is not proof of a second task. A recorder must use exact
binary/BTF/DWARF probe sites and be prepared before costly aging. No warning
suppression, retry lottery, reduced envelope passed off as equivalent, or
callback-order patch based only on source plausibility. Preserve cumulative
health checks and all eventual transition/removal/progress requirements.

A narrowly opt-in first-hotplug diagnostic mode fits this attribution scope,
pending exact-binary/probe/build feasibility and lead scheduling. Preserve the
original CPU/workload/aging parameters and default full qualification. Validate
attachment before aging, arm only the first hotplug, and stop/drain in an ensure
path before cumulative health assessment. Retain the original offline/WARN error
as primary if draining or cleanup also fails. A healthy first hotplug must end
with an explicit diagnostic-stop failure before any v7 activity, never a normal
qualification pass or an expected-failure pass. Mark later phases unexecuted and
retain cumulative dmesg and loss accounting. Exact command, hashes and resource
plan remain prerequisites; this design selects no VM, attach or build operation.

Recorder admission preparation uses a standalone, session-owned native fixture:
`repair/hotplug/probe-admission.nix` with `probe_admission.rb`, owned by
implementer2. Import the existing native test framework and exact 846bb OS
source/locks plus frozen boot configuration, recorder and hash-verified v6.
Do not import the full common qualification fixture merely to obtain its VM:
that adds unrelated v5/v7, helper-module and SDK requirements. Record the smaller
fixture's exact configuration differences. Keep the 128-CPU, 16-GiB topology;
this is admission-only and is not an equivalent qualification workload.

The lead measured AuthenticAMD EPYC 7551 and 64 CPUs in the launch process's
affinity mask. The earlier native capacity of 96 is not physical-CPU evidence.
The runner's default 1.5 overcommit policy cannot admit 128 vCPUs against that
64-CPU affinity. The lead explicitly selected a separate 2:1 exception for this
short probe-only diagnostic: preserve 128 guest vCPUs, require fresh launch
affinity and effective ancestor quota/cpuset capacity of at least 64 logical
CPUs, and refuse unknown or smaller effective capacity. Unrestricted quota is
acceptable when established through the relevant ancestors. Do not claim that
the native 1.5 policy was met or change the native scheduler's defaults.

The exception covers only call attachment/count admission, one two-second count
child and the overall 900-second diagnostic envelope. It selects no hotplug,
aging, workload population, v7, performance or incident-host/timing equivalence.
Record affinity IDs, known quota/cpuset limits and fresh host load/runnable/CPU
pressure context; defer if existing sustained saturation defeats the selected
budget. Do not overlap the session's full-host image compression or terminate
foreign workloads. Direct JSON reserves zero resources, so these checks are
external admission, not a native reservation. Memory/SHM remain separately
admitted without overcommit, and the prior VM's effects proof must release the
session slot. Later aged-workload execution requires a separate CPU-context
selection. This design acceptance does not select the AMD VM itself.

The proposed short-probe guardian may interrupt the authenticated native runner
at 780 seconds from its recorded launch and allow up to 120 further seconds for
native cleanup. At 900 seconds it reports incomplete/escalates if ownership or
effects remain unresolved; this is an escalation boundary, not a hard bound on
VM lifetime or resource residence. An earlier resource breach interrupts
immediately and starts its own 120-second escalation interval. No automatic
broad KILL, data deletion or claim that effects ended follows. The watcher keeps
responsibility for exact process/disk/lock/socket reconciliation beyond the
threshold when needed. Capture/cleanup can be interrupted and remain incomplete;
the current artifact-transfer timeouts do not establish a 120-second completion
bound. Final fixed-command/hash/admission checks and lead selection remain
necessary before any launch.

Architect inspection accepts the prepared short-probe package for lead
selection: guardian SHA256
`01dbef171620b4c7792f9984b9fb7bc1b3656d3ffe07ff1c79f891e9b13a48f1`
and launcher SHA256
`8662565f80d237d8d31b477e0c72e2c44f778b34657fd265e229e29a9ab96572`.
The frozen native JSON has no managed/root disks; the exact installed osvm reads
the existing squashfs as read-only media and places any virtiofs memory backing
in `/dev/shm`. It does not create a writable image copy. This supports a separate
2-GiB future regular-filesystem forecast for this short probe, with 44 GiB free
at launch and cancellation at 42 GiB, preserving the 40-GiB reserve subject to
the disclosed sampled overshoot limitation. The earlier 24-GiB VM forecast
continues to apply to its other lanes; this exception does not admit aging or
additional disks/builds.

The package requires 24 GiB host MemAvailable, at least 20 GiB effective ancestor
memory headroom, and 17 GiB free SHM; its selected command requests a 22-GiB
scope with swap disabled. A smaller ancestor limit can constrain that scope
earlier, so 22 GiB is a ceiling rather than guaranteed available capacity.
The actual 64-CPU affinity/quota policy and two bounded host-load samples are
checked before launch. The main log has a hard 32-MiB writer limit; aggregate
64-MiB output and 2-GiB allocation checks are sampled. Fixed command/root/hash
checks, retained owned process births, canonical references and final
socket/lock checks preserve incomplete results on uncertainty. Signals target
only the authenticated session/process group created by the fixed native spawn;
path matches do not grant signal authority. Escaped references and incomplete
cleanup retain watcher responsibility. Inspection launches no VM and does not
prove fresh host admission, live cancellation or effects completion.

Before attaching, verify AMD vendor, configured/online topology, actual boot
image/notes/build ID, module hash and completed v6 transition with no force or
identity bypass. Run only the bounded recorder probe-only attach/check/detach,
including its short CPU127 child/count checks; no CPU hotplug, stress population,
four-hour age or v7. Retain baseline/final cumulative kernel health and probe/loss
results. Missing or rejected probes fail admission. Native VM shutdown replaces
any attempt to force a quarantined livepatch transition or unload. Later aging
requires admission again in its own exact guest configuration.

Prepare native JSON/complete closure/cache/all-disk metadata and an exact command,
deadline, output/physical budget and native stop plan before lead selection.
There is no VM admission or realization authorization in this path allocation.
The shared native runner/root remains with its assigned owner. The session fixture
does not enter ordinary test discovery or add a generalized harness; ordinary
qualification wiring remains held until actual build/admission feasibility.

### Four execution packages and exclusive files

All members retain their saved model/effort/access. Verify the exact live roster
before assignment. Preparation can proceed immediately in the owned worktree;
source edits require each owner's path/access confirmation and installed hook
status. Git mutations remain serialized by lead-issued ownership windows.

| Owner | Result and exclusive source boundary | Dependencies and initial acceptance |
| --- | --- | --- |
| implementer0 | Impermanence writer, authenticated legacy reader and focused unit regressions. `osctld/lib/osctld/{container.rb,container/run_configuration.rb,commands/container/start.rb,pool.rb,garbage_collector.rb,container/stop_handler.rb}` and directly corresponding osctld specs; propose extra helper paths before adding. | Can implement the proven writer once hooks/access confirmed. Prepare exact recovery algorithm before reader edits; exact legacy state capture is first VM priority. Supply docs prose to implementer3. Never restore removed prefix adoption. |
| implementer1 | DHCP predecessor source/entry diagnostic and proven owner repair. Own session `repair/podman/` tools/brief; may prepare a focused `tests/suite/upgrade/nested-podman-sandbox.nix` and sibling `nested-podman-sandbox/` only after path confirmation. | No speculative kernel/LXC/client source edits. Derive precise one-start command and source/image capture; target-side fix must not claim to repair a never-activated predecessor. Coordinate any added source paths through lead. |
| implementer2 | CPU-hotplug recorder, phase-local health checks, proven kernel-owner repair design. Own session `repair/hotplug/` tools/brief and `tests/suite/kernel/{livepatch-6.12.95-common.nix,livepatch-6.12.95/qualification.rb}` plus new narrowly named hotplug recorder files. | No five-hour run before recorder/probe/ABI/storage preflight. First prepare exact source/binary probe feasibility and budget; kernel worktree/patch/build requires lead scope selection. Preserve existing no-fault and frozen identity contracts. |
| implementer3 | Independent regression/diagnostic support, hooks, shared fixture edits and technical docs. Sole editor of `tests/suite/upgrade/common.nix`, `tests/all-tests.nix`, `docs/os/testing.md`, `docs/os/updates.md`, `docs/containers/datasets.md`; session `repair/support/`. | Lead's current exclusive Git window is hook setup only. Gather exact requested changes from other owners and apply serially; no competing edits to common.nix. Add focused imperative-state capture/regression fixture after agreeing a new exclusive path. Prepare command/resource receipts; do not self-launch long operations. |

No owner edits another owner's files. Unit specs colocated with implementer0's
logic stay with that owner; implementer3 owns integration fixture work. If two
repairs need shared code outside this table, stop overlapping edits and obtain
lead allocation. No one stages another owner's work. Every intended commit's
paths and logical owner are declared before the lead grants its Git window.
Fold caused follow-ups into their logical owner; retain truthful upstream and
downstream provenance/version history. Do not rewrite merged historical owners.

Confirmed preparation paths: implementer3 may add
`tests/suite/upgrade/from-6.12-guests-first-switch.nix` and
`tests/suite/upgrade/impermanence_first_switch.rb` (Ruby snake_case naming). The explicit diagnostic flag
defaults false and registration is opt-in, without `ci` tagging. Give the case
a unique name; strip the flag before predecessor fixture construction. Preserve
the original assertion/exception and normal runner cleanup: a bounded stop after
first-switch capture must not swallow failures or claim full upgrade success.
Inspect the generated default script to ensure no unconditional wrapping or
capture behavior leaks into normal cases. The baseline uses exact archived
846bb source plus only declared diagnostic fixture changes, with actual input
diff recorded; a version marker alone does not establish source equivalence.
The source copy belongs under the session-owned disposable `/tmp/.../support/`
root, not retained evidence. Confirm primary configured memory and every disk
from evaluated JSON: the source's explicit 4-GiB transferpeer setting does not
establish primary memory. An 8-GiB host reservation must not silently change the
guest. Budget every actual disk and all closure growth.

The lead accepted `activationTargetRevision` only for this opt-in first-switch
diagnostic and only at `846bb469505789ba0b2a405fa5905ba6d8253006`. The archived
support snapshot lacks flake `self.rev`; its packaging revision marker alone
does not preserve the system target's derivation. Load the exact baseline flake
for the activation system/input graph while keeping diagnostic scripts in the
immutable support snapshot and the predecessor unchanged. Strip diagnostic
arguments before predecessor fixture construction, reject this override outside
the diagnostic, and keep all ordinary targets local. Prove evaluated target
derivation/store identity against original receipts; matching the revision
string is insufficient. This is not a general target-selection API.

Subsequent graph comparison could not recover the incident target/gem recipes.
The lead accepted the explicit old-writer-state experiment described in
[identity-comparison.md](repair/support/identity-comparison.md): the two
reproducible graphs share the exact target osctld recipe, source/lock inputs and
boot tuple; their differences are accounted version metadata and diagnostic
JSON. Neither establishes equality to the unavailable incident target. Capture
the unchanged predecessor's saved YAML/GC and live root, then the declared new
target's first import. Do not claim incident-exact binaries/images, total causal
attribution or exclusion of generic-service effects. This bounded experiment
supersedes incident-target equivalence as its launch prerequisite; exact
selected-graph identity and resource checks still apply.

The existing stock `test-json-runner` is a possible native entry point for the
fixed prepared JSON, pending lead selection. Its internal resource reservation
is zero because it omits `Test.resources`; normal scheduler limits cannot prove
admission. A selected direct launch therefore needs explicit external admission
for the evaluated 8-GiB RAM/shared-memory requirement, QEMU/runner overhead,
4 CPUs and one VM, with available memory and tmpfs measured separately. Preserve
native Executor cleanup, use one attempt/job and destructive cleanup on newly
owned disposable state, and explicitly set the intended 900-second default
command timeout rather than inheriting the wrapper's 7200 seconds. Hash the
prepared JSON and retain its output closure and stock runner. This avoids a
mutable-source reevaluation; it does not change product/test transport.
Boot `/dev/hvc0` matches the stock host's default virtconsole. The selected
first switch relies on `onChange = "ignore"` preserving that live test shell;
a new target shell naming `org.osvm.shell0` is not certified for this VM.
Verify actual prepared services before launch, and treat missing or malformed
legacy-console output as incomplete evidence. No runner/resource framework
change is part of this diagnostic.

Implementer1 owns `tests/suite/upgrade/nested-podman-sandbox.nix` and
`tests/suite/upgrade/nested-podman-sandbox/capture.rb`; implementer3 registers it
under the same explicit diagnostic opt-in, without CI tagging or default
unfiltered-suite inclusion. Source transport/tooling changes and new guest-image
identity remain declared diagnostic differences from the original incident.

Implementer2 may add
`tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.{nix,c,bpf.c,h}` for the
narrow first-hotplug capture. Archived exact-vmlinux inspection may use a bounded
memory-backed extraction to avoid full SDK restore, but is still a scheduled
operation with its declared memory/disk/output caps. Probe/ABI validity and the
physical VM forecast remain gates before aging; no kernel patch is selected.

### First diagnostic sequence and resource contract

The shared filesystem currently has 108 GiB available (89% used). This is a
moving resource observation, not a reservation. One session-owned diagnostic VM
at a time; unrelated host VMs are not an exclusion or an ownership claim.
No new heavy operation when free space is below 40 GiB; reject plans whose
conservative incremental allocation plus retained outputs would cross that
floor. Lead schedules runs and a fresh watcher from the monitor skill.
Owners prepare exact commands first, with tested commit plus any diagnostic
diff/input identities; no implicit background launches.

Guard the session-owned VM boundary using this session's declared attempt roots,
retained native process/state identity and exact argv/cwd/root references. Match
canonical path components, not loose substrings or process names; retain PID
birth and process-group identity before signalling. A foreign QEMU is resource
context only and must never be cancelled, waited on or cleaned by this session.
Fresh aggregate available RAM, tmpfs, CPU affinity/capacity and physical disk
admission account for concurrent host consumers. Lead serialization and a literal
launch selection remain necessary because direct JSON reserves zero resources.
Ambiguous ownership of a process that references our own attempt requires
reconciliation; a clearly foreign VM does not block solely by existing.

Repeat canonical own-reference inspection at final, lost-parent and observer-error
boundaries, independently of sampled ancestry or current process-group membership.
Retain escaped/reparented process identities in the final result; an empty native
group does not prove all effects ended. Observer exclusions must match the exact
executable and a known read-only invocation; `find` is not generally read-only.
Remaining or ambiguous own references mean incomplete evidence and retained
watcher responsibility. The owner also reconciles managed disks, lock ownership,
sockets and handles before releasing the VM slot or removing disposable data.

The first-switch capture was selected and launched with guardian `b122d8d0...`
before its canonical-reference gap was reported. Keep that script and all live
inputs frozen. The lead supplied the missing final/lost-parent reference checks
to its watcher and requires owner3's native-state reconciliation after the result.
A separate source correction is preparation only and does not select a retry.
Its output threshold is sampled, so report actual peak/overshoot rather than
claiming a hard 64-MiB filesystem quota.

For the first-switch guardian, request cancellation with SIGINT only against the
exact owned native runner/process group, after checking its identity. Retain
native Executor/TestEvaluator cleanup. The 1800-second body deadline and resource
thresholds initiate cancellation; 120 seconds without completed cleanup is an
escalation threshold, not a claim of bounded total termination. Do not add an
automatic broad TERM/KILL or delete data merely because that time elapsed. Report
exact surviving owned process births/handles/state to lead and keep the watcher
responsible until native effects are reconciled. Continue output/growth/resource
guards while cleanup is incomplete; escalate immediately if the reserve is
threatened, rather than waiting out the grace period. Any later targeted native
termination must use proved ownership. Native cleanup may itself TERM/KILL its
owned guests; that is distinct from a guardian assuming all descendants died.
No root or disposable-data removal before verified completion of effects.

Podman's separately proposed cancellation contract retains its 900-second INT
and authenticated owned-group KILL within the following 120-second allowance.
That bounded escalation is compatible with its selected diagnostic scope; it
does not promise complete termination by 1020 seconds. Native cleanup can be
interrupted, and an escaped process can survive the group signal. Return an
incomplete result and retain watcher/owner reconciliation on either condition;
never signal a process solely because its path matches. The narrow Podman
canonical-reference/final-result correction is accepted at guardian
`b02087d33e9c74307050a06bb8f87f030b47a5cda525f66ad2c11cc5232c6195`,
with launcher `f255bdc5786cdd2c42c68686553b366bc201ae44011fc25e7ef9f340dc08295b`.
The focused inert checks prove that a successful native parent and empty group
still return incomplete with a detached own reference retained. Selection still
requires fresh admission and the lead's free session-owned VM slot. First-switch
keeps its distinct INT-only guardian contract above.

Every run brief must name the canonical worktree, exact native command and
state directory, source/input/kernel/image identities, expected **physical**
allocation including sparse-image growth and Nix derivations/copies, hard
trace/log limits, start/end `df` and physical `du`, deadline, reserve-floor
checks and owned native termination/cleanup. Baseline and peak/run-final size
must distinguish apparent capacity from allocated blocks. If space declines
toward the floor, stop owned growth through the declared runner path, preserve
compact evidence and reconcile all processes before cleanup. No global Nix GC,
foreign directory/image deletion or automatic background cleanup. Cleanup is
authorized only for proven session-owned disposable data after effects end;
preserve logs/hashes/identities needed for diagnosis and recovery.

Use session-owned state beneath
`/tmp/ci-failure-analysis-2026-10-22/<lane>/<attempt>/`, with an ownership record
in the lane's existing Markdown brief before creating it. Do not use the source
session's `/tmp/os-test-runner` state or inspect its running VM. All disposable
paths resolve under that new root or an explicitly recorded owned path; no
symlink escape, namespace-wide deletion, branch deletion or lifecycle action.
Retained compact evidence belongs in this session's existing lane directories.

Initial order, subject to exact prepared command and measured cache/storage:

1. **Impermanence, one first-switch capture:** reproduce only one supported
   `upgrade/from-6.12-guests` setup through its first switch using immutable old
   writer and selected target. Capture raw YAML/GC bytes, init birth/root and
   mount/ZFS identities, both markers and timed sysctl status/readbacks before
   and after. Stop before repeated switches/restarts. Target 30-minute outer
   runtime ceiling after preparation, at most 64 MiB retained diagnostic output;
   owner validates this bound against native command behavior and budgets disks
   before launch. This establishes whether the source-proven writer defect was
   realized and informs authenticated recovery. Unit writer work need not wait.
2. **Podman, one predecessor-only start:** reuse the existing scoped proposal,
   with a prepared hashed tracer and no APT/Podman/target activation. A first
   plain trace may answer call/errno without a complex recorder; explicitly
   retain effective-state gaps and trace sensitivity. One 60-second network
   capture, at most 32 MiB trace and 16 MiB other logs. Prepare instrumentation
   before starting the guest so no second unnoticed startup occurs. Owner
   supplies full VM/preparation deadline and physical disk forecast.
3. **AMD, feasibility first:** inspect existing exact artifacts/BTF/DWARF and
   prepare recorder syntax/build/probe validation with bounded outputs; no
   additional VM or kernel build during this step. Only after the lead accepts
   recorder, ABI and free-space preflight select one original 128-vCPU/16-GiB,
   four-hour-aged first-hotplug diagnostic: five-hour outer budget, 120-second
   capture, 128-MiB tracefs +64-MiB BPF buffers, 256-MiB total output cap, loss
   counters. Account for population guest memory, host sharing/backing storage
   and full kernel/SDK substitutions. Preserve all original workload semantics.

Unexpected local kernel builds stop under the verification procedure. A proven
need for an intentional diagnostic kernel must be explained and separately
budgeted to the lead before launch; kernel copies cannot silently consume the
reserve. Unavailable cache objects are a preparation blocker to report, not an
excuse for an unplanned build or broad GC.

### Verification, review, compatibility and completion

Quick native checks: focused osctld RSpec cases for writer/reload/recovery with
one-package/no-assignment/multi-package paths; race/GC/ambiguity failures; Ruby
and Nix parsing/formatting and actual repository Overcommit hooks. Use the
declared Nix environment. Implementer3 validates fixture scripts and completeness
of diagnostic fields without mirroring implementation in vacuous tests.
Known quick checks run inline; uncertain or long checks go through lead's fresh
watcher. Bounded diagnostic experiments establish causes; they are not final
integration acceptance and do not trigger premature final review.

After intended substantive fixes/tests/docs are committed and quick checks pass,
classify HIGH risk (persisted live state, GC, host/kernel and security boundaries).
Lead assigns retained reviewer0 with saved settings under mandatory-change-review:
general, architecture/repetition, scope/proportionality and risk/compatibility.
Review complete base-to-head history, exact final diffs and migration/state
lineage; fold speculative or superseded approaches and any repeated input
updates before review. No reviewer assignment yet.

The first reviewable increment can be the completed impermanence repair and
diagnostic instrumentation, once owner2's intended sources/tests/docs are
committed alongside the other completed owners and all applicable quick checks
pass. Unresolved DHCP and kernel causes remain investigation; they do not make a
completed diagnostic increment intrinsically incomplete, nor does its review
claim those causes fixed or the initiative finished. Do not omit known pending
correctness changes merely to close this boundary. Inventory the entire current
base-to-head series/final diff, logical owners and migration provenance (state
explicitly if none), including opt-in/default behavior and instrumentation
failure/cleanup contracts. Session recipes, guardians and receipts provide exact
operational context; any intended reusable shipping behavior belongs in the
committed scope before review. Use all four HIGH-risk lanes and the eligible
retained reviewer's saved settings after a fresh roster check. The lead alone
assigns review once that gate is met; none is assigned here. Subsequent substantive
fixes or instrumentation changes need the skill's relevant review treatment and
an updated exact final-head/history conclusion. Fixed-head integration, root/data
continuity and remaining causal investigation stay explicit outstanding work.

The lead's continuation reconciliation confirms that the ordinary acceptance
additions below remain selected. Its cleanup checkpoint did not cancel that
package; the temporary source hold is released. At head `87e6bd4a`, the remaining
substantive source packages are owner3's ordinary assertions and owner2's exact
recorder/qualification-health package. Owner0 supplies read-only field/ordering
support. Lead serializes Git windows and logical-owner folding after each
package's quick checks; no reviewer is assigned until both are committed and
the complete intended source/test/documentation scope is ready.

Owner2 must identify its exact shipping paths, required documentation and any
remaining source dependency separately from the active image-assembly watcher.
The current four recorder files and `qualification.rb` checkpoints are not
evidence that the still-held first-hotplug orchestration has been implemented
or admitted. That later wiring retains its probe-admission dependency; no aged
execution or speculative kernel fix joins this increment. Any required source
correction revealed before review belongs in the completed package. Final
review covers the full resulting branch, all four HIGH-risk lanes and explicit
runtime/causal gaps; it does not establish successful probe attachment, legacy
recovery continuity, DHCP repair or completion of the initiative.

Owner2's `repair/hotplug/commit-packet.md` resolves that boundary into two
independent units: cumulative health checkpoints in `qualification.rb`, and
the four standalone experimental `hotplug-recorder.{nix,c,bpf.c,h}` files.
All five inspected source hashes match the packet; the recorder sources match
the retained successful build2/CLI checks. No further recorder source work or
runtime prerequisite is needed merely to commit those unchanged units. Probe
attachment, verifier/count/loss admission and first-hotplug orchestration remain
explicitly unproven. The session probe fixture and operation scripts stay out
of product commits. Owner3 closes the small owning-project documentation gap in
`docs/os/testing.md`: distinguish early cumulative health from the standalone
exact-binary tool, explain its authenticated-header/build-ID/use gates and CLI
entry point, and retain ordinary qualification/recovery requirements. Lead folds
the appropriate documentation with each logical owner.

### Selected ordinary impermanence acceptance additions

Read-only validation preparation found two necessary gaps in the ordinary
guest-policy case: API boot-dataset equality alone does not establish the saved
run/GC/root repair, and the final target-created root was not imported again.
Before the committed-deliverable review, owner3 adds narrow assertions to the
existing scenario, with owner0 supplying the exact field/path contract. Keep
the historical first-switch diagnostic unchanged and introduce no new fixture,
target-selection option or generalized capture/recovery harness.

The source boundary is `guestPolicies && !firstSwitchCapture` in the existing
`common.nix` scenario. Sample after marker creation and before the first switch;
check persisted ownership/root identity inside `assert_retained` before its
resolver setter; sample the target writer immediately after the existing final
guest restart, then perform one existing native osctld reload before deletion.
No fixture/helper/API changes are selected.

The sampler reads each saved file through one held descriptor and compares
descriptor device/inode/size/mtime before and after the bounded read. Retain
ctime and separate pathname observations as diagnostics; an atomic rename can
unlink the old inode and change its ctime without changing its contents. The GC
worker can legitimately replace the file while retiring an unrelated old run.
Treat the descriptor as a coherent point-in-time snapshot, not proof that the
pathname stayed current afterward. Preserve strict selected-row ownership and
uniqueness assertions; an observed replacement does not excuse invalid sampled
semantics. A focused inert rename test covers this observation race without a
semantic, acquisition or VM retry.

For the existing impermanent guest, retain raw runtime YAML and the matching GC
row plus held-proc birth/root/mount-namespace and exact ZFS dataset/private-root
identity before the first switch. The designated immutable 3cc/from-6.12-guests
case must actually establish stale BASE/cleanup-false with valid saved run ID
and a unique matching temporary owner; a pre-corrected state cannot count as
legacy-repair coverage. Other predecessors must not be assumed stale without
evidence. After import and during the existing retained checks, require the
same run ID/GC owner/live root and payload, with saved dataset/cleanup matching
the temporary root. Use direct observations as the test oracle, not production
recovery calls or mutation of saved YAML. Scope identity assertions to the
impermanent guest and retain original scenario behavior for other guests.

Immediately after the existing final target-side guest restart returns, and
before resolver/config mutations can incidentally save state, require a new
run ID and temporary root with that selection already persisted and uniquely
owned. Retain fresh process/root and known marker identities, restart only
osctld once using the existing native restart sequence, then prove that same
new run/root/ownership and markers survive. Keep the existing persistent-data,
old-temporary-retirement and ephemeral-absence assertions and final native
stop/delete. Do not add another guest/VM or an unrelated restart matrix.

Custom `.boot-6hex` authentication remains unit-only for this increment. Owner0
has no authenticated cached archive, so no runtime addition, cache locator or
image fetch is selected. Retain that runtime gap and the focused ordinary
`ct boot --from-file` command/resource proposal in the existing repair brief for
separate post-review selection. Its intended proof remains saved complete boot
selection before daemon reload, unchanged run/GC/root/payload across reload,
then native temporary-root retirement and normal persistent-data preservation.
Owner3 owns common fixture edits; owner0 stays read-only. Lead
serializes commits and settles logical-owner folding before whole-branch review.
No runtime/evaluation/build or review assignment is selected by these additions.

Owner3's source package now implements these assertions in 216 inserted lines
and five ordinary-only gates. The inspected `common.nix` SHA256 is
`6ea3341b5cdebb5e7eae04d0b1e2b6d841dc00dc3bfc4494823fde54f5d9811f`;
the 20-line hotplug documentation addition in `docs/os/testing.md` has SHA256
`aba106bdb05a1e0995146e780c75dbb56eadc2e369cda9764773ebb4b129a185`.
Both match the retained `repair/support/ordinary-acceptance-checks.json` receipt.
Its 29 focused actual-source checks cover retained stale capture fields,
rejection cases and a controlled atomic GC rename; Nix parse/format and the five
added Ruby blocks pass. Source inspection confirms the selected gates/order,
held-descriptor snapshot limits and immediate persistence-before-setter check.
This is architect design acceptance for the lead's serialized Git/folding step,
with normal hooks still required. It is not final independent review, evaluated
configuration equivalence or runtime continuity evidence.

After review, run focused full integration: all five impermanence variants with
payload/root/process continuity, repeated activation and daemon/container
restart/GC; supported confined DHCP plus full nested Podman continuity; original
AMD qualification including both hotplugs, A/B migration, activation/disable,
unload and final health, if its owning fix is within supported exact lineage.
Schedule serial resource use and preserve exact checked heads/input graphs.
A diagnostic pass or a new-image pass does not certify original-image repair.
No blanket CI rerun, assertion weakening or configuration repin substitutes for
the missing causal or compatibility evidence.

New writer state must remain old-reader compatible; old live-state repair must
preserve rollback-readable bytes and correct run/GC ownership. Kernel/security
fixes need explicit supported old/new combinations and rollout/rollback design,
without claiming a deployment was performed. No fleet-wide update requirement
is presently selected; state one explicitly if a later proven fix needs it.
Feature publication is authorized; default-branch integration remains separate.
Finish with published, reviewed, verified fixes or clearly stated unresolved
boundaries, compact evidence and owned disposable data removed after native
shutdown. Leave plan/state/portal and commits with their lead/assigned owners;
leave the session open.

### Capture1 acceptance and reader implementation release

The lead accepts [capture1](repair/support/capture-1/receipt.json) as sufficient
to release implementer0's existing narrow reader, import wiring and retained
identity installer. No equivalent baseline rerun is required for implementation.
The retained after-start and before-switch captures have verified raw hashes:
the saved runtime YAML selects `tank/ct/niximpermanent` with cleanup false,
while its valid saved run ID `1792700667.9359279` has one GC record owning
`tank/ct/niximpermanent.impermanence-4014fb`. The YAML and GC bytes/file identities
are unchanged between those captures. The predecessor API reports that temporary
dataset and a running container despite the stale saved selection.

PID 6498/birth 60064 and mount namespace 4026532949 are stable in both captures.
The unique guest `/` mount is ZFS source `tank/ct/niximpermanent.impermanence-4014fb`,
device `0:99`, with root `/private`. Held guest-root device/inode `99:2` matches
the temporary dataset's host `private` directory; its dataset mountpoint is
`99:34`, and base `private` is `97:128`. Temporary GUID is
`5076182134290402100`. Compare the private root, not the dataset mountpoint.
Idmapping explains the different host/guest uid/gid views; do not add equality
of those values as an identity prerequisite. Both marker contents are captured
before the switch. These facts establish the supported old-writer stale-base
state and required root layout in this declared packaging experiment.

The after-pool-import helper produced a `nil.bytesize` exception instead of
valid capture JSON. This run proves neither post-switch root/data continuity nor
target API behavior, successful recovery or exclusion of other contributions.
Keep that limitation separate from the now-satisfied implementation gate. The
new reader must authenticate the state actually presented at import; missing,
empty, changed or contradictory saved evidence follows safe refusal and pool-GC
inhibition, never a fallback inferred from this captured example.

Implementer0 may now implement the existing contract in its assigned source/spec
paths, using this raw case for meaningful regressions: valid saved ID plus unique
existing GC ownership, authenticated held process/private root, final unchanged
file/GC and identity checks, atomic same-ID repair of only dataset/cleanup fields,
and retained identity installation without reopening the PID. Add the bounded
pool import failure trigger to the already-checked common retirement guard before
GC starts. Preserve every ownership record on refusal, including foreign aliases;
successful fresh import reauthenticates and recomputes normal collection.

Focused checks must cover the actual valid stale case, already-correct and stopped
paths, absent/empty/malformed/conflicting evidence, process/namespace/root/file/GC
changes, installer lifetime and retirement races, real queued/free/prune refusal,
failed reimport and successful fresh import. No new schema, public API, generic
recovery framework or speculative extra helper is selected. Documentation stays
with implementer3; Git windows and long checks remain lead-owned. Commit only the
complete logical impermanence repair with passed quick checks; do not ship the
GC primitive unused. Full fixed-head upgrade/continuity verification still follows
committed-deliverable independent review.

### Affected import publication ordering

The lead accepts a bounded ordering refinement for authenticated running guests
in this reader path. Current `fresh_state` and `Monitor::Master.monitor` can
reopen a numeric init PID before DB publication; the latter can refresh state
synchronously or asynchronously. Run the narrow reader before that fallback.
After preliminary validation, a private preparation block may generate LXC home,
log and configuration from the validated in-memory selection. It does not save
repaired runtime YAML early. After the block, install the retained duplicate
before the final probes, because installation can wait for existing leases.
Then complete final file/GC/ZFS/process validation, authenticate the held process,
save the same-ID repair and publish before monitor/console registration. No
lease wait or numeric PID reopen belongs between final authentication and this
ownership transfer; close an installed duplicate on unpublished failure.

Use the existing per-container manipulation exclusion through publication and
monitor/console registration. Stop commands can find a DB entry while its pool
is importing; pool activity alone does not exclude that command interval. Do not
hold run/GC state locks across preparation or registration. Ordinary monitor
updates after authenticated publication retain their normal lifecycle role.
Keep unrelated and stopped import ordering unchanged.

Before-publication failure, including DB host-link validation refusal, leaves
the container unmanaged and inhibits pool retirement. After-publication monitor
or console failure preserves the authenticated same-run DB and GC ownership,
inhibits retirement and visibly reports incomplete attachment. Do not blindly
remove that DB entry or perform destructive rollback: host-link ownership may
prohibit removal, and publication already made the object visible. Retain
descriptor ownership correctly on each failure path. Focused tests must cover
both failure phases, stop-command exclusion, sync/async monitor registration and
ordinary positive controls. Add a concise source comment explaining this order;
no general transaction framework or additional public interface is selected.

`DB::List#add` inserts before reporting its event, so an exception from `add`
does not by itself prove publication failed. Reconcile exact object identity
through the existing container DB lookup inside the narrow publication callback.
If that same object is present, complete reader ownership transfer, retain the
event error and report attachment failure afterward; do not unwind through the
reader's unpublished-identity cleanup. A pre-insertion host-link refusal remains
unpublished. Tests must exercise both outcomes and prove that the real reader's
installed identity survives the post-insertion error while its standalone probe
identity is closed; a pool test that stubs recovery cannot alone prove that
descriptor boundary. This is the existing failure-phase contract, not a new DB
transaction or retry mechanism.

A complete saved custom-boot selection `<base>.boot-<six hex>`, with cleanup
true and exact same-ID unique GC ownership/private-root authentication, remains
unchanged and is not rewritten. Apply the same no-write rule to a correct saved
impermanence selection. Only a stale base selection may infer the existing
impermanence candidate; arbitrary saved datasets do not become a recovery path.

### Podman observer correction after capture1

The first Podman diagnostic returned a complete framed status 124 from its short
CT-exec/systemctl poll; no byte-transport loss was observed. The uncaught observer
timeout skipped trace retrieval, then ordinary native cleanup destroyed the
guest disk, including its `/run` trace and fetched image archive. There is no
captured failed prctl or product repair result from this execution.

Implementer1 owns the smallest fixture correction in its existing Ruby/Nix paths.
Write entry/trace files under the disposable CT's persistent
`/var/log/podman-sandbox`, keeping the same output limits. Remove the repeated
short systemctl poll from the critical path; retain one monotonic 60-second
observation window from the single CT start. Optional bounded snapshots are
evidence fields, not prerequisites to retrieving the trace. Record timeout,
nonzero, empty and truncated fields explicitly; preserve the first actual
observer exception for re-raising after collection and cleanup.

In ensure, attempt bounded stop of this exact CT, then retrieve through its
previously recorded host private-root path before VM shutdown, even if stop or
optional observation failed. Do not require CT exec or systemctl for retrieval.
Record CT pool/id, dataset/root path and dataset identity before startup; verify
the same root at collection. Keep it mounted or use only the native mount of
that same confirmed stopped CT when needed, never another start, recreation or
deletion. Do not resolve a new root by prefix or follow guest output symlinks
outside that root. If identity/mount status cannot be established, record a
collection error instead of guessing. Trace collected while writers may remain
active or after a failed stop is explicitly partial.

Separate stop, retrieval and VM-shutdown attempts so an earlier failure cannot
skip the later stages. Preserve the original exception while retaining all
collection/cleanup errors; a successful retrieval cannot convert observer failure
to success. Use a focused no-VM fault test proving one start, retrieval before
shutdown on observer/stop failure, and primary-error preservation. No generalized
capture framework, sandbox change, APT, target activation or runtime rerun is
selected. The next image is a new sample unless its exact previous archive hash
and provenance are recovered; new JSON/attempt/cache/resource selection remains
with the lead.

The host-side copy may use the narrow sibling `nested-podman-sandbox/retain.rb`
helper within implementer1's assigned directory. Pin the authenticated dataset
mount and private-root descriptors, then walk the fixed `var/log/podman-sandbox`
components and regular entry/trace files with no symlink following. Recheck the
same CT/dataset GUID/private-root identity and reject a changed device; path
canonicalization followed by a separate read is not sufficient while guest
writers can change paths. Bound each copy independently and retain partial-file
and original-observer-error qualifications. Record the helper's exact Ruby input
in the next native closure/cache preparation. This is one fixture's collection
helper, not a general capture API or permission to launch a second attempt.

If stop fails and the subsequent bounded CT-status read also times out, record
that secondary error and still permit read-only collection from the previously
recorded, already-mounted root when its ZFS GUID, mountpoint and private-root
device/inode remain authenticated. Unknown CT status forbids remounting or
starting it; a contradictory identity refuses collection. Mark such output as
partial with active writers unknown. The focused fault check covers this case
without losing the original observer exception or skipping VM shutdown.

The completed four-file correction satisfies this diagnostic source contract
on inspection. The retained [focused check receipt](repair/podman/observer-correction-2-checks.txt)
records 16 passing examples, syntax/lint/format/parse checks and exact file/tool
hashes. This accepts the source for next-attempt preparation, not runtime
attribution or independent final review. The next native input/cache plan must
include the exact Ruby/helper closure, shared-directory transfer command
timeouts, duplicate trace allocation and the complete ensure/cleanup envelope.
Use a new immutable JSON and attempt; no launch follows automatically.

Attempt-2 metadata script `eb676abe76629a8117015d49ca15ae7d105916accf2b1e8fdcf68f01c44f79ed`
fits that preparation scope: exact source guards, native JSON/script comparison,
Ruby/helper recipe and local-closure checks, and dry-run only. Its 4-GiB physical,
256-MiB scratch and 16-MiB metadata budget preserve the shared reserve. The lead
selected this operation with those disk/output limits and the 330+10-second
outer deadline, without a separate 2-GiB RAM/two-CPU host cap. Do not claim such
a cap or infer it from the later guest's 2-GiB/two-CPU configuration. No material
host-memory concern has been demonstrated. The fresh watcher owns the selected
run; this clarification adds no live change or duplicate observation. No small
file-size limit is inherited by Nix.

Native transfer and cleanup allowances total up to 525 seconds before additional
host I/O/Executor cleanup; `machine.stop(timeout: 45)` does not shorten its
preceding poweroff command. Four coexisting trace copies can occupy 128 MiB.
The existing 900-second guardian plus 120-second cancellation interval can
therefore interrupt collection or cleanup. Treat that as incomplete evidence and
retain effect reconciliation; the next concrete VM package must reconcile its
body, collection and cancellation budgets. Metadata selection does not change
those runtime bounds or certify that cleanup will complete within them.

For attempt 2, architect acceptance of the timing proposal is a 1500-second
native operation deadline, followed by the existing authenticated INT and at
most 120-second escalation/reconciliation interval. The fixture's 900-second
Ruby timeout encloses its body but not the outer ensure. The proposal therefore
allows that body plus the exposed 525-second collection/shutdown allowances
and 75 seconds of slack. Startup, host I/O, native cleanup and kernel-failure
draining are not thereby proven bounded; 1620 seconds is the operation envelope,
not proof that effects end. The lead must select the new immutable launcher and
guardian before execution. Resource breaches still interrupt immediately and
start their own earlier 120-second interval; do not defer them to 1500 seconds.
Keep the command timeout, source/JSON, one-start/60-second observation, full
remaining 24-GiB forecast and fresh 64-GiB admission unchanged. Reconcile exact
owned references, disks, locks and sockets even after parent exit; uncertainty
returns incomplete and retains watcher responsibility. The extra time does not
authorize a new sample claim, automatic retry or second VM.

The frozen VM2 package matches that design on inspection: launcher
`a72f60a2c578119e9b644d288aaaca7fe9b5c37b0bf75e02f77956d4102d1b92`
and guardian
`ca72c0df750c1272bcdee2a21ce73664825d2f9bbded014915734338a8901ba6`.
It consumes fixed `x5vs...` JSON SHA256 `615f76ad...` and the existing shared
runner, with no Nix invocation. The retained fake-process checks exercise
native KILL at 1615/final observation at 1620, resource INT immediately plus
115/120 seconds, and incomplete detached-reference handling. They do not prove
live cleanup. Native byte/root/resource checks and final owner reconciliation
remain required. The lead may select this exact package; no launch is implied
by architect acceptance.

The selected VM2 capture completed with native exit 0 in 325.404 seconds and
no guardian breach. Retained capture-2 bytes show eight complete same-PID
`PR_SET_NO_NEW_PRIVS = 0` / 140-instruction filter-install `= 0` pairs, plus a
DHCP address/default route. No failing NNP/filter call is captured. The archive
and dhcpcd hashes match VM1's diagnostic sample, not a recovered original
incident image. The 106496-byte trace ends mid-line without ifup's exit; the
instrumented oneshot later times out at 60 seconds with broken-pipe messages.
Copy flags certify bounded nonempty retained bytes, not trace/lifecycle
completeness. These observations justify no kernel/LXC/security exception or
claim that the original cause is absent. Owner1's final cause-first findings are
in `repair/podman/capture-2/findings.md`. Exact applicable fbda guard sources map
non-VALID transition results to rejection, but no such rejection was captured.
The absence of an explicit ptrace condition in the examined entry paths proves
neither broader ptrace neutrality nor an incident cause. A future syscall/guard
observation requires exact probe feasibility and retained selected-image bytes
before separate selection; no blind retry or security exception follows. Owner3
supplies independent final effects proof for lead acceptance; no duplicate scan,
cleanup or VM slot release is inferred from successful capture.

The completed metadata result identifies exact `w9ik...` JSON derivation and
`x5vs...` output, with SHA256
`615f76adca40be39b5de225e514a726c04bb2c7401b5fd4443c9523fead72af2`.
The missing plan contains nine assembly/check/helper/image recipes and two
small substitutes; kernel, LXC, Ruby and tracer remain existing outputs. The
prepared `run-preparation-2.sh` at SHA256
`65b6450c5781daa333bccba8f83c2457c383dc6b3917fa1274679c37e24803ca`
fits separate lead selection: verify and root those runtime outputs, allow only
the captured plan, substitute with no builders, then realize the immutable JSON
with one job/two build cores. It does not reevaluate source or launch a VM.

Budget preparation separately at 10 GiB new planned store allocation plus
2 GiB scratch, 16 MiB logs, 1200 seconds of native stages and a 1250+10-second
outer limit, admitting at least 52 GiB free above the 40-GiB reserve. Actual
closure, physical image size and byte identities remain required results before
the next VM proposal. A native root-enumeration query unexpectedly removed
already-stale foreign auto-links during owner reconciliation; that side effect
is disclosed and the query must not be repeated as an observation or cleanup
shortcut. Use exact owned root paths and preserve unrelated state.

The four accepted Podman fixture/helper/spec files are committed as
`405a802857093176883e0f173589b433756a9647`, directly after the legacy-reader
commit. Architect inspection confirms the exact path set and matching accepted
working-tree bytes. The owner's isolated commit receipt records normal hooks,
16 passing examples, an empty shared index and preserved peer bytes/modes; its
Git window is released. This is a diagnostic implementation milestone, not a
DHCP cause/fix or runtime result. Preparation and final review retain their
separate gates.

### AMD admission missing-output preparation

The actual admission metadata selected 46 local derivations, including kernel,
ZFS and an old Nix source build. No realization was performed. Two dependencies
explain this: the frozen package's missing output selects its archive-restoration
recipe and retained old build tools; its reexported original `kernel.configfile`
is referenced by security-evidence JSON, and that missing configuration output
selects the historical config generator, built-in ZFS and plain kernel dev.
These are missing-output preparation paths, not evidence that the recorder needs
a new kernel or ABI.

The lead accepts a bounded output-only operation for the exact frozen `050...`
output and `np082gl8insab5lisjdhqlh4128jlm9m-linux-config-6.12.95`, with closure
availability/physical forecast first, `max-jobs=0`, empty builders and fallback
disabled. Root only accepted outputs and refresh the existing fixture's missing
closure plan once. Do not realize either recipe or permit kernel, ZFS, SDK
restoration tooling or Nix source compilation. Implementer2 supplies the runnable
script/hash and exact resource plan; the lead selects its fresh watcher.

An unavailable configuration output requires a separately assessed diagnostic
metadata proposal using the authenticated actual frozen configuration from its
archive or embedded configuration, preserving image/build ID/v6/ABI/topology.
An unavailable frozen output requires separately budgeted minimal artifact
restoration. Neither failure authorizes generic module suppression, guessed or
empty security evidence, production input changes or an automatic build fallback.

The exact output-only attempt stopped before substitution: all three remote
queries obtained no valid frozen-output closure, without a recorded network or
CLI-option error. The configuration query was not reached, so its cache status
is unknown. Architect acceptance covers the proposed archive-only inventory
`repair/hotplug/inspect-boot-inputs.py` at SHA256
`704ced365e9776ed99e914f29893331ceff7feff22f7878ced5e2425f253fda3`
for lead selection. It verifies the complete original out NAR and bzImage,
measures entries/content/symlink targets, and retains actual root-config
candidates. Only absence of a candidate selects a full hash scan of the dev NAR,
retaining configuration alone. No SDK/vmlinux copy, store restoration or build
is selected. Its cached-tool command is bounded to 300+5 seconds, 512 MiB
process-tree RAM/no swap, 32 MiB helper files, 64 MiB combined output and
96 MiB physical growth with the 40-GiB reserve. Rounded block estimates inform
the next budget; they do not establish actual restored allocation.

Use the resulting authenticated bytes and references to propose the smallest
native out-only diagnostic restoration. Declare its changed store packaging
identity while preserving exact image/modules/build ID/v6/ABI/topology. Multiple
config candidates need explicit selection; unresolved references must not be
silently removed or pull in the historical SDK/toolchain. Lead selection and
actual closure/cache/physical checks remain separate from this inventory.

The completed inventory authenticated both NARs and the bzImage, then exited 1
because its selector considered only root-level config names. The DEV manifest
contains one regular `lib/modules/6.12.95/build/.config`, exactly 226335 bytes.
The OUT inventory has 5788 nodes, no symlinks, 115172528 NAR bytes and a
147918848-byte rounded allocation estimate. DEV was scanned, not restored.
Accept a DEV-only extraction of that exact member after full original-NAR hash,
type, uniqueness and size validation, retaining its content hash and provenance.
This closes the known selector gap without repeating the OUT scan, guessing a
configuration or restoring an SDK. Owner2 prepares the exact bounded command
for lead scheduling and the cached-tool OUT-only native recipe; postrestore
references must also account for embedded store strings, not just symlinks.

The lead selected the combined extraction and no-build metadata package
`run-boot-restore-metadata-1.sh` (SHA256
`3e8fed075f0c998727dd29fd6a1a214da671297288999d57dce36cb997a05046`),
with the exact-member extractor and `probe-boot.nix`. Its 1-GiB/no-swap process
budget covers native Nix evaluation after extraction; the deadline remains
300+5 seconds, physical growth is capped at 1 GiB and the shared reserve at
40 GiB. It creates only the declared configuration/derivation metadata and root,
not a restored output or VM. The future restore recipe checks full restored-NAR
equality and bzImage hash, with `allowedReferences = []`; any discovered store
reference refuses rather than being stripped or pulling historical SDK inputs.
Execution and observation belong solely to the lead's fresh watcher. Exact
resulting output/config identities, dry-run graph and physical/reference budget
still gate selection of the separate restore operation.

That combined attempt authenticated the selected configuration but exited 153
when an inherited 8-MiB `RLIMIT_FSIZE` killed `nix-instantiate`. This is a
process-limit failure, not a recipe/cache or frozen-ABI result. Preserve and reuse
the authenticated configuration in a distinct metadata-only attempt after the
owner reconciles any core file, partial root and client/store effects. Do not
repeat archive extraction. Bound captured log streams and measured owned growth
without inheriting the log-sized file limit into Nix; retain the accepted
memory, deadline and shared-space limits. The corrected command/hash still goes
to the lead for selection, with no automatic realization or VM execution.

Owner reconciliation preserves the valid `3lflyzssby6f211ki1fg4890shwy0r5q`
boot derivation/root; its declared `caql6sk0mnbbrfp6cdfksas7hs903xf6` output is
absent. The evaluated `wqwahjqndks2l13xjgm7dvb2n4igfv70` configuration path is
also absent: evaluation did not realize it. The extracted 226335-byte config
remains authenticated at SHA256
`c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969`.
Metadata-2 script `3a8087dcef7cd8c2907200451d82f085099def3f867e539dca8b6cd0b885e10d`
is accepted for lead selection: it reuses that file, refuses finite inherited
file limits, disables core dumps, caps receipt streams with native exit-status
checks and requires the unchanged boot derivation under a distinct root. No
archive scan, output realization or automatic old-root removal is included.

The next prepared operation is the actual OUT-only restore, separately accepted
for lead selection as `run-boot-restore-1.sh` at SHA256
`61a9cecefae1832e32db57635da710aafb3308d85a60a8c448c318b2093290c3`.
It realizes only the immutable `3lf...` derivation into `caql...`, after a fresh
restricted plan and native roots for the declared stdenv/Bash inputs. The
second plan must need no fetch and only that restore. Full restored-NAR/image
equality, empty native references and single-path closure are acceptance gates;
no reference stripping, SDK or source kernel build is permitted.

Its bound is 544 MiB physical growth, 64 MiB logs, 300+5 seconds and the 40-GiB
reserve. The 1-GiB client scope is separate from the declared 2-GiB aggregate
owned-client/builder budget, which the selected watcher must observe externally
because daemon builders can be outside that scope. Native client cancellation
does not prove builder effects ended. Keep roots and secure owned scratch until
reconciliation; retain the boot output root for its planned consumer. This
acceptance does not select fixture wiring, image realization, VM, BPF or aging.

Restore-1 failed before recipe execution because the daemon builder could not
access the custom private scratch directory. Owner reconciliation reports no
remaining exact client/builder references, absent `caql...`, empty scratch and
retained receipts. The lead directs use of the native daemon build directory;
do not weaken private-directory permissions or native security checks.
Restore-2 script `43911b480de8b883363c0858c5276a2c3a5b4e64aec9dad77b5a7e95d44afed0`
implements only that correction and reuse of the validated retained input roots.
It requires a no-fetch, sole-restore plan and preserves recipe, NAR/image/ref
guards and budgets. Architect acceptance is for the lead's distinct retry
selection, with no ABI change or duplicate execution.

Restore-2 completed with native exit 0 in four seconds. The retained watcher
`item_4` completion and native receipts establish that result despite conflicting
watcher final prose. The output occupies 127807488 physical bytes, has the
original 115172528-byte NAR and exact original bzImage hash, and has no native
store references and a single-output closure. Owner2 records the scope inactive
and no remaining exact client/build-user process references at 21:55:41 UTC.
Keep the output root for its diagnostic consumer; no new restore is needed.

Architect acceptance covers the standalone `repair/hotplug/probe-admission.nix`
wiring for the next lead-selected metadata operation. Reuse the exact 846bb
boot-base package shape and replace only its `outPath`/`modules` with authenticated
`caql...`, its `configfile` with the authenticated 226335-byte configuration,
and its `override` closure with that same diagnostic shape. A higher-priority
kernel-package definition remains local to this fixture. Preserve original
dev/ABI metadata, the full image/build-ID/v6 guards and 128-CPU/16-GiB topology;
no common module, product pin or ordinary qualification behavior changes.
The config store path remains prospective until actual native preparation
proves it. Metadata must establish the resulting JSON and exact dependency/cache
plan, including zero disks and unchanged transport, and refuse any unexpected
SDK restoration or kernel/ZFS/Nix/compiler source build. This accepts bounded
fixture preparation, not image realization, VM/BPF execution, aging or a
qualification result.

The frozen next metadata command is `run-probe-metadata-2.sh`, SHA256
`18d4b5d5258841b08542ad1622d1cb967ac582f787815a77c9ef0ecf3f3b0f74`.
Source inspection confirms guarded native instantiation/JSON extraction and
dry-run only, under a distinct attempt/root, unlimited inherited file-size
limit, 1-GiB/no-swap process budget, 1-GiB physical growth, 64-MiB captured
streams, 300+5 seconds and the 40-GiB reserve. Actual native JSON must match the
accepted topology, disks, transport and boot/config identities. An exit-zero
metadata operation can still reveal an unacceptable missing-output build plan;
lead assessment of that retained plan remains necessary before any realization.
No independent execution or duplicate observation is selected by this acceptance.

Metadata-2 completed with native exit 0 (wrapper elapsed 17 seconds). Its JSON
SHA256 is `daafd11dde916f90772276902b2b1acd7a73e99451e109442a88d4bfb147256a`:
exact `caql...` boot, authenticated config, 128 CPUs, 16 GiB RAM, no disks and
two virtserialport shells. The remaining plan contains 35 assembly derivations
and seven substitutions, 2.3 MiB unpacked. Owner2 inspected all selected recipe
sources; retained examples confirm the named ZFS output is an empty directory,
the predecessor module is exact-byte decompression, and the image streams the
native closure into sqfstar. No kernel, ZFS, Nix or SDK source build is selected.

Architect acceptance covers preparation of one staged native assembly driver
for lead selection. Realize only the exact initrd and guest closure-info first,
then measure actual closure NAR/physical bytes and accumulated owned growth.
Before squashfs/JSON, require an explicit conservative remaining-allocation
calculation, including possible temporary/output coexistence, registration and
receipts. Both stages share the original 4-GiB physical budget; the second stage
does not reset it. Require measured growth plus remaining forecast to fit that
budget and fresh free space minus remaining forecast to preserve 40 GiB. Refuse
before compression when either predicate or exact plan/root validation fails;
retain completed native roots and receipts for reconciliation.

The selected sqfstar invocation uses `-mem 2048M` and autodetected CPU parallelism.
One Nix build job does not constrain its threads, and Nix `cores=2` is not a
two-CPU enforcement mechanism here. Disclose full host CPU use to the lead for
scheduling. The proposed 4-GiB aggregate owned-client/builder RAM budget is
separate from physical disk growth and must cover daemon builders outside a
client scope; do not call the compressor cache or client scope an aggregate
hard cap. The frozen driver must declare deadline, sampled enforcement and
cancellation/effects ownership before selection. No source/configuration change,
VM, BPF or aging is included.

### Impermanence implementation design acceptance

The three source and three spec paths conform to the accepted reader/import/GC
contract on inspection. Retained proc-status reads require the host PID and
namespace PID 1 at both birth checks. GC uniqueness rejects exact aliases and
ancestor/descendant owners that could retire the live root. These are checks of
the existing identity and ownership invariant, with no new supported format.

The real reader plus pool publication test proves that an event exception after
DB insertion keeps the installed identity and same-run metadata while closing
the standalone probe identity. Focused lease/retirement tests and real queue
consumption tests cover unpublished refusal, explicit free, periodic/manual
pruning, fresh-import recovery and ordinary collection. The retained final quick
log records 177 examples with zero failures and six lint-clean files. This is
architect design acceptance for the lead's isolated commit window after owning
project docs, not independent final review or a runtime recovery result.
Keep the writer repair and legacy-reader safety as coherent logical units; fold
the GC primitive into its consumer. Actual post-import root/data continuity is
still a required fixed-head verification after final committed-deliverable review.

The accepted legacy reader and GC safety unit is committed as
`c2c5a006b49730d8b72d103ff063a1e89bba1ee2`, directly after writer
`274e826dae6d5b7230857174a25afa1f91ab4ffb`. Its eight paths contain the
three source files, corresponding specs, and owning datasets/updates docs;
inspection confirms those working-tree bytes match the commit. The owner reports
ordinary hooks passed and has released its Git window. This implementation
milestone does not establish publication, integration, independent final review
or runtime recovery success.

### Selected minimal userspace upgrade-test cleanup and retirement policy

The user selected implementation of the agreed cleanup after the read-only
assessment reported as `6170cdf8-2da4-4d3a-97f8-29e5b041730a`. Implementer3 is
the sole application writer. Scope is the current session's vpsadminos worktree;
this section records the decision without reopening prerequisite, resolver,
helper, source-restoration or historical-matrix work. The supplied configured
production baseline is vpsadminos `2abbe3cc` at configuration `50d263d`; this is
not evidence of live inventory or retirement of all old persisted state.

Delete exactly the following 33 files under `tests/suite/upgrade` (the complete
current directory contents except `production-impermanence.nix`):

- Eight historical 6.12 wrappers: `from-6.12.nix`, `from-6.12-guests.nix`,
  `from-6.12-guests-v1.nix`, `from-6.12-inherited-guests.nix`,
  `from-6.12-management-ops.nix`, `from-6.12-v1.nix`,
  `from-6.12-via-6.18.nix`, `from-6.12-via-6.18-v1.nix`.
- Fifteen historical 6.18 wrappers: `from-6.18.nix`,
  `from-6.18-consumers.nix`, `from-6.18-consumers-v1.nix`,
  `from-6.18-frozen.nix`, `from-6.18-guests.nix`, `from-6.18-guests-v1.nix`,
  `from-6.18-map-pools.nix`, `from-6.18-mapping.nix`,
  `from-6.18-nested-docker.nix`, `from-6.18-nested-incus.nix`,
  `from-6.18-nested-podman.nix`, `from-6.18-netif.nix`,
  `from-6.18-networkd.nix`, `from-6.18-pre-mount.nix`, `from-6.18-v1.nix`.
- Two diagnostics: `from-6.12-guests-first-switch.nix` and
  `nested-podman-sandbox.nix`.
- Eight exclusive support files: `common.nix`, `resource-probe.c`,
  `sysinfo-probe.c`, `wall-receiver.c`, `impermanence_first_switch.rb`,
  `nested-podman-sandbox/capture.rb`, `nested-podman-sandbox/retain.rb`,
  `nested-podman-sandbox/capture_spec.rb`. Do not repair the retired diagnostics.

Remove the complete 23-case historical and two-case diagnostic append blocks
from `tests/all-tests.nix`, including the
`VPSADMINOS_ENABLE_HISTORICAL_UPGRADE_TESTS` and
`VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS` gates. Rename the retained file/template
to `impermanence-from-2abbe3cc1c10.nix` /
`upgrade/impermanence-from-2abbe3cc1c10`, preserving `@v1` and `@v2`. Align its
test-name metadata and add the policy header, but preserve the entire
`testScript`, assertions, full baseline
`2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`, locked production framework/inputs,
stable checkout target, cgroup instances, `upgrade`/`ci` tags and one attempt.
No compatibility alias or replacement matrix is needed.

In `docs/os/testing.md`, retain the focused impermanence explanation with the
new names, remove historical/diagnostic instructions and replace the obsolete
adding/retiring guidance with this small project-local contract. Add a short
Testing Guidelines pointer in repository `AGENTS.md` requiring that policy
before adding, changing or retiring a userspace upgrade test. Top-level test
names use `upgrade/<behavior>-from-<12charSHA>` plus ordinary instance suffixes;
kernel names apply only when the kernel is the actual transition identity.
Each top-level test/template has structured comment labels **Baseline**,
**Purpose**, **Target**, **Removal condition**, **Retirement evidence**. Record
the full immutable baseline(s), explicit target profile (normally checkout),
specific supported transition/data boundary, concrete removal condition and
confirmation references, or explicitly state that retirement evidence is not
established. Never silently repin a case. No checker, registry or automatic
deletion mechanism is introduced.

The retained impermanence transition may be removed ONLY when support for the
equivalent old impermanent saved/running-state boundary explicitly ends,
including supported rollback/restoration paths, OR verified replacement real
transition coverage preserves its old-writer repair, live run/root/payload
continuity, reload stability, new-writer persistence and ordinary cleanup
guarantees. Evidence must identify the support/migration decision or the exact
replacement and successful native results. It is **not established now**.
A fixed userspace rollout alone does not discharge inherited state. Focused
writer/import/refusal/race/GC unit regressions remain lasting behavior coverage
while their behavior is supported; they alone do not replace the real transition.
Retirement removes exclusive helpers/specs, registration and obsolete docs
together. Elapsed age, flaky failures and missing caches are not grounds.

Preserve ordinary current-kernel and cgroup coverage, all livepatch selectors,
shared test infrastructure, persistence fixtures/checks, flake inputs/locks and
all implementation/unit-test code. The retired support has no shared consumer
outside its registrations/docs; the retained test is independent of it.
There is no runtime format, API, deployment-order or recovery behavior change.

Acceptance is the exact deletion/rename/edit boundary, static equality of the
retained test body and behavioral configuration, absence of dangling references,
and scoped syntax/formatting plus ordinary required hooks. No historical VM is
needed. Any later native discovery/check remains separately selected; required
final committed-deliverable review still applies. Unexpected shared consumers
or behavior changes return to lead. This task selects no merge, deployment,
lifecycle action, artifact cleanup or new operation; existing evidence remains.

### Selected minimal finishing: recorder exclusion, final history and verification

The user's “very well, proceed” selects the following finishing scope.
Implementer0 is the sole application/Git owner; lead coordinates review and
native verification. Architect edits only this brief. Inspected clean head
`07e31b96befb3afe2e8898065fe85a9d0b842611`, tree
`70e412f6846a426673de778ea77d4d3b02a06da2`, above base
`846bb469505789ba0b2a405fa5905ba6d8253006`; the nine-commit inventory and prior
`final-review.md`, `final-review-remediation.md`, and `upgrade-cleanup-review.md`
inform this scope, without substituting for the requested final whole-branch review.

Remove only the four experimental files under
`tests/suite/kernel/livepatch-6.12.95/`: `hotplug-recorder.c`,
`hotplug-recorder.bpf.c`, `hotplug-recorder.h`, `hotplug-recorder.nix`.
Remove their owning paragraphs in `docs/os/testing.md`, current lines 338–365
(from the livepatch-source link through the runtime-admission disclaimer).
Keep the hotplug diagnostics heading and cumulative-health paragraph at 330–337,
moving their history ownership to the health change. Keep the exact 12-line
qualification delta (9 additions/3 deletions): phase labels, original example
dmesg baseline, health assertion after CPU/progress checks, and both callers.
No recorder caller exists outside those four files/docs. Exclusion does not
certify recorder correctness or explain the original kernel warning.

Account for all nine old commits as follows; the five surviving logical units
remain independently useful, rather than targeting a commit count:

| Old commit | Final disposition |
| --- | --- |
| `ae33b06b0264b2aabcb5af21bb47c029a6a3f091` | Keep writer fix and units as unit 1. |
| `be4ec430d49395513a0c7188bffcd78f17cd4ae9` | Keep authenticated reader/import/GC safety, units and docs as unit 2. |
| `50a796f2824424252be177aedafb277b6f149073` | Drop superseded DHCP diagnostic introduction; retain evidence outside shipping history. |
| `247c091e6a48083099395e5e1f4847ef5a585be6` | Drop superseded first-switch diagnostic introduction/gate. |
| `a1c4dc932b953cc21fde47a2fc2e6f85bb03e8f8` | Drop obsolete historical opt-in intermediate state. |
| `a2e4c097103eeeba8ae016571ffbe25316ceb10f` | Unit 4: focused impermanence regression, introduced directly at its final name/header by folding that part of `07e31b96`. |
| `39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17` | Unit 3: exact health delta plus its explanatory paragraph from `f74629fa`. |
| `f74629fa4046089e2c53d0cb0e3ba7ef5b178e82` | Omit experimental recorder and owning prose; only health explanation transfers to unit 3. |
| `07e31b96befb3afe2e8898065fe85a9d0b842611` | Unit 5: retire baseline historical matrix/exclusive support and add lifecycle policy/AGENTS routing; rename/header refinements belong to unit 4. |

Preserve old refs, authorship/contributor credit, complete truthful rationale,
retirement evidence, checks and unexecuted limits. Diagnostic and recorder
experiments were used for development evidence, not successful production
verification. There are no schema/migration versions or repeated dependency-pin
streams in this range. Existing YAML/run IDs remain old-reader-loadable; rollback
loses authenticated recovery/GC safeguards, as documented. No coordinated node
update is introduced. Do not rewrite or delete historical evidence/roots.

Before rewriting, owner0 makes the exact dated backup and isolated topic checkout
required by repository policy. Demonstrate history-only consolidation against
the old tree before mixing in recorder exclusion. On the original base, the
intended source tree is **exactly `07e31b96` minus those four files and the stated
docs paragraphs**: all other paths, modes and bytes stay equal. In particular,
impermanence implementation/units, cleanup/policy, final test name, immutable
baseline, assertions and full testScript remain exact; retained script SHA256
is `b949f3fc408e31daa78fcf15d46016fe424ccceafb33096c9e821579be9e78e4`.
Use ordinary Git tree comparisons/range-diff and existing Markdown records,
not a reconstruction framework or new manifest system.
Owner0's read-only plan proposes backup ref
`backup/2026-10-24-ci-failure-analysis-pre-minimal-finish-07e31b96` and isolated
`vpsadminos-final-series` worktree. Its in-memory expected old-base tree is
`30b7c57e4027980683968c72579df3e63b165bc5`, exactly the four deletions and
28 exclusive documentation lines; verify this through native Git during
reconstruction. Preserve the first two exact commits on that original base.

Lead reports cached `origin/staging` at
`e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` (flake impermanence update).
After backup/reconstruction, owner0 may fetch origin once over SSH and rebase
onto the actual current target before final checks/review. Preserve upstream
content; record actual fetched base and old/new ranges. Distinguish the exact
five-path recorder exclusion from upstream changes with native range-diff and
tree comparisons. A rebased tree is not expected to equal the old-base tree;
preserve patch equivalence where possible and route substantive conflicts or
changed behavior to lead. No push or broad CI is selected.
The reported upstream delta is one impermanence-lock commit; retain it rather
than restoring the old lock for tree equality.

Quick acceptance: exact allowed delta and history inventory, no stale recorder
references, retained script/config equality, scoped Nix/Ruby formatting/syntax,
focused existing writer/import/GC units where required by final changes, and
normal hooks. Then review the **committed, checked, rebased complete series**
with retained independent reviewer0 under the mandatory workflow, covering all
four applicable lanes and explicit history/migration conclusions. Resolve
Blocking/Important findings before long VMs; old reviews remain provenance.
No early review, historical VM or repaired diagnostic fixture is needed.

Focused native acceptance uses the normal repository route on that final head:
`./test-runner.sh ls 'upgrade/*'` and
`./test-runner.sh ls -t ci 'upgrade/*'` must each discover exactly
`upgrade/impermanence-from-2abbe3cc1c10@v1` and `@v2`. Then
`./test-runner.sh test --prebuild -j 1 'upgrade/impermanence-from-2abbe3cc1c10@*'`
prepares the selected images before running only that pair serially. This uses
the existing runner's discovery → image preparation → VM phases; it does not
invent a standalone build command or an extra observer. Lead selects the final
head, concrete argv and finite resource scope before those operations.
Bind ordinary native results to the
actual final checkout, baseline, locks and realized inputs/scripts. Retain the
production/candidate service → wrapper → resolved-gem byte check for the four
changed implementation files; names/versions alone are insufficient. Both runs
must observe genuine old-writer stale state, same live run/root/payloads through
repair, reload without rewrite, new-writer persistence and normal retirement,
with unchanged boot/kernel and correct cgroup mode. Missing stale-state coverage
is a failure, not permission to synthesize state or retry. No qualification/BPF
runtime or broad CI is inferred from these two tests.

Even discovery's `test-runner.sh` unconditionally builds the runner. Pinned
sources, tools, guest images or outputs may be absent; no cache availability or
physical fit is assumed. Use ordinary repository installation/build commands
and the existing monitoring procedure with a fresh policy watcher for uncertain
operations. Lead binds command/resource admission and cancellation to the actual
operation; do not repurpose frozen observer/prerequisite/ledger packets, reset
carried accounting, or silently increase old scoped ceilings. Unexpected local
kernel builds stop under workspace verification policy. A real missing-input
or resource blocker returns to lead without a helper/restoration campaign.
The previous 6-GiB contract with the same 512-MiB allowance and only 65,052,672
bytes residual covers no-query validation/read-only prerequisites, not these
builds/VMs. Keep 43-GiB fresh admission/40-GiB free floor; no fresh capacity or
final-output cache availability was measured here. Old source/tool/image receipts
do not establish outputs for the newly rebased head; no retained exact final
pair closure/size proof is available from this inspection. Source trimming,
history preparation and review readiness proceed independently of this native
feasibility decision. Frozen ledgers and their no-refund obligations remain.
Publication, unfiltered CI, merge, deployment, lifecycle and artifact cleanup
remain held; this brief performs none of the proposed commands.

### Proposed discovery client-memory correction after discovery3 OOM

Lead reports final five-owner review PASS and discovery3 on exact `04a2`:
the ordinary source-root derivation built, then the 1-GiB client scope reported
`oom-kill`, terminal status 1 after about 20 seconds, before catalog names;
list2 did not run. Retain that failure and both prelaunch refusals unchanged.
Subject to lead's retained-log assessment, 4 GiB client `MemoryMax` with no swap
is a proportional finite correction for ONE separately selected fresh discovery
batch using the same cached normal runner. It addresses an observed resource
failure, not a source defect; neither 4 GiB nor prior source-root realization
proves future fit, availability or discovery success. Preserve whole daemon plus
client 8/12-GiB admission/stop, host 20/16-GiB gates, free-space 43/40-GiB gates,
300-second deadline and 32-MiB logs; the client cap does not bound daemon use.
Keep the existing prospective 40-GiB cumulative disk scope and all carry:
33,038,344,192 bytes was BEFORE discovery3, not its final charge. The exact later
endpoint/accounting is pending; include that operation and subsequent positive
gaps before admission, retaining the same 512-MiB allowance and no refunds.
No old limit/failure is rewritten, no automatic retry or further increase is
authorized, and no new monitor/helper/accounting design is selected. This is a
resource proposal only; lead selects any fresh operation after reconciliation.

### Selected correction: prove ordinary live base-root import applicability

User selected this narrow correction; source baseline is reviewed
`04a2d2696bb4bcc7602221008a5c5096ede98046`. Session/environment match
`2026-10-22-ci-failure-analysis`; architect0 and sole application writer
implementer0 retain ready/workspace-write settings. This brief precedes edits.
Enabling impermanence on an already-running ordinary NixOS CT updates its
next-start configuration without replacing its current base root. Current pool
import incorrectly requires a temporary GC owner for that legitimate run.

Extend the existing authenticated import method with a proven-base case, using
the same retained process identity and publication transaction. Keep the existing
pool applicability gate; do not add an alternate importer or recovery framework.
Complete saved metadata must select exactly `ct.dataset` with cleanup false.
An ownership snapshot with no same-run temporary claim and no cleanup owner
overlapping the base permits **checking** that base candidate, not accepting it.
Unrelated GC records are allowed. Require the existing held init/PID-1/birth,
cgroup, namespace, exact ZFS source/GUID, mount and `private` directory identity
checks to prove that the actual live root is this base. A real temporary root
cannot pass that proof. Never derive a candidate from arbitrary mount paths or
catch failed authentication and fall back to ordinary import.

Use the current root-identity primitives with a narrow base/temporary distinction:
base datasets may legitimately be clones, so a base proof must not impose the
temporary-only `origin == "-"` requirement. Still compare the exact returned base
properties across preparation. Preserve all temporary-root restrictions. If a
same-run temporary owner exists, retain the existing unique-owner, suffix,
overlap, saved-selection and live-root authentication before repair. Saved
temporary roots keep the same checks and no-rewrite behavior. Base plus cleanup
true, foreign/ambiguous ownership, saved/live disagreement and changed evidence
remain refusals; missing ownership never authorizes temporary-root recovery.

A pool with no temporary datasets can legitimately lack its GC file. Permit an
explicit absent snapshot only for the base-check case with empty in-memory
ownership, rechecking the same absence and empty ownership before publication.
Keep strict ownership reads as the default for temporary recovery. A present
malformed/unreadable/changed file or symlink is not absence. File appearance,
disappearance or ownership changes during preparation refuse. Do not create a
GC file/owner to satisfy this case or weaken the collector's retirement fence.

For a proven base run, preserve saved YAML bytes, run ID, in-memory base selection,
cleanup false and GC records; perform no repair/write/registration/free. Retain
the authenticated descriptors through preparation, final root/birth/file/GC
rechecks and publication in the existing manipulation exclusion. Do not release
proof and fall through to a numeric-PID re-probe. Preserve failure rollback,
identity closure, post-publication managed retention, monitor/console ordering
and pool-wide reclamation inhibition on genuine import failure.

Implementation boundary: `osctld/lib/osctld/container/run_configuration.rb`,
the narrow absent-snapshot support in `osctld/lib/osctld/garbage_collector.rb`,
and `osctld/lib/osctld/pool.rb` only if needed for the existing call/comment;
their existing specs under `osctld/spec/osctld/`, plus the relevant paragraphs in
`docs/os/updates.md` and `docs/containers/datasets.md`. No new API, schema,
framework, test matrix, helper or runtime campaign. Route material deviations
through lead before edits. Disabling next-start impermanence likewise must not
alter the current run's dataset/cleanup ownership; reverse-toggle dispatch is
unchanged here, and this correction does not claim authenticated legacy repair
when that existing gate is disabled. No broader reverse-toggle project is selected.
Existing state formats remain readable by older daemons; rollback can restore
the old refusal/older recovery limitations. Nodes may update independently;
no coordinated update, workload restart or deployment is selected.

Acceptance uses focused existing Ruby specs exercising the actual import methods:
enabled-next-start plus live base imports without rewrite, owner invention or
inhibition (absent GC file, empty file records, unrelated records, and clone
origin); a same-run owner/live-base contradiction refuses; live temporary root
without its owner cannot take the base branch; genuine stale-base recovery and
already-correct temporary no-write import still pass. Retain refusal tests for
identity/root/birth/cgroup, saved-file/GC changes, ambiguity and cleanup mismatch,
plus preparation/publication failure retention and unchanged stopped/ordinary
dispatch. Prove final base checks use the held identity across preparation.

Lead selected source/check preparation within 1 GiB including one isolated
checkout, fixtures capped at 128 MiB and logs at 1 MiB, with 43/40-GiB free gates.
Implementer may reuse the existing cached repository Ruby/spec environment for
focused specs, Ruby syntax/style and normal hooks; no Nix/native discovery retry
is implied. Complete and commit the intended correction and quick checks before
independent review; any later VM verification requires separate bounded selection.
Existing discovery OOM, frozen packets/ledgers and all no-refund obligations stay
unchanged. This design step runs no checks or native operations and dispatches
no implementation. Publishing, integration, deployment and cleanup remain held.

### Selected bounded postmerge failure investigation (2026-10-25)

The user selected investigation of the failed checks on merged head
`75836892e5d446d7c1f76411654a4c1809ceb3a0` and the bounded helper-spec repair.
Session/current/environment and roster32 match; saved settings are unchanged.
Architect0 owns source/evidence synthesis and this design only. Implementer0
owns the missing-phase unit call under lead's small-edit brief; implementer1
owns exact CI prebuild artifacts and implementer2 exact aged-scale artifacts.
Do not duplicate their downloads. No further substantive implementation follows
without a concrete cause, minimal file boundary and selected verification brief.

At this checkpoint, CI40133879811 passed the OS build but failed preparation of
109 selected tests before their VMs; both impermanence names were discovered,
which establishes neither transition success nor an impermanence assertion
failure. The separate `amd-scale-aged-v5` lifecycle job failed while eight other
lifecycle jobs passed. RSpec40133879825 passed osctld1553/0 but failed one of397
test-runner examples. These are separate execution phases; do not infer one
shared cause or that the successful OS build realized every test closure.

Source establishes the unit failure: the hotplug spec at
`test-runner/spec/test_runner/livepatch_qualification_cleanup_spec.rb:317/325`
calls `qualification_hotplug` without its required `phase:` keyword. The helper
at `tests/suite/kernel/livepatch-6.12.95/qualification.rb:231` requires it, and
both production callers supply pre-/post-transition values. Keep that contract
and cumulative kernel-health assertion. The smallest repair is the spec call
and only its necessary fake helper context, preserving CPU identity/progress
and deadline assertions; no default phase or production relaxation. Review the
actual focused check result rather than assuming the keyword fixes every fixture
dependency. This unit error alone explains neither native job failure.

Artifact acceptance must bind head/run/attempt/job/script and retain the first
concrete error before its cascade or cleanup errors. For prebuild, identify the
first failed derivation/build stage and whether the evidence supports source,
missing/substitution/network input, resource failure or still-unknown cause;
retain the exact log and selected configuration identities. For aged-v5, locate
the first assertion/kernel message and its position relative to hotplug, patch
activation and cleanup. Compare signatures only where the actual evidence
matches; old v6 history is not proof of the v5 cause. Preserve kernel health,
workload progress, ABI and ownership assertions. Eight passing rows do not
establish harmlessness or a frequency estimate.

Pending owner reports, no further fix is selected or justified. Recommend only
the smallest change supported by retained evidence, with a meaningful focused
regression and unchanged compatibility/rollback contracts. If evidence cannot
discriminate causes, report that exact gap before proposing any bounded next
diagnostic; do not retry, extend timeouts, retire more cases or widen the kernel
campaign. No production API/schema/state or coordinated node update is proposed.
The already-selected helper repair affects its unit fixture only and cannot
establish native VM success. Required quick checks and committed independent
review belong to its implementation owner/lead, not this read-only assessment.

This assignment permits retained artifacts and source reads plus this existing
design record only: no tests, Nix/builds, probes, fetch, VMs, runtime/retries,
application edits, push/merge or cleanup. Remote/default changes remain held;
old packets, resource ledgers and restoration work remain closed to this scope.

Prebuild evidence received from implementer1 and directly read:
`repair/ci-followup-prebuild-1/prebuild-build.log` records GitHub archive HTTP429
for Linux revisions `1dfea587406b7dd79973831d1677fb2418e5e9aa` and
`a770f5086fc500ca258852aea1cb3e209a342d2b` (first errors1553/1556; retries
exhausted1850–1854; source derivations fail1940/1969). The later kernel-config,
selftests, system and aggregate-prebuild errors are dependency cascades; final
line2039 reports preparation exit1. These revisions are named in
`os/packages/linux/available-kernels.nix`. This establishes an upstream archive
request refusal during realization, not an evaluation defect, OOM or VM
assertion. The responder's precise throttling cause and future availability
are unproved. Keep the pinned revisions/hashes and tests; do not convert the
fetcher or repin kernels just to evade this response. The smallest next decision
is normal exact-source availability/cache handling for those two inputs after
the owner finishes their provenance check, separately selected from any native
retry. No new fetch/check/retry is performed or authorized by this finding.

Implementer1's completed `repair/ci-followup-prebuild-1/findings.md` binds native
job120996309735/attempt1, artifact12577327649 (SHA256
`7cabade3313d7451ad61e3f22af672f9da394adff81c2d01927d003bd14817e3`).
The source owners are `os/packages/linux/packages.nix` (archive URL),
`default.nix` (`fetchurl`) and `available-kernels.nix` (revisions/flat hashes).
Recommend existing trusted publication/availability of those exact archive
outputs before separately selecting fetch-only verification, rather than another
whole-suite run. An alternative official archive endpoint would need its bytes
verified against the existing flat hash before adoption; availability is unknown.
`fetchFromGitHub` is not a mechanical substitute because its unpacked-tree hash
and source identity differ. No source change is currently required by the log.

Aged-v5 interim, read from implementer2's retained
`repair/ci-followup-aged-1/test-runner.log` and `machine-shell.log`: the first
reported assertion is `wakeups` at01:33:26. Population samples at guest elapsed
126.735 and166.928 retain wakeups128 while fork_exec advances2→3; CPU progress
also advances in the displayed rows. The source aging loop directly requires
every counter to advance between its samples. It fails before pre-transition
hotplug/target activation, so this is not evidence of recurrence of the old
hotplug warning or the missing-phase unit call. Producer cadence versus actual
wake starvation remains for owner2's source/evidence assessment; no scheduler
defect, harmlessness, timeout increase or assertion weakening follows yet.

Retained synthesis complete: implementer2's `ci-followup-aged-1/findings.md`
SHA256 `4eec8bad236c76346d5821b3cdcdb9a261c2d9a052d1dc1ec2a38f53a01c7197`
and `evidence.json` bind job120996309853/attempt1/artifact12579606773 to the
same merged head. All256 per-CPU progress/perf counters advanced between the
two samples. The controller requests one futex cohort wake then publishes
immediately; worker execution increments `wakeups` later. The next serialized
fork/exec child must finish before another publication. Thus a newer report
does not guarantee the wake counter advanced. The failed run's controller was
observed in `do_sys_poll` with a child still running; the child's exact kernel
path and eventual progress are unknown. Retained logs show no relevant kernel
fault signature, which is not complete kernel-health proof. This supersedes
the pending producer interpretation above, not the preserved failure.

**Minimal correction PROPOSAL, requiring lead selection:** in the existing
aging loop in `tests/suite/kernel/livepatch-6.12.95/qualification.rb`, keep the
60-second aging sleep, then call existing `qualification_wait_for_progress`
with the prior population before rereading and strictly asserting progress.
That helper already waits at most60seconds for elapsed plus every hard counter;
reuse it without changing its predicate/timeout. This deliberately permits up
to60seconds additional waiting per age iteration, with the original age target
and overall limits unchanged; it is not a promise that this failed run would
pass. Preserve task/CPU identity, strict wake/fork/all-CPU progress/perf, network,
NFS, TUN and kernel-health checks and failure/cleanup behavior. If the bounded
wait expires, report a real progress failure and retain diagnostics, without
retry or further time extension.

If selected, application scope is that aging call and the existing focused
`test-runner/spec/test_runner/livepatch_qualification_cleanup_spec.rb`; serialize
with implementer0's already-selected fixture edit. Meaningful fake checks must
exercise the actual wait predicate and its aging use: newer elapsed/fork with
equal wakeups remains pending, genuine advancement of every counter permits
reread/strict assertion, and never-advancing counters propagate timeout/failure.
Reuse the current cached Ruby environment for focused checks only after selection,
then committed review before any separately authorized VM. No producer/kernel,
resource framework, test retirement, pin, schema/API or deployment change is
proposed; rollback changes only test observation timing. The supported conclusion
is three distinct failures: one unit call-site defect, two HTTP429 input fetches,
and an aging assertion whose single-report timing assumption is unsupported by
its producer. No additional implementation or operation is selected here.

### Selected two fixes: Linux fetch backoff and aging observation

User “all right, let's fix the two issues” selects these source corrections on
merged primary `cb4dcaaa397cad1f18c8f3c067b95bb8036072dd`; the earlier helper fix
stays intact. Current/session environment and roster32 verified; architect0,
implementer0 and implementer1 retain ready/workspace-write settings. This section
selects the previously proposed aging change and the finite fetch policy below,
superseding investigation-only status for these two implementation boundaries.
No further source, kernel or operational campaign is selected.

**Implementer1: Linux source fetch only.** In
`os/packages/linux/default.nix`, extend only the existing `src = fetchurl` with
this `curlOptsList`, plus a short explanatory comment:

```nix
curlOptsList = [
  "--no-retry-all-errors"
  "--retry" "3"
  "--retry-delay" "30"
  "--connect-timeout" "30"
  "--max-time" "600"
  "--retry-max-time" "1800"
];
```

Normal formatting may put each list element on its own line. This permits the
initial request plus at most three transient-error retries, normally30seconds
apart. Connection establishment gets30seconds; each transfer gets600seconds to
allow large Linux archives; new retries have an1800-second initiation window.
These are finite policy choices, not measured archive transfer requirements.
Honor curl's Retry-After behavior; do not promise an exact30-second interval
when the server requests longer. Explicitly undo the fetcher's default
`--retry-all-errors`: curl's ordinary transient set includes429 and selected
5xx/timeouts, but not404. Do not add `--retry-connrefused`, all-error retries,
VM/build/compiler/assertion retries, a new fetcher or whole-CI wrapper.

Support is verified by read-only bytes of the exact failed source derivation
`/nix/store/ikwlcnx4s3diz6carwzxpv6hdvjsz30r-1dfea587406b7dd79973831d1677fb2418e5e9aa.tar.gz.drv`
and its named `vvlgjnnch92k53af32iwim3d7jdxai3y-builder.sh`: default retry3 and
retry-all-errors precede curlOptsList. The installed curl8.22.0 manual, resolved
through the public system/profile man path to
`/nix/store/86h60daxqvclraj4xril7ffjrsagy4gf-curl-8.22.0-man/share/man/man1/curl.1.gz`,
documents the negative flag, last-value semantics, transient status set and
all selected time options. The exact builder dependency's separate manual/source
outputs were absent; this is installed same-version documentation, not a claim
to have run the failed fetcher. Keep curlOpts empty and do not introduce an
environment override; later NIX_CURL_FLAGS can override options if separately set.

The retry window is NOT a whole-fetcher deadline: a transfer started before it
expires can finish later, Retry-After affects sleeps, and the existing builder
can start another curl invocation to resume exit18 partial transfers. Do not
rewrite that builder or add a timeout wrapper. Existing operation/job deadlines
remain the outer bounds (ordinary CI native step350/job360minutes here), with no
new local native operation selected. Record this limitation rather than claiming
the entire fetch is bounded to1800seconds or four HTTP requests across resumes.
Keep URL, full revisions, flat hashes, output name/mode, source contents and
kernel configuration unchanged. Fetch derivation metadata changes; identical
fixed-output archive identity remains reusable, and Nix still rejects wrong
bytes without this curl policy retrying a hash mismatch. Do not claim evaluated
downstream derivation equality or present cache availability from static checks.

**Implementer0: aging call and existing helper spec only.** In
`tests/suite/kernel/livepatch-6.12.95/qualification.rb`, keep `sleep 60`, then
insert `qualification_wait_for_progress(population)` before the existing
population reread and strict comparison. Retain its existing60-second bound:
at most60seconds extra observation time per aging iteration is now selected,
without extending the age target or overall job/operation limits. Preserve all
task/CPU identities, strict counters, health/network/NFS/TUN checks and failure
cleanup. No C/kernel changes or equality acceptance. This fixes the unsupported
single-publication assumption; it does not prove eventual progress on the old run.
Extend only `test-runner/spec/test_runner/livepatch_qualification_cleanup_spec.rb`
using the actual existing helper/predicate and a focused fake aging context:
newer elapsed/fork with equal wakeups remains pending; later advancement of all
counters permits reread/strict assertion; a permanent stalled counter propagates
timeout and does not continue aging. Preserve the already-merged phase/health
fixture and existing progress/CPU/deadline cases. No new test matrix/framework.

Disjoint edits may proceed after lead delivers this brief; lead serializes all
Git/index/commit work in primary. New coherent commits, no rewrite of merged
history. Source preparation <=128MiB per package, logs <=1MiB, free43/40-GiB
gates; old packets/ledgers unchanged, no refund or implicit new native budget.
Quick checks: cached repository Ruby focused spec/syntax/style and normal hooks;
cached nixfmt check and Nix parse-only check on the one changed Nix file plus
static URL/revision/hash/scope comparison. No literal-option mirror tests or
new loopback harness are required. Commit completed changes and pass quick
checks before independent review. No archive fetch, Nix evaluation/build,
tool installation, network probe, VM, CI rerun, push/merge, deployment or cleanup
is selected. If later native fetch validation is needed, propose only exact
pinned source realization after review under separately selected finite bounds.
No API/state/schema or coordinated node update; rollback restores previous
fetch timing and test observation only. No new product documentation page is
needed; adjacent comments explain the narrow invariants and timing limitation.

### Selected impermanence fixture identity-lifetime correction; prior cb4 evidence

This concerns CI40174698311/attempt1 at merged
`cb4dcaaa397cad1f18c8f3c067b95bb8036072dd`, not the separately watched
`96facc49755c17e18f1e57473d8534fac4669f8d` run40215992804. Owner1's complete
`repair/two-fixes-prior-ci-followup/findings.md` and named native logs establish
107/109 tests passed and only the two impermanence instances failed on first
candidate import. The exact records preserve PID/birth (v1:2808/6855;
v2:2823/6798), root, mount namespace, cgroup, ZFS identity, private directory,
GC owner and payload. Only the sampled proc inode differs:
v1 `[29,7694]`→`[29,11274]`; v2 `[29,7077]`→`[29,9648]`. Each observation has
stable root/namespace and birth-before/after. Later reload/new-writer/retirement
steps were not reached and are not certified by this evidence.

The fixture starts a separate Ruby probe for each observation and holds its
proc/root/namespace descriptors only for that probe. It nevertheless compares
proc dev/inode across observations. That is not a retained-handle identity
contract: an independently reopened proc entry need not preserve its inode
number. Inode/dentry recreation is plausible; its cause was not observed.
Production `ProcessIdentity` instead retains its pidfd/proc/root/namespace
objects and checks those exact descriptors while alive. Its checks are correct
for their lifetime and remain completely unchanged.

**Selected minimal correction, sole application owner assigned by lead:** change
only `tests/suite/upgrade/impermanence-from-2abbe3cc1c10.nix` and, only if needed,
a short owning-doc clarification. Keep proc dev/inode in recorded evidence.
Capture that identity immediately after opening the proc directory; include its
unchanged fstat identity at the end of the same sample in the existing `stable`
predicate. All task reads remain relative to that held proc handle; continue
holding root/namespace descriptors and rechecking them, both stat births and
namespace-PID1 evidence before accepting the sample. Remove only `proc` from the
cross-observation equality list, with a comment explaining the lifetime boundary.
Do not drop PID, birth, root, namespace, cgroup, root rows, ZFS, mountpoint,
private-directory or owner comparisons; preserve payload and exact config repair
checks, host boot/kernel checks, genuine stale-writer requirement and all later
reload/new-writer/retirement assertions. No background holder or helper process,
daemon, probe framework or new observation ledger.

The anti-reuse contract is the same host boot plus PID and unchanged process
start ticks, authenticated through the held proc handle on both sides of each
sample, independently corroborated by the same root/mount namespace and saved
run/GC/data identity. Numeric PID reuse with a different birth must fail; a
different task/root/namespace cannot be accepted merely because its path or PID
matches. Held proc reads do not reopen `/proc/<pid>` between checks. This is a
strict observation-to-observation continuity contract at the recorded start-time
resolution, not proof that a pidfd stayed held or liveness was continuously
observed across the userspace switch. The old inode comparison supplied neither
of those stronger guarantees. Do not advertise such a new guarantee or weaken
production authentication to match the fixture.

Quick verification must use the actual embedded Ruby assertion, in a cached
Ruby/RSpec context without running its VM/probe: retained v1/v2 before/after
records differing only in proc inode pass the relevant import checks; perturbing
PID, birth, root, namespace, GC/config or payload still rejects, as does false
within-sample `stable`/changed birth-after. A small fake held-descriptor case
must reject changed within-sample proc identity. Use finite scratch fixtures or
an existing suitable test context, not a new generic harness or duplicate
implementation of the predicate. Nix format/parse and extracted-Ruby syntax,
static assertion/unchanged-baseline review and normal hooks are proportional.
Architect runs none of these checks. Commit/quick-check/review order stays;
any actual v1/v2 VM rerun remains separately bounded and selected. This changes
fixture observations only: no schema/API, production state, deployment order or
fleet coordination; rollback restores the unsupported test assertion. Old
failure artifacts/ledgers and new-head watcher remain untouched. No merge,
network/download, Nix evaluation/build or runtime action is authorized here.

**Separate aged-v6 finding, no fix selected:** oldcb4 job121115448797 passes
initial aging and pre-transition hotplug health, then three nfnetlink_queue
activation refusals precede an RCU-preempt stall at kernel15252.742947 on
CPU97/PID30382 `insmod`. The stack traverses module loading/text ROX/page-attribute
changes into `smp_call_function_many_cond`. Subsequent livepatch7 activation
completes at16045.155135; post-transition cumulative health correctly retains
and fails on the earlier stall. This is not the aged-v5 report-publication race
or the prebuild429 failure. Temporal ordering does not establish which callback,
peer CPU, scheduling condition or kernel defect caused the stall. Keep the strict
health predicate and exact retained event window; owner2's bounded assessment
is separate. No kernel patch, longer timeout, retry, new instrumentation or
broader source acquisition is selected. No verified exact a238 kernel source
path is available in this architect context; do not invent one.
