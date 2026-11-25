# Handoff to kernel bug proposal session

User explicitly requested a new workspace session with a full team to propose
solutions for the syslog, swap and NFS defects. Created using the public
`dev-session start` command with `--new --no-attach --team delegated` and the
full initial goal below. This original investigation session remains open.

New session: 2026-10-20-kernel-bug-fix-proposals

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-bug-fix-proposals/

Thread: 01a15aed-15b5-7621-863c-efb515e257ad

The creation command completed successfully. It reported a terminal client
restart after an App Server disconnect and returned the created slug, stable URL
and thread identity. This conversation remains bound to kernel-check; it does
not address or own the new session team or records. The requested proposal work
belongs to the new lead and full-team preset.

## Initial goal sent

Start a new Full team development session to propose solutions for three source-proven Linux kernel bugs found during the node24 investigation. The user explicitly requested a separate workspace session with a full team, to propose solutions. Work on proposals and verification design first; do not silently expand this request into implementation, kernel builds, merges, livepatching or deployment. Do not claim that any of these bugs caused node24's hang: no such incident attribution was established.

Session ownership and workflow
- This is a NEW initiative, separate from 2026-10-20-kernel-check. Verify your own dev-session current and thread/env binding before using your own records/team. Leave the original session open. Do not address or modify the original session's team, records, branches, worktrees, runtime or machines.
- Use the installed Full team preset (delegated), retained member settings and workspace AGENTS/procedure routing. Lead coordinates, architect owns substantive design and records design.md, both implementers own independent investigation/solution packages with nonoverlapping file boundaries and dependencies. The two implementation-purpose members can research the three proposals in sequential packages, coordinated by the architect. Reviewer is not assigned automatically to investigation-only evidence; follow mandatory review if a completed substantive deliverable triggers it.
- Inspect affected repositories' current instructions/docs and exact source, verify claims rather than trusting these notes, record supported-version scope and check whether newer upstream already fixes a bug. Use canonical repos read-only for proposal work; any actual source edits need an appropriate initiative worktree and explicit scoped implementation instruction.
- Produce a concrete proposal for each bug: failure chain, root cause, minimal correct fix, alternatives/tradeoffs, all relevant success/error paths, target versions and upstream/custom ownership, regression verification plan (including allocation-failure injection where appropriate), acceptance criteria, compatibility/module/livepatch/deployment/rollback implications and implementation boundaries. Explain whether a livepatch is feasible or a reboot is required; do not implement or deploy it.
- Keep results usable independently of the prior conversation. This prompt contains the required technical handoff. The original investigation is preserved in workspace commit bbbeacdd for provenance; do not rely on or mutate another session's active records. No production console command, deliberate crash, watchdog change or operational mutation is authorized.

Exact source provenance
- Incident vpsAdminOS: 2abbe3cc1c102a4b39022d3f73ef4a432ad4d616.
- Incident Linux 6.12.113: 1dfea587406b7dd79973831d1677fb2418e5e9aa (later .113 pin, after proactive DAMON/swap retirement).
- Initial .113 pin: 11058eb4fe1cba30653e8e643546c13bc8bcd792.
- Original 6.12.95 boot source: a2384967b90f24d2470c9eb15f0e66d938df7e08.
- Upstream stable bases: .95 296aabce459470a4c1b68ffd0c0c0920e563aaad; .113 7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e.
- Canonical bare repositories: /home/aither/workspace/ai/vpsfree.cz/repos/linux.git and repos/vpsadminos.git; production configuration only if needed for applicability. Linux is a partial/promisor clone: reads may fetch missing blobs implicitly. Prefer GIT_NO_LAZY_FETCH=1 for bounded reads, serialize necessary exact object-only materialization; avoid broad source fetching or ref mutations without coordination. No unrequested local kernel builds.

Bug 1: custom syslog namespace allocation-error NULL dereference
- kernel/syslog_namespace.c is identical at old/initial/current pins, blob e55346ef9a374d12966d4c10ae3d81fb0d9949c1. This is pre-existing, not a new .113 regression.
- At incident lines 128 onward, clone_syslog_ns kzallocs the namespace, so ns->prb begins NULL. syslog_ns_setup_log_buf (allocation sites around44/48/56/61) separately allocates ringbuffer, text, descriptors and info. It assigns ns->prb only after all allocations succeed (around70).
- Any setup allocation failure frees the locally acquired components and returns -ENOMEM, with ns->prb still NULL. The caller's fail_free_log_buf path (around151-160) nevertheless calls syslog_ns_log_buf_free(ns), whose first free expression dereferences ns->prb->desc_ring.descs (around90).
- Thus setup failure definitely faults in cleanup instead of returning ENOMEM. Some later allocation-failure paths also leave ns->log_buf pointing to locally freed text, but the unconditional NULL dereference happens first; do not present a separately executed double-free as observed.
- Immediate creation paths do not visibly hold the namespace locks or console semaphore across this cleanup. It proves an error-path fault, not a global lock orphan or whole-host hang.
- Proposal must clarify ownership/publication of partially initialized allocations, avoid double cleanup, balance namespace/user/parent/inum references, and cover each allocation failure plus normal namespace teardown.

