# Exclude deleted migration specs from changed-file CI selection

Related initiative: `work/2026-07-20-kernel-boot-evidence-history/`.

## Symptom

GitHub Actions run `29752208265` failed before running examples because the
migration workflow passed both the final migration spec and its deleted
pre-rename path to RSpec. Rerunning could not fix the deterministic selection.

## Cause

`git diff --name-only` includes deleted paths by default. The workflow selected
changed files by pathname but did not restrict diff statuses, so rewriting an
unmerged migration/spec name left a nonexistent RSpec argument.

## Fix

Select paths with:

```shell
git diff --name-only --diff-filter=ACMRTUXB BASE...HEAD
```

This retains added, copied, modified, renamed, type-changed, unmerged and
unknown paths while excluding deletions. Verify the selected list locally and
keep the repository's migration/spec mapping check as a separate guard.

The failed attempt's logs were inspected before the fix. The final-head
migration workflow passed after the selector change.
