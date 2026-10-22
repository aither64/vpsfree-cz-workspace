# PHP session upload-progress mitigation

## Goal and scope

Disable `session.upload_progress.enabled` for web-request PHP/FPM in
`vpsfree-cz-configuration`, pending upstream fixes for the user-reported
CVE-2026-109618 and CVE-2026-109619. Verify advisory identifiers and mitigation
scope rather than asserting unverified coverage. Deliver a reviewed published
feature branch, exact machine inventory and a confctl deployment command.
Latest user direction additionally authorizes master integration after one
affected-machine build. Actual deployment remains outside this request.

## Owners and backlog

| Owner | Expected result | Acceptance / checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | PHP inventory and design.md | Cover service modules, generated INI, all host mappings and confctl syntax; cite advisory evidence | None |
| implementer0 | Configuration execution package | Minimal complete patch, hooks/quick checks, focused commit, published branch | Design, initial tracking commit |
| implementer1 | Independent execution package from design | Own nonoverlapping files or verification/rollout evidence; report coverage and command | Design |
| reviewer0 | Independent final review | Committed final diff, complete history and migration conclusion; no unresolved material findings | All commits and quick checks |
| lead | Coordination, acceptance, tracking and handoff | Exact deploy command and limitations, stable session URL | Member reports |

## User scope correction

User: "let's not waste time with CLI". Focus on web-request PHP/FPM; drop the
default-PHP overlay and PHP CLI evaluation. Three source paths only: shared
FPM module, module-list import, nested kb-staging import. Aitherdev still needs
deployment for its staging FPM pools.

## Approach and documentation

Architect traces PHP configuration entry points and writes the implementation
and verification brief. Implementers own source, technical comments/docs,
checks, commits and fixes; serialize Git and overlapping edits. A concise source
comment should explain temporary mitigation where useful. Keep individual
machine rollout steps, exact revisions and verification evidence in this session.

## Compatibility, deployment and recovery

Disabling PHP session upload progress may remove application upload-progress
reporting; ordinary uploads and sessions should remain functional. Confirm
actual service behavior and INI precedence in design. No schema, API, persisted
state or channel changes are intended. Apply through normal configuration
activation and PHP service restart/reload semantics; removing the setting before
upstream fixes would restore exposure. Mixed-version hosts remain exposed until
their own configuration is activated. Do not deploy. Merge configuration/master only after required review and the
user-authorized single-machine build pass.

## Verification

Run repository hooks and focused syntax/configuration checks first, then final
independent review. Run only int.kb full-system build under fresh Luna/low
verification utility after review, per user fast-track direction. Assess every PHP host and ensure no
runtime-specific setting overrides Off. Confirm the exact confctl selector and
build/deploy syntax against installed tool/repository guidance.

## Latest accepted verification and integration scope

User directs fast-track verification: build one affected machine, then merge.
Representative system: cz.vpsfree/containers/int.kb. Run required final independent
review, then watcher-owned build of that host only, then fast-forward integrate
vpsfree-cz-configuration/master and verify remote exact head. No deployment.

## Fixed PHP follow-up (current scope)

User requests pinning nixos-stable to the newest 26.05 stable source revision
containing nixpkgs PR576865, without waiting for channel promotion; clarified
`release-26.05`. Observed head/PR merge is
8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f. Current nixos-26.05 channel head
cd4ea8d57de16f4810bc5f14207bac45fbf19f67 is75 commits behind and lacks it.
User will build themselves. No PHP/system build or deployment in this follow-up.
Remove temporary Off only for runtimes demonstrated fixed. Independent Foto
PHP5.6.40 is not updated by stable pin and retains narrow workaround.

| Owner | Expected result | Acceptance/checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | Updated design and authoritative release/fix evidence | Exact source head, PR ancestry, per-runtime removal boundaries, compatibility | None |
| implementer0 | Native stable pin + conditional workaround removal, focused commits/publication | confctl-generated lock only; scoped source; hooks/quick checks; full history | Architect brief |
| implementer1 | Independent fixed-runtime coverage evidence | Actual selected pin source/hash/version for ten stable pools; Foto exception | Native pin |
| reviewer0 | Mandatory final review | Complete new committed range, conditional removal security, pin scope, no migrations | All changes/checks |
| lead | Scope/acceptance, records and handoff | Relayed latest SHA immediately; no builds; ready branch status/remaining actions | Reports |

Operator/build evidence belongs in this session; retained Foto source comment is
proportionate lasting rationale. No schema/API/state format change intended;
rolling upgrades safe, deploy new pin/removal together. Rollback to previous
configuration restores its earlier mitigation; Foto retains it throughout.
Upstream stable package update has wider machine impact than original PHP-only
module edit; report that pin consumers span stable channel. Current integration
base 37a338b25192d9271ee211110800c2dc6a094a57 after normal feature refresh;
prior merged workaround commit/history must be preserved. New integration into
master requires explicit direction for this follow-up; earlier merge approval
was for already-integrated workaround and does not cover material new patch.

## Latest user change: disable Foto

User directs temporary disablement of foto.vpsfree.cz because the workaround
is insufficient. Final scope replaces Foto-only mitigation with unavailable
nginx hostname and no Foto FPM/PHP5.6 package reference. Preserve site data,
users/group/domain so restoration can follow real runtime upgrade. No live
activation requested here; source change takes effect on later user deployment.
Keep native exact stable pin commit, consolidate the unmerged functional
iteration to final global-workaround removal plus Foto disablement; no obsolete
workaround-only commit in unmerged series. Ten total FPM pools should all use
fixedPHP8.4.27; no retained partial workaround. Existing plan passages about
Foto-only settings are superseded by this user direction.

## Final user-directed commit and integration scope

Three commits required by user: native exact stable pin, git revert of original
38687a workaround, standalone Foto disablement. Same final tree as accepted
disablement candidate. User explicitly directs merging configuration/master
when done. Complete final review then FF integrate under short merge claim,
verify remote head and release. No PHP/system builds (user owns), no activation.
