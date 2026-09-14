# Risk and compatibility review

No additional findings. No Blocking or Important issue found in the committed
presentation follow-up.

Reviewed dev-workspace `b837f0d974a98857daef7e4cc09d8f3039a059a0` →
`774db1205a0cd653b687cec34e788eabd6a9f1c1`, including each of its three
commits; vpsfree-dev-workspace `f6050a4d661be7c923518e0b962a4372ebad7f50` →
`109e9ded49d9b336a25f44ebfdbe19e5ed598b90`; and the workspace package-pin
delta `1c3f3e156cad0f84090ec1934acbb867eb723345` →
`a24742ab2e999cabafe81926a4271af436546b19`. The workspace's intervening
coordination checkpoint is outside the presentation implementation. Codex-web
remains unchanged at `882c88ccfbebfb646fb2cafbe9bc6790141b2d13`.

## Compatibility and security evidence

- The runtime changes browser assets, one matching template, and tests. There
  are no CLI, HTTP schema, lifecycle journal, archival sidecar, fingerprint,
  retention, Codex protocol, or package-transition contract changes. Existing
  state remains readable by the previous deployed package.
- The Keep open POST still sends the existing explicit boolean and lifecycle
  target ID. The unchanged server retains origin enforcement, request bounds,
  exclusive transition locking, current package-generation checks, archived
  session rejection, and exact lifecycle-target validation. Client read
  generations prevent a read started before the hold operation from replacing
  its newer result; the server remains authoritative for persistence.
- Archival diagnostics and repository paths are inserted with DOM text APIs.
  Raw command failures remain escaped inside the disclosure. The conditional
  merged-tier label agrees with the worker: merge proof is deferred until an
  otherwise eligible candidate is checked. The browser does not authorize or
  initiate automatic archival.
- `onComparisonChange` is an optional internal mount argument. The discovered
  consumers are the portal shell and the repository acceptance fixture; the
  latter can omit it. Routes, editor inputs, saved comparison choices and API
  responses remain unchanged. Shared session/index limits markup continues to
  use its existing popover control.
- Both consuming flakes pin the exact reviewed runtime through the organization
  extension's `lib.mkPackage`. No provider or unrelated dependency revision
  changes appear in the follow-up lockfile delta. Assets and templates are
  embedded in the same portal package, and the server applies `Cache-Control:
  no-store` to static responses. The documented user-profile switch and retained
  previous generation provide the existing deployment/rollback path without
  default-branch integration or host/node coordination.

## Residual risks and verification limits

- Chromium/Firefox acceptance and packaged/deployed checks are intentionally
  pending this review. They must verify sticky boundaries and linked lines in
  all views, sidebar transitions, limits popovers, and archival failure/hold
  states. No long browser or integration tests were run by this reviewer.
- Existing documents retain their loaded shell and CSS while the repository
  module is loaded lazily. A document spanning a package switch may temporarily
  mix presentation generations; the optional callback preserves compatibility,
  and a reload is needed for the full updated presentation. This introduces no
  persisted-state or mutation-contract mismatch.
- Delayed GET-versus-POST ordering and a failed hold followed by a failed
  read-back are useful focused coverage for the new client sequencing. The
  committed fixture covers successful holds and failed reads/posts separately.
- Uncommitted edits appeared after the committed source was inspected. The
  coordinator identified them as the General lane's narrow diagnostic
  remediation and browser assertions; they are excluded from this report.

Method: direct inspection of the review packet, plan/state, local AGENTS.md
files, committed diffs and history, consumer flakes, server routing/security
headers, archival API/worker, renderer consumers and browser fixtures. Lane:
Risk and compatibility; model `gpt-6-astra`, reasoning `xhigh`.
