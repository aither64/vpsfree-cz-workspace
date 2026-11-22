# Isolating portal source checks on a configured host

When running dev-workspace Go tests on a host with a real provider catalog,
set DEV_WORKSPACES_CODEX_PROVIDERS to an absent file in an owned disposable
directory. Unsetting it falls back to /etc/dev-workspaces/codex-providers.json;
unnamed test workspaces then fail with “invalid workspace provider state identity”.
The tests must not consume the host's live provider configuration.

Nix development shells also select a longer TMPDIR. Recovery tests whose Go
testing.TempDir names include long test names can exceed Unix socket pathname
limits and fail with “listen unix .../codex.sock: bind: invalid argument”.
Set TMPDIR=/tmp for the test command after entering the Nix shell. Go still
creates and cleans its unique test directories.

Example, from the dev-workspace checkout, with an absent task-owned catalog path:

```sh
nix develop --command env \
  DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/owned-test-directory/absent.json \
  TMPDIR=/tmp bash -c 'cd portal && go test -mod=readonly ./...'
```

The full portal Go suite passed with this isolation during
work/2026-10-18-portal-message-recovery. The initial host-catalog and socket-path
failures, commands and results are retained in that initiative.
