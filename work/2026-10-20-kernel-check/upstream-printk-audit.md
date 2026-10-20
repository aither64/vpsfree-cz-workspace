# Bounded printk/panic interaction audit

Owner: implementer0. Read-only source audit of the seven upstream printk changes
and their immediate interaction with the downstream syslog namespace port.

## Conclusion

**No source-proven new lock/wait cycle or panic-to-kexec regression was found
in this bounded intersection. No incident cause is established.** The seven
changes are all accounted for below. This does not certify the entire console,
panic, driver or crash-upload path.

Compared stable bases `296aabce459470a4c1b68ffd0c0c0920e563aaad` and
`7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e`, then inspected effective old
`a2384967b90f24d2470c9eb15f0e66d938df7e08` and incident
`1dfea587406b7dd79973831d1677fb2418e5e9aa` sources. All line references below
are to the incident Linux tree unless explicitly labelled old.

The custom v20/v21 patch text is equivalent, but that fact alone was not treated
as proof about upstream caller/lock context. This audit read all seven exact
upstream diffs, the final port and the immediate functions governing handover,
record reading, namespace storage, panic selection and crash-kexec ordering.

## Seven changes

| Stable commit / upstream commit | Change | Source conclusion |
| --- | --- | --- |
| `abe27b84459d34e1fc0520af0a9631cc4c0a6379` / `c1aa3daa517292303d98ff61f0440c354669f948` | Adds optional non-panic CPU ring-buffer writes and adjusts panic record skipping. | Default false preserves old behavior. With the option enabled, an unfinalized record makes the reader return false; it adds no wait for that producer. |
| `1d15ba2d4ae3a310e7c5badd14773dfd42cd400e` / `d0d9c7235548f1d772f1e48c9d5742c65d81c705` | Moves panic state predicates into panic.c and adds helpers. | Existing panic_in_progress expression is unchanged; the new helpers use atomic state/CPU checks, not locks. |
| `1c61055d9062fbe30f4c2ada2ab27cbfb7e0db7e` / `c6be36e2997662f423edfa3979a63935873ff648` | Replaces this_cpu_in_panic with panic_on_this_cpu in printk/nbcon/ringbuffer/dump_stack. | Normalized predicate bodies are equal. Panic dump_stack still bypasses printk_cpu_sync rather than waiting for another CPU. |
| `c5366c72af8b762ba955f92cc55d63857c0aaeaa` / `d4a36db5639db032a434aef968f9188a600139ec` | Replaces other_cpu_in_panic with panic_on_other_cpu. | Normalized predicate bodies are equal. Existing non-panic console suppression/sleep is preserved; no new namespace wait. |
| `d0e8ef0b903ad34baab81ba7bde82e205f659a39` / `741ea7aa95dd9ac77f861e7d0961d8d231ac8448` | Extracts the per-record console loop into console_flush_one_record. | Console semaphore/SRCU/driver ordering and handover contract are retained. Caller stops on handover or another panic CPU, and unlocks when it still owns the semaphore. |
| `f0104a7b730de32eefb3d4a27279592b5504ad59` / `36630cafbeede0b64c370edb2f7b4094327ee1e0` | Moves con sequence reads after the handover test. | Fixes the old use-after-free window after SRCU handover; final incident source contains the fix. |
| `46160d24b6710f9dcb2c9d69f997b1664d027d42` / `560f4deda32785e260056200f8bb911c475c5b88` | Initializes nbcon printer wake work as IRQ_WORK_LAZY. | Defers normal printer-thread wake to a tick; emitter does not wait for it. Panic uses atomic/direct output, not completion of this lazy work. |

Six of these commits touch `kernel/printk/printk.c`; the seventh is the one-line
nbcon lazy-work initializer change. Their path inventory is exhaustive for the
stated printk predicate (`kernel/printk/` or `include/linux/printk*`). Other
upstream subsystems were not added to this audit.

## Lock, ownership and progress checks

The effective path in `kernel/printk/printk.c:2429-2503` is
`vprintk_emit_ns` → namespace ring-buffer storage → selected console flush/wake.
Panic filtering occurs before storing. Namespace-to-init mirroring calls
`vprintk_store_ns_tagged` sequentially for the init buffer and local buffer;
`vprintk_store_ns_tagged:2271-2385` uses the existing IRQ/recursion guard and
ring-buffer reserve/commit operations, not `ns->syslog_lock` or
`ns->dump_list_lock`. Console emit/read paths select `init_syslog_ns.prb`
(`console_emit_next_record:3146-3153`, `nbcon.c:1626-1629`). No newly moved
flush holds a namespace mutex while acquiring the console semaphore.

The synchronous legacy path already disables preemption and calls
`console_trylock_spinning` (`printk.c:2476-2494`). Its potential busy wait on
`console_waiter` is old behavior, not introduced by these seven changes:

1. The writer owns `console_sem`, then obtains a console SRCU read section
   (`console_flush_one_record:3255-3266`), then calls the console's existing
   emit/driver operation.
2. A spinning handover explicitly drops SRCU and transfers semaphore ownership
   (`console_lock_spinning_disable_and_check:1942-2006`). The final loop checks
   `*handover` before any subsequent `con` read (`3291-3308`). A handover returns
   without a second SRCU unlock; the outer flush avoids unlocking a semaphore
   it no longer owns (`3398-3400`). Normal and panic-abandon exits release SRCU.
