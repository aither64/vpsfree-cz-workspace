---
lifecycle: active
---

# 2026-09-13-auth-email

Implementation and production mail templates are committed, reviewed and pushed.
The focused browser integration passed, and all API topic jobs and coverage
checks passed on the final production code. All four account/API documentation
candidates are staged and verified. The final exact documentation pin is pushed. Its CI and the broader
vpsAdmin integration CI run are still in progress.

No default-branch integration, production deployment or KB publication has been
performed. The session and staging remain open for follow-up.

## Repositories

All feature branches are `2026-09-13-auth-email`. Worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-13-auth-email/`, and all
three repositories are registered in `portal.yml`.

| Repository | Base | Current head |
| --- | --- | --- |
| vpsadmin | 791ab3aa89e2f613979da6090b89785c78245db5 | 1b82f44b88663b9a50e82012c1e77f561b294bc5 |
| vpsfree-notification-templates | f944ba03eba5d0d6b58b7eb856f251d1c96f2c11 | 06f03bad4294b6f28ca9478e907f43967ebeb7d0 |
| vpsfree-kb-contracts | 919577d0c770e47b623c591f8bf0cce4e8d30666 | cdc4fa967ad1b8e9daa665e6760db624e736c1fd |

vpsAdmin commits: API `24d7897a2a56c061831de7d6d3ecac12c02c3ef3`, WebUI
`f7a4b68d8695f0958a2badd4e1897915d98cdcae`, and CI regression correction
`ddd01f59ca533c030f29b9b8a75984699e5dc581`, followed by browser test isolation
`1b82f44b88663b9a50e82012c1e77f561b294bc5`. Fetches before pushing found the
recorded upstream bases unchanged. Feature branches remain unmerged.

## Accepted scope and implementation

Implementation authorized on 2026-09-14. User additionally required production
notification templates in `vpsfree-notification-templates`.

- Default-off account preference and separate default-off enrollment gate.
- Correct password, no effective active TOTP/passkey, historical successful
  known-device login, and no current trusted device: require email verification.
  Revoked or expired successful device history still counts.
- Fixed 30-minute challenge lifetime, five wrong attempts, three total sends,
  60-second resend cooldown and three pending challenges per account.
- Shared DB budgets: account five sends/15 minutes, 20 sends/day and ten wrong
  guesses/15 minutes; IP 60 sends/15 minutes and 100 wrong guesses/15 minutes.
  Fixed UTC windows. Resend rotates the code without extending its lifetime or
  resetting guesses. Bcrypt hash in authentication state; normal full
  administrator-only mail/queue history retained by explicit design.
- Primary recipient only. Bilingual built-in and production notification
  templates include the code, expiry, IP, client and support contact.
- Current-password reauthentication for self-service changes, including a
  self-admin; audited administrator override for another account. No separate
  enrollment email. User creation cannot bypass the enrollment gate.
- Password API token issuance supports `email_code` / `email_resend`; Basic
  rejects without sending mail. Existing supplied tokens, completed sessions,
  refresh and valid SSO retain their supported behavior.
- OAuth binds the challenge to the browser and authorization context, then
  rechecks security generation and device evidence under the user lock before
  authorization and code exchange. SSO uses device evidence too. Invalid SSO
  evidence returns the credentials form for password/email authentication.
- Security changes invalidate pending authentication, including password,
  primary email, preference, MFA, token/Basic/OAuth/SSO settings and lockout.
  Completed sessions are retained unless the existing operation signs them out.
- Email-verified forced password reset receives a fresh five-minute continuation;
  late verification renews browser binding without extending the email challenge.
- User API metadata, English/Czech UI strings, semantic profile landmark,
  challenge form, maintenance cleanup, schema and regression tests are included.

## Compatibility and deployment

Deploy additive schema and both template sets before enforcing API workers.
Update every API worker, then WebUI, then enable new enrollment. The gate
controls enrollment only; opted-in accounts remain enforced when it is closed.
Old workers and application rollback lose enforcement. Keep the new API version
while users remain opted in. The additive migration has a tested rollback; no
node protocol, daemon, vpsAdminOS or coordinated node update is needed.

HaveAPI Ruby CLI callbacks were confirmed in the installed client and fetched
`a52769871096e45bf443767bb1a79546857784ae`. PHP client
`0f5f9dad0ff445bdd36c776390ce4c8e8415444e` accepts generic continuations.
Terraform `8e205a3b4b87160a42e69de63c28653d226e65c2` consumes a supplied token;
its separate Go `get-token` helper and pinned Go client cannot answer the new
email continuation. The explicit compatibility boundary is documented in
`doc/email-login-verification.mdwn`, with the HaveAPI CLI as the issuance
replacement. Communicate it before enrollment; do not silently fall back to
password-only authentication. No Go/client repository is added to this scope.

## Quick verification

All intended changes were committed and quick checks passed before mandatory
review and long integration testing.

- Auth/mail/concurrency: 105 examples, zero failures.
- Shared MFA/password policy: 34 examples, zero failures.
- New profile/email-flow cases: 15 examples, zero failures.
- Additive migration/default/unique bucket/rollback: two examples, zero failures.
- Review regressions: seven SSO, seven shared-budget, two Create, one unknown
  flow, one SSO-disable and five SSO fallback/revocation examples passed.
- Budgets include account and IP limits, UTC rollover and independent database
  connections competing for the final shared IP slot.
- Ruby lint, PHP syntax, gettext health/compilation, Playwright JS syntax and
  WebUI Nix parsing passed. All commit hooks passed.
- Built-in template validation: 55 templates / 177 files. Production template
  flake checks passed after new files were staged.
- CI selector: 16 tests / 55 assertions passed. Original recursive API topic
  patterns cover all 406 non-migration specs exactly once.

## Mandatory review and reconciliation

High risk because this changes authentication, persisted state, API contracts
and rolling-upgrade behavior. All four standalone lanes used fresh
`gpt-5.6-sol` agents at `xhigh`, with no nested agents. Reviewed API commit
`2b5ba9d46f8ee7e5a6187b5b35d65c34289092b4`, WebUI/head
`3c24a6aadacb054732a2a22214c98e3edb03ef5c`, and production templates
`06f03bad4294b6f28ca9478e907f43967ebeb7d0`. See `review-packet.md` and the
four lane reports.

- GENERAL/SCOPE Blocking: unconditional SSO evidence bypassed device checks,
  including revocation/expiry and the first-device race. Replaced it with
  ordinary device evidence, preserving device ID through authorization-code
  exchange. Added valid, revoked, expired and unknown-device regressions and a
  credentials-form fallback before authorization.
- GENERAL commit-series finding and SCOPE advisory: reverted the unnecessary
  API topic glob rewrite; original recursive coverage already includes new files.
- ARCHITECTURE Important: documented the unsupported Go helper boundary and
  supported HaveAPI CLI replacement described above.
- ARCHITECTURE Important: added public preference/enrollment-gate descriptions
  and Czech parameter metadata.
- ARCHITECTURE Important: browser tests need HTTPS for Secure cookies. Added a
  test-only authentication certificate and HTTPS navigation for the new scenario;
  production cookie security remains unchanged.
- ARCHITECTURE Important: added shared account/IP/window/concurrency coverage.
- RISK Important: excluded enrollment from User Create and included SSO-setting
  changes in pending-authentication generation invalidation.
- ARCHITECTURE advisory: reject unsupported email flow values explicitly.
- Accepted display advisory: WebUI retains its currently equivalent MFA display
  calculation already used by other profile sections. API policy is authoritative.
- Accepted SCOPE advisory: label-only factor edits conservatively invalidate
  pending authentication for opted-in users. A concurrent login may need restart.

All Blocking findings are fixed. Important findings are fixed except the
explicit documented Go helper compatibility boundary. Direct remediations and
regressions stay within the reviewed behavior; no new design or public contract
required reviewer reruns. Fixes were consolidated into the final API/WebUI
commits before integration began.

## CI failure investigation and correction

First vpsAdmin push was `f7a4b68d`. API topic run 34832422263 failed routes
(core/full jobs 103938579030/103938579190) and engine (core/full
103938579082/103938579264). Downloaded and inspected the failed logs before
correcting anything; no blind rerun was used.

1. Recovery route tests still expected pending OAuth authorizations/codes to
   survive a password change. Updated them for the accepted invalidation policy,
   and explicitly proved completed OAuth sessions/SSO and ordinary token sessions
   survive when signing out other devices is not selected.
2. Recovery model tests exposed a real cached-association bug: an earlier empty
   `User.auth_tokens` load let a later invalidation skip newly created tokens.
   `auth_tokens.reload.destroy_all` fixes the sequence.
3. Global rate-bucket assertions picked up rows left by independent-connection
   examples. Isolated the table before those examples and retained explicit
   cleanup for independently committed data.

Combined recovery/challenge/budget regression suite: 62 examples, zero failures;
three changed Ruby files lint clean. Committed as `ddd01f59c`, pushed, and
cancelled only superseded non-completed runs 34832422359 and 34832422263 on
this feature branch. This is a narrow correction within the reviewed behavior;
no reviewer rerun needed. See the pending-authentication association-cache note.

API topic run **34833870974 passed all 27 jobs** (26 topics plus coverage)
at `ddd01f59c`. The `api/` and `webui/` production trees at the final test-only
head `1b82f44b8` are identical to that tested commit. Minimal durable job
results are in `ci-api.json`. RuboCop 34833870880 and i18n 34833870885 also
passed. At the preceding head, migration 34832422273, WebUI PHPUnit
34832422415 and libnodectld 34832422271 passed; these components were untouched
by the later browser-test commit.

Production template Check passed at its final head (34832373122).
After pushing `1b82f44b8`, cancelled only the superseded still-running
integration run 34833870928. Current integration CI is **34838666221** and
is running on `1b82f44b8`. Its test selection includes the new focused target.
Never cancel runs on the current head.

The long API platform jobs were healthy: the prior successful upstream run
34773269845 took about 29/40 minutes for core/full, and this full job completed
in about 42 minutes. Failed jobs were investigated as described above; no
blind reruns were accepted as validation.

## Browser integration

The two local `./test-runner.sh test 'webui#auth'` runs each passed all 24
existing browser scenarios. The new scenario exposed two test-expectation
mistakes, with successful application behavior before each assertion:

1. The logout label includes a dropdown marker. Used the existing helper's
   regex and 60-second timeout for all three successful-login assertions.
2. Successful enrollment notifications live in `#perex`, outside `#content-in`.
   Used the existing `expectNotification` helper and explicitly checked the
   enabled preference afterward.

