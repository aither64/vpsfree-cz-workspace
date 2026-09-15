# Review packet: readable character diff highlights

## Request and acceptance

The user reported scattered changed-character backgrounds in a saved portal
comparison, accepted the investigation, and authorized the fix and aitherdev
deployment. Preserve exact Git lines/counts, immutable source contents and line
links; group incidental character changes into readable spans in both layouts.

## Repositories and committed range

Worktrees under `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-portal-diff-highlighting/`.
All intended product changes are committed; review each base..head.

| Repository | Base | Head |
| --- | --- | --- |
| dev-workspace | `9a1b16464e45d722110b448a79315a0f3ce134aa` | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` |
| vpsfree-dev-workspace | `c6afe2905506fba0b8e372e0436b570f5597f8bd` | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` |
| workspace | `259c0c3fe7d4f3d454f8b27172cb7a8f99ca79be` | `80b93a8c6b120ce178b4a6479901fde12156e3d5` |

## Commit split and implementation

- Runtime: one functional fix with its comment and focused regressions. Imports
  existing `presentableDiff` instead of raw `diff` from locked merge 6.12.2.
- Extension: separate pin-only commit consuming the runtime.
- Workspace: separate pin-only commit consuming the extension (and runtime).

The runtime owns cosmetic highlight ranges. Both unified and split projection
use `reviewProjection`; `editor.js` decorates its ranges. Git API ranges retain
sole authority for changed lines. Shiki supplies independent foreground colors.
The extension consumes runtime `lib.mkPackage`; workspace consumes extension
`lib.mkPackage` with existing siteConfig. No npm/Codex/cluster input changes.
Lock comparison confirms only runtime node changed in the extension; only
runtime and extension nodes changed in the workspace.

## Scope and residual behavior

Retain existing bounded diff config and Git block boundaries. Do not replace Git
with CodeMirror line classification, add new line pairing/similarity policies,
change colors or syntax tokenization, or change system configuration. Presentation
cleanup remains a heuristic; common punctuation/indentation can still be unmarked
inside rewritten blocks. The reported 27-range block becomes one continuous edit.
User input screenshot and raw capture remain outside Git.

## Documentation and evidence

Tracking: `work/2026-09-15-portal-diff-highlighting/{plan,state,diagnosis}.md` in
shared `/home/aither/workspace/ai/vpsfree.cz` (not copied feature tracking).
Read local AGENTS.md. Checked runtime README (Repository review), portal guide,
extension README, workspace deployment policy. Adjacent comment records the
non-obvious reason for presentation cleanup; no public interface or operator
procedure changed. Session rollout record will hold exact execution evidence.

## Quick checks

- Four new readability regressions fail on old model (identifiers fragmented,
  unrelated block marked in nine pieces on its deleted line).
- `npm run build && npm test` with Nix Node: 13/13 pass with the fix, including
  old exact-Git +116/-6 regression, random source-preservation cases and bounds.
- `git diff --check` passes; no declared hook framework in the three repositories.
- `nix flake check --no-build --print-build-logs` evaluates the packages/checks.
  Verify final state record for command completion before concluding.
- Runtime and extension feature pushes succeeded; CI will be followed through.
- Package builds and browser/deployment acceptance follow review.

## Risk and deployment

High overall review classification conservatively because the scope includes
cross-project deployment pins; runtime implementation alone is low-risk cosmetic
rendering. Review lanes: general, architecture, scope, risk; gpt-6-astra/xhigh.

No persisted formats, journal/state schema, APIs/protocols, cluster contract,
authority policy, Codex version or NixOS host behavior changes. Old/new bundles
consume the same payload. No supported state migration or mixed-version hazard
is introduced by the change. Planned authorized deployment uses stable
`workspace-host switch --source <workspace-worktree>` and keeps the preceding
profile for ordinary rollback. No session lifecycle action is authorized.
Do not mutate or interrupt other sessions to bypass an activation refusal.

The local workspace operator is trusted to administer the host. Root/user
ownership expresses operational responsibility; remote clients and guest
projects remain untrusted. Preserve normal validation/authentication and
credential handling. No change attempts to harden against a compromised operator.

## Review instructions

Perform your assigned lane directly with the mandatory-change-review skill.
Do not edit implementation or launch nested agents. Write concise findings,
severity, exact file/commit references and residual test gaps to the assigned
review artifact under the active tracking directory, and send a summary.
