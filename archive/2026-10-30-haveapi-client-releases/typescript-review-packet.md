# TypeScript candidate final-review packet

Prepared by implementer3. Lead selects and assigns the retained independent
reviewer; this packet does not claim review completion or merge readiness.

## Scope and exact range

Requested package: refresh vpsAdmin TypeScript SDK using the exact HaveAPI 0.32
candidate and accepted full-fixture schema, making a minor release only for
meaningful generated API/type/runtime changes. Preserve runtime 0.30.2 and all
exact-source/full-fixture refusals. No default integration, tag, publication,
publisher configuration, production API mutation or deployment is authorized.

- Repository: `vpsfreecz/vpsadmin-typescript-client`, target `main`.
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/vpsadmin-typescript-client`.
- Branch: `2026-10-30-haveapi-client-releases`.
- Fresh fetched default/base: `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`.
- Final committed head: `55e03a0e0a57533f0572f6f4856af33035472408`.
- Complete series (one commit):
  `55e03a0e0a57533f0572f6f4856af33035472408 Refresh offline generation for HaveAPI 0.32`.
- Worktree/index clean. Comparison captured using `dev-session worktree capture-comparison`.
- Full series/diff: `git log --reverse 60a1b5d..55e03a0` and
  `git diff 60a1b5d..55e03a0` in this worktree.
- No obsolete branches/approaches, fixup commits or superseded pin updates in
  this series. **No migrations** were created, changed, merged, released,
  deployed or externally consumed by this package. Exporter provenance retains
  existing upstream plugin migration inventory as input evidence only.

Plan/design: [plan](plan.md), [design](design.md). Live coordination state belongs
to the lead. Detailed baseline/input evidence: [preparation](typescript-preparation.md).

## Implementation and classification

- Pin candidate `f0465630595b4fd120561337b3d1d7fa96cbe221`, accepted unchanged
  full-fixture schema and refreshed provenance/exporter lock.
- Add exact dev-only Prettier 3.9.10 to package/lock/toolchain and pass its local
  executable explicitly to the Ruby generator. Preserve all existing source
  revision/cleanliness/shared identity/schema/provenance/tooling hash refusals.
- Extend source-refusal test to verify local formatter selection despite an
  invalid inherited `PRETTIER`; existing dirty/untracked/preloaded shared-source
  refusal cases remain and passed.
- Regenerate entire owned tree with formatter provenance in the manifest.
- Apply lead-written focused development-guide correction; no release prose
  because no release qualifies.

**No release; version remains 0.1.1.** All 674 generated TypeScript files exactly
equal the prior released source after running the pinned formatter with the
candidate's packaged config. Inventory unchanged (zero additions/removals),
coverage unchanged, API schema byte-identical. No generated public contract or
runtime behavior change. Exhaustive comparison included literal-bearing files,
not a whitespace-only heuristic. Default and actual last npm release baseline
are reconciled in preparation evidence. Lead accepted the provisional skip,
subject to independent final scope/history review.

Raw diff: **684 files, +57548/-19317**.
Generated portion: **675 files, +57468/-19275** (674 TypeScript files plus
ownership manifest). Remaining nine files: **+80/-42**, including generated npm
lock and exporter provenance/lock metadata. No handwritten subsystem expansion.

One logical commit keeps generator source and tooling pins, their hash-bound
inputs, and manifest/output aligned. Reverting it restores the prior complete
generation contract. Separate intermediate pins would add transient input
states without a release/consumer boundary. The final source/schema/tooling/
generated stream appears exactly once; there are no repeated updates requiring
consolidation. Please independently assess this split and whole-series history.

## Ownership and compatibility

HaveAPI owns the generator, shared schema helper and packaged formatting config.
SDK source helper loads and verifies exact candidate Ruby and TypeScript paths;
it uses stdlib only, without installing or reusing HaveAPI's component bundles.
SDK owns its dev formatter selection, saved inputs, public package metadata and
handwritten entry point. Generated files remain exclusively generator-owned.

Runtime consumer is exact npm `haveapi-client` 0.30.2, verified through package
peer/dev dependencies and strict consumer checks. No runtime dependency changed.
No database/persisted format/node protocol or coordinated fleet upgrade. Restoring
the previous complete source/generated/pin set restores prior generation; client
rollback cannot undo server actions. Live server permissions continue to apply.

Source-based preparation is allowed. Candidate-to-final release correspondence,
HaveAPI's retained package/extracted smoke checks, and rebind/regeneration if
final HaveAPI SHA changes remain lead-owned cross-package gates. No current
candidate evidence is being relabelled as final published evidence.

## Documentation and checks

Owning durable doc: `docs/development.md`, linked from existing README. It names
Prettier, explains exact local selection and packaged config, preserves source
refusals and clarifies that consumers require neither Ruby nor Prettier.
Lead supplied final prose after its user-facing writing pass. Release docs and
README were read and remain accurate for unchanged 0.1.1 installation/runtime.

Quick checks passed on final source contents before commit (only docs were then
changed using lead prose; logical tested code/input/generated bytes unchanged):

- `./tools/regenerate --haveapi-source <frozen-haveapi>` then same `--check`:
  passed, fresh watcher about 27 seconds;
  [exact commands](typescript-generation-command.sh),
  [log](typescript-generation-fixed.log).
- `npm ci --ignore-scripts --no-audit --no-fund`;
  `HAVEAPI_SOURCE=<frozen-haveapi> node --test test/regeneration/sources.test.mjs`;
  `npm run build`; `npm run typecheck`; `npm run typecheck:consumer`; `npm test`:
  all passed, source regression 1/1, unit/release suite 10/10, about 42.7 seconds;
  [exact batch](typescript-quick-command.sh), [log](typescript-quick.log).
- Exhaustive formatted-release equivalence and inventory comparison: 674/674,
  zero additions/removals, unchanged coverage.
- `git diff --check`: passed.
- No repository AGENTS.md, hook framework or configured hooksPath exists; no
  expected hook was bypassed. Commit ran inside the pinned Nix environment.

Suggested review classification: medium for bounded regeneration tooling and
source/provenance correspondence. General, architecture/repetition and
scope/proportionality lanes apply; risk/compatibility lane can check source
selection boundary and unchanged generated/runtime contracts. Lead owns final
selection/assignment; do not override retained reviewer settings. Explicit
whole-branch history, no-migrations and stream-consolidation conclusions required.

Longer/package verification has **not** started. After review, use
[package command](typescript-package-command.sh) through a fresh watcher. It
builds, packs without scripts, validates the retained archive in a disposable
consumer, creates its receipt and verifies that same archive. It does not publish.
Retain tarball/receipt as build-only 0.1.1 artifacts; never publish this unchanged
already released version. Feature push automatically starts release.yml package
validation, so push is held until review to preserve sequencing; no default
integration or tag is proposed.
