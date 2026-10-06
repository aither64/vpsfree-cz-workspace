# Bounded risk follow-up: final corrections

Read the original packet and risk report in this directory for the accepted
scope. This follow-up assesses only the newly enforced User::Create password
boundary, shared ordinary/recovery WebAuthn metadata boundary, and their
compatibility documentation. The root will confirm the canonical fixture
replacement directly under skill step 9. No nested agents.

Committed API head: `6c08f8aa6df5099313c7cae799ba75e004be0c34`, base
`61d2ef6e712345200daddff3abcb4697c028d176`. Compare against first remediation
snapshot `41d590aa86b05439633db68e607405d6132da7f0` (history rewritten; use tree
diff). All changes are folded into the six logical remediation commits.

Configuration head: `00a81e8e68df0b5a4baccdc972cb4857b03a3ed5`, base
`d697bb6baef93b3ce81516e942f8c30d13c326e3`. Runbook introduction `8655e94f`
now documents initial-password validation and pending-login restart. Generated
API pin matches 6c08f8aa. New upstream changes only scheduled unrelated lock
updates; preserve those. No new rollout design or schema change.

- User::Create uses PasswordChanges.valid_length? for explicitly supplied
  passwords before user construction. Omitted passwords retain generation.
  The public minimum remains eight; old accounts/sessions are unaffected.
- WebauthnChallenge.normalize_client_version owns representable UTF-8/255-char
  normalization. Ordinary challenge creation normalizes before UserAgent and
  challenge insertion; recovery calls the same method. Expected WebAuthn
  option errors alone become 422; storage failures still propagate.
- Ordinary WebAuthn tests use the canonical stamped AuthToken helper.

Quick checks: all commits/hooks pass. Six affected Ruby files pass RuboCop.
Focused ordinary registration/authentication, User Write initial-password and
shared-minimum cases, and recovery passkey metadata tests: 74 examples, zero
failures. This was run at tree 6e7cabba3ccf701f5bf7ad1dfd8af793fd105951;
final 6c08f8aa has exactly the same tree after autosquash. Configuration 87
specs, hooks and strict MkDocs pass. No long local integration has started.

Current API CI fast lint/i18n passes. The superseded 41d590 topic run's failed
logs independently confirm six ordinary WebAuthn cases in both full/core topics
caused by the unstamped fixture; the latest focused suite covers these cases.
The old full run was cancelled after final push. No full CI wait is required.

KB final pin/check is mechanical and in progress; its bilingual four-page
preview is staged and verified. Templates remain at f944ba03. These do not
change the bounded risk assessment. No production writes or integration.

Write findings and residual gaps to `risk-followup.md` in this directory.

## Final direct correction and pins

The follow-up report found the false omitted-password generation claim.
The final API `050ea5263812a76dc39f14c5b58a0e88714d634d` changes only the
omitted-password test relative to reviewed 6c08f8aa: it now asserts disabled
password marker `!`. Two focused initial-password examples and all hooks pass.
The configuration guide in `faaa2e73` states the preserved disabled-password
behavior; strict MkDocs and hooks pass. Final configuration is
`bb49f262d263760c26a87b73ad9abae1e28cf9fe`; KB exact pin is
`32888e4f3f0889d869a0e08a9f9519e5ecc36e2d` and its full checker passes.
All four local/remote feature heads match final-revisions.json. Root confirms
this narrow doc/test correction under skill step 9. No further review rerun
is needed; all Blocking/Important findings are resolved.
