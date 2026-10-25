# Independent final review and reconciliation

Reviewer: retained reviewer0, thread01a16f67-b886-7573-a065-dcf2f4b7c262,
gpt-6.1-sol/xhigh/read_only; no setting override, fallback, source authorship
or nested reviewer. Exact session verified from current/trusted thread binding;
both environment markers absent, no conflict. All four mandatory lanes read
and applied. High risk. Final report received2026-10-24; outcome **changes
requested**. This record summarizes the independent report and lead disposition.

## Exact reviewed deliverables

- vpsadmin:b82eeca50cd4dd7bd76728685c7de8aad66e7ba5..
  21872fe6ad373e52f66f193ee432f4885376e5a5 (ff44d95e dependencies/native
  prerequisites;21872fe6a profiles/spec/docs/packaged assertions).
- vpsadmin-webui:5a2d2bdc3ad7a827038f877d75959916528db844..
  39f8fd7d2bee0c4754f0f9921d97855da7fbdddf (cd3577a6 registry/provenance;
  39f8fd7d production adaptation/tests/docs).
- Workspace KB commit87c5e6f96, all8candidate/original/manifest/summary/receipt
  files checked against committed bytes and actual original/candidate delta.

## R1 — Blocking — risk/compatibility and general

vpsadmin api/Gemfile:18,api/lib/vpsadmin/api.rb:46; released HaveAPI1c3c98f0
servers/ruby/lib/haveapi/documentation_context.rb:27-38,server.rb:254-272.

Ordinary documentation GET costs102.376sadmin,49.716smember,139.036sanonymous,
with CPU essentially equal to wall time.639/484/639context derivations take
88.757/42.536/122.885s. Context/renderer timers overlap and must not be added.
Reviewer independently inspected unconditional full authorized-description
copying in Context#with plus availability/render loops and Rust normalization.
Instrumentation forwards unchanged values and measures before CGI/assertions.
This is request CPU, not model startup or RSpec failure formatting. Anonymous
access makes worker exhaustion plausible; no actual production outage asserted.

Supported profile configuration cannot remove cost while preserving behavior.
A provider remedy and authorized version/adoption decision are required before
long integrations, readiness or deployment. Shared privileged HTML/context
caching would violate authorization.

Lead disposition: accepted Blocking, unresolved. Architect decisionB1 in
[design.md](design.md) identifies immutable-context structural sharing and
selected authorized-subtree normalization upstream. Exact published0.30.1
cannot silently include a patch. User choice asked asynchronously; no answer
or upstream/version change at this checkpoint. No long integrations/pushes/
merge/deployment started while blocker remains.

## R2 — Important — risk/compatibility and general

Reviewed WebUI39f8fd7d,src/lib/api/haveapi.ts:370-373,233-247;
src/lib/api/haveapiRequestClient.test.ts:177. Contradictory non2xx/status:true
is retained as ordinary HaveApiError, then ordinary401/403/422is classified
non-ambiguous. Status:true claims action success; HTTP error cannot prove
rejection. Shared mutation guards and VPS creation clear pending protection
on that false classification, permitting duplicate explicit submission after
possible success. Reviewer verified this also exists at base5a2d2bdc and
identified it candidly as a retained supported-boundary gap, not a new regression.

Requested correction: preserve HTTP/envelope/cause/receipt, fail closed as
uncertain, retain no renewal/replay, actual-library401/403/422+shared-guard
regression, actual status:false4xx still authoritative.

Lead disposition: accepted; implementer1 assigned narrow shared-classifier
correction and tests, preserving original authorship and consolidating owning
unmerged production commit. Lead inspected proposed early status:true check;
67focused cases pass so far. Final amended head/evidence inspection pending.
Reviewer's final report explicitly does NOT review future corrected head.
Under mandatory narrow-fix policy lead verifies requested correction directly;
rerun only affected lanes if implementation expands design/contract.

## Explicit history and migration conclusions

Reviewer independently found exactly two coherent commits per project, no
obsolete unmerged approach, intermediate pin, redundant update stream or
transitional compatibility path. A is one final HaveAPI adoption across real
Ruby/PHP/two callbackJS consumers; B is separate configuration behavior with
no second pin. C is one registry/provenance/Nix stream plus production adapter.

Old WebUI pilot0d05a258,proof5dd2333b,vendor3b2eed45,source8772bab are all
nonancestors of reconstructed head. Seven overlaps independently recomputed,
all69final paths mapped; unchanged carried paths equal8772bab bytes. Current
node tests, E2E entries and tsconfig scope preserved. Original author retained.
No supplied supported/deployed/released/external-consumer boundary requires
obsolete pilot/vendor history.8772bab is carried content, never literally
merged. Old local refs/worktree/records and PR74 alias remain separate.
Exact published-history rewrite authorization/lease plan still required.

**No migrations.** All316vpsadmin tracked migration/schema entries identical
across range; WebUI has0. Migration workflow/test filename changes are environment
or fixture changes. No new schema,seeds,data conversion,on-disk format or
migration consumption lineage. KB is one candidate preparation commit.
Consolidate R2into its owning production commit and refresh final inventory.

## Other lane conclusions and independent evidence

No additional Blocking,Important or Advisory findings.

- General: requested scope, coupled generated metadata, coherent purposes and
  rationale. New API spec is selected by shared full/core platform-config
  spec/lib glob; no topic hole. CI native deps precede Bundler. Ordinary hooks
  pass in owner evidence; no claimed long-suite pass.
