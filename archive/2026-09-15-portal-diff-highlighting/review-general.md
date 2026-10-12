# General review

## Findings

No Blocking or Important findings in the committed product changes.

- **Advisory G1 — reconcile historical investigation wording.** The active
  [state.md](state.md:35) still says no fix is implemented, its
  [next action](state.md:39) repeats completed implementation work, and
  [repository status](state.md:48) says no branches or pushes exist. These
  contradict the current head table. [diagnosis.md](diagnosis.md:124) and its
  concluding scope also describe the investigation's former implementation
  status without a clear historical label. Mark those statements as historical
  or replace them with current status before handoff, so resumption does not
  repeat completed work. This concerns working-tree tracking records, not an
  additional product commit. The coordinator acknowledged the cleanup.

## Reviewed ranges and assessment

| Repository | Base | Head |
| --- | --- | --- |
| dev-workspace | `9a1b16464e45d722110b448a79315a0f3ce134aa` | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` |
| vpsfree-dev-workspace | `c6afe2905506fba0b8e372e0436b570f5597f8bd` | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` |
| workspace | `259c0c3fe7d4f3d454f8b27172cb7a8f99ca79be` | `80b93a8c6b120ce178b4a6479901fde12156e3d5` |

Reviewed directly using the general lane, gpt-6-astra/xhigh; no nested agents.
Read all three local AGENTS.md files, the packet, plan/state/diagnosis, runtime
README and portal guide, extension README, and relevant packaging code.

The runtime commit has one logical purpose, with supporting comment and
regressions. Each downstream pin is a separate commit and selects the reviewed
upstream head. The lock diffs contain no unrelated dependency changes. Commit
messages describe the final behavior and compatibility impact.

`dev-workspace/portal/review-ui/editor-model.js:1` selects the already locked
CodeMirror 6.12.2 presentation function with the same arguments and result shape.
Inspection of its installed implementation confirms it wraps the existing
bounded diff with cosmetic cleanup. The call at line 91 still sees one Git
replacement block; clipping at lines 70–72 confines marks to individual source
rows. Line classification, source contents, links, syntax tokens and renderer
decorations are unchanged. The adjacent comment adequately records the reason
for this small repair; no public contract or operator procedure needs revision.

The regressions at `dev-workspace/portal/review-ui/editor.test.mjs:82` cover both
layouts, whole identifier replacements, and the reported unrelated multiline
replacement pattern. Existing tests retain exact Git counts, source identity,
unusual text, invalid-range rejection and source-position coverage.

## Verification and remaining gaps

- Independently ran `nix shell nixpkgs#nodejs -c npm test` in the runtime review
  UI: **13/13 pass**. Runtime `git diff --check` passes.
- The updated state records successful no-build flake checks for all three
  heads. Those checks establish evaluation, not consumer package execution.
- Package builds, remaining CI, served-bundle identity and browser acceptance
  on the complete saved comparison remain for the planned post-review phase.
  This review does not claim deployment or browser verification.
- Presentation remains heuristic: the accepted residual punctuation and
  indentation matches can remain in other rewrites. The tests establish the
  repaired cases and source invariants, not universal semantic line matching.
