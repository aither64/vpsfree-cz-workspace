# Storage profile Admin support — whole-branch review

## Assignment

Independent mandatory **HIGH-risk** review, all four lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Reviewer0
is the retained ready review-purpose member, read-only GPT-6.1 Sol/xhigh.
Use saved settings without override or nested reviewers. Read the canonical
skill/all four references, workspace routes, Admin AGENTS/development/testing
procedures and the current [design](design.md) before inspecting the source.
The final Admin support is committed; the provider implementation is still
in progress and is a separate later review. This review does not declare the
whole storage profile ready or authorize a populated-cluster operation.

## Review result and direct remediation

Reviewer0 completed the assigned four HIGH-risk lanes at the exact range below,
using saved GPT-6.1 Sol/xhigh settings. No Blocking findings. One Important
general/risk compatibility finding in `2323829cc`: validated integer DSL schedule
fields remained integers when compared with RepeatableTask's persisted strings.
This can block valid enrollment reuse and removal for legacy and retained plans.
The accepted direct fix normalizes validated fields to strings at the common
boundary and adds numeric group/backup enrollment, reuse and removal cases for
both plan modes. Focused verification passed eight real-DB examples/0 failures
in 45 seconds with held source hashes unchanged. Log:
`/tmp/storage-numeric-plan-bound-check.d8GL3Zsh/rspec.log`.
Normal Nix sign/amend completed as `46b3bf6f9549eaf579053bc296ebf19c417bb848`,
with all normal hooks passing. The first twenty commits and parent are unchanged;
the reviewed-to-final diff is exactly the three tested paths, and the owning
commit retains its seven-path scope. No wider selector, schema, lock or
confirmation change was introduced. Hook log:
`/tmp/storage-numeric-plan-amend.GFNTMieF/amend.log`.

The reviewer independently checked all 21 commits, complete diff, patch/message
equivalence and all 202 feature blobs. No obsolete history or migration issue:
exactly the two consumed additive migrations below remain unchanged, and the
new scheduler/Plan support adds no migrations. The finding is handled through
mandatory-review step 9; a narrow verified normalization does not require
repeating unaffected review lanes. Provider/package review and retained-root
maintenance/payload acceptance remain separate pending gates.

## Exact source and complete inventory

Session `2026-09-23-storage-redesign`, workspace `/home/aither/workspace/ai/vpsfree.cz`.
Repository/worktree: `worktrees/2026-09-23-storage-redesign/vpsadmin`.
Branch: `2026-09-23-storage-redesign`.
Base/current fetched default: `878a0d10c86060ed2ce62027223832371ca5e49e`.
Reviewed head: `2323829cc79d2d64661825d2f8f9e170ceb98170`; directly remediated
final head: `46b3bf6f9549eaf579053bc296ebf19c417bb848`. Tracked worktree/index
clean at each gate; preexisting untracked
`webui/.phpunit.cache/` is preserved. Full final diff: 202 paths.

Complete 21-commit series:

1. `5a811c7974465b4cc4ae795ed09027fe7474d713` — storage: establish integrity schema and freeze bootstrap
2. `cfbee5ead2948a73eafe57e154868d75db99bde3` — storage: journal observer writes across API and NodeCtld
3. `eb50807171663ad1f2c676beb3a83cfee4d95ca7` — storage: add advisory inventory and reconciliation
4. `98d2154e8bc66795fcd706bd7b35c23f9e9dcd34` — storage: add authenticated freeze API and WebUI
5. `d2e0a367f6d49c9ab9754ecae43a190de6dfb216` — storage: prove strict snapshot dispatch in test mode
6. `8bd4791794055ef0eab401fbe7c334562866bd7f` — storage: document integrity evidence and observer limits
7. `5d4f8d70166fde2e54c5ae77564fffeeef572631` — nodectld: observe bounded local storage activity
8. `c79624c1c1a148a8acdcf9884a8fa53aa9a258e2` — storage: preserve exact GUIDs in signed inventory
9. `a597e69b847422bde7daeb13bf45be81814a8592` — storage: sample node and osctld activity around inventory
10. `d4f9836409492dae55f51f56d1e67bae5bacc8c0` — storage: accept capped settled intents in activity reports
11. `431c0e769154cc3a23d66aaffe05c4f79125316b` — Distinguish completed rollbacks in DB capture overlap
12. `d4223ce97f3fa4a7372d6be54d055896bba65a61` — Keep storage reconciliation replay cold and offline
13. `f9b8a22c90fa60acafad1fbc26b5e228844c0a41` — api: canonicalize captured storage GUID decimals
14. `d6c590f1ac1f9fb13a70d3aa3a894fae07f0ddb7` — storage: version offline coverage conservatively
15. `b7a8d310fa14951871a1efb20090977577473dce` — Bound storage reconciler capture to current evidence
16. `d5bfe29d797416e5347127f1231c5af4af2465c5` — Restore pooled DB isolation after storage capture
17. `2bfdbad31ad76c09a66cfb9b130c5c14ed81d111` — api: avoid fixture IP address collisions
18. `e155614dd16a7aacd4b21502f91470990d66ecb5` — Use the shared transient node exchange for inventory
19. `fea7d275bfe29330717f46b9b4f732f77675168b` — flake: vpsadminos 8e44a5124 -> 8d05dc3ae
20. `a242eee839426724f2b96cafc24b8f2d5c245d0f` — api: support bounded scheduler intervals and task refresh
21. `2323829cc79d2d64661825d2f8f9e170ceb98170` — api: serialize dataset plan membership and retain shared templates

