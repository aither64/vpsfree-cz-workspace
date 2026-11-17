# Final committed-deliverable review packet

## Requested outcome

Create the kernel update skill/process in vpsadminos, then use it to add
6.12.118 carrying every patch above packaged 6.12.117, resolve all conflicts,
tune demonstrated process gaps. User explicitly requires dynamic patch discovery
(no fixed patch list), complete verification and stable/unstable selector movement.
Actual run changes stable only, retains old entry and unstable selection.

## Scope and authority

[Plan](plan.md), [state](state.md), architect-owned [design](design.md),
[Linux port evidence](linux-port.md). No merge/default-ref promotion, deployment,
livepatch qualification, ZFS feature upgrade or unrelated stack redesign authorized.

Risk high: host kernel/container isolation, mixed-version and rollback behavior.
Retained independent reviewer0: gpt-6.1-sol/xhigh, read_only, selected from verified
same-session roster. General, architecture/repetition, scope/proportionality and
risk/compatibility lanes apply. Read mandatory-change-review skill and all four
lane references. Preserve reviewer settings; perform review directly, read-only.

## Repositories and final ranges

- vpsadminos: own worktrees/2026-11-17-stable-kernel-update/vpsadminos;
  initial base a7d71a54a15496976cb0fccebb8a1b589f24f5e2, target staging.
  Process commit initially 46cd1215337a36fbab5b796a956a6cd096ef3384, folded
  demonstrated recovery correction into 435d83468d7a3089eeb45f171d0ab244748f43b4
  (final process owner; no obsolete follow-up retained).
  Catalog commit/final head 5a59f3059ca6ada368deeeeca6dba5034468be93.
  Complete OS series: 435d83468d7a3089eeb45f171d0ab244748f43b4 process,
  5a59f3059ca6ada368deeeeca6dba5034468be93 stable catalog.
  Final diff: 7 files, +324/-1 (process/navigation + new catalog entry/selector).
  Fresh origin/staging equals original base; ancestry verified, no rebase.
- linux: own worktrees/2026-11-17-stable-kernel-update/linux; old packaged head
  764acbb0ca8c4b60ee5b98f89406b152e992b1d6 on upstream
  d3417611a3b40b7f04a29e558cebac2bf69889d7. New upstream
  b869a5313cbfe7102873d3de318ddb68675146d0; final downstream head
  3bba27296b6f4f4a2b1568d65cea6037368f229b (published topic verified).
  Full 50-row old/new correspondence and native source/tree checks are in K evidence.
  No Linux default/maintenance integration approved. Topic source is published;
  master/maintenance refs retained at their original values.
  Review complete old/new downstream series, range-diff, upstream transition and
  final tree. Authoritative upstream changes are mechanical release input;
  preservation correspondence and any adaptations require direct source review.

No database migrations, released/transitional schema paths or intentional
behavior removals are intended. Whole-branch history, migration, repeated-pin
stream consolidation conclusions must be explicit; validate this against actual
final ranges. One final Linux pin and catalog update, separate process commit.

## Documentation routing and fidelity

- Maintainer kernel updates, reusable operations: docs/os/kernel-updates.md,
  reached from README and MkDocs; native Git/Nix examples and preservation,
  hash, selector, compatibility/recovery contract. [P evidence](process-evidence.md): skill/metadata/links/shell syntax, actual
  role/CI-output evaluation, make doc and ordinary commit hooks pass.
- Coding agent discovery: skills/update-kernel/SKILL.md and agents/openai.yaml,
  AGENTS routing. Dynamic source range and single authoritative process.
- Existing downstream patch ownership/version/provenance:
  docs/os/patch-series-policy.md; checked, unchanged.
- Individual port inventory/resolutions/check results: this session's
  linux-port.md and state; no fixed inventory in reusable project process.

Context-owning lead applied vpsfree-user-facing-writing directly after technical
facts settled; commands/identifiers retained. Confirm documentation placement,
link reachability, executable examples and preservation explicitly in review.

## Evidence before review and remaining validation

Quick commands/results, exact pins/hashes, complete series/diffstats and actual
conflict dispositions are in the final K/R evidence and ranges below. All intended changes
must be committed and quick checks pass before review starts. Long exact-target
build and focused stable VM checks follow final review. No runtime/deployment
success is claimed at this preparation stage.

