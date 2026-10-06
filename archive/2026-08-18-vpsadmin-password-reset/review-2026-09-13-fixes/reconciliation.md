# September 13 accepted-fix review

Implementation, quick verification, both specialist reruns and the bounded
risk follow-up are complete. All Blocking and Important findings are resolved.
The three selected browser scripts and seven configuration builds pass; the
development services update and live acceptance pass. This record supersedes the earlier
review's open-remediation status for the fixes confirmed below. Full CI remains
separate and may finish after handoff by user instruction.

## Root confirmation of direct fixes

- Old pending login authority: AuthToken now requires an explicit integer
  generation. Nil/missing/null/string cases and explicit-zero control are
  covered; established sessions survive the old-writer simulation. A separate
  TOTP case proves rejected authority does not consume the factor. The rollout
  guide explicitly says unfinished old logins must restart.
- Password minimum: the constant and small predicate belong to PasswordChanges,
  reused by all four public change paths, both forms and localized descriptions
  and errors. The minimum remains eight. Modified-minimum regressions cover
  validation, forms and both languages; internal system setters retain their
  prior semantics.
- Basic hash upgrade: the request now reaches Password.run. The regression
  proves trusted IP, PTR and user-agent metadata is retained with source other
  before the Basic session exists.
- Passkey boundary: 255/256 ASCII, long multibyte, supplementary characters
  and malformed byte cases all succeed with bounded representable snapshots.
  Expected option-generation errors return 422; injected storage failure
  propagates instead of being reclassified.
- MailLog: Index and Show metadata now declare user nullable, matching existing
  account-neutral serialized responses and the current Go pointer consumer.
- Queue retention advisory: recent claims survive cleanup; expired removed
  rows are tolerated by both finalization paths, and the worker advances to the
  next row after either success or failure. Other database errors still raise.
- History consolidation: final recovery and history migrations now each have
  one owning feature commit. Final API/db and WebUI trees compare unchanged
  against the original reviewed head. Matching ledger backend changes moved
  with their schema; unrelated HTML behavior stayed in its original topic.
  CI and sessionless-WebUI repair commits were folded, and the configuration
  runbook is introduced once with its final rollout and pending-token note.
  Independent features and generated confctl messages remain separate.
- KB advisory: rebuilt complete bilingual pages remove session/ID explanations,
  retain history navigation and reciprocal translation markers. The release
  bundle also retains the two existing metrics pages byte-for-byte. The
  verification-only upstream IP annotations are excluded from publication.

The root confirms the narrow general/scope remediations directly. Architecture
and risk reruns use fresh gpt-5.6-sol at xhigh because the shared policy owner,
queue-race behavior, upgrade rejection, nullable metadata and error boundary
need specialist assessment. Unaffected lanes are not rerun under skill steps
9–10. Exact heads, commands, consumers and deployment assumptions are in
[packet.md](packet.md).

## First architecture rerun — required corrections

The architecture lane found one Blocking and two Important issues at the first
remediation head. Root accepts all three and is correcting them before long
integration tests:

1. Ordinary WebAuthn specs duplicate AuthToken construction without stamping a
   generation. Both reviewers reproduced the positive challenge example
   failing. Replace that fixture with the canonical helper and inspect all
   remaining constructors; the authentication cleanup task intentionally tests
   expiry independently of generation and can retain predecessor records.
2. Ordinary WebAuthn still writes unbounded browser metadata. Move the unchanged
   normalization rule to WebauthnChallenge and call it from both factories,
   including the ordinary UserAgent insert. Add representative normal/long/
   multibyte/malformed-header ordinary authentication requests.
3. User Create consumes the shared minimum description but does not validate
   supplied passwords. Apply the predicate there and cover changed-minimum
   rejection/acceptance plus omitted-password behavior. This closes the
   existing advertised-contract mismatch; no exemption is introduced.

The API working tree currently holds these corrections, with focused tests in
progress. They will be folded into the three corresponding remediation commits
so no knowingly broken intermediate strict-token fixture remains in the series.
The risk lane is assessing the original snapshot and will receive the final
commits and focused evidence for the added initial-password boundary.

The risk rerun independently reports the same three issues (all Important in
that lane); retain the architecture lane's Blocking classification for the
broken positive fixture. No additional actionable issue was found. Residual
coverage gaps remain the real concurrent cleanup/worker interleaving and
non-Go schema-derived clients reading retained null-user mail rows after
rollback. The lock ordering is consistent, existing threaded queue tests cover
the common lock, and the inspected Go client handles null; these do not block
this bounded remediation.

## Root confirmation of the three additional corrections

All three are folded into final API 6c08f8aa. Ordinary WebAuthn now uses the
canonical stamped AuthToken helper. Positive authentication/registration and
negative expiry/lifecycle cases are meaningful again. Shared normalization
lives in WebauthnChallenge and both factories call it, before ordinary
UserAgent insertion. User Create validates supplied passwords with the same
minimum while omitted passwords keep password login disabled. Six affected
Ruby files pass lint; 74 focused examples pass. The final tree equals the
tested pre-autosquash tree. See followup-packet.md for exact final API/config
heads and the bounded risk follow-up scope.

The superseded CI topic logs independently show the six ordinary WebAuthn
fixture failures in both full/core jobs; they match the now-fixed local
reproduction. No unrelated failed CI was dismissed or blindly rerun.

## Bounded risk follow-up correction

The reviewer found an incorrect compatibility claim in the new omitted-password
test and runbook: existing User Create stores `!` when password is omitted; it
does not generate a password. Root accepts the Important finding, preserves
this existing runtime behavior, and is correcting the test to assert `!` and
the guide to say password login remains disabled. No new generator or runtime
behavior is introduced. The prior 74-example result remains valid for its
scope, but its old presence assertion did not establish password generation.

The narrow correction is now verified: two initial-password examples pass,
including exact disabled marker `!`; API commit 050ea526 changes only that test
relative to reviewed 6c08f8aa. The runbook accurately preserves omitted-password
behavior. Root confirms this direct doc/test fix under skill step 9, with no
further reviewer rerun. All Blocking and Important findings are resolved.
There is no new runtime design in this correction; the specialist's accepted
residual test gaps remain as recorded. Proceed to selected local browser tests,
configuration builds and in-place development deployment after final mechanical
pins and quick checks. No merge/production/lifecycle action is authorized.

A final repository-wide constructor check also finds the housekeeping fixture
in tests/suite/tasks/common.nix. Like the authentication cleanup spec, it
creates an already expired token only to test deletion; it does not authorize
a login and intentionally needs no generation stamp. Runtime issuance and all
positive authentication fixtures use explicit generation metadata.

## Final validation checkpoint

All 41 selected browser tests, seven configuration builds and final live
recovery/ordinary OAuth login pass. The same bridge runner and node/DNS
closures are retained; API 050ea526 is deployed with a clean build stamp.
The bilingual four-page KB preview is staged and verified. All final API
topics and both KB workflows pass; explicit full CI 34752301231 remains
separate under the user's no-wait instruction. Deployment/probe diagnostics
and their verified causes are recorded in validation-2026-09-13.md.
