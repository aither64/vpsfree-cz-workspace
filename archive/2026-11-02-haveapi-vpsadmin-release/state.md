---
lifecycle: archived
---

# HaveAPI 0.32.2 downstream release

## Archive-only repair — 2026-11-12

The user reactivated this retained session only for archive-readiness repair.
Ordinary release/development work remains complete and paused. The approved
coordinator is `2026-11-11-session-archival-failures`, request
`25d83046-2c9c-4dd7-af62-c01aa81762cd`; runtime grant
`f2e5903509df4a2f4bd1d15d68be93e7` authorizes deliberate lead messages.
The user wording was “Reactivate, repair, and archive”; the current direct request
assigns archival to the coordinator. No lifecycle or monitor evidence is edited.

- [x] Verify exact session identity and retained team settings.
- [x] Confirm ordinary archive-check: ready=false, 5/6, 960 unmanaged entries.
- [x] Implementer3: moved the whole owned `haveapi-ts-tools` clone atomically
  to `/home/aither/archive-preserved/2026-11-02-haveapi-vpsadmin-release/haveapi-ts-tools`;
  the old worktree-group path is absent. Completed at 2026-11-12 21:13:30 UTC.
- [x] Lead: accepted preservation evidence and independently verified clean exact
  HEAD/tree/origin and identical before/after inventories.
- [x] Ordinary final archive-check: `ready=true`, **6/6**, **0 blockers**.

All 960 regular files and 232 directories (5,617,261 bytes, including `.git`)
are preserved; content, modes, owners, inodes, link counts, mtimes and sizes match.
The before/after inventory SHA256 is
`e691eccb2f447cf9d4b97fccb13295b3e8191a1a49927cf97b036dbdb49deea2`.
HEAD remains `1ef9b204ba45bb261d3334be5c555cc1856b713b`, tree
`fda4d5c159746ffa91887ead63197e7b788e0a64`. Existing Git object alternates still
point to `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git/objects`;
those canonical objects remain a dependency of the preserved clone.
Full preservation evidence is beside it in `haveapi-ts-tools-preservation-evidence/`.

The member report tool rejected delivery despite verified retained membership;
ordinary same-session CLI messaging delivered the final result without settings
or registry changes. No readable process reference or actual writer was found.
Four inaccessible infrastructure processes were not treated as proof of source
use; inventories remained equal across the move. No process was signalled.

Remaining: coordinator receives readiness and performs the authorized ordinary
archive after this repair turn ends. Lead remains available; no further repair,
release/development work, or competing lifecycle action is scheduled.

No archive/delete/stop/retry, merge, deployment, ordinary development, shared
infrastructure change, or lifecycle/monitor evidence rewrite is assigned here.

## Current status

Complete. All five registered exact final feature heads are integrated into
freshly verified remote defaults. TypeScript 0.3.0 is published and its registry
tarball equals the original approved artifact. Go/Rust generated code is unchanged,
so no releases were made for them. Configuration channel update is merged.
Session remains open; no archive/delete/stop or delayed lifecycle action.

## Phase checklist

- [x] Verify exact session/retained team and authorized peer communication.
- [x] Architect design, compatibility and independent execution packages.
- [x] Confirm published HaveAPI 0.32.2 and exact source/registry identities.
- [x] A: coherent vpsAdmin/exporter update, quick checks, review and services-up.
- [x] A: master integration and fresh remote proof.
- [x] B: Go generation/format/compile, no-code/no-release outcome.
- [x] C: Rust metadata-only refresh, quick checks/review/main integration.
- [x] D: repeated clean full-fixture export, generation/checks/commit/review.
- [x] D: main integration, v0.3.0 tag and npm original-artifact verification.
- [x] E: channel-only update/checks/review/master integration.
- [x] All final remote heads/cleanliness/claims verified; handoff reconciled.

## Final repositories and owners

All feature refs use 2026-11-02-haveapi-vpsadmin-release; source worktrees remain
under worktrees/2026-11-02-haveapi-vpsadmin-release/. Canonical SSH remotes are
 git@github.com:vpsfreecz/<project>.git.

