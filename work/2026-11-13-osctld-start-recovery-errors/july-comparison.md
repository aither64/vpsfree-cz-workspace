# July lifecycle comparison for the CT1391 incident

Package B, implementer1, 2026-11-13. Read-only investigation of the named July
records and committed sources; only this document is written. No July worktree,
record, ref, runtime or team was changed or contacted. No production access,
code edit, commit, test execution, review, merge or deployment was performed.

## Result

The July branch addresses overlapping lifecycle effects after a container and
its run can be resolved: exact generations, durable intents, leased callbacks,
and cleanup before replacement. It does **not** establish lossless delivery of
guest shutdown/reboot callbacks while the daemon is down or before the container
is published during import. Both callback handlers still reject a missing
database entry. A stopped-run reconstruction uses the saved reboot flag; it
cannot recover an unseen `LXC_TARGET=reboot` from the stopped state alone.

July also lacks the deployed revision's persisted host-link identity and
recovery-taint admission contract. Its name-based cleanup and permissive link-up
behavior cannot establish a safe fix for the current stale-link lockout. Preserve
the deployed identity/ownership checks when considering a smaller import race
fix. Importing the July branch is outside this package and the session scope.

## Revisions and provenance

All `J:path:lines` citations below mean vpsadminos commit
`9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`; `D:path:lines` means deployed-source
comparison commit `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`. `A:path:lines` means
vpsadmin commit `807e9d7f1277217d3cf2d49b7c4b2525dc441c10`. Line numbers come from
`git --git-dir=repos/<project>.git show <exact-commit>:<path> | nl -ba`.

| Repository / ref | Local branch and origin-tracking ref | Fresh SSH `ls-remote origin` |
| --- | --- | --- |
| vpsadminos `2026-07-24-ct-start-hang` | `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44` | Same exact SHA |
| vpsadmin `2026-07-24-ct-start-hang` | `807e9d7f1277217d3cf2d49b7c4b2525dc441c10` | Same exact SHA |
| vpsadminos `staging` | `origin/staging` = `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62` | Same exact SHA |
| vpsadmin `master` | `origin/master` = `2d0946c4e699aa61092228d8a7cb275477ee46d0` | Same exact SHA |

`git merge-base J D` returned `23cf4fc36f15ce510c63b5134f4ea8038b706e31`, the
July record's final review base. `merge-base --is-ancestor` returned 1 for July
OS head versus D, and for July vpsadmin head versus the observed `origin/master`.
Thus neither exact July head is integrated into its observed remote default.
This checks ancestry, not possible independent patch equivalence. No refs were
fetched or updated. The initial July base recorded in state is
`4476942c4e33092e20e4faa91f32dfcca9a3ea7d`.

The authorized old `plan.md` (230 lines), `state.md` (2,083 lines) and
`portal.yml` (15 lines) under `work/2026-07-24-ct-start-hang/` were read. They
record active/unmerged status, published heads, completed reviews and successful
workflows, not production deployment. Final recorded OS runs are RSpec
`30256514274`, RuboCop `30256514441` and CI `30256514753`; final recorded vpsadmin
run is CI `30280858867`. These are **historical recorded results**, not CI or
test results independently rerun in this package. The vpsadmin `flake.lock` at A,
lines 143–148, independently pins J.

The incident chronology, recovery success and deployed-fleet statement come
from [incident.md](incident.md), supplied by the user and not independently
observed here. In particular, the initiator's intent and the exact failing
callback response remain unproved. The source below makes an early lookup
failure plausible; it does not prove the incident returned that response.

## Shutdown and reboot around daemon downtime and import

