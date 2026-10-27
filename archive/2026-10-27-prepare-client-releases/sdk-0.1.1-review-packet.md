# SDK 0.1.1 final source/history and GitHub setup review

User added a separate milestone after completed HaveAPI0.31.0/SDK0.1.0:
release vpsadmin-typescript-client0.1.1 to confirm trusted publishing. Existing
release workflow unchanged; no new dependency/runtime/schema/generator behavior.

## Exact committed source

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-prepare-client-releases/vpsadmin-typescript-client
Canonical git@github.com:vpsfreecz/vpsadmin-typescript-client.git, targetmain.
Base149c72f11acef67224a47ed77711a3abb805fbd4.
Final4689d00ca4acf0cc26a3507fc3c238b687b53475, committed/clean/notpushed.
Complete two-commit series:
1.38a25ad88d0bf3018670184620cf69cdb71e92e7 firstpublic0.1.0 MIT/docs metadata.
2.4689d00ca4acf0cc26a3507fc3c238b687b53475 version0.1.1 metadata.
First substantive commit already independently reviewed without findings in
final-review.md. Reuse that unchanged-content review, but assess fullfinalseries.
New delta only4files+5/-5: package/rootlock version0.1.1, required rootlockdigest
in tools/generator.json, README installationversion literal (main-agentwriting
pass approved). External dependency records/privatefalse/license/generatedsrc/
schema/workflow/toolchain/docs unchanged; runtimehaveapi-client0.30.2, generator
18b45aed remain intentional. Complete finaldiff7files+81/-18, sdk-0.1.1-final.diff.

0.1.0 IS externallyconsumed: userpublished at2026-10-27T17:40:04.673Z, public
integrity exactly original retained artifact12755255825/receipt source38a; see
manual-publication.md. Retain38a exact publishedsource boundary, not obsolete
unaccepted intermediateversion. Newversion/lockdigest stream therefore has two
justifiablyretained versions: published0.1.0 and the current0.1.1candidate.
Only0.1.0 is public at this gate. No obsolete approaches/dependency
pin upgrades/migrations. Establish independent explicit history/consolidation/
migration conclusion. No0.1.1tag/package yet; freshregistry endpoint404.

Quickchecks atfinalhead: all6existing release.test.mjs, gitdiff--check, strict
structuredonly-version/lockdigest comparisons to38a and unchangedsrc/schema/
workflow/license/toolchain/docs assertions PASS. Nohookframeworkdeclared;
normalgitcommit-F. No longfullcheck/push/tag/main/publish yet. Clean detached
prepared target worktree at149c72f, SDK-target under samegroup.

## Completed documented GitHub prerequisites

Read sdk-trusted-publishing.md and appended design.md milestone in full.
ExistingSDK docs/releasing.md requires releaseenvironment/reviewer/tagpolicy,
release-tagcreationprotection, enablevariable and sourceonmain. Baselineenvs/
vars/rulesetsall empty. Userauthorized0.1.1release covers routineprerequisite
setup; no source integration inferred. Implementer0 applied exactarchitectbrief
and freshreadbacks at18:28:38Z (nonsecret API values):
- releaseenv25494232596, sole requiredrevieweraither64/User4717906,
  prevent_self_review=false, wait0, protectedbranchesfalse/custompoliciestrue.
- soledeploymentpolicy64571929 namev* typetag.
- NPM_RELEASE_ENABLED exactstringtrue, activatedafterprotectedgatereadback.
- soleactiveTagcreationruleset25982494 includesrefs/tags/v*, noexclusions,
  onlycreationrule, soleRepositoryRole5/admin/alwaysbypass. Currentcaller
  aither64 verifiedrepoAdmin and canbypassalways. Noextra update/deletion/
  signing/status rules; no workflowdesignchange or concurrentsettingoverwrite.
Exactrequests/safeIDs/readbacks/baseline and recoverysemantics in record.
This is an externaloperationconfiguration; no sourcecode changes tocommit.
Settings are live but no tag/main/publish occurs before readiness/approval.

npmprivatepublisheraccountstate isn't publiclyproven; earlier exactfields given
touser (vpsfreecz/vpsadmin-typescript-client,release.yml,release,directpublish).
0.1.1actualOIDCpublication willconfirm. No storednpmcredentials/tokenfallback
introduced. Existingworkflow usescloudhostedrunner, pinnednewnpm/Node,
id-tokenwriteonlyprotectedpublishjob, exactretainedtarball/receipt no rebuild.
Read actual committed workflow as needed to validate protection/identityclaims.

## Review scope and next gates

High operationalrisk: persistentpublication+releaseauthorizationconfiguration.
Lanes general, scope/proportionality, risk/compatibility. Noarchitecturelane:
metadata/staticnativeAPIsettings only, no new handwrittenautomationlogic.
Read mandatory-review skill and these references in full (reuseunchanged
already-read references perprocedure allowed). Retainedreviewer0 saved
Sol/xhigh/read_only, nooverride/no fallback/nestedagents. Verifyidentity.
Compare userrequest with minimaldiff/config scope; no extraoptionalhardening.

Deliverable sourcecomplete/committed+quickchecksPASS and configapplied/readback
verified. Final review before longCI. Read actualfullbranchseries and finaldiff,
published0.1.0provenance, staticconfig/directpublisher contract; inspect live
selected API metadata read-only if useful, nosecrets/fullcredentialURLs.
No tests/builds/writes/claims/merges/tags/publishing. Return reporttext forlead
sdk-0.1.1-review.md, findings and explicitwholehistory/migrations/retainedboundary
conclusion. Reuse originalsource0.1 review appropriately.

After review: implementer1 featurepush+canonicalfullCI/archive; userexplicit
SDK/main approval required once concretecheckedresult. Leadshortclaim
freshchecks/ff/push/proof/release, then userauthorizedv0.1.1tag and protected
workflow. No mainintegrationpermission currentlygiven. HaveAPIrelease already
complete; do not reopen its sources/artifacts or hold its milestonebehindthis.
