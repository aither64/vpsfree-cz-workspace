> Historical first-remediation snapshot. Final committed heads are in
> final-revisions.json; followup-packet.md, risk-followup.md and reconciliation.md
> record the additional corrections, verification and completed review gate.

# Accepted review remediation — September 13

This packet is a targeted rerun of the architecture and risk lanes under the
mandatory-change-review skill, after the complete four-lane review in
`../review-2026-09-13/`. Review directly with fresh context; do not spawn agents.

## Outcome and boundaries

Implement the six required and two advisory findings recorded in the prior
reconciliation. Keep the existing dated initiative, four branches/worktrees,
and running bridge development cluster. The user accepted the implementation
plan, including staging Czech/English KB changes for review and updating the
existing development deployment. Do not merge, deploy production, promote KB,
archive, release ownership, delete or stop the session. Full CI may be left
running by explicit user decision.

High risk, xhigh effort: authentication authority across upgrade, browser input
normalization, queue persistence, public metadata and deployment ordering.

The old-token issue concerns pre-existing five-minute AuthToken MFA/required
password-change continuations. Forgotten-password PasswordRecovery links are
new in this initiative. Rejecting unstamped pending authority intentionally
requires unfinished pre-upgrade logins to restart; established sessions remain.
All API writers still cross the documented no-overlap maintenance barrier.

## Implementation scope

- AuthToken requires an explicit integer generation; nil, missing, null and
  string generations cannot authorize a pending login. Explicit zero is valid.
- PasswordChanges owns the unchanged minimum of eight and the small public
  length predicate. Recovery, forced OAuth/token changes and User::Update use
  it, as do HTML constraints, errors and localized parameter descriptions.
  Internal User#set_password remains available for existing system semantics.
- Basic authentication passes its request into hash upgrades so audit metadata
  is preserved before a new session exists.
- Recovery WebAuthn client_version is normalized to the existing utf8mb3 and
  255-character database limit. Only expected option-generation WebAuthn errors
  are handled as an ordinary passkey failure; storage errors propagate.
- MailLog.user describes the existing nullable response in Index and Show.
- Retention preserves recent claims. Completion/retry under the queue lock
  tolerate a removed row but do not suppress other database errors. Existing
  limits, retries and retention policy remain unchanged.
- Unmerged history introduces final recovery/history migrations in their
  original owning commits. Matching recovery ledger backend behavior moves
  with its schema. CI-topic, sessionless WebUI and rollout-guide repairs are
  folded into their owners. No final schema change or added migration.
- KB history prose explains when/how password changes are recorded and where
  to open the history, without session-association or ID implementation detail.
  Both languages retain the English-derived invisible translation marker.

The six runtime repairs remain separate logical commits with their regressions.
Generated confctl pin messages remain verbatim and separate. Root directly
checks the narrow general/scope history remediations; the two specialist reruns
assess the new policy ownership, queue race behavior, upgrade rejection and
public metadata/error boundary. This is not a request for another blanket
full-series review or a rubber stamp.

## Repository locations

Workspace `/home/aither/workspace/ai/vpsfree.cz`; branch and slug
`2026-08-18-vpsadmin-password-reset` in each independent repository.
Worktrees are under `worktrees/2026-08-18-vpsadmin-password-reset/`:
`vpsadmin`, `vpsfree-mail-templates`, `vpsfree-kb-contracts`, and
`vpsfree-cz-configuration`. Plan/state are in this packet's parent directory.
Original reviewed heads remain in each repo at
`refs/backup/password-reset-review-20260913`; previous packet records full
bases, heads, consumers and topology. Exact final revisions are appended below.

## Verification already performed

- Focused API suite: 235 examples, 233 passed initially; two new test-only
  accessor/locale mistakes corrected and both passed on rerun. The two shared
  policy examples passed again after moving them inside the existing spec
  group for lint. That intermediate move first inherited the wrong operation
  class in a setup hook; correcting the context fixed the test setup.
- Twenty changed Ruby files pass RuboCop. All five feature migration specs:
  ten examples, zero failures. API localization health passes, including the
  existing Czech VPS-generated-password description moved by catalog promotion.
- History-only API and configuration rewrites compare exactly equal to the
  original final trees before behavior/doc changes.
