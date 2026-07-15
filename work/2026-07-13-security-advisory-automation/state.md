# 2026-07-13-security-advisory-automation

## Current status

### 2026-07-15 final implementation checkpoint

- The source histories have been rewritten into their owning functional
  commits. Current clean heads are vpsAdmin
  `fb11991d42f4f0cb18298137c8ceed8278dbb9ae`, vpsAdminOS
  `dbc03d00508b89093ecafc5e5abdcfc6bb5bdfbb`, and
  security-advisories `ce0aca81789c7dec31a939ddd5c88ebeafdc7281`.
  The vpsAdminOS feature branch is published at that head; downstream pins and
  the other rewritten branch updates remain pending final verification.
- vpsAdmin's vpsAdminOS input is an isolated generated lock commit and resolves
  the exact final vpsAdminOS head. The earlier intermediate lock revision was
  folded out of history.
- vpsAdmin verification before mandatory review was green: the schema-4
  reporter had 4 examples with no failures; status and record-operation
  coverage has 31 examples with no
  failures; normalized model/resource coverage has 19 examples with no
  failures; migration coverage has 2 examples with no failures; WebUI evidence
  coverage has 5 tests and 17 assertions; and the complete Overcommit gate
  passes migration mapping, WebUI/API i18n, Nixfmt, RuboCop, and PHP CS Fixer.
- security-advisories passes its full 67-example RSpec suite after review
  remediation, RuboCop reports no offenses, and its installed pre-commit hook
  passes.
- vpsAdminOS passes its Overcommit gate and targeted flake evaluation. Its
  repository-wide `nix flake check --no-build` still stops at the existing
  invalid `overlays.all` flake-output type; this is unrelated to the changed
  metadata module and is not treated as validation of this feature.
- A default vpsAdmin development-shell reporter invocation could not load the
  native libosctl extension. Re-running the same spec in the declared
  `.#libnodectld` component shell passed all 4 examples. Migration specs are
  also kept in their own process because their connection switching invalidates
  the ordinary shared test database when combined with model/resource specs.
- Mandatory review found that legacy report schemas could still produce a
  confident assessment, missing native dirty metadata was treated as clean,
  and configured kernel parameters remained in intermediate unmerged commits.
  The evaluator and historical attestations now require schema 4, nodectld
  falls back to closure confctl metadata when native dirty state is unknown,
  and all configured-parameter behavior was folded out of the feature history.
  Commit messages now describe the schema-4 contract and rolling behavior.
- The top-level dev-cluster source-identity plumbing is formatted,
  shell-checked, and committed as `069bd60`. Only this initiative's argument
  and Node metadata hunks were staged; unrelated notification work in the
  shared checkout remains untouched.

### 2026-07-15 exact closure metadata implementation

- Work resumed from heads vpsAdmin `c5803845c`, vpsAdminOS `6a8f1d355`,
  security-advisories `7e3979b`, KB contract `1adabf7`, and configuration
  `e8e60e4d`. All are still unmerged feature branches.
- vpsAdminOS evidence schema 4 removes configured kernel parameters, records
  native revision dirty state, and no longer emits the false `staging`
  fallback. vpsAdmin's native metadata likewise no longer emits `dev`.
- nodectld reports only the ordered `/proc/cmdline` parameters and all six
  booted/current vpsAdminOS/vpsAdmin/nixpkgs identities. It uses closure-native
  metadata first and the matching closure's confctl inputs file only as an
  exact-revision fallback. `/proc/config.gz` remains the no-reboot kernel-config
  fallback for an older booted closure. `/etc/os-release` is not used.
- The normalized database/API stores revision provenance and dirty state for
  current identities and history changes. WebUI links only full Git hashes,
  labels invalid or absent identities unavailable, and marks dirty native
  revisions as modified. Kernel parameter pages now show only the actual boot
  sequence.
- The security-advisories collector/evaluator is being updated to the same
  booted-only and exact-provenance contract. Its focused evaluator tests pass;
  the complete suite and RuboCop remain pending.
- Targeted vpsAdmin verification completed so far: libnodectld 4 examples,
  migration 2 examples, and normalized model/resource 19 examples all pass.
  Status/record-operation focused tests also completed without failures.
- The workspace dev-cluster launcher now derives exact worktree HEAD/dirty
  metadata and injects it into Node closures. These top-level edits overlap a
  shared dirty checkout only in `nix/test.nix`; the unrelated notification
  changes remain untouched and must not be staged in this initiative.
- `nix develop .#webui --command webui/lang/scripts/locales-update` failed
  because the shell changes into `webui`, duplicating the path. The correct
  invocation is `nix develop .#webui --command lang/scripts/locales-update`.


- The requested Node evidence presentation correction is implemented and
  pushed at vpsAdmin head
  `c5803845cc841d0c415b9009fe5878dcea23589c`. Parameter comparison rows follow
  booted positions, raw command lines render as wrapping code, passive
  explanations use a neutral content component, and current/history sysctl
  tables use compact fixed-width layouts.
- Full WebUI PHPUnit passes with 72 tests and 267 assertions. PHP syntax,
  JavaScript syntax, gettext health, PHP CS Fixer, `git diff --check`, and all
  vpsAdmin pre-commit hooks pass. The focused `webui#admin-cluster` integration
  passes end to end, including exact ordering, code markup, table structure,
  and browser width/overflow assertions.
- The first browser integration attempt found a shared fixture still calling
  revision-checked advisory publication without `expected_content_revision`.
  Focused tip commit `c5803845c` passes the fixture's current revision; the
  preserved test log established this as a setup failure before Chromium, and
  the cached rerun completed successfully.
- vpsfree-cz-configuration was rebuilt from feature base `e1cc165c` with
  exactly three generated commits: `751bb183` for `vpsadminosStaging`,
  `81dea6ca` for `vpsadminStaging`, and `e8e60e4d` for `vpsadminServices`.
  The final head is `e8e60e4d`, with vpsAdmin channels pinned to `c5803845c`
  and vpsAdminOS staging pinned to `6a8f1d355`.
- The KB contract is repinned and pushed at `1adabf7`; its complete check
  passes with 37 controls, 65 bindings, 9 exceptions, and 118 PNG variants.
  These administrator-only pages have no current end-user KB page or capture
  binding, so no KB candidate, staging, or production write is required.
- The mandatory fresh-context review initially blocked on repeated same-input
  pins and advised exact row assertions. After those fixes it cleared the
  presentation gate. The same reviewer examined the integration-discovered
  fixture commit and final repins and again found no Blocking, Important, or
  Advisory findings; no residual browser test gap remains.
- The bridge-network development cluster is running and ready with the updated
  services generation; WebUI and API both return HTTP 200 using the development
  CA. No production deployment or write was performed.
- No API/database/protocol compatibility changes are introduced. Deployment
  can update the vpsAdmin services independently; older Nodes continue to
  report the same evidence and rollback reads the unchanged schema.

- The approved relational evidence normalization is complete. Current and
  immutable event snapshots, kernel parameters/modules, security settings,
  livepatch/eBPF state, errors, and parsed kernel options use normalized
  tables. Top-level typed HaveAPI resources expose filterable rows, while the
  superseded opaque route and evidence blobs never appear in feature history.
- The final feedback implementation is committed on top of current
  `origin/master`/`origin/staging`. It replaces CVE-specific reporter fields
  with complete kernel configuration plus generic deployment/runtime inputs,
  excludes service-only Nodes, adds a digest-keyed configuration catalog and
  per-Node readiness preflight, generalizes repository instructions, and
  rewrites all five public texts for standalone clarity.
- The earlier requested implementation and mandatory-review fixes remain the
  base of this work. The final heads and exact downstream pins are recorded in
  the final feedback checkpoint below. The dev cluster has been rebuilt and
  freshly booted from those final vpsAdmin/vpsAdminOS worktrees.
- Exact feature revisions are pinned for vpsAdminOS/vpsAdmin staging and for
  the vpsAdmin services channel used by a later coordinated production service
  rollout. The production vpsAdminOS Node input is unchanged. No production
  deployment, vpsAdmin API write, KB staging, or KB publication has occurred.
- The required fresh standalone review of the final-feedback changes is
  complete. All blocking and important findings were resolved before
  integration: schema-v2 evidence is fail-closed, reconstruction and exact
  reporting share a Node row lock, and the new repository history is clean.
  confctl remains absent from the evidence contract: nodectld reports booted
  and activated system closures directly in every environment.
- The initiative development cluster was cleanly reset after the final history
  rewrite and is running and ready with the `single` topology on the bridge
  network. Its kernel-host Node reports complete normalized schema-v2 evidence;
  service-only Nodes retain no kernel evidence.
- Live per-Node conclusions are intentionally not fabricated from repository
  pins. Until the feature is deployed and exact evidence is collected, the five
  dossiers produce `unknown` rows that may be reviewed in a draft but cannot be
  published.

## 2026-07-14 final feedback verification

- `security-advisories`: all test files pass, all five dossiers validate, Ruby
  syntax and `git diff --check` pass.
- `libnodectld`: generic evidence, publish acknowledgement, and service-role
  suppression specs pass (5 examples).
- vpsAdmin migration/rollback specs pass (2 examples). A newly added Node API
  example initially omitted required `NodeCurrentStatus` fixture fields;
  adding the real non-null fields fixed the fixture and the focused example
  passes. This was a test-data issue, not an implementation failure.
- vpsAdminOS `nixfmt --check` and full system evaluation pass.
- The combined vpsAdmin API/evidence suite passes (57 examples), as do all
  repository pre-commit hooks: migration specs, API/WebUI i18n, Nixfmt,
  RuboCop, and PHP CS Fixer.
- The refreshed KB contract passes `nix develop -c bin/check`: 34 controls,
  29 paths, 32 capture concepts, 3 selectors, 65 bindings, 9 exceptions, and
  all 118 PNG variants.

## 2026-07-14 final feedback commit checkpoint

- `vpsadmin` head `70d4f4e5e8020113405c08b3ffba7d5cacc26c74`
  is pushed. Its seven feature commits are based on `origin/master`
  `1a4fa3031`; the final separate flake commit pins vpsAdminOS
  `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`.
- `vpsadminos` head `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`
  is pushed and based on `origin/staging` `ff9e49b20`.
- `vpsfree-cz-configuration` head
  `7d946a167b69068499ad0ca3474253d67de244b2` has three generated input
  commits: staging vpsAdminOS at `d47ba226...`, staging vpsAdmin at
  `70d4f4e5...`, and the vpsAdmin services channel at `70d4f4e5...`. It is
  pushed.
