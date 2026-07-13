# 2026-07-13-security-advisory-automation

## Current status

- The requested implementation and all mandatory-review fixes are committed in
  five independent repositories. Four feature branches are pushed. The new
  `security-advisories` repository is committed locally and cannot be pushed
  until its GitHub repository exists.
- Exact feature revisions are pinned only in non-production configuration
  channels. No production deployment, vpsAdmin API write, KB staging, or KB
  publication has occurred.
- Quick local verification and the mandatory standalone review are complete.
  All blocking and important findings were resolved. A follow-up removed
  redundant deployment metadata in favor of confctl's existing machine input
  file, and its focused tests and final repository checks pass.
- The initiative development cluster is running and ready with the `single`
  topology on the bridge network.
- Live per-Node conclusions are intentionally not fabricated from repository
  pins. Until the feature is deployed and exact evidence is collected, the five
  dossiers produce `unknown` rows that may be reviewed in a draft but cannot be
  published.

## Repositories and revisions

### vpsadmin

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadmin`
- Base: `458b2ac71` (`origin/master` when created)
- Head: `f934d9312a63074e84bb0dfb558704c8dd39626a`, pushed to `origin`
- Commits:
  - `dd6f40ca5 api: lock security advisory draft revisions`
  - `9854f62fc api: reconstruct Node kernel history`
  - `f94b71e5f api: store Node security evidence`
  - `5ff1c8c29 libnodectld: report Node security evidence`
  - `dcc8f1b8f webui: show Node kernel history`
  - `f934d9312 api: harden security advisory draft synchronization`

### vpsadminos

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadminos`
- Base: `9daf6d67e` (`origin/staging` when created)
- Head: `58be2dd0177427f27e62960f4b5a1b99b4086ac7`, pushed to `origin`
- Commits:
  - `54f2e17b5 os: expose booted kernel build evidence`
  - `3d5bc4a72 os: record livepatch application time`
  - `58be2dd01 os: expose eBPF live-patch link metadata`

### vpsfree-cz-configuration

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsfree-cz-configuration`
- Base: `e1cc165c` (`origin/master` when created)
- Head: `2a76fcb5f8a5de24539e0a8213275350fa2fe58d`, pushed to `origin`
- Commits:
  - `e0235b02 inputs: set vpsadminosStaging to 58be2dd0`
  - `4cfdc892 inputs: set vpsadminStaging to f934d931`
  - `2a76fcb5 inputs: set vpsadminServices to f934d931`
- The input commits were generated with `confctl`; production channels remain
  unchanged. The earlier `nodes: record deployment inputs` commit was removed:
  production Nodes already receive `/etc/confctl/inputs-info.json` from
  confctl, so a second reduced copy was unnecessary.

### vpsadmin-kb-captures

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadmin-kb-captures`
- Base: `470b759`
- Head: `6d45dc0c742d84fdf9919d750004fec2e647aaf4`, pushed to `origin`
- Commits:
  - `f4579b0 contract: track the Node kernel history control`
  - `356ae81 tools: ignore literal navigation tag examples`
  - `6d45dc0 contract: refresh production navigation inventory`

### security-advisories

- Orphan branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/security-advisories`
- Head: `35ca6b94f76658b9bbb5c451e972fc300ebb6e50`
- Commits:
  - `93e8cae Establish the advisory analysis repository`
  - `681e00f Add the narrow vpsAdmin API client`
  - `cb11c30 Create least-privilege vpsAdmin tokens`
  - `00fc520 Evaluate exact deployed Node evidence`
  - `d2c2ba0 Reconcile reviewed advisory drafts safely`
  - `212247d Add the review-gated advisory CLI`
  - `7f549c2 Analyze CVE-2026-23111 nf_tables UAF`
  - `853f6c9 Analyze CVE-2026-46242 epoll flaw`
  - `e0614e1 Analyze CVE-2026-53362 IPv6 flaw`
  - `1e56368 Analyze CVE-2026-53359 KVM flaw`
  - `abbc41d Analyze CVE-2026-43499 GhostLock`
  - `35ca6b9 Test the complete advisory workflow`
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
- Czech follows `doc/i18n-cs.md`: `Node`, `Nody`, and `nod` are used; `uzel` is
  not used. The page label is `Podrobnosti nodu`.
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
  loaded modules, runtime settings, and the exact role/input identity read from
  `/etc/confctl/inputs-info.json`. A missing file is an explicit evidence gap.
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
- Production Nodes already receive `/etc/confctl/inputs-info.json` from
  confctl. The reporter wraps its selected role metadata under
  `deployment.inputs`; it does not install a duplicate metadata file or expose
  secret/general configuration data through the evidence endpoint.

### security-advisories

- The dependency-free Ruby CLI provides `validate`, `collect`, `evaluate`,
  `adopt`, and `sync`. Sync is dry-run by default and requires `--apply`; there
  is no publish command.
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

- The contract pins vpsAdmin `f934d931...` and records the bilingual
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
lost create response without duplicating drafts. The reporter has an explicit
`inputs_info` gap for missing confctl data.

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
- security-advisories: 38 tests, 131 assertions, no failures; all five dossiers
  validate; all Ruby files pass syntax checking; `git diff --check` passes.
- vpsadmin-kb-captures `nix develop -c bin/check` passes: 34 controls, 29 paths,
  32 concepts, 3 selectors; 65 bindings and 9 exceptions; 118 valid PNGs; test
  groups at 8/50 and 7/17 runs/assertions.
- The confctl reuse follow-up passes its focused libnodectld spec (1 example),
  RuboCop on both affected reporter files, all vpsAdmin pre-commit hooks, and a
  repeated full KB contract check with the final vpsAdmin pin.
- Dev cluster `2026-07-13-security-advisory-automation` is `running`, `ready`,
  topology `single`, network `bridge`. WebUI and API are reachable at
  `https://webui.aitherdev.int.vpsfree.cz/` and
  `https://api.aitherdev.int.vpsfree.cz/`.
- The cluster was rebuilt after the final history rewrite. Both endpoints
  return HTTP 200, and the live API description exposes
  `node.kernel_history#index`, `node.security_evidence#index`, advisory
  `external_id`/`content_revision`, and expected-revision parameters on the
  advisory and nested Node-status mutation actions.
- The final vpsAdmin head is green for API migrations, all 27 topic-parallel
  API jobs and endpoint coverage, RuboCop, WebUI PHPUnit, i18n health, and
  libnodectld specs. Its selected VM integration suite remains in progress.
- Final-head vpsAdminOS GitHub CI completed successfully, including the OS
  closure build and VM test suite.
- A superseded API-specs run failed because the two new endpoints were missing
  from the endpoint-coverage manifest. Logs were inspected, the manifest was
  fixed in the final evidence commit, and superseded runs were cancelled after
  the updated branch was pushed.
- After the history rewrite, the remaining superseded vpsAdmin CI run for old
  head `2cf07d4d...` was explicitly cancelled; new-head runs were left intact.
- Final-head migration CI initially found that the new spec called the local
  two-argument `index_exists?` helper with an Active Record keyword. The logs
  were inspected, the spec was changed to inspect the exact index and unique
  flag, the focused suite passed locally, and final-head migration CI is green.
  Superseded long/API jobs for `67281212...` were cancelled.

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

1. Confirm the final-head vpsAdmin selected integration CI completes
   successfully.
2. User creates the private `vpsfreecz/security-advisories` GitHub repository;
   then push `35ca6b94f76658b9bbb5c451e972fc300ebb6e50` over its already
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
- No production vpsAdmin or KB write was made.
