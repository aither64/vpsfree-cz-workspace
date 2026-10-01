# Current-default rebase and disposable React cluster brief

## Scope and authority, 2026-10-01

This is the architect's implementation and verification brief for the user's
authorized rebase of active storage feature branches and redeployment of this
session's disposable cluster with the new React WebUI component. The lead's
subsequent instruction selects **reset and clean rebuild**: the user explicitly
permitted resetting this cluster and said they had not changed its data. This
replaces the earlier retained-disk upgrade proposal. It does not authorize a
session lifecycle change, integration into default branches, or a shared-host
deployment.

Keep the storage feature at its present advisory boundary. Production strict
dispatch, node quiet, repair readiness, executable reconciliation and APPLY
remain off. Keep PHP storage-freeze controls and direct-admin API access. Do
not implement storage-freeze controls in React for this task.

Readers: implementer, lead, independent reviewer and disposable-cluster operator.
The [plan](plan.md) and [state](state.md) own sequence and executed results;
[storage-integrity-design.md](storage-integrity-design.md) owns the storage
architecture and future maintenance/repair gates. The [previous G1a trial](g1a-dev-cluster-trial.md)
remains historical evidence and must survive the reset. This document contains
the acceptance contract and explicitly attributed execution checkpoints;
the lead owns detailed state, rollout and provenance records.

### Execution checkpoint reported by the lead, 2026-10-02

Whole-branch reviews and SSH feature publication are complete for vpsAdmin
`e65a5a6b`, OS `8d05dc3ae` and configuration `5eff`. The exact vpsAdmin API CI
workflow `36925295017` passed all 27 jobs; broader CI is queued.

The first owned clean start built and booted, then failed at the generated
dev-user seed because the added level 99 lacked a namespace. Both consumed
migrations and the freeze singleton were already valid. After checking the
available namespace range, the lead completed the private configuration and
ran the supported services update successfully (exit 0, including refresh).
No source/migration correction, further reset or manual DB seed was used.
A disposable credential was replaced privately and its supported services
update also passed. All services/seeds, the three selected Node generations,
actual osctld `gc_trash_v1` responses and activated nginx/BFF package paths
were proved as recorded in [state](state.md). Served frontend/BFF metadata
matched, with the supported unknown embedded revision reported honestly.

The diagnostic browser trial passed at these exact sources:

- vpsAdmin `e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36`;
- vpsAdminOS `8d05dc3ae1fb71c1385609990acdf093af49ceec`;
- React `aa2f60b89df65d2f987be48784ed42bab7010833`.

The lead reports exit 0, 242 checks and about 46 seconds in the private
`browser-acceptance-php-diagnostics.log`: real React login/API/logout and
anonymous 401; PHP login/status/freeze/unfreeze; stale and same-mode CAS 409;
anonymous 401/nonadmin 403; and valid Pool Create refusal 423 with unchanged
rows. The trial advanced epoch 2 to 4 with exactly two new audit events and
`recovery_attempted=0`. Independent guest SQL, also reported by the lead,
confirmed `read_write`, epoch 4, four total audits, exactly one singleton and
both consumed migrations applied. The compact runtime gates are complete.

Preserve the earlier attempts separately: the token-route helper error was
corrected, but the earlier PHP unfreeze failure remains unexplained. Its API
recovery was not PHP verification, and the later diagnostic pass does not
establish a root cause or an application fix. Broad CI is still queued and
the upstream React nightly remains residual evidence to assess separately.
The architect has not rerun tests or inspected generated seed configuration,
credentials, private browser logs or the running cluster. Production strict,
node quiet, repair readiness and APPLY remain off.

## Source selection and ownership

The following defaults were fetched and reported by the lead on 2026-10-01;
the architect inspected their local Git objects. Save exact old/new refs and
range comparisons before any rebase. Recheck the default if it advances before
the final candidate is selected.

