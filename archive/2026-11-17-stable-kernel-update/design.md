# Kernel update process and Linux 6.12.118 design

Owner: architect0. Session: `2026-11-17-stable-kernel-update`.

## Scope and release boundary

Create the maintainer skill/process **in vpsadminos first**, then use it to
port the complete currently packaged downstream stack from Linux 6.12.117 to
6.12.118. Improve the process from demonstrated execution gaps. All rebase
conflicts must be resolved without losing downstream behavior. No deployment,
release-ref promotion or default-branch integration is authorized.

The user explicitly requires a dynamic process: derive the predecessor and its
complete downstream range from current versioned packaging/source and upstream
release history. Do not hardcode patch names, counts, allowlists or this run's
inventory in the reusable skill/runbook. Moving the applicable stable/unstable
selector and verifying its resolved identity is part of the process. This run
moves **stable** only; unstable stays unchanged.

**Sufficient brief ready for lead acceptance:** package P below. Its files,
interfaces, preservation contract, compatibility and checks are settled. K's
replay contract is also settled, but execution follows P so this task really
uses the new process. Exact replay conflicts, upstream absorption and final
Linux head are execution results, not unresolved choices. Registration package
R waits for K's final head and complete correspondence evidence. No existing
unrelated downstream defects are being audited or redesigned.

## Authoritative source and current packaging

