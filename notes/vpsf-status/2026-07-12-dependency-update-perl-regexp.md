# Scheduled dependency update fails after module update

## Symptom

GitHub Actions run `29182284517` (`Update dependencies`) failed on vpsf-status
master at `3eb6fd86a` after `go get -u` updated several modules.

## Cause

The update step then reported `Unknown regexp modifier "/R"` and `Can't find
string terminator '"' anywhere before EOF` from Perl, exiting with status 255.
The dependency resolution itself completed before the malformed regexp/string
in the workflow script failed.

## Handling

The failure predates and is unrelated to probe-log capitalization. Exact-SHA
i18n and integration workflows for `9c19b23` passed on both the feature branch
and merged master. Investigate and repair the updater's Perl quoting before
accepting a future dependency update; rerunning this failed attempt alone is
not evidence of correctness.

Related initiative: `work/2026-07-10-czech-translation-fixes/`.
