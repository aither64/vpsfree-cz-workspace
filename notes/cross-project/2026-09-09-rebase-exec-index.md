# Rebase exec steps must finish with a clean index

During work/2026-09-09-ip-release-mechanism, a history split used consecutive
rebase todo `exec` lines for applying a staged patch and committing it. Git
stopped after the first line because rebase exec requires a clean index before
continuing; it never reached the commit line.

Make patch application and its commit one exec operation/script. To recover an
already stopped rebase, inspect and commit the intended staged patch with hooks,
remove the now-redundant commit exec from `git rebase --edit-todo`, and continue.
The initiative's final tree was verified identical to its pre-split tree, with
the prerequisite separated from the additive feature. Do not reset shared work.
