# 2026-07-13-security-advisory-automation

## Current status

- The implementation is committed in five repositories and pushed in the four
  repositories whose GitHub remotes already exist.
- The new `security-advisories` repository is committed locally. Its configured
  SSH remote is `git@github.com:vpsfreecz/security-advisories.git`; pushing is
  blocked only because the user has not created that GitHub repository yet.
- Exact feature revisions are pinned only in non-production configuration
  channels. No production API write, deployment, KB staging, or KB publication
  has occurred.
- Quick verification and repository hooks pass. The mandatory independent
  change review is the next step, before longer dev-cluster integration tests.

## Repositories and revisions

- `vpsadmin`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree: `worktrees/2026-07-13-security-advisory-automation/vpsadmin`
  - base: `458b2ac71` (`origin/master` when created)
  - head: `2a52cf35a08958911190b3e54d7a18c108f62115`
  - pushed to the same branch on `origin`
- `vpsadminos`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree: `worktrees/2026-07-13-security-advisory-automation/vpsadminos`
  - base: `9daf6d67e` (`origin/staging` when created)
  - head: `bbc8c01547fa36409d9aba365cae52c98c864589`
  - pushed to the same branch on `origin`
- `vpsfree-cz-configuration`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree:
    `worktrees/2026-07-13-security-advisory-automation/vpsfree-cz-configuration`
  - base: `e1cc165c` (`origin/master` when created)
  - head: `7b7877a8`
  - pushed to the same branch on `origin`
  - commits: deployment evidence plus generated exact pins for
    `vpsadminosStaging`, `vpsadminStaging`, and `vpsadminServices`
- `vpsadmin-kb-captures`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree:
    `worktrees/2026-07-13-security-advisory-automation/vpsadmin-kb-captures`
  - base: `470b759`
  - head: `fd7b1ff`
  - pushed to the same branch on `origin`
- `security-advisories`
  - orphan branch: `2026-07-13-security-advisory-automation`
  - worktree:
    `worktrees/2026-07-13-security-advisory-automation/security-advisories`
  - head/root commit: `3520fe3`
  - remote configured but not created; not pushed

## Implemented behavior

### vpsAdmin

- Added `content_revision` optimistic locking for ordinary advisory, CVE, and
  advisory node-status mutations. All such mutations are draft-only; published
  advisories cannot be changed through these actions. There is no new
  `submit_draft` action.
- Added exact and reconstructed `NodeSecurityEvent` history. The one-time
  `vpsadmin:node:reconstruct_kernel_history` task reconstructs boots and
  same-boot reported-release changes from `node_statuses`, retains observation
  intervals/confidence, is idempotent, and promotes matching reconstructed
  events when exact node evidence arrives.
- Added authenticated, sanitized `node.kernel_history#index`, including inactive
  nodes. It excludes boot IDs and internal evidence.
- Added admin-only `node.security_evidence#index`. It returns active node/storage
  node identity, freshness/revision, exact kernel/build/config facts, history,
  livepatch/eBPF state, loaded modules, selected runtime settings, deployment
  revisions, and explicit gaps. It excludes tenants, VPSes, IPs,
  `untrusted_vps`, KVM counts, and general node metrics.
- Extended nodectld status with schema-versioned evidence: boot ID/time,
  immutable booted release, reported release, vpsAdminOS/kernel revision,
  config digest and selected reachability/hardening options, livepatch state,
  verified eBPF pins, loaded modules, runtime settings, and deployment inputs.
- Added a WebUI kernel-history page and linked node kernel values to it. Czech
  uses `Node`/`Nody` terminology; the label is `Podrobnosti nodu`, never
  `uzel`.

### vpsAdminOS and configuration

- vpsAdminOS installs `/etc/vpsadminos/security-evidence.json` with the exact OS
  revision, boot kernel identity, kernel source revision, and config store path.
- eBPF livepatch metadata includes the link fields required to verify all pinned
  attachments.
- vpsfree-cz-configuration installs a reduced
  `/etc/vpsadminos/deployment-evidence.json` containing only revision/hash/time
  metadata for flake inputs.
- Only staging node and vpsAdmin service inputs point at the feature revisions;
  production inputs are unchanged.

### security-advisories

- Added a pure-Ruby CLI with `validate`, `collect`, `evaluate`, `adopt`, and
  `sync` commands. Sync defaults to reviewable/dry-run usage, uses only existing
  resource actions, refuses unresolved node results, detects review drift, uses
  `content_revision` before every write, reads back the result, and cannot
  publish.
