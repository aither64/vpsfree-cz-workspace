# Scope and proportionality review

Blocking: none. Important: none. Advisory: none.

Reviewed the original recorded series directly, using the mandatory-change-review
scope lane, repository AGENTS.md files, initiative plan/state, commit messages,
implementation, tests, documentation and consumer configuration:

- dev-workspace: `eb658d49e6b8182d5fc07ab98bc897c58490baa9` through
  `a65583d45b707eb23feb7d490ba177e8360dfb8d` (`5deb10c`, `a65583d`).
- vpsfree-dev-workspace: `17da396e7fea5d4e31d4af1382da00fe4d140e17` through
  `1a0bc7db6c968bde9cb9ecbd737d8b1b6f28de44`.
- workspace: `f8d6217a8a6e83bd317a7bef166aa650806ca553` through
  `3610be86615b8710b2e1bfe8a53b9771bad15fdf`.

The retirement fix is proportionate to the demonstrated outer/inner timeout
mismatch. `5deb10c` scopes the existing CommandRunner timeout around the existing
retirement command (`libexec/dev-session:4970`); it relies on the runner's existing
ensure-based restoration and GNU timeout implementation. It does not introduce a
second process supervisor, change the archive transaction, or bypass authoritative
thread discovery. The additional Go stage labels annotate the existing control
flow without changing its identity, idle, force or archive decisions.

The portal change in `a65583d` uses the existing automatic-archive and lifecycle
status endpoints. Its small presentation function and page-local polling state
serve the requested timestamped failure banner, stale-identity rejection, retained
diagnostics during read failures, and coexistence with a live retry. The existing
lifecycle monitor still owns running operations. No generalized polling framework,
new journal fields, server API, or extra persistence was introduced.

The timeout subprocess and journal-resumption regressions exercise the application
boundary that failed. The presentation, template and optional real-browser checks
cover the new warning and asynchronous refresh behavior without attempting to
reimplement upstream timeout or Codex conformance suites. The two functional
runtime commits and separate generated consumer pins form a coherent series.
Both consumers change only the runtime selection needed for the authorized
user-profile deployment; host and system configuration remain outside the change.

Residual risks and review limits:

- Authoritative history lookup can still exceed its 180-second client deadline.
  The approved scope explicitly accepts bounded failure and recovery instead of
  lookup optimization; this is not a reason to widen this implementation.
- The packet records successful quick checks. Real Chromium/Firefox execution,
  packaged checks, isolated archive acceptance, source-session recovery and
  deployment remain the coordinator's post-review verification. This review
  performed static inspection and did not run those operations.
- Concurrent later doc/test remediations are outside these recorded commit heads.

No code or configuration was edited, and no subagents were launched.
