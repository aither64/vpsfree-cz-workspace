# September 13 merge-readiness review

**Not ready for merge.** All four mandatory lanes are complete. After independent
reconciliation, there are **two Blocking, four Important and two Advisory**
findings. No project code, commits, pins, remote feature heads or development
cluster state was changed during this assessment. Required fixes remain open;
no Important finding has been waived. No merge or deployment was performed.

## Review identity and scope

HIGH risk: authentication/MFA, stale authority, authorization, persisted state,
public contracts and cross-repository rollout/rollback. Each lane used a fresh
standalone `gpt-5.6-sol` agent at `xhigh`, with no inherited conversation or
nested agents. General, architecture and risk ran concurrently; scope ran when
a slot became available. The review covered the full committed series, not only
the latest rebase.

| Repository | Reviewed head | Reviewed default base |
| --- | --- | --- |
| vpsadmin | `a2e6d8037c737c61c15bfd845c1b3c57d894f310` | `61d2ef6e712345200daddff3abcb4697c028d176` |
| vpsfree-mail-templates | `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11` | `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676` |
| vpsfree-kb-contracts | `6d8ab17db3ce8ffc41216feeb90bff8468b4d39d` | `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8` |
| vpsfree-cz-configuration | `8928b2aba9230202e805aa5489dc9f7369650ac7` | `b4e120294696578c3871124259f266205bad4393` |

All four worktrees were clean, matched remote feature heads, and included the
September 13 fetched default heads. Configuration and KB pins match these
revisions. Full context and commit lists are in [packet.md](packet.md).

## Required remediations

1. **Blocking — legacy pending tokens survive the cutover with stale authority.**
   Risk lane. `vpsadmin/api/models/auth_token.rb:20-25` treats a missing
   generation as zero; the migration initializes existing users to zero. The
   preceding API issues generation-less MFA/reset tokens and does not revoke
   them on password changes. The runbook's stop barrier leaves these five-minute
   tokens usable by the new API. A legacy reset token can overwrite a password
   changed by the old API before shutdown. Root reproduced that overwrite in
   an isolated database, with a new-writer rejection control. Reject pending
   tokens lacking an explicit generation, or invalidate all pending AuthToken
   authority after the last old writer stops and before the new API starts.
   Established sessions can remain. Cover nil and missing-key opts and record
   the chosen upgrade behavior. See [risk.md](risk.md), Blocking 1.

2. **Blocking — password minimum has four independent runtime owners.**
   Architecture lane. Recovery adds `password.length < 8` at
   `vpsadmin/api/lib/vpsadmin/api/authentication/password_recovery.rb:348`
   beside OAuth reset, token reset and User::Update, plus form metadata.
   All currently enforce eight; this is a maintenance/public-contract finding,
   not a demonstrated weaker password accepted today. Root retains the lane's
   severity under the mandatory rubric for expanded security-sensitive public
   contract duplication. Put the minimum and a small shared predicate in the
   existing PasswordChanges owner and use them across these paths and form
   constraints/messages. No generalized policy framework is needed. See
   [architecture.md](architecture.md).

3. **Important — Basic password-hash upgrades lose client audit metadata.**
   General and risk lanes, deduplicated. The Basic provider does not pass
   `request:` to Password.run at
   `vpsadmin/api/lib/vpsadmin/api/authentication/basic.rb:7-11`. A legacy-hash
   upgrade writes a sessionless audit row with null IP/PTR/user agent despite
   having a real request. Root reproduced the empty snapshot alongside the
   newly created Basic session containing the correct address. Pass the request
   and cover the old-hash path. Attaching the later Basic session is not
   required to fix the promised snapshot. See General Important 1 / Risk
   Important 1.

4. **Important — long browser headers break passkey recovery and hide database errors.**
   General and risk lanes, deduplicated. `password_recovery.rb:500` stores the
   raw User-Agent in a 255-character client_version column. Root reproduced a
   256-character header causing ValueTooLong and HTTP 422; the short-header
   control returned 200. Bound/normalize the value to the existing schema limit
   and narrow the method-wide rescue at 290 to expected WebAuthn failures, so
   persistence failures are not classified as ordinary passkey errors. Cover
   the long-header boundary and a persistence exception.

5. **Important — MailLog metadata contradicts account-neutral responses.**
   Risk lane. `vpsadmin/api/lib/vpsadmin/api/resources/mail_log.rb:8` omits
   nullable:true although recovery mail has user:null. Root confirmed both
   Index and Show advertise nullable:false; existing route tests explicitly
   serialize null. Add nullable:true and metadata regression assertions. The
   inspected Go pointer representation tolerates null, so no current Go-client
   failure is claimed. This is a published protocol-description mismatch.

