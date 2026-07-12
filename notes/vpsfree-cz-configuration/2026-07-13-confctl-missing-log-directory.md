# confctl input listing needs its log directory

- Initiative: `work/2026-07-10-czech-translation-fixes`
- Command: `nix develop -c confctl inputs channel ls`
- Symptom: in a fresh worktree, confctl printed the channel table but also
  reported `No such file or directory` for its file under `.confctl/logs/`.
- Cause: the fresh worktree had no `.confctl/logs` cache directory; input
  listing did not create it before opening the log.
- Workaround: run `mkdir -p .confctl/logs` before the confctl command.
- Verification: rerunning the command exited cleanly and reported
  `vpsadminServices` at `9a5fccf4`.
