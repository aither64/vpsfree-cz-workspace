# R2 compatibility source audit and replay disposition

## Final finding disposition and correction release

P2 is complete; reviewer0 independently inspected the finite receipts. Its final
addendum upgrades Unicode normalization drift to **Important**: U+0661 PID can
create an extra kernel alert; NBSP namespace and LXC trimming change labels.
Raw FF in the nodectld body also proved a concrete missed crash flare/count under
the explicitly chosen whole-record UTF8 rejection policy. Producer passage or
production occurrence was not established, but a UTF8-only producer guarantee
was not established either. Leading-colon LXC slicing is a separate Advisory.

User now explicitly authorizes corrections. D7 is accepted and I3 is executing:
restore ASCII regex/strip semantics and the legacy colon-zero rule; validate real
headers strictly while replacement-decoding invalid body bytes once. Preserve
U+FFFD rather than deleting bytes, document possible body-label coalescence, and
expose one fixed decoded-body counter. No universal byte-label equivalence is
claimed. Existing first-record, malformed-header, framing and monotonic fixes
remain. R3 affected final review follows the committed quick-pass successor.

Normal kernel[], leading-MSG-space/OOM and fresh isolated svlogd controls match.
The earlier mixed svlogd delta was prior-flare contamination, resolved by one
fresh control. Both exact user records match only at the replayed FIFO-input
boundary, not as a reconstruction of the historical entire logging pipeline.
All six P2 services and known tool effects were reaped; a preserved session-lock
stop refusal was reconciled by the exact own-unit stop retry. No production
message, source change or deployment occurred in P2. The accepted final table is
[parser parity](parser-parity.md), with compact fixtures/results under p2-artifacts/.

The following source-audit text preserves the earlier provisional assessment;
its pending/advisory wording is superseded by this final disposition.

## Report identity and scope

Lead record of reviewer0's bounded user-requested source audit; the original full
report remains in this session's conversation. Reviewer retained
`gpt-6.1-sol/xhigh/read_only`, native thread
`01a1c742-93c5-7c50-b59e-f792fafd9624`. General/risk lanes; prior unchanged
architecture/scope/history review retained. Ruby baseline is
`7c5a8e74e44a704cceb99cd05716af6800d78efd`, Rust deployed source is
`6ecada0a9d2f6457a11031a3a4ffc341584fb29c`; consumer remains
`ebe9248d7f57f1cec22089d40432aa95b3b93f60`. No source change, build, service,
production access or executable campaign was performed by the reviewer.

No Blocking or Important unintended regression in normal canonical records was
established by the source pass. This is not universal equivalence. I1/P2 owns
finite executable confirmation; architect0/D6 owns intended-boundary
classification. The exact user-record/positive-control results below now have P2 executable
proof; advisory edge outcomes remain pending the second bounded replay. No
source correction has yet been authorized from these findings.

## Exact user record and tokenization

The supplied line starts with outer timestamp, configured canonical host and
program `1`; the RFC5424 timestamp/FQDN/kernel header is inside its message body.
Old `lib/syslog-exporter/parser.rb` next_value uses literal String#index(' ') and
slices; new `src/parser.rs` uses split_once(' '). Neither recursively unwraps
this nested RFC5424 form. Old Kernel collector and new collectors.rs require
exact program kernel. Both are therefore expected to count the known-host record
under program1 and leave the kernel bug gauge unchanged. A same-host outer
kernel positive control should set it. This does not contradict the user's
successful direct TCP and later /dev/kmsg alert tests.

The lead's whitespace-collapse hypothesis was refuted. Ruby does not use AWK
String#split here. With two spaces after kernel, both bodies retain one leading
space; both anchored namespace recognizers miss it and both OOM substring tests
still match. Extra empty fields inside the required header differ: Ruby's
zero-index slice can manufacture odd fields, while Rust rejects empty required
fields. This belongs to documented malformed-field handling, not normal trimming.

## First executable replay (accepted evidence)

P2 ran actual retained Rubyw7 and deployed Rust3hk with the copied67host config,
private FIFOs/listeners, controlled warmup and marker drain barriers. Both233byte
user records produced exactly one syslog_message_count{program="1"} increment,
and null-pointer gauge0→0, in BOTH applications. All legacy deltas matched.
The direct outerkernel/FQDN positive produced gauge0→1, one kernel-message count
and one programkernel count in BOTH. User-record SHA256s are
b1b4c7cfcac9c082644422f5ea8daf42a11442253102c2be57185132938ea12c and
1cf90f3e892ad8b5d95275587799dee7f3ffc3e8ec8e30dcdf9b10b796431015.

A separately measured initial complete frame had Ruby0/Rust1, isolating the
intentional first-frame fix. The three comparisons followed warmups. Both exact
registered services ended MainPID0/empty cgroup; scratch removed and watcher
cells joined. Runtime22.243s. R0 independently inspected the compact receipt:
[p2 first replay](p2-artifacts/first-compact.json). This verifies these samples,
not arbitrary input equivalence. No production action or source edit occurred.

## Advisory edge differences and unresolved encoding boundary

