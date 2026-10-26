# Final HaveAPI review packet

Status: final committed deliverable. All four intended units are committed,
quick checks pass, and the worktree is clean. Review before long integration tests.
Final head: `b85ec364057f536940d689b09e612512ffffaf82`.

## Requested result and scope

Remove repeated complete-description copies when deriving individual example
contexts; avoid Rust recursive normalization of unrelated description subtrees.
Introduce performance regression protection and a reproducible benchmark.
Preserve rendered output and request-local authorization, constructor ownership,
supplied-value normalization, subclass construction and adapter freshness.

Initiative: `2026-10-24-context-copy-performance-tests` in
`/home/aither/workspace/ai/vpsfree.cz`. Records: `plan.md`, `state.md`, `design.md`
in this directory. Repository/worktree:
`worktrees/2026-10-24-context-copy-performance-tests/haveapi`.
Target: HaveAPI `origin/master`; no merge approval or deployment is authorized.
Base: `39909094649b1d14a23f00615775ca7136acf4fd`.

## Contract and explicit limits

The constructor copies/freezes Hash/Array/String. Exact base Context derivations
share unchanged owned fields, copy only supplied changes, and remain frozen.
Other leaf objects and profile retain existing reference semantics; subclasses
retain their constructor path. No caller-supplied trust flags, request data cache
or rendered-output cache. Explicitly supplied resources/actions/samples still
cost proportional to their size; saved Rust IR resolution still scans actions.
No claim of universally linear rendering or impossible future regressions.

Rust must select from current authorized help, preserve mixed string/symbol key
collision semantics, full provider-description equality and credential ordering.
The shared private generator snapshot resolves SDK names and cannot authorize.

Owning components are HaveAPI Ruby server Context and optional Rust generator
documentation adapter. Actual in-repository consumers include server helpers,
templates, language renderers and Go/Rust bridges. The adapter remains usable
with duck-typed contexts. vpsAdmin consumes the framework, but downstream pins
and rollout are outside scope; no downstream configuration or SDK API changes.

No persistent schema, format, migration, seed, protocol, Nix option or dependency
pin changes. **No migrations**, none merged/released/deployed/externally consumed.
No feature deployment has occurred. Old/new workers may coexist; package rollback
needs no state conversion. Existing matching-generator version rules remain.

## Commit/history intent

Complete base-to-head series, in order:

1. `5003ded2a47db6b1637a3fef2fdd40474ea7de06` servers/ruby: share owned documentation context fields
2. `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c` clients/rust: normalize only selected documentation data
3. `de799b595d04e880d092b3e5ef47bce2f4587130` servers/ruby: guard documentation context copy complexity
4. `b85ec364057f536940d689b09e612512ffffaf82` servers/ruby: benchmark documentation rendering

Final diff: `haveapi-final.diff` in this directory, 13 files, 1,201 additions,
26 deletions. No superseded approaches or migrations were found in lead inventory;
all four units remain in the final tree. No dependency/pin/generated-update
stream exists. Please independently confirm these conclusions.

Four logical units: context fix with behavior specs; Rust normalization fix with
behavior/work specs; page/allocation regression specs and shared fixture; benchmark
tooling with Makefile and supporting developer docs. Fixture must be shared by
tests and benchmark. No repeated input/dependency/generated-update streams are
intended. Message-only amends are consolidated. Lead will attach complete series
and final diff before review; assess obsolete history and migration lineage
explicitly, including no migrations and no repeated streams when appropriate.

## Quick evidence and docs

- Context ownership/compatibility: 26 examples, zero failures; changed-file lint.
- Rust adapter behavior/work: 56 examples, zero failures; changed-file lint.
- Context/page performance plus auth filtering/profile mount: 19 examples, zero
  failures; changed-file lint. Normal commit hooks required for all commits.
- Baseline Context subprocess: all 3 new examples fail, including real HTML.
- Baseline adapter subprocess: all 8 work examples fail; candidate equal-work
  assertions pass. These do not mutate candidate files or checkouts.
- Allocation calibration: 40 derivations, 8/128 resources, profile candidate
  200/200 vs baseline 12,560/151,760; small sample candidate 560/560.
- Benchmark dynamic smoke: both shapes, size 1, two trials/three iterations,
  status 200, stable 59,886-byte HTML digest. Optional Rust: all four adapter
  lanes return code, both variants in status-200 HTML, stable digests. Restricted
  custom/member case and invalid-option JSON/exit checks pass. Syntax and changed
  file lint pass. Baseline source selection smoke loads the exported exact base.

Relevant artifacts: `package-c-notes.md`, `package-c-allocation-calibration.json`,
`package-c-baseline.json`, `package-b-handoff.md`, `package-b-baseline-specs.log`.
Permanent docs: HaveAPI `doc/client-examples.md`,
`doc/agent-instructions/development.md`, `clients/rust/docs/documentation.md`.
Check placement and fidelity to final code, including remaining costs.

Long suites and before/after benchmark campaigns await final review. CI Ruby
3.2/3.3/3.4 allocation behavior has not yet been inspected. No production latency
or production improvement baseline exists; reported incident and all current
measurements are local.

## Review policy

Overall risk high because immutable sharing and authorized subtree selection
touch request isolation and authorization evidence, despite no intentional
authorization behavior change. Lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Read mandatory-change-review SKILL.md
and all four lane references in full. Retained independent reviewer0 has saved
model `gpt-6.1-sol`, effort `xhigh`, read-only role; no fallback/override intended.
Perform review directly without nested agents; report findings by severity and
explicit full-history/migration conclusions. Do not run long suites, edit source,
integrate or deploy. Narrow remediation and affected-lane rerun policy applies.
