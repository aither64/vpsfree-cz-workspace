# Empty saved discovery after reboot can be a provider filter

`dev-session resume` reported `retained recovery identity or submissions cannot
be verified` after reboot. The private `workspace-portal session observe` command
verified all retained subjects but returned `retained_set_unverified`. The
read-only team archive preflight exposed the underlying error: `a retained active
conversation is absent from archive discovery`.

The native `thread/list` query defaults to the server's model provider. Retained
threads belonged to `codex-lb`; the default query returned zero rows, while the
same query with `modelProviders: []` returned all eight expected identities.
Loaded-thread discovery was empty after reboot and could no longer mask the
omission. This was not missing history or corrupt submission evidence.

The fix adds `ThreadListOptions.ModelProviders` in codex-web and selects an empty
non-nil slice in dev-workspace's exact retained-set discovery. Nil deliberately
preserves the native default for other callers. Preserve the distinction between
an omitted field, JSON null and an empty array. Do not load threads or relax
retained identity/submission checks to make a recovery observation succeed.

The wire regression reproduces the original error without the explicit filter
and passes with it, including pagination and rejection of unknown extra threads.
Deployment and final verification evidence is in
`work/2026-10-30-reboot-recovery-fix/state.md` and its linked records.
