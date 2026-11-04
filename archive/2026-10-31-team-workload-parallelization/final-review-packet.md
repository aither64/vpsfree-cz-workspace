# Team package workflow — final review packet

## Current shared-master integration preparation — 2026-11-04

Final target is shared master `5840893834f1d76e2bf3401a9d043e588f636442`,
feature `2b5944e8df2ba06fb3193264c231adafa8329b5c`; complete two-commit series
is A `ebf00e3cbea124ce49289afa3d584ac60c9621c2`,
B `2b5944e8df2ba06fb3193264c231adafa8329b5c`.
Remote default remains `12a3df65467c7c460cae5e0a3cd8dca60138288e`, an ancestor
of shared target. No shared/default branch was mutated by preparation.

The previously reviewed/tested range below remains unchanged. Rebase onto the
shared target is exactly patch-equivalent: both range-diff entries `=`, same
ordered stable IDs and independently reconstructed full final tree
`8a60019df0cc10a30742f0534180d57d1ed6da44`. Incoming paths are exclusively
the installed certification policy's non-behavior `work/archive/notes` paths.
No conflicts, feature edits, migrations, obsolete history or update streams.

[rollout.md](rollout.md) contains the schema-1 accepted original review binding,
report hash, exact old/new ranges, independent scratch-index reconstruction and
installed merge-tree proof. [shared-target-equivalence.json](shared-target-equivalence.json)
uses the installed schema-1 proof shape; lead independently verifies it before
accepting mechanical review reuse. Original reviewer0/settings/report are retained,
with no claim that reviewer0 independently re-reviewed the new head. User approval
persists for the equal patch.

Lead completed its own scratch-index reconstruction and accepted
[shared-target-review-reuse.json](shared-target-review-reuse.json); original
review/report and exact binding are preserved, with no test reuse. Utility
`/root/integration_checks` now owns the required three-output batch on frozen
2b5944e8. Git executable, shared-root hooks/target/index readiness and unchanged
live selection are recorded in rollout.md; no source/target mutation follows
from this read-only preparation.

**Fresh exact verification and final artifact comparison passed; prior
artifact/check results were not reused.** The one added accepted notes file
changed the packaged source input. Actual candidate is `wxvyrlfx...drv` -> `zmyllqw6...`;
instructions `bpq6xw3l...drv` -> `aix09qb2...`; policy `vxma0g30...drv` ->
`bm96lmx7...`. Exact paths, complete graph and fresh 698-second exit-0 receipts
are in rollout.md and integration-checks-{status,result}.json. The realized
3,817-node/472-source graph equals prepared SHA-256
`57d45d380e0048b8bdd52ee890c9f0da9f53fe4fae77a77154511a6b05014b3e`;
runtime/claim/machine/native artifacts match selected myjy32 and generated policy
metadata matches evaluated content. No discrepancy or further review/check.
The frozen final source is published and comparison captured; preparation
ownership is released. Lead owns claimed merge/remote proof and ordinary profile
activation with separate machine ownership and effects/continuity verification.

## Retained tested refresh and deployment preparation — 2026-11-04

**Preparation complete on the frozen refreshed range:** affected review has no
new findings; quick/composition checks, focused packaged checks, candidate build
and realized-artifact comparison pass. The fresh utility batch exited 0 in
667 seconds on exact head `59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5`.
No activation/integration has occurred.
See [final-refresh-review.md](final-refresh-review.md) and [rollout.md](rollout.md).
No further rebase/source change is planned without informing the lead. The prior
packet and independent review remain intact below.

- Fresh accepted workspace remote baseline:
  `12a3df65467c7c460cae5e0a3cd8dca60138288e`.
- Refreshed final head: `59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5`.
- Complete refreshed series, oldest first:
  `e3a9078b20fc5d373e5dec573de1c3a4e920b07e` (catalog),
  `59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5` (guidance).
- Prior final range retained:
  `aa94433b2c41a17d54f8128b119e33f3289e93ba..4c958a01aeb79f40ca3658e4e759b184e6cf64d8`.
- `git rebase --onto 12a3df65467c7c460cae5e0a3cd8dca60138288e
  aa94433b2c41a17d54f8128b119e33f3289e93ba` completed without conflicts.
  Range-diff maps old A `260831af54d39995e033545c54a771e89c4c4908` to new A
  and old B `4c958a01aeb79f40ca3658e4e759b184e6cf64d8` to new B, both `=`.