- `vpsadmin-kb-captures` head
  `f1b91c197e908e16b7b3c26bce2556338459fef5` pins vpsAdmin
  `70d4f4e5e8020113405c08b3ffba7d5cacc26c74`. It is pushed.
- `security-advisories` head
  `0d06b29d2af97699bc440d15d46c496e70ba3ef2` separates general assessment
  guidance, generic evidence evaluation, read-only readiness, and standalone
  public texts. Its GitHub repository still does not exist, so it remains
  local.
- All five project worktrees are clean. Final live-update, mixed-version, and
  fresh-boot integration checks pass.

## 2026-07-14 mandatory final-feedback review

- The standalone reviewer found that schema-v2 payload fields could be omitted
  and that an event configuration digest could be absent from the catalog when
  a dossier had no required kernel options. The receiver now requires every
  generic evidence component, the API emits explicit completeness gaps for
  older stored rows, and the evaluator requires every assessed configuration
  to resolve through the catalog or an explicit historical attestation.
- Reconstruction and exact Node reporting previously used independent event
  transactions. Both now serialize on the same Node row lock; regression
  coverage proves both operations use that lock and exact evidence remains the
  current record.
- Interactive-rebase status text was found in the first twelve
  `security-advisories` commit bodies. The complete orphan history was rewritten
  to retain only the intended subject and rationale.
- The two newly added Czech source labels now use invariant `node`, and the
  stale handoff revision was corrected. No additional functional bundles or
  unrelated changes were found by the reviewer.
- Focused post-fix verification passes: 33 vpsAdmin evidence/history examples,
  27 evaluator tests, the complete 50-test security-advisories suite, all five
  dossier validations, and the full vpsAdmin hook suite.

## 2026-07-14 final mixed-version hardening

- Live activation exposed one additional rolling-upgrade case: the running dev
  Node was still booted from an older closure whose metadata had no
  `schemaVersion` or generic kernel parameters, while its newly activated
  closure had schema 2. Defaulting the old fields to empty values could have
  made incomplete boot evidence appear complete.
- nodectld now validates both booted and current metadata as schema 2 before
  using them. A mixed-version Node reports an explicit `booted_metadata` or
  `current_metadata` error; the API preserves that gap and the evaluator must
  return `unknown`. A legacy-boot-metadata regression was folded into the
  original generic reporter commit.
- The dev cluster first verified the mixed state end to end: vpsAdmin stored
  schema 2 for `dev-node1` with `booted_metadata: schema version 2 metadata is
  unavailable`. A subsequent fresh boot used the final closure for both
  `/run/booted-system` and `/run/current-system` and replaced the gap with a
  complete error-free report.

## Repositories and revisions

### vpsadmin

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadmin`
- Base: `1a4fa3031` (current `origin/master` at final rebase)
- Head: `70d4f4e5e8020113405c08b3ffba7d5cacc26c74`, pushed to `origin`
- Commits:
  - `0b2cdc3c3 api: lock security advisory draft revisions`
  - `39d887ef8 api: reconstruct Node kernel history`
  - `09dcef90c api: store Node security evidence`
  - `6e78b2e80 libnodectld: report generic Node security evidence`
  - `ca210eac6 webui: show Node kernel history`
  - `17e691cba api: harden security advisory draft synchronization`
  - `70d4f4e5e flake: vpsadminos 849282e6b -> d47ba226a`

### vpsadminos

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadminos`
- Base: `ff9e49b20` (current `origin/staging` at final rebase)
- Head: `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, pushed to `origin`
- Commits:
  - `e6a5835f6 os: expose booted kernel build evidence`
  - `897580c12 os: record livepatch application time`
  - `d47ba226a os: expose eBPF live-patch link metadata`

### vpsfree-cz-configuration

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsfree-cz-configuration`
- Base: `e1cc165c` (`origin/master` when created)
- Head: `7d946a167b69068499ad0ca3474253d67de244b2`, pushed to `origin`
- Commits:
  - `5b558cca inputs: set vpsadminosStaging to d47ba226`
  - `a1b92bf9 inputs: set vpsadminStaging to 70d4f4e5`
  - `7d946a16 inputs: set vpsadminServices to 70d4f4e5`
- The input commits were generated with `confctl`. `vpsadminServices` feeds the
  production API/WebUI service channel, so its pin prepares a future
  coordinated deployment; it has not deployed anything. The production
  vpsAdminOS Node input remains unchanged. Configuration pins select the
  feature but are not part of the evidence contract.

### vpsadmin-kb-captures

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadmin-kb-captures`
- Base: `470b759`
- Head: `f1b91c197e908e16b7b3c26bce2556338459fef5`, pushed to `origin`
- Commits:
  - `fa36dad contract: track the Node kernel history control`
  - `fa2f773 tools: ignore literal navigation tag examples`
  - `f1b91c1 contract: refresh production navigation inventory`

### security-advisories

- Orphan branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/security-advisories`
- Head: `0d06b29d2af97699bc440d15d46c496e70ba3ef2`
- Commits:
  - `d0d8816 Establish the advisory analysis repository`
  - `cba1e7b Add the narrow vpsAdmin API client`
  - `d15cbe4 Create least-privilege vpsAdmin tokens`
  - `735941b Evaluate exact deployed Node evidence`
  - `a31b291 Reconcile reviewed advisory drafts safely`
  - `03a0ef1 Add the review-gated advisory CLI`
  - `fc2ec47 Analyze CVE-2026-23111 nf_tables UAF`
  - `8cafa4a Analyze CVE-2026-46242 epoll flaw`
  - `a9ceb98 Analyze CVE-2026-53362 IPv6 flaw`
  - `6a37977 Analyze CVE-2026-53359 KVM flaw`
  - `2ca9acc Analyze CVE-2026-43499 GhostLock`
  - `0280f15 Test the complete advisory workflow`
  - `719f683 Use Node-reported system closure identities`
  - `338628a Generalize CVE platform assessment guidance`
  - `890fd60 Evaluate complete generic Node evidence`
  - `9c20448 Add a read-only publication readiness preflight`
  - `0d06b29 Clarify user impact in initial advisory texts`
- `origin` is the required SSH URL
  `git@github.com:vpsfreecz/security-advisories.git`, but the GitHub repository
  does not exist yet, so this branch is not pushed.

### vpsfree-sms-gateway (development-cluster input only)

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsfree-sms-gateway`
- Head: `af7b3fafb780c849ae03e31712128ecb0749ec0b`, matching
  `origin/2026-06-15-vpsadmin-events`; no files or commits were changed.
- This worktree is a supported local override for the dev cluster's private
  flake input. An unauthenticated Nix GitHub fetch returned 404 even though the
  SSH remote and branch are available.

## Implemented behavior

### vpsAdmin API, evidence, and history

- Ordinary advisory, advisory-CVE, and advisory-Node-status actions now expose
  and require a continuous `content_revision` precondition for mutations. They
  mutate drafts only. No `submit_draft` action was added.
- The automation scope includes the existing
  `security_advisory.node_status#index/create/update/delete` actions in addition
  to advisory/CVE actions; it excludes publish, mail, retract, generic Node/VPS,
  and `all` scopes.
- `NodeSecurityEvent` stores append-only exact or reconstructed kernel history.
  `vpsadmin:node:reconstruct_kernel_history` derives bounded boot/release events
  from historical `node_statuses`, records a per-Node reconstruction checkpoint,
  stops before the first exact Node report, is restartable/idempotent, and never
  supersedes an exact current event with an inferred row.
- Authenticated `node.kernel_history#index` is a sanitized projection available
  to all logged-in users, including inactive Nodes. It exposes boot/release
  intervals and confidence, not boot UUIDs or internal evidence. The WebUI links
  current kernel values to a per-Node history page.
- Czech follows `doc/i18n-cs.md`: the infrastructure term remains `Node` in
  Czech text, with `Nody` for the plural; neither `nod` nor `uzel` is used.
- Admin-only `node.security_evidence#index` returns, per active Node/storage
  Node: ID/name/role, separate Node observation/server receipt times, freshness
  based on receipt, reconstruction completeness and evidence revision; current
  immutable and reported kernel identity; complete internal event history with
  per-event evidence and coverage gaps; livepatch/eBPF state; selected loaded
  modules/runtime settings; deployment identity; and explicit missing-evidence
  gaps. It returns no users, VPSes, addresses, utilization, `untrusted_vps`, or
  KVM-device counts.
- The schema-versioned nodectld payload contains immutable boot ID/time/release,
  reported release, vpsAdminOS/kernel/config identity, livepatch/eBPF metadata,
  loaded modules, runtime settings, and exact booted/current system closure
  identities resolved from `/run/booted-system` and `/run/current-system`.
  Unsupported/malformed evidence becomes a gap without rejecting ordinary Node
  status.

### vpsAdminOS and configuration

- The booted system closure carries exact vpsAdminOS revision, boot kernel
  identity/source revision, and kernel configuration identity. The probe reads
  the immutable `/run/booted-system` metadata rather than a newly evaluated
  system closure and uses `/proc/stat` boot time with explicit inferred
  confidence.
- Livepatch services persist a first-application timestamp marker. eBPF
  livepatch metadata includes the link fields needed to verify every pinned
  attachment.
- nodectld resolves the booted and currently activated Nix system closures
  itself. This single mechanism works on production Nodes, the dev cluster, and
  other installations without confctl or a generated evidence file.

### security-advisories

- The dependency-free Ruby CLI provides `validate`, `collect`, `evaluate`,
  `adopt`, `ready`, and `sync`. Sync is dry-run by default and requires
  `--apply`; `ready` is a fresh read-only publication preflight, and there is
  no publish command.
- Before any remote mutation, sync validates the committed dossier/evaluation,
  recollects and re-evaluates evidence, compares the complete canonical per-Node
  results, verifies active-Node-set digests/freshness, checks the exact remote
  snapshot, and then maintains one revision chain. It atomically records
  recovery checkpoints in tracked `submission.yml` after every successful
  mutation, so partial create/update runs can be safely resumed.
- `unknown` is an honest draft conclusion for missing or stale evidence and is
  synchronized with its reason. Existing vpsAdmin publication validation still
  blocks `unknown` or `vulnerable` active Nodes.
- The evidence digest covers the complete canonical evidence snapshot. Per-event
  kernel/build/config identity, a real baseline event at or before the required
  history start, reconstruction/exact-history gaps, exact accepted build rules,
  runtime mitigations, tristate configuration reachability, and role-specific
  reachability are evaluated. A pin, synthetic current row, or mutable reported
  release alone cannot establish safety.
