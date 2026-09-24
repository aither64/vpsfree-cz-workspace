---
lifecycle: active
---

# 2026-09-23-storage-redesign

## Current status

Implementation authorized on 2026-09-24. The approved first phase is the
existing storage catalog plus verified physical identities, vpsAdmin mutation
guards, one rerunnable reconciliation engine and a simple storage read-only
toggle. Bootstrap and later repair use the same engine. User snapshot deletion
and backup scheduling changes are deferred. No production reconciliation apply,
storage mutation, deployment or default-branch merge is authorized by this
implementation request. [plan.md](plan.md) holds the current contract;
[storage-integrity-design.md](storage-integrity-design.md) records the
architect's reconciled first-phase design.

Implementer0 owns vpsAdmin source edits in the session feature worktree.
Architect0 owns design validation and the session design document. The lead
owns coordination, tracking and review. The vpsAdmin worktree was created at
`486350466e8fb6f966add1cde3fa2bc12b4d6b62` after fetching `origin/master`;
its registration is complete in `portal.yml`. The initial helper invocation
created the worktree but stopped on an Overcommit configuration-signature
check. After reading `.overcommit.yml`, the lead ran
`nix develop .#vpsadmin -c bundle exec overcommit --sign` and retried the
helper successfully. The first source commit passed its pre-commit hooks in
the lead's Nix shell after the implementer prepared and staged the changes.

Inventory branch ready, awaiting merge approval for
`vpsfree-maintenance-tasks` `master`.

