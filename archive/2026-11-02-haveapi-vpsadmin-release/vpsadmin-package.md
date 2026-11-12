# vpsAdmin package A

Owner: implementer0. Current phase: reviewed source and both schema exports
complete; lead owns the packaged `services-up` check and integration. This record describes source and
verification preparation; no integration or deployment has occurred.

## Identity and preparation

- `dev-session current` returned `2026-11-02-haveapi-vpsadmin-release`.
  `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` matched that exact slug and
  `/home/aither/workspace/ai/vpsfree.cz` and the trusted thread binding.
- Retained roster: implementer0, Sol/xhigh, `workspace_write`; installed
  execution policy is full access. Initial plan/state commit `e263572c6`
  predates application edits. Architect-owned `design.md` was read before edits.
- Canonical bare clone: `repos/vpsadmin.git`; SSH origin
  `git@github.com:vpsfreecz/vpsadmin.git`; target `master`.
- Registered branch: `2026-11-02-haveapi-vpsadmin-release`; worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-haveapi-vpsadmin-release/vpsadmin`.
- Fresh fetched initial base: `1d4869b6e81dd60916ecb96688ca14a192000b1f`.
  Managed worktree creation returned exit 1 from an inherited Overcommit
  post-checkout configuration-signature check, but both branch/worktree and the
  ordinary portal registration were created. The resulting checkout was clean.
  No creation retry or branch deletion was needed.
- Root development shell dry run needed only its shell derivation; toolchain
  dependencies were available. A fresh pinned-catalog Luna/low utility ran
  `nix develop .#vpsadmin --command bash -c 'bundle check && ruby --version && bundle exec overcommit --version'`.
  It passed in 41 seconds: 7 development dependencies, 50 gems, Ruby 3.4.9,
  Overcommit 0.74.0. Log: `vpsadmin-environment-preparation.log`.
- Declared `.overcommit.yml` and four custom hooks were inspected. Normal
  Overcommit installation/signing was used, without disabling hooks or signature
  verification. Root shell commands use the declared repository environment.
- Read workspace AGENTS and sessions/git/lifecycle/commits/verification/
  documentation procedures, documentation and monitor skills, vpsAdmin AGENTS,
  development/testing procedures, docs index and API schema export guide.

## Publication and implementation contract

The lead released the registry gate after peer release run `41529223599`,
attempt 1, succeeded. Released HaveAPI source:
`1ef9b204ba45bb261d3334be5c555cc1856b713b`; annotated tag object:
`7f8f656ca7655bafaf2cf5e7095573806085a442`. Public release:
<https://github.com/vpsfreecz/haveapi/releases/tag/v0.32.2>.
The lead's final registry receipt confirms all five gem hashes match approved
manifest SHA256 `7c53624cc059434279e6eba6f8a9ec151a57897f41e96f0b1d261e1b58fa728b`.
Ordinary local dependency resolution and generated hashes are verified below
independently. No peer session files are accessed.

One logical update stream raises all five API HaveAPI dependencies to 0.32.2,
updates the API/client/download-mounter package metadata, and retains the
exporter's exact declaration check and runtime refusal at 0.32.2. The lead
provided the final main-agent prose pass for `docs/api-schema-export.md`.
No DB/schema migration, persisted-state, protocol, API-version or node change is
intended. No first-party source-gem task/build ID/publication is authorized.

## Verification and remaining work

- Three narrow tasks passed using the root development shell's installed rake:
  `nix develop .#vpsadmin --command bash -c 'rake vpsadmin:gems:api vpsadmin:gems:client vpsadmin:gems:download_mounter'`.
  Log: `vpsadmin-metadata-direct.log`. Complete lock/gemset comparison found only
  HaveAPI 0.32.1 to 0.32.2 changes, with no unrelated dependency version churn.
  All five API gems and both client consumers resolve 0.32.2; generated Nix32
  SHA256 values match downloaded RubyGems bytes (`vpsadmin-gem-hashes.json`).