- `bin/create-token` interactively obtains password/TOTP credentials and writes
  a mode-`0600` token outside git. It requests exactly these 12 scopes:
  `node.security_evidence#index`; advisory `index/show/create/update`; CVE
  `index/create/delete`; and advisory Node status `index/create/update/delete`.
- All five CVE dossiers contain detailed source/platform analysis and concise
  Czech/English user text. Each separately discusses root in the VPS user
  namespace, host-Node root/escape, cross-VPS access, and Node availability.
  UAF initialization hardening and monitored NULL/general-protection faults are
  described as exploitation friction/detection, never as prevention.
- Exact accepted deployed-build lists are deliberately empty until live
  deployment evidence is reviewed. The configured 6.12.95 source contains all
  five fixes, but a configuration pin is not proof of a Node's booted build.

### Documentation contract

- The contract pins vpsAdmin `70d4f4e5e...` and records the bilingual
  `node.kernel-history` WebUI control/fingerprint.
- The canonical full production inventory was fetched (116 Czech and 70 English
  pages), checked, and used to build durable candidates. There are zero changed
  pages and zero annotation changes because current KB content does not document
  this admin-controlled Node detail view.
- Empty Czech/English release manifests were generated. With no changed pages,
  staging and production writes were neither useful nor performed.
- The annotation checker now ignores literal example tags inside DokuWiki code,
  file, nowiki, and `%%...%%` constructs; regression tests cover literal and
  real tags.

## Review findings already resolved

An initial independent design/change review found seven issues, all addressed
before the final review:

1. split oversized histories into framework, per-CVE, API/evidence/WebUI, and
   vpsAdminOS evidence commits;
2. bind boot evidence to the immutable booted closure and make timestamp
   confidence explicit;
3. require exact deployed-build identity, per-event evidence, history coverage,
   and role-specific evaluation;
4. bind sync to dossier/evidence/Node-set/freshness digests and recollect before
   writing;
5. use a continuous revision chain plus snapshot checks and partial-run recovery
   checkpoints;
6. make sync dry-run by default with explicit `--apply`;
7. state VPS-user-namespace versus host-Node impact in every public text.

Follow-up hardening also isolates malformed evidence, keeps TLS verification on
by default, hashes all evidence rather than selected labels, and allows
reviewable `unknown` draft rows while preserving the publication gate.

The mandatory final fresh-context reviewer then reported nine findings. All
were resolved before handoff:

1. apply now recollects and freshly evaluates evidence, then compares complete
   canonical node results instead of trusting editable cached rows;
2. reconstruction has a persisted completeness checkpoint, stops before exact
   reports, never promotes synthetic current evidence over exact current data,
   and the evaluator requires a real retained baseline event;
3. kernel configuration predicates use explicit enabled/disabled semantics, so
   both `y` and `m` satisfy enabled while only `n` proves disabled;
4. histories were rewritten into focused evaluator/API/token/reconciler/CLI,
   public-history/private-evidence/reporter, boot/livepatch/eBPF, and combined
   configuration-evidence commits;
5. submission checkpoint writes use fsync plus atomic rename and have an
   interruption regression test;
6. guest cluster status renders a plain kernel value, while only logged-in
   users receive the Node history link;
7. vpsAdmin stores server receipt time separately and uses it for freshness;
8. all five dossiers now link to and record the exact Linux 6.12 stable fix
   commit; and
9. mandatory publish revision preconditions remain intentional security
   hardening. The coordinated client/API deployment and rollback caveat are
   recorded below and in `plan.md`.

The review's final integration audit was also resolved: repeated repin/fixup
history was collapsed; every intermediate security-advisories commit now tests
without depending on later dossiers or classes; eBPF evidence is bound to a
revision/digest and attachment time; every draft mutation requires the expected
content revision; operator historical attestations are exact and digest-bound;
and an admin-only `external_id` plus atomic initial CVE creation recovers a
lost create response without duplicating drafts. The reporter does not depend
on confctl or any other deployment tool.

The mandatory direct-system-identity follow-up review confirmed that nodectld
is the sole source of booted/current closure identity and that missing links
fail explicitly. Its remaining findings were resolved before handoff:

1. repeated staging/services and KB pins were rewritten into one final commit
   per input stream;
2. a same-boot activation now has model/API regression coverage proving that a
   private `deployment_change` is recorded and exposed;
3. evaluator regressions prove that either changed closure, an old
   `deployment.inputs` payload, or a missing closure all invalidate the
   reviewed build and return `unknown`; and
4. these records now distinguish a prepared production services-channel pin
   from an actual deployment and from the unchanged production Node input.

At the user's request, the vpsAdmin history was then rewritten on current
`origin/master` so the direct closure mechanism is part of the original
libnodectld evidence commit. No commit in the final feature range adds or
removes `/etc/confctl/inputs-info.json` or `inputs_info`; the corrective commit
no longer exists. The exact vpsAdminOS feature revision is pinned separately by
the repository-prescribed flake update commit. Configuration and KB histories
were regenerated once more so they retain only the final vpsAdmin head.

## Verification

- vpsAdmin public history/reconstruction: 9 examples, no failures; private
  evidence/receiver/recording: 16 examples, no failures; split migration
  specs: 4 examples, no failures; libnodectld: 4 examples, no failures; WebUI
  visibility regression: 1 test/6 assertions, no failures.
- vpsAdmin RuboCop covered 20 changed non-generated Ruby files with no offenses.
  Every rewritten commit passed repository hooks: MigrationSpecs, WebUI/API
  i18n, Nixfmt, PhpCsFixer, and RuboCop.
- vpsAdminOS final-tree
  `nix eval .#packages.x86_64-linux.toplevel.drvPath --raw` passed; all three
  commits passed Nixfmt hooks.
- vpsfree-cz-configuration hooks passed. The staging Node build evaluated its
  configuration/modules/pinned vpsAdminOS and then stopped while forcing the
  closure because the local system lacks the external
  `/secrets/nodes/initrd/ssh_host_ed25519_key`. See
  `notes/vpsfree-cz-configuration/2026-07-13-confctl-node-build-initrd-secret.md`.
- A push attempted outside `nix develop` could not load the repository's removed
  local `.bundle`; retrying inside the declared Nix development shell ran the
  mandatory pre-push checks and pushed successfully.
- security-advisories: 50 tests, 286 assertions, no failures; all five dossiers
  validate; all Ruby files pass syntax checking; `git diff --check` passes.
- vpsadmin-kb-captures `nix develop -c bin/check` passes: 34 controls, 29 paths,
  32 concepts, 3 selectors; 65 bindings and 9 exceptions; 118 valid PNGs; test
  groups at 8/50 and 7/17 runs/assertions.
- The deployment-tool-independent follow-up passes its focused libnodectld spec
  (1 example), the focused evidence recording/API/receiver specs (19 examples),
  all vpsAdmin pre-commit hooks, 41
  security-advisories tests/143 assertions, and validation of all five
  dossiers.
- After the history rewrite and separate vpsAdminOS flake update, the same
  focused suites remained green and a complete `overcommit --run` passed
  MigrationSpecs, WebUI/API i18n, Nixfmt, RuboCop, and PhpCsFixer.
- The dev cluster was refreshed and all machines were updated from the final
  worktrees. Services and Node closures built and activated successfully; the
  WebUI/API both return HTTP 200 with the dev CA. Before reboot, Node1 had
  activated closure `gq2wq91k...` while retaining legacy booted closure
  `z2d206nn...`; nodectld reported the explicit booted-metadata gap described
  above.
- After a state-preserving cluster stop/start, the dev Node booted directly
  into `gq2wq91kc0h2d25m56gflrfnv6xy4yb2`, which is also its current closure.
  Its stored report has schema 2, an empty error list, booted/reported kernel
  6.12.95, source revision `a2384967...`, a catalogued config digest, complete
  configured and effective state, 341 loaded modules, 37 security settings,
  and a current exact boot report. The WebUI and API return HTTP 200.
- The mailer and both DNS service Nodes have null kernel and security-evidence
  fields after the fresh boot. The evidence collection and public kernel
  history resources filter them by role, so service-container host kernels are
  not exposed as managed Node kernels.
- Dev cluster `2026-07-13-security-advisory-automation` is `running`, `ready`,
  topology `single`, network `bridge`. WebUI and API are reachable at
  `https://webui.aitherdev.int.vpsfree.cz/` and
  `https://api.aitherdev.int.vpsfree.cz/`.
- The cluster was rebuilt after the final history rewrite. Both endpoints
  return HTTP 200, and the live API description exposes
  `node.kernel_history#index`, `node.security_evidence#index`, advisory
  `external_id`/`content_revision`, and expected-revision parameters on the
  advisory and nested Node-status mutation actions.
- Final vpsAdmin head `70d4f4e5e...` is green for API migrations, RuboCop,
  client specs, WebUI PHPUnit, i18n health, libnodectld specs, and the
  topic-parallel API suite. Selected integration run `29331995182` remains in
  progress. Its current reporter delta intentionally selects the broad
  `dns/network/node/storage/supervisor/vps` integration set; the run has no
  failure annotation or downloadable completed log yet.
- Final-head vpsAdminOS GitHub CI completed successfully, including the OS
  closure build and VM test suite.
- A superseded API-specs run failed because the two new endpoints were missing
  from the endpoint-coverage manifest. Logs were inspected, the manifest was
  fixed in the final evidence commit, and superseded runs were cancelled after
  the updated branch was pushed.
- After the history rewrite, the remaining superseded vpsAdmin CI run for old
  head `2cf07d4d...` was explicitly cancelled; new-head runs were left intact.
- After folding the direct-system-identity regressions into the implementation
  commit, the superseded selected integration run for `611d8a351...` was
  cancelled. Its completed API/libnodectld/RuboCop/i18n jobs were green; only
  runs for the then-current head were left active.
- After the final history rewrite, superseded selected-integration work for
  `039a6ecc0...` was cancelled; its API run had already completed before the
  cancellation request. Only current-head `a7781afee...` runs remain active.
- Final-head migration CI initially found that the new spec called the local
  two-argument `index_exists?` helper with an Active Record keyword. The logs
  were inspected, the spec was changed to inspect the exact index and unique
  flag, the focused suite passed locally, and final-head migration CI is green.
  Superseded long/API jobs for `67281212...` were cancelled.

### Typed evidence redesign (2026-07-14)

- Removed the unmerged nested `node.security_evidence#index` implementation
  and its `all/security_evidence` route. The replacement is twelve top-level
  HaveAPI object-list resources with concrete scalar fields; current Nodes,
  exact events, kernel options, parameters, modules, sysctls, livepatches,
  eBPF program details, and evidence gaps are independently filterable.