The read-only backup inventory has been run against a production DB capture
and `backuper2.prg` ZFS capture supplied by the operator. The corrected offline
comparison contains 660 diagnostic findings. See
[investigation.md](investigation.md#read-only-production-inventory-2026-09-24)
for the evidence and interpretation. The private version 2 report is at
`tmp/storage-inventory-report-v2.jsonl` outside the initiative tracking tree;
raw captures and report must not be committed or exposed through the portal.
The [task guide](../../worktrees/2026-09-23-storage-redesign/vpsfree-maintenance-tasks/2026-09-24-storage-inventory/README.md)
documents capture and report semantics.
The DB collector now uses vpsAdmin API models for application rows, following
the repository's maintenance-task pattern. Its few direct SQL statements set
the read-only snapshot and capture DB connection/time metadata.
This session has not connected to production or changed live state. It read the
operator-supplied captures locally. The DB and ZFS observations were separate;
their comparison is diagnostic, not proof of one consistent instant or
permission to delete a snapshot. The follow-up comparator corrections are
pushed to the feature branch and await merge approval.

The current first-phase design retains existing SnapshotInPool and
SnapshotInPoolInBranch meanings and adds physical identity and clone-origin
evidence on catalog-owned rows. The design document is reconciled to this
scope. Snapshot deletion and backup dispatch remain later, separate work.
The requested integrity boundary covers vpsAdmin-initiated commands,
including its osctl wrappers; independent osctld and root ZFS mutations are
outside this guarantee. Backup dispatch remains separate later work.

## Repositories and ownership

- `vpsfree-maintenance-tasks`: worktree
  `worktrees/2026-09-23-storage-redesign/vpsfree-maintenance-tasks`, branch
  `2026-09-23-storage-redesign`, base `2fdc9f2`, current head
  `a457cfc3aa4431565d65d6bbe9f4e63f8d8d327e`, pushed to `origin`.
  The worktree is clean. No merge or deployment occurred.
- `vpsadmin`: session worktree
  `worktrees/2026-09-23-storage-redesign/vpsadmin`, branch
  `2026-09-23-storage-redesign`, base `486350466e8fb6f966add1cde3fa2bc12b4d6b62`,
  current head `aab70d711` (additive foundation plus observer writer slice); registered
  in `portal.yml`. No push, merge or deployment occurred.
- `vpsadminos` canonical bare HEAD `2166e5934fe1`: reference review only.
- `architect0` supplied physical graph and migration design, scheduler
  feasibility came from `implementer0`, and a fresh writable agent wrote the
  first inventory commit. After the environment update, retained
  `implementer0` wrote the model-based revision and reviewer fixes;
  `architect0` assessed its transaction and runner assumptions. The lead
  handled coordination, review integration, and tracking.

This conversation is bound to `2026-09-23-storage-redesign`, as checked with
`dev-session current` and the environment identity. The older session named
in the request was not accessed. The environment update allowed the retained
architect and implementer to verify this session with `dev-session current`
before accessing its worktree.

## Verification and review

- Earlier model-based collector revision: 24 tests and 104 assertions passed;
  Ruby syntax, `git diff --check`, and the README shell-block syntax check
  passed. The final comparator revision is verified below.
- Fetched `origin/master`; it remained at base `2fdc9f2`. Captured the
  repository comparison at base `2fdc9f2` and head `f5440b4`.
- The repository has no GitHub Actions workflows. `gh run list` returned no
  branch runs after push.
- Mandatory review classified the change **high risk** because it reads a
  production database and storage host and emits sensitive topology. A fresh
  independent standalone reviewer from the installed default development
  team's review role, GPT-6 Sol/xhigh, covered general, architecture, scope,
  and risk lanes. Retained read-only peers had reported `dev-session current`
  EROFS failures, so the retained reviewer was treated as unverified.
- Initial review found a blocking missing DB-to-ZFS branch-origin comparison
  and important host-scope, metadata-integrity, and ZFS-type checks. The
  implementation agent fixed them and broadened scoped lock capture. A review
  rerun confirmed those fixes, then found short hostnames could collide and
  asked for one cohesive unpublished commit. The final focused fix requires
  a qualified hostname and rejects short aliases; collision and failure tests
  pass. The two unmerged commits were folded into the single final commit.
  Review covered original `69dac3e` and remediation `86a7612`; their final
  equivalent plus the narrow host-scope reduction is `4ff9b48`. The narrow
  final fix did not require another review rerun.
- The user's model-based correction is committed as `883b846`, followed by
  focused review fixes in `f5440b4`. These are separate commits because
  `4ff9b48` had already been published. Retained reviewer0 (GPT-6 Sol/xhigh)
  independently reviewed `883b846` in the general, architecture, scope, and
  risk lanes at **high risk**. The reviewer found a blocking relative output
  path that fails under the API runner's service user/package CWD and an
  important missing Snapshot resource-lock scope. The implementer added an
  absolute-path CLI check, a private service-user-owned output recipe, and
  Snapshot lock capture with focused tests in `f5440b4`. These are direct,
  narrow fixes; no review rerun was needed. Reviewer0 could not run tests in
  its read-only shell, so the lead reran the passing suite in the writable
  environment.
- Operator captures passed checksums, scope and identity checks. The initial
  private comparison yielded 821 findings. The first follow-up commit
  `12cb437` fixed head-tree, unresolved parent and reference-count scope
  classifications; independent reviewer0 (GPT-6 Sol/xhigh) reviewed the
  general, architecture, scope and risk lanes at high risk, finding two
  Important issues: unresolved pointers also produced unrepresented physical
  edge findings, and pending references could produce a false firm undercount.
  The narrow remediation `a457cfc` fixes both and documents the distinction.
  Its 42-test/165-assertion offline suite passed in the lead's environment,
  along with diff checks. A review rerun was not needed for the direct,
  focused fixes. The corrected comparison yields 660 findings; its version 2
  JSONL report was verified by the Reader and has mode 0600. No integration
  or production commands were run by the team.
- Fetched `origin/master` at `2fdc9f2`, pushed feature head `a457cfc`, and
  captured its comparison at base `2fdc9f2`. `gh run list` returned no
  workflow runs for the branch; this repository has no GitHub Actions
  workflows. The worktree is clean.
- Follow-up design review by architect0 separated logical history from physical
  identity and ZFS clone edges, specified scoped validation, journaled guarded
  mutations and repair classes for the observed anomalies. Implementer0 mapped
  topology-changing handles, including receive `-F`, clone/promote and its
  rollback, export clone lifecycle and osctl-backed VPS operations. The user's
  latest scope correction excludes independent osctld/root operations;
  vpsAdmin-invoked osctl work remains covered. Architect0 and implementer0
  confirmed that SIP is one logical snapshot per DIP while a backup SIP may
  have several SIPB branch occurrences. A minimum additive schema can enrich
  SIP/SIPB with observed identity rather than duplicate every known snapshot.
  No source code, production state or private capture changed in this design
  step.
- Foundation migration and models committed as `cdeb6d616`. In isolated local
  MariaDB, core-only schema load and migration passed; separate migration and
  model specs passed 3 and 10 examples respectively. `api/db/schema.rb` was
  generated by the migration. All pre-commit hooks passed after RuboCop fixes;
  the commit-message hook reported text-width warnings only. Linked physical
  identity remains unpublished during mixed old-writer operation. This code
  does not yet guard writers or reconcile storage.
- Observer writer slice committed as `aab70d711`. It classifies vpsAdmin
  storage transactions, rejects new classified writes through a durable global
  read-only admission row, records observer intents, and gives nonbackup
  CreateSnapshot (5204) an identity-bound node receipt. It does not publish
  physical catalog identities or mark scopes verified. Ordinary proved
  compensation and unprovable attempts are distinguished; hard kills and
  receipt-start failures leave fatal chains and needs-reconcile evidence.
  Focused NodeCtld specs passed 63 examples and API admission/detach specs
  passed 11 examples after the final receipt fix. The normal Nix Overcommit
  pre-commit hooks all passed. The first commit attempt exposed locale ordering;
  the implementer normalized the two new messages before the successful hook
  run. Retained reviewer0 (GPT-6 Sol/xhigh) independently reviewed foundation
  `cdeb6d616` and original writer head `58eb29a8f` at high risk across general,
  architecture, scope and risk lanes. The review found no Blocking or Important
  issue and one Advisory documentation contradiction about when read-only
  admission is enforced. The implementer corrected only that description and
  the lead amended the unpublished writer commit to `aab70d711`; all hooks
  passed again. That narrow correction did not alter runtime behavior and did
  not require a review rerun. Residual limits are mixed-version unverified
  scopes, opaque handles, and no strict legacy-handle refusal, reconciler or
  production freeze/drain CLI. No long integration test has started.

The operator's DB capture lasted about seven seconds, and the two ZFS passes
took about 22 minutes for 48,288 objects. These timings are observations from
the supplied artifacts, not a throughput guarantee. Two ZFS scans can miss a
change that reverts between them. Version 1 draft captures are incompatible
with the final version 2 format and must be recaptured.

## Next actions

1. Implement the single rerunnable reconciler in bounded slices, beginning
   with signed private capture, compare and dry-run classification. Architect0
   specified that contract in `storage-integrity-design.md`; implementer0 is
   mapping extension points while review runs. Do not infer safe correction
   from the time-separated inventory.
2. Complete strict guarded writer coverage, including osctl wrappers and
   `zfs recv -F`, before any verified-scope or deletion claim. Add approved
   DB-only apply and verify through the same reconciler, then run the required
   tests and review gates. Do not run production apply as part of implementation.
3. Obtain explicit direction before merging either feature branch into its
   named default branch; in particular the inventory branch remains outside
   `vpsfree-maintenance-tasks` `master`. Keep this session active.

The task guide owns repeatable operator instructions. The source investigation
and proposed future compatibility/deployment sequence remain in this session;
they are not executed rollout records.
