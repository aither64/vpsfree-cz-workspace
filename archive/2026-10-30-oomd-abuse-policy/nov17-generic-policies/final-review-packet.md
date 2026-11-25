# Generic incident policies: combined final source review

Status: independent final source review COMPLETE with no findings; see
[accepted result](final-review-result.md). The original review input follows.

Status at assignment: RELEASED for independent final source review. All eight intended
repository deliverables are committed, clean and have passing quick checks.
Root verified exact heads and clean source/index again before release. The React
handoff additionally proves the complete consolidated tree equals its checked
preconsolidation tree, with only accepted documentation differences from the
actual preview. Source/check acceptance does not pre-judge independent review.
New long integration/package/runtime work remains held until findings are resolved.

Session: `2026-10-30-oomd-abuse-policy`. Workspace:
`/home/aither/workspace/ai/vpsfree.cz`. Worktrees are under
`worktrees/2026-10-30-oomd-abuse-policy/<repository>`; records are under
`work/2026-10-30-oomd-abuse-policy/`.

## Requested result and scope

The latest user decisions at the top of [plan.md](../plan.md) and
[design.md](../design.md) supersede the older fixed-policy and dynamic-threshold
iterations retained further down those records. Review the final behavior against
those decisions, not against an abandoned intermediate design:

- Site Ruby configuration owns arbitrary policies. One format declares limits
  and an optional `applies_if` hook. Several policies may match one incident.
  Policy keys remain runtime strings, without per-key UI or SDK implementations.
- Evaluate applicability only when an incident is successfully created. Persist
  membership, results and relevant snapshots. Reads, retries and later policy
  changes never rerun selectors or reclassify old incidents.
- Counts and history use saved membership. Current summaries use current declared
  limits and deterministic overrides. Preserve authorization, owner epochs,
  source deduplication, new-event eligibility and shared physical-stop safeguards.
  Several eligible policies may share one physical Stop chain.
- Move full details into a legacy PHP Incidents sidebar page and a React VPS
  Incidents tab. The overview and lists show concise reached-threshold warnings.
  Per-policy nullable limit overrides and shared shutdown permission are separate
  forms. Accepted-write verification failures remain uncertain.
- Send one ordinary source email with its saved matching summaries. Aggregate
  action mail uses the saved base limits plus current overrides, mode and shared
  permission. Live summary limits may therefore differ after a declaration edit.
  Preserve contributor snapshots, owner privacy and confirmed-stop semantics.
- Use the established card style and the root-approved English/Czech text. The
  user explicitly requested older HTML styling in separate commits from the new
  incident mail; backend password recovery and site older HTML remain separate.
- Consolidate the development schema into the original migration. The user
  confirmed no external migration consumers and permitted one later disposable
  demo reset/reseed. This is not a supported upgrade from abandoned demo schemas.

Retain the established default 5 incidents/7 days warning and 10/30 days stop,
observe default, new incident after the 24-hour physical-stop cooldown, and count
expiry recovery. No burst rule, quiet-period latch, frontend enforcement, arbitrary
action engine, new BFF transport, policy editor, node protocol change, hot reload
or production policy activation is requested. No default integration, registry
release, production KB publication or session lifecycle action is authorized.

This is a large change across public contracts and two UIs. The final backend
range has 87 paths (+6463/-217); site templates have 57 (+1529/-294). Client
diffstats include generated schemas and resources and must be assessed separately
from handwritten tests and prose. Work spans prior October/November iterations;
the current generic contract and mail/UI revision is the November 17 work.
Preserved history and elapsed time are context, not evidence that scope growth
was justified. Start review with proportionality and identify any mechanism not
needed by the user decisions above.

## Reviewer and required conclusions

Overall risk: **high**, because this changes persisted membership/actions, schema,
tenant-visible history, stop execution, public API/SDK contracts, trusted policy
configuration and update/recovery ordering.

Select retained independent `reviewer0`, saved `gpt-6.1-sol`, `xhigh`, `read_only`,
after verifying the live same-session roster. Do not override its settings or
spawn nested reviewers. Read `mandatory-change-review/SKILL.md` and all four
references: general, architecture/repetition, scope/proportionality and
risk/compatibility. Inspect repository instructions and actual complete diffs and
series directly. This packet supplies evidence, not a required conclusion.

