# Frozen server bundle setup: first-step stop

The setup stopped because the session script placed `--norc` **before** the
`install` subcommand. I introduced this invocation error in the prepared plan.
The selected RubyGems supports the option on individual commands; no new tool,
source or dependency change is needed.

Actual failed command: `gem --norc install --no-document bundler --version 4.0.23`.
`01-bundler-install.log` reports `Invalid option: --norc`; exit1 in0.162seconds.
The full setup exited1/37.216seconds. Watcher CLI0 only completed its report.
Effective own turn_context proves Luna/low/never/danger-full-access.

Read-only installed-source evidence: `rubygems/command_manager.rb` lines178–195
reject any first `-` argument other than the listed global options; its branch
produces this exact error before invoking InstallCommand. `command.rb` lines621
onward declares `--norc` as a common **command** option. `config_file.rb` checks
for it when deciding whether to merge rc configuration. The correct narrow argv
is therefore:

```sh
gem install --norc --no-document bundler --version 4.0.23
```

This is source-derived, not a new probe/retry. Full exact paths/hashes and
selected Ruby/tool identities are in [diagnosis.json](diagnosis.json).

Effects: own ignored `.gems`, `.bundle/postreview-user` and
`.bundle/postreview-server` are present, empty and nonsymlink. Own server lock
matches retained SHAcec5e86c703239afa8c5914111ec3773ac7b8b485fc8e33cba80872cc51959b5.
No gem was downloaded/installed and no native extension compilation began. The
shell itself realized only its lightweight haveapi-env derivation and two cache
Bash substitutions. Frozen install, bundle check, library activation and every
test/listener/docs/package step were **unreached**. All765tracked inputs,
exact4dc0f7e/treea5c78fa and root450de/Rust7f51 locks are unchanged. No owned
command remains. No source/Git/config change, retry or cleanup was performed.

Proposed separately granted recovery: one fresh policy watcher, new evidence
folder, unchanged exact source/lock/Ruby/platform guards and environment. Assert
recorded own directories still empty, ignored and nonsymlink and serverlock exact;
reuse them without cleanup/recreation/recopy. Move only `--norc` after `install`,
then retain the unchanged frozen install, check and activation/native-path
assertions. Stop on any unexpected destination/source/tool drift. Keep
NIX_ENFORCE_PURITY=0 scoped to frozen installation only. No fallback resolution,
tests/listeners or long campaign. Preserve original script/result/logs verbatim.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
