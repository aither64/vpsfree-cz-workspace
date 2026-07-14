# 2026-07-13-security-advisory-automation

## Current status

- A follow-up API redesign is in progress. The unmerged collector-specific
  `nodes/all/security_evidence` hash response is being replaced by top-level,
  typed, filterable HaveAPI resources. Complete kernel options will be parsed
  into relational rows at ingestion, and the advisory collector will query
  only option names required by committed dossiers. The final feature history
  will be rewritten so the opaque route/schema is never introduced.
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
- The initiative development cluster is running and ready with the `single`
  topology on the bridge network. Its kernel-host Node is booted and activated
  at the same final closure and reports complete schema-v2 evidence without
  gaps; service-only Nodes report neither kernel nor security evidence.
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