Return findings by severity with concrete paths and lines, then explicit
conclusions on scope, whole-branch history, repeated update streams, migration
lineage, documentation placement/preservation, and compatibility/recovery. State
"no migrations" for each applicable repository. Do not run long checks or edit
source. Root routes fixes to their retained implementation owners and uses
focused inspection/checks for direct narrow fixes; another full review is not an
automatic consequence of a narrow remediation.

## Exact source ranges

Every range includes all commits from its stated base, not just the latest fix.
Use `git log --reverse BASE..HEAD` and `git diff BASE HEAD`, and compare the merge
base where relevant. The live worktrees for all eight completed packages were
independently checked clean by root during packet preparation.

| Repository | Base | Head | Tree / source packet |
| --- | --- | --- | --- |
| vpsadmin | `537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02` | `ee9025a8c99f3714d483daed0a6f028520594fbc` | `d4e44289ae0ea1c7fbfb6b00c31eca914d0f4c10`; [G1 packet](g1/packet.md) |
| vpsadmin-webui | `88ac13b89d6421c914cd57e18153de1fee6fc7b7` | `d26cfea0b7e993bc40a9a987c9e13dc78d552080` | `63fc1020f30f8d2c0f96dcf59bd30cde6a27608b`; [G2 packet](../react-generic-nov17/final-review-packet.md) |
| vpsfree-notification-templates | `2cfd218d9152888feea4109f064459078ea9f76e` | `125f132a4c45ea8e8dbf6c392c7ca5f96e15a508` | `092c3638f123f1c275f6c48132bd58d344f9a1a4`; [mail packet](../nov17-mail-copy-rules/g-mail/review.md), [older HTML packet](../nov17-html-uniformity/packet.md) |
| vpsadmin-go-client | `af9a819ca35f6de5556092679b4df7cb72e7aa89` | `bd0d1d2f548c128f4fbc8657679450b7f998e181` | `91f32aa03288066271f8ed9f79045260d1c57573`; [G3](../owner3-g3-delivery.md) |
| vpsadmin-rust-client | `823a4f8450fce4947310fc81bcdebdca91d9ffae` | `e34ef441468b3e7579719ceb68d1b0b2cce8d101` | `49af7ad097d468d8b1717ddac1ef5a5557fe46fd`; [G3](../owner3-g3-delivery.md) |
| vpsadmin-typescript-client | `2da950a98fa13468b36d03b13fb5e81cca206e0e` | `3cb7cf838a607bbafab207307e11626e57cdec8c` | `a227d98471882fb49bf2464df1dfdea05202cda4`; [G3](../owner3-g3-delivery.md) |
| vpsfree-cz-configuration | `15e3b9af90276e41d19e6a33477add58e5f9a8c9` | `1efed32a70a91e8705be2ceeb6b7dac4ad19e10c` | `457391d83177a8ab7a5276078c2ba8ef15b4d6f5`; [current-default receipt](../nov18-g3-client-sync/config-current-default.json) |
| vpsfree-kb-contracts | `ce2c8cd9358c3636e5d39343e595df813a0b197f` | `4be305f13fcd15ba79c5c7bde95a277a6164f442` | `4aadfe21daaa3983406997a3b352dc80fc06e1ed`; [KB packet](../kb-source-evidence/g-kb-source/review.md) |

The HaveAPI generator worktree remains clean at its unchanged initial base
`1ef9b204ba45bb261d3334be5c555cc1856b713b`: no generator change belongs to this
delivery. The separately registered historical API diagnostic branch is retained
as diagnostic evidence, not folded into the product feature or released for new
execution by this review. Its prior review and unresolved operation boundaries
remain in the existing November 14 records.

## Complete series, consolidation and migration provenance

Backend has four purposes: `e50b25b77b73a2ea0123731a673ce7baa3da9ea4`
transactional fixture/isolation docs; `83618d31618f3beb22c726c0b2a5a0f2505e265e`
final backend/schema/API/incident mail; `e87188f8e88e6d06b32cb82bd3ccce4ab8e58e20`
PHP/browser fixture; and final `ee9025a8` older password-recovery HTML. The saved
association, schema, API and mail snapshot contract are one backend behavior
purpose. Fixture and older HTML are independent. See the complete
[series](g1/ci-coverage-final-series.txt), [diff](g1/ci-coverage-complete-final.diff)
and [range comparison](g1/ci-coverage-final-range-diff.txt).

