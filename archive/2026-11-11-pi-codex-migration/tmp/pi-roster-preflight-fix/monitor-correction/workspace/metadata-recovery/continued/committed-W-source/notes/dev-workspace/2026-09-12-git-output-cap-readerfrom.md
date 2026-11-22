# Go subprocess output caps and promoted ReadFrom

While adding bounded local Git review, a focused test ran `git log --all` with a
one-byte output cap and unexpectedly succeeded. The output writer embedded
`bytes.Buffer` and overrode `Write`, but embedding also promoted `ReadFrom`.
`os/exec` copies subprocess output with `io.Copy`, which selected `ReadFrom` and
bypassed the capped `Write` method.

Use a named `buffer bytes.Buffer` field rather than embedding it. Expose only the
intended writer methods; cancel the command as soon as the cap is exceeded.
`TestReviewRejectsWrongBranchAndBoundsGit` verifies an actual Git process fails
with the output-limit sentinel and checks command deadlines. The focused review
suite passes after the fix.

Initiative: `work/2026-09-12-portal-review-experience/`.
