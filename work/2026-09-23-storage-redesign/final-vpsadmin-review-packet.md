# Final vpsAdmin branch review packet

## Assignment

Review the complete unpublished storage integrity feature branch at high risk
in all four mandatory lanes: general, architecture and repetition, scope and
proportionality, and risk and compatibility. Read the canonical
`mandatory-change-review` skill and each selected lane reference. Inspect the
entire commit series and final base-to-head diff, not only the final tree or
earlier per-slice reviews. Report Blocking, Important and Advisory findings
with exact source anchors. This is a read-only review; no production access,
source edits or long integration tests.

## Ownership and outcome

- Session: `2026-09-23-storage-redesign`; records `plan.md`, `state.md` and
  `storage-integrity-design.md` in this directory.
- vpsAdmin worktree:
  `worktrees/2026-09-23-storage-redesign/vpsadmin`.
- Base: current `origin/master` `7045c81b3a5be312eac0d41e8a44f783340abb9f`.
- Head: `175111ee73a848e075a9552c50bfa1d6d7f86fa5`.
- Commits: `b2e5b6a9d storage: add observer integrity and freeze controls`,
  then `175111ee7 docs: explain storage integrity evidence and limits`.
- Requested outcome: one final additive foundation schema, observer admission
  and settlement, authenticated API/WebUI read-only control, private advisory
  reconciliation capture/compare/plan, and test-only strict proofs for 5204
  and opted-in 5215. Production strict dispatch, verified scope publication,
  identity linking and repair APPLY remain disabled.

The functional commit intentionally keeps the final schema, paired API/Node
effect registry, journal, signed input, receipts, API mode CAS and WebUI
control in one cross-component versioned contract. The second commit keeps
lasting system explanation separate from rollout history. There are no
intermediate deployable commits within this feature branch; the operations
guide orders schema, Node, API and WebUI deployment.

## History and migration provenance

The prior unpublished branch contained 25 feature commits above the original
base `486350466e8fb6f966add1cde3fa2bc12b4d6b62`, including six superseded
sudo-launcher/VM commits and five branch-only migrations. The user confirmed
none was deployed, merged or released. The final tree was replayed from the
old final snapshot onto current upstream master. Its binary feature patch
and changed-path inventory were compared exactly with the old final snapshot;
both match. Final patch SHA-256:
`ad15183e58bf9c928c974837b6ff1ace657106c5e219b4548f5eb27e5dcc74ae`.

The final branch adds exactly one migration:
`api/db/migrate/20260924210000_add_storage_integrity_foundation.rb`.
The four later transitional versions 20260925120000, 130000, 140000 and
150000 are absent. The foundation now directly creates final observer
settlement indexes, strict attempt provenance pair and API-user-only freeze
audits. Unused reconciliation decision/action tables and models are absent;
the retired CLIs, Nix sudo launcher and VM fixture are absent. Core-only
`api/db/schema.rb` is generated at the foundation version. Fresh schema loads
still require the explicit singleton bootstrap before the setup marker;
upgrades execute the migration's insert. Missing control row fails closed.

## Documentation and deployment boundary

- Lasting model: `docs/storage/integrity-model.md` explains Dataset, DIP,
  SIP/SIPB, both registry axes, scopes, intents, targets, attempts,
  observations, freeze, drain and physical identity.
- Current constraints: `docs/storage/integrity-foundation.md` and
  `docs/storage/integrity-reconciler.md` describe observer and advisory
  behavior without implying APPLY or node quiet.
- Repository routing: vpsAdmin `AGENTS.md` requires final branch-history and
  unapplied-migration review, and separates lasting docs from rollout notes.
- Site rollout guide (separate repository):
  `vpsfree-cz-configuration/docs/operations/vpsadmin-storage-integrity-deployment.md`
  at feature head `57c6cb9c`. Its writer-hold corrections received a clean
  affected-lane review. The configuration channel is not pinned yet.

The production service channel also reaches shared internal hosts, while
staging/production NodeCtld use separate pins. No shared host, production DB
or dev cluster has been switched. Old API/Node writers may bypass admission;
`db_drained` is DB control flow only, not node child or delayed osctld quiet.
An old-node rollback after publishing linked identities is unsafe. Review
mixed-version behavior, schema-first ordering and software rollback with
these explicit limits.

## Quick verification

- Both new commits passed normal vpsAdmin Nix/Overcommit hooks: Nixfmt,
  MigrationSpecs, WebUI i18n, PHP CS Fixer, RuboCop, API i18n and message checks.
- `ruby tests/ci-selection-test.rb`: 18 runs, 77 assertions, no failures.
- Focused WebUI PHPUnit: 5 tests, 17 assertions, no failures.
- `git diff --check origin/master HEAD`: clean; feature worktree clean.
- On the final clean head, the ordinary API/model/resource selection passed
  76 examples with no failures.
- On the final clean head, the focused Node registry, receipt, settlement,
  inventory and Command selection passed 122 examples with no failures
  using an isolated Bundler directory. The shared gem directory first failed
  to load `i18n` before any examples; it was an environment failure, not a
  product-test failure.
- On the final clean head, the predecessor-schema migration passed 4/0 and
  the fresh-schema singleton bootstrap passed 2/0 in separate DB processes.
  Isolated attempt provenance passed 3/0 on the identical source patch before
  replay.

Do not infer a production repair capability from these checks. The long
cross-component contract and disposable dev-cluster trial follow this review.

## Non-goals and user decisions

The user chose API/WebUI controls over the original host CLI/launcher and
explicitly requested replacement of obsolete unmerged history and schema.
No snapshot deletion, backup scheduler change, production strict switch,
approved repair action journal, ZFS correction, disk-only import, default
branch merge, shared-host deploy or production APPLY belongs to this branch.
The later node-inclusive quiet probe and one-engine frozen APPLY remain
separate implementation gates in the session design and plan. The G0 trial
will run only in the session-owned disposable storage-topology dev cluster
after this independent review passes.

## First review outcome

Reviewer0 (retained GPT-6 Sol/xhigh) reviewed this exact two-commit series
at high risk in all four lanes. The final tree had no additional Blocking or
Important functional finding. The general, architecture and scope lanes found
the 17,073-line functional commit too broad: foundation, observer writer,
advisory reconciler, authenticated freeze UI/API and test-only strict proof
can be reviewed and tested as separate commits. That finding is Blocking for
this history. Implementer0 is reconstructing focused commits in a separate
worktree; the feature ref still points to this reviewed head. The next packet
must name the rewritten commits and prove final-tree equivalence. A narrow
two-spec registry fixture correction was discovered during replay and must
be listed as a deliberate delta from this first reviewed tree.
