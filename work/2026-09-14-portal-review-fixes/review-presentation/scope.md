# Scope and proportionality review

No Blocking, Important or Advisory scope findings.

Reviewed the committed follow-up series in `dev-workspace`,
`b837f0d974a98857daef7e4cc09d8f3039a059a0..774db1205a0cd653b687cec34e788eabd6a9f1c1`,
the organization pin delta `f6050a4..109e9de`, and workspace package pins
`1c3f3e1..a24742a`. Read the review packet, initiative plan/state, local
instructions, related browser tests, the existing editor reveal operation,
and the archival CLI/API contract. The previous deployed implementation and
intervening workspace coordination commit were treated as baseline context.

- `28a49ea` limits sticky headings to the existing file sections. Path
  truncation retains title, accessible name and copy access. The scroll
  correction handles the space occupied by the portal's own header after
  delegating line revelation to the existing editor; it does not introduce a
  second editor or Git projection mechanism.
- `88955af` reuses the existing compact sidebar styles and native popover.
  Its optional mount callback has a current shell consumer and communicates
  only comparison visibility. There is no preference store, fullscreen mode,
  general layout framework or unrelated navigation behavior.
- `774db12` keeps archival interpretation in a small browser adapter. Its
  recognized blockers match current CLI output; unknown command failures
  retain their diagnostics. Keeping the last successful response and ordering
  reads around the existing hold write directly support the requested failure
  behavior. Worker decisions, fingerprint inputs, stored formats and API
  handlers remain unchanged.
- The three commits remain independently understandable, with associated
  coverage. The added browser fixture reuses the existing Go server harness;
  the tests exercise owned presentation behavior rather than reimplementing
  browser, Git or CLI conformance checks. Downstream changes only select the
  reviewed runtime and organization revisions.

Residual validation: browser and integration acceptance is intentionally still
pending. It must establish sticky boundaries and linked-line placement in both
engines, plus compact sidebar/popover behavior. Shared index-template styling
also merits a narrow-screen smoke check because the compact CSS selectors were
moved out of the media query. No long tests or deployment were run by this
reviewer.

Risk: Medium. Lane: Scope and proportionality. Reviewer: gpt-6-astra, xhigh.
