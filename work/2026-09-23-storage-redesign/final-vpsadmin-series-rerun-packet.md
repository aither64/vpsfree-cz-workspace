# Rewritten vpsAdmin series review

## Assignment and scope

Retained reviewer0: rerun the independent mandatory review at high risk in
all four lanes on the rewritten unpublished vpsAdmin series. The first review
of the two-commit series found one Blocking general/architecture/scope issue:
the functional commit bundled independently reviewable work. Inspect every
new commit, its intermediate dependency boundary, and the complete final
base-to-head diff. Check that the six commits resolve the history finding
without introducing an intermediate load, schema, protocol or deployment
defect. This is read-only review; no source edits, long integration tests or
production/cluster action.

## Revisions and commit split

- Session: `2026-09-23-storage-redesign`; plan/state/design are in this
  directory. The worktree under review is the isolated replay at
  `/tmp/storage-review-split-2026-09-23/vpsadmin`; the session feature ref and
  its clean worktree still point to the old `175111ee7` until acceptance.
- Base: `7045c81b3a5be312eac0d41e8a44f783340abb9f` (`origin/master`).
- New head: `a15afb5184efe91c28fe717f3d02963e3836b826`.
- Commits in dependency order:
  1. `0ebec78ec` foundation schema, basic models and fresh bootstrap;
  2. `a669bc76e` paired API/Node observer admission, registry, receipt,
     settlement and DB status;
  3. `163bf3457` signed 5290 inventory and private advisory reconciler;
  4. `f07b23899` authenticated API/WebUI freeze and actor audit;
  5. `0aa5d334c` test-only strict 5204/5215 and cross-component contract;
  6. `a15afb518` lasting model/docs and AGENTS review routing.

These are distinct review and dependency units. The schema is first and has
the only feature migration. Paired API/Node protocol pieces stay together
inside the observer, 5290 and test-only strict commits; production strict
remains off. The API freeze follows admission and audit DDL. The contract
workflow arrives with its test harness. Lasting docs are separate from the
session rollout record and the configuration repository's site runbook.

## Final-tree equivalence and deliberate correction

The prior reviewed final tree was `175111ee7` in the same bare repository.
Independent lead checks show the exact same 163 changed-path name/status
manifest (SHA-256
`72434e31682e6cbf09f7d18c8533d79ba468fdc40a3c4327144b91518dc2c2de`)
and an identical base-to-head binary patch outside two API test fixtures.
Only `api/spec/models/transaction_spec.rb` and
`api/spec/models/transaction_chain_spec.rb` differ: each
`StorageEffectRegistry::Entry.new` no-storage fixture adds the two required
v4 strict-direction fields. This fixes an eight-argument Data constructor
after the registry grew to ten fields. No runtime or schema difference is
introduced by the replay. `git diff --check` passes; the temp worktree is
clean. The original old head is preserved by a verified recovery bundle.

The user confirmed that none of the five prior feature migrations was
deployed, merged or released. The final series adds one additive migration,
`api/db/migrate/20260924210000_add_storage_integrity_foundation.rb`.
The four transitional versions, retired freeze launcher/CLI/VM fixture and
unused approval/action schema do not survive. Fresh schema load invokes the
singleton bootstrap before the setup marker; upgrade migration inserts it.

## Quick verification

- All six commits passed normal Nix/Overcommit pre-commit and message hooks.
- On the final code in staged groups: foundation predecessor migration 4/0
  and fresh bootstrap 2/0 on the identical final source patch; group-2 API
  72/0 and Node 82/0 (including both fixed registry fixtures); group-3 API
  65/0 and Node 54/0; group-4 API 36/0 and WebUI PHPUnit 5 tests/17
  assertions; group-5 API 11/0 and Node 107/0. The group-3 API watcher
  reported exit 0 but did not retain its redirected log. Other focused logs
  are private local test artifacts.
- The old two-commit final tree also passed ordinary API 76/0, focused Node
  122/0, selector 18 runs/77 assertions, and fresh migration/bootstrap
  4/0 and 2/0 on clean head. The rewritten final tree differs only by the
  two corrected fixtures and docs commit placement.
- The long real API-to-Node contract and disposable storage-topology cluster
  trial remain after review. No shared host or dev cluster has been switched.

## Contract and limits

Project explanation: `docs/storage/integrity-model.md`,
`docs/storage/integrity-foundation.md` and
`docs/storage/integrity-reconciler.md` at the rewritten head. Site deployment
guide: configuration feature head `57c6cb9c` in
`docs/operations/vpsadmin-storage-integrity-deployment.md`; it previously
passed its affected-lane review. The configuration channel is not pinned yet.
Old API writers can bypass read-only admission, old nodes may ignore v4 guards,
and `db_drained` proves only DB control-flow closure. The planner still emits
`executable:false`; repair APPLY, verified scope publication and production
strict dispatch are not enabled. The later node/child/osctld quiet gate and
approved repair path remain in the session plan/design. No default-branch
merge, production deploy or repair is authorized.
