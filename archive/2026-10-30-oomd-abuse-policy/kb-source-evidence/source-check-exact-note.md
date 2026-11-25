# Exact source checker execution

Exact command: `nix develop -c bin/check --allow-missing` from the dedicated
KB worktree; log `source-check-exact.log`. Started after the separate utility
invocation rejected a trailing argument before checker execution. Failed
utility evidence remains `source-check.log` + `source-check-result.json` and
must not be treated as a source failure.

The normal source batch includes source/semantic tests and a runtime-plan
projection test; that test evaluates synthetic configurations and inspects
writeText derivations, without constructing application packages or guests.
The transient source-shell setup is296.5MiB unpacked dependencies+5small
Ruby/wrapper derivations. This is not full-runtime capacity admission.
No new custom monitor scaffolding or checker source edits were introduced.
