# HaveAPI integration refresh review packet

User directed in this conversation on 2026-11-02: "so I'd say merge the changes
into haveapi master. I'll handle release in another session." Then: "when haveapi
is merged, continue your work on vpsadmin-webui". Scope is HaveAPI/master only;
release/version/tag/publication and other default branches are excluded. WebUI
is held at b00877a6 with two validated adoption JSONs unstaged.

This packet covers a clean refresh of the completed, independently reviewed
HaveAPI feature. Retain original foundation, narrow-remedy and terminology
conclusions. The affected review is general/history and risk/compatibility for
the new upstream baseline and preserved provenance. Architecture/scope design
is unchanged. Overall original risk remains HIGH (generated public contracts).
Do not repeat unrelated WebUI/source or original generator audits.

- Original reviewed final range: 391b0190241cf195a69b06f7297d3e4eebec5a83..
  52c37027f194ba1141fb7f5e5b6b45828989b126, two commits eea3ae5e and 52c37027.
- Fresh master: eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7.
- Prepared candidate: f29c1e4675bc1f79641faa619b8c68ecec923c71,
  tree 63e1cfcee1ff75a9cc03e5f18ebbf7d44eec76e1; commits 83689f88/f29c1e46.
- Candidate worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/haveapi-integration-candidate.
- Original worktree/remote feature remains literal 52c; original remote ancestry
  keeps consumed generator eea3 fetchable. Candidate is a separate branch.
- Exact original/new paths: 26, +500/-62. Ordered stable patch IDs match, and
  range-diff reports both equal; no conflict resolution or new source edits.
- No DB/schema/persisted-state migrations, repeated dependency/input updates,
  new version, generated archive or downstream pin. VERSION stays 0.32.0.
- Upstream documentation/localization source changes can change the candidate
  generator source digest. Candidate is not the selected generator eea3;
  client99ee and WebUI archive/provenance/pins remain untouched. Do not certify
  old 52c as literally merged when its successor is nonancestor-equivalent.

Evidence: artifacts/package-s/haveapi-integration-preparation/equivalence.json,
range-diff.txt and final preparation receipt/check logs (to be supplied before
assignment). Read complete actual ranges and relevant upstream intersections;
independently verify equivalence, correct retained old refs, current contract
compatibility, coherent two-commit split and explicit no-migration/update-stream
conclusions. A supported consumer requires exact eea3 reachability, so preserve
its remote ref. No release is requested or enabled by the review.

Retained reports: foundation-review-result.md (R1/A1 narrow dispositions included),
local-client-terminology-review-result.md (full final HaveAPI two-commit history),
foundation-integration-result.md and provider-client-ci-2026-11-02/summary.md.
The three HaveAPI CI runs passed at actual52c; do not relabel them to candidate.
Any new quick checks and hook results must bind actual candidate and be appended
from the final preparation receipt before reviewer assignment. No long tests,
claim or integration launches before this gate settles.

Reviewer must read current mandatory-change-review and the assigned general/risk
references and repository guidance. Remain read-only; no tests/build/install,
Git mutation, publication, default merge, release or lifecycle action. Report
findings first and the reviewed exact ranges, settings, evidence and residual
limits. Parent persists the full report and owns integration acceptance.

## Actual completed quick/preparation evidence

Owner confirmed candidate f29c clean on eb91 and detached target eb91 clean.
Both checkouts use realized Ruby3.4.11/Git2.56 and existing G gems; mandatory
configuration verification/all three custom hook signatures pass, with no signing,
install or bypass. Scoped IR/emitter19examples pass in3.93s, including strict
TypeScript/negative/request-spy checks. Logs hook-trust.log/quick-ir-emitter.log
and environment.sh are under the preparation directory.

Candidate generatorSHA1349e1374da696a6411c14cdd5fbf7164f92426d44dddcc042ecd747df8978f4
differs from consumed eea3 only due upstream documentation.rb; shared schema0.32
and e12f graph are unchanged. Review this concrete baseline intersection.
Masterpush runs build-only release checks; publication is tag-only and protected.
The attempted comparison capture refused the deliberately retained registered52c
head; owner is aligning that local registered feature to exact prepared f29c by
ordinary empty-range rebase outside claims, preserving remote52c and old refs.
Candidate source/commits remain frozen and its report scope does not depend on
that registration bookkeeping. Long checks and merge remain held.

## Preparation completed

Final preparation receipt is now available at
artifacts/package-s/haveapi-integration-preparation/preparation-receipt.json.
Registered local feature was aligned to exact f29c by ordinary zero-commit rebase,
originalremote52c/oldrefs remain. Ordinary comparison capture succeeded for
eb91..f29; original refusal log is retained. Clean detached target remains eb91.
Ready commands are in ready-commands.md beside the receipt. No claim acquired.
