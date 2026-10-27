# Static naming evaluator v2 settlement correction

Prepared only. No evaluator, guard, signal helper or source module was imported
or executed. No Nix/query/test/build/native/provider/VM/browser operation ran.
Only this new v2 directory was written. All earlier packets, the original37
inputs and accepted binding proposal remain unchanged. Session/current and the
full environment pair matched; live roster32 confirmed retained ready
Sol/xhigh/workspace_write. Applicable unchanged guidance and monitor instructions
were reused from their full reads.

## Exact correction

stage() records its start_new_session child's PID and group immediately, with
observed group/session/start ticks/executable where available. Observations are
limited to that child. When its monitor exits normally, times out, hits a cap
or raises, finally calls settlement even when the direct child was already
reaped. There is no global process scan or daemon inference.

Settlement uses only killpg(recorded_child_pid,0). ESRCH means absent; EPERM
means present. Other probe errors remain unconfirmed. poll()/wait(timeout=0)
record the actual direct-child exit/reap; child exit alone does not certify its
group. If needed, TERM is sent to that exact group, followed at one fixed
origin+5-second deadline by KILL if still present. Settlement ends by the same
origin+10-second deadline. Observing a reaped child and absent group can finish
earlier; no phase resets or additional join deadline are introduced.

Each stage retains immediate child metadata, group probes, signal outcomes,
actual exit/reap and settlement status. Success requires actual exit0, reaped
child, observed group absence, no timeout/cap/primary exception and appropriate
post-guards. A nonzero command with a settled group still fails. A normal exit0
with descendants may require the recorded finite group escalation; its receipt
shows that action rather than claiming exit0 alone proved completion.

An unconfirmed group stops the sequence. No new subprocess, including the final
current command, may follow it. Pure final file guards still record their actual
result. Existing/partial stdout, stderr, argv, process and outcome receipts stay
retained; there is no retry, source repair, root operation or cleanup action.

On admitted stage failure with groups settled, finally independently records
full final file guards before and after the fixed identity command. A separate
source-file guard failure cannot silently suppress that identity attempt. The
identity command still requires the exact session environment and bound current
tool alias/file identity; if safe admission is unavailable, it fails with an
explicit missing/failed identity rather than invoking a replacement. Only the
literal04-current-after dev-session/current command receives this finalization
path; no Nix stage follows a main failure. Final identity has its existing30s
bound plus the same maximum10s group settlement. Both final file guards and
actual matching current result must pass for overall success.

A runner SIGTERM raises SystemExit so admitted finally paths can settle their
recorded groups. Hard kill, repeated interruption, inaccessible groups or failed
receipt writes can leave partial/uncertain evidence; none is certified settled.
Group absence is a bounded observation, not a daemon or global process claim.

## Preserved scope and launch inputs

The full evaluate-v1-to-v2.diff is retained. Options, all nonfinal stage call
arguments, observe_roots() and require_exact_metadata() compare AST-exact to v1.
All Nix expressions, selectors, source/input expectations, output/raw root gates
and the original verify-evaluation.py remain unchanged. The only projected paths
are v2's evaluator/cwd, future binding/release and new attempt destination.

retained-inputs.json binds v1's exact evaluator, its parent static acceptance,
proposal80dd48cf and parent acceptance64f40871 as immutable external inputs.
No proposal field was rewritten, copied to an active binding, or independently
remeasured as a current tool. ready.json is complete preparation with the existing
argv, bounds and four root gates plus these settlement/finalization conditions.
Original stage deadlines/caps remain unchanged; overall stage admission remains
900s and the parent watchdog960s. Final identity is allowed its bounded
finalization window after main admission expires, subject to the outer watchdog.

After parent inspection and separate release, the exact future command is:

```sh
/home/aither/.nix-profile/bin/python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/naming-runtime-evaluation-availability-successor-v2/evaluate.py --execute-parent-released-evaluation
```

Cwd is this v2 directory. final-bindings.json, parent-release.json and
attempt-evaluation-availability-v2-01 are absent. Parent alone supplies accepted
current tools/environment, copies an approved binding, writes the exact v2
release and launches one fresh policy-selected utility. No execution permission
or output availability follows from this package. The unchanged offline options
retain their documented source/cache limits; no legacy instantiation or automatic
retrieval route is added.

Static evidence is Python AST/JSON decoding and narrow source-equality proofs
only. No process-settlement helper test was run, and no group-empty observation
is claimed. Compilation, evaluated output graph, installed resources, managed/
real canary, provider, system, browser and deployment gates remain separate.
Dedicated real Luna home/account availability remains unresolved. No source/Git,
toolchain scan, peer observation, publication, claim, lifecycle or cleanup action
was performed. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