- Ordered stable patch IDs are identical in both complete ranges:
  `7a3d2aea7e3c8e189ba2f0c8d314980dd6ce3774`,
  `973b4fba3ba512e3eb8c786e45df2d7c60afc8da`.
  Binary diff hashes differ because fresh verification guidance adds an unrelated
  earlier passage; no manual conflict resolution or feature patch change occurred.
- Feature remains the same four files, +140/-24; no migrations, obsolete feature
  iterations, repeated dependency streams, runtime/configuration source upgrade,
  schema or protocol change is introduced by this refresh.

Accepted baseline now selects generic runtime
`3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7` and vpsFree extension
`f8da821e3c76e26e73aa9d89a712eab0e0faa319`. Baseline `machineIdentityConfig`
and `config/machine-identity.nix` are preserved. These are inherited accepted
master inputs, not feature pin-update commits. Original package checks remain
bound to their old exact sources/inputs; equivalence alone does not certify
the refreshed package graph.

Quick verification at refreshed sources: raw catalog evaluation; complete
non-instruction settings equal to fresh base; full observer/reviewer roles equal;
all prompts within 4,096 bytes (maximum 4,023); whole-range diff check; existing
instructions test in repository Nix environment **10 runs / 217 assertions,
zero failures/errors/skips**. No new tests or source edits. Local links/anchor
and CLI syntax checks pass. Composition passed at the exact locks as recorded
in rollout.md; prior packaged results remain tied to their original graph.

Fresh configuration reference is
`f4069909b55fbed907cb658f350ec6a59f97e05a` at the same-session
`worktrees/2026-10-31-team-workload-parallelization/vpsfree-cz-configuration`.
It is unchanged at verified remote master. Ordinary registration retry and
post-checkout hook recovery in its Nix shell completed without hook bypass.
Public protocol-1 read-only machine resolution returned the expected selector
and null shared lock ID; the machine-policy bridge is preserved. No configuration
edit/channel update or host build/deploy is intended.

Selected application is still
`/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0`.
Its actual derivation sources include immutable workspace source
`/nix/store/wx37wyvpzc0jg91imzmla9r3dlwz2s0m-source`; that source's complete
flake.lock, flake.nix and machine-identity config equal the refreshed candidate.
The utility built and implementer1 independently verified actual deriver
`/nix/store/p75rk3ppnyp9wnljrx31wrcyw6a7vl7j-dev-workspace-0.2.0.drv` and
output `/nix/store/fa20p0jm04bvzw5wfhh8ymsjrgpypc5j-dev-workspace-0.2.0`,
matching the evaluated identities.
Complete evaluated graph proof and native/compatibility/identity evidence is in
rollout.md, with the full sanitized graph artifact linked there. Both graphs
contain 3,817 derivations and 472 source vertices; the only source replacement
is the workspace source, and differing derivations are policy-generated data
and the package root. Native Codex and machine identity derivations are shared.
Metadata alone is not treated as graph proof. The actual retained recursive
deriver graph is identical to the evaluated graph (normalized SHA-256
`7b713fcac6f67e035a2accd698ad10d6a3af58f17e73953c7ce37384d8519237`).
Actual runtime/claim/integration/machine descriptors and native entrypoint match
the selected package; generated policy/package/extensions JSON matches evaluated
derivation text. No discrepancy requires another review/check. Exact current
check derivations/outputs and selected/system/profile identities are retained in
rollout.md and candidate-checks-{status,result}.json, separate from old results.

Preparation is for application-only user-profile activation under the design's
settled route. No profile selection, machine claim, host/system build/deploy,
integration, force-push or lifecycle operation is authorized/performed here.
Stop at a concrete prepared candidate for the lead's authorization decision.

## Retained original review and A1 packet — 2026-11-03

Initial preparation owner: implementer1; A1 receipt update: implementer0.
**Independent review completed on the original reviewed range. Its exact A1
wording correction is folded into A and directly checked on the final head.**
Lead owns final acceptance, packet completeness and subsequent packaged checks.
The final head has not been independently re-reviewed; see the unchanged full
[review report](final-review.md) and [A1 direct-remediation receipt](narrow-fix-delivery.md).

## Request and acceptance

The original request asked whether team architecture could improve parallelism;
the user subsequently directed, "all right, implement it" on 2026-11-03.
Implement the accepted operating model in existing workspace prompts and docs:
complete packages with member-prepared evidence, direct routine technical
clarification, sufficient per-package design release, explicit capacity and busy
steering semantics, narrow same-repository sequencing and compact milestone data.

