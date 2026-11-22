# Use CodeMirror presentation cleanup for visible character differences

Portal commit `1741603` retained correct Git line ranges but replaced
`Chunk.build` with raw `@codemirror/merge.diff`, losing the `presentableDiff`
cleanup that `Chunk.build` calls internally. Raw character matches across
replacement blocks leave scattered unmarked letters inside words, comments
and indentation, even for unrelated code. Both layouts share this behavior.

The locked merge 6.12.2 already exports `presentableDiff`. In the reported
comparison it reduced a 27-range replacement to one range without changing
Git line classification. The repair is implemented in runtime `5d853b6` and deployed on aitherdev
as profile generation 46. Live Chromium verification passed in both layouts.
Cleanup remains a heuristic, so heavily rewritten blocks may merit suppressing
character emphasis. Existing tests checked range bounds and line identities,
but not readable segmentation.

Verified with the immutable live payload, 100 repeat runs and a rebuilt bundle
identical to the deployed asset. See
`work/2026-09-15-portal-diff-highlighting/diagnosis.md`.