The first nineteen commits were independently reviewed and published before
this slice; their supported behavior and externally consumed evidence paths
remain necessary. The last two commits are distinct prerequisites: generic
scheduler grammar/reload, then common Plan locking and retained-template
semantics. No transitional profile implementation or intermediate migration
was added. Source, tests and owning explanations accompany each behavior.
The obsolete prior OS pin was already removed before the published series;
one generated current-provider pin remains. Inspect the complete series and
final diff and explicitly conclude on obsolete history and migration lineage.

Immediately before this review, upstream advanced only PHP dependency files
`webui/composer.lock` and `webui/php-packages.nix`. A normal signed replay onto
this base preserved all 21 patches/messages, all 202 feature blobs and exact
base-to-head binary patch SHA256
`a52087a4bb9f6b09c0fa8710daf8f4eb6ef0a3ea682b9d53f86b2f7a15e17cd8`.
All range-diff mappings are `=`. Backup head `96ab16726b516ee601b3f366439f1079a1030d19`
is retained. Private parity evidence is in
`/tmp/storage-admin-default-refresh.Dqw9aj2I`; reviewer need not open private logs.

## Migration provenance

Exactly two feature migrations, unchanged from the published/externally
consumed branch and the populated disposable cluster:

- `20260924210000_add_storage_integrity_foundation.rb`, Git blob
  `7d929052f314d5a821b2ce65345680c0740b1b0c`.
- `20260926100000_add_bounded_storage_capture_indexes.rb`, Git blob
  `d60868e615024c70fb4b87b736a2466ceb8349db`.

Core schema blob remains `e9aa952df7b94451c5491c965d22962265c8f545`.
These versions were published and consumed by disposable runtime/migration
trials, including the retained current cluster. They are not merged/released
or established as applied in production. Preserve their versions/content,
bootstrap and additive rollback contract. The new scheduler/Plan commits add
**no migrations**, schema, Node protocol or capture-format change.

## Requested behavior and ownership

The user found that a created VPS lacked a backup DIP and requested production-like
storage fixtures and automation. They approved this plan: snapshots `*/5`,
backups `2-59/10`, dev refresh 60 seconds (production default 10800), new source
retention 2/3/1800 and backup 2/5/3600, NAS 1 GiB. Existing VPS/files/quotas/
retention/namespace/resource allocations are preserved; no reset. Catch-up
never rotates; later ordinary Backup may rotate under unchanged policy.
Concrete dev pool selection and policy belong in the enabled provider overlay,
not production site hooks or a new generic profile registry.

Scheduler acceptance: strict wildcard/integer/wildcard-step/inclusive-range-step
syntax with field/step bounds and complete-string validation; exact five/ten
minute matching across hour rollover; invalid persisted task replacement keeps
the previous complete loaded set; one positive configured refresh interval.
One RepeatableTask per action, not many minute tasks or a second scheduler.

