# P6 workflow projection and standalone UI evidence

Owner: implementer4, retained Sol/xhigh/workspace_write. Session binding and live
roster verified. This is the lead-released P6-WORKFLOW-PROJECTION-UI package;
prior native component checkpoint 94b4d584 remains accepted separately.

Committed source checkpoint: `d681233ed7c143994745a11968dec75a2b16e3c0`, parent
`cf3997b35fd1e40208e66437888d4b7d6a71916d`. Exactly twelve approved paths
were committed; staged, committed and current SHA256 values match the frozen
manifest. The index is empty, owned paths are clean, and the sole window is
closed/released to the lead before this evidence update. Receipt:
`tmp/p6-workflow-ui-commit-receipt.json`. Normal git commit-F ran in the immutable
D Nix environment; no hook framework or active executable hooks were declared,
and no hooks were bypassed. No push, central edit, lifecycle action, real
provider/model call or SDK rerun occurred. Lead owns acceptance, shared D
publication and final independent review.

## Exact source and independence

Fresh committed D parent:
`cf3997b35fd1e40208e66437888d4b7d6a71916d`, tree
`527f56ed43832187c141bd9251fb1faff5585d3e`.
Manifest: `tmp/p6-workflow-ui-checkpoint.json`; it records all twelve current
SHA256 values, parent values, file sizes, complete 970-file archive input hashes,
snapshot location, and check scope. There are seven new files and five modified
files, 779 additions and 11 deletions. The Git index was empty at freeze.

| Owned paths | Change |
| --- | --- |
| piplan/policy_projection.go and policy_projection_test.go | Exact latest proposal ID/revision/text digest/caller projection and mismatch fixtures |
| piplan/policy_adapter.go | Manual mode projection against genuine absent plan state |
| piplan/read.go and read_test.go | Validated native-free detached LatestProposal read |
| piquestions/admission.go and admission_projection_test.go | Optional pure content/current-handle/binding/origin projection; busy capture allowed; unavailable proof disables controls without inventing stale history |
| piquestions/read.go and read_test.go | Validated native-free Questions read with detached nested options/responses/answers |
| web/static/pi-workflow-ui.js | Standalone raw-fetch API, pinned cards, exact Plan text, manual modes, cancellation and explicit-refresh fence |
| portal/test/pi_workflow_ui_test.cjs | Nine finite browser fixtures |
| docs/pi-questions.md | Narrow Workflow display composition contract |

Domain paths above are under `portal/internal/`. All twelve exact repository
paths are in the manifest. No app.js, template, server, route, packaging,
metadata, P3/runtime or peer source is included.

The clean proof used a Git archive of the exact committed parent plus only the
twelve owned overlays. It does not consume dirty P2/P3 runtime source. Its scoped
Go compile and UI syntax checks pass. No source/schema migration, converter or
policy/store initialization is introduced. Existing strict private readers own
format validation; missing state remains absent. No new state writer is registered.

## Checks and applicability

All commands used the repository's immutable Nix development environment at
`4f390101de7ca5047d9e41faa0b483088d591185`, via the D git+file flake reference.
Go commands passed `-mod=readonly`. The environment revision is an environment
pin, not a claim that the new source exists in that commit.

| Check | Result / exact scope |
| --- | --- |
| `go -C portal test -mod=readonly ./internal/piplan ./internal/piquestions -count=1` | piplan 0.573s; piquestions 0.757s. Final domain bytes, unaffected by later prose/renderer changes. |
| `node --test portal/test/pi_workflow_ui_test.cjs portal/test/pi_workflows_browser_test.cjs` | 16/16, 230.554747ms. Standalone helper plus existing seven question/Plan controller regressions before final two renderer fixes. |
| `node --test portal/test/pi_workflow_ui_test.cjs` | 9/9, 245.56683ms. Final helper/fixture bytes, including clickable explicit Refresh and accepted decision-panel closure. Existing controller bytes unchanged. |
| Parent plus only twelve: domain `go test ... -run '^$' -count=1` | piplan 0.015s; piquestions 0.014s, no tests run. Demonstrates compiled independence, not another behavioral campaign. |
| Parent plus only twelve: `node --check portal/internal/web/static/pi-workflow-ui.js` | Passed on final helper bytes. |
| Owned diff whitespace check | Passed. |

All checks are terminal and known quick; no watcher or long integration run was
needed for this package. No unchanged SDK test was repeated.

One initial browser assertion incorrectly expected completely empty browser
storage. The existing question controller legitimately stores empty draft
records on snapshot. The corrected assertion specifically forbids storing mode
requests; no product behavior or validation was relaxed for that assumption.

## Writing, UI and central handoff

Lead's main writing pass is closed. Documentation SHA256 remains
`7581cc4121d7f839c033508c287928a76d8855f94751bee2213c6a526ba28548`.
Final helper SHA256 is
`6f8baa1a14144f21bd3e57d32da4a8a78397bfb1df41b55f6e83d7fd3d1b0d51`.
The final helper retains the approved read error and all labels. After the pass,
two tested renderer fixes added the actual Refresh action using its existing
label and hid the decision panel after authoritative acceptance. Neither changed
the descriptor, API, domain semantics or visible prose.

[Central hookup handoff](p6-workflow-central-hookup.md) contains named minimal
app/template hunks as an artifact only. It distinguishes proposed page carriers
from the frozen descriptor, requires a separate authoritative Pi backend gate
before legacy listener registration, uses raw fetch, and connects existing stream
apply/reconnect hooks to automatic update without clearing uncertainty.

Pure proofs and the helper establish no live workflow capability. P2 still owns
real authority/retained guards, same-Manager construction, routes, complete
observation refresh/invalidation and wake composition. P3 owns real workflow
proof and attachment/sequence invalidation barriers. Central frontend hookup
needs its later sole-owner window; packaging/capability publication remains P7.
Actual central/installed flow and whole-deliverable review remain separate gates.

Next action: lead accepts the exact committed checkpoint and sequences the
remaining central owners. Implementer4 retains source and review fixes, with
capacity after acceptance; no independent next package is queued. Technical product docs stay with the domain in
docs/pi-questions.md; temporary hookup/check evidence stays in these session
records. This package adds no migration, release, deployment or external consumer
boundary. Whole-branch history assessment remains lead-owned at final review.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)