- Architecture: HaveAPI owns transport,RequestSpec,wire codec and renderers;
  React adapter owns bounded translation,haveApiCall admission/renewal/projection.
  Consumers/public path/unchanged BFF recovery traced. Separate public/auth
  clients; no token cache,alternate transport/decoder,pilot/fallback production
  path. Legacy callback consumers correctly remain separate.
- Scope: no speculative SDK regeneration/schema snapshot/app cache/generic
  framework/BFF rewrite. ControlledXHR fixtures exercise actual dependency.
  Artifact guards are bounded to selected source; current-main work preserved.
- Risk: live credentials,base/scope isolation,stable original retry params/locale,
  one valid same-session read retry,explicit write resubmission,logout/identity/
  impersonation guards retained. No renewal on malformed401/network/abort.
  Profiles finalize private structural model after auth/routes; missing or
  mismatched generators fail startup. Rust Git SDK and Go module correct.
  Ruby client runtime diff only version; protocol2.0,API7.0 unchanged. Rollback
  couples API config/server/generators; no persistent/node change.
- Independently recounted174panels=168programs(52Go,58asyncRust,58blockingRust)
  +6explicitGo limitations,17sample identities,all program files present.
  symbol-audit0issues,compiled:false. Representative SDK imports/auth/init/
  path/setter/output code inspected; static review is not compilation.
- Both npm tarballSHA512verified; ALL53packed files matchHaveAPI1c3c98f0.
  Both legacy bundles and installed React bundle shareSHA256
  1448ad6f6ef8801f088410d7cf3be32cd00de613efb7be031445a9f0bc348593.
  Four cached0.30.1Ruby gems match registry hashes,locks/gemsets align; only
  required fiddle/tomlrb adds. Packaged libffi is evaluation evidence,not build.
- Owner callback12per bundle,PHP13/355,API2/0,WebUI324plus overlapping focused
  reruns,ci:quick/source/audits/signatures inspected; no sum of overlaps.
  Reviewer ran read-only source/history/provenance analysis,no tests/builds.

## KB conclusion

Candidate intro/authentication-through-end bytes preserved,including production
trailing spaces. New installs/version/sync-async/SDK guidance matches artifacts;
existing clients retained,both reciprocal markers correct. Original/candidate
hashes,real IDs,source revision/content guards,paths,localized summaries agree
with schema5manifests; no invented managed provenance.

Manual instruction inventory found no vpsAdmin WebUI action requiring nav tags:
login belongs to HaveAPI docs,remaining actions CLI/code/FUSE,WebUI/default-scope
references explanatory. Canonical failure is unchanged baseline IP-page drift,
not missing API tags or a claimed all-page pass. ExactPython/TSfixture and
Rustconsumer compile receipts supplied,no authenticated production proof.
Foreign staging untouched. Rendered links/history/summary checks still pending.

## Remaining gates

R1unresolved; R2final direct verification pending. No overall readiness,merge
or deployment approval. After blocker correction and review disposition:
emittedGo/Rust compilation/nested-nullable fixtures; packagedservices-up,
generator/Fiddle loads; full/coreAPI; PHP/consolebrowser; fullWebUIunit/build/
Nix/source/desktop-mobileworkflows. Fixtures do not prove realOAuth/member
mutation/task completion. Legitimate KBstaging and exact production approval
remain separate. Keep session open.

## Lead direct verification of R2 — closed

Final corrected WebUI head014f7b9c9f451d6275af73c4af30a24668b77b7b;
old reviewed39f8fd7d2bee0c4754f0f9921d97855da7fbdddf. Dependency commit
cd3577a6365685273c1b39a724814f7d67931508 unchanged; base5a2d2bdc unchanged.
Lead inspected entire old/new delta and range-diff, actual classifier and
actual-library/shared-hook regression code. Only5paths changed: one early
status:true ambiguity guard plus receipt comment, focused tests and matching
contracts/work-log. No new decoder/error class,transport,auth policy,guard
runtime/storage contract or generalized behavior. HTTP/envelope/cause/meta
remain intact, no renewal/replay, genuine status:false4xx remains authoritative.

Four focused files/67tests pass; final installed typecheck,scoped+directESLint,
format,design and structural audit pass under pinned fresh watcher(exit0,81s).
Lead inspected logs, tracked worktree clean and final whitespace check passes.
Original author/date retained; correction folded into owning production commit,
still two coherent commits and no repeated pin/migrations. Exact old reviewed
range,delta and source mapping retained in package-c/review-r2* and reviewed-*
artifacts; PR74plan updated but no PR/ref mutation.

This is the reviewer's requested narrow correction within the reviewed
uncertainty boundary, so mandatory-review step9 direct verification closesR2;
no automatic full rerun or unaffected-lane rerun. R1remains Blocking. No long
integration/builds/publication/deployment were started.

## 2026-10-25 registry adoption follow-up

Same reviewer0 completed affectedall4lane review of vpsadmin57a53e700
and KBdf1944a2: no new findings. Complete2commithistory/sourceprovenance/
registryprofile/init semantics/KBguards independentlyaccepted, no migrations
(316inventoryentriesunchanged). Detailedpacket/result in
[rust-registry-review.md](rust-registry-review.md). R1staysBlocking,user
ownsproviderremedy in another session; no readiness/integrationclaim.