| Component | Existing session head | Fetched default / action |
| --- | --- | --- |
| vpsAdmin | `fa7cec3a89e433e91516a369f10b1b17b6eddfef` | Rebase onto `origin/master` `90184b374ce0a139319b66326a29373b92d8ee93`. |
| vpsAdminOS | Registered `dcad075a171244cc17d67d625ab89c402d11781e`; reviewed staging port `107cef01f` | Use current `origin/staging` `26f28c69149b5312305aceb7f5614bd1d3fe3bbc` plus one copy of the reviewed provider patch. Prefer replaying the staging port; do not put the old `dcad` lineage over current staging. |
| Site configuration | `fc203cb0ff260d741f14a6c446b3d543e9eb06d2` | Rebase onto `origin/master` `029c616ed906de80b8813cc20391e294c3e9f4c2`; preserve current channels and the separate React host. No host switch. |
| Maintenance tasks | `a457cfc3aa4431565d65d6bbe9f4e63f8d8d327e` | Default `2fdc9f2889ac419136cd0cde0e0955c015ae7107` is unchanged: already based on current default; no artificial rewrite or script execution. |
| React WebUI | No storage feature needed | Select published default `main`, `aa2f60b89df65d2f987be48784ed42bab7010833`, through the existing provider's same-session source override. |
| Workspace / extension | Superseded session instruction branches | Retain their refs for provenance. Do not revive, merge or repin them. Use the installed current provider. |

The vpsAdmin default delta since the original base `486350466` consists of
fourteen Ruby/PHP dependency lock/packaging files. It does not extract PHP into
the React repository. `vpsadmin-webui/AGENTS.md` and `README.md` explicitly keep
the API and legacy PHP UI in vpsAdmin. The PHP freeze forms, page, cs/en catalogs,
PHPUnit test and Playwright admin-cluster test therefore stay in vpsAdmin.

The inspected OS default delta `af9543a54..26f28c691` changes only `flake.lock`.
The reviewed staging provider port is based on `af9543a54`; reapply its source
patch while retaining current staging inputs. The original provider branch is
based much earlier and must not discard the staging lineage. Preserve the
unrelated untracked `libosctl/tmp/` in the registered OS worktree. The lead owns
ref backups and branch selection; implementations must not duplicate provider
commits or reset shared/unrelated work.

## Existing React integration: no new application feature

The installed vpsFree development-cluster extension already contains the
integration in `dev-clusters/vpsadmin/{flake.nix,nix/test.nix,README.md}`.
It is separate from vpsAdmin's own `tests/configs/nixos/vpsadmin-services.nix`.

- Enable `newWebui.enable=true` and a distinct `domains.newadmin` in this
  cluster's private config. Keep `storage` topology and `bridge` networking.
