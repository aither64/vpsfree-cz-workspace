# Rebase for approved default-branch integration

User explicitly authorized HaveAPI/master and vpsadmin-rust-client/main merges
on 2026-10-21 and said no releases yet. No tags, registry upload, dispatch,
secret setup or token file access is part of this action. No claims during
preparation/review/verification. Lead owns claimed final merges/proof/release.

Original reviewed source: HaveAPI9e4c29a over5266481, three commits. Original
client091bd70 overneutralb67, four commits. All original fullsource, DELETE,
history, README and Actions reports retained. Exact prior feature CI passed.
Fresh target HaveAPI/master7835acafdda19779815a0f1ba905d78e0085456d has21
upstream commits, including Python and JS clients, Nix pin02c087 and Ruby3.4.
No upstreamclients/rust or servers/ruby change; clients/ruby only spec-support
bundle-lock selection. Rebase overlap in Makefile/README/developmentdocs/flake.
Retain upstream behavior and Rust additions, no new interface/schema/runtime.

New final heads and quick evidence: pending. This packet is not a review
assignment until intended commits and quickchecks complete. Preserve prior
runtime/generator digests, all686client generated Rust files, snapshot/locks,
and public signatures; client provenance revision refresh only if needed.
No migrations or intermediate consumed schema boundaries. Retain original
pin9e4 ref needed by current published client until mechanical refresh lands.
Whole branch series and range-diff/resolution inventory required. Prior
reviews not replaced; affected lanes assess new baseline integration and
history/provenance. New Nix/Ruby inputs need fresh scoped verification, no
whole-matrix source/tree-only reuse. Unchanged clientcrate/compiler inputs
can retain exact prior tests when independently bound by hashes/derivations.
No default branch mutation until final review/checks/currentclaims/prechecks.

Reviewer remains retained reviewer0 Sol/xhigh/read_only. Read mandatory-change-
review and applicable lanes. Suggested all4lanes for cross-component baseline
conflict resolution and workflow/toolchain input impact; focus on actualdelta,
not repeated entire original audits. No source/Git/check/build/CI/server/
registry action by reviewer. Exact completed series and evidence will follow.

## HaveAPI final committed scope (ready now)

Final HaveAPI68cc80b012b7a6b9bcdf35c008c338cbc3f4c000 over
7835acafdda19779815a0f1ba905d78e0085456d, treeba13c1b6183ba225af5ca12e023827e95aeba621.
Three commits77dd0418(runtime),03c765bd(generator),68cc80b0(integration).
Complete proof/range/overlap: haveapi-integration-rebase-proof.json,
haveapi-integration-rebase.range-diff.txt, haveapi-integration-rebase-overlap.diff.
All56nonoverlapfeaturefileblobs match9e4; all183nonoverlapupstreamblobs preserved.
Rustsubtree exact unchanged. Runtime/integration stablepatchIDs equal; generator
changes only upstreamcontext and listresolution. Initialbasec14 preserved.
No migrations, obsolete history or repeated update streams. Preparedtarget
haveapi-master-integration clean7835. No claim or default mutation yet.

All3final commits explicitly ran required hooks and tempfile-F amendments with
newNixRuby3.4.11/Overcommit0.73.0, no bypass. Logs in haveapi-integration-rebase-
{runtime,generator,integration}-hooks.log. Ruby26filesyntax, Nixparse and diffcheck
passed. Formatter attempt could not launch GC'd oldCargo binary; unchangedRust
source previously formatted; freshwatcher must verify current tools/fmt. Hook
setupwatcher passed67.14sec; locks unchanged. No source/build tests rerun yet.

Client is independently receiving ONLY generatorrevision metadata rebind; its
final4commits/evidence will be sent after source freeze, and can be checked in a
subsequent general/history addendum. Review HaveAPI completed scope now; do not
review partly edited client or infer its finalhead. Prior actualclient091bd70
reviews/sourcecontract remain applicable. Selected all4affectedlanes for current
baseline conflict/toolchainintegration; no repeated originalfullsource audit.
Suggested freshverification: generator/unit/no-serverfixture, currenttoolidentity/
fmt/runtime, genericroot+mounted, extractgem/fullsnapshot. ActualserverRuby change
needs explicit scoped acceptance; client/MSRV inputs otherwise unchanged.

## Final client now ready for same review

Frozen client56c4c9d78bc36ccedb5d4173832a61176d24c8d2, tree
da0004a40271d5f91dce8c7ab8e2f1751e38af49, clean. Exactly4logicalcommits
aboveb67:11a1a39bpackage,1abe449agenerated,7e760176README,56c4c9dActions.
Old091..finaltree changes ONLY schema/provenance.json generatorrevision9e4->68cc.
All709other710trackedfiles unchanged; all687srcRust and generatedmanifest match.
Generator/runtime/schema/Rubylock digests recomputed equal; no regeneration.
Metadata refresh foldedoriginalpackage, generatedmessageSHA updated, no redundant
update stream or migrations. Original091 retained localref for evidence; old
remotefeature still091 until reviewed exactlease publication.
Evidence client-integration-provenance.md/json and .range-diff.txt; all710SHA256
recorded, owned686generatedhashes verified. Quickprovenance/bash-n/whitespace
passed. No source/compiler/lock/API/test/workflow changes. Mainneutralb67 still.
No tokenaccess/tag/release/registrysetup. Now include finalclientgeneral/history
and exactsourceinputproof in active review; no extra source audits required.

## Direct Advisory correction accepted by lead

Reviewer flagged sharedNixpin wording only. Lead's exact2lineown-pin correction
was folded into clientpackage; finalHEAD945af6a97717a7a6373507bbc9592d5cd53727c2,
treec993cef64194e86bac41c073409d345846eecf8a, clean. Fourcommits3353620f/
38750a52/f5f28cbb/945af6a. Comparedreviewed56c4 onlydocswording differs; direct
Gitdiff reviewed and accepted, no contract/source/input change. Comparedold091
exactlytwofiles: provenance1+/1-, developmentdocs2+/2-. Evidenceupdated and
708otherfilesunchanged; Rust/README/Actions unchanged. No furtherreviewturn
needed for directnarrowAdvisoryfix; retain reviewed56c4references and finalmap.
