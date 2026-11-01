# Cancellation evidence review

**No Blocking, Important or Advisory findings in the added cancellation
boundary. The review gate is clear for verification of the final pinned
composition.** This does not certify deployment or the pending CI result.

Reviewed provider head
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`, incrementally against
`57dd01b1d860181e12aa7ccb37ecdeae8b2c08c5`, with complete-series history checked
from `11ec57d2203fc735696fe75a837d47da55a5c6af`. The incremental diff contains
only `codex/client.go`, the focused regression in `codex/send_admission_test.go`
and `docs/reference.md`. Provider worktree is clean; complete-range
`git diff --check` passes.

## General and risk assessment

The deferred wrapper at `codex/client.go:1054` preserves an existing failure and
a caller context that has completed by the request's return. Go's two `%w`
operands retain both causes for `errors.Is` and `errors.As`. The original error
is first in the wrapped error tree. Existing context-bearing errors avoid an
extra wrapper, and successful requests remain successful because the defer
requires a nonnil request error. It neither changes response selection nor
replaces an RPC refusal with a cancellation-only error.

This appropriately addresses the observed race. Both retained CI logs show the
same existing `RetireThreadPersistedEmptyRootRefusesUnsafeEvidence/cancel`
failure: the request's disconnection response won while the retirement caller
expected cancellation identity. The fixture calls its local cancellation
function while handling `thread/loaded/list`; that public request crosses the
changed wrapper. The wrapper can therefore retain cancellation when the
disconnection branch wins, while preserving the disconnection diagnosis. The
local successful repetitions do not disprove this ordering race, and the fix
does not weaken the retirement fixture's assertion or archive safeguards.

Delivery classification remains governed by positive admission/ledger evidence:

- Before admission, `unwrittenSendOutcome` checks current shared send/queue
  state with the original normalized options. An advanced uncertain attempt
  remains uncertain; an accepted receipt can still be recovered.
- After a possible mutation write, transport failure still enters conservative
  reconciliation and returns an unknown outcome unless acceptance is proven.
- Explicit permitted RPC refusals remain discoverable through `errors.As`,
  including when cancellation is also present. That positive refusal, rather
  than cancellation, justifies restoring prepared state.

Adding `context.Canceled` or `context.DeadlineExceeded` to a generic request
error does not create `MessageNotSentError`, change the `admitted` flag, alter a
ledger transition or authorize replay. The documentation states that
cancellation alone is not proof of non-delivery. HTTP shutdown/deadline and
browser-cancellation lifetimes are unchanged.

## Architecture, scope and consumers

The public request/admitted-request wrapper is a suitable single owner for
this error-chain contract. It covers ordinary `Request`, the changed send
path, and failures during connection establishment without duplicating policy
in the retirement consumer. Lower-level connection-specific helpers retain
their existing behavior; this change does not claim a new lifetime or
cancellation policy for every private helper.

I inspected representative provider RPC/transport classification and the
runtime's retirement and observation consumers. They use `errors.Is` and
`errors.As`, which traverse this error tree. Transport and exact RPC identities
remain available, and no observed consumer turns generic cancellation into
permission to send again. The addition is bounded by an observed failure and
does not introduce a retry framework or protocol change.

The deterministic test at `codex/send_admission_test.go:14` verifies the precise
new wrapper invariant: a cancelled admission failure retains both the original
transport identity and cancellation, while its noncancelled control retains
only the original failure. It also checks that refused input does not reach
the peer. The test does not recreate the particular response-channel/socket
ordering from CI; that remains an appropriate responsibility of the existing
retirement fixture and the final runtime CI run. Successful-response behavior
is also directly protected by the defer's nonnil-error condition.

## Prior remediations and history

Under the narrow-fix policy I inspected the F1–F3 corrections retained from
`57dd01b`: shared state is rechecked on unwritten exits, the original nonzero
options digest is preserved, and positive history is adopted atomically without
using exclusive mutation admission. The cancelled/noncancelled losing-writer
matrix with uncertain/accepted winners and simultaneous history-recovery tests
cover the requested boundaries. These corrections are intact in the new head;
the cancellation addition does not reopen those findings. Unaffected UI review
was not repeated.

The complete provider series remains **one consolidated functional commit**.
No obsolete intermediate source approach, follow-up fixup commit or repeated
dependency stream remains in that range. There are no provider pin updates to
consolidate. Runtime, configuration and composed-workspace selections are
being refreshed mechanically and are not certified by this report; their final
identities must match the accepted provider/runtime and their update streams
must remain consolidated.

**Migration lineage: no migrations.** The native protocol, schema-3 submission
ledger and successful receipt formats remain unchanged. The only additional
public behavior in this incremental diff is the documented compound error
identity when a failed request and completed caller cancellation coexist.

## Verification limits

Reviewer remains independent `/root/final_review` under the existing
`gpt-6.1-sol/xhigh` policy. I read the corrected packet, design addendum, current
state, prior reports, relevant project guidance and mandatory review lane
references. Review used committed-source/history inspection, CI failure
evidence and quick diff checks. No source edits, long tests, nested reviewers
or deployment were performed.

The reported quick send/shared-ledger/history/cancellation checks support
proceeding. Earlier packaged/native/browser successes bind the preceding
provider/composition; they do not establish final derivation equivalence after
this source change. Remaining work is to regenerate consistent Go/Nix/vendor
and downstream pins, run the applicable final package/CI and composition
checks, then perform the authorized deployment and live verification. In
particular, collect a final runtime CI result for the retirement failure
instead of relying solely on local repetitions or the admission regression.
Merge authorization remains conditional on successful deployment and
verification first.
