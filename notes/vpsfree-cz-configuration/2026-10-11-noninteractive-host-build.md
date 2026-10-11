# Noninteractive confctl build

`confctl build` asks for confirmation even when one exact machine is selected.
An already authorized build launched through a watcher or transient service
needs `confctl build --yes MACHINE`; otherwise it ends with EOF at the prompt.
`confctl build --help` confirms this command option. Deploy commands similarly
accept `--yes`. Preserve the failed log before retrying.

Related initiative: work/2026-10-11-cluster-controls/.
