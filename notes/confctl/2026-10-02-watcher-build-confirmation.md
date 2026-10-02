# Noninteractive configuration builds need --yes

A fresh verification watcher running
`nix develop -c confctl build cz.vpsfree/machines/aitherdev` selected the correct
single machine, then stopped with `Continue? [y/N]:` and `end of file reached`.
The build had not started; the watcher had no interactive input terminal.

The selected confctl's `help build` documents the command option `--yes`.
For an already authorized build, use
`nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev`.
`--no-interactive` is not a build option; inspect each command's own help rather
than carrying deployment flags into builds. Preserve the failed log and run the
corrected command through a fresh watcher. No source or deployment scope changes
are needed.

Related initiative: `work/2026-10-02-portal-creation-performance/`.