- Fresh KB all-page inventories: 114 Czech and 77 English pages. The complete
  navigation verification passes with 94 bindings and nine exceptions.
  Full contract check passed before the final mechanical exact-pin refresh.
- Preview consists of four pages: revised bilingual user history and the two
  unchanged metrics pages already staged by this initiative. Retained staged
  metrics compare byte-for-byte equal to rebuilt candidates.

KB checking needs verification-only upstream IP-address annotation fixtures
because those contract edits have not been published in production. They are
excluded from the four-page release manifests. Preview source inventories,
plans, candidate pages and schema-5 manifests are durable local tracking
artifacts. Production publication is not authorized.

## Compatibility, ownership and deployment

vpsAdmin owns authentication, PasswordChanges policy/audit, queue persistence
and HaveAPI resource metadata. HaveAPI's supported LocalizedMessage mechanism
provides interpolated descriptions; no shared library is modified. Consumers
include OAuth browser forms, Basic/token providers, user update APIs and
existing generated clients. The inspected Go MailLog pointer already accepts
null, so no client regeneration is needed for this metadata correction.

The independent KB repository owns navigation/capture contracts and pins the
exact API revision. Production configuration owns exact service/template pins
and the template-first, five-additive-migration, no-overlap writer rollout.
Both APIs must run the new code before WebUI/proxy rollout and recovery
activation. Rollback disables recovery and crosses the same no-overlap writer
barrier; retaining additive schema is preferred. No node protocol/OS change or
coordinated production node upgrade is required.

After this review, run the three WebUI VM scripts and seven configuration
builds, then update the existing bridge services in place and verify live
mail/TOTP/password/history behavior. Keep all review instances running.
The KB release guard requires a clean production mirror or the exact candidate
before staging; replacing the older staged history therefore uses an owned
KB reset followed by the complete four-page bundle. Existing pages have private
backups and the retained metrics are identical. This does not reset the
vpsAdmin development database. The initial broken host-side KB route was
repaired to its declared address without restarting or altering content.

## Exact committed revisions and final quick checks

| Repository | Default base | Reviewed head |
| --- | --- | --- |
| vpsadmin | `61d2ef6e712345200daddff3abcb4697c028d176` | `41d590aa86b05439633db68e607405d6132da7f0` |
| vpsfree-mail-templates | `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676` | `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11` |
| vpsfree-kb-contracts | `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8` | `497ad8e37e7478aa2fa8e86696829efcf755fd7b` |
| vpsfree-cz-configuration | `b4e120294696578c3871124259f266205bad4393` | `4a7ec36ea5a88b088cd77431fb12f4df0f57bd43` |

All intended repository changes are committed. Worktree-only generated test
caches/tool directories are excluded from review. The API final-tree delta
from the original reviewed head is exactly the six repairs and regressions;
`api/db` and `webui` compare unchanged. The recovery migration appears once in
`1f8e676cd`; the history migration appears once in `cffa3116a`.

Runtime repair commits, oldest first:
`d0dd1f551` unstamped pending tokens;
`7929e050a` Basic audit;
`c69e76e6a` MailLog nullable metadata;
`7fa504b6e` queue retention;
`d889044b3` passkey metadata/errors;
`41d590aa8` public password minimum.

Configuration introduces the consolidated final guide in `c90b619d`, including
pending-token upgrade behavior and final API literals. Generated template and
API pins follow it. KB inventory is `b699e62`; final exact pin is `497ad8e`.

Final quick checks pass: all active commit hooks, 90 PHPUnit tests /376
assertions, CI selector 16 tests /55 assertions, 87 configuration specs, strict
MkDocs, full KB `bin/check` including 120 PNGs, and navigation verification
94 bindings /9 exceptions. The unchanged external package passed its current
head checker earlier today (71 templates /349 files). Both pinned revisions in
configuration match the table. KB's independent OS `6bdf458f` and all input
nodes except vpsadmin compare exactly equal to their original reviewed lock.
A plain flake update initially changed nested OS inputs; the supported explicit
nested-input override restored the intended closure before commit/checks.

The API feature has been pushed with an explicit lease. Current-head CI runs
are launched; do not treat the preceding head's green CI as final validation.
No long local integration tests or development deployment have started yet.
