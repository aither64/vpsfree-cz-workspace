# API-guide documentation follow-up: GENERAL review

## Reviewed scope

- Lane: GENERAL
- Model/effort: gpt-5.6-sol, xhigh
- Initiative: `2026-09-13-auth-email`
- vpsAdmin implementation checked at production head
  `ddd01f59ca533c030f29b9b8a75984699e5dc581` (base
  `791ab3aa89e2f613979da6090b89785c78245db5`)
- vpsfree-kb-contracts checked at
  `4ccc913036b3e904b9a24d2a5808f0ca6170836a` (base
  `919577d0c770e47b623c591f8bf0cce4e8d30666`)
- Local review artifacts: the Czech and English API source/candidate pairs,
  `kb-annotation-plan.yml`, `kb-candidates/review.md`, both schema-5 release
  manifests, `release-changes.yml`, `kb-impact.md`, and the prior account-page
  review

## Findings

No Blocking, Important, or Advisory findings.

## Review evidence

- The English addition at `kb-candidates/en/manuals/vps/api.txt:47` and Czech
  addition at `kb-candidates/cs/navody/vps/api.txt:52` accurately describe the
  implemented authentication contract. vpsAdmin starts an `email_code`
  continuation for applicable password-based token requests, retains the
  requested lifetime, interval and scope, and rejects HTTP Basic without
  starting an email challenge. Existing supplied tokens continue through the
  ordinary token provider and are not invalidated by this feature.
- The statements about applicability are suitably conditional. Email
  verification is effective only for an enrolled account with successful
  known-device history and without active TOTP/passkey MFA; the linked account
  pages explain those policy details. The API guide does not imply that TOTP
  and email verification are both required in one request.
- `vpsfreectl` is a supported continuation client: the released Ruby HaveAPI
  client used by vpsAdmin/vpsfree-client follows advertised `next_action`
  values and prompts for their advertised inputs, including the protected
  `email_code` field. The later guide sections already show how to save the
  resulting token. The Terraform provider accepts such a supplied token.
- The documented incompatibility is concrete and correct. The pinned Go
  `get-token` helper supplies only a TOTP callback; its generated client rejects
  the ungenerated `email_code` continuation with `Unsupported authentication
  action`. Both language variants name that helper and direct users to
  `vpsfreectl` as the supported issuance path.
- The Czech text uses informal singular forms and preserves the same technical
  meaning as the English text. DokuWiki links, inline code, headings and the
  surrounding command syntax remain intact. The two guarded edits introduce no
  WebUI action, so no additional `<vpsadmin-nav>` annotation is needed.
- Source-to-candidate diffs are limited to the two intended authentication
  sections. `kb-annotation-plan.yml:67-138` contains four exact, single-match
  guarded replacements corresponding to those deltas. The account-page
  candidates remain at the hashes covered by the prior GENERAL review.
- Both schema-5 manifests parse, their source and candidate SHA-256 values
  match the reviewed files, and all four localized summaries exactly match
  `release-changes.yml`. The expanded Czech and English releases each staged
  and verified two pages, with the exact revision summaries shown in
  `/tmp/auth-email-kb-expanded-cs-stage.log` and
  `/tmp/auth-email-kb-expanded-en-stage.log`.
- The contract commit remains one cohesive documentation commit after its
  vpsAdmin pin was advanced from the already reviewed implementation head to
  the narrow follow-up fix at `ddd01f59c`. Both contract workflows passed at
  `4ccc913` as recorded in the packet. The API-guide candidates and guarded
  release records are coordination artifacts whose exact hashes provide the
  review boundary; they introduce no additional project-code commit.

## Residual risks and gaps

- This review did not publish to production. Production promotion still needs
  direct user approval.
- The existing unrelated all-page annotation drift recorded in `kb-impact.md`
  is outside this follow-up. The API guide's pre-existing language-marker and
  navigation-tag state is unchanged by the guarded authentication edits; the
  bilingual staging verifier successfully resolved both page pairs.
- Runtime authentication behavior was already covered by the implementation
  review. This follow-up inspected the implementation and client sources only
  as needed to verify the new public claims and did not rerun those suites.
