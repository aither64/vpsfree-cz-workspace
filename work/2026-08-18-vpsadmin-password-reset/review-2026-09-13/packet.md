# Fresh merge-readiness review — September 13

The user requests a fresh mandatory change review of this existing branch to
assess readiness for merge. Review the COMPLETE committed feature series and
final behavior across all four repositories, not only the latest rebase delta.
Do not rely on previous review conclusions as proof of correctness.

This is a review and readiness assessment. Do not merge, rewrite commits, edit
project files, push, deploy, change live fixtures, or stop/reset/release the
running development cluster. No new branch, worktree, or session is authorized.
Report actionable findings; the coordinator will reconcile them with evidence.

Coordination root: /home/aither/workspace/ai/vpsfree.cz
Initiative: 2026-08-18-vpsadmin-password-reset
Plan: work/2026-08-18-vpsadmin-password-reset/plan.md
State: work/2026-08-18-vpsadmin-password-reset/state.md
Worktrees: worktrees/2026-08-18-vpsadmin-password-reset/<repository>
Read the plan including later decisions which supersede its earlier iterations.
The current state is at the top; dated lower sections are historical evidence.

## Requested feature and acceptance

- Self-service OAuth password recovery for ordinary user-role accounts with
  effective TOTP or passkey configuration. Support/admin roles are ineligible.
- Exact login takes precedence over primary email; shared addresses receive
  grouped mail with per-account outcomes and eligible one-use links. Public
  HTTP admission is account-neutral; explicit 429/503 throttling is intended.
- Bounded asynchronous submission queue, digest-backed one-hour links, a
  15-minute flow, MFA proof, password validation and logout-all choice.
  Existing TOTP recovery codes are accepted but intentionally not advertised.
- Factor revocation, role changes, pending destructive lifecycle states,
  password changes, and client deletion must not leave usable stale authority.
  Ordinary authentication and recovery have separate authority state machines.
- Complete via the persisted/default OAuth client's validated start URI,
  including interactive clients and queryless entry. No automatic sign-in.
  Preserve client-bound one-time completion alerts and failed-login prefill.
- Record durable password-change counters and immutable detailed audit rows,
  including nullable initiating session and bounded client snapshots. Owners
  can read their history; another user's initiating-session details are
  redacted. Admin history attribution and sessionless rows must work.
- Bilingual forms, branded notification templates, password visibility controls,
  semantic WebUI documentation bindings, exact downstream pins, worker/service
  exposure, queue alerts, and operator rollout/rollback instructions.

## Scope decisions and constraints

Production deployment, integration, KB publication, unrelated kernel/Guix work,
and session/cluster lifecycle changes are outside this request. Guix maintenance
was assigned to another initiative and its merged fix is inherited. The deployed
runtime packaging repair is independently owned; inspect interfaces only where
relevant, do not audit or modify its entire initiative.

The branch is unmerged. Review history for obsolete branch-only designs and
unnecessary follow-up commits; prior incremental acceptance is not an exemption
from the current skill's commit-series criteria. Source, support tests and a
required migration may stay together for one behavior. Generated pins remain
separate and confctl-generated messages stay verbatim. Current broad split:
API/authentication and recovery; Nix endpoints/worker; copy/mail/UI refinements;
security notices/metrics/history; MFA lifecycle/client/lifecycle hardening;
external branded templates; KB contract; production proxy/alerts/runbook/pins.
No blanket justification is asserted for incidental historical fixup commits.

## Risk and lanes

HIGH risk: authentication, MFA, authorization, secret-bearing mail, persisted
state/migrations, concurrency, owner/admin isolation, public OAuth/API behavior,
and deployment/rollback across repositories. Required lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Every fresh
reviewer uses gpt-5.6-sol with xhigh reasoning and no inherited conversation.

## Owners and discovered consumers

vpsAdmin owns recovery admission/worker, authentication generation, factor proof
primitives, password mutation/audit, OAuth configuration/routes and core mail
variables. Its WebUI consumes OAuth and owner/admin resources. HaveAPI provides
resource/protocol contracts; no HaveAPI patch is part of this series. Generated
Go client/CLI/Terraform require no new mandatory parameters; new optional OAuth
client settings are not yet in the Go client (documented operator paths apply).

