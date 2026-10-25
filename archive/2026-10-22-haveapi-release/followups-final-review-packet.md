# Committed follow-up review packet

Prepared for lead assignment to retained reviewer0; no review has been performed
by this export. Review the complete six-part series and final diff. The completed
0.30.0 release is outside the new change range and remains immutable.

Repository/worktree: HaveAPI,
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-followups`.
Branch: `2026-10-22-haveapi-release-followups`.

- Base: `b64fb25bea8d8222fb3263b99956c0b61438a859`
- Head: `090a188cb4ef3477324718627f4ae3415d1c0975`
- Tree: `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`
- Scope: **six commits, 45 unique paths, no migrations**.
- Final complete binary diff SHA-256:
  `c10184dfaf126e9f6bfcef210ac5f9f3a8ffa9decba55b6d325bd289967d5b41`.

Requested outcome: reliable bounded confirmation of accepted registry uploads,
removal of obsolete JS documentation dependencies and helper/circular-import
warnings without changing SDK behavior, and explicit Rust generator Fiddle
dependency plus scoped naming allowances preserving existing public names.
The user's follow-up scope is development-branch fixes. The user subsequently
said “well commit the fixes”; the lead approved this exact six-purpose split.
No additional release, version bump, default integration, downstream
vpsadmin-rust-client publication or registry mutation is authorized.

## Whole series and boundaries

| Order | Commit | Purpose |
| --- | --- | --- |
| 1 | `cbf6a3f0b34f15e2bb4224872b46c423d7d02313` | Fiddle runtime dependency, locked resolution, libffi in both owning shells, retained-package verification/smoke |
| 2 | `431d7ffed098c7403d3d0555b3b93c4a3ab8b3e3` | Scoped generated resource naming lint and focused compiler mode |
| 3 | `01a30a39cdfc0d81e2eca62dcce912c165d891fa` | Maintained JSDoc/build dependencies and bundled ES5 helpers |
| 4 | `412511176d7f54a96d48bc0995b202f335d1be4f` | Callback/async resource graph correction and dependent tests/config/docs |
| 5 | `c424c579a314593e25cfe661374caafb9ab78a4c` | Strict bounded registry observation and recovery guidance |
| 6 | `090a188cb4ef3477324718627f4ae3415d1c0975` | One cumulative generated JS bundle/declaration update |

Read [full history](followups-final-history.txt),
[series/path/hunk map](followups-final-series.json),
[complete final diff](followups-final.diff),
[name-status](followups-final-name-status.txt) and
[stat](followups-final-stat.txt). Individual patches are
`followups-final-commit-1.patch` through `followups-final-commit-6.patch`.

The [accepted hunk plan](followups-commit-plan.md) separates mixed release-spec
and release-guide hunks between R1 dependency and P1; the Rust guide between
dependency and naming; JS graph sentences and the three-facade isolated emit
config accompany J2. J1's Rollup factory precedes the graph test that consumes
it. Runtime dependency, native prerequisite and retained activation assertions
belong together; naming is independently reviewable. No source version commit
was added. Assess the complete history independently for obsolete approaches.

Three update streams are consolidated once each:

- Fiddle gemspec/component lock resolves **1.1.8**, requirement `~> 1.1`,
  `>= 1.1.8`; native input and retained activation checks in commit 1.
- JS npm manifest/lock selects JSDoc **4.0.5**, tslib **2.8.1**, node-resolve
  **16.0.3**, Acorn **8.19.0**; TypeScript **5.9.3** retained, in commit 3.
- Eight final JS outputs, including new `client_invocation.d.ts` and
  `async/resource_model.d.ts`, introduced cumulatively in commit 6 after both
  authored JS purposes. Exactly one product build, no hand-edited output.

[Exact streams](followups-final-streams.json) bind files, pins, hashes and commits.
No intermediate dependency/generated revisions remain in this new series.
There is no database, persistent-format, protocol or SDK naming migration;
[migration inventory](followups-final-no-migrations.json) records the empty
inventory and immutable released predecessor. No follow-up migration was merged,
released, deployed or externally consumed.

## Contracts, ownership and review focus

Proposed risk: **high**, because registry observations gate irreversible package
uploads and SDK loader/type/class contracts must remain compatible. Proposed
lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Lead retains assignment and risk selection. Retained reviewer0 was verified in
same-session roster revision 34 as ready, review-purpose, read-only,
`gpt-6.1-sol` / `xhigh`; authored none of these changes. Do not substitute this
packet for independent conclusions. Read the mandatory review skill and all
selected lane references.

- Release-tool owner is `utils/release`: CLI and workflow invoke publisher and
  artifact/smoke helpers; Makefile checks exercise the same helpers. RegistryQuery
  owns GET transport/deadlines, Publisher owns strict package validation and
  invocation-local positive Python staging evidence. Check fixed HTTPS hosts/
  exact-version endpoints, no redirects/credential propagation, fatal conflicts,
  60-second transient preflight and 600-second confirmations, absolute deadlines,
  Retry-After/backoff, shared final deadline and zero repeated uploads. Normal
  environment-proxy compatibility is intentional. A cache-distinct GET is a
  mitigation, not proof of origin freshness. One complete response is required
  for final success; union evidence is staging-only.
- JS callback/async SDK owns its distributed UMD and public/deep declarations.
  Entry imports the callback installer; it must retain lookup on the original
  Action completion function. Existing async resource facades re-export one
  model and must preserve constructor identity, private nominal types, local
  association references, immutable submitted snapshots, save/list semantics,
  nonthenability and initialization timing. Existing internal async callers
  continue through those facades. No auth/path/protocol/timing change intended.
- JS gulp and graph checks share one Rollup input factory. ES5 helpers are
  bundled with their license; consumers must not need tslib/build dependencies.
  No Rollup warning filtering or context change. Maintained JSDoc deliberately
  changes template appearance, while API content/navigation and documented old
  Action anchor remain. Fixed alias processing rejects collisions/missing target.
- Rust generator owns its runtime gemspec and generated templates. Loading the
  generator already uses Fiddle for atomic exchange. Explicit native dependency
  affects future installations; retained smoke rejects default-gem fallback.
  Generated double-underscore names/routes remain exactly stable. Only owning
  generated module declarations/accessors get naming allowances; no crate-wide
  suppression, Cargo dependency/MSRV change or regeneration of existing clients.
  The separate vpsadmin-rust-client repository has no source/pin/publication
  change in this range.

No persistent-state conversion or deployment order is needed. Old generated
clients remain usable; future generated bytes/provenance change normally.
Rollback of the development changes requires no state migration. The original
tagged release workflow/artifacts remain the recovery authority for 0.30.0;
these fixes cannot retrofit its tagged source.

## Documentation and acceptance evidence

Design/decisions: [frozen brief](release-followups-design.md), session
`plan.md`, `state.md`; lead owns tracking. Project explanations and procedures
changed in `doc/agent-instructions/releases.md`,
`clients/rust/docs/releasing.md`, `clients/js/test/README.md`. Lead prose passes
and final release-guide wrap are preserved. JS graph relocation changes no user
behavior; tests and owning build guide carry its maintenance constraints.

Quick checks were completed before committing, as accepted by lead:

- P1: root tools-only Nix `make release-check`; `make release-test`:
  **170 Ruby, 6 Python passed**; seven Ruby files syntax/style clean.
  Deterministic fake clock/transport; no real registry/proxy/listener/upload.
  [Receipt and commands](followups-p1-receipt.md).
- J1/J2: client-js shell source typecheck, single build, compatibility
  **53/0**, async **39/0**, resources **11/0**, public/deep declarations,
  ES5/graph/loaders/helpers and real JSDoc pages/old anchor passed.
  [J1 receipt](followups-j1-receipt.md), [J2 receipt](followups-j2-receipt.md).
- R1: isolated frozen Fiddle setup **exit 0, 21.80 seconds**; nondefault 1.1.8;
  `make test-rust-unit` **79/0**; five Ruby files style clean.
  [Receipt](r1-rust-warnings-receipt.md).

Fixture-only JS corrections preceded the final compatibility pass; no product
rebuild followed. One later J2 whitespace correction removed only one extra EOF
LF in new `client_invocation.ts`, explicitly accepted by lead. Its
[original/corrected SHA overlay](followups-commit-whitespace-correction.json)
is the sole exception to equality with the 45 accepted yield hashes: all other
**44 match**, and all eight generated hashes match. No semantics or docs changed.
No broad quick-suite repeat was run during commits.

Actual normal hooks passed for every original commit and every final reworded
commit. First two original messages emitted width warnings; message-only
cleanup ran real hooks for all six. [Final hook log](followups-reword-hooks.log)
has six pre-commit and six commit-msg passes, zero message warnings. Subjects
are at most 60 characters, bodies at most 72. Each original/final commit tree
and full raw diff is identical: [rewrite map](followups-reword-map.json),
[range diff](followups-final-range-diff.txt). Original logs and failure record
for the EOF staging check are preserved.

Final [source/blob hash proof](followups-final-source-proof.json) and
[base-plus-inventory tree reconstruction](followups-final-tree-equivalence.json)
prove the committed tree exactly matches the accepted files plus EOF overlay.
Whole-range whitespace is clean. Tracked source and index are clean. All 302
preexisting untracked cache files remain byte-identical and unstaged:
[cache proof](followups-final-cache-proof.json). They are not source changes.

## Pending work and handoff

Independent final review is pending. Do not start long tests/builds until the
lead accepts its report. The architect's
[post-review verification plan](release-followups-verification-plan.md) is
unexecuted. It covers final exact-head installed npm/Rust smoke, full build/test,
and actual development/MSRV naming lint. Pure mocked compiler tests do not claim
an actual compiler pass. Real retained Fiddle activation and clean installed
package checks remain pending.

Two verification planning details remain visible: the plan's literal
`git status --porcelain` empty assertion must account for the deliberately
preserved, known cache-only untracked files; no cleanup or exclusion change was
performed here. The Rust runner removes its temporary generated input tree on
exit, so current logs cannot claim retained Cargo.lock/schema/tree evidence.
Lead/architect own any later decision about that evidence boundary.

Source/Git/hooks ownership yielded command-free to lead. No feature push, default
integration, tag/version/release action, registry write, application build,
long verification, cache cleanup or lifecycle action occurred in this commit
package. Nix tool environment realization and required hooks were the only
execution beyond staging/commits/evidence exports.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
