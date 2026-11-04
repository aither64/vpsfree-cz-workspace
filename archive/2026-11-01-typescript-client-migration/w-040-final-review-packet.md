# Released 0.4 client and current-main migration: final review packet

Candidate: `db90da33765090f34d74280aad273c4dbfc98090`, tree
`93203cc0d5ef40d0425230abb9cf985a69086ea7`, parent
`9f01268a54f9251a8ed8fe435664b5dffac972a1`.
Base: current authoritative main `1c8478bceb3943645ec06ccde895ee4b0985873f`.
Repository/worktree: `vpsfreecz/vpsadmin-webui`,
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui`.
Session: `2026-11-01-typescript-client-migration`; existing plan/state/design remain
in this directory. The final tree is fully clean, index empty, with no Git
operation or active owned check. W explicitly returns its sole source/Git/index/
dependency-tree turn to lead; the source is frozen.

## Requested outcome and scope

The user authorized released 0.4 adoption, a semantic rebase onto current main,
and migration of old request usages introduced anywhere on newer main, followed
by review/tests and conditional WebUI integration. This is the whole existing
migration branch: 36 commits, 517 changed paths, 15263 insertions and 10075 deletions
relative to main. Inspect the entire series and final diff, not only its last
reconciliation commit. No new framework, backend/provider/generated-client edit,
production deployment or preview update is part of this candidate.

The architect-owned design section **New client release, current-main adaptation
and conditional integration**, W's original caller map
[w-040-migration-boundaries.md](w-040-migration-boundaries.md), and the original
[main diagnosis](w-040-main-request-diagnosis.json) bound this work. Main's
correction/lifecycle additions are combined semantically, including its
nonconflicting new callers. Earlier branch reviews do not certify this new range.

## Complete history and recovery

- [Complete new 36-commit series](w-040-final-series.json) includes literal new
  commit objects, all paths, author/date/message comparisons and tree bindings.
- [Full final diff](w-040-final.diff), [diffstat](w-040-final.diffstat), and
  [old/new range-diff](w-040-final.range-diff) are the review inputs.
- [Original 37 raw objects](w-040-before-rebase.json),
  [conflict dispositions](w-040-rebase-conflict-dispositions.json), and
  [final history/input proof](w-040-final-history-and-input-receipt.json) preserve
  the actual old and new ranges.

Old range: `63d484fc070dbee633d32624de545e834d483701`..
`4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e`. All 37 old objects remain literal.
All 35 retained commits preserve original authors, author dates and messages;
committer identities/dates reflect the ordinary rebase. Independent infrastructure,
users/settings, finance/content, network/DNS and VPS/storage domain stages remain
separate. Their substantive changes were preserved, not arbitrarily squashed.

The temporary archive/provenance/cache-adapter commit `167f8531` and superseded
registry-0.3 commit `4ed519b6` were removed from the new series. The **only** final
client manifest/lock/frontend-hash stream is introduced with generated bindings
in first commit `41919ba169131d6b8937cc54f6601ddf601e1caa`. All 36 new commits
select registry 0.4 and the same final npmDepsHash; no intermediate client pin is
retained. No new-series tree contains the obsolete archive/provenance files.
The preserved negative source-checker fixture `file:vendor/client.tgz` rejects a
substituted HaveAPI dependency; it is not a generated-client archive mode.

Current-main advisory migration, active recovery tests and all source remedies
are folded into their infrastructure owner
`786779a21c88cc40efa0c8e6e3c5cac34fd22686`. Neither the draft-only hook nor its
old tests is ever introduced in the new series. The active correction hook owns
recovery and the existing partial-result component. Later fixture commits retain
distinct canonical response/receipt, creation/assessment, relation and strict
whole-file adoption changes; they introduce no alternate client implementation,
compatibility shim or dependency stream. Documentation/evidence commits preserve
historical execution scopes. The final reconciliation commit contains current
contract documentation, the main advisory fixture/state assertions and strict
adoption metadata. The reviewer should assess these boundaries independently.

Exact deployed old4ed remains at
`refs/keep/2026-11-01-typescript-client-migration/released-040-pre-rebase-4ed519b6`.
Its preview remains running unchanged. It is **not** an ancestor of this semantic
successor, and no patch-equivalent/deployed-lineage integration claim is made.
A second ordinary recovery ref retains the exact checked pre-consolidation tree;
final tree equality is proven, without using write-tree for snapshots.

**No WebUI database/schema or persisted-format migrations.** The changed existing
`src/lib/api/migrations.ts` is a VPS migration API adapter, not a DB migration.
There is no intermediate persisted-state upgrade or rollback path to retain.

## Semantic and compatibility review priorities

The new-main eight-path disposition is in
[w-040-final-request-source-inspection-v2.json](w-040-final-request-source-inspection-v2.json).
Its 1139 production path hashes exactly match this committed candidate. The
fresh full scan finds zero old helper/type/module imports or aliases and zero
handmade advisory endpoint descriptors. New `securityAdvisoryMutations`, correction
and node-snapshot hooks, parent/child adapters, list/detail flows and admin API
orchestration use generated methods/descriptions through the existing policy.

Check authenticated generated root and object/action descriptions; allowed state
choices; all SIX child mutation capability/parameter checks before draft sync;
frozen expected_state and expected_content_revision; parent-before/after child
snapshots; exact rendered/fresh child identity; additions before removals; exact
revision read-back; accepted/completed/remaining progress; visible refusal and
no replay after uncertainty. Missing/replaced node deletion now fails visibly
before confirmation and sends no deletion. Timestamp precision, null/absence,
localized notes, published/retracted corrections and announcement boundaries remain.
Generated Delete returns an empty namespaced response; no async receipt is invented.

Backend `8225229aa0e3306f8b1723c5583969a33c64571c` or independently equivalent
live action/parameter capabilities is required for the new guards. API7 alone
is insufficient. Expected state remains optional non-null string in generated
types, so allowed-state enforcement is application policy. Older-backend missing
actions/parameters/choices must deny without dropping guards or writing. The
running preview API610 stays unchanged and is not a compatible test backend.

Intentional boundaries: one shared HaveAPI executor/policy, separate BFF/session/
OAuth, own configuration/build-info reads, legacy PHP session-timezone sync,
external Nominatim/download navigation and navigator.locks. No generic request
wrapper or manual endpoint registry was recreated. No BFF or credential policy
change was made.

## Release, locks, strict coverage and documentation

Accepted public proof: [release acceptance](released-040-artifact-lead-acceptance.json)
and i1's receipt `artifacts/package-s/published-client-proof-0.4.0-2026-11-03/release-proof-receipt.json`
(SHA256 `cf45d568e9c2560915b9c4dbe95359e9313cb1aae2122d5bfa1b2badee6a9952`).
All 1364 installed files still match its verified archive manifest; actual root
exports/new methods/descriptions/destroy alias and HaveAPI0.32 were inspected with
zero network dispatches. [Installed proof](w-040-installed-proof.json) and
[entrypoint proof](w-040-entrypoint-proof.json) retain their actual scope.

Public version0.4; archive SHA256
`3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`;
source `c53cb4dabb0b3aac8d05834478872d2cfa698fa7`; runtime peer0.32;
generator1ef9/Ruby0.32.2; API942c/schema d6ec6176. This release adds two actions
and seven expected_state inputs; old0.3 whole-program equality is not reused.
No independent Sigstore cryptographic verification is claimed.

Ordinary frontend npmDepsHash:
`sha256-3H/bRfGSY5Mra3MkhjcgBSiP/NciqX0Q58K+zem/i9k=`.
All 484 unrelated root lock records match current main; BFF manifest/lock/hash,
flake/API/localization pins and source-checker security guards match old4ed.
The initial dependency batch installed successfully but exited127 on a vanished
unrooted prefetch executable. Its original failure is retained. Only the affected
ordinary tool realization/prefetch continuation ran again and passed0/7.725s;
no npm install/ci repeat occurred. The tool root remains retained.

Strict coverage143 checked/140 deferred includes the main contract helper and
whole advisory-outage spec. Baseline7bdc and sourceRevisionabab remain exact;
all140 surviving deferral records remain byte-identical and in order. Parsed
compiler options/extends/files/ambient configuration are unchanged from the
accepted rebased config; its only textual change is pinned Prettier formatting.

Current documentation: `docs/design/HAVEAPI_CLIENT.md`, `PACKAGING.md`,
`API_CONTRACTS.md`, generated `IMPLEMENTATION_INVENTORY.md`, and the existing dated
migration worklog. Lead applied its English pass. Old4ed worklog bytes are
preserved, then the approved factual appendix is added. Project docs explain
supported contracts/optional local workflow; session records own rollout and
actual result provenance. No follow-up review/build outcome worklog loop is planned.

## Quick verification and remaining gates

[Completion receipt](w-040-final-completion-receipt.json),
[path/blob/SHA/mode bindings](w-040-final-path-bindings.json),
[history/input receipt](w-040-final-history-and-input-receipt.json),
[retained strict graph](w-040-retained-strict-input-graphs.json), and
[final docs checks](w-040-final-doc-checks.json) bind all checks.

Final appstrict native0/59.822s, zero diagnostics, ran on frozen working inputs
based at734. Tooling/E2E143/140 and six source-checker tests retain their exact
successful unchanged-input executions. Original failed quick batches remain;
fixes passed in affected Vitest continuations. Final node-panel3files/12tests
pass, editor1test passes, and the state/revision-negative API suite passes.
Scoped ESLint/format/docs/catalogs/structure/API-barrel/Nix syntax/whitespace all
pass. The only post-check input change is the approved worklog appendix, whose
format/docs/whitespace checks passed. Metadata-only history moves preserve the
entire checked tree. This is exact source/input reuse, **not** a literal-final-head
execution or a Nix-derivation/graph equality claim; no single blanket Vitest-pass
count is inferred.

Risk: **high** (authenticated API/destructive operations, partial writes and
mixed-version guards). Parent should use the retained independent reviewer with
saved settings and all four lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility, plus explicit whole-series/history/
input-stream/no-migration conclusions. Parent owns assignment and acceptance.

Pending: independent final review, required full core and three native PR-smoke
CI jobs, exact-final-head rooted Nix5, publication with exact old-head lease and
conditional main integration. No new browser/isolated API replay, Nix build,
publication, merge, deployment or preview lifecycle operation was started by W.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