- The initially prescribed `bundle exec rake` invocation failed in child
  `bundix -l` because inherited root Bundler activation reached bundix's wrapped
  Ruby environment. It removed the API lock before failing; the corrected
  ordinary tasks regenerated it. A delayed utility retry overlapped one failed
  parent attempt; both ended at that same failure and were terminal before the
  corrected run. The utility is completed; it was never reused for another
  operation. Original error: `vpsadmin-metadata.log`.
- API setup installed 122 gems. An initial diagnostic `ruby -rjson` activated a
  default JSON before Bundler, causing a version conflict before specs. Changing
  the diagnostic to `require 'json'` inside Ruby after Bundler setup resolved it;
  no source or dependency workaround was made. Original log:
  `vpsadmin-api-focused.log`.
- Corrected focused gate passed (`vpsadmin-quick-checks.log`): 14 documentation,
  API boot and API version examples, 0 failures (82.97 seconds execution,
  13.49 seconds load); 14 database-free exporter safety/snapshot examples,
  0 failures (0.435 seconds); all five loaded HaveAPI gem versions 0.32.2;
  three touched tooling syntax checks and RuboCop checks passed, as did
  `git diff --check`.
- Isolated exporter `--prepare` passed (`vpsadmin-exporter-prepare.log`); its
  ignored tooling lock independently resolves all five HaveAPI gems to 0.32.2.
- Final source diff: 13 files, 47 insertions/47 deletions, including two
  additional consistency-only pin corrections in CLI help and the exporter link
  in `docs/api-client-examples.md`. The supported OAuth minimum remains 0.32.1.
  The lead performed the main-agent prose pass for each touched sentence.
- Final commit `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5` passed declared
  pre-commit hooks (MigrationSpecs, Nixfmt, WebuiI18n, RuboCop, ApiI18n) and all
  commit-message hooks (`vpsadmin-commit.log`). The worktree is clean.
- Complete history from base `1d4869b6e81dd60916ecb96688ca14a192000b1f` is
  exactly one commit, `api: update HaveAPI dependencies to 0.32.2`. There is one
  final dependency update stream and no superseded pins or abandoned approach.
  No migration file is added, edited or removed; no migration lineage is created.
- Fresh fetch confirmed `origin/master` still equals the initial base. The
  feature branch was published over SSH from the declared shell, and fresh
  `git ls-remote --heads` confirms exact remote head
  `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5` (`vpsadmin-push.log`). An initial
  ambient-shell push refused Overcommit's differing configuration signature
  before any remote update. Reusable diagnosis is retained in
  [the Bundler/bundix note](../../notes/vpsadmin/2026-11-02-bundix-root-bundler.md).
- Lead schedules `./test-runner.sh test services-up` after final review; do not
  await broad GitHub CI. Unexpected local kernel builds must be stopped and
  investigated. No resource claim or machine reservation is needed here.
- After final review acceptance, export twice from clean exact final intended
  vpsAdmin source, using fresh temporary databases, alongside the lead's
  `services-up` check. The lead accepted this scheduling improvement; remote
  integration need not precede export. Any A head change invalidates both
  export identities and requires a repeat and TypeScript reconciliation.
  Retain each schema/provenance/tooling
  lock together and prove matching canonical bytes, API/protocol identity,
  final source, HaveAPI 0.32.2 and all six bundled plugins for TypeScript.

## Reviewed-source export receipt

The lead accepted final independent review without findings for exact source
`5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`, including whole history and no
migrations. The lead then released the export gate. No source or head changed.

Two separate `tools/export-api-schema --api-version 7.0 --output DIR` processes
ran sequentially from the declared root Nix shell, after checking exact HEAD and
clean Git status. Each exporter used the existing automatic test-database runner
with a fresh `Dir.mktmpdir` database and its normal native shutdown/prune on exit.
The complete batch exited 0. No operation or temporary database remains owned by
this export batch. Log: `vpsadmin-schema-exports.log`.

The output directories, each retaining all three files together, are:

- `vpsadmin-schema-export-1/`
- `vpsadmin-schema-export-2/`