- Extended the original unmerged kernel-configuration migration with a
  relational `node_kernel_configuration_options` table. The canonical raw
  config remains private and digest-addressed; all `CONFIG_*` assignments are
  parsed atomically on first save, including `# CONFIG_* is not set` as `n`.
- Component resources use `node_active` for Node-state filtering so an eBPF
  program's own typed `active` field remains independently filterable. Service
  roles are excluded centrally; current evidence still uses its row-level
  `active` filter.
- security-advisories now reads and paginates the typed resources, requests
  only the union of exact kernel option names used by committed dossiers,
  reconstructs the evaluator's local snapshot, and re-reads revisioned current
  rows. It retries instead of combining data if evidence changes concurrently.
- Local advisory evidence is schema 4. The least-privilege scope list now names
  only the twelve evidence indexes and the existing advisory/CVE/nested
  Node-status actions; no generic Node inventory scope is required.
- Final quick checks: the normalized API/resource, model, supervisor, and
  migration specs pass; the full security-advisories suite passes 52 tests and
  300 assertions; all five dossiers validate; API catalog health, syntax,
  `git diff --check`, and RuboCop pass. vpsAdmin's complete Overcommit gate
  passed MigrationSpecs, Nixfmt, WebUI/API i18n, and repository-wide RuboCop.
  The KB contract passes its complete check with 118 valid PNGs and the WebUI
  tree is unchanged from the prior feature head.

### Final normalized-resource heads (2026-07-14)

- vpsadmin `0d07921edb969ee079e70b5430540de7d4cb7585`; pushed with rewritten
  history. The normalized implementation is folded into
  `0d04a9486 api: store Node security evidence`, while the vpsAdminOS flake
  input remains a separate final commit.
- security-advisories `6718325ff5e1dc00ea7a205330309edc6b5cc146`;
  local-only because the requested GitHub repository does not yet exist. The
  collector redesign is folded into `9ddbde0 Evaluate complete generic Node
  evidence`.
- vpsfree-cz-configuration `c1c17f27a073787dea2234ee6f8cc25d08b81e1c`;
  the clean feature range contains one generated staging pin and one generated
  services pin directly to vpsAdmin `0d07921e`, plus the independent
  vpsAdminOS staging pin.
- vpsadmin-kb-captures `27383188e6ee8cd896a69616688145ea09abd10a`;
  contract commit `06bb2f6` pins vpsAdmin `0d07921e`. No capture or annotation
  content changed because the normalized API rewrite does not change WebUI
  source.
- vpsadminOS remains `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`.

The configuration and KB branches are committed locally but not yet pushed.
The mandatory fresh-context change review is next, before rebuilding and
testing the dev cluster from the rewritten final inputs.

## Compatibility and deployment

- Database, evidence/history API, status-payload, metadata, and WebUI fields are
  additive. One deliberate contract change requires
  `expected_content_revision` for publication so a stale publisher cannot
  bypass the reviewed revision. Deploy the vpsAdmin API and WebUI together and
  update external administrative publishing clients before their next use; an
  old client then fails safely instead of publishing. Evidence readers ignore
  new response fields, and old nodectld payloads continue updating ordinary
  status while showing an evidence gap.
- Exact event storage and current evidence update atomically. History remains
  append-only; reconstructed events retain uncertainty rather than rewriting
  `node_statuses`.
- Deployment order: migrate and deploy the vpsAdmin receiver/API with its WebUI
  publication caller; update other administrative publishers; deploy node-side
  vpsAdmin; deploy vpsAdminOS/configuration evidence; run reconstruction; then
  collect/review evidence and draft results. Rolling Node upgrades work and no
  coordinated all-Node reboot is required.
- Rollback leaves additive tables/columns and metadata files that older versions
  ignore. An older API can read the revision column but loses publication
  enforcement, so operators must not use stale publishing clients during that
  rollback window. Unsupported evidence schemas do not prevent legacy status
  ingestion.
- The automation never needs root/SSH/log-host access. The unpublished central
  log work is useful only for an operator-controlled historical cross-check.

## Remaining handoff actions

1. Confirm final-head vpsAdmin selected integration run `29331995182`
   completes successfully and inspect its logs if it does not.
2. User creates the private `vpsfreecz/security-advisories` GitHub repository;
   then push `0d06b29d2af97699bc440d15d46c496e70ba3ef2` over its already
   configured SSH remote.
3. Deploy the feature in the recorded coordinated order and allow exact
   evidence to accumulate.
4. Create the scoped token, collect live evidence, populate each dossier's exact
   accepted build identities, evaluate, review the dry-run, and use `--apply`
   to prepare drafts. Resolve all `unknown` rows before human publication.

## Cleanup

- Worktrees remain active for review and deployment preparation.
- Dev cluster `2026-07-13-security-advisory-automation` remains running and
  ready on the bridge network. The previously running
  `2026-07-02-haveapi-i18n` cluster was stopped with the user's explicit
  authorization; graceful stop timed out and the devcluster tool terminated
  its runner and removed its GC root.
- No feature branch is merged or deployed.
- The vpsAdminOS, vpsAdmin, configuration, and KB contract branches are pushed.
  The security-advisories branch remains local only because its GitHub
  repository does not yet exist.
- No production vpsAdmin or KB write was made.

## Final review resolution and live smoke test (2026-07-14)

This section supersedes the older normalized-head and remaining-action
snapshots above.

The mandatory standalone change review completed and its significant findings
were addressed:

- the token generator verifies and grants the exact twelve typed evidence
  index actions plus existing advisory/CVE/nested Node-status draft actions;
- missing kernel configuration is represented by an explicit evidence gap and
  an `unknown` assessment, never a repository-derived assumption;
- eBPF mitigation evidence requires exact attached-link state;
- typed-resource collection is paginated, revision-checked, bounded, and
  retried instead of combining concurrent reports;
- vpsAdmin and security-advisories histories were rewritten so the superseded
  `all/security_evidence`/`node.security_evidence#index` implementation was
  never introduced; remaining string matches are negative regression tests;
- functional work, generated pins, and the vpsAdminOS flake input are split
  into reviewable commits.

Final heads:

- vpsadmin `1fa16a3cd0cb9c5c42904545f80aea210ccaeccf`, pushed;
- vpsadminOS `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, pushed;
- vpsfree-cz-configuration
  `795f459fa07bab1fe9cdf7f663b250b5723622aa`, pushed, with exact vpsadmin
  staging/services and vpsadminOS staging pins;
- vpsadmin-kb-captures
  `06c0f6cc488a07b83d1c56091848990edcf66639`, pushed;
- security-advisories
  `2737812d139facedd1250ccbefb9f5cd87889388`, local-only because the requested
  GitHub repository does not exist yet.

Final verification:

- security-advisories: 57 tests, 318 assertions, zero failures/errors; all five
  committed CVE dossiers validate;
- vpsAdmin ordinary focused suite: 102 examples, zero failures; libnodectld:
  five examples, zero failures;
- vpsAdmin complete Overcommit run: MigrationSpecs, WebUI/API i18n, Nixfmt,
  RuboCop, and PhpCsFixer pass;
- vpsadmin-kb-captures complete check: 34 controls, 29 paths, 32 concepts,
  65 bindings, nine exceptions, and 118 valid PNGs;
- vpsadminOS final-head CI and RSpec workflows pass;
- vpsAdmin final-head migration, API, client, libnodectld, RuboCop, WebUI, and
  i18n workflows pass. Long selected integration run `29355435328` remains in
  progress with its test step running; superseded run `29348186505` was
  cancelled after confirming its head is obsolete.

The dedicated dev cluster was reset after the history rewrite because its old
database had already recorded the same unmerged migration timestamp from the
discarded schema. A clean bridge/single initialization then applied the final
migration and demonstrated that relational kernel-option rows are created.
The cluster remains `running` and `ready`; WebUI and API both return HTTP 200.
The live API exposes all twelve typed evidence resources plus the public
newest-first `node.kernel_history#index`. Current evidence contains only
hosting Node 101; DNS and mailer service containers are excluded. Filtering
`node_kernel_configuration_option#index` by Node 101 and `CONFIG_IPV6` returns
the expected typed option row.

The real token smoke test initially exposed that vpsAdmin's token-management
endpoint is unversioned: authentication was incorrectly attempted below the
configured `/v7.0` resource URL. `TokenIssuer` now derives the API origin for
`/_auth/token/tokens` while retaining the versioned resource URL in the saved
configuration, with an exact-URI regression test. A newly generated token with
23 exact actions then ran `collect` end to end and produced schema-4 evidence
with the Node's booted/current closures, required kernel options, modules,
security settings, and no gaps. The temporary token file and ignored evidence
snapshot were removed; no credential was retained in the repository or notes.

Remaining handoff:

1. Monitor current-head selected integration run `29355435328`; inspect its
   logs if it fails.
2. Create the private `vpsfreecz/security-advisories` repository and push the
   existing SSH-configured local branch.
3. Deploy in the recorded coordinated order, collect production evidence, and
   resolve every per-Node `unknown` before preparing drafts for human review.

No production vpsAdmin, deployment, advisory, publication, notification, or KB
write was made.

## Relational evidence normalization (started 2026-07-14)

The user approved replacing the remaining current/event evidence JSON blobs
with relational storage. The implementation will retain only a canonical
SHA-256 snapshot revision, use a mutable current evidence row per reporting
Node, and create one immutable normalized snapshot shared by all events
detected from the same report. Typed component APIs will expose real evidence
foreign keys and database-backed ID pagination. vpsAdminOS schema 2 and the
existing action scopes remain unchanged.

Because all evidence migrations are unmerged, vpsAdmin and
security-advisories history will be rewritten so the blob-backed schema is
never introduced. Configuration and KB pins will then be refreshed to the new
vpsAdmin head. The dedicated dev cluster must be reset again after that rewrite
because its database has already applied the discarded migration timestamps.

## Relational evidence normalization (implemented 2026-07-14)

The approved normalization is implemented and committed.

- vpsAdmin base/head: `1a4fa3031` / `100e54ec20e3a185f357486d44ab7044c2cf1055`
  in `worktrees/2026-07-13-security-advisory-automation/vpsadmin`.
  The branch was autosquashed and force-pushed. Its history now introduces
  relational history gaps in `e511fd254`, normalized snapshots/components in
  `1f213c7fd`, and their typed top-level resources in `04dfaf658`; the discarded
  blob columns never appear in the rewritten series. The separate vpsAdminOS
  input commit remains the final commit `100e54ec2`.