| Boundary | July source behavior | Consequence / limit |
| --- | --- | --- |
| Hook executes with no user-control socket | `J:osctld/hooks/ct-post-stop:23–35` and `J:osctld/hooks/veth-down:35–48` make one socket connection/request, read one reply, and exit unsuccessfully on a false reply. There is no retry or durable callback spool in these scripts. | A target never accepted by the daemon has no persistence guarantee from these hooks. Socket connection exceptions likewise have no retry path here. |
| Hook reaches new daemon before CT publication | `J:osctld/lib/osctld/pool.rb:683–703` constructs the CT, initializes incarnation/lifecycle, ensures limits, creates LXC home/log and reconfigures before `DB::Containers.add`. `UserControl::Commands::Base.run` first looks up that DB (`J:osctld/lib/osctld/user_control/commands/base.rb:17–39`). `CtPostStop.execute:14–15` and `VethDown.execute:12–13` in their matching `user_control/commands/*.rb` return `container not found` if absent. | The generation reducer does not provide an admission queue before publication. Callback leasing cannot help a CT that cannot yet be found. There is also a publication-to-run-adoption interval: pool lines 705–720 reconstruct/adopt the run only after insertion. |
| Published run receives post-stop target | `J:osctld/lib/osctld/user_control/commands/ct_post_stop.rb:18–36` requires exact run config, saves `run_conf.request_reboot` only for target `reboot` and a normal CT run, then observes post-stop with that boolean. `RunConfiguration#request_reboot` saves `@do_reboot` (`J:osctld/lib/osctld/container/run_configuration.rb:187–196`). | Received reboot intent can survive daemon restart. An absent/rejected callback cannot reach this save. A transient stopped execution does not become a normal CT reboot. |
| Normal guest halt, with no newer intent | `Lifecycle#observe_post_stop` sets a halt/stopped intent when reboot is false and current intent still equals launch intent (`J:osctld/lib/osctld/container/lifecycle.rb:1399–1425`). | A normally halted generation does not automatically restart. This also describes reconstruction after a lost callback when no reboot flag or separate newer running intent was recorded. |
| Guest reboot target received | The same reducer creates a running/reboot intent, unless explicit stopped intent or an already pending running intent takes precedence. `complete_run` returns only a pending replacement intent (`J:osctld/lib/osctld/container/lifecycle.rb:1551–1566,2790–2805`). | Exactly one replacement is requested after cleanup. A newer explicit stop wins; an external start can share the pending replacement. |
| Import finds an existing stopped generation after callback loss | `Pool#load_cts` recovers an active run (`J:osctld/lib/osctld/pool.rb:750–770`). `Recovery#recover_state` takes a reconciliation lease, probes LXC, commits exclusivity, then dispatches stopped-run recovery (`J:osctld/lib/osctld/container/recovery.rb:24–74`). `recover_stopped_run` takes interfaces down, marks stopped and synthesizes `observe_post_stop(aborted: true, reboot: run_conf.reboot? || false)` (`:766–803`). | Reconstructs cleanup, **not the missing target**. With an unchanged launch intent and false saved reboot flag, a lost guest reboot can be treated as halt. If reboot was already saved, a newer start/restart intent exists, or a direct-reboot reservation remains, the corresponding separate durable evidence changes the result. This is source reasoning, not a reproduced incident. |
| First upgrade adopts a legacy run | `J:osctld/lib/osctld/pool.rb:705–720` adopts only an available run config when there is no active reducer run. `Lifecycle#adopt_legacy` records legacy resources/callback permission, saved reboot flag and observed state (`J:osctld/lib/osctld/container/lifecycle.rb:2199–2250`). | Legacy adoption is not a mailbox for callbacks that arrived before lookup/adoption. If no active run or usable run config remains, the stopped active-run reconstruction above cannot be assumed. |

An accepted replacement is not started before pool import completes:
`LifecycleFinalizer#restart_container` registers the reboot, waits for
`pool.imported?`, then issues `Start` with the exact intent ID
(`J:osctld/lib/osctld/container/lifecycle_finalizer.rb:265–284`). This is ordering
for an already known intent, not evidence of recovery of an unknown one.

Direct libLXC reboot has a different ambiguity contract. A reserved
`control_reboot` effect persists `delivery_unknown` after a lost runner reply;
post-stop consumes that reservation as reboot even without a true callback
boolean. Explicit stop can supersede it while retaining a hazard
(`J:osctld/lib/osctld/container/lifecycle.rb:298–326,458–489,1406–1409`). This
does not prove that an arbitrary guest-initiated reboot was durably reserved.

## What callback fencing does cover

After successful CT/run lookup, `Base.run` acquires and releases the exact
callback worker (`J:osctld/lib/osctld/user_control/commands/base.rb:35–48`).
`Lifecycle#begin_callback` rejects a different/inactive run, recovery or cleanup;
persists worker identity; waits behind policy work; asks nonexclusive
reconciliation to yield or waits behind exclusive reconciliation
(`J:osctld/lib/osctld/container/lifecycle.rb:1030–1113`). Reconciliation commits
exclusivity only if no callback asked it to yield (`:955–1024`). These boundaries
prevent two already admitted workers from independently finalizing a run.

The id-less legacy exception is deliberately narrow: only post-stop opts into
it; the base resolves the active run explicitly marked as adopted legacy.
New generated callbacks still require exact identity
(`J:osctld/lib/osctld/user_control/commands/base.rb:9–26,66–82` and
`ct_post_stop.rb:7–8`). This exception does not make a missing CT discoverable.