Read directly from the canonical bare repositories, with worktrees created by
the lead. vpsadminos initial base/target:
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2` / `origin/staging`.

| Identity | Exact value |
| --- | --- |
| Current stable version | `6.12.117` |
| Packaged Linux head / K initial branch base | `764acbb0ca8c4b60ee5b98f89406b152e992b1d6` |
| Current Linux archive-byte hash | `sha256-50USYq3vBk2bZZAjLplWXmqa3qL/UOm6sGx3v4+xRhw=` |
| Upstream v6.12.117 tag object | `3edfb92cd34f439b2e2878c3544a1683871d29ee` |
| Upstream v6.12.117 peeled commit / old base | `d3417611a3b40b7f04a29e558cebac2bf69889d7` |
| Upstream v6.12.118 tag object | `c246b196b4fd25cf49df43b2803caab5f81df459` |
| Upstream v6.12.118 peeled commit / target base | `b869a5313cbfe7102873d3de318ddb68675146d0` |
| Retained stable ZFS head | `481845fca6ae3f61ca2262c1a5693a58ae364650` |
| Retained ZFS hash | `sha256-/zeZH5EJYa0zaNcbMUoeHp6UnHNAMUrjgok/VgWI88A=` |
| Retained ZFS package patch | `os/packages/zfs/zfs235-free-account.patch` |
| Unstable selector (unchanged) | `6.18.49` |

Upstream identities were confirmed with a fresh `git ls-remote` against
`https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git`, including
peeled tag values. K must fetch the exact release deliberately and verify local
object ancestry and Makefile version before replay. The source tree at the
packaged old head has Makefile version 6.12.117, 50 commits above old base and
no merges. There is no Linux `AGENTS.md` at that head.

The local `origin/vpsadminos-6.12` ref points to 6.12.109 and is not the source
of truth for this update. The latest applicable prior version is selected from
the package catalog and its immutable revision, with the selected role as the
starting context; a branch name, timestamp or arbitrary highest version across
other kernel lines cannot substitute for that relationship. If an explicit
requested predecessor conflicts with packaging, surface that concrete conflict.

Sources/interfaces:

- `os/packages/linux/available-kernels.nix`: role selectors, keyed versions,
  Linux archive revision/hash, per-version config/features and ZFS pairing.
- `os/packages/linux/packages.nix`: selector resolution and kernel/ZFS builders.
- `os/packages/linux/default.nix`: `fetchurl` of GitHub archive bytes, plus
  `bridge_stp_helper` package patch; the 6.12.109-only NFS patch stays scoped.
- `flake.nix`: `lib.kernelVersions`, `lib.vpsadminosSystem`, and generated
  `ci-toplevel-kernel-<version with dots/hyphens changed to underscores>` outputs.
  The CI closure includes kernel dev and builtins-config dev outputs.
- `.github/workflows/kernels.yml`: matrix derives all catalog keys; push trigger
  is staging and PR trigger targets staging. Feature-branch push by itself does
  not start this workflow. Do not create a PR solely to work around this without
  the applicable approval; local intentional builds are supported here.
- `docs/os/patch-series-policy.md`: logical ownership, accurate provenance,
  exact backup refs, version increments for substantive revisions, no fixup/WIP
  residue, complete Markdown accounting. Workspace team and review instructions
  govern orchestration despite its historical single-root wording.

## Reusable workflow contract (package P)

Use a concise router at `skills/update-kernel/SKILL.md`, consistent with the
existing `manage-livepatch` skill, linking one maintained process at
`docs/os/kernel-updates.md`. Add ordinary UI metadata in
`skills/update-kernel/agents/openai.yaml`, an AGENTS routing paragraph, README
maintainer link and MkDocs navigation entry. No new scripts, schemas, registry,
ledger, verifier, scheduler or alternate review system is needed. Shell examples
are parameterized native Git/Nix commands, not this execution's fixed patch list.

The process handles adding and replacing a stable or unstable selection:

1. Establish requested target version, role (stable/unstable), and whether it is
   an additional selectable version or replaces the role's current selection.
   Derive the latest applicable predecessor, its immutable packaged Linux head,
   matching upstream old release, and requested upstream release. Inspect
   package-layer patches, features/config and ZFS pairing too. Capture exact refs
   and a dynamically generated complete old-base..old-head inventory in the
   existing Markdown tracker before any replay. Verify old base is an ancestor,
   resolve merge-shaped histories deliberately, and never infer the stack from
   subject prefixes alone: pristine backports count as well.
2. Preserve the exact old head in a dated backup ref, retain published refs and
   work in an owned isolated topic branch/worktree. Use deliberate fetches and
   network ref discovery; on partial clones, `GIT_NO_LAZY_FETCH=1` makes preflight
   object checks explicit rather than accidentally fetching a huge pack.
3. Rebase the whole range onto the exact new upstream base. A suitable example is
   `git rebase --reapply-cherry-picks --empty=stop --onto "$new_base" "$old_base"`
   from the owned topic branch. Disable or inspect automatic rerere reuse; do
   not let it silently determine the port. Preserve already-empty intentional
   commits or account for them explicitly. A branch with merges needs an
   inspected replay shape rather than blindly applying the linear example.
4. Resolve every conflict semantically: inspect old intent, upstream change,
   surrounding callers and ordering/lifetime/locking rules; preserve upstream
   fixes and downstream behavior together. Never use wholesale ours/theirs,
   skip a patch to avoid a conflict, or treat a clean apply as correctness proof.
   Record affected paths, what collided, resolution rationale and focused checks
   against its old logical owner. Fold caused repairs into that owner and follow
   the policy's patch identity/version/development-history rules. An unchanged
   transplant does not need an artificial version bump.
5. Prove complete old-to-new correspondence with native `git range-diff`, full
   old/new logs and direct patch/tree review. Maintain one Markdown row per old
   logical commit: old SHA, new SHA or exact upstream equivalent, disposition
   (unchanged, adapted, upstreamed), and rationale/evidence. Commit counts and
   patch IDs are useful diagnostics but not semantic proof. Investigate every
   omitted/extra/rerere-resolved/empty/changed row. An upstreamed patch needs exact
   commit/ancestry plus source/effect evidence; only then may its redundant replay
   be omitted. Intentional behavior removal is outside this process's default
   preservation contract and must be raised, not silently classified as upstream.
6. Finish logical history and quick checks, publish the topic Linux head through
   the authorized ordinary feature workflow so its immutable archive is
   retrievable, then compute its **archive-byte** hash (`fetchurl`, not unpacked
   NAR/tree hash). No promotion of Linux maintenance/release refs is implied.
7. Add the target catalog entry by carrying the predecessor's compatible
   configuration/features, all package patches and ZFS pairing unless an examined
   compatibility change is necessary. Set the requested `stableKernelVersion` or
   `unstableKernelVersion` to the target when replacing/promoting that role and
   evaluate its resolved version/revision. An add-only request may leave selectors
   unchanged; state this explicitly. Replacing a selector does not authorize
   deleting the old entry. Pruning/overwriting old version identity requires
   evidence about explicit pins, livepatches, reproducibility and recovery.
8. Verify catalog enumeration, selected and retained package identities, Nix
   source realization, required hooks and docs/skill checks. Review all intended
   commits, including the complete downstream series and correspondence, before
   long product checks. Build/test the exact pinned source and correct profile;
   CI job names or green tests booting another kernel do not prove this update.
9. Record actual results and limits in the existing tracker and tune the process
   only for demonstrated gaps. Separate prepared/published/tested from promoted,
   integrated and deployed. Authorization for source work is not deployment or
   default-branch integration permission.

## Compatibility, deployment and recovery

This is a same-series stable patch update with a preserved downstream ABI/behavior
contract. No database, userspace API, protocol, migration, persistent-state format,
ZFS source or pool-feature change is intended. The port must preserve container
isolation, virtualized proc/sys interfaces and NFS terminal-cancellation safety.
External modules must be rebuilt against the new kernel; kernel build identity
and module directory cannot be reused. Existing livepatch targets remain bound
to their exact kernel identity and are not automatically valid for 6.12.118.

Keep 6.12.117 and every other existing catalog entry unchanged. R adds 6.12.118
and switches only stable. This preserves explicit selections and source recovery;
old OS generations remain the runtime rollback mechanism. A future deployment
would build the exact paired closure first, roll out incrementally and reboot
one node at a time under a separate approved deployment plan. No fleet-wide
coordinated update is needed for an unchanged downstream contract. Kernel-only
mixed versions are supported in intent; runtime evidence and any discovered
cross-version incompatibility must be reported honestly. Do not enable new ZFS
pool features or claim rollback was exercised in this task.

Replay recovery: `git rebase --abort` in the owned worktree returns to the saved
start; the exact backup ref remains available. Preserve uncertain work before
repairing and never reset shared/peer worktrees. Build/test failures block
readiness rather than weakening checks or changing the old version identity.
If the source pin is wrong, repair the one final pin before review; no series of
intermediate repins. No default/ref promotion occurs until separately approved.

## Implementation packages and ownership

Lead accepts allocations and owns shared index/commit windows. Proposed owners
refer to the verified retained roster and have workspace-write access. Each
implementer owns its package through quick checks, commits and review fixes.

| Package / proposed owner | Deliverable / files | Dependencies and acceptance | Evidence / release |
| --- | --- | --- | --- |
| D / architect0 | This `design.md` only; source inventory and verification plan | Exact authority and dynamic preservation contract established | Ready for lead to release P; no app edits or commits |
| P / implementer0 | Skill/router/UI metadata, `docs/os/kernel-updates.md`, routing paragraph in `AGENTS.md`, README link, `mkdocs.yml` entry | This brief; dynamic predecessor/range, add/replace semantics, selector movement, conflict resolution, complete correspondence, package/hash/cache/recovery rules. No hardcoded patch catalog or helper framework | Skill validation, link/example inspection, docs build and required hooks; process usable before K starts |
| K / implementer1 | Owned Linux worktree/dated feature branch; complete rebase and logical patch messages | P accepted and read; target exact commit fetched deliberately, backup created; all old behavior mapped and all conflicts resolved | Old/new bases and heads, dynamically derived full correspondence, conflict rationale, range-diff/tree/quick checks, source publication/archive availability; no maintenance-ref/default promotion |
| R / implementer0 after P | `os/packages/linux/available-kernels.nix`; narrow demonstrated P corrections in its owned files | K final source head plus complete correspondence; add 6.12.118 with preserved ZFS/config and raw archive hash; move stable only; no old entry mutation | Nix identities/source realization, hooks, final OS head; report process exercise and changes. Commit window sequenced with any P fix |
| V / lead-coordinated verification owner | Native build/test/CI results and existing session records, no application changes unless delegated as a diagnosed fix | All intended changes committed, quick checks pass and independent final review complete | Exact derivation/source/input receipts, cache diagnosis, runtime profile and revision proof; findings return to K/R owners |

If K needs a genuine new prerequisite or substantive behavior change, it routes
the decision through lead/architect before expanding scope. Routine technical
clarification can go directly between architect0 and assigned implementers.

## Acceptance and checks

Quick, before final review (expected minutes; stop on concrete failure):

- P: skill-creator `quick_validate.py`, relative-link/metadata checks, `make doc`
  in repository Nix environment, required Overcommit hooks. Inspect parameterized
  examples for real CLI and source interfaces; do not add wording-matching tests.
- K: exact ancestry/version and no merge surprises; inventory covers every old
  commit; `git range-diff old_base..old_head new_base..new_head`; direct changed
  patch/final-tree inspection; `git diff --check`; no conflict markers, fixup/WIP
  residue or unaccounted extra/lost patches. Verify metadata/version/provenance
  of adapted owners. Changed objects may get focused compile diagnostics if
  needed, with longer builds monitored rather than called a quick check.
- R: `nix eval --json .#lib.kernelVersions`; evaluate stable and unstable selectors
  and resolved Linux/ZFS identity through `lib.vpsadminosSystem`/actual package
  path. Confirm 6.12.118 is selected, 6.12.117 remains unchanged, unstable remains
  unchanged and generated `ci-toplevel-kernel-6_12_118` evaluates. Realize the
  fixed-output source only to prove raw archive hash without starting compilation.
  Run relevant Nix formatting/hooks. Do not update unrelated flake inputs.