- security-advisories head:
  `f98b88cf4e91b9108343c2b92c38c5b806973c5a` in
  `worktrees/2026-07-13-security-advisory-automation/security-advisories`.
  `46a93c6` collects stable component/evidence IDs, validates snapshot
  revisions, and uses ID pagination for stored rows. Its SSH remote still does
  not exist, so it is not pushed.
- vpsfree-cz-configuration base/head: `e1cc165c` /
  `6ef742eb333c727849f1521366f812481f9eefce`. Obsolete vpsAdmin pins were
  removed before `confctl inputs channel set --commit` generated the final
  staging and services pins to `100e54ec`; the vpsAdminOS staging pin remains
  `d47ba226`.
- vpsadmin-kb-captures base/head: `470b759` /
  `1e233c7daba10733d0e1a24c66fc2e1e79a3caa2`. The vpsAdmin flake,
  capture-manifest, and navigation-contract pins all select `100e54ec` and are
  squashed into the original Node history contract commit.
- vpsAdminOS remains `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`
  on base `ff9e49b20`; its report schema and deployed evidence mechanism did not
  change in this follow-up.

Storage now uses one mutable current snapshot per kernel-hosting Node and one
immutable snapshot shared by all events created from a single report. Scalar
versions/sysctl values are canonicalized before change comparison and digesting
so relational string columns cannot create false history events. Service-only
Node roles still neither retain nor expose kernel evidence.

Quick verification after the rewrite:

- vpsAdmin pre-commit hooks passed for every staged fixup in
  `nix develop .#vpsadmin` (Nixfmt, migration specs, WebUI/API i18n, RuboCop,
  and commit-message hooks). An ambient-shell attempt correctly failed because
  RuboCop/gettext/MariaDB were absent; commits were made only after rerunning in
  the declared shell.
- vpsAdmin migration specs: 4 examples, 0 failures.
- vpsAdmin normalized model/operation/supervisor specs after the final fixture
  correction: 30 examples, 0 failures.
- vpsAdmin combined API/supervisor/resource run before the final fixture-only
  correction: 29 examples, 0 failures. The larger rewritten run exposed only
  a direct test fixture missing mandatory `schema_version`; production reports
  were unaffected and the corrected affected suite is green.
- security-advisories: 57 runs, 319 assertions, 0 failures/errors.
- vpsadmin-kb-captures `bin/validate`: 59 concepts, 118 variants, 118 PNGs.
- `git diff --check` is clean in all changed feature worktrees.

Compatibility/deployment: all rewritten migrations are unmerged and absent
from production, so no blob data migration is needed. nodectld schema 2 and the
old/new reporter compatibility contract are unchanged. The dedicated dev
cluster must be reset before deployment because it used the discarded
migrations with identical timestamps. Long cluster integration is intentionally
deferred until the mandatory fresh-context change review.

## Mandatory normalization review resolution (2026-07-14)

The required standalone fresh-context review completed after the normalized
implementation and quick verification. It found six correctness issues; the
review was intentionally not repeated because the workspace review skill calls
for exactly one standalone reviewer. All blocking and important findings were
fixed and covered by focused tests before integration:

- status ingestion now reloads and updates evidence under the Node lock, uses
  the Node observation time as an ordering watermark, and ignores delayed
  reports; events and current evidence remain one transaction;
- event history selects one matching baseline per Node after applying all event
  filters, with cursor and limit handled by SQL rather than loading the fleet's
  history into Ruby;
- component collection expands back to the oldest exact baseline returned by
  the event API, and the collector recomputes every assembled snapshot digest,
  failing closed when a child row is absent;
- host-role filtering is applied to every component, nested component, kernel
  option, event, current, and gap path, including retained evidence after a Node
  changes to a service-only role;
- duplicate relational keys are rejected by the supervisor and normalized
  before direct model digesting, preventing the stored rows from disagreeing
  with the snapshot revision;
- collector convergence compares per-Node semantic evidence revisions, so a
  harmless observation/receipt timestamp refresh does not force repeated
  retries.

The review found no tenant authorization bypass and confirmed that the typed
resources remain admin-only, the token scopes are exact, the schema-2 Node
report is unchanged, and the flake input remains a separate commit.

Rewritten and refreshed heads:

- vpsAdmin `c83f8db49c5a905322615ba0bf6b55cdb2fab808`, force-pushed;
  normalized ingestion is `98af2959c`, typed resources are `e38063fad`, and the
  separate vpsAdminOS input is the final commit;
- security-advisories `f849a08`, local-only because the requested remote still
  does not exist; the review fixes are folded into `d98f46f`;
- vpsfree-cz-configuration `301ac693`, force-pushed, with generated staging and
  services pins to `c83f8db4` and the existing vpsAdminOS staging pin;
- vpsadmin-kb-captures `c8c592f`, force-pushed, with flake, capture inventory,
  and navigation contract pinned to `c83f8db4`;
- vpsAdminOS remains `d47ba226`.

Verification after the review fixes:

- vpsAdmin supervisor: 17 examples, zero failures, including stale worker,
  out-of-order report, and duplicate-key cases;
- vpsAdmin real MariaDB event checks: per-Node filtered baselines and 1,002-row
  two-page cursor traversal pass without omissions;
- both vpsAdmin fixup commits passed Nixfmt, migration specs, WebUI/API i18n,
  RuboCop, and commit-message hooks from `nix develop .#vpsadmin`;
- security-advisories: 60 runs, 326 assertions, zero failures/errors, including
  incomplete-baseline rejection and stable-revision timestamp convergence;
- vpsadmin-kb-captures validation: 59 concepts, 118 variants, 118 PNGs.

The current vpsAdmin GitHub Actions runs are on `c83f8db4`. Superseded
in-progress CI run `29363677398` for `100e54ec` was cancelled. The dedicated
dev cluster still requires a clean reset and redeployment because the migration
history was rewritten again.

## Final normalized integration checkpoint (2026-07-14)

This section supersedes older head, cluster, and remaining-action snapshots in
this file.

Final heads and pins:

- vpsAdmin `b7ec792464fb095961d9e84f49b4b86502ede694`, pushed. The
  normalized migrations are in `e4ddad399`, typed resources in `a5028934c`,
  generic reporting in `59c1100c7`, and the separate vpsAdminOS flake pin in
  `b7ec79246`.
- vpsAdminOS `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, pushed.
- vpsfree-cz-configuration
  `dda588941e901d49dfe5ae0de89ded0ba190e7ea`, pushed. Generated staging and
  services inputs select vpsAdmin `b7ec79246`; staging vpsAdminOS selects
  `d47ba226`.
- vpsadmin-kb-captures
  `64a1e37e925eed9bfc4b0ee79bb628cf160d9b89`, pushed. Its contract selects
  vpsAdmin `b7ec79246`.
- security-advisories
  `0f67a6047dac9dfc5b092edd3132ef2a7aa9e864`, local-only because the requested
  GitHub repository does not exist. The last commit corrects the documented
  current vpsAdmin resource URL from `/v2` to `/v7.0` after the live smoke test
  exposed the stale example.

The first clean-cluster ingestion exposed a real relational-schema issue. Linux
can simultaneously load case-distinct modules such as `xt_DSCP`/`xt_dscp` and
`xt_TCPMSS`/`xt_tcpmss`, but MariaDB's default Czech case-insensitive collation
treated each pair as a duplicate and rolled back the report transaction. All
machine-identity evidence tables and the kernel configuration catalog/options
now use `utf8mb3_bin`. Migration specs assert the collation and a model
regression preserves both pairs. This fix is folded into the original
normalized-ingestion commit, so the broken schema is absent from branch
history.

Final verification after that fix:

- normalized model and supervisor specs: 21 examples, zero failures;
- migration specs in their supported separate process: four examples, zero
  failures;
- focused RuboCop and the complete vpsAdmin pre-commit gate pass (Nixfmt,
  migration specs, WebUI/API i18n, RuboCop, and commit-message checks);
- security-advisories: 60 runs, 326 assertions, zero failures/errors; all five
  dossiers validate;
- vpsadmin-kb-captures complete validation/check passes with 59 concepts, 118
  variants/PNGs, and both test groups green;
- an attempted combined migration/model RSpec process produced false model
  failures after the migration harness intentionally switched to its stripped
  `vpsadmin_test_migration` database. The supported separate-process runs above
  are green; this was not an application failure.

The clean bridge/single cluster applied the rewritten migrations and is
`running`, `ready`, and serving the final worktrees. The live database contains
one current and one immutable event evidence snapshot, both for hosting Node
101. Service Nodes 100, 301, and 302 have null evidence references. The tested
normalized tables report `utf8mb3_bin`, and both snapshots contain all four
case-distinct `xt_*` module names. The supervisor journal has no ingestion
error. The WebUI returns HTTP 200 after final activation; authenticated typed
API collection succeeds.

The exact documented token workflow was tested with a fixed five-minute token.
It requested 23 actions (the twelve read-only evidence indexes and eleven
existing advisory/CVE/nested Node-status draft actions), saved the versioned
`/v7.0` API URL, and collected schema-4 evidence without overrides. The result
contains only `101:node`, one filtered kernel configuration, 341 loaded modules,
current and historical normalized snapshots, and a canonical evidence digest.
All five dossier evaluations completed and correctly returned `unknown` for the
dev Node because their accepted production build identities are deliberately
empty. The temporary token and command output were removed; no credential was
retained.

At this checkpoint, current-head vpsAdmin GitHub Actions are green for migration
specs, RuboCop, client specs, WebUI PHPUnit, i18n, and libnodectld. The long CI
run `29368532294` and topic-parallel API run `29368532293` are still in
progress. Superseded old-head runs were cancelled after the history rewrite.

Remaining handoff:

1. Monitor the two current-head vpsAdmin runs and inspect logs if either fails.
2. Create the private `vpsfreecz/security-advisories` repository, then push the
   already configured SSH branch.
3. Deploy in the recorded order, collect exact production evidence, and review
   per-Node conclusions. Do not publish until every active hosting Node is
   resolved and a human has reviewed the draft.

No production deployment, advisory mutation/publication, notification, KB
write, or root/log-host access occurred.

## Follow-up implementation started (2026-07-15)

The user approved a history rewrite that replaces the normalized
`node_security_*` family with `node_kernel_*` names and the clearer
`node_sysctl` resource/table. Kernel parameters will gain an explicit
zero-based position and separately stored name/value, preserving duplicates and
the distinctions between a flag, an empty value, and a value containing equals
signs. The observation-bound column names remain and will be documented as the
interval `(observed_after, observed_before]`.

The `security-advisories` repository will be converted from Minitest to RSpec
and receive the repository-standard RuboCop, Overcommit, locked bundle, and CI
setup. No source changes have been made for this follow-up yet. The existing
heads listed in the final normalized integration checkpoint are the rewrite
inputs. The dedicated dev cluster must be reset after rewritten migrations and
downstream pins are ready; no attempt will be made to migrate its old unmerged
schema in place.

## Kernel naming and ordered parameters implemented (2026-07-15)

This section supersedes the preceding follow-up-start snapshot.

Current heads and pins:

- vpsAdmin `dd07e0d26183db7462a92fc43f82443846a551f0`, force-pushed on
  `2026-07-13-security-advisory-automation`. Its rewritten history is four
  commits on `1a4fa3031`: the complete API/storage feature, generic
  libnodectld reporting, the WebUI, and the separately generated vpsAdminOS
  flake pin. The tree is identical to the pre-rewrite feature tree except for
  the approved kernel/sysctl names and ordered parameter representation.
- vpsAdminOS remains
  `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`; no report schema or source change
  was required.
- security-advisories
  `3486db8ebd9e1e898968220e8f3f03cc5ed67da5`, local-only. Its unpublished
  history is now one initial repository commit, so RSpec, RuboCop, Overcommit,
  and the kernel-focused API names exist from the first commit. The configured
  SSH remote still has no repository to accept a push.
- vpsfree-cz-configuration
  `4e827fbe4b6e7d8ee24b2ce207b9e732b1fe43c9`, local pending review. The three
  `confctl inputs channel set --commit` commits select vpsAdminOS `d47ba226`
  for staging and vpsAdmin `dd07e0d2` for both staging and vpsAdmin services.
- vpsadmin-kb-captures
  `b2e54855cdf4fe3e8925f566ac5863cb846434ec`, local pending review. Its rewritten
  single feature commit pins vpsAdmin `dd07e0d2` in the flake, capture
  inventory, and navigation contract.

Implementation details:

- normalized history/snapshot/error tables and resources use
  `node_kernel_*`; sysctls use `node_sysctls`/`NodeSysctl` and
  `node_sysctl#index`;