External notification templates consume vpsAdmin's public template package API.
Production int.api1 and the dev provider install the external package in
replace mode; existing omitted database templates survive reconciliation.
Configuration pins exact vpsAdmin/templates and supplies both API/WebUI hosts,
auth proxy and monitoring. Inspect actual imports/options/pins and the runbook.

KB pins exact vpsAdmin to validate semantic controls/captures/page bindings,
while retaining an independent OS test-framework input at
6bdf458fd9105379860234ff33d352e55844f08f. KB is a separate canonical owner;
production wiki page promotion is a distinct approved operation. Discover other
relevant consumers from code/imports/pins instead of assuming this list is
exhaustive. The development cluster runs OS staging 15802517; no production
node protocol change is introduced by this feature.

## Supported deployment and compatibility

Five additive feature migrations, default-off recovery, nullable OAuth settings,
nullable mail-log user, nullable audit relations, and new auth generation.
Exact predecessor schemas apply; no guards for abandoned disposable schemas.
The deployed core also includes later upstream migrations, including payments.

Templates must exist BEFORE either upgraded API starts: password-change notices
are independent of recovery enablement. Migrate before new application writers.
All old authentication/password writers must be stopped before any upgraded API
runs; api2 remains runtime-masked through its switch. Manual writers are paused.
This deliberately requires a brief API maintenance window. Old/new concurrent
writers are NOT a supported rollout boundary. Apply the symmetric barrier on
rollback, disable recovery first, and stop new workers. Additive schema can
remain. Dropping it loses added audit/recovery data and requires backup/order.
Historical old writers may not record new detailed audit fields; no backfill is
claimed. Inspect the final runbook for executable ordering and actual topology.

The bridge development cluster has been deployed and acceptance passed. Its
former disks/database were already absent before September 11; September 12
startup initialized them under retained configuration/socket identity. Do not
claim preservation of that older database. This review does not mutate it.

## Verification available before this review

All four heads are committed, clean, equal their remote feature heads, and
include freshly fetched origin/master (September13). No rebase was performed.
All four committed diffs pass git diff --check. The CI selector was rechecked with
`nix develop .#vpsadmin -c ruby tests/ci-selection-test.rb`: 16 tests,
55 assertions, zero failures. Notification templates were
rechecked with nix run .#check: 71 templates / 349 files pass.

September 12 exact-head API and configuration hooks pass; configuration 87 specs,
strict MkDocs, full KB bin/check and 120 PNGs pass. Seven configuration builds
pass (api1/api2/webui1/webui2/auth proxy/mon1/mon2). Feature-focused API 573
examples and 11 migration examples plus PHPUnit 90 tests / 376 assertions were
validated September 11 on the unchanged source/dev-bundle trees. One original
metrics-token HTTP 500 did not reproduce in narrow checks or the full identical
order with exception diagnostics; root cause remains unknown, no fix is claimed.

Exact current vpsAdmin CI: all 27 API topic jobs, migration specs, RuboCop,
PHPUnit, i18n and libnodectld pass. Full integration 34715749842 has now completed
SUCCESS, 2026-09-13T00:35:49Z, exact a2e6d803 head; its downloaded log
confirms 118 tests successful:
https://github.com/vpsfreecz/vpsadmin/actions/runs/34715749842
KB Check 34715979633 and runtime 34715979634 pass (12 scripts / 4 tests), including
inherited Guix fix. Live mail/TOTP/reset/normal-sign-in/audit/security-notice
acceptance passes; services/DNS/node/pool health and packaged JWT 3.3.0 pass.
See validation-2026-09-12.md for the deployed state.

## Reviewer working rules

Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and the exact
reference for your assigned lane. Inspect local AGENTS.md, full diffs and commit
history, relevant tests and real consumers. Perform the review directly; no
nested agents. Only write your assigned report under this review directory.
Do not install bundles or run integration tests concurrently in shared worktrees.
Coordinate additional tests with the root agent. No secrets, live fixture
values, or private logs in reports.