| Package / owner | Target | Review base | Exact final head |
| --- | --- | --- | --- |
| A vpsadmin / implementer0 | master | 1d4869b6e81dd60916ecb96688ca14a192000b1f | 5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5 |
| B vpsadmin-go-client / implementer1 | master | 134a9e69f9aa6ddec5c94b53744865c6f81ecdd0 | 134a9e69f9aa6ddec5c94b53744865c6f81ecdd0 |
| C vpsadmin-rust-client / implementer2 | main | 1ab58627a225589fefc983829de5c4cfee770b3b | 3ec8c045dcefcca85b60ffccd38259cda29eeb60 |
| D vpsadmin-typescript-client / implementer3 | main | e5786f69b7c223c3bb5b1de99b7f97186eec368a | d354491537f8b654b4d2c33a705cad84474f95d6 |
| E vpsfree-cz-configuration / implementer2 | master | c040c14cdbacc07998700b524996a89306188d7f | 0d71dd289feeb1ea2686f9c7cf0f93728baf9bd2 |

Final explicit fetches, SSH ls-remote reads and ancestry checks prove every
feature HEAD equals the corresponding remote default and every source worktree
is clean. Comparisons captured for A/C/D/E. B zero-range capture is unsupported
(base=head); no fictitious comparison was created. Rust genuine creation base
80be1c1a90b7009f8ddecf6a7fe042b506de8b42 remains recorded; fresh fetch advanced
the clean feature to actual main with already-published lock tooling. No rewrite
or unsupported equivalence certificate was used.

## Authority and session identity

Initial user request explicitly authorized vpsAdmin master, changed-client
merges/minor releases/publication and final configuration channel integration.
Rust/TypeScript actual defaults are main. No deployment requested. Broad long CI
not awaited. Initial substantive plan/state commit e263572c6 preceded source work.
Normal tracking cadence retained; source commits and publication evidence are
complete, final local records remain in this open session.

Current prints exact slug2026-11-02-haveapi-vpsadmin-release and both initial
DEV_SESSION markers matched trusted workspace binding. Reviewer absent markers
were resolved through current from exact trusted tracking directory, independently
reproduced by lead; no member/access/settings change. Architect0 Astra/xhigh,
implementers0–3 Sol/xhigh/workspace_write, reviewer0 Sol/xhigh/read_only retained.

User approved peer2026-11-02-backport-and-publish-release in initial message;
exact-pair grantc61cca2368b7b2cd5e144bc85b118e6c. Deliberate lead messages only,
no peer file/worktree/team access. Upstream final publication/hash messages
720f8965-41de-4b6f-9335-8f904c05d342 and c3217ac5-8415-4ce4-bf37-a5c144f3ff51.

## Publication and source inputs

HaveAPI v0.32.2 source1ef9b204ba45bb261d3334be5c555cc1856b713b, annotated tag
7f8f656ca7655bafaf2cf5e7095573806085a442; original run41529223599/1 and artifact
13181726847 succeeded. Release manifest SHA256
7c53624cc059434279e6eba6f8a9ec151a57897f41e96f0b1d261e1b58fa728b contains exact
component locks. All five Ruby0.32.2 registry hashes independently verified and
actual downloaded bytes match generated Nix hashes; A receipt preserves graph.

Two independent fresh-process/fresh-DB full-fixture exports from clean reviewed
and finally integrated A5586ea8ab are identical for all3files. API7/protocol2,
151resources/519actions/8720parameters/all6plugins preserved. Schema SHA256
476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794;
provenance d51cfb24217fb381f66c1a0eb46168c637fea7ec988beb7e54b2d9a679ad81b6;
lock62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c.
Export receipt retains seven fixture hashes, six plugin source/migration inventories
and five gem identities. No A rebase, so D exportedSHA==integratedAfeatureSHA;
fresh remote equality checked before D merge.