Acceptance: catalog and guidance agree; effective prompts remain within the
unchanged 4,096-byte limit; non-instruction settings and safety/role/review/approval
boundaries remain unchanged. No scheduler, aggregate API, runtime, new roles,
roster reconfiguration, telemetry, dependency update, deployment or integration.
No claim that these changes prove or eliminate a measured lead bottleneck.

Context in this same session: [plan.md](plan.md), [state.md](state.md),
[design.md](design.md) (current implementation section; October investigation
below is historical), [catalog-delivery.md](catalog-delivery.md) and
[guidance-delivery.md](guidance-delivery.md).

## Repository and exact range

- Owner/component: workspace policy repository;
  `git@github.com:aither64/vpsfree-cz-workspace.git`.
- Shared root: `/home/aither/workspace/ai/vpsfree.cz` (master remains untouched).
- Feature checkout:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-31-team-workload-parallelization/workspace`.
- Branch: `2026-10-31-team-workload-parallelization`.
- Initial base: `6383e8848c92c06a9d817f8109853b5b61305c89`.
- Final base: `aa94433b2c41a17d54f8128b119e33f3289e93ba`, shared master at refresh.
- Final head after A1: `4c958a01aeb79f40ca3658e4e759b184e6cf64d8`.
- Original independently reviewed range:
  `aa94433b2c41a17d54f8128b119e33f3289e93ba..b1e8441dd74a4313da72b434eb991d8c35c6b626`,
  containing original A `2d00c953509fc8ab297b0a8c39d4dc7a4e41567d` and original
  B `b1e8441dd74a4313da72b434eb991d8c35c6b626`. Full report preserved in
  [final-review.md](final-review.md).
- Fetched remote default: `6383e8848c92c06a9d817f8109853b5b61305c89`; it is an
  ancestor of shared master. Baseline delta is tracking/archive/notes only.
- Feature worktree/index clean after both commits and conflict-free rebase.

Complete base-to-head series, oldest first:

```text
260831af54d39995e033545c54a771e89c4c4908 teams: clarify execution packages and member coordination
4c958a01aeb79f40ca3658e4e759b184e6cf64d8 docs: define complete team package workflow
```

Final diffstat:

```text
 config/agent-teams.nix                  |  25 +++---
 docs/agent-instructions/sessions.md     |   4 +
 docs/agent-instructions/verification.md |   4 +-
 docs/agent-teams.md                     | 131 ++++++++++++++++++++++++++++----
 4 files changed, 140 insertions(+), 24 deletions(-)
```

Inspect the full final diff from the feature checkout with
`git diff aa94433b2c41a17d54f8128b119e33f3289e93ba..4c958a01aeb79f40ca3658e4e759b184e6cf64d8`.
The original pre-refresh range is
`6383e8848c92c06a9d817f8109853b5b61305c89..dcd5e837d5e1ee9fab2c0b48097be7c980674585`.
Its refresh to the original reviewed range marks both commits `=`; complete
binary diff payloads are identical,
SHA-256 `d433a99bdc4491d009b996abb80856662f8f06d8f35abfe42b057000e6b6bd0c`.
Refresh receipts and original-to-reviewed commit mapping remain in guidance-delivery.md.
Reviewer0 independently reviewed the refreshed range above. A1 then changed only
`Missing output alone proves no stall.` to `Missing output alone cannot prove a stall.`
in the shared lead requirements. The A1 range-diff marks A `!` for that sentence
only and B `=`; B's binary patch is unchanged. The separate A1 receipt records
exact hashes, focused checks and the no-rerun decision without relabeling the
original independent review.

## Intended history and migration inventory

Two independently reviewable commits remain: A for compact catalog role
instructions; B for the canonical workflow and minimal routed procedure pointers.
The split follows independent file ownership; supporting pointers belong with
their documented behavior. No assertion changes, superseded approaches or fixup
commits remain. No obsolete compatibility path was introduced.

**No migrations.** No database/on-disk state schema, data conversion, API/protocol
format, compatibility shim, or persistent recovery behavior is changed. Therefore
there are no migration versions with merged, released, deployed or external-use
provenance to preserve. No dependency/channel/input or generated-artifact update
streams are intended; no repeated pin updates or intermediate deployment lineage.
Reviewer0 independently confirmed these conclusions on the original reviewed
complete series and diff. A1 is folded into A, leaves B unchanged, and introduces
no migration, repeated update stream or additional commit.

## Documentation, consumers and compatibility

`docs/agent-teams.md#package-workflow` owns the detailed workflow;
`docs/agent-instructions/sessions.md` and `verification.md` link to it. Core
`AGENTS.md` is unchanged at 16,356 bytes and already routes to the guide.
The existing instruction test needs no new phrase assertions. Scope/design
rationale is in design.md; individual check/baseline receipts belong in
guidance-delivery.md. No deployment or upgrade instructions are needed because
this delivery neither changes a persistent format nor performs a rollout.