## Execution learning to verify in final process

Partial clones require deliberate acquisition and availability checks for replay
objects as well as upstream commit/Makefile identity. K encountered absent
promised objects at owner 20 after 19 clean replays, safely interrupted the exact
command and retained its rebase state. Successful command-local promisor classification remedy and exact interrupted
replay reconciliation are in K evidence; P correction folded into its logical
commit. All 50 patches finally verified equal with no omissions/adaptations.

## Linux complete branch/history inventory

Full final downstream series is obtained natively from the exact new-base..head
range; the correspondence table links all 50 old and new commits. Final diff is
that range's native Git diff (113 downstream paths). The upstream transition is
680 authoritative stable commits; review the product's new-base downstream
series and old/new correspondence in addition to the OS base-to-head series.
All 50 preserved messages/authorship/path-status deltas match. No obsolete branch
approach, repair/fixup residue, repeated input stream or migrations in Linux.
Final tree 944e5a57917938df529d6eebb3e30eba40e4afef equals native three-way
merge-tree of full old downstream and new upstream against exact old base.
Seven overlapping paths were directly inspected by owner; independent reviewer
should assess preservation and limits rather than rely on equal counts alone.
No source compilation/runtime qualification has occurred before final review.

## Authoritative final Linux commit series

This is the complete new-base..head list (exact old/new mapping is in K evidence):