- The provider's built-in pin is older WebUI
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`. The lead selects published current
  default `aa2f60b89df65d2f987be48784ed42bab7010833` for this rebuild. Use the
  registered clean same-session `vpsadmin-webui` source override and check both
  immutable packages. This needs no new WebUI behavior patch. The lead owns
  worktree/ref setup; do not silently rewrite the installed provider pin or
  borrow another session's worktree.
- Provider input `vpsadminWebui.inputs.vpsadmin.follows="vpsadmin"` binds the
  frontend/BFF reference to this cluster's selected API. Its `nix_overrides`
  binds both `vpsadminos` and `vpsadmin/vpsadminos` to the selected OS source.
  Frontend and BFF must come from the same input and have matching build-info;
  the accepted path-source provenance boundary below applies.
- The provider owns the new `newadmin` container, TLS frontend routing, private
  nginx port 18082, loopback BFF port 3001, cluster CA trust and API version 7.0.
  Use these existing interfaces, without a parallel hand-written proxy/seed.
- A separate nondefault OAuth client preserves the PHP default client. The
  provider owns the private credential bundle and seeds the exact callback
  from the selected newadmin origin. Do not print credentials, cookie values,
  OAuth codes or tokens in build/test reports.

The site configuration has an independent `vpsadmin-webui` channel mapping to
`vpsadminWebui`, with `inputs.vpsadmin.follows="vpsadminServices"`. Preserve this
new upstream graph and host while rebasing the storage service pin. It does not
select this disposable cluster's React package. Likewise, its
`vpsadminServices` input follows separately pinned `vpsadminosStaging`; a service
pin alone never upgrades osctld. No site OS or React channel update is required
to start this disposable component. A later exact feature pin, if needed, uses
`confctl inputs channel set --commit`, not hand-edited `flake.lock`.

### Accepted path-source provenance boundary

The supported same-session override passes `path:<worktree>`. A clean selected
Git checkout does not guarantee that Nix supplies `self.rev`: WebUI
`aa2f60b:nix/provenance.nix` then emits `commit="unknown"`, `dirty=true`,
`source="unavailable"`. Its package checker explicitly accepts this form and
requires frontend/BFF metadata equality
(`scripts/check-package-contents.mjs:28-43,112-115`). This is acceptable for this
disposable functional trial; it is not evidence of a known clean release build.
Do not rewrite build-info or present the provider's Git selection label as
package metadata. No new packaging feature is required.

Record separately at build/activation time:

- Selected full Git SHA and tree ID, with clean status before and after the
  build; keep that source unchanged while the build runs.
- Evaluated frontend/BFF derivation and output paths, and the filtered source
  store path plus NAR hash consumed by each derivation. Record any BFF source
  subdirectory explicitly. An output hash alone does not prove a Git revision.
- Activated nginx root and BFF executable/package paths; served frontend
  `build-info.json` and installed BFF `share/vpsadmin-webui-bff/build-info.json`
  must agree. Record their actual fields, including unknown/dirty/unavailable
  when present, alongside the separate source-selection evidence.

This evidence binds the selected `aa2f60b` source and the deployed pair without
claiming that embedded metadata contains a revision it does not contain.

### Minimal history and pin order

Proceed with independent clean rebases while pins are coordinated. Rebase the
reviewed OS provider first, verify/review its complete delta on current staging
and publish the selected provider feature head. Rebase the vpsAdmin feature
series concurrently as appropriate; keep its runtime and both migration blobs.
Replace the old provider pin with **one logical generated pin commit** selecting
that new published OS head, using `tools/update_vpsadminos_flake.sh`. Do not keep
an obsolete old-provider pin followed by a corrective new-provider pin in the
final rewritten series. Review the complete final vpsAdmin base-to-head series
and publish its exact candidate.

Checkpoint reported by the lead: the whole OS branch
`26f28c691..8d05dc3ae1fb71c1385609990acdf093af49ceec` passed its four-lane
independent review as one commit with no migrations; the normal signed SSH
lease push succeeded and the remote exact head was confirmed. The vpsAdmin
old-pin removal/replay reached `0bdd6caaa4aadfc16b5f124f16b7b5bb102bc0ed`,
with all 18 retained entries patch-equivalent and no non-lock delta reported.
The architect's read-only comparison also found no `api/db` delta from
`fa7cec3` at that intermediate head. The updater produced final candidate
`e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36`; its source conformance is recorded
below. The lead subsequently reported whole-branch review and feature
publication complete; the later runtime result is recorded in the execution
checkpoint above.

Rebase the site rollout guide onto current config master, then regenerate one
service-channel pin to that published vpsAdmin candidate with
`confctl inputs channel set --commit vpsadmin vpsadmin REVISION`. Replace the
obsolete `fe4` feature pin rather than retaining two successive service-pin
commits. Preserve the new React follows/channel graph and unrelated lock nodes;
inspect required transitive changes individually. Do not update site OS channels
or deploy shared hosts. The lead's inventory reports no application-source
overlap in the vpsAdmin dependency-only upstream delta; the OS test-registration
overlap in `tests/all-tests.nix` must retain both upstream tests and the provider
test. Pin coordination must not hold those otherwise independent clean rebases.

### Final pin and migration conformance, e65a5a6b

The architect's read-only Git/source assessment found no conformance blocker:

- There are 19 commits above `90184b374`. The final generated commit changes
  only `flake.lock`, replacing the original `8e44a5124` pin directly with
  published `8d05dc3ae1fb71c1385609990acdf093af49ceec`. Its recorded NAR hash is
  `sha256-J0GUpTd2OCkPCN0qCl4hQSwZy5HcPl4EljEBKpDEsVY=`. The only other
  changes are the locked revision/hash/time fields of existing
  `nixpkgsUnstable` and `nixpkgs_2`; both match the selected OS's own lock.
  Input mappings, original input specifications and unrelated nodes are
  unchanged. This source check does not independently recompute the NAR hash.
- Relative to `fa7cec3`, the final tree differs only in `flake.lock` and the
  fourteen upstream dependency files. All fourteen equal current default
  `90184b374` exactly. Application source, docs and tests are preserved.
- The branch adds exactly the two consumed migrations relative to the default.
  Both migration blobs and `api/db/schema.rb` equal `fa7cec3`. The bootstrap
  task at `api/lib/vpsadmin/api/tasks/db.rake:2-12` is also unchanged: insert
  singleton row 1 or leave it intact. The fresh setup calls it after schema
  load and before its initialization marker, then runs migrations
  (`nixos/modules/vpsadmin/database-setup.nix:167-182`). Existing setup skips
  bootstrap. Migration `20260924210000:128-135` still supplies the upgrade
  insert. Retain the additive schema on software rollback; do not run `down`.
- Advisory limits remain explicit: `api/models/transaction.rb:204-210` allows
  unsigned observer 5204, while 5290/5291 require signatures. API strict mode
  and the 5215 opt-in still return false; Node `Command` defaults strict
  dispatch to false. Planner output remains non-executable, historical
  coverage unknown, and activity/status output cannot claim repair readiness
  or child quiet. No identity publication or APPLY was added by this rebase.

This assessment ran no tests, evaluated no configuration and touched no
cluster. It does not replace independent review or runtime acceptance; later
lead-reported review/publication and CI results are recorded above.

## Rebase and compatibility invariants

1. Preserve the two consumed migrations **with their existing filenames,
   versions and contents**: `20260924210000_add_storage_integrity_foundation.rb`
   and `20260926100000_add_bounded_storage_capture_indexes.rb`. Compare their
   blobs against `fa7cec3`. Resetting the dev cluster does not make their prior
   consumption disappear. Any later schema change needs a forward migration.
2. Preserve generated final `schema.rb`, fresh-schema singleton bootstrap and
   existing-upgrade behavior. A missing singleton in an established DB fails;
   startup must not reset a frozen epoch or recreate read_write implicitly.
3. Preserve API admin/action-scope/session checks, both-direction epoch CAS,
   append-only transition/catch-up audit, atomic admission and bounded DB-only
   status. Keep `settle_observer` API-only and proof-gated.
4. Preserve unsigned production observer 5204 compatibility, exact Pool/member
   manifests, test-only strict 5204/5215 gates and whole-chain confirmation
   semantics. Rebase must not require a production transaction-signing rollout.
5. Preserve signed 5290/5291, paired registry behavior, inventory framing,
   transient Node exchange compatibility, `(1,1)`/`(2,2)` readers, policy-2
   reports, policy-3 nonexecutable plans and unknown historical coverage.
   Equal samples still do not prove exclusion or child lifetime.
6. Preserve the generic osctld `gc_trash_v1` schema, boot/instance/generation
   semantics and unknown-on-unsupported behavior. A new Node against an old
   provider reports unknown. No provider upgrade turns readiness on.
7. Resolve generated dependency conflicts using current dependency selections
   and project regeneration tools, retaining storage-specific source/gem
   metadata. Do not restore old composer/gem/OS locks wholesale merely because
   they were present in the feature branch.
8. Compare complete old/new patch series and final base-to-head diffs, including
   schema, locale artifacts, CI topic coverage and selector rules. Record any
   semantic resolution; it needs focused verification and independent review.
   Existing migration versions cannot be squashed away. Keep branch backups.

Software rollback returns to saved feature revisions and matching guest system
generations while retaining the additive schema and data. Do not run migration
`down` or select an old API that bypasses admission and then call the system
frozen. React frontend/BFF roll back as a matched pair. Keep the new OAuth
client separate; disabling the new container leaves legacy PHP available.

## Verification brief

The implementer/lead runs these checks; the architect ran none. Use project Nix
environments. Long or uncertain-duration checks belong to a fresh verification
watcher. Complete quick checks and commit before mandatory review; the dedicated
reviewer must assess each complete rewritten branch, migration provenance,
cross-project pins and any conflict resolutions before longer integration.

### Quick source and focused checks

- All affected trees: scoped `git diff --check`, declared hooks, exact old/new
  heads, `git range-diff`, and no accidental unrelated paths. Verify both
  consumed migration blobs and schema version. Keep default refs untouched.
- The vpsAdmin `.#api`, `.#libnodectld` and `.#webui` shells already enter
  their component directory; do not run a second `cd` into that component.
