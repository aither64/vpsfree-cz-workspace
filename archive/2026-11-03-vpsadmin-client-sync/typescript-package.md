# TypeScript Phase 1 package

Owner: implementer2. **Narrow history ownership correction complete; current-head CI passed,
awaiting lead acceptance.** Current final head
`c53cb4dabb0b3aac8d05834478872d2cfa698fa7` is published on the feature branch;
worktree is clean. Original successful local verification/archive evidence below
binds old head `a4fc2449a1b5255b93b0c669ea9c454fac990536` only. No default merge, tag, npm publication or deployment performed.
No TypeScript utility is running; CI-only observation completed and the single
watcher slot is released. Current correction details are in
[typescript-history.md](typescript-history.md).

## Source, branch and history

- Repository: `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`, target
  `main`; fresh default/base `d354491537f8b654b4d2c33a705cad84474f95d6`.
- Registered local/remote feature branch: `2026-11-03-vpsadmin-client-sync`.
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-typescript-client`.
- Complete corrected final series: generated/input `ec08ec1`, handwritten
  consumer `2071a16`, release metadata/prose `c53cb4d`. Exact full SHAs and ranges
  in [typescript-history.md](typescript-history.md). Final base-to-head diff
  remains 23 files, 987 insertions and 40 deletions. No migrations or repeated
  update streams. Old/new final tree exactly equals
  `c85e30b1fc1ae27bba9c08884e11fa78bbb15f7b`.
- Earlier combined-commit rationale was rejected following the user challenge.
  Its prior review conclusion is retained historically, not current approval.
  The first split also wrongly placed a future release-lock hash in the generated
  commit; reviewer blocked it. Final history keeps each hash/assertion with its
  actual owning input, with per-commit object checks.
- npm/tag reads found latest `0.3.0` and no `0.4.0`; lead accepted the user's
  next-minor default. Registry state must be rechecked at publication time.
- No declared hook framework, no custom hooks path and only sample common
  hooks; no installation required or hook bypass used.

API source: `942c6eaed41331f823d8e0f670ed239e2b308440`. Retained exact generator
source: `1ef9b204ba45bb261d3334be5c555cc1856b713b` (0.32.2); peer/dev runtime
`haveapi-client` remains 0.32.0. Source/tooling identities were recomputed with
existing helpers; pinned Node24.21.0/npm11.19.0/Ruby3.4.11/TypeScript6.0.3/
Prettier3.9.10 are unchanged. Shared source worktrees remain read-only and
unchanged under implementer3 ownership.

Raw shared artifacts match [source-inputs.md](source-inputs.md) byte for byte,
including its independent fresh-database repeat:

| Input | SHA256 |
| --- | --- |
| `schema/schema.json` | `d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26` |
| `schema/provenance.json` | `c85815abd315f53a5ef05f324abe377760293786a13a25b7a127ec804c50e0c1` |
| `schema/tooling.Gemfile.lock` | `62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c` |

Final 0.4.0 package-lock tooling hash:
`00f789d4786fdcb2c9e61481e86180e376ea1ed86a022c2e22567b4d03946066`.
Full fixture/plugin/exporter graphs remain in committed provenance.

## Contract, documentation and independent review

The complete parsed schema delta has nine additions: advisory Retract/Delete
and seven optional non-null `expected_state` inputs. No existing value, type,
route or default changed; no removals or profile/authentication changes.
Generated delta: two files added, none removed, ten existing files changed;
677 manifest-owned file hashes and exact ownership set verified. Coverage is
151 application resources/521 actions, plus retained/excluded authentication1/5.
Generated runtime is unchanged. Raw OAuth fixture metadata is unchanged; no Go
projection applies to TypeScript.

Existing calls retain their contracts. New calls/guards require compatible
deployed API support and permissions; npm publication alone does not establish
server availability. The SDK does not implement draft-sync policy, infer
permissions or retry writes. Restore schema/provenance/pins/generated source
together on rollback; retain published versions. No persisted-state conversion,
node coordination, production API check or deployment is involved.

Lead applied required writing skills and approved exact changelog/README text
and the factual development-guide action-count update. No Phase 2 rules or WebUI
WIP changes are included.

Independent reviewer0 (`gpt-6.1-sol`/xhigh) assessed the complete original range,
all four lanes and history/migrations; see
[typescript-review-result.md](typescript-review-result.md) and
[review packet](typescript-review-packet.md). Sole blocking finding: mutation HTTP
fixture omitted declared output namespaces. Owner reproduced the installed
runtime's rejection and fixed the fixture without changing request assertions.
Original head `b432eb4d5a05eca151f42626080460e781a4fcfc` was amended to the then-final tested
`a4fc2449a1b5255b93b0c669ea9c454fac990536`; same base. Lead inspected that exact
fixture-only diff and accepted it under the narrow-fix rule. No review rerun.

## Original exact-head verification and retained archive

Quick checks passed: all recorded input/tooling hashes, generator/shared source
identities, coverage and owned file hashes/set, methods/guards, package/lock
identity, JS syntax, `npm run typecheck`, whitespace and staged whitespace.
Setup passed exit0/17s. Corrected generation passed exit0/15s. The first generation
attempt had an extra transferred `.` argument and failed usage validation before
writes (exit1/3s); no product fix or setup repeat was needed. Logs are retained.

After the original review acceptance, fresh native utility
`/root/typescript_verification_watcher` ran the command now preserved as
[typescript-checks-tested-a4fc244.sh](typescript-checks-tested-a4fc244.sh) against
exact old tested head `a4fc2449a1b5255b93b0c669ea9c454fac990536`, exit0 in about55s. Its result verifies `gpt-6-luna`/low, utility identity
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
danger-full-access/approval never and matching session binding. No retries,
second build, cancellation or running operation remains.

Passed: offline regeneration `--check`; shared-source refusal regression;
one build; strict consumer typecheck; 14 client/release tests (including all nine
new HTTP mutation assertions and invalid-guard checks); npm pack with scripts
disabled; extracted ESM/types/actual-runtime packed consumer; archive receipt
creation and verification. Full [log](typescript-checks.log),
[status](typescript-checks.status) and [watcher result](typescript-checks-result.md).

Original feature branch remote was verified at old head a4fc244. Original CI
[41665146322](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41665146322)
completed successfully on that head; retained [metadata](typescript-ci.json).

Historical validated local archive (built/packed once at old head a4fc244):
[typescript-release-a4fc244/vpsadmin-typescript-client-0.4.0.tgz](typescript-release-a4fc244/vpsadmin-typescript-client-0.4.0.tgz)
and [receipt.json](typescript-release-a4fc244/receipt.json). Receipt binds package
0.4.0, old tested source head a4fc244, tag null, 1,364 package files:

- SHA256: `e3c1cee328c8c0bb6826c209bee971d5e6939d2acbeebf9938fc6f032db95326`;
  independently rehashed after watcher completion.
- Integrity: `sha512-nNjgPuus4ZrqaPXP/D+15IApvW4Gt+nAWiQYhK/5Kc0mlkivgPZrd5H/594Nq2XqAA4/cBNXWyNyxk7G9FX/rA==`.

Keep this old archive/receipt immutable; never relabel it as binding new history
or publish it pretending new-head provenance. Current-head CI41668853169 and a later
exact tagged native workflow supply their own current archive/receipt. No local
rebuild is needed merely for the split. Lead owns current history-review/CI
acceptance, integration/publication authorization, fresh release-state checks and
exact final-default/tag/registry evidence.
Session remains open. No cleanup or lifecycle action authorized.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)

## Reversible integration preparation

Prepared a clean native detached target (no new registered feature obligation):
`worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-typescript-client-integration`.
Fresh fetched remote `main`, target HEAD and `origin/main` all equal
`d354491537f8b654b4d2c33a705cad84474f95d6`; remote feature and local branch equal
`a4fc2449a1b5255b93b0c669ea9c454fac990536`. Exact target-to-feature ancestry
check succeeds; fast-forward is available. Target has detached HEAD and empty
status. No `AGENTS.md`/hook framework or custom hooks path is declared and common
hooks have no active entries; no trust/signing change or dependency preparation
is needed for ordinary Git merge. Git and SSH origin verified. No rebuild/tests.

Read workspace Git/deployment/coordination guidance and selected package guide
(`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`). Captured
feature comparison initially at old head, then repeated with explicit base
`d354491537f8b654b4d2c33a705cad84474f95d6` and current head
`c53cb4dabb0b3aac8d05834478872d2cfa698fa7`. Repeat if head changes. No claim,
default mutation, merge/push/tag/publication occurred during preparation. Lead
must obtain named repository/target integration approval and recheck fresh refs
inside the short merge claim. Leave the prepared worktree/session open.

## Current history correction checkpoint

Complete ranges/proof and current review packet:
[typescript-history.md](typescript-history.md),
[typescript-history-proof.json](typescript-history-proof.json),
[typescript-review-packet.md](typescript-review-packet.md).
Current native CI:
[41668853169](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41668853169).
No duplicate local build/test or utility. Detached target remains clean at base.

## Current native CI result

Actual final-head CI41668853169 passed at c53cb4d. Read-only downloaded
artifact13245379341 and [receipt](typescript-ci-c53cb4d/receipt.json) bind that
exact source, version0.4.0/tag null; archive SHA256
`3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`.
[CI-only result](typescript-ci-c53cb4d-result.md) records the expected Luna/low
utility/policy and no remaining operation. GitHub artifact ZIP digest
`25f7599abbea7ffda2da1c8b21a9ab21156994f92caec03aa813437b7b8dcc13` is distinct
from the package tarball SHA. Preserve old local archive/receipt untouched.
Lead inspects the final narrow history remap; no new local suite or publication.