Only `20261030180000_add_incident_escalation.rb` is introduced after the exact
predecessor `20261006120000_add_network_enabled.rb`. The obsolete additive
`20261115120000` is absent from every reconstructed commit. Old schema revisions
were used in disposable tests and the retained development demonstration; they
were not merged, released or externally consumed. The user explicitly accepted
resetting that disposable demo rather than supporting migration from those
iterations. The old demo is unchanged. Fresh core up/down and focused migration
evidence are in G1's packet. There are no migrations in the other seven ranges.

The accepted exported backend `5aa1df7b51fc22c9d35a2d7f6aec889afa54b303` is
preserved. Its successor `ee9025a8` changes only two spec paths: six endpoint
inventory entries and three lines that actually request registry Show and compare
its metadata. Every other tracked path/mode/blob and exporter input is unchanged.
The follow-up is folded into the backend purpose. The original failed CI and
targeted correction are retained in [the final receipt](g1/ci-coverage-final-receipt.json).
SDK/export/KB inputs remain literally `5aa1`; they are not relabelled or regenerated.
Backend's cached/fetched default `c51d8a41` contains four pre-existing commits
beyond base537b. No rebase or default integration is part of this source review;
later readiness must reconcile the actual default and retest affected inputs.

Site templates have three purposes: `e3aae717cd429b30b198f7d34c2da62fb180add4`
incident mail; `deafdfa953bc5a3ea7f230199b40cb32a6778064` independent authoring
guidance; and `125f132a` older HTML. The H patch remains byte-equal to the preserved
older-HTML change. The final tree equals the checked source, with all old M/H and
published refs retained. No dependency update stream or migration is introduced.

G3's exact full lists and old/new/preservation data are in
[final-history.json](../nov18-g3-client-sync/final-history.json):

- Go: `35e679087674bb39fefdfd403cd6f0595fe03e41` generated snapshot,
  `bd0d1d2f548c128f4fbc8657679450b7f998e181` consumer contract/tests/docs.
- Rust: `23b1200bb5a8f0486597ec9a5edc71e6931943fd` generated snapshot,
  `e34ef441468b3e7579719ceb68d1b0b2cce8d101` consumer contract/tests/docs.
- TypeScript: `544731e400c8bfd7a782064397e6be70890e76b5` generated snapshot,
  `d9d6d53dd0a2fb3b736b912123731bc78d69289e` consumer contract/tests/docs,
  `3cb7cf838a607bbafab207307e11626e57cdec8c` portable development artifact.
- Configuration: `1efed32a70a91e8705be2ceeb6b7dac4ad19e10c`, two-file declaration
  and owning reference. Rebased from the accepted old base onto fresh15e3 with
  identical owned bytes/patch ID; upstream pins are inherited, not G3 changes.

All obsolete generated streams are folded into the final snapshots. Go/Rust trees
equal their checked preconsolidation trees; TS differs only in replaced support
artifacts. Old supported source/artifact refs remain preserved, including the
published TS prior artifact. No generator, formatter, runtime or version bump is
introduced by G3. Nine actual preservation refs are bound in its final receipt.

KB's recorded full series is `d3af1d16cf477b3f0706a900483251586183732b`,
`f97785c2c265172a4c78893e0673034fde56e4dd`,
`cb7825245ea786fb0f51c469d1a7dc5c6a1ececc`,
`91d349c8da837d26a45db426c154fe24a988c9e4`, then `4be305f1`.
The first three are already merged into defaultcb782 and preserved literally.
Independent runtime91d is unchanged and patch-equal. Only the unmerged repeated
five-file pin/obsolete fixture/source stream was folded into the final ten-path
purpose. The final tree and 262 checked inputs equal the tested48c06078 source.
Inspect the full and unmerged range comparisons in the KB packet; do not treat
development publication alone as a reason to retain redundant input updates.