- vpsAdmin API (`nix develop .#api`): `bundle exec rspec
  spec/migrations/20260924210000_add_storage_integrity_foundation_spec.rb
  spec/migrations/20260926100000_add_bounded_storage_capture_indexes_spec.rb
  spec/migrations/storage_freeze_bootstrap_spec.rb`; then focused
  `spec/api/resources/storage_freeze_spec.rb`,
  `spec/models/storage_mutation_admission_spec.rb`,
  `spec/models/storage_observer_settlement_spec.rb`,
  `spec/models/storage_freeze_status_spec.rb`,
  `spec/models/storage_reconciler*_spec.rb` and
  `spec/models/storage_activity_report_spec.rb`.
- Node (`nix develop .#libnodectld`): existing registry,
  receipt, strict-dispatch, command, node-activity, inventory and 5291 specs;
  broaden to the full component suite only for a concrete remaining runtime
  risk. Keep fixture-only strict mode separate from deployed configuration.
- Legacy PHP: `nix develop .#webui`, `composer install`, then
  `composer test -- --filter StorageFreezeUiTest`; check
  changed locale source/generated pairs and normal PHP hooks.
- vpsAdminOS (`nix develop`, `cd osctld`): `bundle exec rspec
  spec/osctld/storage_activity_spec.rb spec/osctld/garbage_collector_spec.rb
  spec/osctld/trash_bin_spec.rb spec/osctld/commands/simple_delegators_spec.rb
  spec/osctld/commands/heavy_system_spec.rb` and declared hooks.