TypeScript v0.3.0 annotated tag5a51d6b108da9e57b10494bdf089b61a270b167b peels
exactd3544915. Original tag workflow41538988296/1, artifact13184014717,
eligible concrete-artifact approval deployment7505242931, build/publish SUCCESS.
No settings/credential change, local upload, republish/repack/rebuild/tagmove.
npm processing caused initial404; fresh200 observed22:45:41UTC. Downloaded registry
tarball byte-identical to approved original, SHA256
57236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610,
integritysha512-jZKO+c9azQqwXYLMp+yCl54pqhjyGDVr6rxOzq2rjusEBQ8Xm5dCdc8a2iHV5buUq8hc6835tmF5wjlP8/HJ/A==.
Owner and lead verified independently. Exact npm peer/dev runtime0.32.0 retained.
SLSA payload binds archive/source/tag/original run; no separate crypto verifier
claim. [Publication receipt](typescript-release.md).

## Checks, independent review and integration

[Handoff](handoff.md) summarizes all successful checks. A28focused examples,
required hooks, real gem-byte hashes and services-up34PASS; B682files identical,
format/compilePASS; C686source hashes unchanged, determinism/provenance/fmt/10refusal
checksPASS; D13tests/build/typechecks/packed actual-runtime consumer/source-refusal
and deterministic checkPASS; E64-node semantic equality and35s evaluationPASS.
E109entries/all17services consumers exactA source
/nix/store/id5q6lvgxqr8z34354db87yhmhcxdf6y-source; only rev/time/NARhash changed.
No machine toplevel build/activation. [Services-up receipt](services-up-receipt.md)
retains exact realized closure paths/source graph, native expected_success and
original11m24s run. No owned test/build/utility process remains.

Independent reviewer0 final reports: [A](review-a-result.md), [C](review-c-result.md),
[D](review-d-result.md), [E](review-e-result.md). No findings, obsolete history,
repeated update streams or migrations. A/D all4lanes/high-risk public contracts;
C/E mechanical-content exemption with independent complete general/history/input
assessment. A/C/D/E each one coherent final commit; no remediation/rerun needed.
No standalone change review for B zero deliverable. Broad long vpsAdmin CI was
observed running with lint/i18n successes, not awaited under explicit scope.

All merges ff-only through fresh clean temporary targets, required hooks enabled,
non-force SSH pushes and fresh exact remote proof. Ownership released before
records/CI/cleanup; all4 authoritative states rechecked released:

| Package | Claim | Verified release UTC |
| --- | --- | --- |
| A | f62de560-92ec-4e36-9375-356f8bf4a27d | 22:28:28 |
| C | c19a5c18-3374-4d70-a5a9-7bf6c5c3acec | 22:29:48 |
| D | 8546b779-22e4-468b-b06a-f19a2d4df080 | 22:37:33 |
| E | 821b4dc0-f8b5-4c46-a8f9-789845a730a2 | 22:56:52 |

No machine reservation/deployment. Detached /tmp/hvrel-merge-* targets removed
with ordinary Git only after exact integrated-head/cleanliness/detached proof;
feature refs/worktrees retained. No session cleanup/lifecycle helper invoked.

## Documentation, reconciled issues and remaining work

[Design](design.md), [A package](vpsadmin-package.md), [Go](go-package.md),
[Rust](rust-package.md), [TypeScript](typescript-package.md),
[configuration](configuration-package.md) retain detailed evidence and source graphs.
Main-agent writing pass applied to exporter docs/help and TS release prose.
No permanent docs were invented for routine channel pin; exact technical guidance
stays with owning repos. [Bundix note](../../notes/vpsadmin/2026-11-02-bundix-root-bundler.md)
records ordinary shell-rake correction without task-source workaround.

All setup/interruption effects reconciled: delayed utility metadata overlap ended
before final isolated retry; default JSON preload removed; source tooling false
registration repaired through independent exact clone, branch retained, idle owned
tmux cwd moved/no old refs. No actual feature obligation dropped. Brief services-up
monitoring interruption resumed same original operation, not a relaunch.
Package receipts retain exact recovery evidence; no unfinished command/journal.

Remaining work: none. Blockers/known material risks: none within completed scope.
Next action: none required. Production deployment/live activation remains outside
this request. Session is open for follow-up, with no scheduled lifecycle action.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/
