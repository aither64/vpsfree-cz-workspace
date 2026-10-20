# Final committed deliverable review

Final review is now requested. All intended source/evaluation changes are
committed, owner quick checks pass, final mechanical gate passes and whole
worktree/index are clean. No long/full suite or advisory writes have started.

## Request, session and authority

Session2026-10-19-vpsadmin-kernel-cves; workspace/home/aither/workspace/ai/vpsfree.cz.
Read plan.md,state.md,design.md and approved-cves.json. User approved exact60
assessments and unpublished drafts. Selection SHA256
8e9906fb11133cb7fafafbcb68cc7ec0900ee7f6e2e7ac50b1ca1af5b2b4b72a.
No publication, email, deployment, default integration or lifecycle authority.

Repository:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories
Feature:2026-10-19-vpsadmin-kernel-cves.
Recorded remote default:2026-07-13-security-advisory-automation.
Base:ea6247687fd02417f87e1e5593fecd8b9055925d
Final source/evaluation head:34ad7d5785382215cbe00b5140174cad5661a132
Last fetched target remained base; no claim of later remote freshness.

## Complete branch history and dispositions

```text
69027fd51efc5c7eb0a4711947b4f9d08190940e docs: define kernel CVE selection before advisory drafting
605d274310890aac5f514924d9b6566033feaee4 Assess 20 packet and network kernel vulnerabilities
42f1e9ee272fa60f8013b5280dd50846439efaef Assess nineteen approved core and virtualization CVEs
3ab9740a964f053d20a2de1e5e89e1f71cc3c650 Evaluate vulnerabilities introduced by exact livepatches
018520cfb8c34eb0bb71258d6eae5e198186c340 Assess the perf regression introduced by historical livepatches
34ad7d5785382215cbe00b5140174cad5661a132 Assess filesystem, MPTCP and XFRM kernel vulnerabilities
```

Final diff:189 files changed, 24008 insertions(+), 20 deletions(-).
Six coherent commits: reusable selection instructions;20 networking assessments;
19 core/KVM/BPF/RT assessments; supporting exact livepatch-introduction model;
74753 dependent custom-regression assessment;20 filesystem/MPTCP/XFRM assessments.
Each assessment contains analysis,YAML and frozen per-node evaluation. Distinct
packages are independently reviewable; the perf dossier depends on its preceding
tooling commit. There are no obsolete intermediate designs or fixup commits,
no repeated dependency/channel/generated pin streams and no migrations. No
new database schema, protocol, API/client, kernel/configuration or deployed
service change. Source is not merged, deployed or used for draft writes yet.
No consolidation needed on this source series. Independently assess these
history and migration conclusions; do not rely only on this packet.

## Risk, lanes and reviewer

High risk: public security/tenant-isolation claims and evaluator outcomes.
Selected retained reviewer0, gpt-6.1-sol/xhigh/read_only, purpose review,
independent of authors. Read mandatory-change-review SKILL.md and all four
references: general, architecture, scope and risk/compatibility. Perform review
yourself with no nested reviewers. Earlier docs review of69027fd does not
replace this complete final branch review. No implementation edits or API/Git
mutation during review. Report findings with severity/path/line and concrete
consequence, plus explicit whole-branch history/migration conclusions and limits.

## Acceptance and sources

Exact approved60 mapped once in assessment/packages.json. Authors0/1/2 own20
per package; lead directly reviewed EN/CS texts under writing skill, receipts
assessment/editorial-*.json. All primary records, stable release joins, exact
HTTP fixes/Makefiles and current downstream source snapshots are retained in
research/ and assessment/owner paths; use each analysis for immutable URLs.
Canonical repository guidance:AGENTS.md,docs/cve-selection.md,docs/evidence.md,
README and docs/api-permissions.md. No exploit execution/instructions.

Check complete mainline/stable/backport introductions/fixes and EOL openbounds,
actual source prerequisites and roles, scoped negative claims, formal CVSS
attribution, VPS root versus node control/cross-VPS access/availability,
protections versus detection, coherent current/history and exact mitigation.
Member relevance is independent of exposure; not-affected findings require
positive scoped evidence. Unknown/vulnerable states are permitted in unpublished
drafts and block publication readiness. No invented safe outcomes, copied history
attestations, ignored YAML keys or manual evaluation edits.

## Specific consequential checks

-64387: named stable fixes6.6.145/6.12.96/6.18.39 modify wrong functions. Effective
 bounds remain null for those branches; mainline7.2 and7.1.4 fix verified. Only
6.12 additionally inspected through downstream.113. Official claims preserved
 as disputed provenance. See assessment/CVE-2026-64387-correction.json.
