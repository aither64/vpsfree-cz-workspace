# Committed narrow review remediation

Final head `670cf286daf9bddb65594035507ca112a9e6d397`, parent
`8e71e70e76276931c8ffe60b5368f508d349ff22`, tree
`51c71ab123c4f10266fafb9b2e895c78d0915053`, base
`1c8478bceb3943645ec06ccde895ee4b0985873f`. Source is frozen, fully clean,
index empty, no Git/check operation. W returns its sole source/Git/index turn.

R040-1 implements the completed review's exact requested remedy. The accepted
parent's returned revision is validated inside the existing post-parent try.
Existing AdvisoryChildSequenceError is preserved; a non-sequence failure becomes
AdvisoryChildSequenceError([], cves, originalError). The existing saved_without_cves
wrapper/cause and onError retain parent identity, requested CVEs, empty accepted
children, remaining intent and persistent no-replay block. No EditorModal change
or new recovery mechanism was introduced. Parameterized active-hook cases for
null and revision2 after reviewing0 prove parentonce, zero child reconciliation,
original concurrent cause and retained intent/block across direct close, fresh
revision1 reopen and attempted resubmission. Existing assertions remain intact.

A040-1 remains an accepted inherited limitation, not a migration regression.
The collector algorithm is byte-identical to revieweddb90. The API sorts CVEs by
cve_id, while HaveAPI filters primary ID>from_id. With101 lexically ordered CVEs
whose IDs descend101..1, the current short-second-page stop can omit ID1.
Producer/cursor alignment with a nonmonotonic-ID regression is a concrete separate
follow-up; no API/backend/SDK or paging algorithm was changed, and no runtime cap
is claimed. The lead-approved paragraph qualifies the existing guarded-advisory
API contract. Unrestricted multi-page CVE completeness in older packet language
is superseded by this explicit limitation; no multi-page certification is made.

The complete four-lane report remains immutable at
[webui-040-final-review-result.md](webui-040-final-review-result.md), SHA256
`444043bbbb9d73833f4feae2ccaaa524fadcc7c8390a2639676bbd31fc0766dc`.
Exact revieweddb90 is retained at
`refs/keep/2026-11-01-typescript-client-migration/040-reviewed-db90da33`;
original4ed recovery ref and all37 old raw objects remain literal. The source/test
fix is folded into infrastructure owner `7928352fc2cbb65d73b09c724007b7862ad8f6dd`;
the paragraph is folded into the owning final docs commit. All36 reviewed stages
preserve original authors, author dates and messages. First client introduction
`41919ba1` remains literal, selecting only final0.4/ordinary hash. No new input
stream, obsolete hook/archive path, DB/schema or persisted-format migration.
Old4ed remains a nonancestor semantic lineage with unchanged preview evidence.

Exactly3 paths differ from revieweddb90, +87/-2: the correction hook, its active
recovery tests, and the single API_CONTRACTS paragraph. All other2592 tracked
blobs/modes match. Entire2595 final contents/modes match the successful R040
snapshot. All1139 production hashes match the fresh scan, with zero legacy helper
aliases/imports or handmade advisory descriptors. All23 protected inputs,
2 deletions,0.4 lock/peer/npmDepsHash/484 unrelated records,11-node committed lock,
143/140 baseline/options/survivors and unchanged tooling/E2E inputs are retained.

Focused4files/9tests pass; leaflint/format/whitespace and approved paragraph
format/docs audit pass. Affected application strict native0/57.974s with zero
diagnostics ran on the exact frozen working source based atdb90. Its source
identity matches the final commit; this is not literal-final-head build/CI proof.
Captured nativePID1026694/start33054989 is absent. No install/prefetch/tooling/E2E
blanket repeat or new Nix/browser/API action occurred.

Artifacts: [completion receipt](w-040-r040-final-completion-receipt.json),
[full36 series](w-040-r040-final-series.json),
[history/input proof](w-040-r040-final-history-input-receipt.json),
[three-path delta](w-040-r040-reviewed.delta),
[reviewed/new range-diff](w-040-r040-reviewed.range-diff),
[original37/new range-diff](w-040-r040-original.range-diff),
[full final diff](w-040-r040-final.diff),
[all path bindings](w-040-r040-final-path-bindings.json),
[fresh source audit](w-040-r040-final-source-audit.json).

The held Nix5 preparation is rebound to literal670 and unique session result
roots in [new preparation](w-040-r040-final-nix-preparation-receipt.json).
It explicitly supersedes, and retains, the unexecuteddb90 preparation. AST/bash-n
only; actual5DRV/output/source/NAR/npmcache/recursive graph/installed build-info
remain for the parent-authorized native build and bounded postbuild inspection.
No derivation/graph equality or build pass is inferred from source equality.

Parent direct committed-fix verification under mandatory-review step9 remains
pending, followed by actual final publication/rootedNix5/requiredcore+three native
PR-smoke CI and conditional integration. No automatic whole-review rerun is
requested for this exact remedy. No default merge, preview/backend/production
change or lifecycle action occurred. Session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
