# Use the exact full revision for a confctl feature pin

Related initiative: `work/2026-09-03-dev-session-portal`

`confctl inputs channel set --commit` passed an invented expansion of an
abbreviated Git SHA to the GitHub flake input. Nix returned HTTP 404 while
fetching the nonexistent revision, before it changed or committed the lock
file.

Read the exact revision from the source repository before pinning it:

```sh
revision=$(git rev-parse HEAD)
confctl inputs channel set --commit CHANNEL ROLE "$revision"
```

The portal initiative repeated the command with the exact 40-character
revision. Confctl then updated and committed the input successfully.