Plan acceptance: `keep_empty_group_snapshots:false` preserves lazy group lifecycle
and first-open backup selection. True uses prebootstrapped exact shared action/
sole task and adds/removes only source membership; shared IDs survive last-member
removal and source-chain rollback. Existing membership shape/schedule/destination
is validated on repeat enrollment. Sole eligible backup destination is required
only for true; provider adds exact configured destination validation.
Common SQL lock order is admission, persisted Plan row, action/task; source
Dataset/DIP foreign locks and pending confirmations refuse conflicting edits.
Same outer-chain ownership is supported through a read-only Confirmable reader.
Direct Dataset Plan API paths use these common guards and ordinary operation
refusals. Savepoints prevent caught staging errors leaking provisional rows.

Actual consumers include direct Dataset Plan add/remove, normal migration/clone
plan copying and provider hook/catch-up enrollment. Inspect those call sites and
ordinary default plans. True-plan configuration must be provisioned separately;
source chains cannot own shared creation/deletion confirmations. Reused logical
Datasets must not go through Dataset::Create merely to attach a backup DIP.
Provider helper/physical provisioning and its rollback/payload proof remain later
work, not claimed by this Admin change.

## Compatibility and deployment

Deploy the new scheduler and Plan code before interval schedules/true definitions.
Keep the definition loaded while retiring enrollment/tasks, drain admitted work
and unregister memberships before rolling code back. Old scheduler silently
truncates the new interval strings; old DSL cannot maintain retained templates.
No new production schedule, strict dispatch, identity publication, node_quiet,
repair_ready, executable plan or APPLY is enabled. Existing unsigned observer
5204 and signed operator 5290/5291 boundaries stay as previously deployed.

Admin still pins reviewed OS `8d05dc3ae1fb71c1385609990acdf093af49ceec`. Site
configuration follows its own OS graph; no OS/shared-host upgrade is implied.
The new provider branch on c56 has only its generated generic input commit
`da058353ac4a43f08313d02b485c1578f3547378` committed, selecting reviewed runtime
`2b67af62b40149e7554bab0c31b139cd52c963c1` policy 3. Maintenance/profile source is
still uncommitted. Later paired package review, retained-root maintenance
regression and in-place payload acceptance are mandatory before activation/use.
No default-branch integration is authorized.

## Quick checks and documentation

Fresh Luna/low scheduler check: 22 examples/0 failures; six Ruby syntax and
RuboCop checks clean, Nix parse/format clean, normal signed hooks passed.
Plan real MariaDB selection reached 57 examples: 56 passed, one fixture tried
an impossible GroupSnapshot duplicate. The fixture now asserts the real unique
constraint and exercises schema-possible EnvironmentDatasetPlan ambiguity;
its narrow rerun at line 245 passed 1/0. Runtime unchanged between those runs.
Normal signed Plan hooks then passed Nixfmt, MigrationSpecs, both i18n checks
and RuboCop. All seven committed hashes matched the tested worktree bytes.
Only two preexisting lint directive comments moved; their code is unchanged.
Selector checks: 18 runs/77 assertions/0 failures. API topic coverage patterns
already cover both changed specs exactly once; no selector expansion needed.

Normal final replay hooks passed and patch equivalence preserves that evidence.
Focused PHP dependency check after replay passed 5 tests/17 assertions.
No unexpected kernel build. Logs are private:
`/tmp/storage-profile-scheduler-check.XAVcqHHF`,
`/tmp/storage-plan-namespace-check.ckLoxIBo`,
`/tmp/storage-plan-fixture-check.wsS3tA3K`,
`/tmp/storage-plan-normal-commit.G24Zov6t`,
`/tmp/storage-admin-default-refresh.Dqw9aj2I`.
Broad exact-head CI and real profile runtime acceptance remain pending.

Owning new explanations: Admin `docs/scheduler.md` and
`docs/storage/dataset-plans.md`, linked by their indexes. They cover supported
syntax, shared ownership, locking/confirmations and rolling rollback. Current
[plan](plan.md), [state](state.md) and [design](design.md) keep prepared/actual
operations separate. Prior independent review retained a documentation advisory
about restrictive identity ownership vs copied scope/target metadata; no new
identity publication or schema change is introduced here. Prior global retained-
lock fan-out/unknown terminal and child coverage limits remain recorded.

Please return ordered findings and explicit complete-history/migration conclusions.
This is a source clearance gate, not a production, reset or deployment approval.
