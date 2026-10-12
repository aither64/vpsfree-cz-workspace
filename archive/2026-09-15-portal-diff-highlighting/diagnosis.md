# Changed-character highlighting diagnosis

## Implementation status

The user accepted the diagnosis and authorized implementation and deployment.
Runtime commit `5d853b6b0c2608549a1f0e940c680ccb40a14bec` now uses the existing
`presentableDiff` and adds four readability regressions; all 13 editor tests pass.
The investigation below records the original behavior and experiment. Deployment
status and exact package chain are maintained in [state.md](state.md) and
[rollout.md](rollout.md).

## Investigation conclusion

The portal renders the raw character edit script from CodeMirror as visual
highlights. It lost CodeMirror's presentation cleanup when the portal changed
to Git-authoritative line ranges in commit
`17416030feaaa12517244f8593b53fc59843736c` on 2026-09-14.
The scattered red/green backgrounds in the supplied screenshot reproduce from
the exact saved comparison. They are deterministic character matches across
replacement blocks, including unrelated statements, comments and indentation.

## Exact reproduction

- Repository: `vpsfree-cz-configuration`.
- File: `configs/vpsadmin/api/abuse_notice_parser/master_dc.rb`.
- Base: `713fb3ba48ae31c87519e75892d1413a48a22fb0`.
- Head: `b6e650ad902482b4c4e66b5a89a4275bed92419e`.
- Review: `459a908f223e248f9e827131190441f8`.
- File ID: `a82b2be05b24ddefa6bdeb1ac4ba00dd`.
- Locked dependency: `@codemirror/merge` 6.12.2.
- Active package: `/nix/store/kimxny34bbmdybfpj7v6mlz6z88zsk5k-dev-workspace-0.2.0`.
- Its source model is byte-identical to `origin/master` at
  `9a1b16464e45d722110b448a79315a0f3ce134aa`.

The saved review was read through the running portal's local Unix socket using
`GET /api/sessions/2026-09-15-abuse-uceprotect/repository-comparison` with the
repository, review and file IDs from the supplied URL. Both returned sources
match their exact Git objects. All 31 returned change blocks match an independent
Git Myers diff with indentation heuristics and zero context. Line totals are
correct: **206 additions, 75 deletions**.

The existing `unifiedProjection` and `splitProjection` were run against that
payload in an isolated temporary copy with the locked npm dependencies.
The input screenshot, source payload, dependency directory and generated bundles
remain outside version control.

## Why the highlights look arbitrary

`portal/review-ui/editor-model.js:1` imports `diff as characterDiff`.
At lines 84–92, the model joins all removed lines in a Git change block into one
string and all added lines into another. It computes a raw character diff across
those strings. It does not first pair corresponding source lines or require
meaningful similarity. `push` clips those offsets back to individual display
rows. `portal/review-ui/editor.js:99` turns them directly into brighter
`review-added-text` / `review-deleted-text` backgrounds.

Consequently an unchanged character means only that the matcher found that
character somewhere in order in the opposing block. It can be inside an entirely
different word, on a different line, or in a comment. These matches do not
indicate that the word, statement or indentation is unchanged.

For example, old line 106 is compared with new lines 112–114. Brackets below
represent brighter deleted-character backgrounds:

```text
[r]et[u]rn [] if [ad]d[r]_s[tr].nil? [||] ti[m]e[.]nil[?]
```

The `r` and `u` in `return` are marked while its other letters are matched
elsewhere in the three new lines. The old CSV parser at lines 111–117 is compared
with the new incident processing at 122–127, producing 53 small edit ranges.
The new explanatory comments at 117–118 are compared against an old
`create_incident(...)` call and `end`, explaining their equally fragmented marks.

Syntax foreground colors come independently from Shiki tokens. The confusing
background ranges already exist before Shiki or browser rendering runs.
Both layouts receive identical character markings for each source line.

## Regression and existing library support

Before commit `1741603`, the model used `Chunk.build(...)`. The locked CodeMirror
implementation calls `presentableDiff(...)` from `Chunk.build`. The new direct
call to `diff(...)` bypasses that cleanup.

The dependency's `presentableDiff` merges short unchanged gaps and expands
suitable changes towards word boundaries. See the local locked package's
`dist/index.js:349–410,489–508,649–651` and
[upstream implementation](https://github.com/codemirror/merge/blob/main/src/diff.ts).
No dependency upgrade is needed to use it.

A temporary experiment, without modifying project code, produced:

| Old lines → new lines | Raw edit ranges | Presentable edit ranges |
| --- | ---: | ---: |
| 106 → 112–114 | 27 | 1 |
| 108–109 → 116–120 | 34 | 2 |
| 111–117 → 122–127 | 53 | 7 |
| 119–122 → 129–133 | 33 | 6 |
| 124–125 → 135–138 | 11 | 3 |

A small independent example makes the difference clear:

```text
Before source: old_name = 123
After source:  new_value = true

Raw before:   [old]_[n]a[m]e = [123]
Raw after:    [new]_[v]a[lu]e = [true]

Presentable before: [old_name] = [123]
Presentable after:  [new_value] = [true]
```

The full reported projection produced identical ranges in 100 runs. The slowest
was about 34 ms in this environment. Removing the configured scan/time limits
also produced the same raw ranges for the three checked replacement blocks
(old starts 105, 110 and 118). There is no evidence that a timeout causes the
reported pattern; this does not exclude timeout fallback on other inputs.

## Recommended repair

The smallest repair is to use the existing `presentableDiff` for cosmetic
within-block marks, retaining Git as the authority for added/deleted lines.
This restores the cleanup lost in the regression, requires no API or state
migration, and preserves the existing line-count correction.

Presentation cleanup is still a text-matching heuristic: the experiment retains
some common punctuation and indentation inside heavily rewritten blocks.
If those remaining marks are distracting, suppress character emphasis for
blocks without a credible line correspondence and use the ordinary whole-line
addition/deletion colors there. Pairing similar lines before character comparison
is a broader alternative, to consider only if the smaller repair is insufficient.
The presentation-cleanup repair is implemented. Additional suppression or line
pairing remains an optional broader change, outside the accepted fix.

A fix should include focused expectations for split identifiers, unrelated
multiline replacements, and agreement between layouts, while retaining the
existing exact-Git line count and source/link invariants.

## Verification of deployed asset and existing tests

Rebuilding the unmodified source with its locked dependencies produced the exact
editor bundle served by the running portal (SHA-256
`37b267ca20ae07b9542741da96bf69326d530e93b157b2079a9b55b2ed320909`).
After `npm run build`, all nine existing editor tests passed. An initial run
before building had eight passes and one missing `dist/review-build.json`
fixture error; this was test setup, not a product failure.

## Coverage gap and scope

The existing projection tests verify line identity, counts, context and bounds
of mark offsets. They do not assert readable changed-character segmentation.
The original model therefore passes those semantic tests despite this defect.

The initial investigation changed no application files or source-session
records and did not run browser or deployment tests. Its evidence was the supplied
screenshot, deployed package/source, immutable live API payload, exact Git objects
and direct model execution. The authorized implementation and subsequent
acceptance results are recorded separately in state.md and rollout.md.