- kernel parameter rows store zero-based `position`, `name`, and nullable
  `value`; reconstruction preserves order, duplicate names, flags, empty
  values, and values containing additional equals signs;
- set-like evidence remains canonicalized independently of report ordering;
- `observed_after`/`observed_before` are documented as the interval
  `(observed_after, observed_before]`, with a null lower bound for the first
  known state and `effective_at` reserved for exact times;
- public `node.kernel_history#index`, the nodectld `security_evidence` wire
  key, and vpsAdminOS schema 2 remain unchanged.

Quick verification:

- every rewritten vpsAdmin commit passed the declared Overcommit gate from
  `nix develop .#vpsadmin` (Nixfmt, migration mapping, WebUI/API i18n,
  RuboCop, PHP formatting where applicable, and commit-message checks);
- vpsAdmin application/API/model/supervisor specs: 89 examples, 0 failures;
- vpsAdmin migration specs in their separate process: 10 examples,
  0 failures;
- libnodectld component-shell specs: 5 examples, 0 failures;
- security-advisories: RuboCop inspected 18 files with no offenses; RSpec ran
  61 examples with 0 failures; its real staged pre-commit RuboCop hook passed;
- vpsadmin-kb-captures `bin/validate && bin/check`: 59 concepts,
  118 variants/PNGs, both test groups green, documentation contract and KB
  annotation inventory valid;
- rewritten worktrees are clean and downstream lock metadata resolves the
  exact revisions above.

Two invalid combined test attempts did not change source. Parallel vpsAdmin
development shells raced over the shared `.gems` cache, and mixing migration
and ordinary specs in one randomized RSpec process sent application examples
to the deliberately partial migration database. The successful sequential,
separate runs above supersede those results. The reusable migration-isolation
lesson is in `notes/vpsadmin/2026-07-15-migration-rspec-db-isolation.md`.
One `confctl` attempt used a mistyped nonexistent full revision and failed with
HTTP 404 before changing the lock; the exact pushed revision then succeeded.

Compatibility remains additive because none of these migrations or API names
has merged or reached production. A mixed deployment still accepts the
unchanged schema-2 Node report, while old vpsAdmin simply ignores its existing
extra report key. The dev database cannot be upgraded in place because the
unmerged migration timestamps were rewritten; the next integration step is a
clean bridge-network cluster reset after the mandatory fresh-context review.

## Focused review history and refreshed pins (2026-07-15)

The mandatory review preparation found that the first follow-up rewrite had
collapsed independent changes too aggressively. Before launching the reviewer,
the histories were made reviewable without changing the validated trees.

- vpsAdmin is now `bd6614122a03c1a2874c898b4872687dc318a506` on the current
  upstream base `8028e5032dcc2b778ae0e6d9cf21944b1c9fe6cf`. The branch was
  force-pushed. It restores the original focused advisory, history,
  normalization, typed-API, reporter, and WebUI commits; the kernel-specific
  naming/ordered-parameter change is `6343bdfdc`; the independent vpsAdminOS
  input update is the final commit. Upstream advanced only through generated
  Ruby and WebUI dependency locks, and the feature rebased without conflict.
- security-advisories is
  `2636f3ba5c0de895939c9c1c836ddb78bdd79091`, still local-only because its
  remote repository does not exist. Its unpublished history now has focused
  project/tooling, token client, collector, evaluator, reconciler, and one
  commit for each of the five CVE dossiers. Its tree is byte-for-byte equal to
  the previously validated single-root history.
- vpsfree-cz-configuration is
  `6e763101859448d9dcedbf470e59cc287f0d452f`, local pending review. Generated
  confctl commits pin staging vpsAdminOS to `d47ba226` and both staging and
  services vpsAdmin to `bd661412`. Lock metadata resolves those exact full
  revisions.
- vpsadmin-kb-captures is
  `2630ac8db3778c9734fad35581219c1c5b01186a`, local pending review. Its single
  contract commit pins `bd661412` in the flake, capture inventory, and
  navigation contract.
- vpsAdminOS remains
  `d47ba226ab759f6d71f0f8dbae5152dd1826e86c` on its staging-line base
  `ff9e49b20`; its evidence contract did not change in this follow-up.

Final quick verification on the review heads:

- vpsAdmin affected application/API/model/supervisor suite: 114 examples,
  0 failures, against a fresh MariaDB schema;
- vpsAdmin migration suite in its isolated process: 10 examples, 0 failures;
- libnodectld component-shell suite: 5 examples, 0 failures;
- security-advisories: RuboCop inspected 18 files without offenses and RSpec
  ran 61 examples with 0 failures;
- vpsadmin-kb-captures complete `bin/validate && bin/check`: 59 concepts,
  118 variants/PNGs, 34 controls, 29 paths, 32 capture concepts, 3 semantic
  selectors, and both test groups green;
- all five affected worktrees are clean.

Two confctl invocations failed without changing the lock: one used a guessed
nonexistent full vpsAdmin revision and GitHub returned 404; another used
`services` as a channel name, while the declared channel is `vpsadmin`. The
successful commands used the exact revision read from Git and the repository's
declared `staging` and `vpsadmin` channels.

The required standalone mandatory change review is the next step. The dev
cluster remains intentionally untouched until that review is resolved; it must
then be reset rather than upgraded in place.

Review-gate operations after freezing the packet:

- the superseded bridge/single dev cluster for this verified session was found
  running and was stopped successfully; its status is now `stopped` and its GC
  root was removed;
- superseded in-progress vpsAdmin CI runs `29403821237` (`dd9801251`) and
  `29402627560` (`dd07e0d26`) were cancelled after the final branch push;
- on final head `bd661412`, RuboCop, API migration specs, WebUI PHPUnit,
  client specs, i18n health, and libnodectld specs are green; the aggregate CI
  and topic-parallel API run were still in progress when recorded.

## Mandatory kernel naming review (2026-07-15)

The one required standalone fresh-context review completed. Long integration
remains paused while four Blocking findings are resolved; the review will not
be repeated because the mandatory review workflow calls for exactly one fresh
reviewer.

1. Collector-shaped reconstructed events always contain a partial
   `security_evidence.kernel` hash, so the evaluator returns that incomplete
   evidence before consulting a historical operator attestation. Advisory
   validation also accepts fewer attestation fields than evaluation needs.
   Fix the exact/reconstructed distinction, align validation, and cover the
   collector-to-evaluator path.
2. vpsAdmin normalization commit `6343bdfdc` combines the mechanical
   `node_security_*` rename with independently reviewable ordered-parameter
   semantics. Fold final names into their introductory commits and retain the
   parameter change as a focused commit.
3. security-advisories still combines tooling/CI with its domain model in
   `44b32f1`, and reconciler behavior with CLI/operator documentation in
   `c0261ae`. Split those layers.
4. KB commit `2630ac8d` combines annotation parser/test behavior with the
   generated contract pin/inventory update. Restore separate commits.

The reviewer found no other significant issue in the requested areas. It
confirmed final-name completeness, ordered command-line/digest semantics,
relational constraints and binary collations, `(observed_after,
observed_before]` meaning, authentication and service-role exclusion, exact
least-privilege scopes including `security_advisory.node_status`, draft
locking/revision checks, and the VPS-root versus Node-compromise wording.

Residual review notes: configuration and KB remotes must be fetched/reconciled
before push; regenerated pins must follow any rewritten head; the clean reset
and live collector/evaluator exercise remain required.

## Mandatory review resolution and final heads (2026-07-15)

All four Blocking findings from the single mandatory review were resolved;
the review was not repeated, as required by the review workflow.

- `security-advisories` no longer treats the collector's partial reconstructed
  event shape as exact evidence. Reconstructed events without an immutable
  snapshot require a complete operator attestation, and dossier validation now
  requires every field consumed by evaluation. The collector-to-evaluator
  regression is covered. Tooling/domain, collector/evaluator,
  reconciler/CLI, and individual dossier commits are separated.
- vpsAdmin introduces the final `node_kernel_*` and `node_sysctl` names in the
  original ingestion and typed-resource commits. Ordered kernel parameters
  and `(observed_after, observed_before]` documentation are independent
  commits; the vpsAdminOS input update remains last. The final tree is
  byte-for-byte identical to the previously reviewed implementation.
- The KB annotation parser/test change and generated navigation-contract pin
  are separate commits.

Final repository heads:

