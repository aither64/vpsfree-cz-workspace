# CI reruns can skip tests after a message-only rewrite

## Symptom

Rerunning a failed GitHub Actions integration job after a message-only branch
rewrite can finish green in seconds without executing any integration tests.

## Cause

The rerun retains the original push event's `before` revision but checks out the
current rewritten head. When those revisions have identical trees, changed-file
selection reports `mode=skip` and `reason=no changed files`.

## Workaround

Inspect the rerun's test-selection output before treating it as validation. A
green skipped rerun does not supersede the original test result. Trigger a new
push or an explicit full workflow dispatch when a real rerun is required.

## Verification

Attempt 2 of run `32652787707` completed in 11 seconds with every integration
step skipped after the vpsAdmin subject-only rewrite. The original 116/118
result remained the applicable evidence for
`work/2026-08-23-vpsadmin-supervisor-issue/`.
