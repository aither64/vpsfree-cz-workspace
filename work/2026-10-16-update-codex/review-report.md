# Independent final review

## Findings

### Blocking B1: the managed naming fixture rejects the selected catalog

In `dev-workspace`,
`portal/cmd/workspace-portal/naming_runtime_integration_test.go:490` still
requires `info.Size() == 62843`. The selected codex-web catalog is **62680
bytes**, with SHA-256
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
Commit `de4878a8b7d36def431c9db6068483c4ad4abde0` updates the fixture's hash and
native version but leaves this predecessor length unchanged.

`nix/workspace-portal.nix:341` installs that exact catalog unchanged, and
`flake.nix:43` selects it from codex-web
`8851f1c35e9424b1240705cb73d09d387d9276f0`. Consequently every managed naming
test using `newManagedSmokeHarness` fails with `fixed naming-only catalog
mismatch` before its native lifecycle assertions. This is a deterministic
release-verification failure, not a pending environmental prerequisite.

Update the expected length to the selected catalog's length in the owning
runtime upgrade commit. Verify the size/hash binding with a quick check, then
run the planned managed native suite after this review gate is resolved.
Refresh and consolidate downstream runtime pins if that changes the published
runtime head. This is a narrow correction within the reviewed design; it does
not require another full review under the skill's narrow-remediation rule.

Originating lanes: general; risk/compatibility verification.

No additional Important or Advisory code/design findings.

## Reviewed identity and scope

Standalone reviewer task: `/root/final_review`. The assignment specifies
`gpt-6-astra` with `xhigh` effort. I independently read the installed catalog at
`/nix/store/a6brrl4a354sn4q25crqw3q54wwg0qag-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json`:
its default development team is `lead_reviewed`, and its review-purpose
`reviewer` role has exactly those settings and read-only access. The packet
records a null session roster as the fallback reason. Separate native runtime
model/effort metadata is not exposed in this reviewer context; the coordinating
agent should retain the launch identity/settings receipt rather than infer it
from this prose.

I read the mandatory review skill and all four assigned lane references,
workspace instructions and applicable procedures, all four repository
instructions and new update skills, the plan/design/state, relevant package,
protocol, deployment and recovery documentation, and actual committed source.
No nested agents were used. This report is the sole output mutation. No long
tests, build, deployment, integration or lifecycle operation was performed.

## Exact history assessment

All four worktrees were clean at the recorded heads. Actual ordered Git history
matches `review-heads.json`; each recorded base is an ancestor of its head.
The inspected refs contain the heads on their dated feature branches and their
remote feature refs, not on a default branch.

| Repository | Reviewed base | Reviewed head | Complete ordered series |
| --- | --- | --- | --- |
| codex-web | `523865195522ad6f4804613e6f54823ddf447924` | `8851f1c35e9424b1240705cb73d09d387d9276f0` | `4a091c94addf908e05f99d49f0432435845c4cda`, `8851f1c35e9424b1240705cb73d09d387d9276f0` |
| dev-workspace | `2b22de8d273a3b75e6cdd62c398fdb2630871d5a` | `c07d5cfaf27ff4b6a23bfeb5538098e1ccbdfc96` | `de4878a8b7d36def431c9db6068483c4ad4abde0`, `c07d5cfaf27ff4b6a23bfeb5538098e1ccbdfc96` |
| vpsfree-cz-configuration | `ae98e9dbf05cd3f6b2d0c32255a4cb2d58c3865b` | `8f9250bfac3d58ca3affdf2103054462a94af042` | `8f9b857dfd806d1b47d624d996e10ad0ce81c083`, `81ab9fad6778ed1880607997f08cd47d2c06f328`, `8f9250bfac3d58ca3affdf2103054462a94af042` |
| workspace | `78a18cccbcd72fe91c68a7b9212628a7e13abe90` | `ed34ef0a63d4387ef26b9dcbdc337d4efc928dd8` | `f5da0f7effc6c7f6d9047bff52b1a36918359c76`, `ed34ef0a63d4387ef26b9dcbdc337d4efc928dd8` |

The complete series and final diffs contain no obsolete unmerged approach,
transitional compatibility path or retained fixup iteration. Procedure/helper
work is separated from the codex-web catalog refresh. The runtime's native
selection, Go/Nix codex-web pins, immutable catalog assertions and version gates
form one necessary compatible selection; its skill installation is separately
reviewable. Configuration keeps its procedure separate from generated input
commits. Workspace keeps procedure/installation separate from its runtime pin.
Commit purposes and messages fit their respective repository guidance;
generated confctl messages retain their generated form.

There are **no repeated update streams** needing consolidation in the submitted
series. Runtime llm-agents and codex-web selections each change once; the
configuration's system llm-agents channel and devWorkspace channel each change
once; the workspace nested runtime changes once; the codex-web catalog refresh
occurs once. The configuration's separate system and runtime llm-agents nodes
are distinct consumer roles, not successive updates of one stream. Transitive
catalog/input changes in downstream locks follow their owning runtime update.
Branch publication and companion consumption were not used as exemptions from
consolidation. Preserve that conclusion when refreshing pins for B1.