The wrapper watcher can reconcile a run whose wrapper disappears without
post-stop (`J:osctld/lib/osctld/container/lifecycle_finalizer.rb:20–64`); a
reconciliation watcher retries after persisted workers leave (`:68–93`).
Finalization retains ownership through hooks/resource cleanup and only then
completes the run and starts its replacement (`:102–175`). Start joins/waits for
that exact predecessor (`J:osctld/lib/osctld/commands/container/start.rb:18–96`),
and stop waits for exact generation cleanup
(`J:osctld/lib/osctld/commands/container/stop.rb:17–80`). The pool executor bounds
parallel effects without adding an effect deadline
(`J:osctld/lib/osctld/container/lifecycle_executor.rb:14–25,51–79`).

## Stale host links and subsequent start gates

July's `NetInterface::Veth#load/save` stores network configuration, not the
deployed name/index/kind/boot ownership record; `setup` discovers a name only
for a running CT; `up` assigns `@veth`; `down` clears that name and deletes links
by name, logging command failures (`J:osctld/lib/osctld/net_interface/veth.rb:
29–52,138–140,195–245`). July records interface name/type/routes per generation
(`J:osctld/lib/osctld/container/lifecycle.rb:1636–1664`), and `VethDown` checks that
the requested veth belongs to that run before calling `netif.down`
(`J:osctld/lib/osctld/user_control/commands/veth_down.rb:16–35`).

July recovery retains names referenced by another active/residual generation,
or discovers routed links and checks other CT references; deletion still uses
names (`J:osctld/lib/osctld/container/recovery.rb:494–587,967–999`). These are
useful generation/DB protections, but they do not validate kernel identity after
name or ifindex reuse. The July tests named “stale veth” exercise route/DB
references with doubles, not the deployed persisted identity tuple.

At D, `Veth#setup` deliberately preserves an existing ownership record even
when its link is absent/reused (`D:osctld/lib/osctld/net_interface/veth.rb:197–229`).
`validate_up_callback` verifies kernel kind/index, taint and shared ownership,
then rejects a changed identity; `up` persists the identity and taints on an
exception (`:269–305,354–383`). `forget_absent_host_link!` verifies both lookup
by name and by index for veth and recorded IFB before clearing ownership
(`:438–466`). Those checks explain why the old record cannot safely be replaced
merely because a new veth-up callback arrived.

The admission difference is concrete:

- July `Container#can_start?` checks staged/error/pool-active only
  (`J:osctld/lib/osctld/container.rb:446–448`), followed by reducer policy,
  generation and recovery checks (`J:osctld/lib/osctld/container/lifecycle.rb:
  60–127`). It still emits generic `start not available` at its first gate
  (`J:osctld/lib/osctld/commands/container/start.rb:21`).
- D adds independent container recovery taint and any netif recovery taint
  to that gate (`D:osctld/lib/osctld/container.rb:413–417`).
  `Recovery#cleanup_or_taint` tries cgroups, interface down, network cleanup
  and released-host-link verification while retaining failure as taint
  (`D:osctld/lib/osctld/container/recovery.rb:94–134`).

The supplied CT1391 changed-identity error, missing recorded link, failed
released-host-link verification and later blocked starts fit D's contract.
July does not reproduce that same contract, so an apparent July ability to
start does not establish safe recovery from the current ownership uncertainty.

D's ordinary import publishes after preparation, monitor and console setup
(`D:osctld/lib/osctld/pool.rb:738–756`); its authenticated running-impermanent
path has a separate earlier publication boundary (`:701–733`). July publishes
before monitor/adoption/recovery but still after preparation (`J:pool.rb:
683–720,748–770`, with the full path above). Moving one publication boundary
therefore cannot by itself prove the race solved for shutdown **and** reboot,
all import stages, and authenticated impermanent runs.

## Coverage inspected and gaps

All rows below refer to J unless marked A. Tests were inspected, not rerun.

