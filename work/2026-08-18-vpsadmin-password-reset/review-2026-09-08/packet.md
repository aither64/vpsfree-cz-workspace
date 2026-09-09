# Current-default rebase review: password reset

Requested outcome: rebase and repin the existing 2026-08-18-vpsadmin-password-reset
initiative onto all four current default branches, preserving reviewed recovery
behavior, verify and push, then refresh its existing development cluster. No
production deploy, merge, KB publication, new branch/worktree/slug, or unrelated
kernel/Guix image maintenance. The user approved a development reset if needed;
prefer preserving its database and disks. No cluster change has happened yet.

Coordination root: /home/aither/workspace/ai/vpsfree.cz
Worktrees: root/worktrees/2026-08-18-vpsadmin-password-reset/<repository>
Plan: root/work/2026-08-18-vpsadmin-password-reset/plan.md
State: root/work/2026-08-18-vpsadmin-password-reset/state.md
Read the plan, including follow-ups that supersede earlier decisions. The state
is long historical evidence; the last current-default rebase section contains
the current request. Inspect earlier review decisions where relevant.

Acceptance criteria: same password recovery and audit behavior atop current
upstream changes; exact matching downstream vpsAdmin/template pins; preserve
KB-owned OS/runtime fixes; quick checks, all four review lanes, three WebUI VM
suites, seven configuration builds, current-head CI, then healthy dev cluster
with shared-email fixtures and live recovery/history smoke. Long tests/builds
and cluster refresh are intentionally still pending this review gate.

Risk HIGH: authentication/recovery, MFA revocation and concurrency, immutable
password audit data, additive migrations, public OAuth/API contracts and
cross-repository deployment/rollback. All reviewers use gpt-5.6-sol/xhigh with
fresh context. Four required lanes: general, architecture, scope, risk.

Rebase shape and commit ownership:
- vpsadmin: all 41 existing feature patches replayed without conflicts or patch
  changes onto master. Seven upstream commits add location IPv6 visibility,
  WebUI host address semantic controls, and Ruby/PHP dependency updates. A
  required compatibility repair bounds API JSON below 3 because the new
  upstream JSON 3.0.1 package cannot boot ActiveSupport 8.1.3.1 (second
  positional JSON.parse options argument removed). The source constraint and
  regenerated API package metadata are separate logical commits. All other
  generated API dependency versions remain unchanged.
- vpsfree-mail-templates (upstream vpsfree-notification-templates): all eight
  feature commits unchanged; default unchanged. Branded CS/EN recovery mails
  and password-change security notices preserve the exact automated footer.
- vpsfree-kb-contracts: three commits, metrics inventory, password history
  control/bindings, final pin. Upstream absorbed older inventory corrections;
  retained feature diff is additive. Preserve independent vpsAdminOS pin
  6bdf458fd9105379860234ff33d352e55844f08f and its nixpkgs closure/workflow refs.
- vpsfree-cz-configuration: six commits, auth proxy, monitor alerts, deployment
  runbook, exact template pin, runbook adaptation to authoritative templates,
  exact vpsAdmin pin. Superseded vpsAdmin pin commits consolidated; generated
  confctl messages kept verbatim. No unrelated master config changes removed.

Current interfaces/consumers:
- vpsadmin owns recovery admission/worker, policies, digest/session state,
  authentication generation/MFA locks, password audit, nullable OAuth default
  client/start URI, owner/admin history API, and core templates.
- WebUI consumes API/OAuth and owner/admin audit relations. HaveAPI 0.29.6
  underlies resource contracts; no HaveAPI edits. Go client/CLI/Terraform have
  no changed mandatory parameters. New OAuth administrator setting is not yet
  exposed in the generated Go client; operator runbook uses supported paths.
- External templates consume vpsadmin's notification-template package API.
  Production int.api1 and existing workspace devcluster consume that package
  in authoritative replace mode; reconciliation preserves omitted DB rows.
- Config pins exact vpsAdmin and template commits; both API/WebUI hosts, auth
  proxy and monitoring consume the reviewed service/modules/metrics.