React's final three purposes are `731c4fcd764c0eae4e1281e54119698fd4e81050`
portable SDK dependency, `c2f612c675beb3f32d619dc0d97ea3c0261fe0ae` generic
application, and `d26cfea0b7e993bc40a9a987c9e13dc78d552080` historical/current
evidence. The complete range has72paths (+2981/-61). [Full diff](../react-generic-nov17/final.diff),
[prior-range comparison](../react-generic-nov17/prior-to-final.range-diff.txt) and
[consolidation proof](../react-generic-nov17/final-history-equivalence.json) retain
all three old refs. Two E2E-only history conflicts were resolved to the exact
preserved final bytes; whole trees match. The final series introduces no obsolete
selected-policy/callback source or repeated SDK input stream. Root independently
compared all2838preview paths (including expected deletions); only seven accepted
prose files differ. All runtime/test/dependency paths match, and the eight returned
prose files plus four PNGs match after the approved link/directory move.

## Contract inputs and compatibility

Two fresh fixture exports at exact5aa1 are byte-identical: schema SHA256
`997045d31c26e2dde0a9ddcadd842ce15e767b52b006bdb02731e5eb08de4f00`, provenance
`869db77e2f5a8dd29efb3cea0f854664bd9a441d21cee4d62d63d315e861c58d`, exporter lock
`2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0`.
The raw application inventory is154 resources/527 actions/8915 parameters.
Rust includes the existing authentication resource/five actions in155/532.
Generated file counts are Go693, Rust697 and TS686, each adding9 and deleting0.

React consumes the independently downloaded 345015-byte immutable HTTPS archive
at TS3cb7, packed fromd9d6, SHA256
`b00e1e457dec33419505a286cf3dd5c937aa982ab4b3e7e6fca1b0fdf47dee20`.
Its installed bytes/provenance and ordinary npm lock match; BFF dependencies are
unchanged. Registry publication remains mandatory before React integration.
Go retains its documented scalar/null limitation; Rust and TS retain optional/null
semantics. Capability checks and actual backend authorization remain required.

The backend owns the registry, membership, counts, privacy and effects. PHP,
React, the three SDKs, site declaration/templates and KB fixture are actual
consumers. Review their selected revisions and code, not a guessed consumer list.
New calls require the final API or capability gating. Trusted declaration loading
must precede new events; old processes do not hot-reload the file. Preserve
mode ceilings, shared exemption, current ownership checks and reconciliation of
already queued/uncertain effects. An older application is not assumed to load the
new feature schema; rollback ordering/recovery limits belong in the backend and
configuration reference. No new coordinated node protocol rollout is required.

KB pins literal5aa1 in all five fields; other11 lock nodes and all edges are
unchanged. Its screenshot-only fixture now uses declared limits5/10, with the
same key/adapter/labels/templates/injection. Canonical runtime/media is pending
for the existing three bilingual concepts: getting-started/vps-list,
restore-backups/playground-vps-list and getting-started/vps-details. Review or
regenerate only actual impact; list crops hide the sidebar and zero fixtures
should not show the threshold warning. Source-check success is not media proof.

The two local unmanaged incident article candidates are final, hash-bound review
inputs in `owner3-runtime-policy-evidence/incidents-{cs,en}-candidate.txt`, not
uncommitted application source or staged production wiki edits. Their hashes are
CS `03d17bd0263d722a399601423a6251410becb7dc26d4e91a68dd56f723df6a6a` and
EN `1e7860fffcdb6a3a10ca9748853dc9e844c10d5855810a1e942e2eab1f41f80d`.
Each has one `vps.incidents.open` annotation and unchanged surrounding sections.
Include manual instruction/binding and factual review; publication stays separate.

## Verification evidence and limits

Do not add batch counts into an invented unique total. Reuse each pass only for
its recorded inputs, including the retained AST/token equivalence of required
hook formatting and exact generated/dependency manifests.

- G1: earlier13 engine and62 regression passes, final12 focused and3 original
  migration passes, core schema up/down, saved-base builtin/site1+1, endpoint
  inventory pass and final discovery1pass. Scoped lint/static/locales and all
  normal reconstruction hooks passed. Exact failures/diagnoses stay in G1.
- Mail:54builtin+19site examples, affected saved-base1+1, template check/lint,
  site check77templates/393files and exact derivation inputs. Root accepted78
  rendered previews and6screenshots. Earlier H rendering/scroll evidence stays
  in the separate H packet; hook newline formatting is AST-equal.
