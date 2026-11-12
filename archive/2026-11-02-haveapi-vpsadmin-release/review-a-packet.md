# Final review packet: package A

## Request and acceptance

Initial user request: consume published HaveAPI0.32.2 in vpsAdmin and merge to
master when verified without waiting for long CI; regenerate Go/Rust/TypeScript,
conditionally merge/minor-release/publish clients with code changes; finally
update/merge configuration vpsadmin channel. This packet reviews completed A,
not future client/config deliverables. User explicitly authorizes named merges;
review does not grant additional authority. No deployment requested.

## Exact committed range

Repository git@github.com:vpsfreecz/vpsadmin.git, target master.
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-haveapi-vpsadmin-release/vpsadmin.
Base1d4869b6e81dd60916ecb96688ca14a192000b1f.
Head5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5, clean.
Complete series:5586ea8ab api: update HaveAPI dependencies to0.32.2.
Full diff: git diff BASE..HEAD,13files47insertions47deletions.
Single coherent dependency/exporter stream. No repeated/superseded pins or
obsolete approach commits; source setup failures left no implementation commits.
No migrations added/edited/removed; no branch migration lineage or migration
release/deployment/external-use boundary. Independently conclude history,
consolidation and migrations, including no migrations.

## Final behavior and boundaries

API's five HaveAPI dependencies, packaged API/client/download-mounter locks and
Nix hashes move0.32.1->0.32.2. Isolated exporter Gemfile/declaration/runtime
refusal and CLI/docs exact reproducibility references match0.32.2. Existing
OAuth minimum0.32.1 remains. No unrelated dependency versions, source gem
publication, database/schema/protocol/API-version, node, UI behavior or machine
change. Generated package metadata and exporter exact version form one atomic
coherence update; no independently unrelated behavior bundled.

HaveAPI source is released1ef9b204ba45bb261d3334be5c555cc1856b713b/tagv0.32.2,
public run41529223599 passed. All five gem registry SHA256 and npm availability
independently read by lead; actual downloaded gem bytes match generated Nix hashes
in vpsadmin-gem-hashes.json. Existing generated clients retain runtime pairs;
new TS generation later uses exact npm0.32.0 per upstream compatibility contract.
Old/new framework versions share API7.0/protocol2.0, no DB migration or coordinated
machine update. Rollback restores prior dependency/exporter metadata together.

## Documentation and evidence

Read plan.md, state.md, design.md and vpsadmin-package.md in this directory.
Project docs checked/changed: docs/api-schema-export.md, docs/api-client-examples.md;
changes only reflect exact exporter reproducibility coupling. Main-agent writing
pass applied. Individual release evidence stays here; no project rollout document.
Owning component is HaveAPI server/generators, consumed by API and exported
client/documentation routes; packaged client/download-mounter consume Ruby client.
Representative consumers are the package locks, exporter and focused doc specs.

Quick gate passed before review:14docs/APIboot/version specs0failures;
14database-free exporter safety/snapshot specs0failures,3tooling syntax checks,
RuboCop3files0offenses,diff--check, actual five HaveAPI versions0.32.2.
Required precommit MigrationSpecs,Nixfmt,WebuiI18n,RuboCop,ApiI18n and commit-msg
hooks all passed. Logs vpsadmin-quick-checks.log, vpsadmin-commit.log; metadata
vpsadmin-metadata-direct.log. Environment failures were diagnostic/root bundle
activation only; corrected without task-source workaround, operations reconciled.

Long services-up has NOT started. Repository requires it after HaveAPI update;
lead launches focused one-VM packaged-content gate after final review without
waiting broad CI. Exports twice from exact reviewed clean head may run alongside;
D merge/release later requires exportedHEAD==integratedAHEAD and fresh ancestry.

## Review selection and scope

High risk classification for framework/public metadata compatibility across
packaged API/exporter/generated consumers, although patch diff is small.
Retained independent reviewer0, Sol/gpt-6.1-sol xhigh, read_only, no overrides.
Apply general, architecture/repetition, scope/proportionality, risk/compatibility
lanes from mandatory-change-review skill; read each reference in full. Prioritize
scope/correctness and exact package coherence. Do review directly; no nested
reviewers, no edits, no tests/build launches, no deployment/integration.
Report concrete findings ordered Blocking/Important/Advisory; explicit whole
series/repeated streams/migration conclusion and residual check gap required.
Write review-a-result.md and report to lead.