- Capture final Linux and OS ranges/diff, source pin/hash, old-to-new accounting,
  conflict resolutions, source provenance and no-migrations conclusion for the
  independent reviewer. This is substantive process/config/kernel work.

Longer product checks, after independent review (hours may be required):

- Build the exact pinned target with the existing
  `make OUTPUT=ci-toplevel-kernel-6_12_118 toplevel` path. This covers built-in ZFS
  and cache-required dev outputs. Record Nix inputs, derivations and resulting
  closure. Local compilation is expected for this intentional kernel update when
  the target is not cached; record that reason. Use the existing monitor skill
  and bounded progress reports. Do not start redundant kernel builds.
- Run `./test-runner.sh test osctl/nfs-cancellation` on final OS source. This
  existing test follows stable and asserts both release and Linux revision,
  then tests NFSv3/v4 cancellation, callback lifetime, namespace teardown,
  sibling isolation, restart/admission and repeated stop cycles.
- Discover and run the existing stable-profile `system/boot/stage-2`,
  `kernel/module-autoload`, and `zfs/boot-modes` cases as applicable after checking
  their evaluated guest kernel. Boot modes exercises ZFS built-in/external
  compatibility; reuse exact build products. If a case deliberately pins another
  kernel, do not claim it covers 6.12.118 or silently rewrite the test.
