# Quote backticks in shell search patterns

## Symptom

An `rg` pattern containing a Markdown-formatted workflow ID was passed inside
double quotes. Bash treated the backticks as command substitution and printed
`command not found`, although the subsequent search still completed.

## Cause

Backticks remain active inside double-quoted shell arguments.

## Workaround

Pass search patterns containing literal backticks in single quotes, or avoid
including the backticks when they are not needed by the search.

## Verification

The initiative archive contains both expected files, and searching for the
plain workflow ID finds the recorded status without shell substitution.

Related initiative: `archive/2026-09-01-tf-dep-update/`.