Moved this initiative's scenario to `auth-email.spec.cjs` and added
`webui#auth-email` with the existing auth selectors. The old `auth.spec.cjs`
now matches the upstream base exactly. Metadata evaluation verified `ci`,
`auth`, `webui-auth` and `webui-auth-email` tags. JavaScript syntax, selector
checks (16 tests / 55 assertions) and all commit hooks passed. These bounded
test corrections do not change production behavior or the reviewed security
boundary; no reviewer rerun was needed.

**`./test-runner.sh test 'webui#auth-email'` passed at `1b82f44b8`.**
The example took 106.58 seconds; total run 740.95 seconds, completed at
2026-09-14 13:27:28 +0200. It covered first-device bootstrap, missing-password
enrollment rejection, successful enrollment, known-device reuse, an unknown
browser's challenge, resend throttling, wrong-code rejection, actual mail code
retrieval and successful completion.

Logs: `/tmp/auth-email-webui-integration.log`,
`/tmp/auth-email-webui-integration-retry.log`,
`/tmp/auth-email-webui-focused.log`. Test runner reused its owned deterministic
directory `/tmp/os-test-runner/os-test-webui-fd1a3b33`; automatic runner VM
lifecycle completed normally. Kernels came from cache; no local kernel build.

## Documentation and staging