- Select extra focused tests/compile checks only for actual conflict areas or
  failures. Many `kernel/*` customizations and `vpsadminos-selftests` explicitly
  force unstable 6.18; a broad kernel glob is not stable coverage. Do not redesign
  those tests as part of the process task. A full VM suite or full ZFS suite is
  not required merely for its size; final coverage follows actual port risk.
- Observe applicable existing CI on final heads if triggered. The kernel workflow
  automatically enumerates the added version but does not trigger for an ordinary
  feature push. Preserve this distinction and report unrun evidence honestly.

The expected stopping condition is a verified source-preserving port with a
reviewed reusable process and selected/pinned 6.12.118 plus passing applicable
product checks. Build or test overrun requires diagnosis and a narrower next
milestone; it does not justify dropping patches or claiming completion.

## This execution's original patch inventory

Generated with `git log --reverse --format='%H %s' old_base..old_head`;
`git rev-list --count` reports 50 and `--merges` reports none. This list belongs
only to this execution. K supplies final dispositions/new SHAs in the existing
session Markdown evidence; architect can reconcile them here once available.
No target correspondence or conflict-resolution result is claimed yet.

| # | Old commit | Logical patch |
| --- | --- | --- |
| 1 | `3e5a54f0672c5ff95d52993c4f4b14d299d81bf0` | memcg: skip root parent updates during rstat flush v2 |
| 2 | `82297e403d2036b455f4c2dc994423a835dcc047` | sched: include mmu_context.h for task_cpu_possible() v2 |
| 3 | `5efab7ae8e6885183f12f9d2d96ff62be9e5ea99` | [vpsAdminOS] Treat CDDL modules as GPL-compatible v2 |
| 4 | `05b61d005e87f0c21d53cddc284f6687734f1c0d` | [vpsAdminOS] Common functions v3 |
| 5 | `002fd814fdfaa232078fdbcfe1c2009199116316` | [vpsAdminOS] Allow mknod in user namespaces v3 |
| 6 | `d5144f0f349b39e65d9d25fd86ac38a99d154bb8` | [vpsAdminOS] Allow Ceph mounts in user namespaces v2 |
| 7 | `cb230c6957349739e2f9360db856297f2f551dc5` | [vpsAdminOS] Allow NFS mounts in user namespaces v2 |
| 8 | `4e832e7e29a02fa05674bc789bf92d49ca943d61` | [vpsAdminOS] nfsd: continue after unknown export words v2 |
| 9 | `cd19e0d6aefe3039ab76fc4da240b56fcda4e5ac` | [vpsAdminOS] NFS: force soft mounts in containers v2 |
| 10 | `9ed81a1d5a228a39d12c573867890b4c0faf9513` | [vpsAdminOS] SMB: force soft mounts in containers v2 |
| 11 | `8bcb24c31b1db48432e5c4f249d0737d26046c70` | [vpsAdminOS] Allow trusted xattrs in first-level user namespaces v2 |
| 12 | `0174c680e26babf1c5db16bdc62be96a58751280` | [vpsAdminOS] Ignore sync() from non-init user namespaces v2 |
| 13 | `802109c7a2767a2ee858a9c3911198dcf17bd2bb` | [vpsAdminOS] fork: let container root bypass RLIMIT_NPROC v2 |
| 14 | `7c3081b7c795b9e18f52df5b8906f296dd481f16` | [vpsAdminOS] proc: allow container OOM score floor updates v2 |
| 15 | `ba8d5482aa1bee1689025ce454c582c8cd7b9566` | [vpsAdminOS] Protect container init and lxc-start from OOM v2 |
| 16 | `d18afd1d95067a440d04fe9e263328a83da50a26` | [vpsAdminOS] vmstat: virtualize oom_kill for containers v3 |
| 17 | `4cd22bd91cdb20ef37f6515d719574734b61d60e` | [vpsAdminOS] memcg: kill allocating task as OOM fallback v4 |
| 18 | `c1c6e00524e5db2ca52e39262fecfd34f145755f` | [vpsAdminOS] netfilter: isolate conntrack sysctl storage v2 |
| 19 | `0a9bf91d91238dfb3aa545d017b8286cf748b3bc` | [vpsAdminOS] taskstats: allow user-namespace administration v2 |
| 20 | `ab3d74408297143884b1f55afd9ef550a712ab3f` | [vpsAdminOS] dump_stack: print memcg path v3 |
| 21 | `20133b5c8beb7b39d80dc7e2c2818692b8b8a1f5` | [vpsAdminOS] Silence module lists in diagnostics v2 |
| 22 | `38f4d1530b026a10f552b08352e541bc797b6c86` | [vpsAdminOS] Virtualize module parameters v2 |
| 23 | `93b74b767b800d6193251c19db1ccfc04738d319` | [vpsAdminOS] IPVS: allow user-namespace administration v2 |
| 24 | `a82a0174bc0671d4ab77e067fbb86e14df101640` | [vpsAdminOS] Allow container admin to renice tasks v3 |
| 25 | `99de4472d8189d311ee6ada4b440abd64d4d2df7` | [vpsAdminOS] procfs: hide uid_map from Docker v3 |
| 26 | `d91a8efe6d62e8f95c02903f0677928e94f18e54` | [vpsAdminOS] sysctl: virtualize vm.swappiness v2 |
| 27 | `eea799b303f5308c398896d40b69b1619c607ab2` | [vpsAdminOS] Allow NFS server mounts in user namespaces v2 |
| 28 | `b2645b594e6fe7844c00b282f7947f21714b4027` | [vpsAdminOS] Map ping_group_range sentinel to container GID v7 |
| 29 | `57c08d059697ba740923b3c2dbab2de7463e0ff9` | [vpsAdminOS] tmpfs: size defaults from memcg limit v4 |
| 30 | `9102ae0d8b574724dc24ae6c5433f956b9361a5e` | [vpsAdminOS] tmpfs: show IDs in the current user namespace v2 |
| 31 | `23c7f07516b2302970ef8f370df1b3c9160c8442` | [vpsAdminOS] memcg: skip slab reclaim when kmem is disabled v2 |
| 32 | `93fdd27d765f41a5080ee3192ef1eaf9cfcb99bb` | [vpsAdminOS] Cache /proc/cpuinfo output v2 |
| 33 | `90827283b536264a5865ee67082daa69c9875b0f` | [vpsAdminOS] proc: allow first-level root to read task stacks v2 |
| 34 | `05797039c77bad208dfbde132fc71dff021f88b5` | [vpsAdminOS] Honor immutable capability in first-level userns v2 |
| 35 | `657977908b2fb9f7976f451554c8994436e282fc` | [vpsAdminOS] syslog_ns: v23 |
| 36 | `0dbe29eee0ec03632ca03453958db6d434bdca53` | [vpsAdminOS] Limit visible CPUs for containers v20 |
| 37 | `ef969339798fd90eba22f0186d469524e5b05c3c` | [vpsAdminOS] Create /sys/fs/vpsadminos v2 |
| 38 | `22614c48017b882d222d5ff67d2d0636114f8c23` | [vpsAdminOS] Hide slabinfo outside the initial user namespace v2 |
| 39 | `8176f94a65e00301d0d1eb66ae341d08f7d94733` | [vpsAdminOS] Hide diskstats outside the initial user namespace v2 |
| 40 | `4e710587c301b6ee4a1c36e270decbebd5a8d0b8` | [vpsAdminOS] Add configurable no-reclaim kvmalloc mode v2 |
| 41 | `9c2e5c52772086d057825f3f80a066337c1c276c` | [vpsAdminOS] Reduce BPF time precision in user namespaces v2 |
| 42 | `a82668abba10764e043cb938daf21775f7cd70a8` | [vpsAdminOS] Expose IPsec sysctls in first-level userns v2 |
| 43 | `5fb54ae2dd75d0308c9ecefad17bdb8b7624c457` | [vpsAdminOS] Virtualize meminfo and swaps v6 |
| 44 | `28d178a9995d6919eeed7d58127a06b4bb0344ba` | [vpsAdminOS] Virtualize loadavg v20 |
| 45 | `274f0a3c23a26746cb9f52aeac0e0b95a7088fc6` | mm: memcg: protect reclaim iterator ancestor walk v2 |
| 46 | `2dfe7e7bd04c643df28360e11d402ecf169f057f` | [vpsAdminOS] NFS: tolerate a cold NLM client during sysfs shutdown v2 |
| 47 | `79efe5a11ae82179f84a351c603434df866ac97b` | NFS: Use nlmclnt_shutdown_rpc_clnt() to safely shut down NLM |
| 48 | `5e383c2411cbd1b22ec0073ad4639a628b48de02` | lockd: stop retrying NLM CANCEL after client shutdown |
| 49 | `02beaa9040c47f489991bac14c0bdc00b7a737c9` | NFS: drain server sysfs before releasing client state v2 |
| 50 | `764acbb0ca8c4b60ee5b98f89406b152e992b1d6` | [vpsAdminOS] NFS: port namespace tree cancellation to 6.12.117 v3 |