- CI plumbing: `ruby tests/ci-selection-test.rb` in vpsAdmin; preserve exact-once
  API spec topics and the separate 5215 contract workflow. Evaluate config/pin
  changes with their owning tools. No `confctl deploy` to shared hosts.

No React source change means no new React implementation suite is required.
The selected published `aa2f60b` needs the accepted provenance evidence above
and the real cluster acceptance below. If a packaging/runtime compatibility change becomes
necessary, use its `nix develop` toolchain and affected declared checks, including
`npm run ci:quick`, `npm run ci:tests`, `npm run build` or module/package checks
as appropriate to the change. Record upstream evidence separately from local
results; synthetic browser fixtures do not certify this real dev API login.

### Required post-review cluster gate

- Build/evaluate the exact selected development-cluster configuration, including
  the React pair and provider-preserving OS source. Stop an unexpected local
  kernel build and investigate cache availability under workspace procedure.
- Reset and start this disposable cluster as below. Require real React login
  and API reads, legacy PHP freeze/auth/CAS checks, fresh bootstrap/OAuth ordering,
  Node provider checks and coexistence. Upstream fixture/VM proof does not
  substitute for this trial.

The lead reports the rebased focused checks passing: OS 36/0 with normal Nix
hooks successful, API 62/0, Node 42/0, PHP 5 tests/17 assertions, and selector
18/77. These are lead-reported results, not architect-executed verification.
Whole-branch review/publication is complete for OS, vpsAdmin and configuration,
as is the architect's final vpsAdmin source conformance assessment. The lead
reports the exact-head API CI workflow passed and compact runtime acceptance
is complete: fresh schema/bootstrap/OAuth setup, honest activated package
evidence, real React login/API/logout, PHP/API freeze/auth/CAS/admission and
return to read_write, and Node/provider health. Broad CI remains queued and
the upstream React nightly is a separate residual. The earlier unexplained PHP
unfreeze failure is retained above; no application fix is claimed. This trial
does not add separate VM prerequisites or establish repair authority.

### Residual checks with a concrete trigger