Read and followed `vpsfree-kb-contracts/docs/webui-change-workflow.md`. Added
`member.email-verification` and `member.email-verification.open`, with Czech
and English account-page bindings. Existing screenshot crops do not include the
new section, so no bitmap regeneration was needed.

The exact vpsAdmin input is updated in all five required files. A normal Nix
input update also reset the KB repository's deliberate newer vpsAdminOS pin.
Restored `6bdf458fd9105379860234ff33d352e55844f08f` through Nix's nested input
override; the final lock diff changes only vpsAdmin. The dedicated note records
the command and rationale. Classified retry support remains available.

`nix develop -c bin/check` passed before documentation review and again after
pinning `ddd01f59c`: 46 controls, 37 paths, 96 bilingual bindings, four managed
pages, eight variants, 12 runtime bindings, 21 samples and 120 PNGs. Separate
GENERAL documentation review at `656d0524f76f2078fb16a8a789a55405f6aba7e5`
(pinning `f7a4b68d`) used fresh `gpt-5.6-sol/xhigh` and found no findings.
The subsequent exact API pin update is mechanical; no rerun required. See
`review-kb-packet.md` and `review-kb.md`.

All-page production inventory: 114 Czech and 77 English pages. Candidate
construction changes exactly four public account/API pages. Bulk source/candidate
inventories include private pages and remain ignored/local; never force-add
those indexes or bulk files. Only the four public changed pages, replacement
plan and review/release artifacts are eligible for tracking commits.