3. On another panic CPU, the loop gives up; the owning wrapper releases the
   semaphore. A panic CPU does not start spinning on the old owner
   (`console_trylock_spinning:2011-2030`). The `console_owner_lock` paths also
   retain the existing panic bypass. The helper conversions do not create a
   panic-CPU dependency on a stopped owner.

The UAF fix specifically removes the old post-handover `con->seq` /
`nbcon_seq_read(con)` accesses before the ownership test. The refactor retains
existing driver callbacks and rescheduling points; it does not add a wait for
namespace readers, namespace creation or namespace destruction. A driver that
never returns, an already stalled old console owner, or unlimited logging can
still be problematic in general, but no newly introduced reachable cycle or
matching incident evidence was established here.

The nbcon change affects only scheduling of `nbcon_irq_work`:
`nbcon_alloc:1698` now uses `IRQ_WORK_INIT_LAZY`; `nbcon_kthreads_wake:1271-1291`
queues it when a printer sleeps, and `nbcon_irq_work:1244-1249` wakes the printer.
The emitting CPU does not wait for this work. For the panic CPU,
`nbcon_get_default_prio:1393-1399` selects `NBCON_PRIO_PANIC`, and
`internal.h:269-298` selects direct/atomic output with no printer offload.
This can change ordinary deferred-console latency; it does not show a new
panic-time dependency on a future tick or printer-thread completion.

## Panic state, ring-buffer read and crash ordering

The normalized bodies of old `panic_in_progress`, `this_cpu_in_panic` and
`other_cpu_in_panic` equal the final `panic_in_progress`, `panic_on_this_cpu`
and `panic_on_other_cpu`, respectively. They read `panic_cpu` and the raw CPU
ID; neither the port nor helper moves add a lock or namespace predicate.
`dump_stack_lvl` retains the panic-CPU bypass of `printk_cpu_sync`
(`lib/dump_stack.c:104-130`).

`debug_non_panic_cpus` is zero-initialized/disabled by default
(`printk.c:2405-2418`); its configurable interface is under
`CONFIG_PRINTK_CALLER`. No runtime value was changed or inferred from that
default. With default behavior, non-panic CPU suppression and panic record
skipping preserve the old logic. If explicitly enabled, `_prb_read_valid`
(`printk_ringbuffer.c:2106-2162`) may return false on an unfinalized record
until panic synchronous flushing is allowed. It does not sleep/spin waiting
for that record's writer. `nbcon_atomic_flush_pending_con:1564-1576` also
returns on errors/unfinalized records rather than waiting for another producer.
Possible output visibility changes are not a proven host progress failure.

Immediate `panic()` ordering is the same in old and incident sources:

| Operation | Old `kernel/panic.c` line | Incident line |
| --- | ---: | ---: |
| Panic `pr_emerg` | 348 | 401 |
| Optional `dump_stack` | 354 | 407 |
| Early `__crash_kexec` when post-notifiers is false | 373 | 426 |
| Other CPU shutdown | 375 | 428 |
| Allow legacy synchronous panic flush | 377 | 430 |
| Late `__crash_kexec` when post-notifiers is true | 399 | 452 |
| Final `console_flush_on_panic` | 412 | 465 |

Thus the final explicit legacy flush and CPU-stop sequence was not newly moved
before the ordinary early crash-kexec call. Early `pr_emerg` or `dump_stack`
can still run console/diagnostic code before that call, as they did in `.95`;
this audit does not certify arbitrary driver behavior there. The final explicit
panic flush ignores the normal console lock, and the panic helper/read changes
above do not establish a new pre-kexec namespace/global-lock wait.

Per the lead, kdump-loaded markers were observed at 18:31:57/59, approximately
26.5 minutes before logging stopped, but no crash upload was seen. These are
important incident constraints. They do not independently prove panic entry,
execution up to `__crash_kexec`, or success/failure inside a crash kernel. No
stack, stopped-CPU trace, console-driver stall or candidate-specific
reproduction supplied the missing failure chain.

## Separate pre-existing cleanup defect

The source-proven namespace-allocation NULL dereference from
[syslog-nfs-audit.md](syslog-nfs-audit.md) remains separate:
`clone_syslog_ns:128-160` initializes but does not acquire the new namespace's
mutex/spinlock; failed ring-buffer allocation leaves `ns->prb == NULL`, then
`syslog_ns_log_buf_free:88-93` dereferences it. The inspected immediate caller
path does not hold a syslog mutex/spinlock or console semaphore across this
cleanup. It proves an allocation-error fault, not an orphaned global-lock cycle.
The namespace file is byte-identical in old/incident trees, and neither
documented v6 livepatch source variant overrides it (see
[upstream-provenance.md](upstream-provenance.md)). Trigger and actual runtime
consequences remain unestablished; it is not a newly proven explanation for
this incident.

## Evidence and limits

Quick source checks completed: seven exact diffs; final handover/access order;
normal/panic release paths; normalized predicate equality; old/new panic call
order; namespace buffer/lock selection; and Markdown whitespace checks.
Read-only diagnosis required 11 exact missing blobs among 28 touched by these
seven commits. One lead-authorized object-only fetch completed in seconds with
`--no-tags --no-write-fetch-head --filter=blob:none --stdin`; no ref refresh.
All later reads used `GIT_NO_LAZY_FETCH=1`. No build, runtime sysctl change,
production mutation or dynamic reproduction was performed.

Outcome: **bounded negative for these seven changes and the immediate custom
namespace intersection**. A new cause claim would require a reachable
lock/progress chain tied to the incident or a discriminating isolated
reproduction; the absence of crash output alone supplies neither.