**Migration lineage: no application migrations.** No migration, seed, schema,
state-format writer or conversion guard is introduced in these four series.
There is no branch migration version to classify as merged, released, deployed
or externally consumed. The changed comment about the native logs DDL is test
provenance, not a migration. Native upstream migrations belong to Codex 0.163.0
and still require the planned old/new reader probes; this conclusion does not
certify downgrade compatibility. The packet reports no deployment or release of
these feature heads, and this review performed neither.

## Lane conclusions

- **General:** the deliverable matches the requested upgrade and layered
  repeatable procedures. Catalog hashes, version gates, dependency pins and
  documentation agree except for B1's smoke-fixture length. The source catalog
  is byte-identical to upstream's `rust-v0.163.0` catalog. Its semantic change
  from the base is removal of null `model_messages.instructions_variables`.
  The Luna result exactly preserves source metadata apart from the three
  intended fields; deterministic serialization produces the committed bytes.
- **Architecture and repetition:** codex-web owns protocol/catalog work;
  runtime owns package selection and naming; configuration owns host channels;
  workspace owns composition and coordinated rollout. Actual consumers were
  checked in runtime imports/pins, `mkPackage`, `mkCodexPackage`, the aitherdev
  module and `codex-ds` wrapper, and workspace Nix composition. Core skills
  reference the selected codex-web source, while the workspace override extends
  the existing organization skills map. Existing catalog validation still
  rejects core-name collisions. No new registry or competing cross-project
  implementation was introduced.
- **Scope and proportionality:** the four skills and one small catalog helper
  fit the requested repository ownership. The implementation retains model
  choices, package assembly and existing module/public API boundaries. It adds
  no fleet rollout, application state redesign or local Rust patch. Retaining
  the assembly helper while checking upstream daemon identity is consistent
  with the accepted scope.
- **Risk and compatibility:** the source changes preserve remote authorization
  and utility policy; they do not relax any restriction to make the upgrade
  pass. The Nix derivation's downstream daemon patch supports the documented
  immutable original-store selection, disabled upstream update path and
  best-effort native root registration. Materialized assembly and retained
  roots remain intact. Ordered system/profile activation, idle-session
  admission, exact daemon identity checks and forward-only application recovery
  are documented. Existing old packages keep their own client/catalog pair.
  Schema and fake-transport evidence cannot establish actual native isolation
  or persisted-state compatibility, so those remain release gates.

The lock graphs preserve all node sets and input/follows edges. Both consumers
select runtime `c07d5cfaf27ff4b6a23bfeb5538098e1ccbdfc96`; system and packaged
llm-agents select `e85b99217baf13a38fc887b31338b1833f1159c0`. Runtime Nix and Go
select codex-web `8851f1c35e9424b1240705cb73d09d387d9276f0`. Workspace extension
revision `767dfd587e346168e1443e65ccdb67ce748f3fe3` and its content identity are
preserved. Other changed lock nodes are the expected llm-agents descendants;
unrelated channels and the runtime's own nixpkgs selection remain unchanged.

## Evidence and remaining gates

I independently verified history/cleanliness, final diffs, catalog semantics
and hashes, all lock graph changes, dependency consumers and the candidate
executable. The latter reports `codex-cli 0.163.0` and SHA-256
`5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5`, matching the
receipt. I read its Nix derivation and downstream daemon patch and compared the
tagged upstream catalog and logs migration. I inspected the reported quick
check coverage; I did not independently rerun the supplied Go/browser/Nix
suites.

The source store path in `candidate.json`,
`/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs`, was absent during
review. The binary derivation does select that source path. Realize/retain that
exact source before the native fixtures that require it; a version string or
the generated schemas alone does not replace this prerequisite. The committed
full catalog was independently matched against the upstream tagged source over
a read-only fetch. This absence limits local reproduction of the previously
reported source-schema validation, not the catalog comparison.

Pending checks remain the packaged suites/builds; native namespace ownership
and hostile-dispatch suites for both supported profiles; managed naming child
lifecycle, ordinary-daemon continuity and the positive ten-second canary;
saved-thread startup/resume/fork and old/new persisted-state readers; exact
system/application builds; and coordinated deployment acceptance. The live
0.162.1 system and 0.160.0 workspace predecessors both need consideration.
Successful HTTP/SSE fixture coverage also does not prove hostile delivery over
WebSockets, as the technical reference already states.

The mandatory review gate is **blocked by B1**. After its narrow correction and
focused verification, the coordinator may proceed to the planned longer gates.
This report does not declare deployment readiness, approve default-branch
integration or authorize lifecycle cleanup.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-16-update-codex/