`config/agent-teams.nix` owns the site catalog and is imported as `teamConfig` by
the workspace flake's extension `mkPackage`; generated catalog readers consume
the resulting role prompts. Workspace agents also read routed documentation.
Existing flake pins select the vpsFree extension
`e4e7e95ed39bf514b33f8f8ae61ba9868de060ae` and generic dev-workspace
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`; these pins must remain unchanged.
No generic runtime or other repository implementation is part of this change.

Catalog text affects future selections only after separately authorized package
deployment. Existing sessions/forks retain saved prompts/settings and custom
instructions; workspace guidance applies as read. Preserve the recognized stock
observer's existing refresh exception. Bounded explicit assignments can use the
workflow within retained role authority. Model/effort/access, preset counts,
Solo/Lead-and-reviewer ownership, Full-team/Lead-designed distinction, review
timing, merge/deployment approvals and lifecycle recovery remain intact.

Rollback is an ordinary scoped corrective feature change; no package switch,
session transition, machine operation or reconfiguration is performed here.

## Quick checks and remaining gates

Detailed commands/results are in catalog-delivery.md and guidance-delivery.md:

- A: raw Nix catalog evaluation, all effective prompt byte bounds, exact
  non-instruction baseline equality, full observer/reviewer equality, unchanged
  existing flake jq policy predicate and default package environment validation
  all passed at the original delivered/reviewed range. Reviewed lead lengths
  were Full team 4,018 bytes and Lead-designed 4,006; limit remains 4,096.
- A1: raw evaluation, exact requested-sentence catalog transformation, equality
  of non-instruction fields with reviewed head/base, byte bounds, focused diff,
  two-commit history and unchanged B patch all passed. Corrected lead lengths:
  Full team 4,023; Lead-designed 4,011; Lead and reviewer 3,029; Solo 2,807.
  No non-instruction settings, other role instructions or flake assertions changed.
- B: `nix develop .#checks.x86_64-linux.agent-instructions --no-update-lock-file
  --command ruby test/agent_instructions_test.rb` passed at final refreshed
  sources: 10 runs, 206 assertions, zero failures/errors/skips.
- Full final-range `git diff --check`, changed local link/anchor checks and
  `bash -n` on the peer CLI example passed. No example submission was executed.
- Ordinary commits used Nix environments; no hook framework/active hooks were
  declared, and none were bypassed. No new prose-mirroring tests.
- A's transient draft exceeded the prompt limit and default validation correctly
  refused it. A consolidated the text and restored validation without expanding
  limits. This failure and B's focused environment choice are recorded, rather
  than accepted as final verification.

Independent final review is complete on the original range; its sole Advisory
was corrected exactly and verified directly under the skill's narrow-fix rule.
No reviewer rerun or long build was launched for A1. After lead inspection, lead runs focused
packaged checks `checks.x86_64-linux.agent-instructions` and
`checks.x86_64-linux.agent-team-policy` as applicable through the monitoring skill.
No broad runtime/lifecycle suite is justified for prompt/documentation changes.
Publication and explicit integration approval remain subsequent gates.

## Completed review and direct-remediation status

Reviewed risk: medium, a bounded compatible change to shared team policy text.
No runtime authorization, persistent-state or public protocol change is intended.
Reviewer0 completed general, architecture/repetition and scope/proportionality
lanes. The full report includes explicit scope, correctness, architecture,
whole-history, no-migrations and no-repeated-update-stream conclusions.

The retained independent reviewer was `reviewer0`, saved `gpt-6.1-sol` / `xhigh`,
read-only role access; exact native identity and preserved settings are in the
original report. It authored no implementation. There were no Blocking or
Important findings and one Advisory A1.

The lead requested the reviewer's exact A1 wording correction. Implementer0
folded it into A and verified the resulting source and history directly.
Mandatory-change-review steps 9–10 and the reviewer's explicit conclusion permit
this exact narrow remediation without another reviewer turn. No new design,
scope or contract was introduced. Final delivery is the reviewed result plus
this documented correction; it is not independently re-reviewed. Lead retains
reconciliation, final acceptance and the remaining packaged checks/publication
and integration gates.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/>.