| Test path and lines | What it establishes | What it does not establish |
| --- | --- | --- |
| `osctld/spec/osctld/container/lifecycle_spec.rb:40–55` | Intent and exact resources survive creating another reducer instance. | Callback accepted while no daemon/CT entry exists. |
| Same file `:1971–2021` | Explicit ordinary halt stays stopped; explicit reboot gets a replacement intent. | Recovering the distinction when the target never reached the daemon. |
| Same file `:2024–2056` | External start and known in-container reboot share replacement generation. | Guest reboot during daemon downtime/import. |
| Same file `:1696–1800` | Dead reconciliation worker replacement, callback yielding, and exclusive reconciliation wait. | CT lookup/adoption admission before those reducer methods can run. |
| Same file `:998–1045,1078–1102` | Direct-reboot reservation and lost-reply behavior; explicit stop supersession. | Unreserved guest reboot target persistence. |
| `osctld/spec/osctld/container/recovery_spec.rb:43–77,178–225` | Name-reference cleanup, recognized newer replacement intent, recovery yielding to admitted callback. | Kernel link identity reuse; recovering unseen target. |
| `osctld/spec/osctld/user_control/commands/managed_lifecycle_spec.rb:70–75,111–179` | Existing DB CT fixture, exact lease wrapping, adopted id-less post-stop acceptance, non-adopted rejection. | Prepublication missing-CT retry/queue; both guest targets during import. |
| `tests/suite/osctld/restart.nix:340–382,437–470` | Restart/death during active externally driven start/restart. | Guest shutdown and guest reboot independently while daemon is unavailable. |
| Same VM file `:385–434` | Guest reboot plus external start converges after a blocked post-stop user hook. | This example does not restart/kill osctld or block CT publication; daemon already accepted the post-stop path. |
| `tests/suite/osctld/lifecycle.nix:265–304,433–445,489–513` | Residual quarantine/disjoint replacement and drained legacy downgrade/re-adoption examples. | Combined loss of callbacks/import/host-link identity cases. |
| A `libnodectld/spec/nodectld/commands/vps/recover_cleanup_spec.rb:148–189,268–365` | Incomplete cleanup proof becomes unknown; partial/quarantined/legacy replies warn and continue; blocked/ambiguous replies reject. | Any callback persistence, guest target inference or host-link repair. |

No direct deterministic regression for “callback before `DB::Containers.add`”
with both shutdown and reboot was found in these inspected lifecycle, recovery,
managed-callback and VM cases. This is a bounded coverage conclusion, not an
assertion that every test in the repository was audited. No July test was run.

## Compatibility and implications for current design

July's atomic lifecycle record is `<pool.ct_dir>/<ctid>/lifecycle.yml`, with
fsync/write/rename/fsync persistence (`J:osctld/lib/osctld/container/lifecycle.rb:
2404–2446`). Its optional persistent incarnation ID, generation-qualified
resources/hooks, policy taint, persistent group quarantine and unsupported live
downgrade are materially broader than an error-message/import-race change.
The shipped man page documents durable acknowledgement and client-only wait
deadlines (`J:osctl/man/man8/osctl.8.md:888–896`), bounded-risk residual cleanup
and strict drained downgrade prerequisites (`:2646–2685`). The old plan says
nodes can update independently and prefers vpsadmin first; it does not require
fleetwide synchronized rollout. That historical compatibility claim is not
verification of compatibility with D's later ownership/impermanence behavior.

The vpsadmin change at A retains cleanup evidence, treats complete typed
`cleaned` proof as clean, and records continuable warnings for qualified
partial/quarantined/legacy results
(`A:libnodectld/lib/nodectld/commands/vps/recover_cleanup.rb:5–58,67–122`). It
does not transmit missing guest target information or repair early hook lookup.

For the current design owner, the supported inference is to preserve D's link
ownership checks and recovery gates, distinguish callback admission from
reconciliation after admission, and require separate evidence for shutdown and
reboot intent across downtime/import. A scheme that only reconstructs
`stopped` cannot prove the lost guest target; a scheme that only publishes
earlier cannot prove authenticity/readiness or handle the entire daemon-down
interval. Selecting that fix and any protocol/persistence change belongs to the
architect/lead, not this comparison package.

## Commands and delivery limits

Session identity was verified with `dev-session current` and both matching
`DEV_SESSION_*` values. Same-session roster confirmed implementer1 and architect0
addresses/access. Repository inspection used canonical bare `git show`, `git
grep`, `git ls-tree`, `for-each-ref`, `merge-base` and fresh SSH `ls-remote`; no
old worktree was entered. Source examples and tests were read at the exact
commits above. Historical state was read in bounded sequential chunks. Relevant
repository guidance, documentation index and lifecycle man-page contracts were
read. No expensive checks were required or performed.

Package findings were sent directly from implementer1 to architect0 with stable
message IDs `7ecf7e52-2e3b-4a6b-90b9-a65ebce1df51` and
`4734242c-0814-4710-8c4d-6a8a8b153751`; milestone report to lead used
`900bc159-6932-40c5-95a7-59a113cf8c03`. No design deviation or new execution
package was accepted. Lead owns state/manifest links, acceptance and any next
assignment. This evidence record does not invoke independent final review.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctld-start-recovery-errors/>