- vpsAdmin: `0e9c345f6c50b4c880382b237cc251a4eee9ed47`, force-pushed;
- vpsAdminOS: `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, unchanged;
- security-advisories: `334ae8d1e8ff7f426f075146ee1e3235cf73877c`, pushed
  to the newly created private remote;
- vpsfree-cz-configuration: `97220d423a3b49cce83ba36f2ec6b89d2e03f792`,
  force-pushed with generated `confctl` commits;
- vpsadmin-kb-captures: `c1c0fb2`, force-pushed.

The configuration lock resolves `vpsadminosStaging` to `d47ba226` and both
`vpsadminStaging` and `vpsadminServices` to `0e9c345f6`. The KB flake,
capture inventory, and navigation contract pin the same vpsAdmin revision.

Final quick verification after the history rewrite:

- vpsAdmin affected API/model/supervisor suite: 101 examples, 0 failures;
- isolated vpsAdmin migration suite: 10 examples, 0 failures;
- libnodectld component-shell suite: 5 examples, 0 failures;
- security-advisories: after the self-revocation follow-up, RuboCop inspected
  21 files without offenses and RSpec ran 64 examples with 0 failures;
- vpsadmin-kb-captures complete `bin/validate && bin/check`: 59 concepts,
  118 variants/PNGs, 34 controls, 29 paths, 32 capture concepts, 3 semantic
  selectors, and both test groups green.

The old session cluster was stopped, then its persisted state was reset. A
clean single-Node bridge-network cluster is running and ready from the exact
vpsAdmin and vpsAdminOS worktrees above. The prior migration timestamps could
not be upgraded in place because the unmerged history was intentionally
rewritten.

An ambient `vpsfree-cz-configuration` push failed locally before contacting
GitHub because its pre-push hook could not load bundled gems. The identical
lease-protected push passed inside `nix develop`; the reusable note is
`notes/vpsfree-cz-configuration/2026-07-15-push-hooks-require-nix-shell.md`.

Clean-cluster live verification:

- WebUI and API return HTTP 200 through the bridge-network endpoints.
- The schema-4 collector returned exactly active hosting Node 101. DNS and
  mailer/service Nodes were excluded. It collected Linux 6.12.95, the exact
  booted/current system closures, all six required `CONFIG_*` options, generic
  loaded-module/sysctl state, and no evidence gaps.
- `node_kernel_parameter#index` returned separate event/current relational
  rows with contiguous positions 0 through 4 and explicit `name`/nullable
  `value` fields. Their tokens reconstruct the configured parameter array
  exactly.
- All five dossiers evaluated the one authoritative Node and remained
  `unknown`, correctly fail-closing because the fresh cluster has no retained
  history back to `2026-01-01`. A dry-run sync for CVE-2026-23111 proposed one
  Node status and no writes; no advisory or draft was created.
- The real narrow token could read the typed evidence resources and received
  HTTP 403 for generic `node#index`.

The live cleanup exposed that HaveAPI describes self-revocation as the exact
`token#revoke` provider action. The repository now grants that one additional
non-domain action and provides `bin/revoke-token`; it still has no generic
inventory, VPS, publication, mail, or unrelated-resource authority. A new
24-scope token revoked itself successfully and removed its saved file. The
earlier 23-scope development token was closed and its token row deleted from
the disposable dev database. Generated `.state` evidence/evaluations and both
temporary credential files were removed.

Final GitHub Actions status:

- security-advisories RuboCop and RSpec are green on `334ae8d1`;
- all completed vpsAdmin workflows on `0e9c345f6` are green except the full
  platform shard of the topic-parallel API workflow, which GitHub cancelled at
  its 30-minute job limit while examples were still passing. Its complete log
  shows no failure before cancellation; the topic-coverage job and every other
  shard passed. The focused local platform tests covering this change passed;
- the vpsAdmin aggregate vpsAdminOS integration workflow remains in progress.

## 2026-07-15 software/sysctl evidence follow-up start

- The verified active session remains
  `2026-07-13-security-advisory-automation`; all five affected feature
  worktrees started clean and matched their remote feature branches.
- Starting heads are vpsAdmin `0e9c345f6`, vpsAdminOS `d47ba226a`,
  security-advisories `334ae8d1`, vpsfree-cz-configuration `97220d42`, and
  vpsadmin-kb-captures `c1c0fb25`.
- vpsAdmin `origin/master` remains `8028e5032`. vpsAdminOS `origin/staging`
  advanced from the feature base `ff9e49b20` to `c21989035` through a nixpkgs
  input update and packaged-gem update. Its unmerged feature branch will be
  rebased before the new implementation.
- Approved decisions are recorded in `plan.md`: booted/current identities for
  vpsAdminOS, vpsAdmin, and nixpkgs; grouped Nix deployment history; ordered
  configured and booted parameters; a versioned merit-based sysctl policy with
  availability and per-name history; and three admin-only Node detail pages.
- Receiver/API deployment precedes Node activation. Legacy schema-2 reports
  remain accepted, the new reporter emits schema 3, and exact legacy software
  history is not fabricated. The rewritten migrations require a clean dev
  cluster reset after mandatory review.

## 2026-07-15 software/sysctl evidence review checkpoint

All intended follow-up changes are committed and the review packet is frozen.
The final histories contain one vpsAdminOS input update and one generated pin
per configuration channel; superseded intermediate pins were removed before
review without changing the implementation trees.

Repository heads and commit shape:

- vpsAdmin is `f578c8adb77db7d64690524ecafa5c124aed1e19`, force-pushed.
  The follow-up is split into `5abee06af` for normalized API/database history,
  `b33f58c8e` for the schema-3 reporter, `b7855d72f` for the administrator
  WebUI, and `f578c8adb` for the separate final vpsAdminOS input pin.
- vpsAdminOS is `a42a9fc95997122769a1012ac208214b56c6dfae`,
  force-pushed after rebasing on current `origin/staging`. Its follow-up is the
  focused `os: expose exact nixpkgs build identity` commit on top of the
  existing boot/livepatch/eBPF evidence series.
- security-advisories is
  `829fa15aaa79ded43fef62ec33adff1e8ca9d2a4`. The follow-up adds typed exact
  software collection, schema-3 completeness/digests, and matching minimal
  token scope in one evidence-contract commit. It is committed locally and
  pending the review gate before push.
- vpsadmin-kb-captures is
  `2f86e434526c815427d68231c3bdaf37841e0dc2` locally. Its final contract commit
  pins vpsAdmin `f578c8adb`, refreshes the production navigation inventory,
  and registers kernel history, ordered parameters, sysctls, and software
  versions. The three new administrator pages have no current end-user KB page
  or screenshot bindings.
- vpsfree-cz-configuration is
  `1e340b498de25370c635d7cae34d78a0b4ee7d08` locally. Three clean generated
  confctl commits pin staging vpsAdminOS to `a42a9fc9` and staging/services
  vpsAdmin to `f578c8ad`; production vpsAdminOS remains unchanged.

Quick verification before review:

- vpsAdmin focused model/operation/supervisor/API-resource and advisory specs
  passed in their ordinary database; the isolated migration suite passed.
- libnodectld's schema-3 reporter specs passed. The vpsAdmin build-info module
  evaluated to schema 1 with the exact injected revision and version.
- vpsAdmin WebUI regression specs passed with 3 tests and 13 assertions. API
  and WebUI catalogs regenerated successfully, Czech uses `Node`, and all
  affected RuboCop/PHP CS Fixer/Nixfmt/migration/i18n hooks passed.
- vpsAdminOS system evaluation succeeded and its metadata evaluation returned
  the exact nixpkgs revision/version with evidence schema 3. `nix flake check
  --no-build` still reaches the repository's pre-existing invalid
  `overlays.all` list output; the targeted system check used by this change is
  green.
- security-advisories RSpec passed 65 examples with no failures, RuboCop
  inspected 21 files without offenses, and its staged Overcommit hook passed.
- vpsadmin-kb-captures `nix develop -c bin/check` passed: 37 controls, 29
  paths, 32 capture concepts, 3 selectors, 65 bindings, 9 exceptions, both
  test groups green, and all 118 PNG variants valid. The final rewritten pin
  was rechecked against the byte-identical vpsAdmin source tree.
- All generated confctl commits ran the active Nixfmt hook successfully. One
  attempted pin used a mistyped nonexistent vpsAdmin revision and failed with
  HTTP 404 before changing `flake.lock`; the exact revision read from Git then
  succeeded.

Compatibility remains additive. vpsAdmin accepts evidence schemas 2 and 3;
the reporter emits schema 3 only after the tolerant receiver/API is deployed.
The six exact software identities, booted parameters, and policy availability
are never synthesized for schema-2 history. A rollback ignores the new rows,
but cannot reconstruct identities that were not reported. Since the unmerged
migration was rewritten in place, the next integration step is a clean
bridge-network dev-cluster reset after the standalone review.

## 2026-07-15 mandatory software/sysctl review resolution

The one required fresh-context standalone review completed and was not
repeated. It found one Blocking schema-contract issue, two Important findings,
and two Advisory hardening opportunities. Every finding was resolved before
the clean integration test:

1. Schema 3 now supports one explicit policy version whose exact 35-control
   inventory is shared consistently by reporter, receiver/API, and advisory
   evaluator. Empty/partial maps and unknown policy versions fail closed.
   Software version and revision fields must be nonempty at receiver,
   API-completeness, evaluator, and historical-attestation boundaries.
2. vpsAdminOS records a nixpkgs revision only when the actual `pkgs.path`
   matches the flake input source. Caller-supplied package sets with unproven
   provenance record no revision, and dirty input metadata is never stripped
   into a clean-looking commit.
3. The WebUI labels an available but unread sysctl as an effective-value read
   failure, not as effective. Czech translates this as
   `efektivní hodnotu se nepodařilo načíst`.
4. A sysctl policy-version-only transition now creates an immutable internal
   history event even when serialized values are unchanged.
5. nodectld validates that parsed metadata is a JSON object; arrays, scalars,
   and null become explicit evidence gaps instead of aborting Node status
   construction.

Post-fix focused verification:

- security-advisories RuboCop: 21 files, no offenses; RSpec: 67 examples,
  0 failures, including receiver-equivalent empty/partial/unknown-policy and
  historical-attestation cases;
- vpsAdmin API/model/supervisor/operation resources: 48 examples, 0 failures;
- libnodectld probe: 3 examples, 0 failures;
- WebUI evidence regression: 4 tests, 15 assertions; all repository hooks for
  the API, reporter, and WebUI fix folds passed;
- vpsAdminOS Nix formatting and targeted system evaluation passed; a matching
  package set evaluates the exact nixpkgs revision
  `8eeec934ae0dbeca3d7868c059568a65c08b2fc3`;