- PHP:10tests/67assertions, locales/static checks and scoped synthetic views;
  final required formatter changes in five files are PHP-token-equivalent.
  Real end-to-end browser execution remains postreview work.
- G3: TS generation/build/type/consumer/package checks and18tests; Go4projection
  and9native tests; Rust quick checks plus exact automatic CI44211967472 with
  all4jobs passing, pinned and1.95 default/blocking matrices8tests each,
  provenance7/mode, refusal10, docs/package708files. Real-server tests are
  explicitly ignored; no duplicate local matrix or re-export ran.
- Configuration: exact pure parser load, currentRuby3.4.12 syntax/scoped lint and
  normal hooks pass. Old extension/missing-gem failures remain distinguishable.
- KB: pinned `bin/check --allow-missing` passed with262 unchanged source inputs;
  exact selected pure parser loads the fixture. This includes source/Nix
  evaluation tests but no new runtime/build/capture campaign.
- React: full application types,12files/98tests, E2E core typing, lint/format,
  i18n/structure, docs/structural/component-contract/UI-string/mutation audits,
  build and prefetch passed. Two implemented synthetic flows passed and root
  viewed all four PNGs. Read the retained failure/continuation/input receipts,
  final prose return and final committed-source equality. Affected docs audit passed
  after the move (288documents/76requirements/268routes/75modules), scoped format
  passed82reviewed files, and diff-check passed. App/build/browser batches were
  not repeated for prose or history changes.

Exact successor backend CI was checked with bounded ordinary reads because the
runtime observer previously refused caller ownership before registration. No
replacement watcher or manual run was started. API44214920284 completed success, including all26topic jobs and the topic-coverage
job; main CI44214920366 completed success but its integration run steps were skipped,
so it is not integration-test coverage. Five other successor workflows passed.
Raw snapshots are under `g1/root-ci-*-status.json` and bind the exact successor
head/attempt and terminal conclusions. Original failed5aa1 API evidence is retained.

## Documentation routing and ownership

| Topic | Reader / class | Authoritative home | Evidence or remaining limit |
| --- | --- | --- | --- |
| Registry, saved membership, limits, actions, mail and recovery | Backend contributors/operators; reference | vpsadmin `docs/incident-escalation.md` | G1 source/specs; no new deployment claim |
| Export and client synchronization | Contributors; how-to | vpsadmin `docs/api-schema-export.md` | Two fresh identical exports and unchanged tool inputs |
| API/current-history/write uncertainty and UI workflow | WebUI contributors; reference | React API_CONTRACTS, WORKFLOWS, REQ-051 | Generated resource wiring and98tests; root final prose |
| SDK input and registry gate | WebUI maintainers; reference/how-to | React HAVEAPI_CLIENT and PACKAGING | Installed archive, lock/provenance and prefetch; release still required |
| SDK nullability and capabilities | SDK consumers; reference | Go README development section; Rust/TS docs/development.md | Actual generated fields and wire/type checks |
| Site declaration, activation and software recovery | Site operators; reference/operations | configuration `configs/vpsadmin/api/README.md` | Current parser/hooks; activation unexecuted |
| Member incident behavior/navigation | Members; how-to | Existing CS/EN incident article candidates | Root bilingual pass and one binding each; canonical publication pending |
| Screenshot fixture behavior | KB contributors; reference | KB `cluster/README.md` and existing runtime contract | Exact pinned parser/source check; no runtime/media claim |
| Mail authoring | Template maintainers; instructions | Site template AGENTS and backend reference | Separate guidance purpose, root copy/render pass |
| UI execution evidence | Contributors; dated record | Existing React work-log and screenshot home | Actual synthetic source limits; new files use docs/work-log/screenshots |
| Exact revisions, raw failures, histories and rollout | Session operators; execution records | This packet and linked owner packets/state | Preserve original records; no lifecycle or production authority |

Assess all seven documentation questions in the general lane. Preserve public
anchors, commands, warnings and recovery conditions; flag temporary rollout
state in lasting reference when it creates a real maintenance problem. Do not
expand into a historical backfill or optional polishing campaign.

Implementation/review-fix owners remain: backend1, React2, SDK/config3, PHP4,
mail/KB0. Architect0 retains design clarification. Root owns final writing,
acceptance, review invocation and approval-bound coordination.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