-74753: source037a3c43 introduced in mainline7.2-rc1 and older stable backports,
6.12.96..108. Observed cumulative.95.2-.6 introduce it without EXIT checks.
 Canonical release bounds must remain exact; runtime rules model custom source.
 No7.2/RC observed in frozen current/history; older RC parser caveat remains
 scoped in assessment/prerelease-boundary.json.
-Source-bound platform.affected_livepatches requires dossier schema2, oldloader
 rejects2 and schema1rejects newfield. Existing schema1 behavior must remain.
 Active exact introduction precedes nominal safe version/build; inactive does
 not introduce; transitions/missing or mismatched identity/ambiguous inventory
 and release-only introducing family stay unknown. No state across reboot,
 no unsupported protection-wins ordering or duplicate transition engine.
 See focused specs, docs/evidence.md and design brief. Evidence/evaluation/
 submission schema unchanged. Tool rollback requires withholding schema2 dossier,
 not relabeling it1. No coordinated node update or service deployment.
-99999 assessed tenant route already requires administrator; external microVM
 host execution attributed, no reproduced platform escape or ordinary-user path.
-98368 IPsec setup authority differs from ordinary sender on existing path.
-CIFS no FS_USERNS_MOUNT does not exclude ordinary fileusers of host-prepared
 mounts. Host mount state is conditional/unmodeled, not proven fleet absence.
-MPTCP/RT disabled exact archived build is not never-vulnerable fleet history.
 BPF/token/module/CPU/LSM conditions remain qualified, not generic safe predicates.
-74597 IPV6_TUNNEL built in; separate host mip6 registration prerequisite.
-Observed11 source-bound v6 corrections accepted;74630 whole-helper fanout
 unproven so v6 blanket mitigation withheld. Quarantine does not erase verified
 old activation and does not become a deployment recommendation.
-Lifecycle126 override independently verified from source commit+parent and
 same-day retained firstboot; globalJan1 unchanged, scope not invented exact
 deployment instant. No override for missing storage161. See node126-lifecycle.json.

## Frozen evidence and checks

Ignored restricted.state/evidence.json SHA256
61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274,
schema8,13nodes,collected2026-10-19T21:48:39Z. One existing collector successful,
no per-CVE recollection. Raw evidence/logs stay restricted, no credentials in
artifacts. Owner3 mechanical receipt and architect existing offline reuse guard
pass. All60 evaluation files generated by existing normal tool, not hand edited.
Raw Node/event references only ignored.state or repository's supported evaluation
records; sanitized session ledgers should not expose raw component snapshots.

Quick checks: owner normal Nix CLI validate/evaluate/readback, exact sourcefix
joins, local links/whitespace, normal active Overcommit precommit/commitmsg hooks
for every commit; no bypass. Supporting targeted RSpec113 examples/0failures,
4Rubyfile RuboCop0offenses. Old69027 loader accepts schema1/rejects schema2;
new loader accepts supported1/2. gitdiffcheck base-to-head clean. Owner0 earlier
commit paused for owner2 WIP lint; author fixed lint, normalhooks then passed.

Final mechanical gate at exacthead: all111 dossiers loader valid,110schema1+
one2; exact60 new=59schema1+one2,13exactnodeIDs, frozen SHA/evidence/node-set/
collectiontime/dossierdigests allmatch; summary states/counts/flags/blockingsets,
primary fixedsha/version (documented64387exception),74753canonicalbounds,
prior-report dedup and localizedpresence allpass. No errors. Read
assessment/implementer3/final-acceptance-result.json. This checks consistency,
not independent security correctness. Fullsuite waits this finalreview.

## Operations and recovery boundary

Read assessment/implementer1/draft-sync/README.md and exact order.json. Prepared
explicit per-CVE steps only, no new API/client/framework. After finalreview and
assigned checks, singlewriter1 uses existing dry-run/apply with explicit frozen
snapshot, exact draft/CVE/text/node/revision readback and one normal-hook
submission.yml commit before next CVE. Stop on first uncertain outcome; existing
external-ID/revision recovery only, no automatic retry/adopt/recreate/delete.
No ready/publish/mail. Finalsourcecommit may be externally bound by later
submission source_commit fields; preserve those recovery boundaries. No such
external writes exist at this review boundary.

Project explanations changed:docs/cve-selection.md and routing,docs/evidence.md
for source-bound introductions; per-CVE analyses own durable assessment rationale.
Temporary release/verification/operator details remain session artifacts.
No remaining generic documentation backfill or new skill framework required.