- the three policy inventories were compared mechanically and are identical,
  sorted, and contain 35 controls.

Fixes were folded into their owning commits. Final pre-integration heads are
vpsAdmin `a757f6918123bd445ad71a47e45290857f216a85`, vpsAdminOS
`2b86a03952cc322bf43b506908bcf05e370d18d8`, security-advisories
`7e3979bf1c07a10442c6eebfdfab4f96a8359bb8`, vpsadmin-kb-captures
`0a551088637562c288261db206593df83b499cdd`, and
vpsfree-cz-configuration `814f02621b4719c33a4d59d0137c484513511c8c`.
The final contract and generated configuration pins resolve those exact
vpsAdmin/vpsAdminOS revisions.

## Final clean integration and live workflow (2026-07-15)

The clean bridge-network cluster exposed one additional integration gap after
the mandatory review: vpsAdminOS' raw test-framework evaluation did not carry
the locked nixpkgs revision into the generated closure. The receiver correctly
rejected that first schema-3 report instead of accepting a partial software
identity. Production flake systems already received the identity module; the
test framework now carries the same locked revision only when the evaluated
`pkgs.path` is the matching nixpkgs source. An unrelated caller-supplied
package set still records no revision. The active Node was updated and the
cluster was stopped and started so both booted and current closures contain
nixpkgs `8eeec934ae0dbeca3d7868c059568a65c08b2fc3`.

The resulting final heads are:

- vpsAdmin `d57c6f0fc66927bf5cea16dd10cbe519b31a3c86`, pushed;
- vpsAdminOS `6a8f1d35539f9aade7a0535a535587f025aa96d2`, force-pushed;
- security-advisories `7e3979bf1c07a10442c6eebfdfab4f96a8359bb8`, pushed;
- vpsfree-cz-configuration
  `fa01112c44afa31f53d21cc3e278ba3fef2cf6a0`, force-pushed with generated
  confctl commits for the corrected staging/services pins;
- vpsadmin-kb-captures
  `e060503b2de25c963ded49a1567de43d1b847452`, force-pushed and pinned to the
  exact final vpsAdmin/vpsAdminOS revisions.

Final live verification on the running, ready, single-Node bridge cluster:

- WebUI and API return HTTP 200. The normalized database contains one hosting
  Node and excludes the mailer and two DNS service Nodes from kernel evidence.
- Node 101 reports evidence schema 3 with no gaps. The canonical kernel
  configuration contains 8,047 parsed relational options; the advisory
  collector requested the six dossier-relevant options and received all six.
- Both current and event snapshots contain the exact 35-control sysctl policy:
  34 controls are available and one is explicitly unavailable. The initial
  event contains typed before/after sysctl rows and all six booted/current
  software identities.
- Configured kernel parameters reconstruct at positions 0 through 4 and the
  actual boot command line at positions 0 through 8, preserving order and
  values independently. The first boot event correctly has no
  `observed_after` lower bound and has its first `observed_before` upper bound.
- A real token created by `bin/create-token` had mode 0600 and exactly 25
  scopes: the typed evidence indexes, draft advisory/CVE/Node-status actions,
  and self-revocation. Collection returned evidence schema 5 for Node 101 only.
- All five CVEs evaluated that Node as `unknown`, fail-closing because the
  clean cluster has no history back to 2026-01-01. Dry-run sync for
  CVE-2026-23111 proposed one unknown Node status and no write; no advisory or
  draft was created.
- The automation token received HTTP 403 for generic `node#index` and
  `security_advisory#publish`. A normal member token received HTTP 200 for the
  nested public `node.kernel_history#index` and HTTP 403 for admin-only
  sysctls. All temporary tokens were revoked or removed from the disposable
  database, token files and generated `.state` files were removed, and no
  credential remains.
- The complete KB check remains green: 37 controls, 29 paths, 32 capture
  concepts, 3 semantic selectors, 65 bindings, 9 exceptions, both test groups,
  and all 118 PNGs.

Current-head GitHub checks are green for security-advisories RuboCop/RSpec and
the completed vpsAdmin and vpsAdminOS jobs. The long selected vpsAdmin
integration run `29432504910` and vpsAdminOS test-suite run `29432240364` are
still in progress at this checkpoint. Superseded vpsAdmin run `29429676226`
was cancelled after confirming that its head was obsolete.

The cluster remains running for review. No production deployment, vpsAdmin
advisory mutation/publication, user notification, or KB write was performed.

## Node evidence WebUI presentation completion (2026-07-15)

- vpsAdmin head `c5803845cc841d0c415b9009fe5878dcea23589c` is
  pushed. The functional WebUI commit is `b27406af2`; focused tip commit
  `c5803845c` updates the shared advisory browser fixture for the existing
  optimistic-concurrency publication contract.
- vpsfree-cz-configuration head
  `e8e60e4d4a999188b4b1e72e6abc86adf566e270` is force-pushed with exactly
  three generated pin commits from `e1cc165c`: `751bb183`, `81dea6ca`, and
  `e8e60e4d`. vpsadmin-kb-captures head
  `1adabf736d5bde9dd6b65d916b65b48d2b5efc6a` is force-pushed and pins the
  exact final vpsAdmin revision.
- WebUI PHPUnit passes 72 tests and 267 assertions. The complete KB contract
  check passes. `webui#admin-cluster` passes its Playwright scenario, including
  boot-position order, raw-command-line code markup, neutral descriptions,
  compact table columns, and horizontal-overflow checks.
- The first integration attempt failed during fixture creation before
  Playwright because `SecurityAdvisory#publish!` now requires
  `expected_content_revision`. The preserved log identified the exact call;
  passing `advisory.content_revision` fixed it, and the cached rerun passed.
- The same mandatory standalone reviewer checked this post-gate delta and the
  regenerated downstream pins. The result contains no Blocking, Important, or
  Advisory findings, and no residual test gap.
- The bridge development cluster remains `running` and `ready` on the default
  network, with WebUI and API returning HTTP 200 through the development CA.
  Its active services generation contains the final runtime WebUI changes;
  `c5803845c` changes test fixtures only.
- Current-head vpsAdmin CI run `29441379490` is still executing the full
  `tag=ci` set because the fixture lives in shared `tests/suite/webui.nix`.
  Setup, selection, and preview are green and the check has no annotations at
  this checkpoint. Superseded in-progress runs `29439429583`, `29438336356`,
  and `29432504910` were cancelled only after their heads became obsolete.
- All three affected project worktrees are clean and synchronized with their
  SSH remotes. No production deployment, API mutation, advisory publication,
  notification, KB staging, or KB publication was performed.

## 2026-07-16 exact closure final rollout

The exact-closure refinement is complete and all five project worktrees are
clean and synchronized with their SSH feature branches:

- vpsAdmin `9de28b8fb92c383f50e5ca3605642d7a78b46cf1`;
- vpsAdminOS `dbc03d00508b89093ecafc5e5abdcfc6bb5bdfbb`;
- security-advisories `ce0aca81789c7dec31a939ddd5c88ebeafdc7281`;
- vpsadmin-kb-captures `3fb8b0cfe7b53cfd83724766cb333553b96d3c46`;
- vpsfree-cz-configuration
  `9a7db1519ebea5bdc003c7232a5a167c50af18c9`.

The configuration branch consists of three generated confctl commits that pin
staging vpsAdminOS and staging/services vpsAdmin to the exact final revisions.
The KB contract pins the same vpsAdmin head and its complete contract check is
green. The top-level exact source-injection implementation is published on
workspace master as `cf437a53809cbc9b25d78bd7585325763ff26e86`.

The previous cluster was stopped and its state was reset before integration.
The final single-Node cluster is running and ready on the bridge network. A
clean temporary checkout was required so unrelated shared-workspace
notification edits could not enter the build. Nix rejected symlinked path
inputs, so project inputs were real detached worktrees. Workspace master also
contains an unmerged notification-stack harness whose NixOS options do not yet
exist on vpsAdmin master. The final build therefore used compatible committed
harness baseline `a98bdb9` plus only the 47-line source revision/dirty-state
plumbing from `cf437a5`; product inputs remained the exact clean final commits.
Both issues have durable troubleshooting notes.

Live evidence verification through the real narrow API token established:

- Node 101 is the only active kernel-hosting Node; DNS and other service roles
  are excluded from the evidence set;
- report schema 4 has no evidence gaps and identifies kernel `6.12.95`;
- booted and current vpsAdminOS are `dbc03d005`, vpsAdmin is `9de28b8fb`, and
  nixpkgs is `8eeec934ae0dbeca3d7868c059568a65c08b2fc3`; all six identities have
  native provenance and `revision_dirty=false`;
- booted/current system paths are identical in this fresh cluster, while the
  API still stores the two generations separately;
- `/proc/cmdline` reconstructed exactly as nine typed rows at positions 0
  through 8, including the valueless `quiet` token. There is no configured
  parameter origin or configured-parameter data;
- the typed sysctl resource contains the exact 35-control merit-based policy;
  the six dossier-required kernel options were retrieved by exact-name filters
  from the digest-addressed relational configuration;
- the first boot event correctly has `observed_after=null` and a populated
  `observed_before`, because no earlier observation can bound its lower side.

`bin/create-token` wrote a mode-0600 token with exactly 25 scopes. The complete
collector returned schema-5 evidence for Node 101 and all five CVEs fail-closed
to `unknown`: the fresh development database cannot prove history back to
2026-01-01. The real apply workflow created development draft 1, its CVE row,
and Node 101's unknown status. `ready` refused the draft because the Node is
unknown and resolution is incomplete. Generic `node#index` and
`security_advisory#publish` both returned HTTP 403. The token was then revoked
and its file removed; ignored development evidence/evaluation files were also
removed. The development draft remains for WebUI review, but no advisory was
published and no mail or user notification was sent.

Final current-head CI status at this checkpoint:

- security-advisories RuboCop and RSpec are green;
- vpsAdmin migration, RuboCop, WebUI, client, libnodectld, and i18n workflows
  are green. The topic-parallel full platform shard was cancelled exactly at
  its configured 30-minute timeout while examples were still passing; its log
  reached the new evidence resource specs without a test failure, and every
  other shard plus topic coverage passed. The long integration CI remains in
  progress;
- vpsAdminOS RSpec and the closure-build job are green; its long test-suite job
  remains in progress.

The bridge cluster is intentionally left running for review. Its state and
source mounts depend on
`/tmp/vpsfree-security-advisory-devcluster-compat-20260715` until it is stopped.