Start with Blocking / Important / Advisory findings ordered by severity, with
precise file/line, commit, concrete trigger and failure, and smallest credible
remediation. If no findings, say so and state coverage/residual risks. This is a
fresh assessment, not a confirmation of earlier reviewers. Root will reconcile
independently and preserve dissent supported by code evidence.

## Exact repository ranges and commit series

### vpsadmin

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-08-18-vpsadmin-password-reset/vpsadmin

Base: `61d2ef6e712345200daddff3abcb4697c028d176`

Head: `a2e6d8037c737c61c15bfd845c1b3c57d894f310`

```text
2a844e772 api: serialize authentication against password changes
6f45ee44c api: queue password recovery mail
ee70a09ca api: add MFA-protected OAuth password recovery
12ce20436 nixos: deploy password recovery endpoints
c0b07176b api: simplify password recovery wording
d20bab0e5 api: add HTML password recovery mail
b5d62240d api: show the logo during password recovery
d6eb5cdc8 tests: restart OAuth from password recovery
89eb40b45 api: make recovery throttling explicit
124dbdb41 api: notify users after password changes
f0b7f768c api: restore automated mail notice
50bcd1ac8 oauth2: show password reset success on login form
9286213a8 api: use proxy-controlled addresses in recovery notices
ed4a64604 api: adapt recovery completion to OAuth clients
9e46ae088 api: expose password security metrics to account owners
df0a7566a api: export password recovery security events
aaaeb2946 api: document recovery user agent retention
e28bff713 oauth2: describe available recovery factors
f6196aedc oauth2: label the recovery account login
fa8866bb3 tests: exercise direct WebUI recovery completion
eaad07112 api: serialize recovery submission retention
dd930d8f1 oauth2: reveal recovery password fields
bd32e1628 api: record password change history
ef7869182 webui: show password change history
994e2eaa3 oauth2: render expired password recovery page
b12f2e1cd oauth2: select a default client
1fae19609 ci: cover password change log specs
218ad4331 oauth2: label required password reset fields
44c6144e8 webui: attribute administrator password changes
4cb648353 password recovery: poll idle queue every five seconds
3a3af31f0 i18n: keep Login as the Czech account identifier
f15d19547 webui: handle sessionless password history entries
18e75847c password recovery: exclude administrator accounts
6a1cf297f api: record password change client details
068581cea webui: show password change client details
2639ac721 authentication: serialize MFA factor lifecycle
a636ece73 webauthn: trust proxy-owned client metadata
94fd206f9 password recovery: bound passkey challenges
7364380e6 oauth2: cancel recoveries when clients are deleted
4eb9290d3 authentication: reject pending destructive states
a2e6d8037 oauth2: prefill password recovery login
```

### vpsfree-mail-templates

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-mail-templates

Base: `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`

Head: `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`

```text
02cfe29 Add combined password recovery mail
c160b57 password_recovery: simplify verification wording
5e0fd29 password_recovery: add HTML messages
fc49ba7 password_recovery: restore automated mail notice
22a85a3 user_password_changed: add security notice
1472f2c user_password_changed: render vetted client address
1b6e072 password_recovery: use Login in Czech messages
f944ba0 password_recovery: explain administrator restriction
```

### vpsfree-kb-contracts

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-kb-contracts

Base: `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8`

Head: `6d8ab17db3ce8ffc41216feeb90bff8468b4d39d`

```text
145945e contract: describe account security metrics
a65a447 Document password change history navigation
6d8ab17 contract: pin rebased password recovery source
```

### vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-cz-configuration

Base: `b4e120294696578c3871124259f266205bad4393`

Head: `8928b2aba9230202e805aa5489dc9f7369650ac7`

```text
443ed244 vpsadmin-config: expose password recovery on auth proxy
c6b97275 monitor: alert on password recovery queue capacity
aa517293 docs: add password recovery deployment runbook
d99663a7 inputs: set vpsfreeNotificationTemplates to f944ba03
ad6c41ea docs: coordinate password recovery template rollout
8928b2ab inputs: set vpsadminServices to a2e6d803
```