## Investigation completion and observed limits

The design package is ready for lead acceptance. P can proceed immediately;
K follows the accepted process and deliberate target fetch. With lazy fetching
disabled, the target object is still absent locally, so no target-source replay
or conflict outcome has been claimed by D. A missing-object `cat-file` earlier
triggered Git's promisor auto-fetch; its exact process tree was terminated and
confirmed gone. No explicit ref was changed. Use bounded deliberate acquisition
for K, and preserve any resulting repository temporary state for its owner to
inspect rather than cleaning a shared object store.

Source inspection confirms `zfs/boot-modes` and `kernel/module-autoload` use normal
kernel selection; `system/boot/stage-2` likewise has no explicit kernel override.
The boot-modes test checks the selected module-provider path and actual release,
then verifies payloads through snapshot, clone, rollback and send/receive in both
built-in and external ZFS packaging modes. Final evaluated guest/source identity
is still required when running them. These are test selections, not test results.

Only this design file was intentionally written by architect0. Lead owns state,
portal updates and tracking commits. No application source edits, kernel rebase,
product builds, deployment or integration were performed by this package.

## D3: uniform Linux publication instructions

Sufficient brief, architect0; supersedes earlier wording that leaves the final
Linux delivery endpoint as an unspecified topic publication or default merge.
Lead reports the user's explicit acceptance (“yup”) of version branches,
`vpsadminos-<upstream-version>`, branches only, and exact-SHA OS pins. For this
run the accepted endpoint is `refs/heads/vpsadminos-6.12.118` at
`3bba27296b6f4f4a2b1568d65cea6037368f229b`. No Linux merge is intended.
This section is instruction design; it performs no publication or lifecycle action.