Four pre-existing all-page annotation mismatches are outside this feature:
missing `networking.host-addresses.add` in Czech/English IP-address pages and
unregistered `member.public-keys.add` in Czech/English KB-authoring pages.
See `kb-impact.md`. Changed account pages pass focused counts, reciprocal
language markers and content checks. The expanded API-guide annotation count check reports
only the two already-known IP-address count gaps; no new mismatch was added.

Claimed staging with `kb-stage start`. Both schema-5 manifests passed
`kb-release stage --manifest … --yes` and `kb-release verify --manifest …`:
`kb-release-cs.yml` and `kb-release-en.yml`. Each writes two pages, no media or
deletions; summaries and reciprocal page pairs were verified. See
`kb-staging.md` for clickable pages and exact revision summaries. Staging stays
owned by this session with publication pending. Production promotion requires
direct user approval of the exact staged manifests.

The API guides were expanded after detecting stale password/TOTP-only token
issuance prose. Four guarded schema-3 replacements explain email continuation,
Basic refusal without email, existing tokens, `vpsfreectl` prompting and the
unsupported Go helper in both languages. Existing navigation/language markup
is unchanged. A separate fresh GENERAL review (`gpt-5.6-sol/xhigh`) found no
findings; see `review-api-docs-packet.md` and `review-api-docs.md`. The owning
agent applied the English/Czech writing skills directly before review.

Both expanded schema-5 manifests staged and verified successfully, including
the two reciprocal page pairs and exact localized summaries. Logs:
`/tmp/auth-email-kb-expanded-cs-stage.log` and
`/tmp/auth-email-kb-expanded-en-stage.log`. See `kb-staging.md` for all four
clickable revision histories. Production pages remain unchanged.

At contract head `4ccc913`, both CI workflows passed: Check 34834111563 and
Managed page runtime 34834111545. The final follow-up commit `cdc4fa967ad1b8e9daa665e6760db624e736c1fd`
advances only the vpsAdmin revision to tested `1b82f44b8`; it preserves the
deliberate OS pin. `nix develop -c ruby tools/check-contract.rb` passed, and a
separate structural check verified all five revision references and no other
changed lock nodes. Both new workflows are active: Check 34839179515 and
Managed page runtime 34839179476. The prior complete contract/runtime results
remain valid for unchanged behavior; current-head CI is not yet complete.

## Environment lessons

- Component Nix shells automatically cd into api/ or webui/; root shell stays
  at the repository root. Use component-relative command paths.
- API RSpec/rake launches isolated temporary MariaDB on dynamic ports.
- Use `bundle exec ruby` for API-adjacent YAML tooling to avoid incompatible
  ambient date gem versions. Use RuboCop --force-exclusion for generated schema.
- Read unchanged Overcommit config/hooks before the initial signature. Later
  ambient-shell hook mismatches disappeared when the same Git commands ran in
  the root Nix shell; do not resign or bypass hooks to work around the shell.
- Chromium discards Secure cookies on HTTP even with its insecure-origin flag;
  the new integration scenario uses test-only HTTPS.
- Installed writing skills are under `/home/aither/.codex/skills/`; current
  workspace instructions override the KB repository's stale removed skills path.
- `gh api …/actions/jobs/ID/logs --allow-escape-sequences` downloads ANSI job
  logs; the flag belongs to `api`, not the root command. Strip terminal escapes
  before inspecting. Never record credentials or full fixture payloads.

Imported public candidate pages retain the production pages' existing trailing
whitespace so the reviewed and staged content hashes stay exact. Verified that
no new trailing-whitespace line was introduced by candidate edits. Normalized
blank YAML indentation after proving identical parsed replacement values.

## Remaining work

Monitor vpsAdmin integration CI 34838666221 and contract workflows
34839179515 / 34839179476; investigate any failure before integration.
All implementation, templates and exact contract pins are committed and pushed.
The scoped handoff checkpoint contains only this initiative's public candidates,
reviews, tracking and seven reusable notes; private inventories remain ignored. Implementation does not authorize default-branch
integration, production deployment, wiki promotion or session cleanup. Keep all
branches, worktrees, staging and this session open.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-auth-email/