```text
5f080b7bee110d6aab945bfb65331b2549047386 memcg: skip root parent updates during rstat flush v2
f7a01466a953b5c7e140019405b0091fb4625c87 sched: include mmu_context.h for task_cpu_possible() v2
ac8e87592de403b0acc37127bd1816a707e44683 [vpsAdminOS] Treat CDDL modules as GPL-compatible v2
6e7f40f3bbf5606592af7560be736205694f3b69 [vpsAdminOS] Common functions v3
0d7f6d7cefc9db13e2c2dfd9e37c11d5e2f01356 [vpsAdminOS] Allow mknod in user namespaces v3
ef467b5e173a641a66fd7c710bd991223f8490ef [vpsAdminOS] Allow Ceph mounts in user namespaces v2
0f8044674ecc9d2822097decc7468ab2c0f5e2f9 [vpsAdminOS] Allow NFS mounts in user namespaces v2
d2355bc89099b2bce9561d57356f94b9425de0ab [vpsAdminOS] nfsd: continue after unknown export words v2
780a664ed03a11afe0de49be951db3d3730121fd [vpsAdminOS] NFS: force soft mounts in containers v2
0fd551e37adaadd8d6f6169e5c2d9195f0706bc2 [vpsAdminOS] SMB: force soft mounts in containers v2
16c0e92435afa3664b9ceed4841dd631dd5dd70d [vpsAdminOS] Allow trusted xattrs in first-level user namespaces v2
0c674741b67626cbdbd2acfafa3dd6c9305b75e7 [vpsAdminOS] Ignore sync() from non-init user namespaces v2
8bd4d3983a00cc2031de872b1385b1f1d6df3ff7 [vpsAdminOS] fork: let container root bypass RLIMIT_NPROC v2
9485ae50424c15dfd4ff217ea6950585958f4ec3 [vpsAdminOS] proc: allow container OOM score floor updates v2
c67899aa152fe4edeeef70da98caf9268d6c5fff [vpsAdminOS] Protect container init and lxc-start from OOM v2
af5c2c40ed53e9a7c8c5ec497efb3910ff00ff68 [vpsAdminOS] vmstat: virtualize oom_kill for containers v3
372a9b2a4b7e74b47d7c5e1168fee6fc59f3247e [vpsAdminOS] memcg: kill allocating task as OOM fallback v4
8f7916f7e4cf526e55e91ed24f1046d158315c98 [vpsAdminOS] netfilter: isolate conntrack sysctl storage v2
07c1b2ef830616bd7ffc32a6f8156623f4c47b7a [vpsAdminOS] taskstats: allow user-namespace administration v2
ffda621248096628e7a2ddf58bb632b85536abc9 [vpsAdminOS] dump_stack: print memcg path v3
40130614ed0589bb5cf273043d58865e9cb1fb23 [vpsAdminOS] Silence module lists in diagnostics v2
3f23248e13814872fbf8e0c88ffbb64cd7e15a56 [vpsAdminOS] Virtualize module parameters v2
5f033fc8e921c1d1ab1f839797f36f6c4d9c8a96 [vpsAdminOS] IPVS: allow user-namespace administration v2
71e607b05441f3bd4e9c29fb437303bf95bcb341 [vpsAdminOS] Allow container admin to renice tasks v3
25c8debcb7defc6ddea69d911ba64859de1f588d [vpsAdminOS] procfs: hide uid_map from Docker v3
e07e5e3429e42ed472fd84fea9341fe730ee4d8e [vpsAdminOS] sysctl: virtualize vm.swappiness v2
043be1a4e6a5db09db24d23548478b0b18288bf8 [vpsAdminOS] Allow NFS server mounts in user namespaces v2
3040962882c0bf79ff6530949861e391026577c6 [vpsAdminOS] Map ping_group_range sentinel to container GID v7
e716c3af2ed2428b6f3fadd17fa9af2b090fef86 [vpsAdminOS] tmpfs: size defaults from memcg limit v4
4043312ea3e3c1fcabc76bb0e8135ec0a8e3a0e6 [vpsAdminOS] tmpfs: show IDs in the current user namespace v2
109befbd4e01ce3b826b7ebdab7c20ee5111f731 [vpsAdminOS] memcg: skip slab reclaim when kmem is disabled v2
591e202d529f227721edf00cf1c9d68b18863cfb [vpsAdminOS] Cache /proc/cpuinfo output v2
075f9c0e950d21f31fce89bce5b09c51d42333fe [vpsAdminOS] proc: allow first-level root to read task stacks v2
365f64c9bee03e90a401cd66b75765f55ec96321 [vpsAdminOS] Honor immutable capability in first-level userns v2
620355cacc76691afe84abbba0a09b58132f0341 [vpsAdminOS] syslog_ns: v23
fca3ce37aa081fcd75261f4624ed68e03f87c4d5 [vpsAdminOS] Limit visible CPUs for containers v20
74401186b85b5f0693e2b6550e1b7e80c6f6a5ce [vpsAdminOS] Create /sys/fs/vpsadminos v2
64ad42c9eb28f799d722971deffe556c94f9ea08 [vpsAdminOS] Hide slabinfo outside the initial user namespace v2
030eb5b9cdb209a3245634d600bd59a764ad00c4 [vpsAdminOS] Hide diskstats outside the initial user namespace v2
2c300d9249a680e8b8d411cc9f945b6cad45ff80 [vpsAdminOS] Add configurable no-reclaim kvmalloc mode v2
6c90b3ce59022436d0084a0964605183c60c562b [vpsAdminOS] Reduce BPF time precision in user namespaces v2
fc22ae5fbafd09722a723e6f258d0c6c33c87002 [vpsAdminOS] Expose IPsec sysctls in first-level userns v2
3ad5c50bc03d76ff5edac830256bb32bc274c4e8 [vpsAdminOS] Virtualize meminfo and swaps v6
91d1dcc40dddd54ccb572fc9a69bcaa4f6968839 [vpsAdminOS] Virtualize loadavg v20
cb41a34072ca1433640fd72906d573a6be8c9468 mm: memcg: protect reclaim iterator ancestor walk v2
179bc48e7d9d23dcc8b1b8a776e28df75fdaf904 [vpsAdminOS] NFS: tolerate a cold NLM client during sysfs shutdown v2
b82822cf9c89c0c480e05fd8899bcee3d89ec825 NFS: Use nlmclnt_shutdown_rpc_clnt() to safely shut down NLM
30debdf77eff185338e2f91661af661b578b6970 lockd: stop retrying NLM CANCEL after client shutdown
c1a4905a610d408150cb1f4a6d5ff34f4bbcc1f2 NFS: drain server sysfs before releasing client state v2
3bba27296b6f4f4a2b1568d65cea6037368f229b [vpsAdminOS] NFS: port namespace tree cancellation to 6.12.117 v3
```

