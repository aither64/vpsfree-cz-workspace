# 2026-07-13-security-advisory-automation

## Repositories

- `vpsadmin`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree:
    `worktrees/2026-07-13-security-advisory-automation/vpsadmin`
  - base: `origin/master` at `458b2ac71`
- `vpsadminos`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree:
    `worktrees/2026-07-13-security-advisory-automation/vpsadminos`
  - base: `origin/staging` at `9daf6d67e`
- `vpsfree-cz-configuration`
  - branch: `2026-07-13-security-advisory-automation`
  - worktree:
    `worktrees/2026-07-13-security-advisory-automation/vpsfree-cz-configuration`
  - base: `origin/master` at `e1cc165c`
- `vpsadmin-kb-captures`
  - affected by the newly proposed user-visible kernel-history WebUI;
  - no worktree prepared yet because this phase is design-only and the capture
    contract changes with the eventual implementation.
- `security-advisories`
  - intended remote: `git@github.com:vpsfreecz/security-advisories.git`
  - not created locally because the upstream repository does not exist yet

## Status

- Active initiative verified through both `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Isolated reference/feature worktrees prepared for the three existing
  repositories. No source changes or commits have been made.
- Repository-local `AGENTS.md` files read in all worktrees.
- The end-to-end architecture, least-privilege boundary, repository layout,
  and preliminary assessment of all five requested CVEs are documented in
  `plan.md`.
- The design now separates an authenticated user-visible kernel lifecycle from
  the richer admin-only security-evidence snapshot and defines user-focused
  advisory text requirements.
- The unpublished kernel-log initiative was inspected read-only. It is fully
  implemented and locally reviewed/tested, not merely a sketch, but remains
  unpushed, unmerged, and undeployed.

## Commands run

- `bin/dev-session current`
- `git status --short` in the shared coordination checkout
- `bin/dev-session worktree add 2026-07-13-security-advisory-automation <repo> --as-is`
  for `vpsadmin`, `vpsadminos`, and `vpsfree-cz-configuration`
- `git status --short --branch` and `git remote -v` in all worktrees
- read all three repository-local `AGENTS.md` files
- read `work/2026-07-10-node-kernel-version-logs/{plan,state}.md`
- inspected vpsAdmin security advisory models, migration, resources, specs,
  token/session scope handling, node resources, nodectld status production,
  supervisor status ingestion, and historical node status API
- inspected vpsAdmin VPS feature defaults, creation/migration paths, nodectld
  device grants, and `/dev/kvm` exposure
- inspected the existing public node status, raw historical node-status API,
  persistence interval, and current WebUI kernel presentation
- inspected vpsAdminOS kernel configuration, packaged kernel revisions,
  cumulative livepatches, eBPF programs, and production configuration pins
- queried the official CVE records and upstream Linux stable commits for all
  five identifiers, and verified fix-commit ancestry in the pinned custom
  6.12.95 kernel revision
- fetched the top-level `origin/master` and verified it had not diverged before
  recording this initiative
- `git diff --check` on `plan.md` and `state.md`

## Results

- Shared top-level changes existed before this initiative and were not touched.
- All project remotes use the required SSH URLs.
- vpsAdmin detached tokens accept exact HaveAPI action scopes and optional path
  restrictions. `all` is not required.
- Security-advisory draft creation, update, CVE association, per-node status
  creation/update, and reads already have individual scopes. Publication is a
  separate `security_advisory#publish` action and can be excluded.
- vpsAdmin nodes already submit `kernel` and `uptime` every two minutes over
  their existing status channel. The API stores sampled history in
  `node_statuses` approximately every 15 minutes and exposes it through the
  admin-only, separately scoped `node.status#index` action.
- Historical sample time minus uptime can reconstruct the boot instant without
  log-server access. Production retention still needs to be established.
- The reported `kernel` is the mutable UTS release. vpsAdminOS's cumulative
  livepatch changes this value, so it cannot be treated as immutable proof of a
  rebooted kernel. Future reports need boot ID, immutable booted kernel,
  vpsAdminOS revision, and verified livepatch/eBPF state.
- Direct `node.status#index` access is possible but unnecessarily discloses
  general node metrics and transfers raw samples. A narrow
  `node.security_evidence#index` aggregate is the recommended interface.
- Add a separate `node.kernel_history#index` projection for all logged-in users.
  Backfill a first-class event log from `node_statuses`; preserve inferred time
  bounds and confidence instead of presenting 15-minute samples as exact.
