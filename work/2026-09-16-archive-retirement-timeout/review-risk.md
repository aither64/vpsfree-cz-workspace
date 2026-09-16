# Risk and compatibility review

No findings.

Reviewed directly with gpt-6-astra/xhigh: dev-workspace
`eb658d49e6b8182d5fc07ab98bc897c58490baa9..a65583d45b707eb23feb7d490ba177e8360dfb8d`
(both functional commits), vpsfree-dev-workspace
`17da396e7fea5d4e31d4af1382da00fe4d140e17..1a0bc7db6c968bde9cb9ecbd737d8b1b6f28de44`,
and workspace
`f8d6217a8a6e83bd317a7bef166aa650806ca553..3610be86615b8710b2e1bfe8a53b9771bad15fdf`.
Read the packet, plan/state, local AGENTS, changed tests/docs and relevant
lifecycle, worker, operation-state, packaging and activation consumers.

- `5deb10c`, `libexec/dev-session:4970`: retirement overrides the worker's
  per-command timeout only inside the existing `with_timeout` scope. Its
  `ensure` restores the prior value on success or error. The 210-second limit
  surrounds the existing 180-second Go deadline; ordinary worker commands
  retain their 60-second limit. Packaging already supplies GNU timeout.
- Retirement still uses authoritative directory discovery, ambiguity rejection,
  exact thread identity, idle checks and the existing archive journal phases.
  Error wrapping preserves the underlying cause through `%w`. Retry from
  `tracking_committed` still verifies committed tracking and retained identities
  before retirement, without another tracking commit.
- `a65583d`, `portal/internal/web/static/app.js:775`: historical failures require
  the same journal and conversation identities, a failed worker result and a
  valid timestamp. Text is rendered through `textContent`. Refresh failures
  preserve the last record, and the refresh guard avoids replacing a running
  lifecycle monitor. No mutating endpoint or read-only boundary changed.
- Consumer diffs update only the intended runtime/extension revisions. Codex,
  codex-web, runtime contracts, manifests, journals and sidecar schemas are
  unchanged. Previous packages can read the same state. Existing switch and
  rollback paths reject pending lifecycle journals; recovering the exact
  source archive with the installed manual command before switching matches
  that constraint.

Residual risks and verification limits: authoritative history discovery can
still exceed 180 seconds and fail safely; lookup optimization is an explicit
non-goal. Reviewed the subprocess deadline/retry, error-stage, identity-filter
and browser fixtures and the reported quick-check results; did not rerun them.
Packaged tests, real-browser execution, isolated acceptance, live source archive
recovery and deployment verification remain the coordinator's planned
post-review work. This review does not claim those operational steps succeeded.