Final Linux diff is available directly with `git diff
b869a5313cbfe7102873d3de318ddb68675146d0..3bba27296b6f4f4a2b1568d65cea6037368f229b`
in the Linux worktree. Native range-diff compares against old
`d3417611a3b40b7f04a29e558cebac2bf69889d7..764acbb0ca8c4b60ee5b98f89406b152e992b1d6`.
For partial-clone Git inspections use `GIT_NO_LAZY_FETCH=1`; K's evidence gives
command-local promisor overrides if required. Never alter stored shared config.

Archive bytes (R's single watcher exit0):
`sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=`,
`/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz`.
Actual package-source realization/role evaluations and final OS head are complete in
catalog-evidence.md and the final R receipt below.

## OS final history and quick results

`git diff a7d71a54a15496976cb0fccebb8a1b589f24f5e2..5a59f3059ca6ada368deeeeca6dba5034468be93`
is the complete final OS diff. Two logical commits only; process fix folded into
owner, one final source pin/catalog update, no superseded intermediate pin or
branch fix. No database migrations or externally consumed transitional schema.
Source-only realization returned the prefetched archive exit0. R reports all
eight retained entries semantically unchanged, unstable unchanged, both stable
ZFS packaging modes and patches match predecessor. Nixfmt/diff check and ordinary
commit hooks pass. Exact clean-head derivation/source receipt is complete in catalog evidence. All source work is committed; no long product check started.

R final receipt: all intended changes committed/clean, quick checks pass. Fresh
SSH origin/staging a7d71a54a15496976cb0fccebb8a1b589f24f5e2 unchanged.
Committed CI output `/nix/store/smzzgsm45k9qiir8sv7wwfrn8z4f4174-vpsadminos-system-vpsadminos-26.05.git.5a59f30.drv`.
Full unchanged source/input graph and exact source/package identities in
[catalog evidence](catalog-evidence.md). Review is now released; no long check
or OS publication started. Linux topic publication was needed for archive.

## Independent review completed

Report [review.md](review.md) concludes pass with one Advisory, no Blocking or
Important issues; explicit history/migration/repeated-stream/docs/compatibility
conclusions included. A1 is a narrow partial-clone export clarification; lead
chose to fix it in P before publication, preserving Linux/catalog source. Original
reviewed range above remains authoritative; final refreshed doc heads/equivalence
and focused verification will be appended after owner completion. No full review
rerun needed under narrow-fix rule if that remains the only change.

## Final A1 remediation and history equivalence

Reviewed OS base..5a59f3059ca6ada368deeeeca6dba5034468be93 refreshed to same
base..ba7e99b5e3d435826bd387e64f1c1a6ec173169c. Final process owner
18f820a1df8fc473a496f13f7e1d32ca75151bf1; catalog ba7e99b5. Lead native
range-diff confirms only requested owned-shell export clarification in process,
catalog `=`. Head tree diff only runbook +11/-4; source/catalog/inputs unchanged.
Focused skill/docs/link/shell/hook checks pass. A1 fixed and directly accepted
under narrow-fix rule; original independent review retained, no new design or
full rerun. No migrations/repeated pin stream/obsolete history introduced.

## D3 affected instruction review packet (preparation)

User clarified Linux is never merged anywhere, approved branch naming
`vpsadminos-<upstream-version>` and no automatic downstream tags. Named
vpsadminos-6.12.118 is freshly published exact3bba2729 (linux-port.md).
This adds substantive documentation/instruction scope, not a new kernel port.

OS baseline advanced froma7d71a54 to42baba6117bebcde3d04555a71377381df197925
(one disjoint exporter Puma dependency update). Clean rebase was proven with two
equal ordered stable patch IDs and native range-diff; complete kernel/ZFS
derivations/source/config/input graphs and test sources unchanged. Full old
OS CI does not claim testing the new exporter-composed closure. Evidence in
verification.md records exact old/new ranges and reuse limits.

Final D3 OS range42baba..f33f5fd10b53232b5670862f832f4ec5ea835e84, two logical
commits:2352449568afa3b2f5bd500dba3fbed1c1163e0b process, f33f5fd catalog.
Compared with rebased equivalent ba6837de, only three docs/skill/AGENTS files
change (+45/-14); catalog patch remains'='. No source/hash/ZFS/flake changes,
no migrations/intermediate pins/fixes. Quick skill/docs/links/shell/hooks pass.
Exact new OS drv6a560v0f442rchkda1024cvsjnliswdn differs by revision, kernel3slqrm
and ZFSx4468 inputs retained. No full kernel re-audit/retest required for prose.

Workspace instruction feature at worktrees/<slug>/workspace contains only
AGENTS.md, docs/agent-instructions/git.md, docs/agent-instructions/sessions.md.
Final head/check packet pending owner. One narrow Linux-only source-publication
exception, short completion crossrefs, no runtime/schema/ledger/helpers/manifest
changes. If installed/retained contracts cannot express endpoint, leave lifecycle
unchanged rather than bypass. Canonical OS runbook link uses staging branch.

Lead direct writing passes complete on both; exact immutable OS SHA/hash pins,
existing-ref collision behavior, no default/series merge, no automatic tags,
upstream tag discovery preserved. Other repositories' approval/merge requirements
unchanged. Source publication receipt already accepted; no new Linux changes.

Affected final review: same retained reviewer0/saved settings, high-risk
instruction boundary, general/architecture/scope/risk lanes as applicable; assess
complete final doc histories and compatibility with ordinary/recovery/lifecycle
rules. Reuse prior source review/CI within exact proven scope. Do not re-audit
50 unchanged kernel patches or demand new full VM run for documentation.
Workspace default integration requires separate explicit target approval; OS
staging approval already granted. No default mutation/claim taken yet.

### D3 final committed heads and quick checks

OS complete range42baba6117bebcde3d04555a71377381df197925..f33f5fd10b53232b5670862f832f4ec5ea835e84
(two commits2352449568afa3b2f5bd500dba3fbed1c1163e0b andf33f5fd).
Workspace complete policy range066f7b2c431aef53b206e196ce36750bf2649593..9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b
(one commit9610ea74). Initial workspace remote baseline5cde17b6..68eb91f2
cleanly rebased over shared tracking-only master066f7b2c; no tracking edits in
policy commit, same three source files, native range-diff expected'=' in receipt.
Workspace initial single source commit68eb91f2924b36735bddb791666c7bf38fdf831c
retained as provenance, final source unchanged. Declared Nix agent-instructions
check10tests/220assertions pass after shortening only completion bullet to fit
AGENTS16,381bytes; links/anchors/diff check pass, no declared hook framework.
OS quick skill/docs/links/shell/hooks and exact kernel/ZFS/source graph pass.
No migrations, pins, runtime/schema/metadata changes in D3.

## C4 mechanical configuration update — history packet preparation

User explicitly requests vpsadminos role updates in vpsfree-cz-configuration
channels staging/os-staging/production and master merge, no deployment. Own
config base9c6a0313d1689099c1dfcb065171a4aead44f183 ->
15e3b9af90276e41d19e6a33477add58e5f9a8c9. Complete one-commit series:
`inputs: update vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to f33f5fd1`.
Generated confctl grouped role-only update, changelog retained. Onlyflake.lock
+9/-9: each of3inputs locked.rev/lastModified/narHash to publishedf33f5fd1
andsha256-GwlQPVUCe6mGGFvBEhB4YTT+zdPNm0ZGGforhseLm8s=. No code/docs/channelmap
changes. Old staging/os-staginga7d71a54, oldproductione643cbef; explicit follows
keep distinct configNixpkgs. Fullgraph/key/follows/catalog/inventory checks in
C4-evidence.md (completion pending). Required hooks passed generatedcommit.

This is genuinely mechanical dependency-only content; standalone substantive
content-review exemption applies if final checks confirm no other change.
Whole-branch/history/repeated-pin/migration obligations remain; one final
update stream/onecommit per three distinctroleinputs, no intermediate repins,
no migrations or externally consumed transition. Underlying OS/kernel source
and D3 instructions already independently reviewed, prior exact kernelCI110tests
and postintegrationCI observed separately. Do not claim production deployment
or current active CI success. No config documentation needed for routine pins,
repo prohibits per-release receipts; evidence only in session.