- Added an interactive token creator that requests exactly 12 resource scopes
  and stores the token with mode `0600`. Token issuance/TOTP are HaveAPI
  authentication operations rather than extra resource scopes.
- Per-node evaluation verifies retained kernel history, stable-version rules,
  selected booted config options, optional reviewed config digests, livepatch
  and eBPF state, freshness, and evidence gaps. Missing/stale evidence yields
  `unknown`; inferred mitigation preserves last-known-vulnerable and
  first-known-mitigated bounds.
- Added detailed bilingual dossiers for CVE-2026-23111, CVE-2026-46242,
  CVE-2026-53362, CVE-2026-53359, and CVE-2026-43499. Public text separately
  addresses root in the VPS user namespace, host-node root/escape, cross-VPS
  access, and node availability. UAF hardening and monitored failure modes are
  described without claiming prevention or demonstrated node escape.

### Documentation contract

- Pinned `vpsadmin-kb-captures` to vpsAdmin `2a52cf35...` and registered the
  bilingual `node.kernel-history` landmark with its reviewed source
  fingerprint.
- No current KB page or screenshot concept documents host-node kernel history,
  so the control intentionally has no page/capture binding. No KB content was
  changed or staged.

## Verification

- vpsAdmin targeted API run: 44 examples, 0 failures. Covered advisory/CVE/node
  status revision conflicts, published mutation rejection, public history,
  admin evidence authorization/output, reconstruction, exact event recording,
  and supervisor ingestion.
- Dedicated migration run: 4 examples, 0 failures, including up/down behavior
  for both new migrations.
- libnodectld focused run: 4 examples, 0 failures.
- vpsAdmin API and libnodectld RuboCop: no offenses.
- vpsAdmin WebUI locale generation/health and PHP syntax: passed.
- vpsAdmin complete `overcommit --run`: passed MigrationSpecs,
  VpsadminWebuiI18n, VpsadminApiI18n, Nixfmt, PhpCsFixer, and RuboCop.
- vpsAdminOS Nix evaluation:
  `nix eval .#packages.x86_64-linux.toplevel.drvPath --raw` passed.
- vpsAdminOS complete `overcommit --run`: passed Nixfmt and RuboCop.
- vpsfree-cz-configuration complete `overcommit --run`: passed Nixfmt and
  RuboCop.
- `confctl build -y "cz.vpsfree/nodes/stg/*"` evaluated configuration and
  modules, then stopped while forcing the system closure because the local
  machine lacks `/secrets/nodes/initrd/ssh_host_ed25519_key`. This is an
  external secret, not a Nix evaluation error; see the durable note recorded
  for this initiative.
- security-advisories: 15 tests, 69 assertions, 0 failures; all five dossiers
  validate; `nix flake check` passes.
- vpsadmin-kb-captures `nix develop -c bin/check`: valid contract with 34
  controls/29 paths, annotation inventory tests green, and all 118 PNG variants
  valid.

## Compatibility and deployment

- Migrations and API resources are additive. Existing clients ignore new
  fields.
- Old nodectld payloads remain valid; evidence is shown as missing until the
  node-side package is deployed. Unsupported future evidence schema versions
  are ignored without losing ordinary status.
- vpsAdmin stores current evidence and its semantic event atomically, so a
  failed event write is retried by the next node report rather than silently
  advancing the comparison baseline.
- Missing OS/configuration metadata is an explicit gap and blocks a confident
  automation result.
- Deployment order: vpsAdmin migration/receiver, node-side vpsAdmin package,
  vpsAdminOS/configuration metadata, then one-time reconstruction and evidence
  collection. Rolling upgrades are supported; no coordinated all-node update
  or reboot is required.
- Rollback may leave additive tables/columns and metadata files, which older
  code ignores. New stored evidence is JSON/schema-versioned; no old persisted
  format is rewritten.

## Blockers and next steps

1. Run the mandatory fresh-context change review and record its findings.
2. Address significant findings, then run proportionate longer integration
   tests (dev vpsAdmin API and scoped-token allow/deny matrix).
3. The user creates `vpsfreecz/security-advisories`; then push `3520fe3` over
   SSH and use its branch/commit in review links.
4. With a scoped vpsAdmin token and deployed evidence support, collect live
   node evidence. Current repository/config defaults do not prove which kernel
   each node booted.
5. Resolve every `unknown`, inspect dry-run output, and only then create/update
   drafts. Human review and publication remain separate.

## Cleanup

- Worktrees remain active for review/integration.
- No feature branch has been merged or deployed.
- No production vpsAdmin or KB writes were made.