### Settled contract

- Linux is a publication-only downstream source repository for these kernel
  ports. Final delivery is a reviewed/verified exact head published on
  `vpsadminos-<upstream-version>`; do not merge it into Linux master or another
  default branch. A dated preparation branch is optional and may supply the
  archive during verification. Retain it and backup refs under existing rules.
- Do not create downstream release tags automatically. Reading/verifying
  authoritative upstream release tags remains required and is unaffected.
- Keep the catalog pinned to the full immutable Linux commit and archive-byte
  hash, never the moving branch name. Publication evidence records exact remote,
  full version-branch ref, fresh remote head equality, final tested Linux SHA,
  and the consuming OS catalog revision/hash. Preserve existing range/correspondence,
  review and build receipts; add no ledger or evidence schema.
- If the version branch already has the desired exact head, publication is
  already satisfied. If it points elsewhere, preserve it and inspect the reason;
  do not force-update or repoint it merely to finish the task. For an intentional
  later stack revision on the same upstream version, the existing `-2`, `-3`
  branch convention is sufficient when needed, after checking current refs.
  No new revision-numbering framework is needed for this first publication.
- Do not update a generic series alias such as `vpsadminos-6.12` without direction.
  Exact packaged-source predecessor discovery remains authoritative.
- Final version-branch publication follows the existing patch policy's review
  and exact-head validation gates. Topic publication before builds is distinct
  from declaring the version ready. OS integration and all other repositories
  retain their explicit approval, final-head review/check and merge obligations.

### Why a workspace exception is needed

Repository guidance is sufficient to define branch naming, but not to reconcile
workspace completion requirements: workspace `AGENTS.md` and
`docs/agent-instructions/sessions.md` currently require **every** registered head
to be merged into its remote default. Leaving them unchanged would recreate the
Linux-merge demand even with an explicit repository runbook. Make one narrowly
scoped Linux publication exception authoritative in the workspace Git procedure,
with short cross-references at the two contradictory completion statements.
Do not generalize it to ZFS, LXC or arbitrary feature repositories.

The exception substitutes fresh exact-head version-branch publication proof for
Linux's default-merge delivery condition. It does not equate “published” with
“merged”, waive other unfinished work, or authorize session closure. Preserve
ordinary exact-final-head completion rules for every other registered repository.
If the installed runtime or a retained recovery contract cannot represent this
publication endpoint, report that limitation and leave lifecycle state unchanged;
do not alter metadata, registrations, runtime code, private helpers or recovery
contracts to make it pass. Documentation approval does not authorize such changes.