- KB pins vpsAdmin for semantic WebUI contract/captures and has an independent
  vpsAdminOS test-framework pin; preserve its current classified retries.

Accepted compatibility and policy boundaries:
- Five additive unreleased migrations; no sixth migration or schema change in
  this rebase. Migration predecessor is exact; no schema-existence guards.
- Recovery only for ordinary users with effective TOTP or passkey; privileged
  accounts get grouped mail with an administrator support outcome and no link.
  Matching login takes precedence over shared primary email. Public response
  is neutral; admission explicitly returns rate/capacity errors.
- MFA/authentication and recovery have separate authority state machines and
  shared factor proof primitives/lock order. Exact factor revocation and
  pending destructive lifecycle states must prevent new authority.
- Email tokens are one-use digest-backed links, then bounded flow sessions.
  CSRF, account/client context, logout-all choice, default-client continuation,
  audit metadata and owner/admin redaction remain as accepted in the plan.
- Password-change mail is independent of recovery feature flag, so templates
  must exist before upgraded API runs. Follow runbook's template reconciliation,
  additive migrations, API drain/switch, then WebUI/proxy/monitoring sequence.
  Enable recovery only after all authentication writers are upgraded. The
  documented rolling audit-detail gap with old processes is accepted.
- Rollback: disable recovery first, restore preceding configs; additive schema
  can remain. Omitted templates are preserved. Down migrations lose added
  audit/recovery data and require operator backup/ordering.
- No coordinated vpsAdminOS node protocol update is introduced.

Known external gap: prior KB runtime tests failed on Ubuntu mirror mismatch and
Software Heritage delay; current KB master adds retry support. Its dated Guix
20260819 image was absent September 7; investigate any repeated failure, do not
turn this rebase into unrelated image publication. No pending failure is a pass.

Reviewer instructions: inspect committed series, diffs, local AGENTS and relevant
provider/consumer/tests. Review directly, no nested agents. Do not mutate files,
Git refs, clusters, or remote services; avoid installing bundles or launching
integration tests in shared worktrees. If additional local tests are needed,
coordinate with the primary agent first. Report evidence-backed findings with
severity and file/commit references, or explicitly no findings plus residual
risks. Rebase interactions and the JSON compatibility repair deserve focus,
while concrete serious defects anywhere in the retained feature remain in scope.

## Exact reviewed commits
### vpsadmin
Base 438d946482801b7229c7535935c3b7e45f6760b8
Head 9f30c1fe095a66315a293c8a45e5c4a9f8ec2819

08bf60725 api: serialize authentication against password changes
e695ea253 api: queue password recovery mail
185ad305f api: add MFA-protected OAuth password recovery
b5f2557a6 nixos: deploy password recovery endpoints
bc6a0d0c8 api: simplify password recovery wording
d246797c2 api: add HTML password recovery mail
b3f70ba66 api: show the logo during password recovery
510d52e4f tests: restart OAuth from password recovery
8483344f9 api: make recovery throttling explicit
43631750c api: notify users after password changes
62167664d api: restore automated mail notice
08d1a4d97 oauth2: show password reset success on login form
8018cb953 api: use proxy-controlled addresses in recovery notices
03c1a6be4 api: adapt recovery completion to OAuth clients
e7fd83799 api: expose password security metrics to account owners
a86ec26df api: export password recovery security events
1c9facdd9 api: document recovery user agent retention
dcf0ee93f oauth2: describe available recovery factors
f3591a502 oauth2: label the recovery account login
9fa7943b1 tests: exercise direct WebUI recovery completion
8d7f2ffe1 api: serialize recovery submission retention
60dac78b3 oauth2: reveal recovery password fields
65908870c api: record password change history
663b89b94 webui: show password change history
b4b6168e2 oauth2: render expired password recovery page
322345fba oauth2: select a default client
47f5c10c4 ci: cover password change log specs
7ac9e9980 oauth2: label required password reset fields
a60ebf9ab webui: attribute administrator password changes
cb3485169 password recovery: poll idle queue every five seconds
5636a6a1b i18n: keep Login as the Czech account identifier
04cdf466c webui: handle sessionless password history entries
ec136f4c1 password recovery: exclude administrator accounts
410972aa9 api: record password change client details
55dd24692 webui: show password change client details
1f62b46ad authentication: serialize MFA factor lifecycle
7c9367407 webauthn: trust proxy-owned client metadata
8f66ee291 password recovery: bound passkey challenges
07a0f7db2 oauth2: cancel recoveries when clients are deleted
a48e84388 authentication: reject pending destructive states
aa81d2a83 oauth2: prefill password recovery login
2ad6ec93e api: constrain JSON to the ActiveSupport-compatible series
9f30c1fe0 packages: resolve API JSON to the compatible series

