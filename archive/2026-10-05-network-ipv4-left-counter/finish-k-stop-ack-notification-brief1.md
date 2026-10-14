# Bounded first-stop acknowledgement-loss repair

Parent verified reviewer0's Important finding against exact K29b at the control
request path. The original four-lane review continues on unchanged committed
objects. No application edit may begin until root supplies its completion boundary.

The accepted one-shot shutdown must start after the first valid request wins the
latch even if reply delivery fails. Keep current live peer/request checks, latch,
readiness withdrawal, notifier and main drain. Put the existing first-request
notification in a narrow ensure around acknowledgement puts/flush (or an equally
small ordering with a concrete reason), so reply EPIPE/IOError cannot skip it.
Do not notify invalid requests or repeat notification for later valid requests.
Do not broaden rescue, swallow new errors, add polling/retry/deadline/controller
frameworks, change protocol/phase/claims/cleanup semantics or touch Engine/E.

Owners: cluster/lib/devcluster_runner.rb and existing tools/test-machine.rb only.
Add one deterministic actual-owned runner/socket regression: a valid first stop
is read and latches before a fixture-only real-socket response barrier; close that
first client before permitting the actual acknowledgement write, prove its native
broken reply, then observe the same runner entering one graceful drain. A later
actual public stop must authenticate and wait for that same drain, with no repeated
machine stop, readiness false, retained claims/children before exit and ordinary
complete/gone/socket cleanup only after fixture-owned children exit. Use existing
owned pipe/socket/runner helpers and bounded guards; no production test hook or
probabilistic disconnect race. Preserve primary failure/native diagnostics and
reap/release only synthetic fixture-owned resources on failure. Keep all current
methods, original delayed_shutdown helper and five-second guards byte-identical.

Read mandatory workspace procedures and K AGENTS/runtime contract first. Retain
saved identity/model/effort/workspace_write settings. No local tests/syntax/lint/
formatter/eval/build, CI polling, process or guest probes, Git/index/ref/pins, private
campaign or preview access. Freeze exact two-path source/modes/full diff/protected
baseline/control hashes and source-only static explanation; root owns normal
consolidation, exact hosted K/E proof and direct mandatory-review step9 disposition.
Return any material design deviation before expanding the boundary.