### Files, owner and acceptance

Owner proposed: implementer0 (parked M), subject to lead release. One small
instruction package, with separate repository commit windows:

| Repository / files | Minimal change | Checks and evidence |
| --- | --- | --- |
| vpsadminos `docs/os/kernel-updates.md` | Replace generic publication paragraph and final action distinction with the settled Linux endpoint, exact-ref proof and preserved recovery contract | Link/example review; no hardcoded patch inventory; preserve full replay/selector/hash/verification process |
| vpsadminos `skills/update-kernel/SKILL.md`, `AGENTS.md` kernel routing paragraph | One concise publication-only/version-branch statement and runbook link; remove implication Linux default merge is a later required step | Skill validation; consistent ordinary OS integration boundary; docs build and existing hooks |
| workspace `docs/agent-instructions/git.md` | One small “Linux kernel source publication” exception linking the repository process; define exact remote-head proof instead of Linux default merge | Check scope remains Linux only and review/exact-head/recovery rules remain intact |
| workspace `AGENTS.md`, `docs/agent-instructions/sessions.md` | Qualify their universal default-merge completion wording with a link to that single exception; preserve all other lifecycle requirements | Cross-reference/contradiction inspection and workspace hooks; no runtime/schema changes |

No README, MkDocs navigation, project map, Linux source or packaging pin change
is necessary for D3. Existing links already discover the runbook. Workspace
instruction changes are feature work in an owned workspace worktree, not a
tracking-only shared-master exception. Lead owns workspace scope/setup and any
separate integration approval; repository instruction editing does not grant it.

### Dependency order and handoff

1. Lead accepts this narrow six-file/two-repository brief and releases M. The
   accepted source/ref policy is already settled; no further kernel audit needed.
2. Implementer edits the three OS files on the prepared OS branch and the three
   workspace files on an owned workspace feature branch, preserving unrelated
   work. Lead handles required prose; implementer runs checks/commits. Give final
   independent review the instruction diffs and previous review/test lineage.
3. Authorized source publication creates the absent version branch at the already
   verified Linux SHA and checks it freshly with `ls-remote`. It changes no source
   bytes or archive hash and requires no new kernel build solely for the ref name.
4. Update existing evidence with that publication receipt. Integrate OS only under
   its existing approval and fresh final checks; workspace default integration has
   its own approval/claim workflow. No lifecycle action is part of this brief.

The prepared OS head is `ba6837de511ef9364fa4126e24c91de0251f33ad`, rebased onto
staging `42baba6117bebcde3d04555a71377381df197925`; lead reports `=` equivalence
to original reviewed/tested `ba7e99b5e3d435826bd387e64f1c1a6ec173169c`. D3 adds
instruction changes requiring their affected review/checks, not a new Linux port.

## D4: update the three configuration channel roles

Sufficient bounded brief, architect0. User requested updating vpsAdminOS in
`staging`, `os-staging` and `production`, then explicitly “and merge it”. Lead
records that authorization for configuration `master`; no deployment is included.
One implementer package, proposed owner implementer0, follows the separate hook
setup owner's successful environment handoff. No kernel source re-audit required.

Configuration worktree: `worktrees/2026-11-17-stable-kernel-update/vpsfree-cz-configuration`,
initial base `9c6a0313d1689099c1dfcb065171a4aead44f183`. Only expected tracked
file change is `flake.lock`. No `flake.nix`, host/module, channel-map, deployment
receipt or per-release documentation changes.

### Exact role mapping and target

Read from current configuration `flake.nix` and `flake.lock`:

| Channel / role | Root input | Old vpsAdminOS SHA | Preserved Nixpkgs follow |
| --- | --- | --- | --- |
| `staging/vpsadminos` | `vpsadminosStaging` | `a7d71a54a15496976cb0fccebb8a1b589f24f5e2` | `nixpkgsStaging` |
| `os-staging/vpsadminos` | `vpsadminosOsStaging` | `a7d71a54a15496976cb0fccebb8a1b589f24f5e2` | `nixpkgsStable` |
| `production/vpsadminos` | `vpsadminosProduction` | `e643cbef6c94fc8e7d7331f5e91b9d5dc6812a79` | `nixpkgsProduction` |

All three target the published vpsAdminOS source
`f33f5fd10b53232b5670862f832f4ec5ea835e84`. Fresh read-only SSH `ls-remote`
confirmed both upstream HEAD and `refs/heads/staging` equal that SHA. Their
original input URLs use the upstream default, so normal `channel update` resolves
it; an unmerged feature `channel set` is inappropriate here. Recheck if upstream
moves during execution and report an unexpected target before publishing it.