All three files are byte-identical across the two independent exports:

| Artifact | SHA256 |
| --- | --- |
| `schema.json` | `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794` |
| `provenance.json` | `d51cfb24217fb381f66c1a0eb46168c637fea7ec988beb7e54b2d9a679ad81b6` |
| `tooling.Gemfile.lock` | `62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c` |

Source is `git@github.com:vpsfreecz/vpsadmin.git` at exact reviewed head above;
API 7.0, protocol 2.0, profile `vpsadmin-full-fixture`, locale English. Inventory:
151 resources, 519 actions, 8720 parameters; scopes digest
`2e575a597445cf4b4277596c5f7f990b04f75a56dca2a0a3ce80d5c7a2abe177`.
Database: MariaDB 11.4.12. Exporter Gemfile SHA256:
`87df3509b79a68dcf55f4f344017c619a8fcf0dbb9e70e576a2d2d39891a8ef2`.
All five loaded HaveAPI gems are 0.32.2, with byte hashes matching the independent
registry-download receipt above. Full gem/input/plugin graph is in each
`provenance.json`, the retained lock, and `vpsadmin-schema-export-receipt.json`.

All fixture-input digests were independently recomputed from the clean source:

| Input | SHA256 |
| --- | --- |
| `api/config/dataset_plans.rb` | `33397be38d3ab9fd2b93ab8210156e0bec6bb303cc521f512b2255ddb6ff78b1` |
| `api/config/dataset_properties.rb` | `d4e80f78ecafccd75c5adc5e87f058beb16c4a38f7e2108e5ac3ad8e1e30f7f3` |
| `api/db/schema.rb` | `995b1f5dbd7f58d1e7dd8be7ca94459e6472e45a09303dc4565e4ca4cd084ad8` |
| `api/spec/support/db_setup.rb` | `3bf201e552741272f3a79b8c631e5eed0e295b4e4c8ec8a30a5d66980bcddc9c` |
| `api/spec/support/spec_plugins.rb` | `b930102255afc99583a37b6229c760be2afb9ed2f2537fc5ba41c091f08bfea2` |
| `api/spec/support/spec_seed.rb` | `d0836d875dea8ed8046ff2a925dc8176a3a0fa2a79bacb3b3369525da3700d31` |
| `tools/test_db.rb` | `b9faee4880ac40526808eae5aa408e3160adff5f4efe92eddfdaee115eb29e5c` |

Each plugin is version 4.2.1. Its source digest was independently recomputed from
the canonical hash map of all Git-tracked files below its plugin directory:

| Plugin | Source SHA256 | Applied existing migration versions |
| --- | --- | --- |
| monitoring | `6a1aefecdbf92031cf0d18bd1a2179d5681d83c707d4b33b681d47e6c617ec9b` | 20170408184500, 20230123085900, 20231105124400 |
| newslog | `1b922e7de93274b1d4752b160b33be7a9603b196324381746c7a022c06a47d37` | 20170201082030, 20260706210000 |
| outage_reports | `b575d3086c53a9d77af6e8fce94658ec1d6004b8e5c959aeb68817178ed35a5d` | 20170223191015, 20201129113300, 20240123092400, 20240124093200, 20240124185400, 20260601121000 |
| payments | `a842dd5796fc05305a5e0ebac2694a145a86965ebf657e6599b1f12f0fff6a86` | 20170121214350, 20260706212000, 20260905180000 |
| requests | `daca23ec4afeedd258e3a71ffba57d8c76b238b904bc0af256080f3d35df26c7` | 20170122083340, 20170908165000, 20201126142500, 20260606223100 |
| webui | `8b3faedb05e40874cfb80f56e697e4972fc77b357cc44f401d70f5d4ea168c62` | 20170201093720, 20260607190000, 20260706211000 |

Package D can consume export 1's complete three-file set. Before D integration
or publication, the lead must establish fresh remote evidence that this exact
exported SHA equals A's integrated final SHA. Any A rebase/head change invalidates
both exports and requires fresh exports and D provenance reconciliation.

Stable portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/>.
