# Final review packet

## Requested result and scope

User authorized a separate HaveAPI patch initiative: fix documentation OAuth
Switch user, inspect actual supported stable/master, backport compatible existing
fixes and publish next patch through protected repository procedure. No production
deployment, peer-session file access, lifecycle cleanup, cookie sliding redesign,
provider-specific SSO implementation or broad downstream/runtime campaign.

Only HaveAPI is affected. Source extension owner is DocumentationOAuth; public
interface is `switch_user_revoke_params: Hash<String,String>` default `{}` in
`api.documentation_oauth`. Required credentials/token/token_type_hint cannot be
overridden. Only validated switching includes extras on revoke POST; ordinary
Sign out, authorize/token, failures/fresh PKCE remain unchanged. Representative
provider fixture retains a second valid authorization sharing SSO. The consumer
lead receives `close_sso => 1` interface through authorized communication and owns
vpsAdmin adoption/site docs/config channels; do not read its files/team/worktrees.

## Identity, ownership and references

Session 2026-11-01-haveapi-0321-docs-switch-user under verified workspace
/home/aither/workspace/ai/vpsfree.cz. Read plan.md, state.md, design.md and release.md
in this directory. Architect0 designed; implementer0 owns source/spec/doc and
review fixes; implementer1 owns -x backports, notes and patch version/checks.
Selected independent reviewer0: saved purpose review, Astra gpt-6-astra/xhigh,
read-only. User changed the saved model and explicitly requested restart; prior incomplete Sol review is superseded. No fallback or effort override. Lanes: general, architecture/repetition,
scope/proportionality and risk/compatibility. Risk high because OAuth boundary and
public cross-project config, despite bounded compatible implementation.

Required skill: installed mandatory-change-review/SKILL.md and all four lane
references. Read workspace/repository instructions and routed procedures directly.
Review committed deliverables only after final heads/quick evidence are filled.
Do not launch subreviewers or long checks. Report findings by severity; explicit
whole-history, repeated-update and migration conclusions required.

## Ranges, series and disposition

Master base 209a7ac0c2fe6cd1b78735f50b5e60d979309543; source commit
ff0c2f072e1e4f49fcab587ddca0f510c95470bf. Final master head cc06cb8c2a6305f13d3b80ebc0a461507055b14c.
Master worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-haveapi-0321-docs-switch-user/haveapi.
Stable base 0e7166a0f8f15827bfac051666a53bf449e999ec; final head c54404c0818284135add1e77f43feb92e192116c.
Stable worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-haveapi-0321-docs-switch-user/haveapi-stable.

Stable intended series: -x backport of existing master CI-only fix 209a7ac0,
-x backport of final OAuth source ff0c2f07, separate 0.32.1 metadata/changelog.
Master keeps 0.32.0 metadata and general source/release notes. All maintained
components use coordinated version by release policy. Verify complete actual
series and final diff for both ranges, not only last commit.

No migrations, schemas, seeds or persisted-format changes; none merged, released,
deployed or externally consumed. No dependency pin updates; internal package
version constraints move once on stable, external dependency locks must remain
unchanged. Library locks stay untracked. No superseded approaches remain in
intended series; briefly seen source 3540eff4 was replaced pre-publication for
commit-message/docs wrapping and is absent from reviewed series. Confirm independently.

## Documentation and compatibility

`doc/documentation-oauth.md` owns the static configuration/default/reserved fields,
normal logout/provider semantics and rollback ordering. Lead applied user-facing
writing + English Humanizer directly before source commit. `CHANGELOG.md` records
patch behavior and bounded CI backport; release-owner draft accepted by lead.
`doc/performance.md` is part of existing CI fix. No site setup docs here.

Existing config remains unchanged on new library. Old library rejects new option,
so upgrade before enabling and remove option before rollback. Cookie format and
initial fixed expiry unchanged. No production deployment. Publication is atomic
only per destination; retain source tag/original artifacts on partial failure.

## Quick evidence

Source ff0c2f07: make doc passed; focused OAuth 92 examples, 0 failures (7.52 s,
seed19213); changed Ruby root RuboCop and diff --check passed. Final mandatory
HaveapiI18n/RuboCop/TextWidth/SingleLineSubject/TrailingPeriod hooks all OK without
bypass. Stable full dependency preparation completed once, check-inputs 0.32.0
passed before versioning; exact 10 locks/flake receipts in preparation.md and
local evidence/stable-prepared-inputs.json. Stable final quick evidence recorded below.

Review first; existing protected tag workflow supplies required longer component
checks/build/package verification afterwards. Avoid duplicating broad matrix
locally. Tag or committed candidate is not usable publication readiness.

## Complete committed series and diff inventory

Master 209a7ac0..cc06cb8c:
1. ff0c2f072e1e4f49fcab587ddca0f510c95470bf source/spec/guide.
2. cc06cb8c2a6305f13d3b80ebc0a461507055b14c applicable patch notes only.
Final diff: 4 files, 219 insertions/17 deletions.

Stable 0e7166a0..c54404c0:
1. 9d404273ffe90a257f76cb1c1c80a6380aaaf304 -x CI baseline fix from 209a7ac0.
2. 0116bbe1ea20b1b9dbfe324726fe116ac9484a5d -x OAuth fix from ff0c2f07.
3. c54404c0818284135add1e77f43feb92e192116c coordinated version+notes.
Final diff: 24 files, 345 insertions/39 deletions. CI source/spec/docs are exactly
existing master fix, not a new runtime subsystem. Version stream occurs once.
Both tracked trees were clean at lead inspection; range diff --check passed.

User acceptance prose is settled and applied; source guide/patch notes match
accepted static interface. No migrations and no repeated superseded dependency
streams. Treat these as packet claims to independently verify.

## Final quick-green handoff (release owner)

Both worktrees clean and Git ownership released. Stable `make doc` and combined
`bundle exec rspec spec/documentation/oauth_spec.rb spec/performance/event_baseline_spec.rb`
passed 152 examples, 0 failures, 10.22 s seed59208. Changed Ruby RuboCop: 4 files,
no offenses. On committed stable head, `make release-check` validates metadata and
prepared inputs 0.32.1. `overcommit --diff` original stable base passed
HaveapiI18n/PythonChecks/JsFormat/PhpCsFixer/RuboCop. Metadata commit pre-commit and
commit-msg hooks all pass; master notes hooks pass and `check-clean --master`
validates 0.32.0. Final prepared external-lock comparison passes; only local
HaveAPI package versions changed. No tracked library locks. Stable pre-metadata
0116bbe1 source tree equals master source ff0c2f07 exactly. Final master/stable
diff consists only of 17 version/internal-dependency files.

Logs: /tmp/2026-11-01-haveapi-0321-docs-switch-user-stable-focused.log,
-stable-final-quick.log and -stable-version-commit.log. Prepared/versioned input
receipts in evidence/stable-{prepared,versioned}-inputs.json (local raw evidence).
Recovery refs <slug>-recovery-master at 209a7ac0 and <slug>-recovery-stable at
0e7166a0 retained. No feature pushes or long suites launched; review gate preserved.