Bug 2: custom cgroup-v1 swap reporting unsigned underflow
- More precisely this is swap-reporting arithmetic/snapshot consistency, not proven actual swap charge/reclaim corruption. Introduced after proactive swap removal/restored ordinary views in incident 1dfea587. Complete patch touches fs/proc/meminfo.c, kernel/sys.c, mm/swapfile.c; older/initial wrappers bounded the outputs.
- Finite v1 sysinfo free swap around kernel/sys.c:2873-2893 computes S - (M - U), S=memsw.max-memory.max, U=earlier resident-memory usage read, M=later combined memory+swap usage read. Individual page_counter_read calls are atomic, but not a joint snapshot.
- Concrete legal source interleaving: memory limit1024 pages, memsw limit1280 => S256; read U0, charge512 resident pages, read M512. Actual swap may remain0 and limits are respected, but reported unsigned free value becomes256-512 and wraps.
- v1 virtual /proc/swaps around mm/swapfile.c:3027-3047 computes (M-U)*PAGE_SIZE without saturation. Read U512, free256 resident pages, read M256 => negative difference wraps and prints a huge used value. Old wrappers bounded derived values/capacity.
- The outputs are formatted or returned in sysinfo, not used here as allocations, indices, charges or reclaim targets. No host-hang chain was established.
- Memory helper get_current_most_limited_memcg and seq-file open/release ownership are already fixed/balanced at all final pins; kernel/vpsadminos.c whole blob062ad3f5617ddea097566d69b46006ce452aa003 is identical. Do not regress those lifetimes while fixing reporting.
- Proposal should audit all related finite/unlimited v1/v2 reporting branches, zero capacity, concurrent limit/usage changes, units/overflow and consistency relationships. Prefer justified bounded values over adding unnecessary locks to obtain an unrealistic global snapshot.

Bug 3: upstream NFSv4.1 FREE_STATEID calldata allocation reference leak
- Stable ed1161ab6239761958b38d5667225634fc2be894 (upstream cf616096a0f3a2b60f7d68b6b39674a6867ded9c) adds a server pin during asynchronous FREE_STATEID to repair a use-after-free.
- Incident fs/nfs/nfs4proc.c nfs41_free_stateid around10630-10643 first increments clp->cl_count, then nfs_sb_active(server->super). That helper increments server->active and retains aggregate sb->s_active. Its failure branch drops the client ref correctly.
- On subsequent calldata kmalloc(sizeof(*data), GFP_KERNEL) failure, immediate return -ENOMEM drops neither pin. No RPC/calldata was created to invoke a later release callback. Success balances pins in nfs41_free_stateid_release around10585-10592.
- Proven effect: mount/server/client resources remain pinned. No held lock or host-wide wait mechanism was demonstrated. NFSv4.1 use and this allocation failure at the incident were not established.
- Do NOT generalize this to RPC task allocation failure: rpc_new_task's failure calls rpc_release_calldata in net/sunrpc/sched.c around1147-1152, so that later error path does invoke cleanup and balances pins.
- Pristine old stable already leaked the client ref on allocation failure, but actual old .95.6 effective alternatives differ: documented livepatch branch fc37ccc43227ab8eef70b50660a081f2615d0ead has vpsadminos_nfs_freeid adapter with kmalloc-failure goto out_deactive and balanced nfs_sb_deactive+nfs_put_client around10776/10864-10867; dispatch uses the adapter when v6 control exists around10905-10908. Raw fallback/control transition state remains distinct.
- Historical NFS boot tree563bbb35e8753e1bb34dad19ebeec8962ee3c1cd independently balances both refs on allocation failure around10640-10644. Exact old loaded module/control state was unknown. These are useful correct unwind examples, not permission to rewrite published livepatch history.
- Proposal must preserve success, failed acquisition, calldata allocation failure, RPC task allocation failure, async release and server/superblock lifetime ordering. Check for a newer official upstream fix before proposing a downstream-only patch, and describe upstream submission/backport options.

Deliver the three proposed solutions and discriminating verification briefs, with clear remaining decisions. Keep incident causality, watchdog/SysRq troubleshooting and production changes out of this proposal's scope.