- Link the existing WebUI kernel value to a per-node boot/livepatch timeline.
  This makes `vpsadmin-kb-captures` an affected repository for implementation.
- Use the existing advisory, CVE, and node-status resource actions rather than
  adding `security_advisory#submit_draft`. The client reconciles them
  idempotently; an interrupted sequence leaves only an incomplete unpublished
  draft and converges on rerun.
- Scope the token to advisory index/show/create/update, CVE index/create/delete,
  node-status index/create/update/delete, security evidence, and self-revoke.
  Publication, mail, retraction, generic node/VPS access, sessions, and `all`
  remain excluded.
- Review feedback is committed to the repository and reconciled into the same
  draft. A canonical snapshot digest/optimistic precondition detects concurrent
  WebUI edits. Existing mutation actions should reject published/retracted
  advisories.
- New VPSes enable the KVM feature by default. nodectld grants character device
  10:232 as `/dev/kvm`, and pool defaults permit that device. A tenant can run
  KVM userspace and a nested guest, so CVE-2026-53359 must be treated as
  reachable on affected nodes with KVM-enabled VPSes. The evidence endpoint
  should expose only a per-node aggregate, not tenant or VPS records.
- Current vpsAdminOS kernel hardening includes init-on-alloc, init-on-free,
  hardened/randomized slab freelists, non-merged slabs, stack initialization,
  and strong stack protectors. These controls reduce reliability for some UAFs
  but do not block the triggers of the requested CVEs.
- The currently pinned custom vpsAdminOS 6.12.95 kernel contains all five
  upstream fixes. The prior 6.12.93 kernel lacks the epoll, IPv6, and KVM fixes.
  Production pins progressed through 6.12.70, .79, .81, .87, .91, .93, and .95,
  but pins do not prove node boot state.
- No configured cumulative kernel livepatch or enabled eBPF mitigation covers
  any of the five requested CVEs.
- Preliminary fix points and stable commits:
  - CVE-2026-23111: 6.12.70,
    `1444ff890b4653add12f734ffeffc173d42862dd`;
  - CVE-2026-46242: 6.12.95,
    `9324de74a3a59b9fde9b62ee45ebaa71458ba2e5`;
  - CVE-2026-53362: 6.12.95,
    `46f201f8b4c39633a1fa3dc12459f506d470993d`;
  - CVE-2026-53359: 6.12.95,
    `2ad3afa40ac6aa340dada122f9abfa46c0a6eb35`;
  - CVE-2026-43499: 6.12.86,
    `6d52dfcb2a5db86e346cf51f8fcf2071b8085166`.
- The configuration worktree checkout hook initially reported missing ambient
  Overcommit gems, then the helper retried and created a clean worktree. This
  is the already documented Nix-shell hook behavior; hooks must be installed
  and run inside `nix develop` before any commit.

## Decisions

- Do not grant the new project SSH/root access to `int.log` or any node.
- Make vpsAdmin the broker for narrowly aggregated security evidence.
- Keep detailed analysis in git and submit only concise bilingual conclusions
  and per-node statuses to vpsAdmin.
- Write public advisory text for VPS operators: attacker prerequisite, root in
  the VPS, host escape/cross-VPS and availability impact, hardening limits,
  plausible monitored kernel failure modes, administrator remediation, and
  whether the user must act. Monitoring is detection, not mitigation.
- Default all submission commands to dry-run. The project token cannot publish
  or send mail; publication stays in a separate human WebUI session.
- Keep the future repository private while it may contain embargoed CVE work.
- Do not create a local `security-advisories` checkout until the canonical SSH
  remote exists.

## Open questions

- How long are production `node_statuses` retained, and do they cover all
  kernel transitions needed for these advisories?
- Should historical central logs be retained only as an operator cross-check,
  or imported once to close gaps before current status history?
- What lifetime should the runtime token use in production: permanent and
  explicitly revocable (recommended for sporadic work), or a fixed renewal
  interval?
- Which vpsAdmin account will own automation-created drafts, and should a human
  edit transfer ownership or merely advance the optimistic lock?

## Cleanup

- Worktrees are active for investigation; nothing has been pushed, merged,
  deployed, or written to production APIs.
- All three project worktrees remain clean.
- No mandatory change review or test suite was run because this phase made no
  code, schema, API, configuration, or deployment changes; it prepared a
  design and clean worktrees only.
