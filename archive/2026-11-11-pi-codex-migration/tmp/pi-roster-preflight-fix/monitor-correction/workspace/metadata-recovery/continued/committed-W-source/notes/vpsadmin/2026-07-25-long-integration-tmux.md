# Run long vpsAdmin integration tests in retained tmux panes

Related initiative: `work/2026-06-15-vpsadmin-events`.

## Symptom

Running
`./test-runner.sh test alerts/oom-report-group-and-prune` directly through the
command tool received SIGTERM at five minutes while the two-VM scenario was
still starting. The runner had reported zero unexpected failures and had not
completed an example.

## Cause

The command wrapper's execution ceiling was shorter than the normal
approximately 8-12 minute VM scenario. This was not a test-runner or
application timeout.

## Workaround

Start the exact test command in a dedicated tmux session, enable
`remain-on-exit`, and monitor it with `tmux capture-pane` and
`tmux list-panes`. The retained pane exposes both the complete output and
`pane_dead_status` after the command exits. Stop unrelated dev-cluster VMs
first when practical to reduce resource contention.

The rerun reached both examples and produced a complete result plus preserved
test-state directory, which allowed an unrelated test-fixture failure to be
diagnosed from full evidence.