6. **Important — consolidate superseded schemas, repairs and rollout instructions.**
   General and scope lanes, merged at their agreed severity. Introduce the
   final recovery and password-history migration definitions in their owning
   commits. Fold the CI-topic fix `1fae19609` into the history API commit and
   the sessionless WebUI fix `f15d19547` into the administrator-attribution
   change. Consolidate the configuration runbook so `aa517293` introduces the
   final supported rollout instead of relying on `ad6c41ea` to replace its
   obsolete mixed-writer/manual-template procedure. Preserve independently
   reviewable feature changes and generated confctl messages. After history
   changes settle, regenerate the exact downstream pins. The final tree does
   not retain the superseded migration definitions; this finding concerns the
   unmerged series and independent reviewability, not a claim of a current
   schema mismatch. Details: General Important 3 and [scope.md](scope.md).

## Advisory decisions

- **Retention cleanup versus a claimed stale submission** (risk): a row older
  than one day can be deleted before worker finalization; finalization and its
  rescue retry then both raise RecordNotFound, causing a systemd restart after
  30 seconds. Root verified the static claim/cleanup/finalization trace and
  accepts deferral as a bounded availability risk. This interleaving was not
  dynamically reproduced. A follow-up can exclude recent claims and tolerate
  an already removed row without adding a new queue framework.
- **Old bilingual KB history publication candidates** (general): the retained
  untracked candidates say required password changes stay sessionless, while
  final token/OAuth completion attaches the issued session. They are outside
  the reviewed project branches. Root accepts deferral from this merge review,
  but their text and checksummed manifests must be refreshed before staging or
  publication. Do not promote the retained manifests unchanged.

## Investigated concerns that were not retained

- The initial suspected missing final lifecycle check was withdrawn after root
  and reviewer traced NewBasicLogin/NewTokenLogin → User::Login → CheckLogin
  under the reloaded user row lock. That check exists.
- Completed hard-deleted users are excluded by User.including_deleted, so
  retained deleted rows do not establish a shared-email sort failure. The risk
  report records an unmeasured intermediate hard-delete-chain window only as
  a residual test gap, not an actionable finding.

## Verification and probe limits

All nine exact-head CI workflows pass; metadata is in
[ci-results.json](ci-results.json). Full API integration
[34715749842](https://github.com/vpsfreecz/vpsadmin/actions/runs/34715749842)
completed at 2026-09-13T00:35:49Z and its log reports 118 tests successful.
September 12's seven configuration builds, required hooks, configuration specs,
KB checks and live recovery acceptance remain applicable to the unchanged heads.

New quick checks passed: all four committed diffs pass git diff --check;
`nix develop .#vpsadmin -c ruby tests/ci-selection-test.rb` passes 16 tests /
55 assertions; template `nix run .#check` passes 71 templates /349 files.

The coordinator additionally ran isolated characterization probes, not new
integration suites. They deliberately assert observed defects, so their passing
status does not mean the secure requirement is met:

- [legacy-token-probe_spec.rb](legacy-token-probe_spec.rb): two examples pass,
  13.5 seconds (seed 1828), reproducing stale legacy reset acceptance and the
  contrasting new-writer rejection.
- [boundary-probes_spec.rb](boundary-probes_spec.rb): Basic rehash audit and
  MailLog metadata checks pass. The UA control and failure also reproduced;
  an extra assertion about retaining an earlier challenge failed because the
  application's transaction joined the ordinary RSpec outer transaction. That
  assertion was outside the finding and was removed. Only the UA example was
  rerun: one example passes, 12.65 seconds (seed 19840), again demonstrating
  ValueTooLong/422 for 256 characters after a 200 response for a short header.
  No production rollback conclusion is drawn from that first assertion.

Run the probes from the vpsadmin root with `nix develop .#api -c bundle exec
rspec <absolute-probe-path> --format documentation`; add `--tag review_probe`
for boundary-probes_spec.rb. The API shell enters api/. The test harness used
an isolated temporary database after checking that no DATABASE_URL or local
api/config/database.yml was configured. No live cluster fixtures were touched.
Private transient logs remain outside tracking. The pre-existing intermittent
metrics-token HTTP 500 still lacks a root cause; it did not recur in its
identical-order diagnostic rerun or current CI.

## Next step

Implement the required remediations and history cleanup in the retained
branches, verify each fix, then refresh exact pins and run the applicable
verification/review steps. No reviewer rerun has been performed in this review
pass. Under the skill, narrow direct fixes need focused confirmation; rerun
only affected lanes if a fix introduces a new design or changes the accepted
contract. This assessment itself leaves the session active and the existing
bridge cluster untouched.