Unchanged source patches plus an OS dependency rebase do not by themselves
require separate backup, migration, provider, PHP or 5215 integration runs
before this disposable trial. Keep their prior results as historical evidence.
Run an affected test if a conflict resolution, focused failure or actual runtime
change exposes a remaining risk:

- `tests/contracts/storage_group_snapshot_v4/run.sh` for changed API/Node
  staging, signatures, receipts or confirmation behavior.
- OS `./test-runner.sh test osctld/storage-activity` for changed provider logic
  or a node-provider failure in the fresh cluster.
- vpsAdmin `./test-runner.sh test 'webui#admin-cluster'` for changed PHP controls
  or a browser failure that requires its isolated fixture.
- `storage/backup-full-incremental` and `storage/dataset-migrate-retain-source`
  for demonstrated transfer/rollback/data-preservation risk; retain their
  file-content assertions. These tests do not clear older unrelated CI failures
  unless those failures are reproduced and investigated explicitly.

## Selected clean rebuild and acceptance sequence

Only the lead/assigned operator executes this sequence. The stopped/stale
preflight state below is historical: the owned clean start has since built and
booted, followed by the supported seed recovery and successful second services
update recorded above. Browser/provider acceptance is complete by the lead's
reported evidence, with the remaining limitations preserved above. The numbered
sequence records the trial's acceptance contract, not a request to repeat it.
Do not repeat reset or run cluster actions as an architect-side verification step.

**Pre-start occupancy history:** the lead's 2026-10-01 preflight found the default
bridge address `172.16.106.53` occupied by another session's active cluster;
this session was stopped then. The user subsequently explicitly requested
releasing those addresses, saying they considered that session done. The lead
assigned a fresh verification utility only the stable command
`vpsadmin-devcluster stop 2026-09-30-portal-review-improvements`. This is narrow
authorization for that cluster stop, not permission to archive/delete a session,
reset its disks, edit its records or change its team. The architect takes no
foreign-session action. The lead reports that the authorized stop completed
with exit 0 and the frontend no longer responded to ping. This records the
reported release outcome, not a permanent reservation or an architect-run
probe. Any later start still requires a fresh address-availability check. Do not use
`--force` or switch to local networking to bypass an occupancy refusal.

1. Before reset, verify exact workspace/slug and retained process/socket/disk
   ownership through the supported lifecycle tooling. Privately preserve the
   current cluster config, selected result-config/provenance, source heads,
   prior generation references and earlier DB backup/trial records. Reconcile
   stale runtime state through supported refusals; do not remove ownership
   metadata manually. Retain Git backups and historical session evidence.
2. The user waived preservation of old VM data. A new old-DB dump or complicated
   frozen in-place upgrade is therefore not a prerequisite. Perform the
   explicitly authorized reset of **this cluster only** with
   `vpsadmin-devcluster reset 2026-09-23-storage-redesign`. Do not reuse an old
   runner to prepare disks, reset another cluster or change session lifecycle.
3. Recreate/configure this cluster with storage topology, bridge networking,
   `newWebui.enable=true` and distinct configured `domains.newadmin`. Preserve
   other reviewed seed/config choices rather than assuming defaults are
   identical. Credentials belong to the provider; after a clean reset it may
   generate a new complete private bundle. Do not combine old DB OAuth rows
   with a different credential bundle. Keep diagnostics private.
4. Start the reviewed sources with
   `vpsadmin-devcluster start 2026-09-23-storage-redesign --topology storage --network bridge`.
   Do not use `--force` to bypass an occupied bridge address. Prove selected OS
   supports rootDisk/per-disk preservation before runtime construction; current
   provider rejects an older incompatible runner. Record selected revisions,
   clean/dirty provenance and actual activated systems separately.
5. Check fresh initialization: schema load, singleton bootstrap, core/plugin
   migrations, ordinary dev seed, runtime WebUI credentials, React OAuth seed,
   then `container@newadmin`. Require successful unit results and both migration
   versions recorded as applied, singleton row 1 exactly once, expected initial
   mode/epoch, and no synthetic bootstrap reset of an existing control.