The new source selects stable kernel 6.12.118 at Linux
`3bba27296b6f4f4a2b1568d65cea6037368f229b`. It includes the already-integrated
packaged-gem update `42baba6117bebcde3d04555a71377381df197925` as well as the
kernel/process commits. Production additionally spans upstream Nixpkgs-lock
commit `a7d71a54`; configuration's explicit follows keep its own Nixpkgs pin
unchanged. Preserve and report the actual generated upstream changelog; do not
misdescribe this as fetching only one kernel commit.

### Preservation and transitive graph

The three inputs retain their distinct `nixpkgs` follows above and the common
`nixpkgsUnstable` follow. Preserve all top-level Nixpkgs, vpsAdmin, runtime,
confctl and other input revisions/identities. Preserve existing aliases and
channel selections. `vpsadminStaging` and `vpsadminServices` already follow
`vpsadminosStaging`, and `vpsadminProduction` follows `vpsadminosProduction`;
their consumed OS source advances through those aliases without changing their
own vpsAdmin revisions.

Direct graph comparison against the target OS lock found the currently selected
`impermanence`, its `home-manager` and `nixpkgs` children, `netlinkrb` and
`ruby-lxc` locked identities identical for all three channels. No transitive
revision change is expected. Generated node renaming alone is not an input
change; compare logical paths, follows and locked identities. Unexpected content
or follows changes need diagnosis, not manual lock editing or blanket acceptance.
No persistent-state migration or runtime activation occurs from this pin commit.
Rollback preparation is the prior exact lock/configuration commit; any actual
node rollback retains its ordinary deployment and compatibility requirements.

### Execution, checks and evidence

After hook setup is accepted and the owned checkout is ready, enter the pinned
repository Nix environment. Its README supports grouped role updates; the pinned
confctl `ff5e017780a35fb97b549db2a51b570193867c3b` resolves the channel selector to
three distinct inputs and invokes one updater/commit operation:

```sh
confctl inputs channel ls '{staging,os-staging,production}'
confctl inputs channel update --commit '{staging,os-staging,production}' vpsadminos
```

Keep changelog enabled and its generated message intact. One grouped generated
commit is the smallest conventional result; do not manufacture three identical
history streams. `--forward-only` is optional when deliberately using its guarded
workflow and existing mirror/tooling prerequisites; it is not a reason to add a
new setup project. Never omit the `vpsadminos` role (that would select unrelated
channel roles), use `--no-changelog`, hand-edit the lock, bypass hooks or fall back
to a direct whole-flake update. If a commit hook fails after installing a candidate,
inspect the actual lock/index/HEAD before retrying; reconcile effects instead of
rerunning blindly.

Quick acceptance, before lead's ordinary final-review/merge decision:

1. All three full locked revisions equal the target and share its correct source
   identity/hash. Fresh channel listing and `confctl inputs ls --json` establish
   actual mappings; direct complete lock comparison proves unrelated inputs,
   follows and reachable dependency identities unchanged.
2. Evaluate `.confctl.channels` via `nix eval --json .#confctl.channels` and the
   normal machine metadata/build-plan outputs as needed (`confctl ls` evaluates
   inventory without building systems). Verify the selected inputs still map to
   the requested roles; no channel or machine-selection change is intended.
3. Evaluate each selected source's `lib.availableKernels`: stable 6.12.118,
   expected full Linux revision/archive hash, preserved unstable/older entries.
   For example, use the configuration flake's
   `inputs.vpsadminosStaging.lib.availableKernels` and the corresponding two
   inputs through `builtins.getFlake`; do not substitute an ambient checkout.
   Confirm each effective Nixpkgs follow still resolves to its old configuration
   pin. These are pin/evaluation checks, not proof of a built or booted fleet.
4. Required hooks pass; `git diff --check` and complete base-to-head diff contain
   only the intended lock update. No new tests, broad fleet build or activation
   is necessary for this routine pin-only package. A real evaluation error gets
   a focused diagnosis rather than an unrelated pin refresh.
5. Report exact configuration base/head, generated commit/changelog, old/new
   logical input graph and checks in existing session Markdown. Retain the OS
   original-source passing CI and the separately observed post-integration run
   as scoped evidence; do not claim an active run has passed or start a duplicate
   observer/build. Apply the mandatory-review skill's mechanical-update criteria
   honestly; its whole-history/no-migrations conclusion remains required.

Lead owns final approval scope, review decision, fresh remote-target comparison
and authorized fast-forward master integration with ordinary hooks/claim/push
verification. Complete all preparation outside the repository claim. No machine
reservation, deployment, runtime mutation or session lifecycle action is needed.
Routine channel updates need no configuration documentation commit; all execution
evidence remains in this session. D4 performed read-only source/ref inspection
and edited only this design file.
