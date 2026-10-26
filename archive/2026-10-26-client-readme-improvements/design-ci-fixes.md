# CI environment fixes

## Active superseding brief: conventional benchmark setup

Accepted by the user and lead on 2026-10-26 after the user rejected the large
`utils/performance-env` subsystem. This section supersedes the earlier Phase 2
and every receipt/proof/snapshot clarification below. Those sections are history,
not implementation requirements. The architect's earlier design was excessive.
Published `08355a22` is rejected and not mergeable; its checks are historical.
Implementer3 reports the checkout reconstructed to exact Ruff-only
`65a9082ed68cd2546b9a12c69bd9b0ac0b9859b8`, clean index, with the rejected
performance subsystem absent. Preserve that Ruff change exactly.

The lead accepted the source-pair decision below before implementation. This
written brief supplies the release boundary for the lead to start the owners.
No further investigation, remote recovery, build or test was performed for this
revision. Architect0 edits this design only; implementer3 owns all Git operations.

### Runtime and evidence contract

Use one conventional benchmark tool bundle owned by `servers/ruby/benchmarks/`:
one ordinary `Gemfile` and tracked `Gemfile.lock`, a small pinned Nix shell
(prefer `shell.nix`), and a short launch/install script only if needed. This is
an application/tool lock, not a committed library lock. It installs third-party
benchmark dependencies, not either measured HaveAPI tree. Do not copy historical
source skeletons, component gemspecs or three historical bundle trees into it.

Pin the benchmark shell independently to calibrated nixpkgs
`02c087f3fe673c9e317f206a627cb6b910336dbe` and its known NAR hash
`sha256-IoNisKcGbUjdd45qCqywGMCYmZ5EnkxezvLII0FWwNA=`. Use ordinary Nix and
Bundler frozen installation in an owned gem directory. Both exported roots run
outside Bundler with the same Ruby and gem search paths. Clear inherited
Bundler/Ruby injection settings, including `RUBYGEMS_GEMDEPS`. Keep native
installation under that Ruby and fail on installation or activation errors.
There is no custom native inventory, installed-file/archive/Nix-closure hashing,
portable validator, receipt schema, commit/tree/blob proof or source byte union.

