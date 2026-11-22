# `vpsadmin-api-ruby` loads maintenance scripts

## Symptom

An executable maintenance script with a `$PROGRAM_NAME == __FILE__` guard exits
without running its command-line entry point.

## Cause

`vpsadmin-api-ruby` starts `vpsadmin-api-ruby-runner`, which removes the script
path from `ARGV` and calls `load script`. `$PROGRAM_NAME` therefore identifies
the runner, while `__FILE__` identifies the loaded maintenance script.

## Fix

Maintenance scripts using the `vpsadmin-api-ruby` shebang are standalone
programs. Put their command-line entry point at top level without a conventional
direct-execution guard. Derive usage text from `File.basename(__FILE__)` rather
than `$PROGRAM_NAME`.

## Verification

A load-based invocation of the repaired IP charging-environment task executes
its option parser and prints the script name. Related initiative:
`archive/2026-09-07-fix-ip-charged-environments`.
