# Reconciled parent launch failure and diagnostic field correction

Parent launched the accepted command once in scope
`vpsadmin-haveapi-upgrade-e-20261026T151600Z.scope`, invocation
`e608b2ecf94e456bbf52c4621fd7b08f`, tool handle 72625. Parent reports exit 125
and only the generic driver failure diagnostic. This attempt is retained;
it was not retried or given a manufactured identity/result receipt.

Read-only reconciliation at 15:18:47 UTC found the scope inactive/dead and
already collected (`LoadState=not-found`, no cgroup). Its current default
`Result=success` property is not historical startup success. The exact attempt
contains only zero-byte `events.jsonl`; there is no identity/result file.
Native state remains the original config/socket-only stub, stopped/not ready,
no pending selection, socket absent. Config SHA-256 remains
`10819c2d393795f4909695f04e4caf3d4035a94e84e25c871ecfc1ab19a16332`;
socket-file SHA-256 remains
`e7c1b9ea25d44de6b4642ade1a26e53862cfeece18e95156e3d198e6072bf3d2`.
No exact-session native start client, VM runner or QEMU was found.
See [allowlisted effects evidence](activation-failure-20261026T151600Z.json).

The driver creates/opens the attempt event file only after all initial
session/generation/source/config/socket, requested Nix 2-job/4-core and cgroup
limit preconditions have passed. Its next statement expands `scope=args.scope`
and `**accounting(cgroup)`, but the accounting dictionary also returned `scope`.
That call deterministically raises duplicate-keyword TypeError before entering
`emit` and before native `Popen`. The final event has the same collision through
the result identity's `scope` key. The generic handler did not retain the raw
exception; the exact empty-event boundary and synthetic original-code assembly
reproduce this deterministic defect. This failure supplied no native start.

Per lead's bounded correction release, one driver dictionary key changed:
`scope` to `scope_accounting`. Identity `scope` remains the unit-name string;
counter contents, preconditions, command, scope policy and startup behavior are
otherwise unchanged. Command/observer documentation now names the two fields.
Original driver `2473cac0...`, documents, receipt, effects and empty event bytes
are preserved in `history/w6j9bzb-activation-failure-20261026T151600Z/`, together
with the one-line driver diff.

Focused checks evaluated the actual original/corrected accounting return and
initial/final/snapshot call ASTs using synthetic counters and identity only.
Original initial/final events both reproduced the duplicate-scope TypeError;
corrected initial/final/snapshot events all assemble successfully and preserve
identity plus every counter. Python AST, three shell blocks and four output
filter cases also pass. Neither driver main nor native invocation was executed.
See current `activation-static-checks.json`.

- Corrected driver SHA-256: `1830a590031e71156d7ae35539c408bb7b2861cab31e06d2da99e0e215aa2d5a`.
- Command document SHA-256: `5b7ae4351b2ff6a2c349a153501a32e5e05f55e9600b937f4e023f11f7db20ee`.
- Observer brief SHA-256: `cc0d861b9145a9293f062619fd79b44dc109cc447f34f5338bc2585a73bea2e7`.

No execution-flag diagnosis, observer, retry, scope/guest stop, reset, host policy,
provider, application/source/lock/ref, foreign hold, KB or lifecycle mutation was
performed. Parent retains startup ownership. A later intentional attempt must
use a fresh directory/scope and fresh ownership/capacity/IP checks; no new full
metadata check is justified by this diagnostic-only change itself.