Require the actual Ruby identity and complete activated dependency graph to
match the existing calibrated weekly identity exactly, including the executable
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`, JSON 2.21.2,
Faraday 2.15.0 and the calibrated platform choices. Do not fabricate a matching
fingerprint or normalize a different Ruby. A single tool lock has its own actual
hash: it is not byte-identical to the three historical library locks. Ordinary
lock preparation may use their known resolved versions without claiming their
historical bytes. If a conventional bundle cannot produce the required loaded
graph, stop and report the specific mismatch; do not silently recalibrate.

Keep existing source exports/archive hashes, raw manifests, source identity and
loaded-source checks. Retain source-root `flake.nix`/`flake.lock` as provenance;
they do not supply the runtime and therefore need not equal one another in this
explicit benchmark setup. Retain the actual benchmark shell/lock input hashes
and runtime graph as consumed inputs. Preserve strict comparison of every other
supported declaration, Ruby requirement and existing narrowly verified JSON and
maintenance version normalization. Validate supported declarations against the
selected runtime/dependencies before timing; unsupported changes fail fast.
Use existing evidence structures with only the direct fields needed to record
those inputs, not a new validation framework. Historical schema-2 replay retains
its old semantics; it does not acquire the new subsystem's prerequisites.

Keep fixed reference `b85ec364057f536940d689b09e612512ffffaf82`, every budget and
calibration byte, response/query/authorization checks, timing classifier and
no-blind-retry behavior unchanged. Relative allocations compare candidate with
the selected baseline; existing absolute historical allocation ceilings also
remain. An already excessive allocation count can fail even when a push improves
it. Changing push pairs does not require changing that independent safety cap.

### Exact source selection

| Event | Baseline | Candidate and constraints |
| --- | --- | --- |
| Existing branch push, quick | Exact nonzero event `before` | Exact event `after`; all branches use the pushed pair |
| New branch push, quick (`before` all zeros) | Merge-base of `after` and captured exact default-branch SHA | Exact `after`; retain the captured fallback SHA and reason |
| Pull request | Existing merge-base of exact event base/head | Exact head; existing restrictions unchanged |
| Weekly and manual | Existing selection and restrictions | Fixed-reference weekly and verified maintenance mapping unchanged |

Reject deleted branches, malformed/noncommit/missing object SHAs, zero `after`,
equal endpoints and unavailable new-branch fallback. Do not replace a missing
nonzero `before` with the default or `HEAD^`. Fetching exact event objects belongs
to the workflow's existing source preparation, not selection guesswork.

**Accepted force-push decision:** a valid existing-branch quick push may compare
nonancestor `before`/`after`. Carry a narrow explicit push-pair exception through
the resolver, Campaign and runner's existing ancestry guards. It must bind the
selected pair to that event; no generic ancestry override and no silent merge-base
substitution. Both exact roots are exported independently and their ordinary
source/runtime contracts still apply. Other PR/manual/weekly ancestry rules and
maintenance normalization restrictions remain unchanged. Relevance uses the
direct before/after tree diff. New benchmark setup files are relevant paths.

Source basis: pre-performance-fix `cb43ae23`, `utils/performance_ci.rb` Resolver
and Campaign, `endpoints.rb` run_samples/source_identity, and
`performance_compare.rb` validate_source_pair/allocation classifier. The
comparator itself needs distinct exact sources, not ancestral ordering. The
three caller ancestry guards need the narrow event exception; no timing algorithm
or allocation threshold change is needed.

### Independent implementation packages

| Owner | Exclusive files and result | Dependencies |
| --- | --- | --- |
| implementer2 | New benchmark `Gemfile`, `Gemfile.lock`, small `shell.nix`, optional short launcher; only the `.gitignore` exception needed for that application lock | Confirm the short launch command and gem paths with owner1; no root `flake.nix` edit |
| implementer1 | `utils/performance_ci.rb`, `.github/workflows/servers-ruby-performance.yml`, benchmark `endpoints.rb`/`performance_compare.rb`, affected runner/comparator specs and `doc/performance.md` | Consume owner2's setup; implement event selection against owner0's expectations; do not edit owner0's test file |
| implementer0 | `servers/ruby/spec/performance/event_baseline_spec.rb` only: exact push-pair/fallback/rejection regression expectations | Can write fixtures independently now; owner1 owns resolver code |
| implementer3 | Checkout, hooks, staging, commits, history consolidation, publication and approved integration | Sole Git/index/ref owner; preserve Ruff and do not reintroduce rejected commits |

Start owner1 from the pre-performance-fix implementation already restored by
owner3. Do not port the rejected Preparation module, receipt options, proof specs,
helper directory or corresponding documentation. Keep only useful existing
source/runtime/classifier checks. Owner1 and owner2 settle the small command
interface directly and route a material contract deviation through the lead.
The source selection specs are an independent package, not a request for a new
mocking/provenance framework. Simplicity is an acceptance criterion: ordinary
Nix/Bundler files and bounded runner changes, no replacement subsystem.

### Acceptance and proportional verification

Before fresh final review, owners run one focused deterministic batch covering:

- Existing-branch pushes use exact `before`/`after` across default, feature and
  maintenance branches, including multi-commit and nonancestor force pushes.
  New branches use the captured-default merge-base; malformed/deleted/equal/
  missing-object pairs fail. PR/manual/weekly/maintenance contracts stay intact.
- Frozen tool installation and one untimed source/native loading smoke show the
  calibrated Ruby and activated graph for both roots. Changed dependency or
  Ruby identity fails before timing. Contributor flake differences are retained
  and accepted only as unused runtime inputs; other unsupported declarations fail.
- Existing replay, deterministic correctness and allocation/timing specs pass;
  budget/reference bytes remain unchanged. No custom portable-proof tests remain.
  Check workflow syntax and the relevant focused Ruby lint/hooks.

Known fast checks run inline; uncertain installation/smoke duration uses the
existing watcher procedure, initially bounded to 10 minutes with a stop/report
on a build problem. No measured campaign before all intended changes are
committed and freshly reviewed. Stop after relevant checks pass; no broad test
expansion or repeated preparation without a concrete failure.

After review, run ONE actual final-head hosted quick campaign within its existing
15-minute limit, plus the hosted release job for Ruff/full-build validation.
The hosted push must retain the real event `before`/`after`, exact exported roots,
lock/runtime evidence and report, including a rewritten pair if publication is
non-fast-forward. No duplicate local timing batch. Weekly selection is covered
deterministically; no default weekly measured run. Failed, timed-out or
inconclusive evidence is diagnosed honestly; never rerun until green or alter
budgets automatically.

This changes benchmark preparation/CI semantics only: no API, database, service,
deployment or persisted application state changes. It intentionally changes
feature pushes from whole-feature comparison to push-relative comparison.
Historical results remain historical. A future benchmark runtime update needs a
separate reviewed calibration applicability decision and measured evidence.
Recovery reverts the CI change and restores the explicit mismatch, rather than
hiding it. The user's HaveAPI/master integration approval remains conditional on
accepted remediation and verification; no deployment or lifecycle action follows.

---

## Prior brief and historical decisions

Phase 1 below remains the preserved Ruff rationale. All prior Phase 2 decisions
below are superseded by the active brief above and must not guide implementation.

Architect0 brief, 2026-10-26. The user authorized merging the reviewed README
changes and then diagnosing and fixing the two CI failures. Implementer3 reports
the documentation head `cb43ae2367b12e22e602d69312bfd1f7331b4995` merged into
remote master and the merge claim released. Fixes use branch
`2026-10-26-client-ci-fixes` in the registered same-session
`worktrees/2026-10-26-client-readme-improvements/haveapi-ci-fixes` checkout.
Implementer3 owns Git/index/ref operations. The user subsequently authorized
CI-fix integration into HaveAPI `master` with "merge it when you're done", after
accepted remediation and hosted verification. This supersedes the earlier
pending-approval status; it does not claim those conditions are satisfied.
No deployment or session lifecycle action is authorized.

Session identity and retained roster verified. Required workspace verification,
repository development and `doc/performance.md` procedures read. Investigation
uses source at `cb43ae23` and this session's retained CI artifacts; no application
code changes or tests were made by the architect.

## Phase 1: Python Ruff parity (accepted, ready for implementation)

The upstream `ec84ec874eb209ab59848873998456293ddf3c52` changed only `flake.lock`,
advancing nixpkgs from `02c087f3fe673c9e317f206a627cb6b910336dbe` to
`3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`. The new native Ruff is 0.17.2;
`clients/python/pyproject.toml` still requires `ruff==0.17.1`. Both root and
client-python shells export `HAVEAPI_RUFF` from `pkgs.ruff`. The shared
`run_ruff.py` correctly refuses an executable whose version differs from the
installed Python Ruff distribution. Release run 40314732571 installed 0.17.1
then refused 0.17.2 at its first formatting check. This is a tool input mismatch,
not a Python formatting finding or a README regression.

The recurrence mechanism is two independently maintained version sources plus
an updater that currently evaluates/builds no Ruff parity check. The updater
already calls `nix flake check` before staging or committing the new lock.

Implementer0 owns these independent files:

- `clients/python/pyproject.toml`: change the exact Ruff dev pin to 0.17.2.
- `clients/python/CONTRIBUTING.md`: correct its pin explanation and describe
  the automatic parity gate. Keep ordinary local `uv.lock` preparation rules.
- Root `flake.nix`: add a narrowly named flake check that reads the declared
  Python dev requirement and compares it with the selected native Ruff version.
  Require exactly one well-formed exact Ruff pin; missing, ambiguous or ranged
  requirements fail. Check the executable's reported version as part of the
  derivation where practical. Avoid duplicated handwritten version constants.
- A focused test/helper file only if needed to exercise the check; do not build
  a generic dependency-update framework or edit the update workflow/helper.

Keep `run_ruff.py`'s exact runtime parity check. The Nix check is an earlier guard,
not its replacement. Do not execute PyPI's generic Linux binary on NixOS, loosen
the requirement, silently pick an arbitrary executable, or automatically bump
the Python requirement during an input update. A future incompatible Nix update
must fail before its ordinary commit and require an intentional paired change.

Quick acceptance:

1. Prepare an ignored local uv environment/lock normally for the changed
   declarations. Do not commit library lockfiles.
2. Positive evidence: declared pin, installed Python distribution and Nix
   executable all report 0.17.2; the isolated flake parity check succeeds.
3. Negative deterministic evidence: an owned fixture with a mismatched pin
   fails the same check. Verify missing/ambiguous/nonexact pins fail if the
   parsing path would otherwise accept them. Check that the updater still runs
   `nix flake check` before `git add`/`git commit`; no real updater commit needed.
4. Run the existing focused Ruff formatting/lint commands against Python and
   release helpers. Inspect any changed formatting before expanding scope.
   No full Python/server integration run is required for this tooling-only pin.

Budget: focused static/negative checks should take seconds; environment setup
and isolated Nix build may require a watcher. Stop after one successful parity
and format/lint batch. Investigate a failure; do not blindly repeat setup.
Commit with required hooks, then include this package in fresh independent
final review before broad CI or long checks.

Sources: `flake.nix` root/client-python package and `HAVEAPI_RUFF` declarations;
`clients/python/utils/run_ruff.py:12-23`; `clients/python/utils/check.sh:4-6`;
`utils/update-nixpkgs.sh:42-55`; retained
`artifacts/ci-refreshed-head/40314732571-failed.log:431,1271-1276` and
`performance-artifact/shell-input-graph.txt:2340` beneath that directory.

Compatibility: no published runtime requirements, API, persisted state, protocol,
database or generated client behavior changes. This aligns contributor tools.
No deployment is required; recovery reverts the tooling change and leaves the
known parity failure explicit. Do not roll back the shared Nix input merely to
hide this check.

## Historical Phase 2: rejected frozen environment subsystem (superseded)

### Root cause and recovered authority

The performance workflow prepares current default/server/Rust shells using
ordinary `bundle install`, then starts unbundled workers with their combined gem
stores. Ignored local locks preserve one preparation but do not constrain a fresh
CI resolution. Only JSON has explicit activation before requires. Faraday moved
from calibrated 2.15.0 to 2.15.1. The unrelated Nix update also changed Ruby's
executable from `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`
to `/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin/ruby`.
The exact calibration guard correctly rejected both differences. Comparing two
sources in one environment does not establish equivalence to the calibrated one.

The runner also compares source `flake.nix` and `flake.lock` bytes, so merely
restoring the old executable would leave weekly fixed-reference comparisons
blocked after contributor Nix changes. The fix separates the pinned measurement
environment from source contributor-tool configuration explicitly and records
both. It does not claim the measurements cover the moving contributor runtime.

One public artifact inventory and one selected artifact inspection recovered
the exact original prepared locks. Search stopped on that success. No other
session's private files were inspected. Authority:

- Run https://github.com/vpsfreecz/haveapi/actions/runs/40187949233
- Artifact `performance-40187949233-1`, ID `12597024214`, API URL
  https://api.github.com/repos/vpsfreecz/haveapi/actions/artifacts/12597024214
- Workflow head `38ecca75edaf797d048fb36c6a50ea7e05eb50a9`; retained report is
  weekly/pass against fixed reference `b85ec364057f536940d689b09e612512ffffaf82`.
- Downloaded ZIP SHA256
  `4e8dc2aaead88ffbf565d864910b66a6b3d225c19e5093e643abfc0042c510e1`.
- Original root lock SHA256
  `0a48c3e68d0b78caf945cb5a0430d13841ee140eb1bdca5734d823617a42afe6`.
- Original server lock SHA256
  `fdc5129f60f9ed2f6a56fbf7f9483af5d6a003fedb13a93e895e9cab87193b52`.
- Original Rust lock SHA256
  `53b94ab0ef92f5dccfd413eb1e313ed65868f1e2ba41af8b95ce6e62ae8d447f`.

All three hashes match the existing weekly calibration. The retained manifest
files and reference-source gemspecs also match every weekly calibration manifest
hash. All locks record Bundler 4.0.23. Evidence is in this session's
`artifacts/calibration-recovered/`, including exact inputs, original shell
derivation/input graph, flake metadata, runtime, selection, report and
`recovery-receipt.json`. This is authoritative prepared-input recovery, not a
claim that the recovered report is the original raw calibration measurement.

The recovered Nix input is `02c087f3fe673c9e317f206a627cb6b910336dbe`, NAR
`sha256-IoNisKcGbUjdd45qCqywGMCYmZ5EnkxezvLII0FWwNA=`. It selects the required
old Ruby closure. The budget's weekly runtime has 87 activated third-party/default
gems, including JSON 2.21.2, Faraday 2.15.0, fiddle 1.1.8 and
sqlite3 2.10.1 with platform `x86_64-linux-gnu`. Preserve those native/platform
identities; a same-version replacement of the Ruby store path is insufficient.

### Independent implementation boundaries

| Owner | Files | Output and dependency |
| --- | --- | --- |
| implementer2 | New `utils/performance-env/` tree: nested pinned Nix environment, authoritative snapshot/manifests/locks, preparation helper, environment contract tests and brief README; narrowly scoped `.gitignore` exception if needed | Frozen, isolated benchmark tool preparation and a validated receipt consumed by implementer1. No root flake or runner/classifier edits. |
| implementer1 | `utils/performance_ci.rb`, `servers/ruby/benchmarks/endpoints.rb`, `performance_compare.rb`, performance specs, `.github/workflows/servers-ruby-performance.yml`, `doc/performance.md`; `Makefile` only for a necessary entrypoint | Consume fixed preparation, enforce/retain provenance, preserve replay, wire CI and update operation instructions. Depends on implementer2 receipt contract below. |

These snapshot locks belong to a dedicated benchmark tool fixture, not the
published library components. Keep root/server/Rust ordinary library locks
ignored and untouched. Explain this placement in the tool README; do not remove
the general library lock policy. Implementer3 alone stages and commits after
package owners report checks. Material interface deviations go through the lead.

### Preparation and receipt interface

Prepare the benchmark independently of the root or component developer shells.
Use the nested Nix environment pinned to the recovered input, exact Bundler
4.0.23 and the three recovered locks/manifests. Preserve their relative component
layout, including original path-gemspec/version files needed for frozen install;
retrieve missing source files from the verified reference or artifact head and
record which source supplies them. Do not fabricate a lock from hashes or add
pins to library Gemfiles. A shadow installation skeleton may contain these
historical package declarations; measured HaveAPI code must still load only from
the selected exported baseline/candidate source roots.

Installation may copy snapshot inputs to a session/CI-owned preparation directory.
Run Bundler frozen, verify input hashes before and after, and fail on unresolved
dependencies or attempted lock rewrites. Never resolve or update locks in a
campaign. Separate gem homes from normal `.gems` and do not reuse native gems
built under the new Ruby closure. Isolate `GEM_HOME`/`GEM_PATH` to the prepared
stores and the pinned Ruby's default gems. Clear inherited Bundler and Ruby
injection settings for workers. Preserve JSON activation before require; do not
eagerly activate extra gems merely to make a fingerprint match.

Implementer2 provides one preparation entrypoint with an explicit owned output
directory, and a check-only path that validates an existing preparation without
installing. It emits a JSON receipt consumed by implementer1. Owners agreed on
receipt schema 1, mode `calibrated-snapshot-v1`, and shared
`validate_receipt!(..., budgets:)` validation. Remaining option/key details are
coordinated directly between owners. The required receipt data is fixed here:

- Schema/mode identifying `calibrated-snapshot-v1`, selected snapshot content
  digests and fixed reference/budget identities.
- Exact original source/manifest/lock bytes or retained paths plus digests;
  three lock hashes must equal the calibration values above.
- Nested flake definition/lock, resolved immutable input graph, actual shell
  derivation and its complete requisites; actual Ruby executable/runtime tuple.
- Prepared gem directories and resolved graph, including versions, platforms,
  native build runtime and artifact checksums present in original lock data.
  Record original and actual shell graphs separately; a new minimal shell is
  not literally the historical full contributor-shell derivation.
- Evidence of unchanged frozen locks after installation. Live preparation and
  run validation must check actual files/runtime rather than trust receipt
  fields; missing or stale preparation fails before measurement.

The shared `validate_receipt!(receipt, budgets:)` validates retained evidence
and the tool contract only: embedded bytes/digests, source proofs, snapshot
identity and recorded runtime/input-graph claims. Historical absolute paths are
recorded identities, not filesystem dependencies for replay. Keep all required
bytes in the retained evidence bundle or its portable relative members; replay
must not read vanished CI preparation directories, require historical GEM_HOME
or Nix store paths to exist, reinstall gems, or activate the measured Ruby.
Replay may use its documented verifier dependencies, including Git for the new
source proof mode; it does not execute the historical environment.

`prepare.rb check` and the live run entrypoint separately enforce actual
filesystem, interpreter, gem-store, native-extension and frozen-input checks.
Run both the shared retained-evidence validation and these live checks before
measurement. Keep one evidence contract rather than a weaker replay receipt.
This clarifies the original retention intent and requires no format change or
new compatibility mode; requiring ephemeral paths during replay would break
that intent and must be removed from the shared validator.

The run entrypoint validates the receipt and the actual Ruby/native/runtime
context before expensive measurement. After normal source loading, the complete
activated gem map must equal the existing weekly environment exactly. Do not
remove or normalize `ruby.executable`, gem versions or platforms. Preserve the
existing `environment.weekly` and all budget bytes unchanged.

Implementation clarification reported by the lead: the pinned Ruby distribution
also contains bundled gems that are not marked as default gems. Recognize only
the inventory anchored to that exact old Ruby distribution and its digests;
do not classify those gems as foreign solely from their default-gem flag.
This is not permission to admit arbitrary gems beside a Ruby installation or
to change the expected activated weekly graph. Foreign stores, native artifacts
and mismatched distribution contents must still fail closed.

The recovered lock includes multiple platforms. Select its applicable `ruby`
and `x86_64-linux-gnu` entries for the calibrated target, preserving exact
versions, platform identities and checksums; do not require installing unrelated
platform variants or substitute a differently built native artifact.

Preparation metadata binds explicit frozen flake bytes and lock, pinned NAR,
actual derivation and complete input graph. An incidental mutable helper-path
fingerprint is not the environment identity. This distinction does not normalize
the actual Ruby path, source/input digests or runtime/native checks.

Lead-reported environment milestone: frozen installation completed in 65 seconds,
native smoke passed and produced a real receipt; 17 contract tests passed,
including portable replay. Architect0 records this report without claiming to
have rerun it. Implementer1 consumes the real receipt for source-loading and
complete activated-graph smoke validation; full acceptance still requires that
validation and the planned independent review/hosted campaign.

### Source/provenance contract

Retain complete raw source manifests, hashes and source-tree identity for each
selected source, including its root `flake.nix` and `flake.lock`. Add an explicit
prepared-environment receipt to the new mode; the frozen snapshot is the consumed
runtime environment for both sources. The root flake files are still source
provenance but are not consumed to prepare that mode's measured environment.
This is the only new source-input separation; no general hash-ignore option.

For this mode, allow differing contributor flake bytes only after validating
the complete pinned environment proof and both raw files against their exact
source trees. Report those differences. All other dependency declarations,
gemspec Ruby requirements and `.ruby-version` retain current strict equality
and existing narrowly verified JSON/release normalization rules. Verify the
frozen resolved dependencies and Ruby satisfy the selected sources' declared
requirements. A changed runtime requirement or unsupported source shape fails
for a separately reviewed environment migration; do not silently select another
runtime or widen source compatibility.

Use the actual prepared snapshot lock identities in the effective input graph,
not fresh candidate-checkout locks. Raw source provenance and effective runtime
inputs must be distinct, validated fields. Replay recomputes digests from retained
bytes, validates the receipt and raw-source bindings, and requires all workers
to use the same exact effective graph. Merely deleting flake/manifest/lock fields
from comparisons is forbidden. Unknown modes, partial receipts, unexpected
normalization or a forged claimed environment must fail.

Preserve replay of existing schema-2 evidence under its existing strict rules.
An explicit versioned optional preparation receipt within that format is
acceptable if the old path remains intact and new-path validation is mandatory
whenever the field is present. Do not silently reinterpret old observations as
using the frozen snapshot. If implementation needs a format bump, route that
decision through the lead before changing the evidence contract.

The lead approved raw commit, recursive tree and blob proof validation for the
new mode using Git plumbing in a bounded disposable bare object store. Retained
raw bytes must bind to the claimed source commit and complete tree; use Git's
object validation rather than handwritten Git hashing or parsing machinery.
Only owned temporary fixture object writes are permitted. This validation must
not alter the shared project index or refs, create a checkout, run hooks, or
execute retained source content. Implementer1 owns the proof path and its
documentation; implementer2 declares Git in the benchmark environment. New-mode
replay requires Git and must document that dependency. Existing schema-2 replay
without the new receipt keeps its prior path and prerequisites.

For the new mode, retain the union of actually loaded source bytes once per
selected source. Validate each retained blob with the existing Git blob helper
to bind its source-tree object ID to the SHA256 used by loaded-source inventories.
Every observation's loaded inventory must resolve through that verified union;
SHA256 claims alone cannot establish the Git object binding. Do not execute
retained bytes or copy them into every observation. Include a negative test for
altered loaded bytes or a mismatched object ID/SHA256. This completes the
source-only replay proof; existing replay without the new mode is unchanged.

Accepted final-review clarification at committed fix head `ea093280`:
`Preparation.validate_blobs!` must reuse the sanitized, explicitly SHA-1 Git
context used by `validate_tree!`, rather than inherit ambient Git configuration
or repository context. Implementer1 owns the narrow fix and hostile-Git
replay/tamper regression. This preserves the existing proof design and evidence
format. Publication remains held until the correction and final review are
accepted; this record does not claim those checks have completed.

The lead also accepted the reviewer's advisory to clear `RUBYGEMS_GEMDEPS` in
`Performance::Preparation.environment` and the workflow/documented public launch,
matching preparation's existing isolation. Implementer1 owns this narrow change
alongside Git-context isolation. It adds no environment contract or format and
does not change the calibrated runtime identity.

The suspected pre-Nix JSON prerequisite in the workflow resolver did not
reproduce in retained evidence: resolution output and selection succeeded with
empty stderr. The lead accepted the existing loader unchanged. No loader
factoring or additional host-environment work is part of this fix.

Weekly continues to select the immutable fixed reference, including the existing
verified 0.30 maintenance mapping. Quick continues to support its selected
ancestor pair. Both modes use one neutral harness and fixed environment; source
selection/ancestry and relevance rules remain unchanged. Keep aggregate failure,
no-work and inconclusive distinctions. Add the new environment paths to relevant
path detection so edits cannot skip the performance gate.

### Checks, duration and stopping rules

Before final review, perform deterministic focused checks only:

1. Snapshot hashes equal recovered authority and calibration; preparation is
   frozen, isolated and repeatable. Native imports load under the exact pinned
   Ruby and expected SQLite platform. A preparation smoke may load dependencies
   and validate identity; it is not a timing campaign. Use a watcher for installs
   or checks with uncertain duration. Budget 10 minutes initially; report actual
   progress and reassess a slow build rather than expanding scope silently.
2. Tampered/missing snapshot or prepared lock, changed Ruby path, wrong gem
   version/platform, foreign gem-store leakage and stale receipt are rejected.
   No test should need to install an untrusted or new dependency to demonstrate
   rejection; use owned fixture data/process stubs for negative paths.
3. Contributor-flake-only source change succeeds only under valid explicit
   fixed-environment proof, while another dependency manifest, source tree,
   runtime requirement or receipt change still fails. Cover both quick ancestor
   and fixed-reference weekly selections plus existing maintenance normalization.
4. Retained schema-2 replay remains valid under its old rules. New evidence
   replay rejects altered receipt/raw bytes/worker graph and still rejects
   allocation/query/authorization/output defects. Keep timing policies, reference
   identity and entire budget file unchanged; assert their byte/hash invariance.
   Add a deterministic replay test after removing its owned preparation fixture
   directory; unchanged retained evidence must still validate, tampered evidence
   must fail, and the corresponding live preparation check must reject the
   missing directory. No install or measurement is needed for this boundary test.
5. Verify workflow syntax, changed action refs against official upstream if any,
   unchanged hard quick/weekly time limits and no retry/automatic calibration.

Package owners run the smallest existing focused specs and lint needed for their
changes. Stop on their first successful relevant batch; add checks only for a
failure or unresolved contract. Completed fixes must be committed and receive
fresh independent final review, including runtime/provenance and replay lanes,
before long measurements or broad CI. The prior docs review is not reusable.

After all intended fixes are committed and fresh final review passes, use the
actual final-head feature-push CI performance job as the one real quick paired
campaign. It must retain the exact candidate/selected ancestor, neutral runner,
frozen preparation receipts and report, within the existing 15-minute quick
bound. A fresh watcher monitors the hosted batch. Do not also run an equivalent
local timed campaign. The same final-head release job supplies Ruff and full
build validation; it does not publish packages on the feature branch.

Deterministic quick, fixed-reference weekly and maintenance path checks, plus
native/source-loading smoke checks, remain required before review. If the hosted
campaign cannot verify a required path, identify the gap and reassess one scoped
local fallback; do not repeat automatically. A weekly timing run is not a
default follow-up and would need a concrete unresolved requirement and its own
bounded plan within the existing 45-minute limit. Failed preparation, timeout,
regression or inconclusive timing is a disposition to diagnose and report,
not permission to retry until green or change budgets. This validation choice
requires no additional workflow action changes.

### Compatibility, intentional updates and recovery

This is a benchmark preparation/provenance migration that restores the calibrated
runtime; it is not a new calibration. It changes no application protocol, state,
schema, persisted data or deployed service. Historical evidence and old replay
remain attributable. Ordinary contributor Nix updates may proceed when Ruff
parity passes without moving this pinned measurement environment.

Updating the benchmark's Ruby/native/gem graph later requires its own reviewed
environment migration with measured evidence against the fixed reference and
an explicit decision about calibration applicability. Do not redefine identity
to ignore intended updates. The current repair neither moves the reference nor
changes allocation/timing budgets or historical calibration metadata.

No deployment or machine reservation is required. Reverting the fix restores
the known environment rejection; keep source/input evidence rather than removing
guards. Preserve original failure artifacts alongside new results. CI-fix
integration into HaveAPI `master` is authorized by the user's subsequent
"merge it when you're done", conditional on accepted remediation and hosted
verification. This approval authorizes no deployment or lifecycle action.

Primary source references: `.github/workflows/servers-ruby-performance.yml`;
`utils/performance_ci.rb:154-302`; `servers/ruby/benchmarks/endpoints.rb:192-211,
378-415`; `performance_compare.rb:14-19,80-160,310-382` in the same benchmarks
directory; `doc/performance.md`; original `performance_budgets.json` calibration
and weekly environment; this session's `performance-ci-diagnosis.md` and retained
failed run 40314732573 artifacts. No new measured result is claimed here.
