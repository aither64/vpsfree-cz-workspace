# General documentation review

## Reviewed scope

- Lane: GENERAL
- Model/effort: gpt-5.6-sol, xhigh
- Contract repository: `vpsfree-kb-contracts`
- Base: `919577d0c770e47b623c591f8bf0cce4e8d30666`
- Head: `656d0524f76f2078fb16a8a789a55405f6aba7e5`
- Downstream implementation checked as needed: vpsAdmin
  `f7a4b68d8695f0958a2badd4e1897915d98cdcae` (API
  `24d7897a2a56c061831de7d6d3ecac12c02c3ef3`)
- Local review artifacts: the two bilingual account-page candidates,
  `kb-annotation-plan.yml`, `kb-candidates/review.md`, both schema-5 release
  manifests, and `release-changes.yml`

## Findings

No Blocking, Important, or Advisory findings.

## Review evidence

- The range contains one clean, cohesive documentation commit. The semantic
  WebUI control/path, bilingual page bindings, capture/page revision metadata,
  and exact flake pin depend on the same reviewed vpsAdmin head and are
  reasonable to review and revert together. The commit message describes the
  final result and rationale.
- The final lock-file diff changes only the intended vpsAdmin input. The
  vpsAdminOS revision remains `6bdf458fd9105379860234ff33d352e55844f08f`,
  and no screenshot bitmap, capture scenario, or runtime logic changed.
- The semantic landmark and localized labels match the pinned WebUI source:
  `member.email-verification` identifies the **Email verification** /
  **Ověřování e-mailem** profile section. The path correctly composes
  `member.edit-profile` and that landmark.
- Manual enumeration of the added instructions found one WebUI action in each
  candidate: enable the preference in the email-verification profile section
  and enter the current password. Each is wrapped once in
  `<vpsadmin-nav id="member.email-verification.open">`, and the contract binds
  that count to the affected language page. The remaining added instructions
  concern email delivery, codes, API authentication, and recovery choices and
  do not introduce another WebUI navigation action.
- The Czech and English additions state the same behavior. Source inspection
  confirmed the effective-MFA exception, successful known-device history,
  retained expired/revoked history, primary-address delivery, fixed 30-minute
  deadline, replacement-code invalidation without extension, three total
  sends with a 60-second interval, five failed codes, shared account/IP
  budgets, password-token continuation, HTTP Basic refusal, and unchanged
  existing sessions/tokens/refresh/valid SSO behavior. Self-service preference
  changes require the current password.
- The accepted Go `get-token` incompatibility is explicit in the vpsAdmin
  rollout guide together with the HaveAPI CLI replacement. The public account
  pages accurately direct unattended clients to an existing supplied token and
  do not claim that the Go helper supports the email continuation.
- Candidate construction changed exactly the Czech and English account pages.
  Their reciprocal `<page>` marker is preserved. Candidate and source hashes,
  source revisions, page IDs, policies, and localized summaries agree with the
  two release manifests and the all-page candidate index.
- `git diff --check` passed for the reviewed range. The packet records the
  repository's full `bin/check` result at this head, including contract,
  annotation, managed-page, sample, and 120-PNG inventory checks.

## Residual gaps

- This lane did not stage or render the candidates in DokuWiki. Staging and
  manifest verification remain the next reviewable publication step;
  production is unchanged and still requires explicit approval.
- The four pre-existing annotation mismatches listed in `kb-impact.md` affect
  unrelated pages and were intentionally excluded from this feature review.
- Runtime behavior and production templates were reviewed in the upstream
  implementation review. This downstream lane spot-checked only the sources
  needed to validate the documentation claims and did not rerun that review.