| ID | Source difference | Expected effect / evidence needed |
| --- | --- | --- |
| A1 | Rust regex numeric/whitespace shorthand classes have Unicode semantics; corresponding Ruby classes are ASCII | Arabic-digit kernel PID can normalize to kernel only in Rust; NBSP in a namespace can be consumed only by Rust, changing syslogns. Also applies to the svlogd numeric recognizer. No affected live producer is established. |
| A2 | Ruby String#strip and Rust str::trim accept different whitespace sets; LXC colon-zero slicing differs | NBSP around an LXC id can remain only in Ruby. Leading-colon body gives Ruby its entire stripped body as id (slice0..-1), Rust empty id. Ordinary numeric-prefix and colon-free behavior agrees. |
| Q1 | Rust rejects any record containing invalid UTF8 before routing; some Ruby paths use only byte-compatible substring matching | A valid header/nodectld body `Daemon crashed ` followed by byte255 may count and flare in Ruby but be rejected by Rust. Other Ruby regex paths may instead fail. Pinned rsyslog high-byte preservation does not prove UTF8-only messages. |

Exact candidate vectors sent directly by R0 to P2 include:

```text
2026-11-11T12:00:00Z KNOWNHOST kernel[١] BUG: kernel NULL pointer dereference
2026-11-11T12:00:00Z KNOWNHOST kernel [ <NBSP>ns ] ordinary
2026-11-11T12:00:00Z KNOWNHOST lxc <NBSP>42<NBSP>: Failed to spawn container "42"
2026-11-11T12:00:00Z KNOWNHOST lxc : Failed to spawn container "42"
```

NBSP denotes actual U+00A0; invalid-byte replay must use byte0xff, not its printed
escape. Reviewer references: old parser.rb PID regex and next_value:89–94,
kernel_message.rb namespace extraction, collectors/lxc_start.rb id slice/strip;
new parser.rs:5–9,18–22,29–46 and collectors.rs:181–183.

Invalid UTF8 rejection was an explicit design choice, so Q1 was not classified
as an undisclosed Important regression. It remains a real limit on the broader
claim that every rsyslog record Ruby accepts is accepted by Rust. Concrete
required producer content must not be dismissed by retroactively calling it
unsupported. P2 must establish actual effects before a source-policy decision.

## Normal behavior inspected

- Exact configured-key/FQDN host matching, first-config collision selection,
  alias as output label, no DNS/case folding/auto-add; unknown hosts ignored.
- ASCII PID stripping and retained colons; accepted kernel forwarded/PID fixes
  are distinct from recursively interpreting nested protocol headers.
- All kernel signatures and precedence: nullptr, unregister_netdevice, GPF
  traps exclusion, conntrack, OOM; namespace counter; independent ZFS detection.
- LXC OS/program gates, netns-before-spawn ordering, prefix-derived id.
- Nodectld OS/program gate and crash/segmentation/incremental precedence.
- Osctld OS/program gate, command-before-internal-error ordering and optional
  final LF matching Ruby's end anchor for framed single-line input.
- Opt-in WebUI nginx/FastCGI and first matching error class, one update per line.
- Flare test on every host, same15s; same240/180s other flares, renewal, retained
  zero series and no PID/cross-line correlation. New monotonic single-owner
  expiry fixes wall-clock/reset races without changing intended durations.
- Eighteen legacy family names/HELP/types/label sets and normal startup/creation
  lifecycle, supported by finite actual Ruby goldens. Both reset on restart and
  retain dynamic series; neither has total bounded metric cardinality memory.

## Explicit decisions and remaining limits

Accepted R/D documents: first complete line processed; per-record rejection for
malformed required fields/timestamps/UTF8; producer-backed RFC3339 subset;
safe kernel PID/forwarded normalization; 1MiB bound and EOF/shutdown partial-tail
drop; no unbounded message queue; monotonic ordered expiry; stronger config/FIFO
validation; capacity fallback, diagnostics and bounded HTTP admission. These
are intentional differences, not universal Ruby emulation. Date-only,
missing-zone/non-RFC3339 ISO inputs and unterminated EOF tails need explicit
support/producer evidence before their rejection can be called a regression.

Canonical producer support cannot certify arbitrary bodies or every Unicode
class/trim/encoding edge. Existing goldens did not cover all such cases or the
user's exact nested-header record. Shared producer loss, UDP, short writes,
unknown-host policy, no durable replay and retained cardinality are not new
Rust-only defects. No new broker, generic fuzzing/parser framework or hardening
campaign is warranted. The next step is the already dispatched finite P2 table
and lead/architect disposition of confirmed differences.

The source tree6ec equals prior reviewedfaf tree5d3e; current provider remains one
replacement commit. No new obsolete history, repeated pin stream or migration
was introduced. No migrations. Existing reference placement remains sound but
must be read with its explicit boundaries and finite fixture limits. Any
meaningful confirmed gap needs the smallest owning correction/fixture/reference
update after a lead decision. Source code is unchanged by R2/D6/P2 so far.

See [design D6](design.md), [current state](state.md), and the forthcoming
parser-parity.md for executable results. Deployment and machine hold remain
unchanged; both branches intentionally remain unmerged.