6. The ordering is source-backed: vpsAdmin
   `nixos/modules/vpsadmin/database-setup.nix:173-182` bootstraps immediately
   after fresh schema load and before migrations; provider
   `nix/test.nix:1513-1552` makes the React seed depend on database setup,
   ordinary seed and credentials, and makes its container depend on that seed.
   A failed prerequisite must prevent the new container starting. Do not
   force-start BFF around these gates or seed clients manually to conceal a
   setup failure.
7. Verify services API/Supervisor/MariaDB/RabbitMQ/nginx and all three nodes.
   Check provider `pool_storage_activity`/`gc_trash_v1` where osctld manages the
   selected pool, preserving unknown child coverage. An absent/inapplicable
   provider remains explicit unknown, never invented quiet proof. Verify actual package/process revisions
   and `/run/current-system`, not just the built result link. Take a fresh
   private logical DB backup and record guest generations after successful
   fresh initialization and before further stateful trial work.
8. New React endpoint: verify trusted TLS and the accepted path-source evidence
   above, including actual frontend/BFF metadata equality; unknown embedded
   revision is reported truthfully. Check `/config.json`, anonymous
   `/session.json`, OAuth login
   with a seeded disposable member and successful actual API data retrieval.
   Verify logout; check that API errors are surfaced and no standalone fallback
   masks BFF failure. Check direct SPA navigation, PHP UI availability and its
   separate default OAuth client. Do not put cookies or authentication URLs
   containing codes into public/session evidence.
9. Legacy PHP/direct-admin API: show the full bounded DB-only status; CAS to
   read_only using the observed epoch and a reason, reject a stale CAS without
   an extra transition, verify a nonadmin is denied, and confirm new
   storage-mutating chains are refused. Use an existing disposable fixture for an
   admission test; do not interpret a missing-resource error as freeze proof.
   Preexisting work settles normally. Return to read_write using the fresh
   epoch and verify one audit event per successful transition. React is usable
   without new storage-admin controls; those remain in PHP/API.
10. Report cluster running/usable, React and legacy URLs, exact component
    revisions, mode/epoch, migrations, observed unit results and limitations.
    `db_drained` remains DB-only; `node_quiet=false`, `repair_ready=false`,
    executable plans/APPLY off and production strict off. No private raw
    topology or credentials belong in this report.

## Failure and recovery decisions

- A build/evaluation failure leaves deployment incomplete. Diagnose source/input
  compatibility; do not select an older OS lineage, alter consumed migrations,
  bypass hook failures or repair the cluster state by hand.
- Fresh DB/bootstrap/OAuth-seed failure blocks acceptance. Preserve bounded
  private logs, identify the failing unit and retry the supported setup path
  after a reviewed correction. Do not reset blindly to hide a migration defect.
- After successful fresh setup, a services regression may use a saved compatible
  system generation and matching frontend/BFF pair. Preserve the additive DB
  and credential pairing. Any DB restore must match the recorded backup's
  schema and client-secret bundle; a guest-generation rollback alone is not a
  DB rollback.
- API release from read_only requires a fresh authenticated epoch CAS. Do not
  reset the singleton or delete intents/locks to make a trial appear drained.
  If normal release cannot be proved, report the actual frozen state and blocker.
- This task does not claim G1b child/orphan exclusion, historical terminal proof,
  production repair approval, or resolution of the retained-lock scale caveat.

## Remaining evidence and implementation boundary

No substantive new application feature is expected. The implementer owns rebase
resolutions, generated dependency consistency and any demonstrated packaging
compatibility fix. The lead owns fetches/ref backups, current plan/state,
review coordination and the exact authorized disposable reset/start. The
architect owns this brief only. Material source deviations return to the lead.

The selected React `aa2f60b` revision, activated package/source evidence and
actual private cluster settings are recorded by the lead; the selected default
and provider's built-in pin differ. Broad CI and the upstream React nightly
remain separate residual checks. Preserve the unexplained earlier PHP unfreeze
failure without claiming that the passing diagnostic trial fixed it.
Upstream WebUI documentation retains some older verification-status text, so
use exact revision evidence and this trial's observations, not broad readiness
claims. Existing provider support, rather than a revived workspace instruction
branch, is the implementation boundary.