### vpsfree-mail-templates
Base 9e1ddbd973703cf48a43f0e5afc2bfb392a8b676
Head f944ba03eba5d0d6b58b7eb856f251d1c96f2c11

02cfe29 Add combined password recovery mail
c160b57 password_recovery: simplify verification wording
5e0fd29 password_recovery: add HTML messages
fc49ba7 password_recovery: restore automated mail notice
22a85a3 user_password_changed: add security notice
1472f2c user_password_changed: render vetted client address
1b6e072 password_recovery: use Login in Czech messages
f944ba0 password_recovery: explain administrator restriction

### vpsfree-kb-contracts
Base e5ed479f9d4058556dcf225b4c16afd5b9f0051a
Head 344d3809b1b058acfaa14f0cfc9fd066901e673f

f6128a7 contract: describe account security metrics
c8dc69d Document password change history navigation
344d380 contract: pin rebased password recovery source

### vpsfree-cz-configuration
Base 7cfe38378a1b40952b8019cd895942cda7c32233
Head 9c98cdc9fffd645e52c08f0b7ab5a033f707eaf5

883ddbd4 vpsadmin-config: expose password recovery on auth proxy
cd4a212f monitor: alert on password recovery queue capacity
8f97442b docs: add password recovery deployment runbook
9ade7db4 inputs: set vpsfreeNotificationTemplates to f944ba03
7440faf3 docs: adapt password recovery template rollout
9c98cdc9 inputs: set vpsadminServices to 9f30c1fe

## Quick verification evidence

- vpsadmin full feature-focused batch: 548 examples, 0 failures, 2 expected
  plugin-dependent pending examples; all five migration files / 10 examples
  separately pass. API localization health passed.
- After the JSON constraint: removed the ignored development lock to force
  fresh dependency resolution. JSON 2.21.2 and ActiveSupport round-trip pass;
  50 smoke/system-config/template examples pass and API i18n passes. Fresh
  development resolution also upgraded RuboCop from the repository CI's 1.85
  to 1.90, reporting 25 new-cop offenses in existing source. Avoided unrelated
  reformatting: the exact root-CI command with declared RuboCop ~>1.85 passes
  all 2,144 files. Initial API lint (1.85) passed all 1,512 API files.
- All root Overcommit hooks pass; all two new commits also pass normal hooks.
  Root hook CLI must be invoked directly in the full development shell;
  wrapping Overcommit in bundle exec contaminates the child API bundle.
- CI selector: 16 tests, 55 assertions, no failures.
- WebUI composer test: 90 tests, 376 assertions, passed on identical WebUI tree.
- Built-in template checker: 54 templates, 172 files, passed; external
  template `nix run .#check` and `nix flake check` passed at unchanged head.
- Full KB `nix develop -c bin/check` passes at final source pin, including
  capture validation and all unit checks; preceding pin also validated 120 PNGs.
- Configuration Overcommit and strict MkDocs passed; final exact-pin and
  runbook-revision amendment also passed normal hooks. Source config logic is
  unchanged by the final re-pin.
- API/i18n CI failure logs identified JSON 3 startup failure before rerun.
  New exact-head i18n CI 34276294939 is green; full API topics 34276294946
  and broad CI 34276294973 remain in progress, not accepted as passes.

Transient detailed logs and 41-patch range-diff:
/tmp/password-reset-rebase-20260908.IuiV71/
